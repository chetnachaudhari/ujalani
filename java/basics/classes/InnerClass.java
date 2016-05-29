public class InnerClass {
  public static void main(String[] args) {
    OuterClass outerClass = new OuterClass();
    outerClass.displayInnerClass();
  }
}
class OuterClass {
  int num = 100;

  void displayInnerClass() {
    InnerClass innerClass = new InnerClass();
    innerClass.print();
    innerClass.getNum();
  }

  // Notice: We can reuse classname for inner class
  private class InnerClass {
    public void print() {
      System.out.println("Inside inner class");
    }

    public void getNum() {
      System.out.println("Num = " + num);
    }
  }
}
