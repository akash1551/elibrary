$(function(){

	$('#search').keyup(function() {

		$.ajax({

			type:"POST",
			url:"/books/search/",
			data: {
				'search_text': $('#search').val()

			},
			success:searchSuccess,
			dataType:'html'
		});

	});
});

function searchSuccess(data,textStatus,jqXHR)
{
	$('#search_results').html(data);
}