package quicksort;


import static quicksort.Utils.*;

import java.util.concurrent.TimeUnit;
import java.util.ArrayDeque;
import java.util.Deque;

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
/*	We implement the refinements recommended in
	Sedgewick, Robert. "Implementing quicksort programs." 
	Communications of the ACM 21.10 (1978): 847-857.
*/
	private static final Deque<Integer> stack = new ArrayDeque<>();
	private static final int CUTOFF = 10;
	
	
	public static void sort(int[] a) {
		if (a == null || a.length == 0) return;

		stack.push(a.length - 1); stack.push(0);
		
		while(!stack.isEmpty()) {
			int lo = stack.pop();
			int hi = stack.pop();
			
			if (hi - lo > CUTOFF) {
				// pivot is the median of lo, hi, and mid
				// pivot is set to lo, and lo + 1 and hi are sentinels
				medianOfThree(a, lo, hi);
				
				// some alternatives are:
				// shuffle(a);  // random shuffle of entire array (do this before sorting)
				// setRandomPivot(a, lo, hi);  // select random pivot, as suggested by Hoare
		        // various median schemes:
				// median of another number, but Sedgewick found 3 or 5 was best
				// median of random sample (if we are worried about denial-of-service attacks)
				// Tukey's ninther (median of medians)
				
				int pivot = partition(a, lo, hi);
				
				// push smaller "half" onto auxiliary stack last
				// this will greatly mitigate stack overflow (stack size ~ log(n))
				if (pivot - lo < hi - pivot) {
					stack.push(hi); stack.push(pivot + 1);
					stack.push(pivot - 1); stack.push(lo);
				} else {
					stack.push(pivot - 1); stack.push(lo);
					stack.push(hi); stack.push(pivot + 1);
				}
			}
		}
		
		insertionSort(a);
	}
	
	private static void medianOfThree(int[] a, int lo, int hi) {
		// precondition: need hi - lo > 1
		// we use Sedgewick's median of three implementation, which sets up
		// sentinels at each end of the subarray
		int mid = lo + (hi - lo) / 2 ;
		swap(a, mid, lo + 1);
		if (a[lo + 1] > a[hi]) swap(a, lo + 1, hi);
		if (a[lo] > a[hi]) swap(a, lo, hi);
		if (a[lo + 1] > a[lo]) swap(a, lo + 1, lo);
	}

	private static int partition(int[] a, int lo, int hi) {
		// precondition: sort method should pass in lo & hi with lo <= hi
		// i, j can be set to the sentinels setup by median of three
		int i = lo + 1;
		int j = hi;
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
	
	
	/*  State : Random array to be sorted */
	
	@SuppressWarnings("unused")
	public int[] randomArray;
	
	@Setup(Level.Invocation)
	public void initializeRandomArray() {
		randomArray = getRandomArray(100000, 1000);
		shuffle(randomArray);
	}
	
	/* * * * * * * * * * * * * * * * * */
	
	@Benchmark
	public boolean testSort() {

		sort(randomArray);
		
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
                .measurementIterations(10)
                .mode(Mode.AverageTime)
                .timeUnit(TimeUnit.MILLISECONDS)
                .forks(1)
                .shouldFailOnError(true)
                .shouldDoGC(true)
                .jvmArgs("-server")
                .build();
 
        new Runner(opt).run();

//		int[] randomArray = getRandomArray(10000000, 10000);
//		shuffle(randomArray);
//		sort(randomArray);
//		System.out.println( validateSort(randomArray) );
    }
	
//	public static void main(String[] args) throws Exception {
//	     Main.main(args);
//	}
//	
}
