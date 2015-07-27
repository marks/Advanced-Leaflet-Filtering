# Advanced-Leaflet-Filtering
Allows the user to create a Leaflet map with multiple filters, each of which interacts with one another allowing for a more precise breakdown of the data represented.
<br><br>
Setup:<br>
1. Build your CSV file.<br>
  *Your csv file can contain two types of values:
    -True and false values. Let true be represented by 'y' and false be represented by 'n'. <br>
    - Value types. These are represented by a string. Say we had a column filled with coutries, some of the values may be           "United States", "China", "Australia", etc.<br>
2. Setting up the index.html file.<br>
  - Very little work needs to be done in the index.html file. <br>
  - First, scroll down until you see the large comment block that says "USER INPUT". Follow the instructions given.<br>
3. The map should now be ready to use.<br>
  -When testing locally on Chrome you need to first start a localhost inorder for the JQuery to work properly. I suggest using a   python SimpleHTTPServer for this. <br>
    -Locate the directory of the map and enter "python -m SimpleHTTPServer" to start the server.<br>
  -All other browsers should work fine without the server.<br>
<br>
Resources:<br>
Leaflet <br>
GeoCSV <br>
L.Control.Sidebar <br>
Active Layers <>
