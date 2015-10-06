# Advanced-Leaflet-Filtering
Allows the user to create a Leaflet map with multiple filters, each of which interacts with one another allowing for a more precise breakdown of the data represented.
<br><br>
__Setup:__<br>
__1. Build your CSV file. Your csv file can contain two types of values:__ <br>
  *The CSV must contain latitude and longitude values for each address. These columns should be named 'lat' and 'lng'.<br>
  *True and false values. Let true be represented by 'y' and false be represented by 'n'.<br>
  *Value types. These are represented by a string. Say we had a column filled with coutries, some of the values may be           "United States", "China", "Australia", etc.<br>
__2. Setting up the index.html file:__<br>
  *Scroll down until you see the large comment block that says "USER INPUT". Follow the instructions given.<br>
__3. The map should now be ready to use.__<br>
  *When testing locally on Chrome you need to first start a localhost inorder for the JQuery to work properly. I suggest using a  python SimpleHTTPServer for this. <br>
    *Locate the directory of the map and enter "python -m SimpleHTTPServer" to start the server.<br>
  *All other browsers should work fine without the server.<br>

__*Resources:__<br>
  *[Leaflet](http://leafletjs.com/) <br>
  *[GeoCSV](https://github.com/joker-x/Leaflet.geoCSV) <br>
  *[L.Control.Sidebar](https://github.com/turbo87/leaflet-sidebar/) <br>
  *[Active Layers](https://github.com/vogdb/Leaflet.ActiveLayers) <br>
  
  __*Examples:__<br>
   *[Apartments](http://www.codedes.com/Apartments)<br>
   *[Coffee Shops](http://www.despecialreport.com/coffee)<br>
  
  <br><br>
  Also, I am working on interactive GUI right now that should help ease the process even more.<br><br>
