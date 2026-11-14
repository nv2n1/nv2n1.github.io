---
title: "iotop(8)"
name: "iotop"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iotop/"
description: "iotop – simple top-like I/O monitor"
---

<p>iotop &#8211; simple top-like I/O monitor</p>
<h2>Synopsis</h2>
<p><code>iotop</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>iotop watches I/O usage information output by the Linux kernel (requires 2.6.20 or later) and displays a table of current I/O usage by processes or threads on the system. At least the CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING, CONFIG_TASKSTATS and CONFIG_VM_EVENT_COUNTERS options need to be enabled in your Linux kernel build configuration. </p>
<p> iotop displays columns for the I/O bandwidth read and written by each process/thread during the sampling period. It also displays the percentage of time the thread/process spent while swapping in and while waiting on I/O. For each process, its I/O priority (class/level) is shown. </p>
<p> In addition, the total I/O bandwidth read and written during the sampling period is displayed at the top of the interface. <code>Total DISK READ</code> and <code>Total DISK WRITE</code> values represent total read and write bandwidth between processes and kernel threads on the one side and kernel block device subsystem on the other. While <code>Current DISK READ</code> and <code>Current DISK WRITE</code> values represent corresponding bandwidths for current disk I/O between kernel block device subsystem and underlying hardware (HDD, SSD, etc.). Thus <code>Total</code> and <code>Current</code> values may not be equal at any given moment of time due to data caching and I/O operations reordering that take place inside Linux kernel. </p>
<p> Use the left and right arrows to change the sorting, r to reverse the sorting order, o to toggle the &#8211;only option, p to toggle the &#8211;processes option, a to toggle the &#8211;accumulated option, q to quit or i to change the priority of a thread or a process&#8217; thread(s). Any other key will force a refresh.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Show the version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show usage information and exit</p>
<dt><code>-o</code>, <code>&#8211;only</code></p>
<dd>Only show processes or threads actually doing I/O, instead of showing all processes or threads. This can be dynamically toggled by pressing o.</p>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd>Turn on non-interactive mode. Useful for logging I/O usage over time.</p>
<dt><code>-n</code> NUM, <code>&#8211;iter</code>=<i>NUM</i></p>
<dd>Set the number of iterations before quitting (never quit by default). This is most useful in non-interactive mode.</p>
<dt><code>-d</code> SEC, <code>&#8211;delay</code>=<i>SEC</i></p>
<dd>Set the delay between iterations in seconds (1 second by default). Accepts non-integer values such as 1.1 seconds.</p>
<dt><code>-p</code> PID, <code>&#8211;pid</code>=<i>PID</i></p>
<dd>A list of processes/threads to monitor (all by default).</p>
<dt><code>-u</code> USER, <code>&#8211;user</code>=<i>USER</i></p>
<dd>A list of users to monitor (all by default)</p>
<dt><code>-P</code>, <code>&#8211;processes</code></p>
<dd>Only show processes. Normally iotop shows all threads.</p>
<dt><code>-a</code>, <code>&#8211;accumulated</code></p>
<dd>Show accumulated I/O instead of bandwidth. In this mode, iotop shows the amount of I/O processes have done since iotop started.</p>
<dt><code>-k</code>, <code>&#8211;kilobytes</code></p>
<dd>Use kilobytes instead of a human friendly unit. This mode is useful when scripting the batch mode of iotop. Instead of choosing the most appropriate unit iotop will display all sizes in kilobytes.</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd>Add a timestamp on each line (implies &#8211;batch). Each line will be prefixed by the current time.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>suppress some lines of header (implies &#8211;batch). This option can be specified up to three times to remove header lines.</p>
<dt><code>&#8211;no-help</code></p>
<dd>Suppress the keyboard shortcuts help display.</p>
<dl>
<dd>
<dl>
<dt><code>-q</code></p>
<dd>column names are only printed on the first iteration,</p>
<dt><code>-qq</code></p>
<dd>column names are never printed,</p>
<dt><code>-qqq</code></p>
<dd>the I/O summary is never printed.</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-vmstat/">vmstat</a></code>(1), <code><a href="/docs/linux/man/1-atop/">atop</a></code>(1), <code><a href="/docs/linux/man/1-htop/">htop</a></code>(1)</p>
<h2>Author</h2>
<p>iotop was written by Guillaume Chazarain. </p>
<p> This manual page was started by Paul Wise for the Debian project and is placed in the public domain.</p>
