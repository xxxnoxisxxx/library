$(document).ready(function() {
    var table = $('#loan-wrapper').DataTable( {
        "columnDefs": [
            {
                "targets": [ 6 ],
                "visible": false,
            }
        ]
    } );
    $('#loan-wrapper tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        
       $(".modal-body").eq(0).html("<p>" + data[6] + "</p>");
       $(".modal-title").eq(0).html(data[1]);

    } );
    
   
    
} ) ;

