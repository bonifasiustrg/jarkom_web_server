function searchImage() {
    var searchTerm = document.getElementById("searchBox").value;
    var imgPath = "htdocs/imag/" + searchTerm + ".jpg"; // replace with your own image directory path
    var searchResults = document.getElementById("searchResults");
    searchResults.innerHTML = "<img src='" + imgPath + "'>"; // display the image on the page
}