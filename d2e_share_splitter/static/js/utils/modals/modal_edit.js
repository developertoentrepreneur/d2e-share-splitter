// modal Update
function getInstance(id) {
  loadingModal = showLoadingModal();
  let url = url_edit.replace("0000", id);
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

function onPageLoadShowModalIfInvalidInput() {
  if (document.getElementsByClassName("is-invalid").length) {
    var modalUpdate = new bootstrap.Modal(
      document.getElementById("modalCreate")
    );
    modalUpdate.show();
    alert("Class exists");
  } else {
    alert("Class does not exist");
  }
}

onPageLoadShowModalIfInvalidInput();
