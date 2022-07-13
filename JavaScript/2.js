var a = 1, b = 1, c = 0, num;
while (b<4000000) {
    num = b
    b += a
    a = num
    if (b%2 === 0) {
        c += b
    }
}

window.alert(c)