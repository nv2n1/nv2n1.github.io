---
title: "haveged(8)"
name: "haveged"
section: "8"
letter: "h"
url: "/docs/linux/man/8-haveged/"
description: "haveged – Generate random numbers and feed linux random device."
---

<p>haveged &#8211; Generate random numbers and feed linux random device.</p>
<h2>Synopsis</h2>
<p><code>haveged [options]</code></p>
<h2>Description</h2>
<p><code>haveged</code> generates an unpredictable stream of random numbers harvested from the indirect effects of hardware events on hidden processor state (caches, branch predictors, memory translation tables, etc) using the HAVEGE (HArdware Volatile Entropy Gathering and Expansion) algorithm. The algorithm operates in user space, no special privilege is required for file system access to the output stream. Linux pools randomness for distribution by the /dev/random and /dev/urandom device interfaces. The standard mechanisms of filling the /dev/random pool may not be sufficient to meet demand on systems with high needs or limited user interaction. In those circumstances, <code>haveged</code> may be run as a privileged daemon to fill the /dev/random pool whenever the supply of random bits in /dev/random falls below the low water mark of the device. <code>haveged</code> tunes itself to its environment and provides the same built-in test suite for the output stream as used on certified hardware security devices. See <code>NOTES</code> below for further information. </p>
<h2>Options</h2>
<dl>
<dt>-b nnn, &#8211;buffer=nnn</p>
<dd>Set collection buffer size to nnn KW. Default is 128KW (or 512KB).</p>
<dt>-d nnn, &#8211;data=nnn</p>
<dd>Set data cache size to nnn KB. Default is 16 or as determined dynamically.</p>
<dt>-f file, &#8211;file=file</p>
<dd>Set output file path for non-daemon use. Default is &quot;sample&quot;, use &quot;-&quot; for stdout.</p>
<dt>-F , &#8211;Foreground</p>
<dd>Run daemon in foreground. Do not fork and detach.</p>
<dt>-i nnn, &#8211;inst=nnn</p>
<dd>Set instruction cache size to nnn KB. Default is 16 or as determined dynamically.</p>
<dt>-n nnn, &#8211;number=nnn</p>
<dd>Set number of bytes written to the output file. The value may be specified using one of the suffixes k, m, g, or t. The upper bound of this value is &quot;16t&quot; (2^44 Bytes = 16TB). A value of 0 indicates unbounded output and forces output to stdout. This argument is required if the daemon interface is not present. If the daemon interface is present, this setting takes precedence over any &#8211;run value.</p>
<dt>-o &lt;spec&gt;, &#8211;onlinetest=&lt;spec&gt;</p>
<dd>Specify online tests to run. The &lt;spec&gt; consists of optional &quot;t&quot;ot and &quot;c&quot;ontinuous groups, each group indicates the procedures to be run, using &quot;a&lt;n&gt;&quot; to indicate a AIS-31 procedure A variant, and &quot;b&quot; to indicate AIS procedure B. The specifications are order independent (procedure B always runs first in each group) and case insensitive. The a&lt;n&gt; variations exist to mitigate the a slow autocorrelation test (test5). Normally all procedure A tests, except the first are iterated 257 times. An a&lt;n&gt; option indicates test5 should only be executed every modulo &lt;n&gt; times during the procedure&#8217;s 257 repetitions. The effect is so noticable that A8 is the usual choice. </p>
<p> The &quot;tot&quot; tests run only at initialization &#8211; there are no negative performance consequences except for a slight increase in the time required to initialize. The &quot;tot&quot; tests guarantee haveged has initialized properly. The use of both test procedures in the &quot;tot&quot; test is highly recommended because the two test emphasize different aspects of RNG quality. </p>
<p> In continuous testing, the test sequence is cycled repeatedly. For example, the string &quot;tbca8b&quot; (suitable for an AIS NTG.1 device) would run procedure B for the &quot;tot&quot; test, then cycle between procedure A8 and procedure B continuously for all further output. Continuous testing does not come for free, impacting both throughput and resource consumption. Continual testing also opens up the possibility of a test failure. A strict retry procedure recovers from spurious failure in all but the most extreme circumstances. When the retry fails, operation will terminate unless a &quot;w&quot; has been appended to the test token to make the test advisory only. In our example above, the string &quot;tbca8wbw&quot; would make all continuous tests advisory. For more detailed information on AIS retries see <code>NOTES</code> below. </p>
<p> Complete control over the test configuration is provided for flexibility. The defaults (ta8bcb&quot; if run as a daemon and &quot;ta8b&quot; otherwise) are suitable for most circumstances. </p>
<dt>-p file, &#8211;pidfile=file</p>
<dd>Set file path for the daemon pid file. Default is &quot;/var/run/haveged.pid&quot;,</p>
<dt>-r n, &#8211;run=n</p>
<dd>Set run level for daemon interface: </p>
<p> n = 0 Run as daemon &#8211; must be root. Fills /dev/random when the supply of random bits<br />
&nbsp;<wbr>falls below the low water mark of the device.&nbsp;<wbr> </p>
<p> n = 1 Display configuration info and terminate. </p>
<p> n &gt; 1 Write &lt;n&gt; kb of output. Deprecated (use &#8211;number instead), only provided for backward compatibility. </p>
<p> If &#8211;number is specified, values other than 0,1 are ignored. Default is 0.</p>
<dt>-v n, &#8211;verbose=n</p>
<dd>Set diagnostic bitmap as sum of following options: </p>
<p> 1=Show build/tuning summary on termination, summary for online test retries. </p>
<p> 2=Show online test retry details </p>
<p> 4=Show timing for collections </p>
<p> 8=Show collection loop layout </p>
<p> 16=Show collection loop code offsets </p>
<p> 32=Show all online test completion detail </p>
<p> Default is 0. Use -1 for all diagnostics.</p>
<dt>-w nnn, &#8211;write=nnn</p>
<dd>Set write_wakeup_threshold of daemon interface to nnn bits. Applies only to run level 0.</p>
<dt>-?, &#8211;help</p>
<dd>This summary of program options. </p>
</dl>
<h2>Notes</h2>
<p>haveged tunes the HAVEGE algorithm for maximum effectiveness using a hierarchy of defaults, command line options, virtual file system information, and cpuid information where available. Under most circumstances, user input is not required for excellent results. Run-time testing provides assurance of correct haveged operation. The run-time test suite is modeled upon the AIS-31 specification of the German Common Criteria body, BIS. This specification is typically applied to hardware devices, requiring formal certification and mandated start-up and continuous operational testing. Because haveged runs on many different hardware platforms, certification cannot be a goal, but the AIS-31 test suite provides the means to assess haveged output with the same operational tests applied to certified hardware devices. AIS test procedure A performs 6 tests to check for statistically inconspicuous behavior. AIS test procedure B performs more theoretical tests such as checking multi-step transition probabilities and making an empirical entropy estimate. Procedure A is the much more resource and compute intensive of the two but is still recommended for the haveged start-up tests. Procedure B is well suited to use of haveged as a daemon because the test entropy estimate confirms the entropy estimate haveged uses when adding entropy to the /dev/random device. No test is perfect. There is a 10e-4 probability that a perfect generator will fail either of the test procedures. AIS-31 mandates a strict retry policy to filter out false alarms and haveged always logs test procedure failures. Retries are expected but rarely observed except when large data sets are generated with continuous testing. See the <code><a href="/docs/linux/man/3-libhavege/">libhavege</a>(3)</code> notes for more detailed information. </p>
<h2>Files</h2>
<p>If running as a daemon, access to the following files is required</p>
<dl>
<dd><i>/dev/random</i> </p>
<p> <i>/proc/sys/kernel/osrelease</i> </p>
<p> <i>/proc/sys/kernel/random/poolsize</i> </p>
<p> <i>/proc/sys/kernel/random/write_wakeup_threshold</i></dl>
<h2>Diagnostics</h2>
<p>Haveged returns 0 for success and non-zero for failure. The failure return code is 1 &quot;general failure&quot; unless execution is terminated by signal &lt;n&gt;, in which case the return code will be 128 + &lt;n&gt;. The following diagnostics are issued to stderr upon non-zero termination: </p>
<p> Cannot fork into the background</p>
<dl>
<dd>Call to <a href="/docs/linux/man/3-daemon/">daemon</a>(3) failed. </p>
</dl>
<p> Cannot open file &lt;s&gt; for writing.</p>
<dl>
<dd>Could not open sample file &lt;s&gt; for writing. </p>
</dl>
<p> Cannot write data in file:</p>
<dl>
<dd>Could not write data to the sample file. </p>
</dl>
<p> Couldn&#8217;t get pool size.</p>
<dl>
<dd>Unable to read /proc/sys/kernel/random/poolsize </p>
</dl>
<p> Couldn&#8217;t initialize HAVEGE rng</p>
<dl>
<dd>Invalid data or instruction cache size. </p>
</dl>
<p> Couldn&#8217;t open PID file &lt;s&gt; for writing</p>
<dl>
<dd>Unable to write daemon PID </p>
</dl>
<p> Couldn&#8217;t open random device</p>
<dl>
<dd>Could not open /dev/random for read-write. </p>
</dl>
<p> Couldn&#8217;t query entropy-level from kernel: error</p>
<dl>
<dd>Call to <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) failed. </p>
</dl>
<p> Couldn&#8217;t open PID file &lt;path&gt; for writing</p>
<dl>
<dd>Error writing /var/run/haveged.pid </p>
</dl>
<p> Fail:set_watermark()</p>
<dl>
<dd>Unable to write to /proc/sys/kernel/random/write_wakeup_threshold </p>
</dl>
<p> RNDADDENTROPY failed!</p>
<dl>
<dd>Call to <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) to add entropy failed </p>
</dl>
<p> RNG failed</p>
<dl>
<dd>The random number generator failed self-test or encountered a fatal error. </p>
</dl>
<p> Select error</p>
<dl>
<dd>Call to <a href="/docs/linux/man/2-select/">select</a>(2) failed. </p>
</dl>
<p> Stopping due to signal &lt;n&gt;</p>
<dl>
<dd>Signal &lt;n&gt; caught. </p>
</dl>
<p> Unable to setup online tests</p>
<dl>
<dd>Memory unavailable for online test resources. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>Write 1.5MB of random data to the file /tmp/random</p>
<dd>haveged -n 1.5M -f /tmp/random</p>
<dt>Generate a /tmp/keyfile for disk encryption with LUKS</p>
<dd>haveged -n 2048 -f /tmp/keyfile</p>
<dt>Overwrite partition /dev/sda1 with random data. Be careful, all data on the partition will be lost!</p>
<dd>haveged -n 0 | dd of=/dev/sda1</p>
<dt>Generate random ASCII passwords of the length 16 characters</p>
<dd>(haveged -n 1000 -f &#8211; 2&gt;/dev/null | tr -cd &#8216;[:graph:]&#8217; | fold -w 16 &amp;&amp; echo ) | head</p>
<dt>Write endless stream of random bytes to the pipe. Utility pv measures the speed by which data are written to the pipe.</p>
<dd>haveged -n 0 | pv &gt; /dev/null</p>
<dt>Evaluate speed of haveged to generate 1GB of random data</p>
<dd>haveged -n 1g -f &#8211; | dd of=/dev/null</p>
<dt>Create a random key file containing 65 random keys for the encryption program aespipe.</p>
<dd>haveged -n 3705 -f &#8211; 2&gt;/dev/null | uuencode -m &#8211; | head -n 66 | tail -n 65</p>
<dt>Test the randomness of the generated data with dieharder test suite</p>
<dd>haveged -n 0 | dieharder -g 200 -a</p>
<dt>Generate 16k of data, testing with procedure A and B with detailed test results. No c result seen because a single buffer fill did not contain enough data to complete the test.</p>
<dd>haveged -n 16k -o tba8ca8 -v 33</p>
<dt>Generate 16k of data as above with larger buffer. The c test now completes &#8211; enough data now generated to complete the test.</p>
<dd>haveged -n 16k -o tba8ca8 -v 33 -b 512</p>
<dt>Generate 16m of data as above, observe many c test completions with default buffer size.</p>
<dd>haveged -n 16m -o tba8ca8 -v 33</p>
<dt>Generate large amounts of data &#8211; in this case 16TB. Enable initialization test but made continuous tests advisory only to avoid a possible situation that program will terminate because of procedureB failing two times in a row. The probability of procedureB to fail two times in a row can be estimated as &lt;TB to generate&gt;/3000 which yields 0.5% for 16TB.</p>
<dd>haveged -n 16T -o tba8cbw -f &#8211; | pv &gt; /dev/null</p>
<dt>Generate large amounts of data (16TB). Disable continuous tests for the maximum throughput but run the online tests at the startup to make sure that generator for properly initialized:</p>
<dd>haveged -n 16T -o tba8c -f &#8211; | pv &gt; /dev/null </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/3-libhavege/">libhavege</a>(3),</code></p>
<dd><code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a>(8),</code> <code><a href="/docs/linux/man/1-aespipe/">aespipe</a>(1),</code> <code><a href="/docs/linux/man/1-pv/">pv</a>(1),</code> <code><a href="/docs/linux/man/1-openssl/">openssl</a>(1),</code> <code><a href="/docs/linux/man/1-uuencode/">uuencode</a>(1)</code> </p>
<h2>References</h2>
<p><i>HArdware Volatile Entropy Gathering and Expansion: generating unpredictable random numbers at user level</i> by A. Seznec, N. Sendrier, INRIA Research Report, RR-4592, October 2002 </p>
<p> <i>A proposal for: Functionality classes for random number generators</i> by W. Killmann and W. Schindler, version 2.0, Bundesamt fur Sicherheit in der Informationstechnik (BSI), September, 2011 </p>
<p> <i>A Statistical Test Suite for the Validation of Random NUmber Generators and Pseudorandom Number Generators for Cryptographic Applications,</i> special publication SP800-22, National Institute of Standards and Technology, revised April, 2010 </p>
<p> Additional information can also be found at <code><a rel="nofollow" href="http://www.issihosts.com/haveged/">http://www.issihosts.com/haveged/</a></code></p>
<h2>Authors</h2>
<p>Gary Wuertz &lt;gary [at] issiweb.com&gt; and Jirka Hladky &lt;hladky jiri AT gmail DOT com&gt;</p>
