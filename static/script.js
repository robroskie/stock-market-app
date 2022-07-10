$(document).ready(function () {
  $("#date-left").val("2011-09-29");
  $("#date-right").val("2011-09-29");

  console.log("connected");
  $(".dl, .dr").on("click", function () {
    console.log("clicked");
    let dateStart = $("#date-left").val();
    let dateEnd = $("#date-right").val();

    $.ajax({
      url: "/calculate_result",
      cache: false,
      type: "GET",
      data: {dateStart : dateStart, dateEnd : dateEnd},
			success: function(response){
        console.log('success\n');
        // console.log(resp.path);
        $('#stock-container-img').attr('src', "static/plot7.png");
        
				// console.log(response);
			},
			error: function(error){
				console.log('***error***      ' + error);
			}
    });
  });
});
