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
console.log("ASDASD");

$(".modal-body").eq(0).html("Done!");

var checkboxes = document.getElementsByName("checkbox");

for (var i=0; i<checkboxes.length; i++) {

    if (checkboxes[i].checked) {
        selected.push(checkboxes[i]);
    }
}
    
    for(var i=0; i<selected.length; ++i) {
    	console.log(selected[i].value);
    }

}


