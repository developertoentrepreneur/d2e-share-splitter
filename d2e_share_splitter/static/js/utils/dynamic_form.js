function dynamicFormRequest() {
  modal = getModal("modalCreateDynamic");
  modal.hide();
  loadingModal = showLoadingModal();
  var form = document.querySelector("form");
  var formData = new FormData(form);
  postRequest(urlUpdateForm, formData).then((response) => {
    $("#formCreate").html(response);
    loadingModal.hide();
    modal.show();
  });
}
