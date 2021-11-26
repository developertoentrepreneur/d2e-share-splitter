// Create Django Ajax Call
$("form#addProj").submit(function () {
  var nameInput = $('input[name="name"]').val().trim();
  if (nameInput) {
    // Create Ajax Call
    $.ajax({
      url: var_url_proj_create,
      data: {
        name: nameInput,
      },
      dataType: "json",
      success: function (data) {
        if (data.proj) {
          appendToProjTable(data.proj);
        }
      },
    });
  } else {
    alert("All fields must have a valid value.");
  }
  $("form#addProj").trigger("reset");
  return false;
});

// Delete Django Ajax Call
function deleteProj(id) {
  var action = confirm("Are you sure you want to delete this proj?");
  if (action != false) {
    $.ajax({
      url: var_url_proj_delete,
      data: {
        id: id,
      },
      dataType: "json",
      success: function (data) {
        if (data.deleted) {
          $("#projTable #proj-" + id).remove();
        }
      },
    });
  }
}

function appendToProjTable(proj) {
  $("#projTable > tbody:last-child").append(`
          <tr id="proj-${proj.id}">
              <td class="projName" name="name">${proj.name}</td>
              '<td align="center">
                  <button class="btn btn-danger form-control" onClick="deleteProj(${proj.id})">
                    <span class="glyphicon glyphicon-trash"></span>
                  </button>
              </td>
          </tr>
      `);
  $("#myModal").modal("hide");
}
