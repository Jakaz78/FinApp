from app import create_app
import os

app = create_app()
app.secret_key = os.getenv("SUPER_SECRET_KEY")
if __name__ == "__main__":
    app.run(debug=True)