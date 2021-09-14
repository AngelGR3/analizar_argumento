$(function(){ 

 // $("#id_ensayo").on('submit', function(){
    $("#texto").keyup(function(){
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
                    console.log(texto)
                    console.log(response)
                    //resultados enviados al template crear_ensayo
                    $('#premisa').val(response.premisa);
                    $('#conclu').val(response.conclu);
                    $('#mar_valorpremisa').val(response.mar_valorpremisa);
                    $('#mar_valorconclu').val(response.mar_valorconclu);
                },

                error: function (){
                    alert("Algo salio mal");
                }
            });
        return false;
        
     });
});

