$(document).ready(function() {
    alert("working")
    $("#rsvpform").submit(function(event){
        event.preventDefault();
        $.ajax({data:$(this).serialize(),
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                success: function(response){
                    console.log(response);
                    if(response['success']) {
                        $('#formmessage').html("<div class='alert alert-success'>"
                            + "Succesfully sent feedback, thank you!</div>");
                        $('#rsvpform').addClass("hidden");
                        $('#rsvpform')[0].reset();
                    }
                    if(response['error']){
                        $('#formmessage').html("<div class='alert alert-danger'>"
                                    + response['error']['comment'] + "</div>");
                    }
                },
                error: function(request, status, error){
                    console.log(request.response.Text);
                }
        });
    });

})
