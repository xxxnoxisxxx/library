var table = null;

$(document).ready(function() {
    table = $('#loan-wrapper').DataTable( {
        "columnDefs": [
            {
                "targets": [ 8 ],
                "visible": false,
            }
        ]
    } );
    $('#loan-wrapper tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        
       $(".modal-body").eq(0).html("<p>" + data[8] + "</p>");
       $(".modal-title").eq(0).html(data[1]);

    } );
    
   
    
} ) ;



function loan() {
var selected_books = [];
var selected_user = $('input:radio:checked').val()
    	
    	       $("input:checkbox:checked", $('#loan-wrapper').dataTable().fnGetNodes()).each(function(){
 	selected_books.push($(this).val());
});
    


    
   if(selected_books.length > 0){
    $.ajax({
        method: 'POST',
        url: '../loan/',
        datatype:'json',
        data:JSON.stringify({'selected_books': selected_books, 'selected_user' : selected_user}),
        error: function (data) {
        	alert('Oops...')
        },
        success: function (data) {

           	$(".modal-body").eq(0).html("Done!");
           	$("#myModal").on('hidden.bs.modal', function () {
  			document.location.reload(true);
		});
        }
       }); 
       
       }
       
       else
           $(".modal-body").eq(0).html("Select something!");
       
}


