/**
* This is my simpel elevator simulation.
* The program has an Elevator class and a Controller class.
* It runs from the Controller class which creates an instance of Elevator.
*
* I have no Scanner.close() methods and I dont get yellow warnings, but I read that if you have them in a try/catch it closes on auto?
*
* @author  Robert Sundh
* @version 1.0
*/

import java.util.concurrent.TimeUnit;

public class Elevator{

  private int currentFloor = 0;
  private int desiredFloor = 0;
  private int maxFloor = 0;
  private int minFloor = 0;
  private String elevatorName = "";

  //Constructor for the Elevator instance.
  public Elevator(int maxFloor, int minFloor, String elevatorName){
    this.maxFloor = maxFloor;
    this.elevatorName = elevatorName;
    this.minFloor = minFloor;
  }

  public void errorMessageUp(){
    System.out.println("Cant go that high. Maxfloor is " + this.maxFloor + "\n");
  }

  public void errorMessageDown(){
    System.out.println("Cant go that low. Minfloor is " + this.minFloor + "\n");
  }

  //Method to make the elevator go up.
  public void goUp(int nFloorsToTravel){
    while(getCurrentFloor() != desiredFloor){
      System.out.println("Pling .. at floor --> " + (getCurrentFloor()+1));
      try {TimeUnit.MILLISECONDS.sleep(100);} catch (InterruptedException e) {e.printStackTrace();}
      setCurrentFloor(getCurrentFloor()+1);
    }
  }

  //Method to make the elevator go down.
  public void goDown(int nFloorsToTravel){
    while(getCurrentFloor() != desiredFloor){
      System.out.println("Pling..! " + (getCurrentFloor()-1));
      try {TimeUnit.MILLISECONDS.sleep(100);} catch (InterruptedException e) {e.printStackTrace();}
      setCurrentFloor(getCurrentFloor()-1);
    }
  }

  public int getCurrentFloor(){
    return this.currentFloor;
  }

  public void setCurrentFloor(int currentFloor){
    this.currentFloor = currentFloor;
  }

  public int getDesiredFloor(){
    return this.desiredFloor;
  }

  public void setDesiredFloor(int desiredFloor){
    this.desiredFloor = desiredFloor;
  }

  public int getMaxFloor(){
    return this.maxFloor;
  }

  public int getMinFloor(){
    return this.minFloor;
  }
}
