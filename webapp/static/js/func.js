function getUsername(selectObject){
  var value = selectObject.value;
  document.querySelector("#username").value = value;
}

function cleanFields(selectObject){
  document.querySelector("#username").value = '';
  document.querySelector("#filename").value = '';
  nameFields(this);
}

function nameFields(selectObject){
    let id = selectObject.id;
    let username = '';
    let filename = '';

    if (typeof id !== 'undefined'){
    console.log(id);
    let idname = 'idname';
    let idfile = 'idfile';
    let foundName = id.match(idname);
    let foundFile = id.match(idfile);

    if (!foundName){
        username = '';
    } else {
        username = document.getElementById(id).innerText;
    }
    console.log('username:', username);

    if (!foundFile){
        filename = '';
    } else {
        filename = document.getElementById(id).innerText;
    }
    console.log('filename:', filename);
    }


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
                $('#id_table tbody').append(content);
            },
            error: function(data) { console.log('Ошибка выполнения'); },
    });
}

