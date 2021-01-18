import kotlin.math.abs
import kotlin.math.min

fun main(){
    val n:Long = readLine()!!.toLong();
    for(i in 0 until n){
        val inputs:List<Long> = readLine()!!.split(" ").map{ it -> it.toLong()}
        val aMinusN:Long = inputs[0] - inputs[4];
        val bMinusN:Long = inputs[1] - inputs[4];
        val mid:Long = inputs[4]/2;
        val rest:Long = inputs[4] - mid;
        var minValue:Long = 0
        val cond = (inputs[0] - inputs[4] ) - inputs[2]
        minValue = when {
            aMinusN >= inputs[2] && bMinusN >= inputs[3] -> min(min(aMinusN * inputs[1], bMinusN * inputs[0]), min((inputs[0] - mid) * (inputs[1] - rest), (inputs[0] - rest) * (inputs[1] - mid)))
            cond <= 0 && (inputs[1] - cond) - inputs[3] <= 0 -> {
                inputs[2] * inputs[3]
            }
            aMinusN >= inputs[2] -> {
                val k = abs(inputs[3] - bMinusN)
                min(aMinusN * inputs[1], (inputs[0] - k) * inputs[3])
            }
            else -> {
                val k = abs(inputs[2] - aMinusN)
                min(bMinusN * inputs[0], (inputs[1] - k) * inputs[2])
            }

        }
        println(minValue)
    }
}