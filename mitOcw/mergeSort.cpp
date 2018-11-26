#include <stdio.h>
#define MAX 99999999

using namespace std;

void print(int* arr, int len) {
    printf("============================\n");
    for(int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n============================\n");
}

void merge(int a[], int p, int q, int r){
	int n1 = q - p + 1;
	int n2 = r - q;

	int *left = new int[n1 + 1];
	int *right = new int [n2 + 1];
	int i = 0;
	int j = 0;

	for (i = 0; i < n1; i++)
		left[i] = a[p + i];
	for (j = 0; j < n2; j++)
		right[j] = a[q + 1 + j];

	left[n1] = MAX;
	right[n2] = MAX;

	print(left, n1 + 1);
	print(right, n2 + 1);

	i = 0;
	j = 0;
	for (int k = p; k <= r; k++){
		if (left[i] <= right[j]){
			a[k] = left[i];
			i++;
		}
		else{
			a[k] = right[j];
			j++;
		}
	}
}


void mergeSort(int a[], int p, int r){
	if (p < r){
		int q = (p + r) / 2;
		mergeSort(a, p, q);
		mergeSort(a, q + 1, r);
		merge(a, p, q, r);
	}
	return;
}


int main(){
	int a[] = { 1, 2, 3, 6, 5, 4 };
	mergeSort(a, 0, 5);
	print(a, 6);
    return 0;
}
