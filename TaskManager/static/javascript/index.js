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
           const reponse=await fetch('http://localhost:2000',{headers:{'Content-Type':"application/json"},method:'PUT'})
           if(reponse.ok)
           {
            const data=await reponse.json();
            console.log(data);
            return data;
           }
           console.log('Network issue!');
        })
    }
  }
}