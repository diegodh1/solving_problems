fun main(){
    val n:Int = readLine()!!.toInt()
    for(i in 0 until  n){
        val numbers:List<Int> = readLine()!!.split(" ").map { it -> it.toInt() }
        val result = if (numbers[0] % numbers[1] == 0) "YES" else "NO"
        println(result)
    }
}