/* @author: Jonas T. Ulbrich
 * @date: 27.03.2020
 * To implement call script in head and set following html at desired position:
 <div id="file_reader_id" class="file_reader" >
   <script type="text/javascript">
     var readerImgs=new file_reader('file_reader_id','fs','cb','dz');
   </script>
 </div>
 * to deactivate  drag and drop don't feed 'dz' as parameter or set to false/undefined
 */

 // Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  console.log("All the File APIs are supported the file_reader class can be defined properly!");
}
else
  alert('The File APIs are not fully supported in this browser! Uploading files may not work properly...');

class file_reader extends FileReader {
  constructor(container_id,file_select_id,clear_button_id,drop_zone_id,ManageFiles_cb) {
    super();
    this.file_list=[];
    this.file_data=[];
    this.ManageFiles_cb=ManageFiles_cb;

    this.container_id=container_id;
    this.CreateHTMLFileReader(container_id,file_select_id,clear_button_id,drop_zone_id);
    if(drop_zone_id)
      this.SetupDragZone(drop_zone_id);
    this.SetupFileClear(clear_button_id);
    this.SetupFileSelect(file_select_id);
  }

  CreateHTMLFileReader(container_id,file_select_id,clear_button_id,drop_zone_id) {
    this.file_select_id=file_select_id;
    this.clear_button_id=clear_button_id;
    this.drop_zone_id=drop_zone_id;
    this.drop_zone_file_container_id=drop_zone_id+'_file_container';

    var html=`<input class="file_select" type="file" id="`+this.file_select_id+`" name="" multiple />
    <div class="drop_zone" id="`+this.drop_zone_id+`">
      <div class="drop_zone_file_container" id="`+this.drop_zone_file_container_id+`">
      </div>
    </div>

    <div class="file_select_buttons">
      <label for="`+this.file_select_id+`">Load Files</label>
      <input type="button" id="`+this.clear_button_id+`" name="Clear" value="Clear Files">
    </div>`;

    document.getElementById(container_id).innerHTML=html;
  }

  SetupFileSelect(file_select_id) {
    //binding this attribute to point at class and not element wich fired event
    //in context of called function!
    document.getElementById(file_select_id).addEventListener('change', this.FileSelect_cb.bind(this), false);
  }

  SetupDragZone(drop_zone_id) {
    var dropZone = document.getElementById(drop_zone_id);
    dropZone.addEventListener('dragover', this.DragOver_cb.bind(this), false);
    dropZone.addEventListener('dragleave', this.DragLeave_cb.bind(this), false);
    dropZone.addEventListener('drop', this.DropFile_cb.bind(this), false);
    document.getElementById(drop_zone_id).innerHTML+= '\n<p class="drop_here">Drop files here</p>';
  }

  SetupFileClear(clear_button_id) {
    document.getElementById(clear_button_id).addEventListener('click', this.ClearFiles_cb.bind(this), false);
  }

  ClearFiles_cb() {
    this.file_list=[];
    this.file_data=[];
    document.getElementById(this.drop_zone_file_container_id).innerHTML='';
  }

  RedefineManageFiles_cb(ManageFiles_cb) {
    this.ManageFiles_cb=ManageFiles_cb;
  }

  FileSelect_cb(evt) {
    //retrieve files
    var files=evt.target.files
    this.RetrieveData(files);

    if(typeof this.ManageFiles_cb==='function')
      this.ManageFiles_cb(this.file_list,this);
  }

  DropFile_cb(evt) {
    //stop propagation on other elements
    evt.stopPropagation();
    evt.preventDefault();

    //set style back to normal
    var styles=document.getElementById(this.drop_zone_id).style;
    styles['font-size']='';
    styles['transition']='';
    styles['outline-color']='';
    styles['color']='';

    //retrieve copied files
    var files=evt.dataTransfer.files
    this.RetrieveData(files);

    if(typeof this.ManageFiles_cb==='function')
      this.ManageFiles_cb(this.file_list,this);
  }

  DragOver_cb(evt) {
    //stop propagation on other elements
    evt.stopPropagation();
    evt.preventDefault();
    //change style for fancy display
    var styles=document.getElementById(this.drop_zone_id).style;
    styles['font-size']='2.5vh';
    styles['transition']='all 0.5s';
    styles['outline-color']='rgb(100,230,160)';
    styles['color']='rgb(100,230,160)';
    //copy dragged document
    evt.dataTransfer.dropEffect = 'copy';
  }

  DragLeave_cb(evt) {
    var styles=document.getElementById(this.drop_zone_id).style;
    styles['font-size']='';
    styles['transition']='';
    styles['outline-color']='';
    styles['color']='';
  }

  RetrieveData(files) {
    for(var i=0,file;file=files[i];i++) {
      this.file_list.push(file);

      //get last index of file_data to match index of file_list
      this.file_data.push(''); //create place fore data
      var idx=this.file_data.length-1;

      //add html element with loading gif
      document.getElementById(this.drop_zone_file_container_id).innerHTML+='<div class="uploaded_item"><div class="file_tb_container"><img src="img/loading.gif" class="uploaded_file_tb" id="'+this.drop_zone_file_container_id+'_tb'+idx+'"/></div><p>'+file.name+'</p><div class="delet_item"></div></div>\n';

      //define reader for each file:
      var reader =new FileReader;
      //set onload callback
      reader.onload=(function(file_idx,that) {
        return function(e) {
          var r=e.target.result;
          //save result
          that.file_data[file_idx]=r;

          //set tb
          document.getElementById(that.drop_zone_file_container_id+'_tb'+file_idx).src="img/plain_file_ico.png";
        };
      })(idx,this);

      //read file
      reader.readAsDataURL(file);
    }
  }

  GetFileData() {
    return this.file_data;
  }
}
