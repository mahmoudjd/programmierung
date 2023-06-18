#include <stdio.h> 

int main () { 
  
  int n;

  printf("Enter a number:");
  scanf("%d",&n);

  for(int i = n; i > 0; i--) {

    for(int j = n; j > i; j--) {
      printf("  ");
    }
    for(int k = 0; k < i; k++) { 
      printf("%d ", i);
    }
    printf("\n");
  }
  return 0;

}
