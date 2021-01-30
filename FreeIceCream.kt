//LINK TO THE PROBLEM https://codeforces.com/problemset/problem/686/A
fun main(){
    var inputs = readLine()!!.split(" ").map { it -> it.toLong() }.toMutableList()
    var distress = 0
    for (i in 0 until inputs[0]){
        val child = readLine()!!.split(" ")
        if (child[0] == "+"){
            inputs[1] += child[1].toLong()
        }
        else{
            if (child[1].toLong() > inputs[1]){
                distress++
            }
            else{
                inputs[1] -= child[1].toLong()
            }
        }
    }
    println("${inputs[1]} $distress")
}