import java.util.*;

public class MontyHall{
	
	static final byte doorOptions[] = {0, 1, 2};
	static final byte MIN_DOOR_INDEX = 0;
	static final byte MAX_DOOR_INDEX = 2;
	
	static private Random rnd = new Random();

	public static boolean play(boolean change) {
		
		byte doors[] = {1, 0, 0};
		Collections.shuffle(Arrays.asList(doors));
		
		byte chosenDoor = (byte) (Math.random() * (MAX_DOOR_INDEX - MIN_DOOR_INDEX + 1));
		
		byte otherDoors[] = new byte[2];
		int i = 0;
		for (byte door : doorOptions) {
			if (door != chosenDoor) { 
				otherDoors[i++] = door;	
			} 
		}	
	
		byte prizeDoor = -1;
		for (byte door : doorOptions) {
			if (doors[door] == 1) {
				prizeDoor = door;
				continue;
			}
		}
		
		byte revealDoor = -1;
		if (Arrays.binarySearch(otherDoors, prizeDoor) < 0) {
			revealDoor = otherDoors[rnd.nextInt(otherDoors.length)];
		}
		else {
			for (byte door: otherDoors) {
				if (door != prizeDoor) {
					revealDoor = door;
				}
			}
		}
	
		if (change) {
			for (byte door : otherDoors) {
				if (door != revealDoor) {
					chosenDoor = door;
				}
			}
		}
		
		boolean ret = doors[chosenDoor] == 1? true : false;
		return ret;
		
	}
	
	public static void main(String args[]) {
		
		long win = 0;
		long games = 200000000;
		
		for (int game=0; game < games; game++) {
			if (play(true)) {
				win++;
			}
		}
		
		System.out.println("Probability of winning if switched door after reveal = " + ((double) (win * 100) / (double) games));
		
	}
}
