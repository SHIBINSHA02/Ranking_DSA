import subprocess
import sys

# ... existing code ...

if __name__ == "__main__":
    try:
        # Check if Streamlit is installed
        import streamlit
    except ImportError:
        print("Streamlit is not installed. Please install it using 'pip install streamlit'.")
        sys.exit(1)

    # Run the Streamlit app
    try:
        subprocess.run(["streamlit", "run", "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to run Streamlit: {e}")
        sys.exit(1)

# ... existing code ...