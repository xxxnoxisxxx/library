$(document).ready(function() {
    var table = $('#book-wrapper').DataTable( {
        "columnDefs": [
            {
                "targets": [ 7 ],
                "visible": false,
            }
        ]
    } );
    $('#book-wrapper tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        
       $(".modal-body").eq(0).html("<p>" + data[7] + "</p>");
       $(".modal-title").eq(0).html(data[1]);

    } );
    
   
    
} ) ;

