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
	
	public static int[] copyArray(int[] a) {
		int[] b = new int[a.length];
		for (int i = 0; i < a.length; i++) {
			b[i] = a[i];
		}
		return b;
	}
	
	public static boolean validateSort(int[] a) {
		if (a == null || a.length == 0 || a.length == 1 ) 
			return true;
		
	    for (int i = 1; i < a.length; i ++) {
	    	if ( a[i-1] > a[i] )
	    		return false;
	    }
	    
	    return true;
	}
	
	public static void shuffle(int[] a) {
		// Fischer-Yates shuffle
		
		for (int i = a.length - 1; i > 0 ; i--) {
			int j = rand.nextInt(i+1);
			swap(a, i, j);
		}
	}
	
	public static void setRandomPivot(int[] a, int lo, int hi) {
		if (a == null || a.length == 0) return;
		int p = rand.nextInt(hi - lo + 1) + lo;
		swap(a, lo, p);
	}
	
	public static void insertionSort(int[] a) {
		if (a == null || a.length == 0) return;
		
		for (int i = 1; i < a.length; i++) {
			int unsorted = a[i]; // a[0:i-1] is sorted
			int j = i;
			while (j > 0 && a[j-1] > unsorted) {
				a[j] = a[j-1];
				j--;
			}
			a[j] = unsorted; 
		}
	}
	
}


