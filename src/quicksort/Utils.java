package quicksort;

import java.util.Random;

public class Utils {
	
	public static void swap(int[] a, int i, int j) {
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
	
	static final Random rand = new Random();
	public static int getRandomInt(int size) {
		return rand.nextInt(size + 1);
	}
	
	public static int[] getRandomArray(int arrayLength, int intSize) {
		int[] a = new int[arrayLength];
		for (int i = 0; i < arrayLength; i++) {
			a[i] = getRandomInt(intSize);
		}
		return a;
	}
	
	public static void printArray(int[] a) {
		if (a == null || a.length == 0) return;
		for ( int x : a) {
			System.out.print(x + " ");
		}
	}
	
	public static boolean validateSort(int[] a) {
		if (a == null || a.length == 0 || a.length == 1 ) return true
				;
	    for (int i = 1; i < a.length; i ++) {
	    	if ( a[i-1] > a[i] )
	    		return false;
	    }
	    
	    return true;
	}

}
