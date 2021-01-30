//LINK TO THE PROBLEM https://codeforces.com/problemset/problem/1304/A
fun main(){
    val testCases = readLine()!!.toInt()
    var inputs:List<Long>
        for(i in 1..testCases){
            inputs = readLine()!!.split(" ").map { it -> it.toLong() }
            if ((inputs[1] - inputs[0])%(inputs[2] + inputs[3]) == 0L){
                println((inputs[1] - inputs[0])/(inputs[2] + inputs[3]))
            }
            else{
                println("-1")
            }
    }
}