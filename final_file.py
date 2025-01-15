import requests
import json
import time

# Chave Discorgs 
API_KEY = "KbugxmSGcxDYaHpBtdAkNCuEPbeclKcdrlhoDIfy"

def search_artist(name):
    """Pegando nome de artistas declarados """
    url = "https://api.discogs.com/database/search"
    params = {"q": name, "type": "artist", "token": API_KEY}
    response = requests.get(url, params=params)
    time.sleep(5)  # Delay between artist requests
    if response.status_code == 200:
        results = response.json().get("results", [])
        return results[0] if results else None
    print(f"Error searching for artist: {response.status_code}")
    return None

def artist_details(artist_id):
    """Pegando detalhes de artistas pelo ID."""
    url = f"https://api.discogs.com/artists/{artist_id}"
    response = requests.get(url)
    time.sleep(5)  # Delay after getting artist details
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching artist details: {response.status_code}")
    return None

def search_albums(artist_id):
    """Procurando pelos 3 ultimos albuns lançados ."""
    url = f"https://api.discogs.com/artists/{artist_id}/releases"
    params = {"sort": "year", "sort_order": "desc", "per_page": 3, "page": 1}
    response = requests.get(url, params=params)
    time.sleep(5)  # Delay
    if response.status_code == 200:
        return response.json().get("releases", [])
    print(f"Error searching for albums: {response.status_code}")
    return []

def album_details(release_id):
    """Detalhes dos albuns."""
    url = f"https://api.discogs.com/releases/{release_id}"
    response = requests.get(url)
    time.sleep(5)  # Delay 
    if response.status_code == 200:
        return response.json()
    print(f"Error fetching album details: {response.status_code}")
    return None

def collect_data(artists):
    """Coletando informações artistas, caso não encontre, skippa ."""
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
                
                # Delay
                time.sleep(10)

            data[artist] = {
                "Artist Name": details.get("name"),
                "Members": [member["name"] for member in details.get("members", [])] if "members" in details else None,
                "Artist Websites": details.get("urls", []),
                "Albums": album_data
            }
        except Exception as e:
            print(f"Error fetching information for artist '{artist}': {e}")
        
        # Delay
        time.sleep(15)
    
    return data

def save_to_json(data, file):
    """Salvando no Json"""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {file}")

# Por questão de volume, foi separado em 3 listas para captura 
artists_list_part1 = ["Nirvana", "The Beatles", "Radiohead"]
artists_list_part2 = ["Linkin Park", "Led Zeppelin", "Metallica"]
artists_list_part3 = ["Pearl Jam", "Green Day", "Aerosmith", "My Chemical Romance"]

all_data = {}  # Jogando para somente um arquivo

# Indexando em grupos 
for idx, group in enumerate([artists_list_part1, artists_list_part2, artists_list_part3], start=1):
    print(f"Starting collection for group {idx}...")
    collected_data = collect_data(group)
    all_data.update(collected_data)  # Mesclando todos os grupos 
    print(f"Collection for group {idx} complete!")
    time.sleep(20)  # Delay

save_to_json(all_data, "complete_data.json")
print("Data collection completed and saved!")
