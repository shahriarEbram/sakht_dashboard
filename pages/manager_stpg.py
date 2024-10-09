def manager_page_stoppage(username):
    from cons import work_shift, unit_name, categories
    from database import fetch_all_stoppage  # Use functions for stoppage
    import streamlit as st
    import cons

    # Apply RTL and Persian font
    st.markdown("""
        <style>
        @import url('https://v1.fontapi.ir/css/Vazir');
        body {
            direction: rtl;
            font-family: 'Vazir', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True)

    # Fetch stoppage data from the database
    df_manager = fetch_all_stoppage()
    # df_manager = df_manager.drop(columns=['id'])
    # Show the data editor with the fetched stoppage data
    # machines = []
    # for machine in categories.keys():
    #     machines.append(machine)
    # print(machines)
    edited_df_manager = st.data_editor(
        df_manager,
        hide_index=True,
        use_container_width=True,
        disabled=["stpg_id", "person_name", "machine", "reason", "date", "stoppage_duration"],
        column_order=["person_name", "machine", "reason", "date", "stoppage_duration"],
    )

    # Add a button to save changes
    if st.button("Save Changes", key="manager_stoppage_sub"):
        if not edited_df_manager.equals(df_manager):
            try:
                # Update the stoppage data in the database
                # update_sakht_table(edited_df_manager)
                st.success("تغییرات با موفقیت اعمال شد.")
            except Exception as e:
                st.error(f"خطای: {e}")
        else:
            st.warning("تغییری اعمال نشد.")
