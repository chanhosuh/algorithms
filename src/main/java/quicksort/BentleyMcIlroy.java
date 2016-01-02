package quicksort;

import static quicksort.Utils.*;


public class BentleyMcIlroy {
	
	private static final int CUTOFF = 10;

	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;
		sort(a, 0, a.length - 1);
		insertionSort(a);
	}
	
	private static void sort(int[] a, int lo, int hi) {
		if (hi <= lo + CUTOFF) return;
		
		int[] indices = partition(a, lo, hi);
		
		sort(a, lo, indices[0]);
		sort(a, indices[1], hi);
	}
	
	private static int[] partition(int[] a, int lo, int hi) {
		// sort method should pass in lo & hi with lo <= hi

		// swap random element to index lo
		setRandomPivot(a, lo, hi);
		int val = a[lo];

		int i = lo; 
		int j = hi + 1; 
		int p = lo + 1; // new space for key == val
		int q = hi; // new space for key == val
		
		while (true) {
			while ( a[++i] < val ) if ( i == hi) break ;
			while ( a[--j] > val ) if ( j == lo) break ;
			
			if (i < j) {
				swap(a, i, j);
				if (a[i] == val) swap(a, i, p++); // swap eq key to left end
				if (a[j] == val) swap(a, j, q--); // swap eq key to right end
			}
			else { // eventually i >= j
				if (a[j] < val) swap(a, j, lo); // make sure a[j] is in sorted position
				break;
			}
		}
		// a[lo + 1, p), a(q, hi] has eq keys (possibly a[lo] is a < key now)
		// a[p, j) has < keys
		// a[j] is eq (sorted)
		// a[j + 1, q] has > keys
		
		i = j-1;
		j = j+1;

		/* swap < and > keys to ends and eq keys to middle */
		
		// precondition: a[lo+1, p) has eq keys, a[p,i] has < keys
		for (int k = lo+1; k < p; k++) {
			swap(a, k, i);
			i--;
		} // postcondition: a[lo+1, i] has all the < keys
		
		// precondition: a(q, hi] has eq keys, a[j, q] has > keys
		for (int k = hi; k > q; k--) {
			swap(a, k, j);
			j++;
		} // postcondition: a[j, hi] has all the > keys
		
		return new int[] {i, j};
	}
	
	
	public static void main(String[] args) {
		for (int i = 2; i < 100000; i *= 2) {
			int[] a = getRandomArray(10000000, i);
			Timer timer = new Timer();
			sort(a);
			double elapsedTime = timer.getElapsedTime();
			System.out.println("#keys: " + i + ", sorted: " + validateSort(a) 
								+ ", time: " + elapsedTime + " seconds");
		}
	}
	

}
