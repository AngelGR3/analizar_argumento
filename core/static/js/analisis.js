$(function(){ 
    
    
    $("#texto").keyup(function(){

        if($("#texto").val().length ==0 || $("#texto").val() == " ") {
            console.log("campos vacios")
     
         }
        else{
        var post_url = $("#id_ensayo").data("post-url");
        var formData = new FormData($("#id_ensayo").get(0));
            $.ajax({
                url : post_url,
                type : "POST",
                data : formData,
                processData : false,
                contentType: false,
                success:function(response)
                {
                    //resultados enviados al template crear_ensayo
                    $('#premisa').val(response.premisa);
                    $('#conclu').val(response.conclu);
                    $('#mar_valorpremisa').val(response.mar_valorpremisa);
                    $('#mar_valorconclu').val(response.mar_valorconclu);
                    $('#numparrafos').val(response.numparrafos);
                    $('#promedio').val(response.promedio);
                    console.log("1")
                },

                error: function (){
                    alert("Algo salio mal");
                }
            });
        
        }
     });
    
});

