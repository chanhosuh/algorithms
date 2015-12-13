package quicksort;

public class Timer {
	
	Long start;
	
	public Timer() {
		// nanoTime since this is elapsed time, not wall-clock
		this.start = System.nanoTime();
	}
	
	// return time elapsed in seconds
	public Double getElapsedTime() {
		Long now = System.nanoTime();
		
		return (now - start) / 1000000000.0 ;
	}
	
}