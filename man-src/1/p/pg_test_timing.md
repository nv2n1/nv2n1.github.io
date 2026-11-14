---
title: "pg_test_timing(1)"
name: "pg_test_timing"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_test_timing/"
description: "pg_test_timing – measure timing overhead"
---

<h2 class="name">NAME</h2>
<p> pg_test_timing &#8211; measure timing overhead </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_test_timing</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_test_timing is a tool to measure the timing overhead on your system and confirm that the system time never moves backwards. Systems that are slow to collect timing data can give less accurate <code>EXPLAIN ANALYZE</code> results.</p>
<h2>OPTIONS</h2>
<p> pg_test_timing accepts the following command-line options: </p>
<p> <code>-d </code><i>duration</i>, <code>&#8211;duration=</code><i>duration</i></p>
<dl>
<dt>
<dd> Specifies the test duration, in seconds. Longer durations give slightly better accuracy, and are more likely to discover problems with the system clock moving backwards. The default test duration is 3 seconds.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_test_timing version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_test_timing command line arguments, and exit.</dl>
<h2>USAGE</h2>
<h3>Interpreting results</h3>
<p> Good results will show most (&gt;90%) individual timing calls take less than one microsecond. Average per loop overhead will be even lower, below 100 nanoseconds. This example from an Intel i7-860 system using a TSC clock source shows excellent performance: </p>
<dl>
<dt>
<dd>
<pre>
Testing timing overhead for 3 seconds.
Per loop time including overhead: 35.96 nsec
Histogram of timing durations:
   &lt; usec:      count   percent
       16:          2  0.00000%
        8:         13  0.00002%
        4:        126  0.00015%
        2:    2999652  3.59518%
        1:   80435604 96.40465%
</pre>
</dl>
<p> Note that different units are used for the per loop time than the histogram. The loop can have resolution within a few nanoseconds (nsec), while the individual timing calls can only resolve down to one microsecond (usec).</p>
<h3>Measuring executor timing overhead</h3>
<p> When the query executor is running a statement using <code>EXPLAIN ANALYZE</code>, individual operations are timed as well as showing a summary. The overhead of your system can be checked by counting rows with the psql program: </p>
<dl>
<dt>
<dd>
<pre><code>
CREATE TABLE t AS SELECT *FROM generate_series(1, 100000);
	iming
    SELECT
    COUNT(*) FROM t;
EXPLAIN ANALYZE SELECT COUNT(*) FROM t;
</code></pre>
</dl>
<p> The i7-860 system measured runs the count query in 9.8 ms while the <code>EXPLAIN ANALYZE</code> version takes 16.6 ms, each processing just over 100,000 rows. That 6.8 ms difference means the timing overhead per row is 68 ns, about twice what pg_test_timing estimated it would be. Even that relatively small amount of overhead is making the fully timed count statement take almost 70% longer. On more substantial queries, the timing overhead would be less problematic.</p>
<h3>Changing time sources</h3>
<p> On some newer Linux systems, it&#8217;s possible to change the clock source used to collect timing data at any time. A second example shows the slowdown possible from switching to the slower acpi_pm time source, on the same system used for the fast results above: </p>
<dl>
<dt>
<dd>
<pre>
# cat /sys/devices/system/clocksource/clocksource0/available_clocksource
tsc hpet acpi_pm
# echo acpi_pm &gt; /sys/devices/system/clocksource/clocksource0/current_clocksource
# pg_test_timing
Per loop time including overhead: 722.92 nsec
Histogram of timing durations:
   &lt; usec:      count   percent
       16:          3  0.00007%
        8:        563  0.01357%
        4:       3241  0.07810%
        2:    2990371 72.05956%
        1:    1155682 27.84870%
</pre>
</dl>
<p> In this configuration, the sample <code>EXPLAIN ANALYZE</code> above takes 115.9 ms. That&#8217;s 1061 nsec of timing overhead, again a small multiple of what&#8217;s measured directly by this utility. That much timing overhead means the actual query itself is only taking a tiny fraction of the accounted for time, most of it is being consumed in overhead instead. In this configuration, any <code>EXPLAIN ANALYZE</code> totals involving many timed operations would be inflated significantly by timing overhead. </p>
<p> FreeBSD also allows changing the time source on the fly, and it logs information about the timer selected during boot: </p>
<dl>
<dt>
<dd>
<pre>
dmesg | grep &quot;Timecounter&quot;
sysctl kern.timecounter.hardware=TSC
</pre>
</dl>
<p> Other systems may only allow setting the time source on boot. On older Linux systems the &quot;clock&quot; kernel setting is the only way to make this sort of change. And even on some more recent ones, the only option you&#8217;ll see for a clock source is &quot;jiffies&quot;. Jiffies are the older Linux software clock implementation, which can have good resolution when it&#8217;s backed by fast enough timing hardware, as in this example: </p>
<dl>
<dt>
<dd>
<pre>
$ cat /sys/devices/system/clocksource/clocksource0/available_clocksource
jiffies
$ dmesg | grep time.c
time.c: Using 3.579545 MHz WALL PM GTOD PIT/TSC timer.
time.c: Detected 2400.153 MHz processor.
$ pg_test_timing
Testing timing overhead for 3 seconds.
Per timing duration including loop overhead: 97.75 ns
Histogram of timing durations:
   &lt; usec:      count   percent
       32:          1  0.00000%
       16:          1  0.00000%
        8:         22  0.00007%
        4:       3010  0.00981%
        2:    2993204  9.75277%
        1:   27694571 90.23734%
</pre>
</dl>
<h3>Clock hardware and timing accuracy</h3>
<p> Collecting accurate timing information is normally done on computers using hardware clocks with various levels of accuracy. With some hardware the operating systems can pass the system clock time almost directly to programs. A system clock can also be derived from a chip that simply provides timing interrupts, periodic ticks at some known time interval. In either case, operating system kernels provide a clock source that hides these details. But the accuracy of that clock source and how quickly it can return results varies based on the underlying hardware. </p>
<p> Inaccurate time keeping can result in system instability. Test any change to the clock source very carefully. Operating system defaults are sometimes made to favor reliability over best accuracy. And if you are using a virtual machine, look into the recommended time sources compatible with it. Virtual hardware faces additional difficulties when emulating timers, and there are often per operating system settings suggested by vendors. </p>
<p> The Time Stamp Counter (TSC) clock source is the most accurate one available on current generation CPUs. It&#8217;s the preferred way to track the system time when it&#8217;s supported by the operating system and the TSC clock is reliable. There are several ways that TSC can fail to provide an accurate timing source, making it unreliable. Older systems can have a TSC clock that varies based on the CPU temperature, making it unusable for timing. Trying to use TSC on some older multicore CPUs can give a reported time that&#8217;s inconsistent among multiple cores. This can result in the time going backwards, a problem this program checks for. And even the newest systems can fail to provide accurate TSC timing with very aggressive power saving configurations. </p>
<p> Newer operating systems may check for the known TSC problems and switch to a slower, more stable clock source when they are seen. If your system supports TSC time but doesn&#8217;t default to that, it may be disabled for a good reason. And some operating systems may not detect all the possible problems correctly, or will allow using TSC even in situations where it&#8217;s known to be inaccurate. </p>
<p> The High Precision Event Timer (HPET) is the preferred timer on systems where it&#8217;s available and TSC is not accurate. The timer chip itself is programmable to allow up to 100 nanosecond resolution, but you may not see that much accuracy in your system clock. </p>
<p> Advanced Configuration and Power Interface (ACPI) provides a Power Management (PM) Timer, which Linux refers to as the acpi_pm. The clock derived from acpi_pm will at best provide 300 nanosecond resolution. </p>
<p> Timers used on older PC hardware including the 8254 Programmable Interval Timer (PIT), the real-time clock (RTC), the Advanced Programmable Interrupt Controller (APIC) timer, and the Cyclone timer. These timers aim for millisecond resolution.</p>
<h2>AUTHOR</h2>
<p> Ants Aasma &lt;ants.aasma [at] eesti.ee&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-explain/">EXPLAIN</a></code>(7) </p>
<h2>Index</h2>
