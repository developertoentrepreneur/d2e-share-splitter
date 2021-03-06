function performRequest(url, type, data) {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: url,
      type: type,
      headers: getTokenHeaders(),
      processData: false,
      contentType: false,
      data: data,
      success: function (data) {
        resolve(data);
      },
      error: function (error) {
        reject(error);
      },
    });
  });
}

function getRequest(url) {
  return performRequest(url, "GET", "");
}

function patchRequest(url, data) {
  return performRequest(url, "PATCH", data);
}

function postRequest(url, data) {
  return performRequest(url, "POST", data);
}
