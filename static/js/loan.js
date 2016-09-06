var table = null;

$(document).ready(function() {
    table = $('#loan-wrapper').DataTable( {
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



function loan() {
var selected = [];
    	
    	       $("input:checked", $('#loan-wrapper').dataTable().fnGetNodes()).each(function(){
 	selected.push($(this).val());
});
    
console.log(selected);

    
   if(selected.length > 0){

    $.ajax({
        method: 'POST',
        url: '../loan/',
        datatype:'json',
        data:JSON.stringify({'selected': selected}),
        success: function (data) {
        },
        error: function (data) {
        	alert('Oops...')
        }
       }); 
       
       }
       
       else
           $(".modal-body").eq(0).html("Select something!");
       
}


