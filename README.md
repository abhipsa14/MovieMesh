🎬 MovieMesh
Movie Recommender
<img width="1178" height="576" alt="image" src="https://github.com/user-attachments/assets/ce6ca250-ae63-43d6-a25b-cc9e04d037c0" />

A simple Python utility that fetches movie posters using TMDB (The Movie Database) API with a movie ID. It's designed to be integrated into movie recommendation systems or any application requiring visual movie media.

This utility is helpful for building movie recommendation systems, displaying movie posters in your app, or integrating visual media into your projects.

📌 Features
🔍 Fetches high-resolution movie posters from TMDB by movie ID.

💥 Handles missing posters and API/network failures gracefully, returning a placeholder.

🔐 Uses environment variables for API key to keep it secure.

🖼️ Returns a placeholder image if the poster is unavailable.

🚀 Integrates with Streamlit for a simple web-based movie recommendation interface.

🧰 Tech Stack
Python 3

requests (for making HTTP requests to the TMDB API)

pandas (for data manipulation, especially with movie dataframes)

streamlit (for building the web application interface)

pickle (for loading pre-trained model and data)

python-dotenv (recommended for environment variable loading, although os.getenv is used directly)

TMDB API

🛠️ Installation & Setup
Follow these steps to get MovieMesh up and running on your local machine.

Clone the repository

git clone https://github.com/your-username/MovieMesh.git # Replace with your actual repo URL
cd MovieMesh

Install Required Packages
It's recommended to use a virtual environment.

# Create a virtual environment
python -m venv venv
# Activate the virtual environment
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

If you don't have a requirements.txt file, you can create one with:

streamlit
pandas
requests
scikit-learn # Assuming similarity matrix is from here

Get Your TMDB API Key

Go to The Movie Database (TMDb) website.

Sign up for an account or log in.

Navigate to your account settings and then to the API section.

Request a new API key (Developer or Personal use). You will need an "API Key (v3 auth)".

Set Up Environment Variable for API Key
To keep your API key secure and out of your code, it's best to store it as an environment variable.

Create a file named .env in the root directory of your project (where app.py or your main script is located).

Add the following line to the .env file, replacing YOUR_TMDB_API_KEY with the actual key you obtained from TMDb:

TMBD_API_KEY=YOUR_TMDB_API_KEY

Ensure your Python script loads this environment variable. If you're using python-dotenv, you'd typically add from dotenv import load_dotenv; load_dotenv() at the top of your script. If you're relying solely on os.getenv(), make sure the environment variable is set in your system's environment before running the app.

Prepare Data Files
This project relies on pre-processed data files:

movie.dict.pkl: A pickled dictionary containing movie data (e.g., movie IDs and titles).

similarity.pkl: A pickled similarity matrix (e.g., cosine similarity) used for recommendations.
Place these files in the same directory as your main Streamlit application script.

▶️ Running the Application
Once you have completed the installation and setup steps, you can run the Streamlit application:

streamlit run your_main_script_name.py # e.g., streamlit run app.py

This command will open the MovieMesh application in your default web browser.

💡 Usage
The fetch_poster function is a core utility:

from your_module import fetch_poster # Assuming it's in a module

movie_id = 550 # Example movie ID (Fight Club)
api_key = os.getenv('TMBD_API_KEY')

if api_key:
    poster_url = fetch_poster(movie_id, api_key)
    print(f"Poster URL: {poster_url}")
else:
    print("TMBD_API_KEY not set in environment variables.")

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
