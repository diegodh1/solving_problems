//link to the problem https://codeforces.com/problemset/problem/1398/B

fun solve(game:String):Int{
    val charList = game.toMutableList();
    var turn:Boolean = true
    var aliceScore:Int = 0
    val onesList:MutableList<Int> = mutableListOf()
    var count:Int = 0;
    for (i in charList.indices){
        //count the consecutive ones
        if(charList[i] == '1'){
            count++;
        }
        else{
            if (count > 0){
                onesList.add(count)
            }
            count = 0;
        }
    }
    if (count > 0){
        onesList.add(count)
    }
    //iterate over the ones
    val maxConsOnes = onesList.sortedDescending()
    for(i in maxConsOnes){
        if(turn){
            aliceScore += i;
        }
        turn = !turn;
    }
    return aliceScore;
}

fun main() {
    // read input
    val n:Int = readLine()!!.toInt()
    var game:String;
    for (i in 0 until n){
        game = readLine()!!;
        println(solve(game));
    }
}
