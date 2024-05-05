from app import create_app

# run_application()
if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(host='0.0.0.0', debug=True)
