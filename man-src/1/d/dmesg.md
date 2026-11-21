---
title: "dmesg(1)"
name: "dmesg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmesg/"
description: "dmesg – print or control the kernel ring buffer"
---
<h2 class="name">NAME</h2>
<p> dmesg - print or control the kernel ring buffer </p>
<h2>SYNOPSIS</h2>
<p> <code>dmesg</code> [options] </p>
<p> <code>dmesg</code> <code>--clear</code> </p>
<p> <code>dmesg</code> <code>--read-clear</code> [options] </p>
<p> <code>dmesg</code> <code>--console-level</code> <i>level</i> </p>
<p> <code>dmesg</code> <code>--console-on</code> </p>
<p> <code>dmesg</code> <code>--console-off</code>  </p>
<h2>DESCRIPTION</h2>
<p> <code>dmesg</code> is used to examine or control the kernel ring buffer. </p>
<p> The default action is to display all messages from the kernel ring buffer.  </p>
<h2>OPTIONS</h2>
<p> The <code>--clear</code>, <code>--read-clear</code>, <code>--console-on</code>, <code>--console-off</code>, and <code>--console-level</code> options are mutually exclusive. </p>
<p> <code>-C</code>, <code>--clear</code> </p>
<dl>
<dd> <p> Clear the ring buffer. </p>
 </dd></dl>
<p> <code>-c</code>, <code>--read-clear</code> </p>
<dl>
<dd> <p> Clear the ring buffer after first printing its contents. </p>
 </dd></dl>
<p> <code>-D</code>, <code>--console-off</code> </p>
<dl>
<dd> <p> Disable the printing of messages to the console. </p>
 </dd></dl>
<p> <code>-d</code>, <code>--show-delta</code> </p>
<dl>
<dd> <p> Display the timestamp and the time delta spent between messages. If used together with <code>--notime</code> then only the time delta without the timestamp is printed. </p>
 </dd></dl>
<p> <code>-E</code>, <code>--console-on</code> </p>
<dl>
<dd> <p> Enable printing messages to the console. </p>
 </dd></dl>
<p> <code>-e</code>, <code>--reltime</code> </p>
<dl>
<dd> <p> Display the local time and the delta in human-readable format. Be aware that conversion to the local time could be inaccurate (see <code>-T</code> for more details). </p>
 </dd></dl>
<p> <code>-F</code>, <code>--file</code> <i>file</i> </p>
<dl>
<dd> <p> Read the syslog messages from the given <i>file</i>. Note that <code>-F</code> does not support messages in kmsg format. The old syslog format is supported only. </p>
 </dd></dl>
<p> <code>-f</code>, <code>--facility</code> <i>list</i> </p>
<dl>
<dd> <p> Restrict output to the given (comma-separated) <i>list</i> of facilities. For example: </p>
<p> <code>dmesg --facility=daemon</code> </p>
<p> will print messages from system daemons only. For all supported facilities see the <code>--help</code> output. </p>
 </dd></dl>
<p> <code>-H</code>, <code>--human</code> </p>
<dl>
<dd> <p> Enable human-readable output. See also <code>--color</code>, <code>--reltime</code> and <code>--nopager</code>. </p>
 </dd></dl>
<p> <code>-k</code>, <code>--kernel</code> </p>
<dl>
<dd> <p> Print kernel messages. </p>
 </dd></dl>
<p> <code>-L</code>, <code>--color</code>[=<i>when</i>] </p>
<dl>
<dd> <p> Colorize the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>--help</code> output. See also the <code>COLORS</code> section below. </p>
 </dd></dl>
<p> <code>-l</code>, <code>--level</code> <i>list</i> </p>
<dl>
<dd> <p> Restrict output to the given (comma-separated) <i>list</i> of levels. For example: </p>
<p> <code>dmesg --level=err,warn</code> </p>
<p> will print error and warning messages only. For all supported levels see the <code>--help</code> output. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--console-level</code> <i>level</i> </p>
<dl>
<dd> <p> Set the <i>level</i> at which printing of messages is done to the console. The <i>level</i> is a level number or abbreviation of the level name. For all supported levels see the <code>--help</code> output. </p>
<p> For example, <code>-n 1</code> or <code>-n emerg</code> prevents all messages, except emergency (panic) messages, from appearing on the console. All levels of messages are still written to <i>/proc/kmsg</i>, so <code>syslogd</code>(8) can still be used to control exactly where kernel messages appear. When the <code>-n</code> option is used, <code>dmesg</code> will <i>not</i> print or clear the kernel ring buffer. </p>
 </dd></dl>
<p> <code>--noescape</code> </p>
<dl>
<dd> <p> The unprintable and potentially unsafe characters (e.g., broken multi-byte sequences, terminal controlling chars, etc.) are escaped in format \x&lt;hex&gt; for security reason by default. This option disables this feature at all. It&#8217;s usable for example for debugging purpose together with <code>--raw</code>. Be careful and don&#8217;t use it by default. </p>
 </dd></dl>
<p> <code>-P</code>, <code>--nopager</code> </p>
<dl>
<dd> <p> Do not pipe output into a pager. A pager is enabled by default for <code>--human</code> output. </p>
 </dd></dl>
<p> <code>-p</code>, <code>--force-prefix</code> </p>
<dl>
<dd> <p> Add facility, level or timestamp information to each line of a multi-line message. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Print the raw message buffer, i.e., do not strip the log-level prefixes, but all unprintable characters are still escaped (see also <code>--noescape</code>). </p>
<p> Note that the real raw format depends on the method how <code>dmesg</code> reads kernel messages. The <i>/dev/kmsg</i> device uses a different format than <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2). For backward compatibility, <code>dmesg</code> returns data always in the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) format. It is possible to read the real raw data from <i>/dev/kmsg</i> by, for example, the command &#8216;dd if=/dev/kmsg iflag=nonblock&#8217;. </p>
 </dd></dl>
<p> <code>-S</code>, <code>--syslog</code> </p>
<dl>
<dd> <p> Force <code>dmesg</code> to use the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) kernel interface to read kernel messages. The default is to use <i>/dev/kmsg</i> rather than <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) since kernel 3.5.0. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--buffer-size</code> <i>size</i> </p>
<dl>
<dd> <p> Use a buffer of <i>size</i> to query the kernel ring buffer. This is 16392 by default. (The default kernel syslog buffer size was 4096 at first, 8192 since 1.3.54, 16384 since 2.1.113.) If you have set the kernel buffer to be larger than the default, then this option can be used to view the entire buffer. </p>
 </dd></dl>
<p> <code>-T</code>, <code>--ctime</code> </p>
<dl>
<dd> <p> Print human-readable timestamps. </p>
<p> <code>Be aware that the timestamp could be inaccurate!</code> The <code>time</code> source used for the logs is <code>not updated after</code> system <code>SUSPEND</code>/<code>RESUME</code>. Timestamps are adjusted according to current delta between boottime and monotonic clocks, this works only for messages printed after last resume. </p>
 </dd></dl>
<p> <code>--since</code> <i>time</i> </p>
<dl>
<dd> <p> Display record since the specified time. The time is possible to specify in absolute way as well as by relative notation (e.g. &#8216;1 hour ago&#8217;). Be aware that the timestamp could be inaccurate and see <code>--ctime</code> for more details. </p>
 </dd></dl>
<p> <code>--until</code> <i>time</i> </p>
<dl>
<dd> <p> Display record until the specified time. The time is possible to specify in absolute way as well as by relative notation (e.g. &#8216;1 hour ago&#8217;). Be aware that the timestamp could be inaccurate and see <code>--ctime</code> for more details. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--notime</code> </p>
<dl>
<dd> <p> Do not print kernel&#8217;s timestamps. </p>
 </dd></dl>
<p> <code>--time-format</code> <i>format</i> </p>
<dl>
<dd> <p> Print timestamps using the given <i>format</i>, which can be <code>ctime</code>, <code>reltime</code>, <code>delta</code> or <code>iso</code>. The first three formats are aliases of the time-format-specific options. The <code>iso</code> format is a <code>dmesg</code> implementation of the ISO-8601 timestamp format. The purpose of this format is to make the comparing of timestamps between two systems, and any other parsing, easy. The definition of the <code>iso</code> timestamp is: YYYY-MM-DD&lt;T&gt;HH:MM:SS,&lt;microseconds&gt;&larr;+&gt;&lt;timezone offset from UTC&gt;. </p>
<p> The <code>iso</code> format has the same issue as <code>ctime</code>: the time may be inaccurate when a system is suspended and resumed. </p>
 </dd></dl>
<p> <code>-u</code>, <code>--userspace</code> </p>
<dl>
<dd> <p> Print userspace messages. </p>
 </dd></dl>
<p> <code>-w</code>, <code>--follow</code> </p>
<dl>
<dd> <p> Wait for new messages. This feature is supported only on systems with a readable <i>/dev/kmsg</i> (since kernel 3.5.0). </p>
 </dd></dl>
<p> <code>-W</code>, <code>--follow-new</code> </p>
<dl>
<dd> <p> Wait and print only new messages. </p>
 </dd></dl>
<p> <code>-x</code>, <code>--decode</code> </p>
<dl>
<dd> <p> Decode facility and level (priority) numbers to human-readable prefixes. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<h2>COLORS</h2>
<p> Implicit coloring can be disabled by an empty file <i>/etc/terminal-colors.d/dmesg.disable</i>. See <code>terminal-colors.d</code>(5) for more details about colorization configuration. </p>
<p> The logical color names supported by <code>dmesg</code> are: </p>
<p> <code>subsys</code> </p>
<dl>
<dd> <p> The message sub-system prefix (e.g., &quot;ACPI:&quot;). </p>
 </dd></dl>
<p> <code>time</code> </p>
<dl>
<dd> <p> The message timestamp. </p>
 </dd></dl>
<p> <code>timebreak</code> </p>
<dl>
<dd> <p> The message timestamp in short ctime format in <code>--reltime</code> or <code>--human</code> output. </p>
 </dd></dl>
<p> <code>alert</code> </p>
<dl>
<dd> <p> The text of the message with the alert log priority. </p>
 </dd></dl>
<p> <code>crit</code> </p>
<dl>
<dd> <p> The text of the message with the critical log priority. </p>
 </dd></dl>
<p> <code>err</code> </p>
<dl>
<dd> <p> The text of the message with the error log priority. </p>
 </dd></dl>
<p> <code>warn</code> </p>
<dl>
<dd> <p> The text of the message with the warning log priority. </p>
 </dd></dl>
<p> <code>segfault</code> </p>
<dl>
<dd> <p> The text of the message that inform about segmentation fault. </p>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>dmesg</code> can fail reporting permission denied error. This is usually caused by <code>dmesg_restrict</code> kernel setting, please see <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) for more details.  </p>
<h2>AUTHORS</h2>
<p> <code>dmesg</code> was originally written by  </p>
<h2>SEE ALSO</h2>
<p> <code>terminal-colors.d</code>(5), <code>syslogd</code>(8)  </p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>dmesg</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COLORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">EXIT STATUS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">AVAILABILITY</a></dt>
<dd>  </dd></dl>
