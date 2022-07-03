$(document).ready(function () {
    console.log('connected');
    $(".dl, .dr").on("click", function () {
    console.log("clicked");
    let dateStart = $("#date-left").val();
    let dateEnd = $("#date-right").val();
    $.ajax({
      url: "/calculate_result",
      type: "get",
      data: { dateStart: dateStart, dateEnd: dateEnd },
      success: function (response) {
        $(".result").html("<p>" + response.result.toString() + "</p>");
      },
    });
  });
});
