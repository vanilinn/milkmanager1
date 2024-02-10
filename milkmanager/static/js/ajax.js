$(document).ready(function () {
    $('#fillForm').submit(function (e) {
        e.preventDefault();
        let form = $(this);
        const csrf = $('input[name=csrfmiddlewaretoken]').val();
        let name = $('input[name=name]').val();
        let volume = $('input[name=volume]').val();
        //console.log('csrf ->', csrf);
        //console.log('name ->', name, volume);
        $.ajax({
            type: 'POST',
            url: 'fill_milk/',
            data: {
                'csrfmiddlewaretoken': csrf,
                'name': name,
                'volume': volume,
            },
            success: function (response) {
                if (response.success) {
                    //console.log('send message ->', response.cistern_name);
                    $('#fillMessage').text('Молоко успешно налито');
                    //перерисовываем цистерну и добавляем в историю запись
                    $(`#${response.cistern_id}`).text(response.cistern_name + ' заполнена на  ' + response.cistern_volume + ' л. из 300 л.');
                    $('#fill_history_table').append('<li>' + response.name + ' залил ' + response.milk_filled + ' л. в ' + response.cistern_name + '</li>');
                    form.trigger('reset');
                } else {
                    $('#fillMessage').text(response.error_message);
                }
            }
        });
    });
});
