window.onload = function(){

    var truth = document.getElementById("green");
    var fake = document.getElementById("red");
    var verified = document.getElementById("blue");

    var total = ( parseFloat(truth.dataset.stat) + parseFloat(fake.dataset.stat) + parseFloat(verified.dataset.stat));
    var h = parseFloat(truth.dataset.stat);
    var s = parseFloat(fake.dataset.stat);
    var c = parseFloat(verified.dataset.stat);
    var list = [h,s,c]

    var longest = 0;
    for(i = 0; i<list.length; i++){
        if (longest < list[i]){

            longest = list[i];

        }


    }
    var percent = [0.0,0.0,0.0];
    for(i=0; i<list.length; i++){
        if(list[i] == longest ){
            percent[i] = 1;
        }else{
            percent[i] = list[i]/longest;
        }
    }

    SetStat(percent[0], truth);
    SetStat(percent[1], fake);
    SetStat(percent[2], verified);
}

function SetStat(percentage, stat_type) {

    stat_type.style.width = (percentage*100) + "%" ;
}
