// JavaScript Document

//Code to help with Sorting the Cert Number in proper order
jQuery.fn.dataTableExt.oSort['numeric-comma-asc']  = function(a,b) {
	var x = (a == "-") ? 0 : a.replace( /,/, "." );
	var y = (b == "-") ? 0 : b.replace( /,/, "." );
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ? -1 : ((x > y) ?  1 : 0));
};

jQuery.fn.dataTableExt.oSort['numeric-comma-desc'] = function(a,b) {
	var x = (a == "-") ? 0 : a.replace( /,/, "." );
	var y = (b == "-") ? 0 : b.replace( /,/, "." );
	x = parseFloat( x );
	y = parseFloat( y );
	return ((x < y) ?  1 : ((x > y) ? -1 : 0));
};




//Code for Table display and function
$('#table').dataTable( 
	{
		
		"sDom": "<'top'fl><'clear'><'title'ip><'clear'>rt<'F'ip><'clear'>",		 
		"sPaginationType": "full_numbers",
		"bSortClasses": false,	
		"sLengthMenu": [[10,25,50,100,-1], [10,25,50,100,"All"]],
		//"sSearch": {"caseInsensitive":false, "bEscapeRegex": false},
		//select the column to sort by default starting at 0
		//turning off sorting so that the order is as shown in the entries above
		//"aaSorting": [[ 1, "asc" ]],

		//order will be as entered
		"aaSorting": [],
		//One null for each column
		"aoColumns":
		[
			{"sType": "html", "aTargets": [0]}, //Bank Name
			
			null, //City
			
			null, // State
			
			{"sType": "numeric-comma"}, //CERT
			
			null, //Acquiring Institution
			
			{ "mRender": function(s) { return false; }, //Closing Date
	format: function(s) {
		var mon = s.substring(0, s.indexOf(" "));
		var day = s.substring(s.indexOf(" ") + 1, s.indexOf(',')); 
		if (day.length < 2) { day = "0" + day; } 
		var year = String(s.substring(s.length-5));
		var m = monthNames[mon];
		return year + m + day;
	},
	type: "Numerical"},
	
			{ "mRender": function(s) { return false; },  //Updated Date
	format: function(s) {
		var mon = s.substring(0, s.indexOf(" "));
		var day = s.substring(s.indexOf(" ") + 1, s.indexOf(',')); 
		if (day.length < 2) { day = "0" + day; } 
		var year = String(s.substring(s.length-5));
		var m = monthNames[mon];
		return year + m + day;
	},
	type: "Numerical", "bSearchable":false},

		],
		




});	


//Code for months to apply for sorting order	
	var monthNames = {};
monthNames["January"] = "01";
monthNames["February"] = "02";
monthNames["March"] = "03";
monthNames["April"] = "04";
monthNames["May"] = "05";
monthNames["June"] = "06";
monthNames["July"] = "07";
monthNames["August"] = "08";
monthNames["September"] = "09";
monthNames["October"] = "10";
monthNames["November"] = "11";
monthNames["December"] = "12";





 