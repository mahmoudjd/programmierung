public class Heart {

  public static void main(String[] args) { 
    for(int row = 0; row < 10 ; row++) { 
      for(int col = 10; col > 0; col--) {
        if (row - col > 0) { 
          System.out.print(" *");
        } else { 
          System.out.print(" ");
        }
      }
      System.out.println();
    }
  }
}
