function GetRatings(index) {

    var truth = document.getElementById("truth_rating " + index.toString());
    var truthSpans = document.getElementById( 'truth_rating '  + index.toString()).getElementsByTagName( 'span' );

    var fake = document.getElementById("fake_rating " + index.toString());
    var fakeSpans = document.getElementById( 'fake_rating ' + index.toString() ).getElementsByTagName( 'span' );

    var verified = document.getElementById("verified_rating " + index.toString());
    var verifiedSpans = document.getElementById( 'verified_rating ' + index.toString() ).getElementsByTagName( 'span' );

    var empty_star = "fa fa-star";
    var truth_star_full = "fa fa-star checked_green";
    var fake_star_full = "fa fa-star checked_red";
    var verified_star_full = "fa fa-star checked_blue";

    SetPictureRatingsStarClass(truthSpans, truth_star_full, empty_star, truth);
    SetPictureRatingsStarClass(fakeSpans, fake_star_full, empty_star, fake);
    SetPictureRatingsStarClass(verifiedSpans, verified_star_full, empty_star, verified);

}

function GetUserRatings(index) {
    var truth = document.getElementById("user_truth_rating " + index.toString());
    var truthSpans = document.getElementById( 'user_truth_rating '  + index.toString()).getElementsByTagName( 'span' );

    var fake = document.getElementById("user_fake_rating " + index.toString());
    var fakeSpans = document.getElementById( 'user_fake_rating ' + index.toString() ).getElementsByTagName( 'span' );

    var verified = document.getElementById("user_verified_rating " + index.toString());
    var verifiedSpans = document.getElementById( 'user_verified_rating ' + index.toString() ).getElementsByTagName( 'span' );

    var empty_star = "fa fa-star inside";
    var truth_star_full = "fa fa-star inside checked_green";
    var fake_star_full = "fa fa-star inside checked_red";
    var verified_star_full = "fa fa-star inside checked_blue";

    SetPictureRatingsStarClass(truthSpans, truth_star_full, empty_star, truth);
    SetPictureRatingsStarClass(fakeSpans, fake_star_full, empty_star, fake);
    SetPictureRatingsStarClass(verifiedSpans, verified_star_full, empty_star, verified);
}

function SetPictureRatingsStarClass(spanList, checkedClass, uncheckedClass, rating_type) {

    for (i = 0; i < rating_type.dataset.rating; i++) spanList[i].className = checkedClass;

    for (i = rating_type.dataset.rating; i < 5; i++) spanList[i].className = uncheckedClass;
}
