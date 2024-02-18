from dev.app import create_app
from dev.configs import config

app = create_app(config=config.Config)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

