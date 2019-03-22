$( document ).ready(function() {

$(function(){
  $(".description").each(function(i){
    len=$(this).text().length;
    if(len>80)
    {
      $(this).text($(this).text().substr(0,170)+'...');
    }
  });
});


});