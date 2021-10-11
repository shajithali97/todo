const task_dateEl=document.getElementById('task_date');
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; 
var yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
    
today = yyyy + '-' + mm + '-' + dd;

task_dateEl.setAttribute("value", today);
task_dateEl.setAttribute("min", today);

console.log(today);