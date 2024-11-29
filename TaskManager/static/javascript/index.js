const formSubmit=document.getElementById('addtask');


window.onload=()=>{
    formSubmit.onsubmit=async(e)=>{
        e.preventDefault();
        const entries=new FormData(e.target);
        const object=Object.fromEntries(entries.entries());
    
        const response=await fetch('/createTask',{headers:{'Content-Type':'application/json'},method:'POST',body:JSON.stringify(object)});

        if(response.ok)
        {
             const data=await response.json();
             console.log(data);
             return data;
        }
        else
        {
             console.log('Network issue!');
        }
    }
    
}
