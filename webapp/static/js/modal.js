$(document).ready(function() {
    $('a[data-bs-toggle=modal], button[data-toggle=modal]').click(function () {
    var data_id = '';
    if (typeof $(this).data('id') !== 'undefined') {
      data_id = $(this).data('id');
    }
    console.log(data_id);
    $('.modal-body #id_kill_value').val(data_id);

    var strLink = "session?userid=" + data_id;
    console.log(strLink);
//    document.getElementById("id_kill").setAttribute("href", strLink);
    document.getElementById("id_kill").on('click', function(event) {
            $(event.currentTarget).style('color', 'blue');
        })

    })
});
