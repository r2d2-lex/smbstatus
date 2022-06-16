function getUsername(selectObject)
{
  var value = selectObject.value;
  document.querySelector("#username").value = value;
}

function cleanFields(selectObject)
{
  document.querySelector("#username").value = '';
  document.querySelector("#filename").value = '';
}

function ajaxFields(selectObject){
    let id = selectObject.id;
    let username = document.getElementById(id).innerText;
    let filename = '';
    $.ajax({
            type: 'GET',
            url: '/ajax',
            data: {
                'username': username,
                'filename': filename,
            },
            dataType: 'json',
            success: function(data) {
                let content = data.content;

                $('#id_table tr').remove();
                $('#id_table tbody').append('<tr class="table-info">'+
            '<th scope="col">Имя пользователя</th>'+
            '<th scope="col">PID (Kill session)</th>'+
            '<th scope="col">Ресурс</th>'+
            '<th scope="col">Имя файла/папки</th>'+
            '<th scope="col">Дата</th>'+
            '</tr>');
                $('#id_table tbody').append(content);
            },
            error: function(data) { console.log('Ошибка выполнения'); },
    });
}