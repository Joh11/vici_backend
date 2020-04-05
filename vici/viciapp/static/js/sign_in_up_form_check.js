
function setupFormCheck() {
  document.getElementById('pw').addEventListener('input', checkPwFormatCb);
  document.getElementById('pwConfirm').addEventListener('input', checkPwConfirmCb);
  document.getElementById('signInUp').addEventListener('submit', submitCb);
}


//CHOOSE COLORS PROPERLY AND FINALIZE FUNCTIONALITEIS
function checkPwFormatCb(evt) {
  if(document.getElementById('registerFormCheck').checked){
    var pw=evt.target.value, styles=evt.target.style;
    var errorBox=document.getElementById('pwErrorJS');
    var strength=0, pwIsTooShort=true;
    var red='rgb(255, 153, 51)', dark_orange='rgb(255, 204, 0)',orange='rgb(255, 255, 77)',green='rgb(204, 255, 51)'

    if (pw.match(/[a-z]+/))
      strength += 1;
    if (pw.match(/[A-Z]+/))
      strength += 1;
    if (pw.match(/[0-9]+/))
      strength += 1;
    if (pw.match(/[$@#&!]+/))
      strength += 1;

    //set info string
    if(pw.length<8) {
      errorBox.innerHTML="Password must have at least 8 characters";
      pwIsTooShort=true;
    }
    else {
      errorBox.innerHTML="";
      pwIsTooShort=false;
    }

    if(strength<3) {
      if(pwIsTooShort){
        errorBox.innerHTML+="</br>Use MAJUSC,minusc numbers or symbols to increase pw strenght";
      }
      else {
        errorBox.innerHTML="Use MAJUSC,minusc numbers or symbols to increase pw strenght";
      }
    }

    //change border color according to pw strenght
    if(pwIsTooShort) {
      styles['border']='2px solid '+red;
    }
    else {
      switch (strength) {
        case 0:
          styles['border']='2px solid '+red;
          break;

        case 1:
          styles['border']='2px solid '+red;
          break;

        case 2:
          styles['border']='2px solid '+dark_orange;
          break;

        case 3:
          styles['border']='2px solid '+orange;
          break;

        case 4:
          styles['border']='2px solid '+green;
          break;
        default:
          styles['border']='2px solid '+green;
      }
    }
  }
  else {
    evt.target.style['border']='none';
    document.getElementById('pwErrorJS').innerHTML=''
  }
}

//SUBMIT CALL BACK... FURTHER EDITING NEEDED TO IMPLEMENT ALL CHECKPOINTS!!!
function submitCb(evt) {
  var empty="";
  if(document.getElementById('registerFormCheck').checked) {
    var email=document.getElementById('email').value;
    var companyName=document.getElementById('companyName').value;
    var pw=document.getElementById('pw').value;
    var pwConfirm=document.getElementById('pwConfirm').value;

    if(email==empty || pw==empty || pwConfirm==empty || companyName==empty){
      evt.preventDefault();
      document.getElementById('submitErrorJS').innerHTML="please fill in correctly the form"
      return false;
    }
    else if (!document.getElementById('termsAndConditionsCheck').checked) {
      evt.preventDefault();
      document.getElementById('submitErrorJS').innerHTML="Please accept the terms and conditions"
      return false;
    }

    //ADD OTHER CHECKS
  }
  else {
    var email=document.getElementById('email').value;
    var pw=document.getElementById('pw').value;

    if(email==empty || pw==empty){
      evt.preventDefault();
      document.getElementById('submitErrorJS').innerHTML="please fill in correctly the form"
      return false;
    }

    //ADD OTHER CHECKS
  }
}

function checkPwConfirmCb(evt) {
  if(document.getElementById('registerFormCheck').checked) {
    var pwConfirm=evt.target.value,styles=evt.target.style
    var pw=document.getElementById('pw').value;
    var red='rgb(255, 153, 51)',green='rgb(204, 255, 51)';

    if(pw!=pwConfirm) {
      styles['border']='2px solid '+red;
    }
    else {
      styles['border']='2px solid '+green;
    }
  }
}
