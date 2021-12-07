// UpdateUser
function getUserForm(id) {
  loadingModal = showLoadingModal();
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
      loadingModal.hide();
      $("#editModalContainer").html(response);
      var modalUpdate = new bootstrap.Modal(
        document.getElementById("userFormModalUpdate")
      );
      modalUpdate.show();
    },
    (error) => {
      alert(error);
    }
  );
}

// Delete Django Ajax Call
function deleteUser(id, username) {
  $("#formDelete").each(function () {
    $(this).attr("action", $(this).attr("action").replace("0000", id));
  });
  $("#modalDeleteTitle").text(`Delete user ${username}`);
}
