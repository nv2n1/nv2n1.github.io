---
title: "syslog(2)"
name: "syslog"
section: "2"
letter: "s"
url: "/docs/linux/man/2-syslog/"
description: "syslog, klogctl – read and/or clear kernel message ring buffer; set console_loglevel"
---

<h2 class="name">NAME</h2>
<p> syslog, klogctl &#8211; read and/or clear kernel message ring buffer; set console_loglevel </p>
<h2>SYNOPSIS</h2>
<pre><code>
int syslog(int type, char *bufp, int len);
/* No wrapper provided in glibc */
/* The glibc interface */
#include &lt;sys/klog.h&gt;
int klogctl(int type, char *bufp, int len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: Probably, you are looking for the C library function <code>syslog</code>(), which talks to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8); see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for details. </p>
<p> This page describes the kernel <code>syslog</code>() system call, which is used to control the kernel <i>printk</i>() buffer; the glibc wrapper function for the system call is called <code>klogctl</code>().</p>
<h3>The kernel log buffer</h3>
<p> The kernel has a cyclic buffer of length <code>LOG_BUF_LEN</code> in which messages given as arguments to the kernel function <code>printk</code>() are stored (regardless of their log level). In early kernels, <code>LOG_BUF_LEN</code> had the value 4096; from kernel 1.3.54, it was 8192; from kernel 2.1.113, it was 16384; since kernel 2.4.23/2.6, the value is a kernel configuration option (<code>CONFIG_LOG_BUF_SHIFT</code>, default value dependent on the architecture). Since Linux 2.6.6, the size can be queried with command type 10 (see below).</p>
<h3>Commands</h3>
<p> The <i>type</i> argument determines the action taken by this function. The list below specifies the values for <i>type</i>. The symbolic names are defined in the kernel source, but are not exported to user space; you will either need to use the numbers, or define the names yourself.</p>
<dl>
<dt><code>SYSLOG_ACTION_CLOSE</code> (0)</p>
<dd> Close the log. Currently a NOP.</p>
<dt><code>SYSLOG_ACTION_OPEN</code> (1)</p>
<dd> Open the log. Currently a NOP.</p>
<dt><code>SYSLOG_ACTION_READ</code> (2)</p>
<dd> Read from the log. The call waits until the kernel log buffer is nonempty, and then reads at most <i>len</i> bytes into the buffer pointed to by <i>bufp</i>. The call returns the number of bytes read. Bytes read from the log disappear from the log buffer: the information can be read only once. This is the function executed by the kernel when a user program reads <i>/proc/kmsg</i>.</p>
<dt><code>SYSLOG_ACTION_READ_ALL</code> (3)</p>
<dd> Read all messages remaining in the ring buffer, placing them in the buffer pointed to by <i>bufp</i>. The call reads the last <i>len</i> bytes from the log buffer (nondestructively), but will not read more than was written into the buffer since the last &quot;clear ring buffer&quot; command (see command 5 below)). The call returns the number of bytes read.</p>
<dt><code>SYSLOG_ACTION_READ_CLEAR</code> (4)</p>
<dd> Read and clear all messages remaining in the ring buffer. The call does precisely the same as for a <i>type</i> of 3, but also executes the &quot;clear ring buffer&quot; command.</p>
<dt><code>SYSLOG_ACTION_CLEAR</code> (5)</p>
<dd> The call executes just the &quot;clear ring buffer&quot; command. The <i>bufp</i> and <i>len</i> arguments are ignored.</p>
<dt>
<dd> This command does not really clear the ring buffer. Rather, it sets a kernel bookkeeping variable that determines the results returned by commands 3 (<code>SYSLOG_ACTION_READ_ALL</code>) and 4 (<code>SYSLOG_ACTION_READ_CLEAR</code>). This command has no effect on commands 2 (<code>SYSLOG_ACTION_READ</code>) and 9 (<code>SYSLOG_ACTION_SIZE_UNREAD</code>).</p>
<dt><code>SYSLOG_ACTION_CONSOLE_OFF</code> (6)</p>
<dd> The command saves the current value of <i>console_loglevel</i> and then sets <i>console_loglevel</i> to <i>minimum_console_loglevel</i>, so that no messages are printed to the console. Before Linux 2.6.32, the command simply sets <i>console_loglevel</i> to <i>minimum_console_loglevel</i>. See the discussion of <i>/proc/sys/kernel/printk</i>, below.</p>
<dt>
<dd> The <i>bufp</i> and <i>len</i> arguments are ignored.</p>
<dt><code>SYSLOG_ACTION_CONSOLE_ON</code> (7)</p>
<dd> If a previous <code>SYSLOG_ACTION_CONSOLE_OFF</code> command has been performed, this command restores <i>console_loglevel</i> to the value that was saved by that command. Before Linux 2.6.32, this command simply sets <i>console_loglevel</i> to <i>default_console_loglevel</i>. See the discussion of <i>/proc/sys/kernel/printk</i>, below.</p>
<dt>
<dd> The <i>bufp</i> and <i>len</i> arguments are ignored.</p>
<dt><code>SYSLOG_ACTION_CONSOLE_LEVEL</code> (8)</p>
<dd> The call sets <i>console_loglevel</i> to the value given in <i>len</i>, which must be an integer between 1 and 8 (inclusive). The kernel silently enforces a minimum value of <i>minimum_console_loglevel</i> for <i>len</i>. See the <i>log level</i> section for details. The <i>bufp</i> argument is ignored.</p>
<dt><code>SYSLOG_ACTION_SIZE_UNREAD</code> (9) (since Linux 2.4.10)</p>
<dd> The call returns the number of bytes currently available to be read from the kernel log buffer via command 2 (<code>SYSLOG_ACTION_READ</code>). The <i>bufp</i> and <i>len</i> arguments are ignored.</p>
<dt><code>SYSLOG_ACTION_SIZE_BUFFER</code> (10) (since Linux 2.6.6)</p>
<dd> This command returns the total size of the kernel log buffer. The <i>bufp</i> and <i>len</i> arguments are ignored.</dl>
<p> All commands except 3 and 10 require privilege. In Linux kernels before 2.6.37, command types 3 and 10 are allowed to unprivileged processes; since Linux 2.6.37, these commands are allowed to unprivileged processes only if <i>/proc/sys/kernel/dmesg_restrict</i> has the value 0. Before Linux 2.6.37, &quot;privileged&quot; means that the caller has the <code>CAP_SYS_ADMIN</code> capability. Since Linux 2.6.37, &quot;privileged&quot; means that the caller has either the <code>CAP_SYS_ADMIN</code> capability (now deprecated for this purpose) or the (new) <code>CAP_SYSLOG</code> capability.</p>
<h3>/proc/sys/kernel/printk</h3>
<p> <i>/proc/sys/kernel/printk</i> is a writable file containing four integer values that influence kernel <i>printk()</i> behavior when printing or logging error messages. The four values are:</p>
<dl>
<dt><i>console_loglevel</i></p>
<dd> Only messages with a log level lower than this value will be printed to the console. The default value for this field is <code>DEFAULT_CONSOLE_LOGLEVEL</code> (7), but it is set to 4 if the kernel command line contains the word &quot;quiet&quot;,10 if the kernel command line contains the word &quot;debug&quot;, and to 15 in case of a kernel fault (the 10 and 15 are just silly, and equivalent to 8). The value of <i>console_loglevel</i> can be set (to a value in the range 1-8) by a <code>syslog</code>() call with a <i>type</i> of 8.</p>
<dt><i>default_message_loglevel</i></p>
<dd> This value will be used as the log level for <i>printk()</i> messages that do not have an explicit level. Up to and including Linux 2.6.38, the hard-coded default value for this field was 4 (<code>KERN_WARNING</code>); since Linux 2.6.39, the default value is a defined by the kernel configuration option <code>CONFIG_DEFAULT_MESSAGE_LOGLEVEL</code>, which defaults to 4.</p>
<dt><i>minimum_console_loglevel</i></p>
<dd> The value in this field is the minimum value to which <i>console_loglevel</i> can be set.</p>
<dt><i>default_console_loglevel</i></p>
<dd> This is the default value for <i>console_loglevel</i>.</dl>
<h3>The log level</h3>
<p> Every <i>printk</i>() message has its own log level. If the log level is not explicitly specified as part of the message, it defaults to <i>default_message_loglevel</i>. The conventional meaning of the log level is as follows: </p>
<table>
<tr VALIGN=top>
<td><code>Kernel constant</code></td>
<td><code>Level value</code></td>
<td><code>Meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_EMERG</code></td>
<td ALIGN=center>0</td>
<td>System is unusable
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_ALERT</code></td>
<td ALIGN=center>1</td>
<td>Action must be taken immediately
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_CRIT</code></td>
<td ALIGN=center>2</td>
<td>Critical conditions
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_ERR</code></td>
<td ALIGN=center>3</td>
<td>Error conditions
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_WARNING</code></td>
<td ALIGN=center>4</td>
<td>Warning conditions
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_NOTICE</code></td>
<td ALIGN=center>5</td>
<td>Normal but significant condition
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_INFO</code></td>
<td ALIGN=center>6</td>
<td>Informational
</td>
</tr>
<tr VALIGN=top>
<td><code>KERN_DEBUG</code></td>
<td ALIGN=center>7</td>
<td>Debug-level messages
</td>
</tr>
</table>
<p> The kernel <i>printk()</i> routine will print a message on the console only if it has a log level less than the value of <i>console_loglevel</i>.</p>
<h2>RETURN VALUE</h2>
<p> For <i>type</i> equal to 2, 3, or 4, a successful call to <code>syslog</code>() returns the number of bytes read. For <i>type</i> 9, <code>syslog</code>() returns the number of bytes currently available to be read on the kernel log buffer. For <i>type</i> 10, <code>syslog</code>() returns the total size of the kernel log buffer. For other values of <i>type</i>, 0 is returned on success. </p>
<p> In case of error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> Bad arguments (e.g., bad <i>type</i>; or for <i>type</i> 2, 3, or 4, <i>buf</i> is NULL, or <i>len</i> is less than zero; or for <i>type</i> 8, the <i>level</i> is outside the range 1 to 8).</p>
<dt><code>ENOSYS</code></p>
<dd> This <code>syslog</code>() system call is not available, because the kernel was compiled with the <code>CONFIG_PRINTK</code> kernel-configuration option disabled.</p>
<dt><code>EPERM</code></p>
<dd> An attempt was made to change <i>console_loglevel</i> or clear the kernel message ring buffer by a process without sufficient privilege (more precisely: without the <code>CAP_SYS_ADMIN</code> or <code>CAP_SYSLOG</code> capability).</p>
<dt><code>ERESTARTSYS</code></p>
<dd> System call was interrupted by a signal; nothing was read. (This can be seen only during a trace.)</dl>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> From the very start, people noted that it is unfortunate that a system call and a library routine of the same name are entirely different animals.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
