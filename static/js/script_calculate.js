const matrix_element = document.getElementsByClassName("matrix_e");

var cal_btn = document.getElementById("cal_btn");
cal_btn.addEventListener('submit',check_element);

function check_element(){
    for(let i=0;i<matrix_element.length;i++){
        if(isNaN(matrix_element[i].value)==true){
            return false;
        }
    }
    return true;
}






