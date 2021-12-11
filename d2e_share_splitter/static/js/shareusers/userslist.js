// UpdateUser
function getUserForm(id) {
  loadingModal = showLoadingModal();
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
      loadingModal.hide();
      $("#editModalContainer").html(response);
      var modalUpdate = new bootstrap.Modal(
        document.getElementById("modalUpdate")
      );
      modalUpdate.show();
    },
    (error) => {
      alert(error);
    }
  );
}
