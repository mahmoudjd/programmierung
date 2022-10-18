#include <stdio.h>

int main() { 
  int n = 15;
  for(int i = 0; i < n; i++) { 
    for(int j = n; j > 0; j--) { 
      if (i >= j) { 
        printf(" *");
      } else { 
        printf(" ");
      }
    }
    printf("\n");
  }
  return 0;
}
