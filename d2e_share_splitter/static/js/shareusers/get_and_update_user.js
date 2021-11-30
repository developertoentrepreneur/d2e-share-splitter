function getUserForm(id) {
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
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
