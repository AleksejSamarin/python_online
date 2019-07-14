function launch() {
    $.ajax({
        type: "POST",
        url: "/launch",
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            var json = jQuery.parseJSON(response)
            $('#output').html(json.output)
        }
    });
}