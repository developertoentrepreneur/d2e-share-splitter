/* Project specific Javascript goes here. */
function showLoadingModal() {
  let loading = new bootstrap.Modal(document.getElementById("modalLoading"));
  loading.show();
  return loading;
}

function hideActiveModalShowLoading(modalId, formId) {
  if (isValidForm(formId)) {
    let active = getModal(modalId);
    active.hide();
    showLoadingModal();
  }
}

function deleteInstance(id, instance) {
  $("#formDelete").each(function () {
    $(this).attr("action", $(this).attr("action").replace("0000", id));
  });
  $("#modalDeleteTitle").text(`Delete  ${instance}`);
}

function isValidForm(formId) {
  var Form = document.getElementById(formId);
  return Form.checkValidity();
}

function getModal(modalId) {
  return new bootstrap.Modal(document.getElementById(modalId));
}
