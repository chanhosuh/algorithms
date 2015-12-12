package quicksort;

import static quicksort.Utils.*;

public class Sedgewick extends Hoare {

	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;
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
	
	
	public static void main(String[] args) {
		// log(n) stack space, so this is fine, but heap ran out
		//int[] a = getRandomArray(1000000000, 2);
		int[] a = getRandomArray(10000, 2);  //Number of calls: 61,622,708
		
		sort(a);
		//printArray(a);
		System.out.println("\n" + validateSort(a));
	}
	
}
