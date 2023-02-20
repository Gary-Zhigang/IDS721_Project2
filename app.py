from flask import Flask, render_template, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Spotify API credentials
client_id = '427c7e94df2b4d1f89ad703f2d83d005'
client_secret = '02a04d31f6a64e3ca79f8d16b7dfa51e'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = sp.search(query, limit=1, type='track')

    if not result['tracks']['items']:
        return jsonify({'message': 'No search results found.'}), 404

    track_id = result['tracks']['items'][0]['id']
    track_name = result['tracks']['items'][0]['name']
    artist_name = result['tracks']['items'][0]['artists'][0]['name']
    results = sp.recommendations(seed_tracks=[track_id], limit=10)

    return render_template('results.html', query=query, track_name=track_name, artist_name=artist_name, results=results['tracks'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
