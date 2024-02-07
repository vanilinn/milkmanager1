$(document).ready(function() {
    $('#fillForm').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        $.ajax({
            type: 'POST',
            url: '/fill_milk/',
            data: form.serialize(),
            success: function(response) {
                if (response.success) {
                    $('#fillMessage').text('Молоко успешно налито');
                    location.reload(); // Обновляем страницу после успешного залива
                } else {
                    $('#fillMessage').text(response.error_message);
                }
            }
        });
    });
});
