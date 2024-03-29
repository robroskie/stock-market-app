$(document).ready(function () {
  console.log('script connected');
  // Set default dates
  $("#date-left").val("2020-09-29");
  $("#date-right").val("2021-09-29");
  $("#search-box").val("tesla");

  // Ajax request to update chart when dates changed
  $("#date-left, #date-right").on("change", function () {
    let dateStart = $("#date-left").val();
    let dateEnd = $("#date-right").val();

    $.ajax({
      url: "/calculate_result",
      cache: false,
      type: "GET",
      data: { dateStart: dateStart, dateEnd: dateEnd },
      success: function (response) {
        $("#stock-container-img").attr("src", "/static/images/plot9.png");
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  function changeInput(availableTags) {
    $("#search-box").autocomplete({
      source: availableTags,
    });
  }

  // Top matches as returned from alphavantage API
  $("#search-box").on("keyup", function (event) {
    if (event.key != "Enter") {
      console.log("keypress");
      let searchVal = $("#search-box").val();

      console.log(searchVal);
      $.ajax({
        url: "/get_ticker",
        cache: false,
        type: "GET",
        data: { searchVal: searchVal },
        success: function (response) {

          // This code block populates the autocomplete searchbox
          console.log(JSON.stringify(response));
          let data = [];
          let availableTags = [];

          let resultJSON = response["bestMatches"];
          if(resultJSON != undefined){
            for (let i = 0; i < resultJSON.length; i++) {
              availableTags.push({
              label:
                resultJSON[i]["2. name"] +
                "          Symbol: " +
                resultJSON[i]["1. symbol"],
            });
            console.log(resultJSON[i]["1. symbol"]);
            console.log(resultJSON[i]["2. name"]);
            data.push([resultJSON[i]["2. name"], resultJSON[i]["1. symbol"]]);
          }

          }
          console.log(availableTags);
          changeInput(availableTags);




        },
        error: function (error) {
          console.log(error);
        },
      });
    }
  });

  
  $('#search-box').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    let ticker = $("#search-box").val();

    if(keycode == '13'){
      alert('You pressed a "enter" key in textbox :)');  
      let dateStart = $("#date-left").val();
      let dateEnd = $("#date-right").val();

      $.ajax({
        url: "/get_news",
        cache: false,
        type: "GET",
        data: {ticker: ticker},
        success: function (response) {
          $("#stock-container-img").attr("src", "/static/images/plot9.png");


          // This code block updates the news section according to selected ticker val




        },
        error: function (error) {
          console.log(error);
        },
      });
    }
    else if(keycode == 8 || keycode == 46 ){
      console.log('erasing all!');
      searchVal = '';
    }
  });


});
