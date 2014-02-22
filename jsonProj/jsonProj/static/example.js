function buildList(data)
{
	var testJS = JSON.parse(data);
		
		//not the ideal way to build a ul object, but easy to follow the logic
		$.each(testJS, function(index, obj){
			$(".list-group").append("<li class='list-group-item'>" + obj + "</li>");
		})
}