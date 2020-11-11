$(document).ready(function() {
    $('#generateBtn').click(function() {
        let link = $('#link').val();
        if (link) {
            $.ajax({
                url: 'generate_qr/',
                type: 'POST',
                data: {
                    'user_link': link,
                    'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
                },
                success: function(data) {
                    $('#output_qr').attr('src', data);
                    $('#downloadBtn').attr('href', data);
                },
                error: function() {
                    console.log('Error');
                    alert('Error');
                }
            });
        } else {
            alert('Please enter the URL first')
        }
    });
});