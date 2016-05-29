/** Method Local Inner Class:
 * 1. Class defined inside a method.
 * 2. This class is local to the method, and can be instantiated only within the method.
**/
public class MethodLocalInnerClass {
  void testMethod() {
    class MethodLocalClass {
      public void print() {
        System.out.println("We are inside Method local inner class");
      }
    }
    MethodLocalClass methodLocalClass = new MethodLocalClass();
    methodLocalClass.print();
  }

  public static void main(String[] args) {
    MethodLocalInnerClass methodLocalInnerClass = new MethodLocalInnerClass();
    methodLocalInnerClass.testMethod();
  }
}
