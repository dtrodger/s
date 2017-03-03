$(document).ready(function() {
  initEvanstonMap();
  initHPMap();
  initChiMap();
  initMPMap();
});

function initEvanstonMap() {
    var evanstonLatLng = {lat: 42.062802, lng: -87.697877}
    var evanstonMapDiv = document.getElementById('evanston_map');
    var evanstonMap = new google.maps.Map(evanstonMapDiv, {
        center: evanstonLatLng,
        zoom: 15
    });
    var marker = new google.maps.Marker({
      position: evanstonLatLng,
      map: evanstonMap,
    });
}

function initHPMap () {
    var hpLatLng = {lat: 42.185918, lng: -87.797339}
    var hpMapDiv = document.getElementById('hp_map');
    var hpMap = new google.maps.Map(hpMapDiv, {
        center: hpLatLng,
        zoom: 15
    });

    var marker = new google.maps.Marker({
      position: hpLatLng,
      map: hpMap,
    });
};

function initChiMap () {
    var chiLatLng = {lat: 41.893739, lng: -87.638988}
    var chiMapDiv = document.getElementById('chi_map');
    var chiMap = new google.maps.Map(chiMapDiv, {
        center: chiLatLng,
        zoom: 15
    });
    var marker = new google.maps.Marker({
      position: chiLatLng,
      map: chiMap,
    });
};

function initMPMap () {
    var mpLatLng = {lat: 42.063401, lng: -87.936185}
    var mpMapDiv = document.getElementById('mp_map');
    var mpMap = new google.maps.Map(mpMapDiv, {
        center: mpLatLng,
        zoom: 15
    });
    var marker = new google.maps.Marker({
      position: mpLatLng,
      map: mpMap,
    });
  };