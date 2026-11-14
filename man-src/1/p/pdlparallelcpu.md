---
title: "pdlparallelcpu(1)"
name: "pdlparallelcpu"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlparallelcpu/"
description: "PDL::ParallelCPU – Parallel Processor MultiThreading Support in PDL (Experimental)"
---

<p>PDL::ParallelCPU &#8211; Parallel Processor MultiThreading Support in PDL (Experimental) </p>
<h2>Description</h2>
<p><font SIZE="-1">PDL</font> has support (currently experimental) for splitting up numerical processing between multiple parallel processor threads (or pthreads) using the <i>set_autopthread_targ</i> and <i>set_autopthread_size</i> functions. This can improve processing performance (by greater than 2-4X in most cases) by taking advantage of multi-core and/or multi-processor machines.</p>
<h2>Synopsis</h2>
<pre> use PDL;
 
 # Set target of 4 parallel pthreads to create, with a lower limit of
 # 5Meg elements for splitting processing into parallel pthreads.
 <a href="//www.systutorials.com/docs/linux/man/4-set_autopthread_targ/">set_autopthread_targ</a>(4);
 <a href="//www.systutorials.com/docs/linux/man/5-set_autopthread_size/">set_autopthread_size</a>(5);
 
 $a = zeroes(5000,5000); # Create 25Meg element array
 
 $b = $a + 5; # Processing will be split up into multiple pthreads
 
 # Get the actual number of pthreads for the last
 # processing operation.
 $actualPthreads = get_autopthread_actual();</pre>
<h2>Terminology</h2>
<p>The use of the term <i>threading</i> can be confusing with <font SIZE="-1">PDL,</font> because it can refer to <i></i><font SIZE="-1"><i>PDL</i></font><i> threading</i>, as defined in the PDL::Threading docs, or to <i>processor multi-threading</i>. </p>
<p> To reduce confusion with the existing <font SIZE="-1">PDL</font> threading terminology, this document uses <code>pthreading</code> to refer to <i>processor multi-threading</i>, which is the use of multiple processor threads to split up numerical processing into parallel operations.</p>
<h2>Functions that control PDL PThreads</h2>
<p>This is a brief listing and description of the <font SIZE="-1">PDL</font> pthreading functions, see the PDL::Core docs for detailed information.</p>
<dl>
<dt>set_autopthread_targ</p>
<dd>Set the target number of processor-threads (pthreads) for multi-threaded processing. Setting auto_pthread_targ to 0 means that no pthreading will occur. </p>
<p> See PDL::Core for details.</p>
<dt>set_autopthread_size</p>
<dd>Set the minimum size (in Meg-elements or 2**20 elements) of the largest <font SIZE="-1">PDL</font> involved in a function where auto-pthreading will be performed. For small PDLs, it probably isn&#8217;t worth starting multiple pthreads, so this function is used to define a minimum threshold where auto-pthreading won&#8217;t be attempted. </p>
<p> See PDL::Core for details.</p>
<dt>get_autopthread_actual</p>
<dd>Get the actual number of pthreads executed for the last pdl processing function. </p>
<p> See PDL::get_autopthread_actual for details.</dl>
<h2>Global Control of PDL PThreading using Environment Variables</h2>
<p><font SIZE="-1">PDL</font> PThreading can be globally turned on, without modifying existing code by setting environment variables <font SIZE="-1"><code>PDL_AUTOPTHREAD_TARG</code></font> and <font SIZE="-1"><code>PDL_AUTOPTHREAD_SIZE</code></font> before running a <font SIZE="-1">PDL</font> script. These environment variables are checked when <font SIZE="-1">PDL</font> starts up and calls to <i>set_autopthread_targ</i> and <i>set_autopthread_size</i> functions made with the environment variable&#8217;s values. </p>
<p> For example, if the environment var <font SIZE="-1"><code>PDL_AUTOPTHREAD_TARG</code></font> is set to 3, and <font SIZE="-1"><code>PDL_AUTOPTHREAD_SIZE</code></font> is set to 10, then any pdl script will run as if the following lines were at the top of the file: </p>
<pre> <a href="//www.systutorials.com/docs/linux/man/3-set_autopthread_targ/">set_autopthread_targ</a>(3);
 set_autopthread_size(10);</pre>
<h2>How It Works</h2>
<p>The auto-pthreading process works by analyzing threaded array dimensions in <font SIZE="-1">PDL</font> operations and splitting up processing based on the thread dimension sizes and desired number of pthreads (i.e. the pthread target or pthread_targ). The offsets and increments that <font SIZE="-1">PDL</font> uses to step thru the data in memory are modified for each pthread so each one sees a different set of data when performing processing. </p>
<p> <code>Example</code> </p>
<pre> $a = sequence(20,4,3); # Small 3-D Array, size 20,4,3
 
 # Setup auto-pthreading:
 <a href="//www.systutorials.com/docs/linux/man/2-set_autopthread_targ/">set_autopthread_targ</a>(2); # Target of 2 pthreads
 set_autopthread_size(0); # Zero so that the small PDLs in this example will be pthreaded
 # This will be split up into 2 pthreads
 $c = maximum($a);</pre>
<p>For the above example, the <i>maximum</i> function has a signature of <tt>&quot;(<a href="/docs/linux/man/n-a/">a</a>(n); [o]c())&quot;</tt>, which means that the first dimension of <tt>$a</tt> (size 20) is a <i>Core</i> dimension of the <i>maximum</i> function. The other dimensions of <tt>$a</tt> (size 4,3) are <i>threaded</i> dimensions (i.e. will be threaded-over in the <i>maximum</i> function. </p>
<p> The auto-pthreading algorithm examines the threaded dims of size (4,3) and picks the 4 dimension, since it is evenly divisible by the autopthread_targ of 2. The processing of the maximum function is then split into two pthreads on the size-4 dimension, with dim indexes 0,2 processed by one pthread<br />
&nbsp;<wbr>and dim indexes 1,3 processed by the other pthread.</p>
<h2>Limitations</h2>
<h3>Must have <font SIZE="-1">POSIX</font> Threads Enabled</h3>
<p>Auto-PThreading only works if your <font SIZE="-1">PDL</font> installation was compiled with <font SIZE="-1">POSIX</font> threads enabled. This is normally the case if you are running on linux, or other unix variants.</p>
<h3>Non-Threadsafe Code</h3>
<p>Not all the libraries that <font SIZE="-1">PDL</font> intefaces to are thread-safe, i.e. they aren&#8217;t written to operate in a multi-threaded environment without crashing or causing side-effects. Some examples in the <font SIZE="-1">PDL</font> core is the <i>fft</i> function and the <i>pnmout</i> functions. </p>
<p> To operate properly with these types of functions, the PPCode flag <code>NoPthread</code> has been introduced to indicate a function as <i>not</i> being pthread-safe. See <font SIZE="-1">PDL::PP</font> docs for details.</p>
<h3>Size of <font SIZE="-1">PDL</font> Dimensions and PThread Target</h3>
<p>Due to the way a <font SIZE="-1">PDL</font> is split-up for operation using multiple pthreads, the size of a dimension must be evenly divisible by the pthread target. For example, if a <font SIZE="-1">PDL</font> has threaded dimension sizes of (4,3,3) and the <i>auto_pthread_targ</i> has been set to 2, then the first threaded dimension (size 4) will be picked to be split up into two pthreads of size 2 and 2. However, if the threaded dimension sizes are (3,3,3) and the <i>auto_pthread_targ</i> is still 2, then pthreading won&#8217;t occur, because no threaded dimensions are divisible by 2. </p>
<p> The algorithm that picks the actual number of pthreads has some smarts (but could probably be improved) to adjust down from the <i>auto_pthread_targ</i> to get a number of pthreads that can evenly divide one of the threaded dimensions. For example, if a <font SIZE="-1">PDL</font> has threaded dimension sizes of (9,2,2) and the <i>auto_pthread_targ</i> is 4, the algorithm will see that no dimension is divisible by 4, then adjust down the target to 3, resulting in splitting up the first threaded dimension (size 9) into 3 pthreads.</p>
<h3>Speed improvement might be less than you expect.</h3>
<p>If you have a 8 core machine and call <i>auto_pthread_targ</i> with 8 to generate 8 parallel pthreads, you probably won&#8217;t get a 8X improvement in speed, due to memory bandwidth issues. Even though you have 8 separate CPUs crunching away on data, you will have (for most common machine architectures) common <font SIZE="-1">RAM</font> that now becomes your bottleneck. For simple calculations (e.g simple additions) you can run into a performance limit at about<br />
&nbsp;<wbr>4 pthreads. For more complex calculations the limit will be higher.</p>
<h2>Copyright</h2>
<p>Copyright 2011 John Cerney. You can distribute and/or modify this document under the same terms as the current Perl license. </p>
<p> See: <a rel="nofollow" href="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a></p>
