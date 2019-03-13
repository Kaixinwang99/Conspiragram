function viewBigPost(index) {
    var modal = document.getElementById('big_post ' + index.toString());

    modal.style.display = "block";

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close " + index.toString())[0];

    var body = document.getElementsByTagName('body')[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
        body.style.overflow = "visible";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            body.style.overflow = "visible";
        }
    }
}