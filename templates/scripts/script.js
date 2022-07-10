$(document).ready(function () {
    $('#date-left').val("2011-09-29");
    $('#date-right').val("2011-09-29");

    console.log('connected');
    $(".dl, .dr").on("click", function () {
    console.log("clicked");
    let dateStart = $("#date-left").val();
    let dateEnd = $("#date-right").val();
    var date_data = [
      {"dateStart": dateStart},
      {"dateEnd": dateEnd}
    ];
    $.ajax({
      url: "/calculate_result",
      type: "POST",
      data: JSON.stringify(date_data),
      contentType: "application/json",
      dataType: 'json' 
    });
  });
});
