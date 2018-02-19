/*
 * https://www.acmicpc.net/problem/2156
 * DP - Using 2-D(numOfGlasses*3) list 
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class WineDp {

  int numOfGlasses;
  List<Integer> glassQty = new ArrayList<>();
  List<List<Integer>> totalQty = new ArrayList<List<Integer>>();
  
  private void inputDatas() {
    Scanner scan = new Scanner(System.in);
    numOfGlasses = scan.nextInt();
    for(int i=0; i<numOfGlasses; i++) {
      glassQty.add(scan.nextInt());
    }
  }
  
  private void calWineQty() {
    totalQty.add(Arrays.asList(0,glassQty.get(0), glassQty.get(0)));
    
    for(int i=1; i<numOfGlasses; i++) {
      List<Integer> beforeQty = totalQty.get(i-1);
      int maxOfBefore = Collections.max(beforeQty);
      List<Integer> nowQty = Arrays.asList(maxOfBefore, beforeQty.get(0)+glassQty.get(i), beforeQty.get(1)+glassQty.get(i));
      totalQty.add(nowQty);
    }
  }
  
  private int getWineQty() {
    return Collections.max(totalQty.get(numOfGlasses-1));
  }
  
  public static void main(String[] args) {
    WineDp wp = new WineDp();
    wp.inputDatas();
    wp.calWineQty();
    int result = wp.getWineQty();
    System.out.println(result);

  }

}
