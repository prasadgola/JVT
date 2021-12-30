function validateform(){  
var name=document.myform.email.value;  
var password=document.myform.pass.value;  
  
if (name==null || name==""){  
  alert("Username can't be blank");  
  return false;  
}else if(password==null || password==""){  
  alert("Please enter the password");  
  return false;  
  }  
} 