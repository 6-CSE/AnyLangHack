function bubbleSort(arr){
   
  var i, j;
  var len = arr.length;
   
  var isSwapped = false;
   
  for(i =0; i < len; i++){
     
    isSwapped = false;
     
    for(j = 0; j < len; j++){
        if(arr[j] > arr[j + 1]){
          var temp = arr[j]
          arr[j] = arr[j+1];
          arr[j+1] = temp;
          isSwapped = true;
        }
    }
          
    if(!isSwapped){
      break;
    }
  }
   
  console.log(arr)
}