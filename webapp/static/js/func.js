function getUsername(selectObject){
  var value = selectObject.value;
  document.querySelector("#username").value = value;
}

function cleanFields(selectObject){
  document.querySelector("#username").value = '';
  document.querySelector("#filename").value = '';
}

function nameFields(selectObject){
    let id = selectObject.id;
    let username = document.getElementById(id).innerText;
    $.ajax({
            type: 'GET',
            url: '/ajax',
            data: {
                'username': username,
            },
            dataType: 'json',
            success: function(data) {
                let content = data.content;
                $('#id_table tr').remove();
                $('#id_table tbody').append(content);
            },
            error: function(data) { console.log('Ошибка выполнения'); },
    });
}

function fileFields(selectObject){
    let id = selectObject.id;
    let filename = document.getElementById(id).innerText;
    $.ajax({
            type: 'GET',
            url: '/ajax',
            data: {
                'filename': filename,
            },
            dataType: 'json',
            success: function(data) {
                let content = data.content;
                $('#id_table tr').remove();
                $('#id_table tbody').append(content);
            },
            error: function(data) { console.log('Ошибка выполнения'); },
    });
}

