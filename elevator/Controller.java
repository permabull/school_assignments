import java.util.Scanner;


public class Controller{

  private int nFloorsToTravel = 0;

  Elevator n = new Elevator(100, 0, "robbans hiss");

  //When you arrive at your floor you can choose to exit(exits the program). Or keep traveling.
  public boolean exitElevator(){
    String choice = "";
    System.out.println("Do you wish to exit at this floor press E");
    System.out.println("Otherwise press the Anybutton");

    Scanner sc = new Scanner(System.in);

    try { choice = sc.nextLine().toLowerCase(); }
    catch(Exception e){}

    if(choice.equals("e")){
      return true;
    }
    return false;
  }

  public void nToTravel(){
    boolean correctFloor = false;
    int choice = 0;
    Scanner sc = new Scanner(System.in);

    //The while loop will run until it gets a good input that doesen't violate the minimum or maximum floor.
    while(correctFloor == false){
      System.out.println("*  Current floor " + n.getCurrentFloor() +"  * "+ " Max Floor : " + n.getMaxFloor() + "\n");
      System.out.println("What floor sir?");

      //Try input for an int, otherwise make another try or exit.
      try { choice = sc.nextInt(); n.setDesiredFloor(choice); }
      catch(Exception e){ System.out.println("Not a valid choice");}

      if(n.getDesiredFloor() < n.getMinFloor()){
        n.errorMessageDown();
      }
      else if(n.getDesiredFloor() > n.getMaxFloor()){
        n.errorMessageUp();
      }
      else{
        correctFloor = true;
      }
    }
  }

  //This method checks if you wanna go up or down depending on where your current location is.
  public void goUpOrDown(){
    if (n.getCurrentFloor() > n.getDesiredFloor()){
      this.nFloorsToTravel = n.getCurrentFloor() - n.getDesiredFloor();
      n.goDown(nFloorsToTravel);
      System.out.println("\n* You arrived at floor " + n.getCurrentFloor() +" *"+ "\n");
    }
    else if (n.getCurrentFloor() < n.getDesiredFloor()){
      this.nFloorsToTravel =  n.getDesiredFloor() - n.getCurrentFloor();
      n.goUp(nFloorsToTravel);
      System.out.println("\n* You arrived at floor " + n.getCurrentFloor() +" *"+ "\n");
    }
  }

  public static void main(String[] args) {

    boolean runElevator = true;

    Controller c = new Controller();

    while(runElevator == true){
      //This "clears" the screen to make the program less messy, but it doesent work on windows so remove the comment if you are on linux/mac
      //System.out.print("\033[H\033[2J");
      c.nToTravel();
      c.goUpOrDown();

        if(c.exitElevator() == true){
          System.out.println("Bye Bye");
          runElevator = false;
        }
        else{
          continue;
      }
    }
 }
}
