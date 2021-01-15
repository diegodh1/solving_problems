fun main(){
    val n:Int = readLine()!!.toInt();
    for (i in 0 until n){
        val t:Int = readLine()!!.toInt();
        if (t < 2){
            println(-1);
        }
        else{
            var number:String = "23";
            if(t > 2){
                number += "3".repeat(t - 2);
            }
            println(number)
        }

    }
}