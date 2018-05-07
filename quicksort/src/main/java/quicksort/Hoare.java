package quicksort;


import static quicksort.Utils.*;


public class Hoare {
		
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
		// swap random element to index lo
		setRandomPivot(a, lo, hi);
		int val = a[lo];

		// sort method should pass in lo & hi with lo <= hi
		int i = lo;
		int j = hi + 1;
		
		while (true) {
			// original Hoare conditions for ending sweeps, cf
			// Hoare, Charles AR. "Quicksort." The Computer Journal 5.1 (1962): 10-16.
			while ( a[++i] <= val ) if ( i == hi) break ; // sweep from left end, stop when key > val
			while ( a[--j] >= val ) if ( j == lo) break ; // sweep from right end, stop when key < val
			
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
		// easily blows the stack
		//int[] a = getRandomArray(1000000, 2);
		int[] a = getRandomArray(10000, 50);
		
		sort(a);
		//printArray(a);
		System.out.println("\n" + validateSort(a));
	}
	

}
