from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Table, MetaData, select, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
import pandas as pd
from pathlib import Path
from cons import operator_workers
from sqlalchemy import desc

# Database setup
db_path = Path(__file__).parent / "data/sakht_dashboard.db"
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
metadata = MetaData()

# Define the table structure
sakht_table = Table(
    'sakht', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('task_date', String), # تاریخ به فرمت میلادی
    Column('person_name', String),
    Column('unit', String),
    Column('shift', String),
    Column('operation', String),
    Column('machine', String),
    Column('product', String),
    Column('work_type', String),
    Column('project_code', String),
    Column('date', String),  # تاریخ به فرمت شمسی
    Column('operation_duration', String),  # به صورت HH:MM
    Column('announced_duration', String),  # به صورت HH:MM
    Column('done_duration', String)  # به صورت HH:MM
)

stoppage_table = Table(
    'stoppage', metadata,
    Column('stpg_id', Integer, primary_key=True, autoincrement=True),
    Column('stpg_date', String),  # تاریخ به فرمت میلادی
    Column('person_name', String),
    Column('machine', String),
    Column('reason', String),
    Column('date', String),  # تاریخ به فرمت شمسی
    Column('stoppage_duration', String)  # به صورت HH:MM
)

# Create tables if they do not exist
metadata.create_all(engine)


# Context manager for handling sessions
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()


def fetch_users(username):
    staff_list = operator_workers.get(username)
    print(staff_list)
    if username == "damerchi" or username == "sohrabi":
        """Fetch tasks for a specific staff member."""
        with get_session() as session:
            query = select(sakht_table).order_by(desc(sakht_table.c.task_date))
            return pd.read_sql(query, con=engine)
    else:
        with get_session() as session:
            query = select(sakht_table).where(sakht_table.c.person_name.in_(staff_list))
            return pd.read_sql(query, con=engine)


def fetch_tasks(staff):
    """Fetch tasks for a specific staff member."""
    with get_session() as session:
        query = select(sakht_table).where(sakht_table.c.person_name == staff)
        return pd.read_sql(query, con=engine)


def insert_task(task_data):
    """Insert a new task into the database."""
    with get_session() as session:
        insert_stmt = sakht_table.insert().values(**task_data)
        session.execute(insert_stmt)


def delete_tasks(staff):
    """Delete tasks for a specific staff member and reset auto-increment if table is empty."""
    with get_session() as session:
        # Delete all tasks for the specific staff
        delete_stmt = sakht_table.delete().where(sakht_table.c.person_name == staff)
        session.execute(delete_stmt)

        # Check if the table is empty
        query = select(sakht_table).limit(1)
        result = session.execute(query).fetchall()

        # Reset the auto-increment sequence only if sqlite_sequence exists
        if not result:
            try:
                session.execute(text("DELETE FROM sqlite_sequence WHERE name='sakht'"))
                session.commit()
            except SQLAlchemyError as e:
                # Handle the case where sqlite_sequence doesn't exist
                if "sqlite_sequence" not in str(e):
                    raise e
                else:
                    print("sqlite_sequence table doesn't exist, skipping sequence reset.")


def update_tasks(df, staff):
    """Update tasks in the database for a specific staff member."""
    # Delete current user's records from the database
    delete_tasks(staff)

    # Ensure 'id' column is not included in the insertion
    df = df.drop(columns=['id'], errors='ignore')

    # Insert updated dataframe records into the database
    if not df.empty:
        with get_session() as session:
            df.to_sql('sakht', con=engine, if_exists='append', index=False)


def insert_stoppage(stpg_data):
    """Insert a new task into the database."""
    with get_session() as session:
        insert_stmt = stoppage_table.insert().values(**stpg_data)
        session.execute(insert_stmt)


# def fetch_stoppage(staff):
#     """Fetch tasks for a specific staff member."""
#     with get_session() as session:
#         query = select(stoppage_table).where(stoppage_table.c.person_name == staff)
#         return pd.read_sql(query, con=engine)

def delete_stoppage(staff):
    """Delete stoppage for a specific staff member and reset auto-increment if table is empty."""
    with get_session() as session:
        # Delete all stoppages for the specific staff
        delete_stmt = stoppage_table.delete().where(stoppage_table.c.person_name == staff)
        session.execute(delete_stmt)

        # Check if the table is empty
        query = select(stoppage_table).limit(1)
        result = session.execute(query).fetchall()

        # Reset the auto-increment sequence if the table is empty
        if not result:
            try:
                session.execute(text("DELETE FROM sqlite_sequence WHERE name='stoppage'"))
            except SQLAlchemyError as e:
                # Handle the case where sqlite_sequence doesn't exist
                if "sqlite_sequence" not in str(e):
                    raise e
                else:
                    print("sqlite_sequence table doesn't exist, skipping sequence reset.")


def update_stoppage(df, staff):
    """Update tasks in the database for a specific staff member."""
    # Delete current user's records from the database
    delete_stoppage(staff)

    # Ensure 'id' column is not included in the insertion
    df = df.drop(columns=['stpg_id'], errors='ignore')

    # Insert updated dataframe records into the database
    if not df.empty:
        with get_session() as session:
            df.to_sql('stoppage', con=engine, if_exists='append', index=False)


def update_user_data(edited_df):
    """Update the user data in the database."""
    with get_session() as session:
        # Assuming 'users' is the name of the table to be updated
        session.execute('DELETE FROM users')  # Clear the current data

        # Insert the updated data
        edited_df.to_sql('users', con=engine, if_exists='append', index=False)
        session.commit()


def fetch_stoppage(staff):
    """Fetch stoppages for a specific staff member and sort by date in ascending order."""
    with get_session() as session:
        query = select(stoppage_table).where(stoppage_table.c.person_name == staff).order_by(stoppage_table.c.stpg_date)
        return pd.read_sql(query, con=engine)



def fetch_all_stoppage():
    """Fetch stoppages for a specific staff member."""
    with get_session() as session:
        query = select(stoppage_table).order_by(stoppage_table.c.stpg_date)
        return pd.read_sql(query, con=engine)


def update_sakht_table(df):
    """
    Function to update sakht_table data in the database.
    This will delete current records and insert updated records.
    """
    from sqlalchemy import delete

    # Step 1: Delete current records from the sakht table
    with get_session() as session:
        delete_query = delete(sakht_table)
        session.execute(delete_query)
        session.commit()

    # Step 2: Insert updated data
    if not df.empty:
        edited_df = df.drop(columns=['id'], errors='ignore')  # Ignore 'id' if it exists
        edited_df.to_sql('sakht', con=engine, if_exists='append', index=False)
