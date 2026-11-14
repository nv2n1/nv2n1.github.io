---
title: "time(1)"
name: "time"
section: "1"
letter: "t"
url: "/docs/linux/man/1-time/"
description: "time – run programs and summarize system resource usage"
---

<h2 class="name">NAME</h2>
<p> time &#8211; run programs and summarize system resource usage </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>time</code></p>
<dd> [ <code>-apqvV</code> ] [ <code>-f</code><i> FORMAT</i> ] [ <code>-o</code><i> FILE</i> ]<br />
 [ <code>&#8211;append</code> ] [ <code>&#8211;verbose</code> ] [ <code>&#8211;quiet</code> ] [ <code>&#8211;portability</code> ]<br />
 [ <code>&#8211;format=</code><i>FORMAT</i> ] [ <code>&#8211;output=</code><i>FILE</i> ] [ <code>&#8211;version</code> ]<br />
 [ <code>&#8211;help</code> ] <i>COMMAND</i> [ <i>ARGS</i> ]</dl>
<h2>DESCRIPTION</h2>
<p> <code>time</code> run the program <i>COMMAND</i> with any given arguments <i>ARG&#8230;</i>. When <i>COMMAND</i> finishes, <code>time</code> displays information about resources used by <i>COMMAND</i> (on the standard error output, by default). If <i>COMMAND</i> exits with non-zero status, <code>time</code> displays a warning message and the exit status. </p>
<p> <code>time</code> determines which information to display about the resources used by the <i>COMMAND</i> from the string <i>FORMAT</i>. If no format is specified on the command line, but the <code>TIME</code> environment variable is set, its value is used as the format. Otherwise, a default format built into <code>time</code> is used. </p>
<p> Options to <code>time</code> must appear on the command line before <i>COMMAND</i>. Anything on the command line after <i>COMMAND</i> is passed as arguments to <i>COMMAND</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i> FILE, </i><code>&#8211;output=</code><i>FILE </i></p>
<dd> Write the resource use statistics to <i>FILE</i> instead of to the standard error stream. By default, this overwrites the file, destroying the file&#8217;s previous contents. This option is useful for collecting information on interactive programs and programs that produce output on the standard error stream.</p>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd> Append the resource use information to the output file instead of overwriting it. This option is only useful with the `-o&#8217; or `&#8211;output&#8217; option.</p>
<dt><code>-f</code><i> FORMAT, </i><code>&#8211;format</code><i> FORMAT </i></p>
<dd> Use <i>FORMAT</i> as the format string that controls the output of <code>time</code>. See the below more information.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command line options and exit.</p>
<dt><code>-p</code>, <code>&#8211;portability</code></p>
<dd> Use the following format string, for conformance with POSIX standard 1003.2:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;real&nbsp;%e<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;user&nbsp;%U<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sys&nbsp;%S</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Use the built-in verbose format, which displays each available piece of information on the program&#8217;s resource use on its own line, with an English description of its meaning.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Do not report the status of the program even if it is different from zero.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number of <code>time</code> and exit. </p>
</dl>
<h2>FORMATTING THE OUTPUT</h2>
<p> The format string <i>FORMAT</i> controls the contents of the <code>time</code> output. The format string can be set using the `-f&#8217; or `&#8211;format&#8217;, `-v&#8217; or `&#8211;verbose&#8217;, or `-p&#8217; or `&#8211;portability&#8217; options. If they are not given, but the <i>TIME</i> environment variable is set, its value is used as the format string. Otherwise, a built-in default format is used. The default format is:<br />
&nbsp;<wbr>&nbsp;%Uuser&nbsp;%Ssystem&nbsp;%Eelapsed&nbsp;%PCPU&nbsp;(%Xtext+%Ddata&nbsp;%Mmax)k<br />
&nbsp;<wbr>&nbsp;%Iinputs+%Ooutputs&nbsp;(%Fmajor+%Rminor)pagefaults&nbsp;%Wswaps </p>
<p> The format string usually consists of `resource specifiers&#8217; interspersed with plain text. A percent sign (`%&#8217;) in the format string causes the following character to be interpreted as a resource specifier, which is similar to the formatting characters in the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) function. </p>
<p> A backslash (`\&#8217;) introduces a `backslash escape&#8217;, which is translated into a single printing character upon output. `	&#8217; outputs a tab character, `
&#8217; outputs a newline, and `\&#8217; outputs a backslash. A backslash followed by any other character outputs a question mark (`?&#8217;) followed by a backslash, to indicate that an invalid backslash escape was given. </p>
<p> Other text in the format string is copied verbatim to the output. <code>time</code> always prints a newline after printing the resource use information, so normally format strings do not end with a newline character (or `
&#8217;). </p>
<p> There are many resource specifications. Not all resources are measured by all versions of Unix, so some of the values might be reported as zero. Any character following a percent sign that is not listed in the table below causes a question mark (`?&#8217;) to be output, followed by that character, to indicate that an invalid resource specifier was given. </p>
<p> The resource specifiers, which are a superset of those recognized by the <code><a href="/docs/linux/man/1-tcsh/">tcsh</a></code>(1) builtin `time&#8217; command, are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%</p>
<dd> A literal `%&#8217;.</p>
<dt>C</p>
<dd> Name and command line arguments of the command being timed.</p>
<dt>D</p>
<dd> Average size of the process&#8217;s unshared data area, in Kilobytes.</p>
<dt>E</p>
<dd> Elapsed real (wall clock) time used by the process, in [hours:]minutes:seconds.</p>
<dt>F</p>
<dd> Number of major, or I/O-requiring, page faults that occurred while the process was running. These are faults where the page has actually migrated out of primary memory.</p>
<dt>I</p>
<dd> Number of file system inputs by the process.</p>
<dt>K</p>
<dd> Average total (data+stack+text) memory use of the process, in Kilobytes.</p>
<dt>M</p>
<dd> Maximum resident set size of the process during its lifetime, in Kilobytes.</p>
<dt>O</p>
<dd> Number of file system outputs by the process.</p>
<dt>P</p>
<dd> Percentage of the CPU that this job got. This is just user + system times divided by the total running time. It also prints a percentage sign.</p>
<dt>R</p>
<dd> Number of minor, or recoverable, page faults. These are pages that are not valid (so they fault) but which have not yet been claimed by other virtual pages. Thus the data in the page is still valid but the system tables must be updated.</p>
<dt>S</p>
<dd> Total number of CPU-seconds used by the system on behalf of the process (in kernel mode), in seconds.</p>
<dt>U</p>
<dd> Total number of CPU-seconds that the process used directly (in user mode), in seconds.</p>
<dt>W</p>
<dd> Number of times the process was swapped out of main memory.</p>
<dt>X</p>
<dd> Average amount of shared text in the process, in Kilobytes.</p>
<dt>Z</p>
<dd> System&#8217;s page size, in bytes. This is a per-system constant, but varies between systems.</p>
<dt>c</p>
<dd> Number of times the process was context-switched involuntarily (because the time slice expired).</p>
<dt>e</p>
<dd> Elapsed real (wall clock) time used by the process, in seconds.</p>
<dt>k</p>
<dd> Number of signals delivered to the process.</p>
<dt>p</p>
<dd> Average unshared stack size of the process, in Kilobytes.</p>
<dt>r</p>
<dd> Number of socket messages received by the process.</p>
<dt>s</p>
<dd> Number of socket messages sent by the process.</p>
<dt>t</p>
<dd> Average resident set size of the process, in Kilobytes.</p>
<dt>w</p>
<dd> Number of times that the program was context-switched voluntarily, for instance while waiting for an I/O operation to complete.</p>
<dt>x</p>
<dd> Exit status of the command.</p>
<dl>
<dt>
<dd>
</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<p> To run the command `wc /etc/hosts&#8217; and show the default information:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time wc&nbsp;/etc/hosts </p>
<p> To run the command `ls -Fs&#8217; and show just the user, system, and total time:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time -f&nbsp;&quot;	%E real,	%U user,	%S sys&quot;&nbsp;ls -Fs </p>
<p> To edit the file BORK and have `time&#8217; append the elapsed time and number of signals to the file `log&#8217;, reading the format string from the environment variable `TIME&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;export TIME=&quot;	%E,	%k&quot;&nbsp;#&nbsp;If using bash or ksh<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setenv TIME&nbsp;&quot;	%E,	%k&quot;&nbsp;#&nbsp;If using csh or tcsh<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time -a -o log emacs bork </p>
<p> Users of the <code>bash</code> shell need to use an explicit path in order to run the external <code>time</code> command and not the shell builtin variant. On system where <code>time</code> is installed in <i>/usr/bin</i>, the first example would become<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/usr/bin/time wc&nbsp;/etc/hosts </p>
<h2>ACCURACY</h2>
<p> The elapsed time is not collected atomically with the execution of the program; as a result, in bizarre circumstances (if the <code>time</code> command gets stopped or swapped out in between when the program being timed exits and when <code>time</code> calculates how long it took to run), it could be much larger than the actual execution time. </p>
<p> When the running time of a command is very nearly zero, some values (e.g., the percentage of CPU used) may be reported as either zero (which is wrong) or a question mark. </p>
<p> Most information shown by <code>time</code> is derived from the <code><a href="/docs/linux/man/2-wait3/">wait3</a></code>(2) system call. The numbers are only as good as those returned by <code><a href="/docs/linux/man/2-wait3/">wait3</a></code>(2). On systems that do not have a <code><a href="/docs/linux/man/2-wait3/">wait3</a></code>(2) call that returns status information, the <code><a href="/docs/linux/man/2-times/">times</a></code>(2) system call is used instead. However, it provides much less information than <code><a href="/docs/linux/man/2-wait3/">wait3</a></code>(2), so on those systems <code>time</code> reports the majority of the resources as zero. </p>
<p> The `%I&#8217; and `%O&#8217; values are allegedly only `real&#8217; input and output and do not include those supplied by caching devices. The meaning of `real&#8217; I/O reported by `%I&#8217; and `%O&#8217; may be muddled for workstations, especially diskless ones. </p>
<h2>DIAGNOSTICS</h2>
<p> The <code>time</code> command returns when the program exits, stops, or is terminated by a signal. If the program exited normally, the return value of <code>time</code> is the return value of the program it executed and measured. Otherwise, the return value is 128 plus the number of the signal which caused the program to stop or terminate.</p>
<h2>AUTHOR</h2>
<p> <code>time</code> was written by David MacKenzie. This man page was added by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, the Debian GNU/Linux maintainer, for use by the Debian GNU/Linux distribution but may of course be used by others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcsh/">tcsh</a></code>(1), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) </p>
<h2>Index</h2>
