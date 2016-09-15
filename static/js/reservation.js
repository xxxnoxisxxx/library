var table = null;

$(document).ready(function() {
    table = $('#res-wrapper').DataTable( {
        "columnDefs": [
            {
                "targets": [ 8 ],
                "visible": false,
            }
        ]
    } );
    $('#res-wrapper tbody').on( 'click', 'button', function () {
        var data = table.row( $(this).parents('tr') ).data();
        
       $(".modal-body").eq(0).html("<p>" + data[8] + "</p>");
       $(".modal-title").eq(0).html(data[1]);

    } );
    
   
    
} ) ;



function reserve() {
    var selected_books = [];
    var selected_user = $('#userId').text();

  //   $("input:checkbox:checked", $('#res-wrapper').dataTable().fnGetNodes()).each(function(){
  // selected_books.push($(this).val());
    

    alert("user");
    alert(selected_user);
    
   if(selected_books.length > 0){
    $.ajax({
        method: 'POST',
        url: '../reserve/',
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


