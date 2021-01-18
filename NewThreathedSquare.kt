import kotlin.math.floor
import kotlin.math.min

fun main(){
    val n:Int = readLine()!!.toInt()
    var row:String
    for(i in 0 until n){
        val values:List<Int> = readLine()!!.split(" ").map { it -> it.toInt() }
        var sum = 0
        var minValue = 0
        for(j in 0 until values[0]){
            row = readLine()!!
            sum = 0
            var pairs = 0
            var cons = 0
            for (k in row.indices) {
                if (row[k] == '.') {
                    sum++
                }
                when{
                    k > 0 && row[k] == '.' && row[k] == row[k-1] && cons == 0 -> cons += 2
                    k > 0 && row[k] == '.' && row[k] == row[k-1] -> cons += 1
                    k > 0 && row[k] != row[k-1] && cons != 0 -> {
                        pairs += cons
                        cons = 0
                    }
                }
            }
            if (cons > 0){
                pairs += cons
            }
            var twoTiles:Int = 0
            if (pairs > 0){
                twoTiles = floor((pairs / 2).toDouble()).toInt()
            }
            val minV = min(twoTiles * values[3] + (sum - 2 * twoTiles) * values[2], sum * values[2])
            println(minV)
            minValue += minV
        }
        println(minValue)
    }
}