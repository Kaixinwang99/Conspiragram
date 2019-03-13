window.onload = function(){

    var health = document.getElementById("purple");
    var style = document.getElementById("red");
    var cooking = document.getElementById("blue");

    var total = ( parseFloat(health.dataset.stat) + parseFloat(style.dataset.stat) + parseFloat(cooking.dataset.stat));
    var h = parseFloat(health.dataset.stat);
    var s = parseFloat(style.dataset.stat);
    var c = parseFloat(cooking.dataset.stat);
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

    SetStat(percent[0], health);
    SetStat(percent[1], style);
    SetStat(percent[2], cooking);
}

function SetStat(percentage, stat_type) {

    stat_type.style.width = (percentage*100) + "%" ;


}
