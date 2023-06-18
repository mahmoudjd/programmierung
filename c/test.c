#include <stdio.h>
void print(char* s) { 
  printf("%s", s);
}
int main () { 
 /*
  for(int row = 0; row < 6; row++) { 
    for(int col = 0; col< 7; col++) {
      if((row==0 && col%3 != 0) || (row==1 && col%3==0) || (row-col ==2) || (row+col==8)) {
        printf(" * ");
      } else { 
        printf("  ");
      }
    }
    printf("\n");
  }
  */
  for(int row= 0 ; row < 5; row++) { 
    for (int col= 0; col < 5; col++) { 
      if(col == 0 || row == 0 || row == 4 || col == 4) { 
        print(" *");
      } else { 
        print("  ");
      }
    }
    print("\n");
  }
}
