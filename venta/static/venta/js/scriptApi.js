$(document).ready(function(){
    $("#mostrar").click(function(){
        $.get("https://colaboradores-e374e-default-rtdb.firebaseio.com/colaboradores.json",
        function(data){
            $.each(data,function(i,item){
                $("#tabla").append("<tr><td>"+item.id+"</td><td>"+item.nombre+"</td><td>"+item.año+"</td><td>"+item.descripcion+"</td></tr>");
            });
        });
    });

 

});