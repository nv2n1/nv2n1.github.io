---
title: "pv(1)"
name: "pv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pv/"
description: "pv – monitor the progress of data through a pipe"
---

<h2 class="name">NAME</h2>
<p> pv &#8211; monitor the progress of data through a pipe </p>
<h2>SYNOPSIS</h2>
<p> <code>pv</code> [<i>OPTION</i>] [<i>FILE</i>]&#8230;<br />
 <code>pv</code> [<i>-h</i>|<i>-V</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pv</code> shows the progress of data through a pipeline by giving information such as time elapsed, percentage completed (with progress bar), current throughput rate, total data transferred, and ETA. </p>
<p> To use it, insert it in a pipeline between two processes, with the appropriate options. Its standard input will be passed through to its standard output and progress will be shown on standard error. </p>
<p> <code>pv</code> will copy each supplied <code>FILE</code> in turn to standard output (<code>&#8211;</code> means standard input), or if no <code>FILE</code>s are specified just standard input is copied. This is the same behaviour as <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1). </p>
<p> A simple example to watch how quickly a file is transferred using <code><a href="/docs/linux/man/1-nc/">nc</a></code>(1): </p>
<dl>
<dt>
<dd> <code>pv file | nc -w 1 somewhere.com 3000</code></dl>
<p> A similar example, transferring a file from another process and passing the expected size to <code>pv</code>: </p>
<dl>
<dt>
<dd> <code>cat file | pv -s 12345 | nc -w 1 somewhere.com 3000</code></dl>
<p> A more complicated example using numeric output to feed into the <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1) program for a full-screen progress display:<br />
&nbsp;</p>
<dl>
<dt>
<dd> <code>(tar cf &#8211; . \</code><br />
 <code> | pv -n -s $(du -sb . | awk &#8216;{print $1}&#8217;) \</code><br />
 <code> | gzip -9 &gt; out.tgz) 2&gt;&amp;1 \</code><br />
 <code>| dialog &#8211;gauge &#8216;Progress&#8217; 7 70</code></dl>
<p> Taking an image of a disk, skipping errors: </p>
<dl>
<dt>
<dd> <code>pv -EE /dev/sda &gt; disk-image.img</code></dl>
<p> Writing an image back to a disk: </p>
<dl>
<dt>
<dd> <code>pv disk-image.img &gt; /dev/sda</code></dl>
<p> Zeroing a disk: </p>
<dl>
<dt>
<dd> <code>pv &lt; /dev/zero &gt; /dev/sda</code></dl>
<p> Note that if the input size cannot be calculated, and the output is a block device, then the size of the block device will be used and <code>pv</code> will automatically stop at that size as if <code>-S</code> had been given. </p>
<p> (Linux only): Watching file descriptor 3 opened by another process 1234: </p>
<dl>
<dt>
<dd> <code>pv -d 1234:3</code></dl>
<p> (Linux only): Watching all file descriptors used by process 1234: </p>
<dl>
<dt>
<dd> <code>pv -d 1234</code></dl>
<h2>OPTIONS</h2>
<p> <code>pv</code> takes many options, which are divided into display switches, output modifiers, and general options. </p>
<h2>DISPLAY SWITCHES</h2>
<p> If no display switches are specified, <code>pv</code> behaves as if <code>-p</code>, <code>-t</code>, <code>-e</code>, <code>-r</code>, and <code>-b</code> had been given (i.e. everything except average rate is switched on). Otherwise, only those display types that are explicitly switched on will be shown.</p>
<dl>
<dt><code>-p, &#8211;progress</code></p>
<dd> Turn the progress bar on. If standard input is not a file and no size was given (with the <code>-s</code> modifier), the progress bar cannot indicate how close to completion the transfer is, so it will just move left and right to indicate that data is moving.</p>
<dt><code>-t, &#8211;timer</code></p>
<dd> Turn the timer on. This will display the total elapsed time that <code>pv</code> has been running for.</p>
<dt><code>-e, &#8211;eta</code></p>
<dd> Turn the ETA timer on. This will attempt to guess, based on previous transfer rates and the total data size, how long it will be before completion. This option will have no effect if the total data size cannot be determined.</p>
<dt><code>-I, &#8211;fineta</code></p>
<dd> Turn the ETA timer on, but display the estimated local time of arrival instead of time left. When the estimated time is more than 6 hours in the future, the date is shown as well.</p>
<dt><code>-r, &#8211;rate</code></p>
<dd> Turn the rate counter on. This will display the current rate of data transfer.</p>
<dt><code>-a, &#8211;average-rate</code></p>
<dd> Turn the average rate counter on. This will display the average rate of data transfer so far.</p>
<dt><code>-b, &#8211;bytes</code></p>
<dd> Turn the total byte counter on. This will display the total amount of data transferred so far.</p>
<dt><code>-T, &#8211;buffer-percent</code></p>
<dd> Turn on the transfer buffer percentage display. This will show the percentage of the transfer buffer in use &#8211; but see the caveat under <code>%T</code> in the <code>FORMATTING</code> section below.</p>
<dt><code>-A, &#8211;last-written NUM</code></p>
<dd> Show the last <code>NUM</code> bytes written &#8211; but see the caveat under <code>%nA</code> in the <code>FORMATTING</code> section below.</p>
<dt><code>-F, &#8211;format FORMAT</code></p>
<dd> Ignore the options <code>-p</code>, <code>-t</code>, <code>-e</code>, <code>-r</code>, <code>-a</code>, <code>-b</code>, <code>-T</code>, and <code>-A</code>, and instead use the format string <code>FORMAT</code> to determine the output format. See the <code>FORMATTING</code> section below.</p>
<dt><code>-n, &#8211;numeric</code></p>
<dd> Numeric output. Instead of giving a visual indication of progress, <code>pv</code> will give an integer percentage, one per line, on standard error, suitable for piping (via convoluted redirection) into <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1). Note that <code>-f</code> is not required if <code>-n</code> is being used.</p>
<dt>
<dd> Note that if <code>&#8211;numeric</code> is in use, then adding <code>&#8211;bytes</code> will cause the number of bytes processed so far to be output instead of a percentage; if <code>&#8211;line-mode</code> is also in use, then instead of bytes or a percentage, the number of lines so far is output. And finally, if <code>&#8211;timer</code> is also in use, then each output line is prefixed with the elapsed time so far, as a decimal number of seconds.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> No output. Useful if the <code>-L</code> option is being used on its own to just limit the transfer rate of a pipe. </p>
</dl>
<h2>OUTPUT MODIFIERS</h2>
<dl>
<dt><code>-W, &#8211;wait</code></p>
<dd> Wait until the first byte has been transferred before showing any progress information or calculating any ETAs. Useful if the program you are piping to or from requires extra information before it starts, eg piping data into <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) or <code><a href="/docs/linux/man/1-mcrypt/">mcrypt</a></code>(1) which require a passphrase before data can be processed.</p>
<dt><code>-D, &#8211;delay-start SEC</code></p>
<dd> Wait until <code>SEC</code> seconds have passed before showing any progress information, for example in a script where you only want to show a progress bar if it starts taking a long time. Note that this can be a decimal such as 0.5.</p>
<dt><code>-s SIZE, &#8211;size SIZE</code></p>
<dd> Assume the total amount of data to be transferred is <code>SIZE</code> bytes when calculating percentages and ETAs. The same suffixes of &quot;k&quot;, &quot;m&quot; etc can be used as with <code>-L</code>.</p>
<dt>
<dd> Has no effect if used with <code>-d PID</code> to watch all file descriptors of a process, but will work with <code>-d PID:FD</code>.</p>
<dt><code>-l, &#8211;line-mode</code></p>
<dd> Instead of counting bytes, count lines (newline characters). The progress bar will only move when a new line is found, and the value passed to the <code>-s</code> option will be interpreted as a line count. Note that file sizes are not automatically calculated when this option is used, to avoid having to read all files twice.</p>
<dt><code>-0, &#8211;null</code></p>
<dd> Count lines as null terminated. This option implies &#8211;line-mode.</p>
<dt><code>-i SEC, &#8211;interval SEC</code></p>
<dd> Wait <code>SEC</code> seconds between updates. The default is to update every second. Note that this can be a decimal such as 0.1.</p>
<dt><code>-w WIDTH, &#8211;width WIDTH</code></p>
<dd> Assume the terminal is <code>WIDTH</code> characters wide, instead of trying to work it out (or assuming 80 if it cannot be guessed).</p>
<dt><code>-H HEIGHT, &#8211;height HEIGHT</code></p>
<dd> Assume the terminal is <code>HEIGHT</code> rows high, instead of trying to work it out (or assuming 25 if it cannot be guessed).</p>
<dt><code>-N NAME, &#8211;name NAME</code></p>
<dd> Prefix the output information with <code>NAME</code>. Useful in conjunction with <code>-c</code> if you have a complicated pipeline and you want to be able to tell different parts of it apart.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force output. Normally, <code>pv</code> will not output any visual display if standard error is not a terminal. This option forces it to do so.</p>
<dt><code>-c, &#8211;cursor</code></p>
<dd> Use cursor positioning escape sequences instead of just using carriage returns. This is useful in conjunction with <code>-N</code> (name) if you are using multiple <code>pv</code> invocations in a single, long, pipeline. </p>
</dl>
<h2>DATA TRANSFER MODIFIERS</h2>
<dl>
<dt><code>-L RATE, &#8211;rate-limit RATE</code></p>
<dd> Limit the transfer to a maximum of <code>RATE</code> bytes per second. A suffix of &quot;K&quot;, &quot;M&quot;, &quot;G&quot;, or &quot;T&quot; can be added to denote kibibytes (*1024), mebibytes, and so on.</p>
<dt><code>-B BYTES, &#8211;buffer-size BYTES</code></p>
<dd> Use a transfer buffer size of <code>BYTES</code> bytes. A suffix of &quot;K&quot;, &quot;M&quot;, &quot;G&quot;, or &quot;T&quot; can be added to denote kibibytes (*1024), mebibytes, and so on. The default buffer size is the block size of the input file&#8217;s filesystem multiplied by 32 (512KiB max), or 400KiB if the block size cannot be determined.</p>
<dt><code>-C, &#8211;no-splice</code></p>
<dd> Never use <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), even if it would normally be possible. The <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) system call is a more efficient way of transferring data from or to a pipe than regular <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2), but means that the transfer buffer may not be used. This prevents <code>-A</code> and <code>-T</code> from working, so if you want to use <code>-A</code> or <code>-T</code> then you will need to use <code>-C</code>, at the cost of a small loss in transfer efficiency. (This option has no effect on systems where <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) is unavailable).</p>
<dt><code>-E, &#8211;skip-errors</code></p>
<dd> Ignore read errors by attempting to skip past the offending sections. The corresponding parts of the output will be null bytes. At first only a few bytes will be skipped, but if there are many errors in a row then the skips will move up to chunks of 512. This is intended to be similar to <code>dd conv=sync,noerror</code> but has not been as thoroughly tested.</p>
<dt>
<dd> Specify <code>-E</code> twice to only report a read error once per file, instead of reporting each byte range skipped.</p>
<dt><code>-S, &#8211;stop-at-size</code></p>
<dd> If a size was specified with <code>-s</code>, stop transferring data once that many bytes have been written, instead of continuing to the end of input.</p>
<dt><code>-d PID[:FD], &#8211;watchfd PID[:FD]</code></p>
<dd> Instead of transferring data, watch file descriptor <code>FD</code> of process <code>PID</code>, and show its progress. The <code>pv</code> process will exit when <code>FD</code> either changes to a different file, changes read/write mode, or is closed; other data transfer modifiers &#8211; and remote control &#8211; may not be used with this option.</p>
<dt>
<dd> If only a <code>PID</code> is specified, then that process will be watched, and all regular files and block devices it opens will be shown with a progress bar. The <code>pv</code> process will exit when process <code>PID</code> exits.</p>
<dt><code>-R PID, &#8211;remote PID</code></p>
<dd> If <code>PID</code> is an instance of <code>pv</code> that is already running, <code>-R PID</code> will cause that instance to act as though it had been given this instance&#8217;s command line instead. For example, if <code>pv -L 123K</code> is running with process ID 9876, then running <code>pv -R 9876 -L 321K</code> will cause it to start using a rate limit of 321KiB instead of 123KiB. Note that some options cannot be changed while running, such as <code>-c</code>, <code>-l</code>, <code>-f</code>, <code>-D</code>, <code>-E</code>, and <code>-S</code>. </p>
</dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-P FILE, &#8211;pidfile FILE</code></p>
<dd> Save the process ID of <code>pv</code> in <code>FILE</code>. The file will be truncated if it already exists, and will be removed when <code>pv</code> exits. While <code>pv</code> is running, it will contain a single number &#8211; the process ID of <code>pv</code> &#8211; followed by a newline.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a usage message on standard output and exit successfully.</p>
<dt><code>-V, &#8211;version </code></p>
<dd> Print version information on standard output and exit successfully. </p>
</dl>
<h2>FORMATTING</h2>
<p> If the <code>-F</code> option is given, then the output format is determined by the given format string. Within that string, the following sequences can be used:</p>
<dl>
<dt><code>%p</code></p>
<dd> Progress bar. Expands to fill the remaining space. Should only be specified once. Equivalent to <code>-p</code>.</p>
<dt><code>%t</code></p>
<dd> Elapsed time. Equivalent to <code>-t</code>.</p>
<dt><code>%e</code></p>
<dd> ETA as time remaining. Equivalent to <code>-e</code>.</p>
<dt><code>%I</code></p>
<dd> ETA as local time of completion. Equivalent to <code>-I</code>.</p>
<dt><code>%r</code></p>
<dd> Current data transfer rate. Equivalent to <code>-r</code>.</p>
<dt><code>%a</code></p>
<dd> Average data transfer rate. Equivalent to <code>-a</code>.</p>
<dt><code>%b</code></p>
<dd> Bytes transferred so far (or lines if <code>-l</code> was specified). Equivalent to <code>-b</code>.</p>
<dt><code>%T</code></p>
<dd> Percentage of the transfer buffer in use. Equivalent to <code>-T</code>. Shows &quot;{&#8212;-}&quot; if the transfer is being done with <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), since splicing to or from pipes does not use the buffer.</p>
<dt><code>%nA</code></p>
<dd> Show the last <code>n</code> bytes written (e.g. <code>%16A</code> for the last 16 bytes). Shows only dots if the transfer is being done with <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), since splicing to or from pipes does not use the buffer.</p>
<dt><code>%N</code></p>
<dd> Name prefix given by <code>-N</code>. Padded to 9 characters with spaces, and suffixed with :.</p>
<dt><code>%%</code></p>
<dd> A single %.</dl>
<p> The format string equivalent of turning on all display switches is <code>`%N %b %T %t %r %a %p %e&#8217;</code>. </p>
<h2>COMMON SWITCHES</h2>
<p> Some suggested common switch combinations: </p>
<dl>
<dt><code>pv -ptebar</code></p>
<dd> Show a progress bar, elapsed time, estimated completion time, byte counter, average rate, and current rate.</p>
<dt><code>pv -betlap</code></p>
<dd> Show a progress bar, elapsed time, estimated completion time, line counter, and average rate, counting lines instead of bytes.</p>
<dt><code>pv -t</code></p>
<dd> Show only the elapsed time &#8211; useful as a simple timer, e.g. <code>sleep 10m | pv -t</code>.</p>
<dt><code>pv -pterb</code></p>
<dd> The default behaviour: progress bar, elapsed time, estimated completion time, current rate, and byte counter. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> An exit status of 1 indicates a problem with the <code>-R</code> or <code>-P</code> options. </p>
<p> Any other exit status is a bitmask of the following: </p>
<dl>
<dt><code>2</code></p>
<dd> One or more files could not be accessed, <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)ed, or opened.</p>
<dt><code>4</code></p>
<dd> An input file was the same as the output file.</p>
<dt><code>8</code></p>
<dd> Internal error with closing a file or moving to the next file.</p>
<dt><code>16</code></p>
<dd> There was an error while transferring data from one or more input files.</p>
<dt><code>32</code></p>
<dd> A signal was caught that caused an early exit.</p>
<dt><code>64</code></p>
<dd> Memory allocation failed. </p>
<p> A zero exit status indicates no problems. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Andrew Wood, with patches submitted by various other people. Please see the package README for a complete list of contributors. </p>
<h2>KNOWN PROBLEMS</h2>
<p> The following problems are known to exist in <code>pv</code>:</p>
<dl>
<dt><code>*</code></p>
<dd> The <code>-c</code> option does not work properly on Cygwin without <code>cygserver</code> running, if started near the bottom of the screen (IPC is needed to handle the terminal scrolling). To fix this, start <code>cygserver</code> before using <code>pv -c</code>.</dl>
<dl>
<dt><code>*</code></p>
<dd> The <code>-R</code> option is not available on Cygwin without <code>cygserver</code> running (SYSV IPC is needed). To fix this, start <code>cygserver</code> before running the instance of <code>pv</code> you want, at runtime, to change the parameters of.</dl>
<p> If you find any other problems, please report them. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs in <code>pv</code> to pv [at] ivarch.com or use the contact form linked from the <code>pv</code> home page: &lt;<a rel="nofollow" href="http://www.ivarch.com/programs/pv.shtml">http://www.ivarch.com/programs/pv.shtml</a>&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) </p>
<h2>LICENSE</h2>
<p> This is free software, distributed under the ARTISTIC 2.0 license. </p>
<h2>Index</h2>
