package mergesort;


public class MergeSort {
	
	public static void sort(int[] a){
		if (a == null || a.length == 0) return;

		int[] temp = new int[a.length];
		int lo = 0;
		int hi = a.length-1;
		sort(a, lo, hi, temp);
	}
	
	public static void sort(int[] a, lo, hi, int[] temp) {
		// preconditions: 0 <= lo <= hi <= a.length -1;
		// a.length == temp.length;
		if (hi <= lo) return;
		
		int mid = lo + (hi-lo)/2;
		
		sort(a, lo, mid, temp);
		sort(a, mid+1, hi, temp);
		merge(a, lo, hi, temp);
	}
	
	private static void merge(int[] a, int[] temp, lo, hi){
		copy(a, temp, lo, hi);  // copy a[lo:hi] to temp[lo:hi]
		
		// now merge from temp to a
		int mid = lo + (hi-lo)/2;
		int i = lo;
		int j = mid+1;
		for (int n=lo; n <= hi; n++) {
			if (i > mid) // left half empty
				a[n] = temp[j++];
			else if (j> hi) // right half empty
				a[n] = temp[i++];
			else if (temp[i] <= temp[j])
				a[n] = temp[i++];
			else
				a[n] = temp[j++];
		}
	}
	
	private static void copy(a, temp, lo, hi){
		for (int i = lo; i <= hi; i++)
			temp[i] = a[i];
	}
	
	
	public static void main(String[] args){
		
	}
}