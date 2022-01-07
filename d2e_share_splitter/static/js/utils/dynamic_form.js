function dynamicFormRequest() {
  hideModalShowLoading("modalContentCreate", "modalLoading");
  var form = document.querySelector("form");
  var formData = new FormData(form);
  postRequest(urlUpdateForm, formData).then((response) => {
    $("#formCreate").html(response);
    hideLoadingShowModal("modalContentCreate", "modalLoading");
  });
}
