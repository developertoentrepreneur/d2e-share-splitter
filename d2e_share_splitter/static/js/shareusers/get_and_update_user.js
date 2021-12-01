function getUserForm(id) {
  let loading = new bootstrap.Modal(document.getElementById("modalLoading"));
  loading.show();
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
      loading.hide();
      $("#modalsContainer").html(response);
      console.log("userFormModalUpdate");
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
