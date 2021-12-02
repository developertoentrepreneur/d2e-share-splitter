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
