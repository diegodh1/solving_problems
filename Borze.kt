fun main(){
    val borze:String = readLine()!!
    var number = ""
    var i = 0
    while (i < borze.length){
        when{
            borze[i] == '-' && borze[i+1] == '.' -> {number += "1"; i += 2;}
            borze[i] == '-' && borze[i+1] == '-' -> {number += "2"; i += 2;}
            else->{
                number += "0";
                i++
            }
        }
    }
    println(number)
}