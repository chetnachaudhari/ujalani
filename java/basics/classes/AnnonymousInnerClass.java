/** Annonymous inner class :
 * 1. Inner class declared without a name
 * 2. Declared and instantiated at the same time
 * 3. Used when there is need to override a method of class or interface
 */
abstract class AnnonymousInner {
  public abstract void testMethod();
}

interface Message {
  String greet();
}
public class AnnonymousInnerClass {
  public static void main(String[] args) {
    AnnonymousInner annonymousInner = new AnnonymousInner() {
      @Override
      public void testMethod() {
        System.out.println("Here is annonymous inner class.");
      }
    };
    annonymousInner.testMethod();

    // Annonymous inner class as a parameter.
    AnnonymousInnerClass annonymousInnerClass = new AnnonymousInnerClass();
    annonymousInnerClass.greetPeople(new Message() {
      @Override
      public String greet() {
        return "Good Morning ";
      }
    });
  }

  public void greetPeople(Message message) {
    System.out.println(message.greet() + "all");
  }
}
