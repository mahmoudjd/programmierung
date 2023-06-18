#include <stdio.h> 

int main () { 

  for (int row = 0; row < 6; row++) { 
    for (int col = 0; col < 7; col++) { 
      if ((row==0 && col%3!= 0) || (row==1 && col%3==0) || (row-col==2) || (row+col== 8)) { 
        printf(" * ");
      } else { 
        printf("  ");
      }
    }
    printf("\n"); 
  }

  return 0;
}
