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