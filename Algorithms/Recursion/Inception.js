let counter = 0;
function inception() {
    debugger;
    console.log(counter);
    if (counter > 3) {
        return 'done!';
    }
    counter++;
    return inception();
}

inception();

// 1. identify base case.
// 2. identify recursive case.
// 3. return when needed - usually 2 returns.