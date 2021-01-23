//LINK TO THE PROBLEM: https://codeforces.com/problemset/problem/1454/B
fun main(){
    val testCase = readLine()!!.toInt()
    var participants:Int
    var numbers:MutableList<String> = mutableListOf()
    for (i in 0 until testCase){
        participants = readLine()!!.toInt()
        numbers = readLine()!!.split(" ") as MutableList<String>
        val mapParticipants = mutableMapOf<String, MutableList<Int>>()
        //add elements to map struct
        for (j in 0 until participants){
            val list = mapParticipants[numbers[j]]?: mutableListOf()
            list.add(j)
            mapParticipants[numbers[j]] = list
        }
        //get min
        var index:Int = -1
        var minValue:Int = Int.MAX_VALUE
        for ((k, v) in mapParticipants){
            if (v.size == 1 && k.toInt() < minValue){
                minValue = k.toInt()
                index = v[0] + 1
            }
        }
        println(index)
    }
}