var max = 0;
for (i=100;i<1000;i++){
    for (j=100;j<1000;j++){
        var s;
        s = i * j
        temp = s
        rev = 0
        while (s >0){
            var dig = s%10
            rev = rev*10+dig
            s = Math.floor(s/10)
            if (temp === rev & temp > max){
                max = temp
            }
        }
    }
}
console.log(max)