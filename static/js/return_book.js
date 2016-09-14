
function return_book() {

var selected_book = $('input:radio:checked').val()
console.log(selected_book)
$.ajax({
        method: 'POST',
        url: '../returnloanedbook/',
        datatype:'json',
        data:JSON.stringify({'selected_book': selected_book}),
        error: function (data) {
        	alert('Oops...')
        },
        success: function (data) {
  			document.location.reload(true);
        }
       }); 
       

}
    

    



