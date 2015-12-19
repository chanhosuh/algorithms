package quicksort;


import static quicksort.Utils.*;

import java.util.concurrent.TimeUnit;

import org.openjdk.jmh.Main;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.Level;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.Setup;
import org.openjdk.jmh.annotations.State;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

@State(Scope.Benchmark)
public class Sedgewick {

	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;
		// for benchmarking, we use random array so we can skip the shuffle...
		// shuffle(a);  
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
		// for benchmarking, we use random array so we can skip the shuffle...
		// shuffle(a); 
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
		// for benchmarking, we use random array so we can skip the shuffle...
		// shuffle(a); 
		hybridSort(a, 0, a.length - 1);
		insertionSort(a);
	}
	
	private static void hybridSort(int[] a, int lo, int hi) {
		if (hi <= lo + 10) return;
		
		int pivot = partition(a, lo, hi);
		hybridSort(a, lo, pivot - 1);
		hybridSort(a, pivot + 1, hi);
	}
	
	/*  State : Random array to be sorted */
	
	@SuppressWarnings("unused")
	public int[] randomArray;
	
	@Setup(Level.Invocation)
	public void initializeRandomArray() {
		randomArray = getRandomArray(100000, 100);
		shuffle(randomArray);
	}
	
	/* * * * * * * * * * * * * * * * * */
	
	@Benchmark
	public boolean testSort() {

		sort(randomArray);
		
		return validateSort(randomArray);

	}
	
	@Benchmark
	public boolean testSortWithSentinels() {

		sortWithSentinels(randomArray);
		
		return validateSort(randomArray);

	}
	
	@Benchmark
	public boolean testHybridSort() {

		hybridSort(randomArray);
		
		return validateSort(randomArray);

	}
	
//    @Benchmark
//    public int testShuffle() {
//		shuffle(randomArray);
//		return randomArray[0] + randomArray[101];
//    }
    
    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder()
                .include(Sedgewick.class.getSimpleName())
                .warmupIterations(5)
                .measurementIterations(25)
                .mode(Mode.AverageTime)
                .timeUnit(TimeUnit.MILLISECONDS)
                .forks(1)
                .shouldFailOnError(true)
                .shouldDoGC(true)
                .jvmArgs("-server")
                .build();
 
        new Runner(opt).run();

//		randomArray = getRandomArray(100000, 100);
//        Benchmark                        Mode  Cnt  Score   Error  Units
//        Sedgewick.testHybridSort         avgt   25  4.604 ± 0.065  ms/op
//        Sedgewick.testSort               avgt   25  5.059 ± 0.049  ms/op
//        Sedgewick.testSortWithSentinels  avgt   25  5.184 ± 0.043  ms/op

    }
	
//	public static void main(String[] args) throws Exception {
//	     Main.main(args);
//	}
//	
}
