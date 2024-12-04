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
        button.addEventListener('click',async(e)=>{
            const id=button.getAttribute('data-id');
            console.log(id);
           const response=await fetch('http://localhost:2000/update',{headers:{'Content-Type':"application/json"},method:'PUT',
            body:JSON.stringify(id)
            })
           if(response.ok)
           {
            const data=await response.json();
            console.log(data);
            return data;
           }
           console.log('Network issue!');
        })
    }
  }
}