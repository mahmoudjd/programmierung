#include <stdio.h>

void numbers(int n) { 
  for (int i = 1; i <= n; i++) { 
    for (int j = n; j >= 1; j--) {
      if (i >= j) {
        printf("%d ", i);
      } else { 
        printf(" ");
      }
    }
    printf("\n");
  }
}

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

  printf("\n");

  numbers(9);
  return 0;
}
