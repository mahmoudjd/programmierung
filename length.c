#include <stdio.h>
int length(char input[]) { 
  int i = 0;
  while(input[i]!= '\0') {
      i++;
  }
  return i;
}

int main(int argc, const char*argv[]) { 
  if (argc > 0) { 
    printf("Length is %d\n", length((const char*)argv[1]));
  }
  return 0;
}
