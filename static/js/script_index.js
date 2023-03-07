var A_column = document.getElementById("A_column")
var B_row = document.getElementById("B_row")


function check(){
    if (A_column.value!=B_row.value){
        alert("Aの列数、Bの行数が正しく演算することができません")
        return false;
    }
    return true;
}





