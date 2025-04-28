from ytmusicapi import YTMusic

def test_search():
    ytmusic = YTMusic()
    query = "test query"
    
    try:
        search_result = ytmusic.search(query=query, limit=1)
        print("Search result:", search_result)
    except Exception as e:
        print("Error occurred during search:", e)

if __name__ == "__main__":
    test_search()
