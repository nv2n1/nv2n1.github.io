---
title: "kcbench(1)"
name: "kcbench"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcbench/"
description: "kcbench – Kernel compile benchmark"
---

<h2>NAME</h2>
<p> <code>kcbench </code>&#8211; Kernel compile benchmark</p>
<h2>SYNOPSIS</h2>
<pre>
<code>kcbench</code> [<i>options</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> Compiles a Linux kernel to benchmark a system or test its stability</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;compiledir</code> &lt;path&gt;</p>
<dd></dl>
<pre>
   Use the subdirectory kcbench in &lt;path&gt;/ when compiling results -- passes
   'O=&lt;path&gt; /kcbench/' to make when calling it to compile a kernel; use a
   tempdir if not given
</pre>
<p> <code>-r</code>, <code>&#8211;detailedresults</code> </p>
<pre>
   Print more detailed results
</pre>
<p> <code>-a</code>, <code>&#8211;ignore-running-apps</code> </p>
<pre>
   Do not warn if cron or other daemons run in the background; the results
   might not be stable when those run and call jobs that consume CPU time or
   do a lot of I/O
</pre>
<p> <code>-i</code>, <code>&#8211;infinite</code> </p>
<pre>
   run endlessly to test system stability
</pre>
<p> <code>-n</code>, <code>&#8211;iterations</code> &lt;int&gt; </p>
<pre>
   Number or iterations per number of jobs (default: 3)
</pre>
<p> <code>-j</code>, <code>&#8211;jobs</code> &lt;int&gt; </p>
<pre>
   Number of jobs to use ('make -j #'); option can be given multiple times
   (default: number of CPUs * 2)
</pre>
<p> <code>-c</code>, <code>&#8211;no-cachefill</code> </p>
<pre>
   Omit the initial kernel compile to fill caches; saves time, but first
   result might be slightly lower then the following ones
</pre>
<p> <code>-v</code>, <code>&#8211;verbose</code> </p>
<pre>
   Increase verboselevel; option can be given multiple times
</pre>
<p> <code>-l</code>, <code>&#8211;savefailedlogs</code> &lt;path&gt; </p>
<pre>
   Save log of failed compile runs in &lt;path&gt;
</pre>
<p> <code>-s</code>, <code>&#8211;src</code> (&lt;path&gt;|&lt;version&gt;) </p>
<pre>
   Take sources in &lt;path&gt; or from /usr/share/kcdata/linux-&lt;version&gt;
</pre>
<p> <code>-h</code>, <code>&#8211;help</code> </p>
<pre>
   Show usage
</pre>
<p> <code>-V</code>, <code>&#8211;version</code> </p>
<pre>
   Output program version
</pre>
<h2>ENVIRONMENT</h2>
<p> Kcbench looks for a kernel to compile in /usr/share/<code>kcbench</code>-data and will take the one that a &quot;ls usr/share/<code>kcbench</code>-data | head <code>-n</code> 1&quot; outputs by default</p>
<h2>EXAMPLE</h2>
<p> To compile the default kernel 3 times in a row run: </p>
<pre>
      $ kcbench
</pre>
<p> To compile the defaukt kernel 3 times with 2 jobs and 3 times with 4 jobs run </p>
<pre>
      $ kcbench --iterations 3 --jobs 2 --jobs 4
</pre>
<h2>RESULTS</h2>
<p> By default the line you are looking for is this: </p>
<pre>
      Run 1 (-j 4): 5775 (e:173.15P:192%  U:263.49 S:69.42 F:0)
</pre>
<p> Here it has taken 173.15 seconds real time (e) to compile the kernel; the CPU-Usage (P) was 192 percent; user time (U) spend was 296.49 and sys time (S) 69.42 and there we no major page faults (see the info or man pages for time for details about the notation). </p>
<p> As most people prefer if higher numbers mean faster systems &#8212; to give them what they expect <code>kcbench</code> divides 1000000 by the real time spend, which results in 5775 <code>kcbench</code> points (1000000/173.15) in this example. </p>
<p> When running with &quot;<code>-r</code>|<code>&#8211;detailedresults</code>&quot; you&#8217;ll get more detailed results: </p>
<pre>
      Run 1 (-j 4):       6662 (e:150.10 P:197% U:259.51 S:36.38 F:0)
        Elapsed Time(E): 2:30.10 (150.10 seconds)
        Kernel time (S): 36.38 seconds
        User time (U): 259.51 seconds
        CPU usage (P): 197%
        Major page faults (F): 0
        Minor page faults (R): 9441809
        Context switches involuntarily (c): 69031
        Context switches voluntarily (w): 46955
</pre>
<h2>HINTS</h2>
<dl>
<dt>*</p>
<dd> sometimes using exactly as much jobs as processors in the system results in a result that&#8217;s a bit faster than the default (two times the number of processors)</p>
<dt>*</p>
<dd> the compiler has a huge impact on the results; if you compare results from different machines make sure they use a similar one. The running kernel and its settings also have a impact on the results. Thus it&#8217;s the best not to compare different distributions/different patch levels.</p>
<dt>*</p>
<dd> the kernel that is being compiled of course has a huge impact as well; compare only results where you compiled the same kernel version</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-time/">time</a></code>(1).</p>
<h2>BUGS</h2>
<p> None know, but there are likely some</p>
<h2>AUTHOR</h2>
<p> Thorsten Leemhuis &lt;fedora [AT] leemhuis [DOT] info&gt; </p>
<h2>Index</h2>
