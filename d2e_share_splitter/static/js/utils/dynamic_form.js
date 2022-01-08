function dynamicFormRequest() {
  hideModalShowLoading("modalContentCreate", "modalInnerLoading");
  var form = document.querySelector("form");
  var formData = new FormData(form);
  postRequest(urlUpdateForm, formData).then((response) => {
    $("#formCreate").html(response);
    hideLoadingShowModal("modalContentCreate", "modalInnerLoading");
    (error) => {
      $("#formCreate").html(error.data);
      hideLoadingShowModal(`modalContentCreate`, `modalInnerLoading`);
    };
  });
}

function validateAndPostForm() {
  if (isValidForm("formCreate")) {
    hideModalShowLoading(`modalContentCreate`, `modalInnerLoading`);
  }
}
