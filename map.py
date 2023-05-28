#findLocation()
import requests # send HTTP requests to API

API_KEY = 'YOUR_API_KEY'  # Google API key placeholder

# function that finds the location user requested
def search_location(query):
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={query}&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key={API_KEY}'
    response = requests.get(url) # GET request to API server
    data = response.json() # data in json format
    
    if 'candidates' in data: # if data is found, assign them to results
        results = data['candidates']
        for result in results:
            name = result['name']
            address = result['formatted_address']
            print(f"Name: {name}\nAddress: {address}\n")
    else:
        print('No results found.') # error message

# Usage
search_query = input("Enter an address to search: ")
search_location(search_query)



#showLocationOnMap
import webbrowser

def showLocationOnMap(address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK': # geocoded OK
        location = data['results'][0]['geometry']['location'] 
        lat = location['lat'] # latitude
        lng = location['lng'] # longitude
        map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=15&size=600x400&markers={lat},{lng}&key={API_KEY}'
        return map_url # url of location centered in maps
    else:
        print('No results found.') # error message
        return None

# Usage
search_query = input("Enter an address to search: ")
static_map_url = showLocationOnMap(search_query)

if static_map_url:
    webbrowser.open(static_map_url)
else:
    print("Invalid address or no results found.")



#findKeywordlocations

def findKeywordlocations(keyword, current_location):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={current_location}&radius=1000&keyword={keyword}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':  # API request successful
        results = data['results']
        for result in results:
            name = result['name']
            address = result['vicinity'] # approximate location
            location = result['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=15&size=600x400&markers={lat},{lng}&key={API_KEY}'
            print(f"Name: {name}\nAddress: {address}\nMap URL: {map_url}\n")
    else:
        print('No results found.')
        return None

# Usage
search_query = input("Enter a keyword to search: ")
current_location = input("Enter your current location (latitude,longitude): ")
findKeywordlocations(search_query, current_location)



#findIconLocations
#Θεωρητικά θα αντιστοιχεί ένα hyperlink που θα σε πάει στα αντίστοιχα keywords


# traceRouteAndDisplayOnMap
def traceRouteAndDisplayOnMap(start, finish):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={finish}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Usage
start_location = input("Enter the start location: ")
end_location = input("Enter the end location: ")

directions_data = traceRouteAndDisplayOnMap(start_location, end_location)
print(directions_data)



# getSubwayPath
def getSubwayPath(start, finish):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={finish}&mode=transit&transit_mode=subway&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Usage
start_location = input("Enter the start location: ")
end_location = input("Enter the end location: ")

directions_data = getSubwayPath(start_location, end_location)
print(directions_data)
