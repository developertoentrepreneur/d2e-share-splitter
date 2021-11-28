function getUserForm(id) {
  let url = url_user_form.replace("0000", id);
  getRequest(url).then(
    (response) => {
      console.log(response);
    },
    (error) => {
      console.log("error");
      console.log(error);
      alert(error);
    }
  );
}
