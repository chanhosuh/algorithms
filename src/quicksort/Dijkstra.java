package quicksort;

import static quicksort.Utils.*;
import quicksort.Timer;

public class Dijkstra {
	
	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;
		sort(a, 0, a.length - 1);
	}
	
	private static void sort(int[] a, int lo, int hi) {
		if (hi <= lo) return;
		
		int[] pivots = partition(a, lo, hi);
		sort(a, lo, pivots[0]);
		sort(a, pivots[1], hi);
	}
	
	// Dijkstra's 3-way partitioning: keys < val, keys == val, keys > val
	private static int[] partition(int[] a, int lo, int hi) {
		// sort method should pass in lo & hi with lo <= hi
		int lt = lo; // space for key < val
		int gt = hi; // space for key > val
		int eq = lo; // space for key == val
		
		int val = a[lo];
		while(eq <= gt) {
			if (a[eq] < val) swap(a, eq++, lt++); // increase "<" section and shift "=" section
			else if (a[eq] > val) swap(a, eq, gt--); // increase ">" section
			else eq++; // key == val, increase "equals" section
		}
		return new int[]{lt - 1, gt + 1};
	}
	
	public static void main(String[] args) {
		// 2-way partitioning (Sedgewick) Elapsed time : 16.844911082
		// 3-way partitioning (Dijkstra) Elapsed time : 0.738166288
		int[] a = getRandomArray(100000000, 2);
		Timer timer = new Timer();
		
		sort(a);
		Double elapsedTime = timer.getElapsedTime();
		System.out.println("Elapsed time : " + elapsedTime);
		//printArray(a);
		System.out.println("\nSorted : " + validateSort(a));
		

	}
}
