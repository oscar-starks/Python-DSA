/*
write an algorithm that performs a sum on a list of integers and 
stops summing through when it encounters a negative integer
*/

// create a function that accepts an array as a parameter
    // create a variable that will hold the values of the item in the array during each iteration and call it iteration_val
    // pass an array as argument
    // get the length of the array
    // create a for loop that loops using the length-1 of the array
    // counter increases by one in every iteration with the length-1 as the terminating value
        //if array[counter] > 0:
            // break
        //else:
            // iteration_val += array[counter]
            // print iteration_val
#include <iostream>
using namespace std;            

int iteration_val = 0;

int iteration(int arr[], int length){
    length -= 1;
    for(int i; i <= length; i++){
        int val = arr[i];
        int value = int(val);
        if(val < 0){
            break;
        }
        iteration_val += val;
        cout << iteration_val<<endl;
        
    }

}

int num1 = 0;
int num2 = 1;
int fibonnaci(int fib){
    cout << num1 << endl;
    cout << num2 << endl;
    fib -= 2;
    for(int i = 0; i < fib; i++){
       
        int ans = num1 + num2;

        cout << ans << endl;
        num1 = num2;
        num2 = ans;
       


    }
}
int main(){
    // int array[] = {2,3,4,-5,6};
    // iteration(array, 5);

    fibonnaci(5);
}





