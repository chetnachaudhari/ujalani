/** Static class - can be accessed without instantiating parent class.
 * It does not have access to instance variables and methods of outside class.
 */
public class StaticNestedClass {
  int num = 1000;
  static class TestClass {
    public void print() {
      System.out.println("Inside static nested class");
    }

//    Following method will not work.
//    public void printNum() {
//      System.out.println("Num = " + num);
//    }
  }

  public static void main(String[] args) {
    TestClass testClass = new TestClass();
    testClass.print();
  }
}
