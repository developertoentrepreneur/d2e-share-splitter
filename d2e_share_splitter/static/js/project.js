/* Project specific Javascript goes here. */
function showLoadingModal() {
  let loading = new bootstrap.Modal(document.getElementById("modalLoading"));
  loading.show();
  return loading;
}

function hideActiveModalShowLoading(modalId) {
  let active = new bootstrap.Modal(document.getElementById(modalId));
  active.hide();
  showLoadingModal();
}

// Delete Django Ajax Call
function deleteInstance(id, instance) {
  $("#formDelete").each(function () {
    $(this).attr("action", $(this).attr("action").replace("0000", id));
  });
  $("#modalDeleteTitle").text(`Delete  ${instance}`);
}
