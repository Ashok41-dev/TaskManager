const formSubmit=document.getElementById('addtask');


window.onload=()=>{
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
  const editButton=document.querySelectorAll('.editbtn');

  if(editButton)
  {
    for(let button of editButton)
    {
        button.addEventListener('click',(e)=>{
            console.log(e);
        })
    }
  }
}