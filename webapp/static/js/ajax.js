$(document).ready(function(){
    $('#id_kill').on('click', killsession);
    function killsession() {
        var session = $('#id_kill_value').val();
        $.ajax({
            method : "GET",
            url: '/session/',
            data: {
                'userid': userid,
            },
            dataType: 'json',
            success: function (data) {
                /* ----- Success ---- */
                let status = data.status;
                showData(status);

                function showData(status) {
                    console.log(status)
                }
            },
            error: function(data){
                $('#id_spells').empty();
                console.log(data);
            }
        })
    }
})