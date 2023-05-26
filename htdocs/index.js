const formSearch = document.getElementById("form-search");
const searchInput = document.getElementById('searchInput')
formSearch.addEventListener("submit", createList)


function createList(e) {
    e.preventDefault()

    if (searchInput.value){
        searchImages()
    }else{
      var imageContainer = document.getElementById('imageResults');
      while(imageContainer.firstChild){
        imageContainer.removeChild(imageContainer.firstChild)
      }
      var pElement = document.createElement('p');
      pElement.innerHTML = "anda belum mencari apapun"
      imageContainer.appendChild(pElement)
    }

}


function searchImages() {
  var searchQuery = searchInput.value;
  var imageDirectory = 'img/';

  // Clear previous results
  document.getElementById('imageResults').innerHTML = '';

  // Search images in the directory
  searchDirectory(searchQuery, imageDirectory, function(results) {
    var imageContainer = document.getElementById('imageResults');

    // Display images
    results.forEach(function(imageUrl) {
      var imgElement = document.createElement('img');
      imgElement.src = imageUrl;
      imageContainer.appendChild(imgElement);
    });
  });
}

function searchDirectory(query, directory, callback) {
  var results = [];

  // Simulating the search process (replace with your own logic)
  var imageFiles = [
    'avatar_g.jpg',
    'bridge.jpg',
    'coffee.jpg',
    'falls2.jpg',
    'gondol.jpg',
    'light.jpg',
    'londonjpg',
    'mist.jpg',
    'nature.jpg',
    'notebookk.jpg',
    'ocean',
    'ocean2',
    'photographer.jpg',
    'rock.jpg',
    'rocks(1).jpg',
    'rocks.jpg',
    'skies.jpg',
    'sound(1).jpg',
    'sound.jpg',
    'woods.jpg',
    'workbench.jpg',
    'workshop.jpg',

    // Add more image file names here
  ];

  imageFiles.forEach(function(fileName) {
    if (fileName.toLowerCase().includes(query.toLowerCase())) {
      results.push(directory + fileName);
    }
  });

  callback(results);
}
