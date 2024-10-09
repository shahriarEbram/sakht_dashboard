def manager_page_tasks(username):
    from cons import work_shift, unit_name, categories
    from database import fetch_users, update_sakht_table  # Use functions for stoppage
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
    df_manager = fetch_users(username)
    # df_manager = df_manager.drop(columns=['id'])
    # Show the data editor with the fetched stoppage data
    edited_df_manager = st.data_editor(
        df_manager,
        hide_index=True,
        use_container_width=True,
        column_order=["person_name", "unit", "shift", "operation", "machine",
                      "product", "work_type", "project_code", "date",
                      "operation_duration", "announced_duration", "done_duration"
                      ],
        column_config={
            "unit": st.column_config.SelectboxColumn(
                options=unit_name,
                required=True,
            ),
            "shift": st.column_config.SelectboxColumn(
                options=work_shift,
                required=True,
            ),
            "operation": st.column_config.SelectboxColumn(
                options=list(categories.keys()),
                required=True,
            ),

        }
    )

    # Add a button to save changes
    if st.button("Save Changes", key="manager_tasks_sub"):
        if not edited_df_manager.equals(df_manager):
            try:
                # Update the stoppage data in the database
                update_sakht_table(edited_df_manager)
                st.success("تغییرات با موفقیت اعمال شد.")
            except Exception as e:
                st.error(f"خطای: {e}")
        else:
            st.warning("تغییری اعمال نشد.")
