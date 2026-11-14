---
title: "rtc(4)"
name: "rtc"
section: "4"
letter: "r"
url: "/docs/linux/man/4-rtc/"
description: "rtc – real-time clock"
---

<p>rtc &#8211; real-time clock</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/rtc.h&gt;
int ioctl(fd, RTC_request, param);</code></pre>
<h2>Description</h2>
<p>This is the interface to drivers for real-time clocks (RTCs). </p>
<p> Most computers have one or more hardware clocks which record the current &quot;wall clock&quot; time. These are called &quot;Real Time Clocks&quot; (RTCs). One of these usually has battery backup power so that it tracks the time even while the computer is turned off. RTCs often provide alarms and other interrupts. </p>
<p> All i386 PCs, and ACPI-based systems, have an RTC that is compatible with the Motorola MC146818 chip on the original PC/AT. Today such an RTC is usually integrated into the mainboard&#8217;s chipset (south bridge), and uses a replaceable coin-sized backup battery. </p>
<p> Non-PC systems, such as embedded systems built around system-on-chip processors, use other implementations. They usually won&#8217;t offer the same functionality as the RTC from a PC/AT.</p>
<h3>RTC vs system clock</h3>
<p>RTCs should not be confused with the system clock, which is a software clock maintained by the kernel and used to implement <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) and <code><a href="/docs/linux/man/2-time/">time</a></code>(2), as well as setting timestamps on files, and so on. The system clock reports seconds and microseconds since a start point, defined to be the POSIX Epoch: 1970-01-01 00:00:00 +0000 (UTC). (One common implementation counts timer interrupts, once per &quot;jiffy&quot;, at a frequency of 100, 250, or 1000 Hz.) That is, it is supposed to report wall clock time, which RTCs also do. </p>
<p> A key difference between an RTC and the system clock is that RTCs run even when the system is in a low power state (including &quot;off&quot;), and the system clock can&#8217;t. Until it is initialized, the system clock can only report time since system boot &#8230; not since the POSIX Epoch. So at boot time, and after resuming from a system low power state, the system clock will often be set to the current wall clock time using an RTC. Systems without an RTC need to set the system clock using another clock, maybe across the network or by entering that data manually.</p>
<h3>RTC functionality</h3>
<p>RTCs can be read and written with <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), or directly with the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests listed below. </p>
<p> Besides tracking the date and time, many RTCs can also generate interrupts</p>
<dl>
<dt>*</p>
<dd>on every clock update (i.e., once per second);</p>
<dt>*</p>
<dd>at periodic intervals with a frequency that can be set to any power-of-2 multiple in the range 2 Hz to 8192 Hz;</p>
<dt>*</p>
<dd>on reaching a previously specified alarm time.</dl>
<p> Each of those interrupt sources can be enabled or disabled separately. On many systems, the alarm interrupt can be configured as a system wakeup event, which can resume the system from a low power state such as Suspend-to-RAM (STR, called S3 in ACPI systems), Hibernation (called S4 in ACPI systems), or even &quot;off&quot; (called S5 in ACPI systems). On some systems, the battery backed RTC can&#8217;t issue interrupts, but another one can. </p>
<p> The <i>/dev/rtc</i> (or <i>/dev/rtc0</i>, <i>/dev/rtc1</i>, etc.) device can be opened only once (until it is closed) and it is read-only. On <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-select/">select</a></code>(2) the calling process is blocked until the next interrupt from that RTC is received. Following the interrupt, the process can read a long integer, of which the least significant byte contains a bit mask encoding the types of interrupt that occurred, while the remaining 3 bytes contain the number of interrupts since the last <code><a href="/docs/linux/man/2-read/">read</a></code>(2).</p>
<h3><a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) interface</h3>
<p>The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests are defined on file descriptors connected to RTC devices:</p>
<dl>
<dt><code>RTC_RD_TIME</code></p>
<dd>Returns this RTC&#8217;s time in the following structure:</p>
<dd>struct rtc_time {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_sec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_min;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_hour;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_mday;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_mon;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_year;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_wday;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_yday;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tm_isdst;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;*/ };</p>
<dd>The fields in this structure have the same meaning and ranges as for the <i>tm</i> structure described in <code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3). A pointer to this structure should be passed as the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument.</p>
<dt><code>RTC_SET_TIME</code></p>
<dd>Sets this RTC&#8217;s time to the time specified by the <i>rtc_time</i> structure pointed to by the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. To set the RTC&#8217;s time the process must be privileged (i.e., have the <code>CAP_SYS_TIME</code> capability).</p>
<dt><code>RTC_ALM_READ</code>, <code>RTC_ALM_SET</code></p>
<dd>Read and set the alarm time, for RTCs that support alarms. The alarm interrupt must be separately enabled or disabled using the <code>RTC_AIE_ON</code>, <code>RTC_AIE_OFF</code> requests. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is a pointer to an <i>rtc_time</i> structure. Only the <i>tm_sec</i>, <i>tm_min</i>, and <i>tm_hour</i> fields of this structure are used.</p>
<dt><code>RTC_IRQP_READ</code>, <code>RTC_IRQP_SET</code></p>
<dd>Read and set the frequency for periodic interrupts, for RTCs that support periodic interrupts. The periodic interrupt must be separately enabled or disabled using the <code>RTC_PIE_ON</code>, <code>RTC_PIE_OFF</code> requests. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is an <i>unsigned long&nbsp;*</i> or an <i>unsigned long</i>, respectively. The value is the frequency in interrupts per second. The set of allowable frequencies is the multiples of two in the range 2 to 8192. Only a privileged process (i.e., one having the <code>CAP_SYS_RESOURCE</code> capability) can set frequencies above the value specified in <i>/proc/sys/dev/rtc/max-user-freq</i>. (This file contains the value 64 by default.)</p>
<dt><code>RTC_AIE_ON</code>, <code>RTC_AIE_OFF</code></p>
<dd>Enable or disable the alarm interrupt, for RTCs that support alarms. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is ignored.</p>
<dt><code>RTC_UIE_ON</code>, <code>RTC_UIE_OFF</code></p>
<dd>Enable or disable the interrupt on every clock update, for RTCs that support this once-per-second interrupt. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is ignored.</p>
<dt><code>RTC_PIE_ON</code>, <code>RTC_PIE_OFF</code></p>
<dd>Enable or disable the periodic interrupt, for RTCs that support these periodic interrupts. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is ignored. Only a privileged process (i.e., one having the <code>CAP_SYS_RESOURCE</code> capability) can enable the periodic interrupt if the frequency is currently set above the value specified in <i>/proc/sys/dev/rtc/max-user-freq</i>.</p>
<dt><code>RTC_EPOCH_READ</code>, <code>RTC_EPOCH_SET</code></p>
<dd>Many RTCs encode the year in an 8-bit register which is either interpreted as an 8-bit binary number or as a BCD number. In both cases, the number is interpreted relative to this RTC&#8217;s Epoch. The RTC&#8217;s Epoch is initialized to 1900 on most systems but on Alpha and MIPS it might also be initialized to 1952, 1980, or 2000, depending on the value of an RTC register for the year. With some RTCs, these operations can be used to read or to set the RTC&#8217;s Epoch, respectively. The third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument is an <i>unsigned long&nbsp;*</i> or an <i>unsigned long</i>, respectively, and the value returned (or assigned) is the Epoch. To set the RTC&#8217;s Epoch the process must be privileged (i.e., have the <code>CAP_SYS_TIME</code> capability).</p>
<dt><code>RTC_WKALM_RD</code>, <code>RTC_WKALM_SET</code></p>
<dd>Some RTCs support a more powerful alarm interface, using these ioctls to read or write the RTC&#8217;s alarm time (respectively) with this structure:</dl>
<dl>
<dd>struct rtc_wkalrm {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char enabled;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char pending;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct rtc_time time; };</dl>
<dl>
<dd>The <i>enabled</i> flag is used to enable or disable the alarm interrupt, or to read its current status; when using these calls, <code>RTC_AIE_ON</code> and <code>RTC_AIE_OFF</code> are not used. The <i>pending</i> flag is used by <code>RTC_WKALM_RD</code> to report a pending interrupt (so it&#8217;s mostly useless on Linux, except when talking to the RTC managed by EFI firmware). The <i>time</i> field is as used with <code>RTC_ALM_READ</code> and <code>RTC_ALM_SET</code> except that the <i>tm_mday</i>, <i>tm_mon</i>, and <i>tm_year</i> fields are also valid. A pointer to this structure should be passed as the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument.</dl>
<h2>Files</h2>
<dl>
<dt><i>/dev/rtc</i>, <i>/dev/rtc0</i>, <i>/dev/rtc1</i>, etc.</p>
<dd>RTC special character device files.</p>
<dt><i>/proc/driver/rtc</i></p>
<dd>status of the (first) RTC.</dl>
<h2>Notes</h2>
<p>When the kernel&#8217;s system time is synchronized with an external reference using <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2) it will update a designated RTC periodically every 11 minutes. To do so, the kernel has to briefly turn off periodic interrupts; this might affect programs using that RTC. </p>
<p> An RTC&#8217;s Epoch has nothing to do with the POSIX Epoch which is used only for the system clock. </p>
<p> If the year according to the RTC&#8217;s Epoch and the year register is less than 1970 it is assumed to be 100 years later, that is, between 2000 and 2069. </p>
<p> Some RTCs support &quot;wildcard&quot; values in alarm fields, to support scenarios like periodic alarms at fifteen minutes after every hour, or on the first day of each month. Such usage is nonportable; portable user-space code expects only a single alarm interrupt, and will either disable or reinitialize the alarm after receiving it. </p>
<p> Some RTCs support periodic interrupts with periods that are multiples of a second rather than fractions of a second; multiple alarms; programmable output clock signals; nonvolatile memory; and other hardware capabilities that are not currently exposed by this API.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/2-stime/">stime</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8) </p>
<p> <i>Documentation/rtc.txt</i> in the Linux kernel source tree</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
