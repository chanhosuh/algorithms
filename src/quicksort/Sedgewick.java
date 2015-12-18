package quicksort;

import static quicksort.Utils.*;

import java.util.concurrent.TimeUnit;

import org.openjdk.jmh.Main;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;


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
	
	public static void sortWithSentinels(int[] a) {
		if (a == null || a.length == 0) return;
		shuffle(a);
		sortWithSentinels(a, 0, a.length - 1);
	}
	
	private static void sortWithSentinels(int[] a, int lo, int hi) {
		if (hi <= lo) return;
		
		// ensure that a[lo] <= a[hi], so that we don't fall off the ends
		// during Sedgewick-type sweeps
		if (a[lo] > a[hi]) swap(a, lo, hi);
		
		int pivot = partitionWithSentinels(a, lo, hi);
		sortWithSentinels(a, lo, pivot - 1);
		sortWithSentinels(a, pivot + 1, hi);
	}
	
	private static int partitionWithSentinels(int[] a, int lo, int hi) {
		// sort method should pass in lo & hi with lo <= hi
		int i = lo;
		int j = hi + 1;
		int val = a[lo];
		
		while (true) {
			// R. Sedgewick's modification of Hoare's sweeps
			// stop on key equal to pivot value; this avoids quadratic run-time
			// when there are few keys (one sweep can go across most of the array if
			// sweep continues on values equal to pivot's)
			while ( a[++i] < val ) ; // sweep from left end, stop when key >= val
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
	
	@Benchmark
	public static boolean testSort() {
		int[] a = getRandomArray(100000000, 1000);

		sort(a);
		
		return validateSort(a);

	}
	
	@Benchmark
	public static boolean testSortWithSentinels() {
		int[] a = getRandomArray(100000000, 1000);

		sortWithSentinels(a);
		
		return validateSort(a);

	}
	
	@Benchmark
	public static boolean testHybridSort() {
		int[] a = getRandomArray(100000000, 1000);

		hybridSort(a);
		
		return validateSort(a);

	}
	
    
    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder()
                .include(Sedgewick.class.getSimpleName())
                .warmupIterations(5)
                .measurementIterations(10)
                .mode(Mode.AverageTime)
                .timeUnit(TimeUnit.MILLISECONDS)
                .forks(1)
                .build();
 
        new Runner(opt).run();

//        # Benchmark: quicksort.Sedgewick.testHybridSort
//
//        Result "testHybridSort":
//          21598.849 ±(99.9%) 1119.697 ms/op [Average]
//          (min, avg, max) = (21116.605, 21598.849, 23568.521), stdev = 740.610
//          CI (99.9%): [20479.152, 22718.546] (assumes normal distribution)
//
//        # Benchmark: quicksort.Sedgewick.testSort
//
//        Result "testSort":
//          21116.172 ±(99.9%) 621.166 ms/op [Average]
//          (min, avg, max) = (20684.254, 21116.172, 21808.136), stdev = 410.863
//          CI (99.9%): [20495.006, 21737.339] (assumes normal distribution)
//
//        # Benchmark: quicksort.Sedgewick.testSortWithSentinels
//
//        Result "testSortWithSentinels":
//          21624.132 ±(99.9%) 665.105 ms/op [Average]
//          (min, avg, max) = (20740.663, 21624.132, 22343.349), stdev = 439.926
//          CI (99.9%): [20959.028, 22289.237] (assumes normal distribution)
//
//
//        # Run complete. Total time: 00:16:03
//
//        Benchmark                        Mode  Cnt      Score      Error  Units
//        Sedgewick.testHybridSort         avgt   10  21598.849 ± 1119.697  ms/op
//        Sedgewick.testSort               avgt   10  21116.172 ±  621.166  ms/op
//        Sedgewick.testSortWithSentinels  avgt   10  21624.132 ±  665.105  ms/op

    }
	
//	public static void main(String[] args) throws Exception {
//	     Main.main(args);
//	}
//	
}
