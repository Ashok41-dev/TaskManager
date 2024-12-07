
window.onload=()=>{
  const formSubmit=document.getElementById('addtask');

   if(!formSubmit)
    return;
    formSubmit.onsubmit=async(e)=>{
        e.preventDefault();
        const entries=new FormData(e.target);
        const object=Object.fromEntries(entries.entries());
        const message=document.getElementById('message');
        const response=await fetch('/createTask',{headers:{'Content-Type':'application/json'},method:'POST',body:JSON.stringify(object)});

        if(response.ok)
        {
             const data=await response.json();
             message.innerText=data.message;
             return data;
        }
        else
        {
             console.log('Network issue!');
        }
    }
    
}

UpdateTask()
async function UpdateTask(){
  const updateTask=document.querySelector('#updatetask');

  if(updateTask)
  {
  
    updateTask.onsubmit=async (e)=>{
         e.preventDefault();
      
          const formData=new FormData(e.target);
          const entries=Object.fromEntries(formData.entries());
          const id=window.location.pathname.split('/')[2];
          const message=document.querySelector('#message');

           const response=await fetch(`/update/${id}`,{headers:{'Content-Type':"application/json"},method:'PUT',
            body:JSON.stringify(entries)
            })
           if(response.ok)
           {
            const data=await response.json();
            message.innerText=data.message
            return data;
           }
           console.log('Network issue!');
        
    }
  }
}
SearchTask();

async function SearchTask(){
  const searchInput=document.querySelector('.searchinput');
  const searchButton=document.querySelector('.searchbtn');

  if(searchInput)
  {
    searchButton.onclick=async (e)=>{
         e.preventDefault();
         console.log('work',searchInput.value);
          window.location.href=`/search/${searchInput.value}`;
    }
  }
}