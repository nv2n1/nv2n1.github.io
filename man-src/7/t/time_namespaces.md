---
title: "time_namespaces(7)"
name: "time_namespaces"
section: "7"
letter: "t"
url: "/docs/linux/man/7-time_namespaces/"
description: "time_namespaces – overview of Linux time namespaces"
---

<p>time_namespaces &#8211; overview of Linux time namespaces</p>
<h2>Description</h2>
<p>Time namespaces virtualize the values of two system clocks:</p>
<dl>
<dt>&bull;</p>
<dd><code>CLOCK_MONOTONIC</code> (and likewise <code>CLOCK_MONOTONIC_COARSE</code> and <code>CLOCK_MONOTONIC_RAW</code>), a nonsettable clock that represents monotonic time since&#8212;as described by POSIX&#8212;&quot;some unspecified point in the past&quot;.</p>
<dt>&bull;</p>
<dd><code>CLOCK_BOOTTIME</code> (and likewise <code>CLOCK_BOOTTIME_ALARM</code>), a nonsettable clock that is identical to <code>CLOCK_MONOTONIC</code>, except that it also includes any time that the system is suspended.</dl>
<p> Thus, the processes in a time namespace share per-namespace values for these clocks. This affects various APIs that measure against these clocks, including: <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_settime/">timerfd_settime</a></code>(2), and <i>/proc/uptime</i>. Currently, the only way to create a time namespace is by calling <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) with the <code>CLONE_NEWTIME</code> flag. This call creates a new time namespace but does <i>not</i> place the calling process in the new namespace. Instead, the calling process&#8217;s subsequently created children are placed in the new namespace. This allows clock offsets (see below) for the new namespace to be set before the first process is placed in the namespace. The <i>/proc/[pid]/ns/time_for_children</i> symbolic link shows the time namespace in which the children of a process will be created. (A process can use a file descriptor opened on this symbolic link in a call to <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) in order to move into the namespace.)</p>
<h3>/proc/PID/timens_offsets</h3>
<p>Associated with each time namespace are offsets, expressed with respect to the initial time namespace, that define the values of the monotonic and boot-time clocks in that namespace. These offsets are exposed via the file <i>/proc/PID/timens_offsets</i>. Within this file, the offsets are expressed as lines consisting of three space-delimited fields: </p>
<pre><code>&lt;clock-id&gt; &lt;offset-secs&gt; &lt;offset-nanosecs&gt;</code></pre>
<p> The <i>clock-id</i> is a string that identifies the clock whose offsets are being shown. This field is either <i>monotonic</i>, for <code>CLOCK_MONOTONIC</code>, or <i>boottime</i>, for <code>CLOCK_BOOTTIME</code>. The remaining fields express the offset (seconds plus nanoseconds) for the clock in this time namespace. These offsets are expressed relative to the clock values in the initial time namespace. The <i>offset-secs</i> value can be negative, subject to restrictions noted below; <i>offset-nanosecs</i> is an unsigned value. In the initial time namespace, the contents of the <i>timens_offsets</i> file are as follows: $ <code>cat /proc/self/timens_offsets</code> monotonic 0 0 boottime 0 0 In a new time namespace that has had no member processes, the clock offsets can be modified by writing newline-terminated records of the same form to the <i>timens_offsets</i> file. The file can be written to multiple times, but after the first process has been created in or has entered the namespace, <code><a href="/docs/linux/man/2-write/">write</a></code>(2)s on this file fail with the error <code>EACCES</code>. In order to write to the <i>timens_offsets</i> file, a process must have the <code>CAP_SYS_TIME</code> capability in the user namespace that owns the time namespace. Writes to the <i>timens_offsets</i> file can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>An <i>offset-nanosecs</i> value is greater than 999,999,999.</p>
<dt><code>EINVAL</code></p>
<dd>A <i>clock-id</i> value is not valid.</p>
<dt><code>EPERM</code></p>
<dd>The caller does not have the <code>CAP_SYS_TIME</code> capability.</p>
<dt><code>ERANGE</code></p>
<dd>An <i>offset-secs</i> value is out of range. In particular;</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><i>offset-secs</i> can&#8217;t be set to a value which would make the current time on the corresponding clock inside the namespace a negative value; and</p>
<dt>&bull;</p>
<dd><i>offset-secs</i> can&#8217;t be set to a value such that the time on the corresponding clock inside the namespace would exceed half of the value of the kernel constant <code>KTIME_SEC_MAX</code> (this limits the clock value to a maximum of approximately 146 years).</dl>
</dl>
</dl>
<p> In a new time namespace created by <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), the contents of the <i>timens_offsets</i> file are inherited from the time namespace of the creating process.</p>
<h2>Notes</h2>
<p>Use of time namespaces requires a kernel that is configured with the <code>CONFIG_TIME_NS</code> option. </p>
<p> Note that time namespaces do not virtualize the <code>CLOCK_REALTIME</code> clock. Virtualization of this clock was avoided for reasons of complexity and overhead within the kernel. </p>
<p> For compatibility with the initial implementation, when writing a <i>clock-id</i> to the <i>/proc/[pid]/timens_offsets</i> file, the numerical values of the IDs can be written instead of the symbolic names show above; i.e., 1 instead of <i>monotonic</i>, and 7 instead of <i>boottime</i>. For redability, the use of the symbolic names over the numbers is preferred. </p>
<p> The motivation for adding time namespaces was to allow the monotonic and boot-time clocks to maintain consistent values during container migration and checkpoint/restore.</p>
<h2>Examples</h2>
<p>The following shell session demonstrates the operation of time namespaces. We begin by displaying the inode number of the time namespace of a shell in the initial time namespace: </p>
<p> $ <code>readlink /proc/$$/ns/time</code> time:[4026531834] </p>
<p> Continuing in the initial time namespace, we display the system uptime using <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1) and use the <i>clock_times</i> example program shown in <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2) to display the values of various clocks: </p>
<p> $ <code>uptime &#8211;pretty</code> up 21 hours, 17 minutes $ <code>./clock_times</code> CLOCK_REALTIME : 1585989401.971 (18356 days + 8h 36m 41s) CLOCK_TAI : 1585989438.972 (18356 days + 8h 37m 18s) CLOCK_MONOTONIC: 56338.247 (15h 38m 58s) CLOCK_BOOTTIME : 76633.544 (21h 17m 13s) </p>
<p> We then use <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1) to create a time namespace and execute a <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) shell. From the new shell, we use the built-in <code>echo</code> command to write records to the <i>timens_offsets</i> file adjusting the offset for the <code>CLOCK_MONOTONIC</code> clock forward 2 days and the offset for the <code>CLOCK_BOOTTIME</code> clock forward 7 days: </p>
<p> $ <code>PS1=&quot;ns2# &quot; sudo unshare -T &#8212; bash &#8211;norc</code> ns2# <code>echo &quot;monotonic $((2*24*60*60)) 0&quot; &gt; /proc/$$/timens_offsets</code> ns2# <code>echo &quot;boottime $((7*24*60*60)) 0&quot; &gt; /proc/$$/timens_offsets</code> </p>
<p> Above, we started the <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) shell with the <code>&#8211;norc</code> options so that no start-up scripts were executed. This ensures that no child processes are created from the shell before we have a chance to update the <i>timens_offsets</i> file. </p>
<p> We then use <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) to display the contents of the <i>timens_offsets</i> file. The execution of <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) creates the first process in the new time namespace, after which further attempts to update the <i>timens_offsets</i> file produce an error. </p>
<p> ns2# <code>cat /proc/$$/timens_offsets</code> monotonic 172800 0 boottime 604800 0 ns2# <code>echo &quot;boottime $((9*24*60*60)) 0&quot; &gt; /proc/$$/timens_offsets</code> bash: echo: write error: Permission denied </p>
<p> Continuing in the new namespace, we execute <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1) and the <i>clock_times</i> example program: </p>
<p> ns2# <code>uptime &#8211;pretty</code> up 1 week, 21 hours, 18 minutes ns2# <code>./clock_times</code> CLOCK_REALTIME : 1585989457.056 (18356 days + 8h 37m 37s) CLOCK_TAI : 1585989494.057 (18356 days + 8h 38m 14s) CLOCK_MONOTONIC: 229193.332 (2 days + 15h 39m 53s) CLOCK_BOOTTIME : 681488.629 (7 days + 21h 18m 8s) </p>
<p> From the above output, we can see that the monotonic and boot-time clocks have different values in the new time namespace. </p>
<p> Examining the <i>/proc/[pid]/ns/time</i> and <i>/proc/[pid]/ns/time_for_children</i> symbolic links, we see that the shell is a member of the initial time namespace, but its children are created in the new namespace. </p>
<p> ns2# <code>readlink /proc/$$/ns/time</code> time:[4026531834] ns2# <code>readlink /proc/$$/ns/time_for_children</code> time:[4026532900] ns2# <code>readlink /proc/self/ns/time</code> # Creates a child process time:[4026532900] </p>
<p> Returning to the shell in the initial time namespace, we see that the monotonic and boot-time clocks are unaffected by the <i>timens_offsets</i> changes that were made in the other time namespace: </p>
<p> $ <code>uptime &#8211;pretty</code> up 21 hours, 19 minutes $ <code>./clock_times</code> CLOCK_REALTIME : 1585989401.971 (18356 days + 8h 38m 51s) CLOCK_TAI : 1585989438.972 (18356 days + 8h 39m 28s) CLOCK_MONOTONIC: 56338.247 (15h 41m 8s) CLOCK_BOOTTIME : 76633.544 (21h 19m 23s)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
