function update(){
	//alert("Test OK!");
	update_holder = $('#update-holder');
	most_recent   = update_holder.find("div:first");
	$.getJSON("/updates-after/" + most_recent.attr('id') + "/",
	function(data){
		cycle_class = most_recent.hasClass("odd") ? "even" : "odd";
		jQuery.each(data, function(){
			update_holder.prepend("Test!");
			cycle_class = (cycle_class == "odd") ? "even" : "odd"
		});
	}
	)
}

$(document).ready(function(){
    //alert("About Page!");
	setInterval("update()", 60000);
});