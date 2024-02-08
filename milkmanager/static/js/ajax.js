$(document).ready(function() {
    $('#fillForm').submit(function(e) {
        e.preventDefault();
        let form = $(this);
        const csrf = $('input[name=csrfmiddlewaretoken]').val();
        let name = $('input[name=name]').val();
        let volume = $('input[name=volume]').val();
        console.log('csrf ->', csrf);
        console.log('name ->', name, volume);
        $.ajax({
            type: 'POST',
            url: 'fill_milk/',
            // url: '/',
            data: {
            'csrfmiddlewaretoken': csrf,
            'name': name,
            'volume': volume,
        },
            success: function(response) {
                if (response.success) {
                    console.log('send message ->', response);
                    $('#fillMessage').text('Молоко успешно налито');
                    $(`#${response.cistern_id}`).text(response.cistern_id  + ' - ' + response.cistern_volume + 'L / 300L');



                    form.trigger('reset');
                    // location.reload(); // Обновляем страницу после успешного залива
                } else {
                    $('#fillMessage').text(response.error_message);
                }
            }
        });
    });
});
