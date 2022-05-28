function deepGet(arr) {
    let deep = arr.length;
    for (let item of arr) {
        if (Array.isArray(item)) {
            deep += deepGet(item);
        }
    }
    return deep;

}

console.log(deepGet([0, 1, 2, 3, [10]]));