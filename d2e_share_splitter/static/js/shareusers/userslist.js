// UpdateUser
function getUserForm(id) {
  let loading = new bootstrap.Modal(document.getElementById("modalLoading"));
  loading.show();
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
      loading.hide();
      $("#modalsContainer").html(response);
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
  $("#modalUserDeleteTitle").text(`Delete user ${username}`);
}
