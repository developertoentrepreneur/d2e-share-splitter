// Create Django Ajax Call
$("form#addUser").submit(function () {
  var nameInput = $('input[name="name"]').val().trim();
  var emailInput = $('input[name="email"]').val().trim();
  var jobTitleInput = $('input[name="jobTitle"]').val().trim();
  var yearSalaryInput = $('input[name="yearSalary"]').val().trim();
  console.log("Calling POST");
  if (nameInput && emailInput && jobTitleInput && yearSalaryInput) {
    console.log("Calling posr");
    // Create Ajax Call
    $.ajax({
      url: var_url_user_create,
      method: "POST",
      data: {
        name: nameInput,
        email: emailInput,
        jobTitle: jobTitleInput,
        yearSalary: yearSalaryInput,
      },
      dataType: "json",
      success: function (data) {
        if (data.user) {
          appendToUsrTable(data.user);
        }
      },
    });
  } else {
    alert("All fields must have a valid value.");
  }
  $("form#addUser").trigger("reset");
  return false;
});

// Delete Django Ajax Call
function deleteUser(id) {
  console.log("Delete");
  alert("Creating");
  var action = confirm("Are you sure you want to delete this user?");
  if (action != false) {
    $.ajax({
      url: var_url_user_delete,
      data: {
        id: id,
      },
      dataType: "json",
      success: function (data) {
        if (data.deleted) {
          $("#userTable #user-" + id).remove();
        }
      },
    });
  }
}

// Create Django Ajax Call
$("form#updateUser").submit(function () {
  var idInput = $('input[name="formId"]').val().trim();
  var nameInput = $('input[name="formName"]').val().trim();
  var emailInput = $('input[name="formEmail"]').val().trim();
  var jobTitleInput = $('input[name="formJobTitle"]').val().trim();
  var yearSalaryInput = $('input[name="formYearSalary"]').val().trim();
  if (nameInput && emailInput && jobTitleInput && yearSalaryInput) {
    // Create Ajax Call
    $.ajax({
      url: var_url_user_update,
      data: {
        id: idInput,
        name: nameInput,
        email: emailInput,
        jobTitle: jobTitleInput,
        yearSalary: yearSalaryInput,
      },
      dataType: "json",
      success: function (data) {
        if (data.user) {
          updateToUserTabel(data.user);
        }
      },
    });
  } else {
    alert("All fields must have a valid value.");
  }
  $("form#updateUser").trigger("reset");
  $("#myModal").modal("hide");
  return false;
});

// Update Django Ajax Call
function editUser(id) {
  if (id) {
    tr_id = "#user-" + id;
    name = $(tr_id).find(".userName").text();
    email = $(tr_id).find(".userEmail").text();
    jobTitle = $(tr_id).find(".userJobTitle").text();
    yearSalary = $(tr_id).find(".userYearSalary").text();
    $("#form-id").val(id);
    $("#form-name").val(name);
    $("#form-email").val(email);
    $("#form-jobTitle").val(jobTitle);
    $("#form-yearSalary").val(yearSalary);
  }
}

function appendToUsrTable(user) {
  $("#userTable > tbody:last-child").append(`
          <tr id="user-${user.id}">
              <td class="userName" name="name">${user.name}</td>
              '<td class="userEmail" name="email">${user.email}</td>
              '<td class="userJobTitle" name="jobTitle">${user.jobTitle}</td>
              '<td  name="slices">${user.slices}</td>
              '<td class="userYearSalary" name="yearSalary">${user.yearSalary}</td>
              '<td align="center">
                  <button class="btn btn-success form-control" onClick="editUser(${user.id})" data-toggle="modal" data-target="#myModal")">EDIT</button>
              </td>
              <td align="center">
                  <button class="btn btn-danger form-control" onClick="deleteUser(${user.id})">DELETE</button>
              </td>
          </tr>
      `);
  $("#myModal1").modal("hide");
}

function updateToUserTabel(user) {
  $("#userTable #user-" + user.id)
    .children(".userData")
    .each(function () {
      var attr = $(this).attr("name");
      if (attr == "name") {
        $(this).text(user.name);
      } else if (attr == "email") {
        $(this).text(user.email);
      } else if (attr == "jobTitle") {
        $(this).text(user.jobTitle);
      } else {
        $(this).text(user.yearSalary);
      }
    });
}
