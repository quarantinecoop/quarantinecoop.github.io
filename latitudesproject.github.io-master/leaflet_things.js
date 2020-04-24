function main() {

var mymap = L.map('map').setView([39.8, -98.56], 4);

   var positron = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png', {
        attribution: '©OpenStreetMap, ©CartoDB'
}).addTo(mymap);

   L.marker([39.8, -98.56]).addTo(mymap)
		.bindPopup("<b>Hello world!</b><br />I am a popup.");
   var polygon = L.polygon([
    [39.8, -98.56],
    [39.8, -90.56]
], {color: 'grey'}).addTo(mymap);
   
   
}
 window.onload = main;


