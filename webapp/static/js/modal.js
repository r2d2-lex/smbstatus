$(document).ready(function() {
    $('a[data-bs-toggle=modal], button[data-toggle=modal]').click(function () {
    let data_id = '';
    if (typeof $(this).data('id') !== 'undefined') {
      data_id = $(this).data('id');
    }
    $('.modal-body #id_kill_value').val(data_id);
    })
});

function closeModal(selectObject) {
    let userid = $('.modal-body #id_kill_value').val();
    $.ajax({
        type: 'GET',
        url: '/session',
        data: {'userid': userid,},
        dataType: 'json',
        success: function(data) {
            let status = data.status;
            $('#id_status').empty();
            let div = showMessage(status, 'alert-danger');
            $('#id_status').append(div);
            goUp();
            console.log(data);

            function showMessage(message, classAlert)
                {
                    let div = document.createElement('div');
                    div.classList.add("alert");
                    div.classList.add(classAlert);
                    div.setAttribute("role", "alert");
                    div.innerHTML = message
                    return div
                }
            function goUp()
                {
                    window.scrollBy(0,-1000000000);
                }
            },

        error: function(data) { console.log('Ошибка выполнения'); },
    });
    $("#exampleModal").modal('hide');
}

