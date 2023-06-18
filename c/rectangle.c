#include <stdio.h> 

int main () { 
  for (int row = 0; row < 10; row++) { 
    for (int col = 10; col > 0; col--) { 
      if (row - col > 0) { 
        printf(" *");
      } else {
        printf(" ");
      }
    }
    printf("\n");
  }
  return 0;
}
