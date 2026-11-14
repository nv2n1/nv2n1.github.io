---
title: "adjtimex(8)"
name: "adjtimex"
section: "8"
letter: "a"
url: "/docs/linux/man/8-adjtimex/"
description: "adjtimex – display or set the kernel time variables"
---

<p>adjtimex &#8211; display or set the kernel time variables</p>
<h2>Synopsis</h2>
<p><code>adjtimex</code> [<i>option</i>]&#8230;</p>
<h2>Description</h2>
<p>This program gives you raw access to the kernel time variables. Anyone may print out the time variables, but only the superuser may change them. </p>
<p> Your computer has two clocks &#8211; the &quot;hardware clock&quot; that runs all the time, and the system clock that runs only while the computer is on. Normally, &quot;hwclock &#8211;hctosys&quot; should be run at startup to initialize the system clock. The system clock has much better precision (approximately 1 usec), but the hardware clock probably has better long-term stability. There are three basic strategies for managing these clocks. </p>
<p> For a machine connected to the Internet, or equipped with a precision oscillator or radio clock, the best way is to regulate the system clock with <code><a href="/docs/linux/man/8-ntpd/">ntpd</a></code>(8). The kernel will automatically update the hardware clock every eleven minutes. </p>
<p> In addition, <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) can be used to approximately correct for a constant drift in the hardware clock. In this case, &quot;hwclock &#8211;adjust&quot; is run occasionally. <code>hwclock</code> notes how long it has been since the last adjustment, and nudges the hardware clock forward or back by the appropriate amount. The user needs to set the time with &quot;hwclock &#8211;set&quot; several times over the course of a few days so <code>hwclock</code> can estimate the drift rate. During that time, <code>ntpd</code> should not be running, or else <code>hwclock</code> will conclude the hardware clock does not drift at all. After you have run &quot;hwclock &#8211;set&quot; for the last time, it&#8217;s okay to start <code>ntpd</code>. Then, &quot;hwclock &#8211;systohc&quot; should be run when the machine is shut down. (To see why, suppose the machine runs for a week with <code>ntpd</code>, is shut down for a day, is restarted, and &quot;hwclock &#8211;adjust&quot; is run by a startup script. It should only correct for one day&#8217;s worth of drift. However, it has no way of knowing that <code>ntpd</code> has been adjusting the hardware clock, so it bases its adjustment on the last time <code>hwclock</code> was run.) </p>
<p> For a standalone or intermittently connected machine, where it&#8217;s not possible to run <code>ntpd</code>, you may use <code>adjtimex</code> instead to correct the system clock for systematic drift. </p>
<p> There are several ways to estimate the drift rate. If your computer can be connected to the net, you might run <code>ntpd</code> for at least several hours and run &quot;adjtimex &#8211;print&quot; to learn what values of tick and freq it settled on. Alternately, you could estimate values using as a reference the CMOS clock (see the <code>&#8211;compare</code> and <code>&#8211;adjust</code> switches), another host (see <code>&#8211;host</code> and <code>&#8211;review</code>), or some other source of time (see <code>&#8211;watch</code> and <code>&#8211;review</code>). You could then add a line to <i>rc.local</i> invoking <code>adjtimex</code>, or configure <i>/etc/init.d/adjtimex</i> or <i>/etc/default/adjtimex</i>, to set those parameters each time you reboot.</p>
<h2>Options</h2>
<p>Options may be introduced by either <code>&#8211;</code> or <code>&#8212;</code>, and unique abbreviations may be used. </p>
<p> Here is a summary of the options, grouped by type. Explanations follow.</p>
<dl>
<dt><code>Get/Set Kernel Time Parameters</code></p>
<dd>-p &#8211;print -t &#8211;tick<i> val</i> -f<i> newfreq</i> &#8211;frequency<i> newfreq</i> -o<i> val</i> &#8211;offset<i> val</i> -s<i> adjustment</i> &#8211;singleshot<i> adjustment</i> -S<i> status</i> &#8211;status<i> status</i> -m<i> val</i> -R &#8211;reset &#8211;maxerror<i> val</i> -e<i> val</i> &#8211;esterror<i> val</i> -T<i> val</i> &#8211;timeconstant<i> val</i> -a[<i>count</i>] &#8211;adjust[=<i>count</i>]</p>
<dt><code>Estimate Systematic Drifts</code></p>
<dd>-c[<i>count</i>] &#8211;compare[=<i>count</i>] -i<i> tim</i> &#8211;interval<i> tim</i> -l<i> file</i> &#8211;logfile<i> file</i> -h<i> timeserver</i> &#8211;host<i> timeserver</i> -w &#8211;watch -r[<i>file</i>] &#8211;review[=<i>file</i>] -u &#8211;utc -d &#8211;directisa -n &#8211;nointerrupt</p>
<dt><code>Informative Output</code></p>
<dd>&#8211;help -v &#8211;version -V &#8211;verbose </p>
<dt><code>-p</code>, <code>&#8211;print</code></p>
<dd>Print the current values of the kernel time variables. NOTE: The time is &quot;raw&quot;, and may be off by up to one timer tick (10 msec). &quot;status&quot; gives the value of the <code>time_status</code> variable in the kernel. For Linux 1.0 and 1.2 kernels, the value is as follows: </p>
<pre> 0 clock is synchronized (so the kernel should 
 periodically set the CMOS clock to match the
 system clock)
 1 inserting a leap second at midnight
 2 deleting a leap second at midnight
 3 leap second in progress
 4 leap second has occurred
 5 clock not externally synchronized (so the 
 kernel should leave the CMOS clock alone)</pre>
<p>For Linux kernels 2.0 through 2.6, the value is a sum of these: </p>
<pre> 1 PLL updates enabled
 2 PPS freq discipline enabled
 4 PPS time discipline enabled
 8 frequency-lock mode enabled
 16 inserting leap second
 32 deleting leap second
 64 clock unsynchronized
 128 holding frequency
 256 PPS signal present
 512 PPS signal jitter exceeded
 1024 PPS signal wander exceeded
 2048 PPS signal calibration error
 4096 clock hardware fault</pre>
<dt><code>-t</code> <i>val</i>, <code>&#8211;tick</code> <i>val</i></p>
<dd>Set the number of microseconds that should be added to the system time for each kernel tick interrupt. For a kernel with USER_HZ=100, there are supposed to be 100 ticks per second, so <i>val</i> should be close to 10000. Increasing <i>val</i> by 1 speeds up the system clock by about 100 ppm, or 8.64 sec/day. <i>tick</i> must be in the range 900000/USER_HZ&#8230;1100000/USER_HZ. If <i>val</i> is rejected by the kernel, <code>adjtimex</code> will determine the acceptable range through trial and error and print it. (After completing the search, it will restore the original value.)</p>
<dt><code>-f</code> <i>newfreq</i>, <code>&#8211;frequency</code> <i>newfreq</i></p>
<dd>Set the system clock frequency offset to <i>newfreq</i>. <i>newfreq</i> can be negative or positive, and gives a much finer adjustment than the <code>&#8211;tick</code> switch. When USER_HZ=100, the value is scaled such that <i>newfreq</i> = 65536 speeds up the system clock by about 1 ppm, or .0864 sec/day. Thus, all of these are about the same: </p>
<pre> <code>--tick 9995 --frequency 32768000</code>
 <code>--tick 10000 --frequency 6553600</code>
 <code>--tick 10001 --frequency 0</code>
 <code>--tick 10002 --frequency -6553600</code>
 <code>--tick 10005 --frequency -32768000</code></pre>
<p>To see the acceptable range for <i>newfreq</i>, use &#8211;print and look at &quot;tolerance&quot;, or try an illegal value (e.g. &#8211;tick 0).</p>
<dt><code>-s</code> <i>adj</i>, <code>&#8211;singleshot</code> <i>adj</i></p>
<dd>Slew the system clock by <i>adj</i> usec. (Its rate is changed temporarily by about 1 part in 2000.)</p>
<dt><code>-o</code> <i>adj</i>, <code>&#8211;offset</code> <i>adj</i></p>
<dd>Add a time offset of <i>adj</i> usec. The kernel code adjusts the time gradually by <i>adj</i>, notes how long it has been since the last time offset, and then adjusts the frequency offset to correct for the apparent drift. <i>adj</i> must be in the range -512000&#8230;512000.</p>
<dt><code>-S</code> <i>status</i>, <code>&#8211;status</code> <i>status</i></p>
<dd>Set kernel system clock status register to value <i>status</i>. Look here above at the <code>&#8211;print</code> switch section for the meaning of <i>status</i>, depending on your kernel.</p>
<dt><code>-R</code>, <code>&#8211;reset</code></p>
<dd>Reset clock status after setting a clock parameter. For early Linux kernels, using the <a href="/docs/linux/man/2-adjtimex/">adjtimex</a>(2) system call to set any time parameter the kernel think the clock is synchronized with an external time source, so it sets the kernel variable time_status to TIME_OK. Thereafter, at 11 minute intervals, it will adjust the CMOS clock to match. We prevent this &quot;eleven minute mode&quot; by setting the clock, because that has the side effect of resetting time_status to TIME_BAD. We try not to actually change the clock setting. Kernel versions 2.0.40 and later apparently don&#8217;t need this. If your kernel does require it, use this option with: <code>-t</code> <code>-T</code> <code>-t</code> <code>-e</code> <code>-m</code> <code>-f</code> <code>-s</code> <code>-o</code> <code>-c</code> <code>-r</code>.</p>
<dt><code>-m</code> <i>val</i>, <code>&#8211;maxerror</code> <i>val</i></p>
<dd>Set maximum error (usec).</p>
<dt><code>-e</code> <i>val</i>, <code>&#8211;esterror</code> <i>val</i></p>
<dd>Set estimated error (usec). The maximum and estimated error are not used by the kernel. They are merely made available to user processes via the <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2) system call.</p>
<dt><code>-T</code> <i>val</i>, <code>&#8211;timeconstant</code> <i>val</i></p>
<dd>Set phase locked loop (PLL) time constant. <i>val</i> determines the bandwidth or &quot;stiffness&quot; of the PLL. The effective PLL time constant will be a multiple of (2^<i>val</i>). For room-temperature quartz oscillators, David Mills recommends the value 2, which corresponds to a PLL time constant of about 900 sec and a maximum update interval of about 64 sec. The maximum update interval scales directly with the time constant, so that at the maximum time constant of 6, the update interval can be as large as 1024 sec. </p>
<p> Values of <i>val</i> between zero and 2 give quick convergence; values between 2 and 6 can be used to reduce network load, but at a modest cost in accuracy.</p>
<dt><code>-c</code>[<i>count</i>], <code>&#8211;compare</code>[<code>=</code><i>count</i>]</p>
<dd>Periodically compare the system clock with the CMOS clock. After the first two calls, print values for tick and frequency offset that would bring the system clock into approximate agreement with the CMOS clock. CMOS clock readings are adjusted for systematic drift using using the correction in <i>/etc/adjtime</i> &#8212; see <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8). The interval between comparisons is 10 seconds, unless changed by the <code>&#8211;interval</code> switch. The optional argument is the number of comparisons. (If the argument is supplied, the &quot;<code>=</code>&quot; is required.) If the CMOS clock and the system clock differ by more than six minutes, <code>adjtimex</code> will try shifting the time from the CMOS clock by some multiple of one hour, up to plus or minus 13 hours in all. This should allow correct operation, including logging, if the &#8211;utc switch was used when the CMOS clock is set to local time (or vice-versa), or if summer time has started or stopped since the CMOS clock was last set.</p>
<dt><code>-a</code>[<i>count</i>], <code>&#8211;adjust</code>[<code>=</code><i>count</i>]</p>
<dd>By itself, same as <code>&#8211;compare</code>, except the recommended values are actually installed after every third comparison. With <code>&#8211;review</code>, the tick and frequency are set to the least-squares estimates. (In the latter case, any <i>count</i> value is ignored.)</p>
<dt><code>&#8211;force-adjust</code></p>
<dd>Override the sanity check that prevents changing the clock rate by more than 500 ppm.</p>
<dt><code>-i</code> <i>tim</i>, <code>&#8211;interval</code> <i>tim</i></p>
<dd>Set the interval in seconds between clock comparisons for the <code>&#8211;compare</code> and <code>&#8211;adjust</code> options.</p>
<dt><code>-u</code>, <code>&#8211;utc</code></p>
<dd>The CMOS clock is set to UTC (universal time) rather than local time.</p>
<dt><code>-d</code>, <code>&#8211;directisa</code></p>
<dd>To read the CMOS clock accurately, <code>adjtimex</code> usually accesses the clock via the /dev/rtc device driver of the kernel, and makes use of its CMOS update-ended interrupt to detect the beginning of seconds. It will also try /dev/rtc0 (for udev), /dev/misc/rtc (for the obsolete devfs) and possibly others. When the /dev/rtc driver is absent, or when the interrupt is not available, <code>adjtimex</code> can sometimes automatically fallback to a direct access method. This method detects the start of seconds by polling the update-in-progress (UIP) flag of the CMOS clock. You can force this direct access to the CMOS chip with the <code>&#8211;directisa</code> switch. </p>
<p> Note that the /dev/rtc interrupt method is more accurate, less sensible to perturbations due to system load, cleaner, cheaper, and is generally better than the direct access method. It is advisable to not use the <code>&#8211;directisa</code> switch, unless the CMOS chip or the motherboard don&#8217;t properly provide the necessary interrupt.</p>
<dt><code>-n</code>, <code>&#8211;nointerrupt</code></p>
<dd>Force immediate use of busywait access method, without first waiting for the interrupt timeout.</p>
<dt><code>-l</code>[<i>file</i>], <code>&#8211;log</code>[<code>=</code><i>file</i>]</p>
<dd>Save the current values of the system and CMOS clocks, and optionally a reference time, to <i>file</i> (default <i>/var/log/clocks.log</i>). The reference time is taken from a network timeserver (see the <code>&#8211;host</code> switch) or supplied by the user (see the <code>&#8211;watch</code> switch).</p>
<dt><code>-h</code> <i>timeserver</i>, <code>&#8211;host</code> <i>timeserver</i></p>
<dd>Use <code>ntpdate</code> to query the given timeserver for the current time. This will fail if <i>timeserver</i> is not running a Network Time Protocol (NTP) server, or if that server is not synchronized. Implies <code>&#8211;log</code>.</p>
<dt><code>-w</code>, <code>&#8211;watch</code></p>
<dd>Ask for a keypress when the user knows the time, then ask what that time was, and its approximate accuracy. Implies <code>&#8211;log</code>.</p>
<dt><code>-r</code>[<i>file</i>], <code>&#8211;review</code>[<code>=</code><i>file</i>]</p>
<dd>Review the clock log <i>file</i> (default <i>/var/log/clocks.log</i>) and estimate, if possible, the rates of the CMOS and system clocks. Calculate least-squares rates using all suitable log entries. Suggest corrections to adjust for systematic drift. With <code>&#8211;adjust</code>, the frequency and tick are set to the suggested values. (The CMOS clock correction is not changed.)</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase verbosity.</p>
<dt><code>&#8211;help</code></p>
<dd>Print the program options.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the program version.</dl>
<h2>Examples</h2>
<p>If your system clock gained 8 seconds in 24 hours, you could set the tick to 9999, and then it would lose 0.64 seconds a day (that is, 1 tick unit = 8.64 seconds per day). To correct the rest of the error, you could set the frequency offset to (2^16)*0.64/.0864 = 485452. Thus, putting the following in rc.local would approximately correct the system clock: </p>
<pre> adjtimex --tick 9999 --freq 485452</pre>
<h2>Notes</h2>
<p><code>adjtimex</code> adjusts only the system clock &#8212; the one that runs while the computer is powered up. To set or regulate the CMOS clock, see <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8).</p>
<h2>Authors</h2>
<p>Steven S. Dick &lt;ssd at nevets.oau.org&gt;, Jim Van Zandt &lt;jrv at comcast.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1L-date/">date</a></code>(1L), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/8-ntpdate/">ntpdate</a></code>(8), <code><a href="/docs/linux/man/8-ntpd/">ntpd</a></code>(8), <i>/usr/src/linux/include/linux/timex.h, /usr/src/linux/include/linux/sched.h, /usr/src/linux/kernel/time.c, /usr/src/linux/kernel/sched.c</i> </p>
