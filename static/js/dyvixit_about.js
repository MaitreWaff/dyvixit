function update_info_section(){
	// alert("Test OK!");
	update_holder = $('#info-update-holder');
	// alert(update_holder);
	most_recent   = update_holder.find("div:last"); // ("div:first");
	$.getJSON("/dyvixitsolutions/update-info-after/" + most_recent.attr('id') + "/",
	function(data){
		// cycle_class = most_recent.hasClass("odd") ? "even" : "odd";
		jQuery.each(data, function(){
			// update_holder.prepend("<b>Eureka!</b>");
			content_to_update = $('div.last-info');
			content_to_update.replaceWith('<div class="panel-body latest-info" id="'
			+ this.pk +'"><h1><a href="' + this.fields.link + '">' + this.fields.titre + '</a></h1>'
			+ '<p><a href="' + this.fields.link +'"><img src="/dyvixitsolutions/media/' + this.fields.photo + '" alt="Photo De la Derniere Info" width="225" height="225"></img></a></p><p>' + this.fields.desc + '</p></div>');
			// cycle_class = (cycle_class == "odd") ? "even" : "odd"
		});
	}
	);
}

$(document).ready(function(){
    //alert("About Page!");
	setInterval("update_info_section()", 10000);
});