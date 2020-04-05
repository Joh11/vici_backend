
function setupFormCheck(file_reader_array) {
    document.getElementById('changeProfileData').addEventListener('submit', (function(reader_array) {
	return function(e) {
	    ///event is passed as 'e' in params
	    ///takes reader_array with file_reader_array as value
	    ///START SUBMIT CALLBACK//////////////////////////////////////////////////
	    var hidden_inputs="";
	    for(var i=0,r;r=reader_array[i];i++) {
		fd=r.file_data;
		fl=r.file_list;

		for(var j=0,f;f=fd[j];j++){
		    //create for each file a hidden input with its data as value
		    hidden_inputs+=`<input type="file" name="`+fl[j].name+`" value="`+f+`">`;
		}
	    }
	    //add hidden inputs to form before submitting
	    document.getElementById('changeProfileData').innerHTML+=hidden_inputs;

	    ///END SUBMIT CALLBACK////////////////////////////////////////////////////
	};
    })(file_reader_array));
}
