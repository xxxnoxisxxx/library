$(document).ready(function() {
    var table = $('#loan-wrapper').DataTable( {
        "columnDefs": [
            {
                "targets": [ 7 ],
                "visible": false,
            }
        ]
    } );
    $('#loan-wrapper tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        
       $(".modal-body").eq(0).html("<p>" + data[7] + "</p>");
       $(".modal-title").eq(0).html(data[1]);

    } );
    
   
    
} ) ;

var selected = [];

function loan() {

    	var checkboxes = document.getElementsByName("checkbox");
    
    for (var i=0; i<checkboxes.length; i++) {

  	  if (checkboxes[i].checked) {
  	      selected.push(checkboxes[i]);
  	  }
	}
    
    for(var i=0; i<selected.length; ++i) {
    	console.log(selected[i].value);
    }
    
   if(selected.length > 0){
        $(".modal-body").eq(0).html("Done!");
}

	console.log("ASDADASD");
    
    $.ajax({
        method: 'POST',
        url: '../loan/',
        data: {'selected': selected},
        success: function (data) {
             alert("it worked!");
        },
        error: function (data) {
             alert("it didnt work");
        }
       }); 
       
       }
       
       else
           $(".modal-body").eq(0).html("Select something!");
       
}


