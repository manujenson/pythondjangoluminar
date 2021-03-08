
//while

let i=0;
while(i<10){
    console.log(i);
    i++
}
//
//odd or even1-50
let i=0;
while(i<=50){
    if(i%2==0){
        console.log(`number ${i} is even`);

    }
    else{
        console.log(`number ${i} is odd`);
    }
}

//for loop

for(let i=0;i<=10;i++){
    console.log(i);
}

//prime no
var num=17;
var flag=0;
for(let i=2;i<num;i++){
    if(num%i==0){
        flag+=1;
        break
    }
    else{
        flg=0;
    }
}
if(flag==0){
    console.log("prime");
}
else{
    console.log("not prime");
}