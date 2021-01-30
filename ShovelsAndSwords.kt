import java.lang.Integer.max
import java.util.*

fun solve(stick:Long, diamond:Long):Int{
    return when{
        stick == 0L ->  0
        diamond == 0L ->  0
        else ->{
            var matrix = Array(stick.toInt() + 1) { IntArray(diamond.toInt() + 1) }
            for (i in 1..stick){
                for (j in 1..diamond){
                    var numSticks = (i / 2).toInt()
                    when{
                        numSticks < j -> {
                            numSticks += matrix[(i - (numSticks * 2)).toInt()][(j - numSticks).toInt()]
                            if ((j - numSticks) > 1 && i.toInt() % 2 != 0){
                                numSticks ++
                            }
                        }
                        else ->{
                            numSticks = j.toInt()
                            numSticks += matrix[(i - numSticks).toInt()][0]
                        }
                    }
                    var numDiamonds = (j / 2).toInt()
                    when{
                        numDiamonds <= i -> {
                            numDiamonds += matrix[(i - numDiamonds).toInt()][(j - (numDiamonds * 2)).toInt()]
                            if ((i - numDiamonds) > 1 && j.toInt() % 2 != 0){
                                numDiamonds ++
                            }
                        }
                        else ->{
                            numDiamonds = i.toInt()
                            numDiamonds += matrix[0][(j - numDiamonds).toInt()]
                        }
                    }
                    matrix[i.toInt()][j.toInt()] = max(numSticks, numDiamonds)
                }
            }
            matrix[stick.toInt()][diamond.toInt()]
        }
    }
}

fun main(){
    val testCases = readLine()!!.toInt()
    for (i in 0 until testCases){
        val sticksAndDiamonds = readLine()!!.split(" ").map { it -> it.toLong() }
        println(solve(sticksAndDiamonds[0], sticksAndDiamonds[1]))
    }
}