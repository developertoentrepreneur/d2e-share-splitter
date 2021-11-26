// To see the datepicker: https://formden.com/blog/date-picker
var date_input = $('input[name="date"]'); //our date input has the name "date"
var container = $('.bootstrap-iso form').length > 0 ? $('.bootstrap-iso form').parent() : 'body';
var options = {
    format: 'yyyy-mm-dd',
    container: container,
    todayHighlight: true,
    autoclose: true
};
date_input.datepicker(options);

// Hide data initially
$('#expensesDiv').hide();
$('#expenses').removeAttr('required');
$('#expenses').removeAttr('data-error');

// https://jsfiddle.net/solodev/dpo07Ly5/
$('#contribType').change(function () {
    if ($(this).val() == 'time') {
        $('#hoursDiv').show();
        $('#hours').attr('required', '');
        $('#hours').attr('data-error', 'This field is required.');
        $('#expensesDiv').hide();
        $('#expenses').removeAttr('required');
        $('#expenses').removeAttr('data-error');
    } else if ($(this).val() == 'expenses' || $(this).val() == 'supplies' || $(this).val() == 'equipment') {
        $('#hoursDiv').hide();
        $('#hours').removeAttr('required');
        $('#hours').removeAttr('data-error');
        $('#expensesDiv').show();
        $('#expenses').attr('required', '');
        $('#expenses').attr('data-error', 'This field is required.');
    } else {
        $('#hoursDiv').hide();
        $('#hours').removeAttr('required');
        $('#hours').removeAttr('data-error');
        $('#expensesDiv').hide();
        $('#expenses').removeAttr('required', '');
        $('#expenses').removeAttr('data-error', 'This field is required.');
    }
});

// Create Django Ajax Call
$('form#addContrib').submit(function () {
    var date_input = $('input[name="date"]').val();
    var userInput = $('select[name="user"]').val();
    var contribTypeInput = $('select[name="contribType"]').val();
    var projectTypeInput = $('select[name="projectType"]').val();
    var expensesInput = parseFloat($('input[name="expenses"]').val());
    var descriptionInput = $('textarea[name="description"]').val();
    var hoursInput = parseFloat($('input[name="hours"]').val());

    if (userInput && contribTypeInput && projectTypeInput) {
        // Create Ajax Call
        $.ajax({
            url: var_url_contrib_create,
            data: {
                date: date_input,
                user: userInput,
                contribType: contribTypeInput,
                projectType: projectTypeInput,
                expenses: expensesInput,
                description: descriptionInput,
                hours: hoursInput
            },
            dataType: 'json',
            success: function (data) {
                if (data.contrib) {
                    appendToUsrTable(data.contrib);
                }
            }
        });
    } else {
        alert('All fields must have a valid value.');
    }
    $('form#addContrib').trigger('reset');
    return false;
});

// Delete Django Ajax Call
function deleteContrib(id) {
    var action = confirm('Are you sure you want to delete this contrib?');
    if (action != false) {
        $.ajax({
            url: var_url_contrib_delete,
            data: {
                id: id
            },
            dataType: 'json',
            success: function (data) {
                if (data.deleted) {
                    $('#contribTable #contrib-' + id).remove();
                }
            }
        });
    }
}

function appendToUsrTable(contrib) {
    $('#contribTable > tbody:last-child').append(`
          <tr id="contrib-${contrib.id}">
              <td name="name">${contrib.user}</td>
              '<td name="contribType">${contrib.contribType}</td>
              '<td name="projectType">${contrib.projectType}</td>
              '<td name="value">${contrib.value}</td>
              '<td name="hours">${contrib.hours}</td>
              '<td name="date">${contrib.date}</td>
              '<td name="details">${contrib.details}</td>
              '<td name="slices">${contrib.slices}</td>
              '<td align="center">
                  <button class="btn btn-danger form-control" onClick="deleteContrib(${contrib.id})">
                    <span class="glyphicon glyphicon-trash"></span>
                  </button>
              </td>
          </tr>
      `);
    $('#myModal1').modal('hide');
}
