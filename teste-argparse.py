import requests
import json
import time
import argparse

# Discogs API acesso
API_KEY = "KbugxmSGcxDYaHpBtdAkNCuEPbeclKcdrlhoDIfy"


def search_artist(name):
    """Procurando por artistas baseados nos nomes ."""
    url = "https://api.discogs.com/database/search"
    params = {"q": name, "type": "artist", "token": API_KEY}
    response = requests.get(url, params=params)
    time.sleep(10)  # Delay between artist requests
    if response.status_code == 200:
        results = response.json().get("results", [])
        return results[0] if results else None
    print(f"Error searching for artist: {response.status_code}")
    return None

def artist_details(artist_id):
    """Capturando detalhes dos artistas/ID."""
    url = f"https://api.discogs.com/artists/{artist_id}"
    response = requests.get(url)
    time.sleep(10)  # Delay para evitar erro 429
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching artist details: {response.status_code}")
    return None

def search_albums(artist_id):
    """Procura por 3 albuns mais recentes do artista."""
    url = f"https://api.discogs.com/artists/{artist_id}/releases"
    params = {"sort": "year", "sort_order": "desc", "per_page": 3, "page": 1}
    response = requests.get(url, params=params)
    time.sleep(15)  # Dalay para evitar excesso de requisição novamente
    if response.status_code == 200:
        return response.json().get("releases", [])
    print(f"Error searching for albums: {response.status_code}")
    return []

def album_details(release_id):
    """Captura de detalhes dos albuns."""
    url = f"https://api.discogs.com/releases/{release_id}"
    response = requests.get(url)
    time.sleep(15)  # Delay 
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching album details: {response.status_code}")
    return None

def collect_data(artists):
    """Dados de multiolos artistas com tratamento de dado skippando não encontrados."""
    data = {}
    for artist in artists:
        try:
            print(f"Fetching information for: {artist}")
            artist_info = search_artist(artist)
            if not artist_info:
                print(f"Artist '{artist}' not found. Skipping...")
                continue
            
            artist_id = artist_info["id"]
            details = artist_details(artist_id)
            if not details:
                print(f"Unable to get details for artist {artist_id}. Skipping...")
                continue

            albums = search_albums(artist_id)
            album_data = []

            for album in albums:
                try:
                    album_details_data = album_details(album["id"])
                    if album_details_data:
                        album_data.append({
                            "Album Name": album_details_data.get("title"),
                            "Release Year": album_details_data.get("year"),
                            "Label": [label["name"] for label in album_details_data.get("labels", [])],
                            "Genres": album_details_data.get("genres", []),
                            "Styles": album_details_data.get("styles", []),
                            "Tracks": [
                                {
                                    "Track Number": track.get("position"),
                                    "Track Name": track.get("title"),
                                    "Track Duration": track.get("duration")
                                }
                                for track in album_details_data.get("tracklist", [])
                            ]
                        })
                except Exception as e:
                    print(f"Error fetching details for album '{album.get('title')}': {e}")
                
                # Outro Delay
                time.sleep(15)

            data[artist] = {
                "Artist Name": details.get("name"),
                "Aliases": details.get("aliases", []),
                "Members": [member["name"] for member in details.get("members", [])] if "members" in details else None,
                "Artist Websites": details.get("urls", []),
                "Albums": album_data
            }
        except Exception as e:
            print(f"Error fetching information for artist '{artist}': {e}")
        
        # Delay
        time.sleep(20)
    
    return data

def save_to_json(data, file):
    """Salvando em Json."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {file}")

def main():
    parser = argparse.ArgumentParser(description="Collect artist data from Discogs")
    parser.add_argument("artists", nargs="+", help="List of artists to search for")
    args = parser.parse_args()

    artists = args.artists
    print(f"Starting collection for artists: {', '.join(artists)}")
    collected_data = collect_data(artists)
    save_to_json(collected_data, "collected_data.json")
    print("Collection complete!")

if __name__ == "__main__":
    main()
