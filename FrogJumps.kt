//link to the problem https://codeforces.com/problemset/problem/1077/A
import kotlin.math.floor

fun main(){
    val n:Int = readLine()!!.toInt();
    for (i in 0 until n){
        val input:List<Long> = readLine()!!.split(" ").map { it -> it.toLong() }
        var result:Long = 0
        val number = input[2] % 2
        val mod:Long = 0
        result = if(number == mod){
            val c = input[2]/2
            c * (input[0] - input[1])
        } else{
            val c = floor(input[2] / 2.toDouble()).toLong()
            (input[2] - c) * input[0] - c * input[1]
        }
        println("$result")
    }
}