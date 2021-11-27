function serializeForm(formId) {
  const form = document.getElementById(formId);
  let data = Object.fromEntries(new FormData(form).entries());
  data = { ...data, username: data.login };
  return data;
}

function loginAndStoreToken(formId, loginUrl) {
  let formData = serializeForm(formId);
  console.log(formData);
  console.log(loginUrl);
  postRequest(loginUrl, formData).then((response) => {
    storeToken(response.token);
  });
}

function storeToken(data) {
  localStorage.setItem("Token", data);
}
