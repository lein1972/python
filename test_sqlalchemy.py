try:
    from sqlalchemy import create_engine
    print("SQLAlchemy import successful!")
except ImportError as e:
    print(f"Error importing SQLAlchemy: {e}")