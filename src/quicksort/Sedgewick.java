package quicksort;

import static quicksort.Utils.*;
import quicksort.Timer;

public class Sedgewick {

	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;
		shuffle(a);
		sort(a, 0, a.length - 1);
	}
	
	private static void sort(int[] a, int lo, int hi) {
		if (hi <= lo) return;
		
		int pivot = partition(a, lo, hi);
		sort(a, lo, pivot - 1);
		sort(a, pivot + 1, hi);
	}
	
	private static int partition(int[] a, int lo, int hi) {
		// sort method should pass in lo & hi with lo <= hi
		int i = lo;
		int j = hi + 1;
		int val = a[lo];
		
		while (true) {
			// R. Sedgewick's modification of Hoare's sweeps
			// stop on key equal to pivot value; this avoids quadratic run-time
			// when there are few keys (one sweep can go across most of the array if
			// sweep continues on values equal to pivot's)
			while ( a[++i] < val ) if ( i == hi) break ; // sweep from left end, stop when key >= val
			while ( a[--j] > val ) ; // sweep from right end, stop when key <= val
			
			if (i < j) 
				swap(a, i,j);
			else {  // eventually i >= j
				// partition always puts one element in sorted position,
				// guaranteeing termination of quicksort
				swap(a, j, lo);
				break;
			}
		}
		
		return j;
	}
	
	/* hybrid sort method: start with quicksort, but leave unsorted small arrays
	 * which are sorted all at once with insertion sort */
	public static void hybridSort(int[] a) {
		if (a == null || a.length == 0) return;
		shuffle(a);
		hybridSort(a, 0, a.length - 1);
		insertionSort(a);
	}
	
	private static void hybridSort(int[] a, int lo, int hi) {
		if (hi <= lo + 10) return;
		
		int pivot = partition(a, lo, hi);
		hybridSort(a, lo, pivot - 1);
		hybridSort(a, pivot + 1, hi);
	}
	
	
	public static void main(String[] args) {
		// log(n) stack space, so this is fine, but heap ran out
		//int[] a = getRandomArray(1000000000, 2);
		int[] a = getRandomArray(100000000, 100);
		int[] b = copyArray(a);
		
		Timer timer = new Timer();
		sort(a);
		Double elapsedTime = timer.getElapsedTime();
		System.out.println("Elapsed time : " + elapsedTime);
		
		Timer timer2 = new Timer();
		hybridSort(b);
		Double elapsedTime2 = timer2.getElapsedTime();
		System.out.println("Elapsed time : " + elapsedTime2);
		
		//printArray(a);
		System.out.println("\nSorted : " + validateSort(a));
		System.out.println("\nSorted : " + validateSort(b));


	}
	
}
