#include<iostream>
using namespace std;

void BubbleSort(int *arr, int len){
    for(int i = 0; i < len; i++){
        bool flag = false;
        for(int j = 0; j < len-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j],arr[j+1]);
                flag = true;
            }
        }
        if(flag == false)break;
    }
}
void SelectionSort(int *arr, int len){
    for (int i = 0; i < len; i++){
        int min_index = i;
        for (int j = i+1; j < len; j++){
            if(arr[min_index] > arr[j]){
                min_index = j;
            }
        }
        swap(arr[i], arr[min_index]);
    }
}
void InsertionSort(int *arr, int len){

    int j = 0, key = 0;
    for (int i = 0; i < len; i++){
        key = arr[i];
        for (j = i-1; j >= 0 && arr[j] > key; j--){
            arr[j + 1] = arr[j];
        }
        arr[j+1] = key;
    }
}
void Display(int *arr, int len){
    for(int i = 0; i < len; i++){
        cout << arr[i] << " ";
    }
}
int main(){
    int Arr[7] = {7, 1, 6, 2, 5, 4, 8};
    int len = 7;

    //BubbleSort(Arr,len);
    //SelectionSort(Arr, len);
    InsertionSort(Arr, len);
    Display(Arr,len);
}