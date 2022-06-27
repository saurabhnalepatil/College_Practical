#include<iostream>
using namespace std;

void SelectionSort(int arr[], int size){
    
    int j = 0;
    for(int i = 0; i < size-1; i++){
        int min_index = i;
        for(j = i+1; j < size; j++){
            if(arr[j] < arr[min_index]){
                min_index = j;
            }
        }
        swap(arr[min_index],arr[i]);
    }
    cout<<"Selection Sort is : "<<endl;
}

void DisplaySortArr(int arr[], int size){
    for(int i = 0; i < size; i++){
        cout<<arr[i]<<" ";
    }
    cout<<"\n"<<endl;
}

int main(){
    int even[7] = {8, 2, 4, 3, 5, 9, 1};

    SelectionSort(even,7);
    DisplaySortArr(even,7);
}