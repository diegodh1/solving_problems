//link to the problem https://codeforces.com/problemset/problem/1391/B
fun main(){
    val testCases = readLine()!!.toInt()
    for (i in 1..testCases){
        val dimensions = readLine()!!.split(" ").map { it -> it.toInt() }
        var right = 0
        var down = 0
        for (k in 0 until dimensions[0]){
            if (k != dimensions[0] -1){
                val value = readLine()!!
                if (value[value.length - 1]!='D'){
                    down++
                }
            }
            else{
                val value = readLine()!!
                for (j in 0 until value.length - 1){
                    if (value[j] != 'R'){
                        right++
                    }
                }
            }
        }
        println("${right+down}")
    }
}