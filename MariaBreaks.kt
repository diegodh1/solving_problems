//main function
data class Granie(var key: Int, var value: Int);
fun main(){
    //read the size of tests
    val n:Int = readLine()!!.toInt();
    for (i in 0 until n){
        val listSize :Int = readLine()!!.toInt();
        var grannies:List<Int> = readLine()!!.split(" ").map{ it -> it.toInt()};
        grannies = grannies.sorted();
        val listGrannies: MutableList<Granie> = mutableListOf();
        var numGrannies:Int = 1;
        var count = 1;
        for(i in 0..listSize){
            if(i == listSize){
                listGrannies.add(Granie(numGrannies, count));
                break
            }
            else if (numGrannies == grannies[i]){
                count++;
            }
            else{
                listGrannies.add(Granie(numGrannies, count));
                count = 1;
                numGrannies = grannies[i];
            }
        }

        var maxGrannies = if (listGrannies[0].value == 1) 1 else {
            var result = listGrannies[0].value;
            for (i in 1 until listGrannies.size) {
                if (listGrannies[i].key <= (listGrannies[i - 1].value + listGrannies[i].value) && listGrannies[i].value > 1) {
                    result = (listGrannies[i].value + listGrannies[i - 1].value);
                } else if (listGrannies[i].key <= (listGrannies[i - 1].value)) {
                    result = (listGrannies[i].value + listGrannies[i - 1].value);
                }
                listGrannies[i].value = (listGrannies[i].value + listGrannies[i - 1].value);
            }
            result
        }
        println(maxGrannies)
    }
}