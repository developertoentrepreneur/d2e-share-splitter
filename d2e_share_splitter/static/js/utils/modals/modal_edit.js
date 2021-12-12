// modal Update
function getInstance(id) {
  loadingModal = showLoadingModal();
  let url = url_edit.replace("0000", id);
  getRequest(url).then(
    (response) => {
      loadingModal.hide();
      $("#editModalContainer").html(response);
      var modalUpdate = getModal("modalUpdate");
      modalUpdate.show();
    },
    (error) => {
      alert(error);
    }
  );
}

function showModalIfInvalidInput(modalId) {
  let modalElmnt = document.getElementById(modalId);
  if (modalElmnt && modalElmnt.getElementsByClassName("is-invalid").length) {
    modal = getModal(modalId);
    modal.show();
  } else {
  }
}

function onPageLoadShowModalsIfInvalidInput() {
  showModalIfInvalidInput("modalUpdate");
  showModalIfInvalidInput("modalCreate");
}

onPageLoadShowModalsIfInvalidInput();
