def stoppage_page(username):
    import streamlit as st
    from cons import operator_machine_group, employee_names, stoppage_list, categories, employee_names
    import jdatetime
    from database import insert_stoppage, fetch_stoppage, update_stoppage
    import pandas as pd
    from datetime import datetime
    toady_milady = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    def miladi_to_shamsi(date):
        return jdatetime.date.fromgregorian(date=date)

    today_shamsi = miladi_to_shamsi(jdatetime.datetime.now().togregorian())

    # اعمال تنظیمات راست به چپ برای بدنه و فونت فارسی
    st.markdown("""
        <style>
        @import url('https://v1.fontapi.ir/css/Vazir');
        body {
            direction: rtl;
            font-family: 'Vazir', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True)

    staff = employee_names.get(username)
    if username in operator_machine_group:
        # with st.expander(f"{staff} خوش آمدید!"):
        #     authenticator.logout("خروج از حساب کاربری", "main")

        # Get all machines for the operator
        machine_groups_for_operator = operator_machine_group[username]
        machines = []

        # Combine all machines from different groups
        for group in machine_groups_for_operator:
            machines.extend(categories[group])
        df_key = f"df_stoppage_{username}"
        # *** Dataframe Setting *** #
        if df_key not in st.session_state:
            # Fetch data from the database

            df = fetch_stoppage(staff)

            if df.empty:
                df = pd.DataFrame(columns=[
                    'person_name',
                    'machine',
                    'reason',
                    'date',
                    'stoppage_duration',
                    'stpg_date'
                ])

            # df['task_name'] = df['task_name'].astype(pd.CategoricalDtype(cons.task_name.values()))
            st.session_state[df_key] = df
        with st.form(key="stoppage_form", clear_on_submit=False):
            col1, col2 = st.columns(2)
            with col1:
                # Display all machines for the operator
                selected_machine = st.selectbox("دستگاه مورد نظر را انتخاب کنید:", machines)
            with col2:
                # Select stoppage type
                stoppage_reason = st.selectbox("علت توقف را وارد کنید:", stoppage_list)

            with st.container():
                st.write("تاریخ توقف")
                col3, col4, col5 = st.columns(3)
                with col3:
                    day = st.number_input('روز', min_value=1, max_value=31, value=today_shamsi.day)
                with col4:
                    month = st.number_input('ماه', min_value=1, max_value=12, value=today_shamsi.month, disabled=True)
                with col5:
                    year = st.number_input('سال', min_value=1300, max_value=1500, value=today_shamsi.year,
                                           disabled=True)
                # تبدیل تاریخ شمسی به رشته با فرمت 1403-6-31
                task_date = f"{year}-{month}-{day}"

            st.write("مدت زمان توقف")
            stp_hour = st.number_input('ساعت', min_value=0, max_value=24, key="stop_du_h")
            stp_minute = st.number_input('دقیقه', min_value=0, max_value=60, key="stop_du_m")
            stp_duration = f"{stp_hour:02d}:{stp_minute:02d}"
            submitted_stoppage = st.form_submit_button("ثبت")

            # بررسی اینکه هیچ یک از فیلدها خالی نباشد
            if submitted_stoppage:
                new_row = {
                    'person_name': staff,
                    'machine': selected_machine,
                    'reason': stoppage_reason,
                    'date': task_date,
                    'stoppage_duration': stp_duration,
                    'stpg_date': toady_milady
                }
                insert_stoppage(new_row)
                # Update session state
                st.session_state[df_key] = pd.concat([pd.DataFrame([new_row]), st.session_state[df_key]],
                                                     ignore_index=True)

                st.toast("Submitted!")
        stoppage_df = st.data_editor(st.session_state[df_key],
                                     disabled=['person_name',
                                               'machine',
                                               'reason',
                                               'date',
                                               'stoppage_duration'],

                                     column_order=['person_name', 'machine', 'reason', 'date', 'stoppage_duration'],

                                     key="stoppage_df",
                                     use_container_width=True,
                                     num_rows="dynamic",
                                     hide_index=True,
                                     )

        # فیلتر کردن سطرهای خالی اضافه شده
        stoppage_filtered_df = stoppage_df.dropna(how='all')
        update_stoppage(stoppage_filtered_df, staff)
        st.session_state[df_key] = stoppage_filtered_df
