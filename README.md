# shubhNewsLetter: Newsletter Web Application

shubhNewsLetter is a dynamic web application designed to allow users to sign up, log in, create, and subscribe to newsletters. 
Users can subscribe to newsletters of their choice, and they will receive the latest content directly in their inbox when new newsletters are posted by the publishers on the platform.

## Technologies Used

- **HTML5**
- **CSS3**
- **Jinja2**
- **Flask**
- **Python**
- **SQLite3**

## Features

- **User Authentication**: Users can securely sign up and log in to the platform.
- **Create Newsletters**: Authenticated users can create and manage their newsletters.
- **Subscribe to Newsletters**: Users can subscribe to newsletters and receive them via email when the publisher posts new content.
- **Responsive Design**: The front-end uses HTML5 and CSS3 to ensure the platform is user-friendly and accessible across devices.
- **Dynamic Content Rendering**: Jinja2 is used to dynamically render content for subscribers and publishers.
  
## Deployment

shubhNewsLetter can be deployed locally or on any hosting platform that supports Flask. The application stores data using SQLite3, providing a lightweight and easy-to-setup database.

## Usage

To run the application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/shubhnewsletter.git
   ```
2. **Install dependencies** using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the SQLite3 database**:
   - Ensure the database is properly configured in the Flask application (`app.py` or `web_app.py`).
4. **Run the application**:
   ```bash
   python app.py
   ```
5. **Access the application** in your web browser at:
   ```
   http://localhost:5000
   ```

## Key Functionalities

1. **Sign Up and Log In**: Users can create an account and log in to manage newsletters and subscriptions.
2. **Create Newsletters**: Logged-in users can create newsletters and post them on the platform.
3. **Subscription Management**: Users can subscribe to newsletters, and the system automatically sends new posts via email to the subscribers.
4. **Responsive UI**: The front-end is designed for mobile and desktop users, ensuring a seamless experience across devices.

## Contribution

Contributions are highly encouraged! To contribute:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -am 'Add some feature'`).
5. **Push to your branch** (`git push origin feature/your-feature`).
6. **Submit a Pull Request** and we’ll review your changes.

## Contact

For inquiries, suggestions, or feedback regarding shubhNewsLetter, feel free to contact me via [LinkedIn](https://linkedin.com/in/shubhamgurjar1).

