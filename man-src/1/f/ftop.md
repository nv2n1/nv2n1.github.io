---
title: "ftop(1)"
name: "ftop"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftop/"
description: "ftop – show progress of open files and file systems"
---

<h2>NAME</h2>
<p> ftop &#8211; show progress of open files and file systems</p>
<h2>SYNOPSIS</h2>
<p> <code>ftop</code> [options]</p>
<h2>COPYRIGHT</h2>
<p> ftop is Copyright (C) 2009 Jason Todd. Send bug reports and suggestions/patches/etc. to <i>jtodd1 [at] earthlink.net</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>ftop</code> program displays progress information for the open files and file systems in a Linux system. As processes read and write files, ftop displays data rates and time estimates. Its feature-rich interface is similar to <code>top</code>, and includes extensive run-time configuration options. </p>
<p> While this manual page contains the full documentation for <code>ftop</code>, the built-in online help is the best source for the most up to date documentation. To access the online help, run ftop with the <code>-h</code> command line option, or simply press &#8216;<code>h</code>&#8216; while ftop is running.</p>
<h2>OPTIONS</h2>
<p> Every option listed below is supported as a command-line argument (for example, <code>-f</code>) and as a run-time keyboard command (<code>f</code>)<code>.</code> Thus, any option can be set when ftop is started, and can be changed later while it is running. Options with uppercase characters are boolean values (enabled or disabled), and lowercase option characters require other types of values. </p>
<p> Boolean options are disabled by default. When supplied as a command-line argument, the option is enabled. If the corresponding key is pressed while ftop is running, the option&#8217;s value is toggled. </p>
<p> Non-boolean options accept values of the type shown next to their option characters. <i>List</i> values accept one or more values, separated by comma characters (with no spaces). Values of type <i>num</i> are numeric, and values of type <i>user</i> can be specified as either a valid login or numeric UID. </p>
<p> Please refer to the additional details following the list of options. </p>
<dl>
<dt><code>-a</code><i> list</i></p>
<dd> Additional files/fs</p>
<dt>
<dd> Manually specify files or file systems to monitor. These are in addition to all currently open files. If any directories are specified, their file system usage is displayed. This option is useful for monitoring files written by NFS clients, or for observing the addition of a large number of files to a file system (for example, while extracting a large archive or restoring from a backup).</p>
<dt>
<dd>
<dt><code>-A</code></p>
<dd> Addl. files/fs only</p>
<dt>
<dd> Only show the files and file systems specified in &#8216;Additional files/fs&#8217; (see above) and &#8216;File system types&#8217; (see below).</p>
<dt>
<dd>
<dt><code>-B</code></p>
<dd> Expand at-beginning</p>
<dt>
<dd> Show the progress bar for files that are still at the beginning. When this option is disabled, a file&#8217;s progress bar doesn&#8217;t appear until there has been some activity. Often, there are processes that hold log files open for append, but haven&#8217;t yet written anything new. Leaving this disabled reduces the clutter in the presence of those (and similar) situations.</p>
<dt>
<dd>
<dt><code>-c</code><i> num</i></p>
<dd> Closed files count</p>
<dt>
<dd> Additionally show the specified number of most recently closed files for each displayed process.</p>
<dt>
<dd>
<dt><code>-d</code><i> num</i></p>
<dd> Delay</p>
<dt>
<dd> Change the time between updates. The value is specified in seconds, with optional tenths or hundredths (for example: 1 or 0.5 or 1.25 are all valid).</p>
<dt>
<dd>
<dt><code>-D</code></p>
<dd> Hide path directories</p>
<dt>
<dd> Hide all leading directory components of each file path. If the file path refers to an unnamed pipe or socket, or otherwise is not valid, then the full path will still be displayed.</p>
<dt>
<dd>
<dt><code>-E</code></p>
<dd> Expand at-end</p>
<dt>
<dd> Show the progress bar for files that are at the end. When this option is disabled, a file&#8217;s progress bar disappears once the process reaches the end of the file. Whenever a process writes to a file, the resulting position is at the end. Processes that write to log files tend to have several files open in this state. Leaving this disabled &quot;reduces the clutter in the presence of those (and similar) situations. See also &#8216;File keywords &amp; sizes&#8217; below.</p>
<dt>
<dd>
<dt><code>-f</code><i> list</i></p>
<dd> File keywords</p>
<dt>
<dd> Only show files whose path contains, anywhere within, one of the specified keywords. For instance, if a file /tmp/live-cd.iso is open, and the keyword list contains cd.i, then that file will be shown.</p>
<dt>
<dd>
<dt><code>-F</code></p>
<dd> Show un-expanded files</p>
<dt>
<dd> Show all files that are open within the displayed processes. See also</dl>
<h2>ow un-expanded procs&#8217; below.</h2>
<dl>
<dt>
<dd>
<dt><code>-h</code></p>
<dd> Help</p>
<dt>
<dd> Toggle the help screen.</p>
<dt>
<dd>
<dt><code>-l</code><i> list</i></p>
<dd> Log types</p>
<dt>
<dd> Specify the type(s) of messages to log. Valid types are none, all, or one or more of the following: err, warn, info, debug. The value none disables logging. If logging is enabled, and &#8216;Limited output mode&#8217; (see below) is enabled, the log is output on stderr. See also &#8216;View log&#8217; below.</p>
<dt>
<dd>
<dt><code>-L</code></p>
<dd> View log</p>
<dt>
<dd> Toggle the log screen, if logging is enabled.</p>
<dt>
<dd>
<dt><code>-m</code><i> list</i></p>
<dd> Access modes</p>
<dt>
<dd> Specify the access mode(s) of files to show. Valid modes are one or more of the following: r, w, rw. If r is specified, files open for read-only access will be shown. If w is specified, files open for write-only access will be shown. If rw is specified, then files open for read and write will be shown. Note, rw does not include read-only or write-only files.</p>
<dt>
<dd>
<dt><code>-n</code><i> num</i></p>
<dd> Iterations</p>
<dt>
<dd> Specify the total number of update iterations to run, after which ftop will exit.</p>
<dt>
<dd>
<dt><code>-N</code></p>
<dd> Show all FDs numeric</p>
<dt>
<dd> Display all file descriptors as their numeric values. When this option is disabled, file descriptors 0, 1, and 2 are given the symbolic names in, out, and err, respectively, to reflect stdin, stdout, and stderr.</p>
<dt>
<dd>
<dt><code>-o</code></p>
<dd> View options</p>
<dt>
<dd> Toggle the options summary screen.</p>
<dt>
<dd>
<dt><code>-O</code></p>
<dd> Limited output mode</p>
<dt>
<dd> Toggle between full output mode and limited output mode. By default, full mode is selected if the ncurses library is available and stdout is a terminal (e.g. not redirected or piped). If neither of the above is true, then only limited mode will be available. If this option is specified on the command line, limited mode will be used initially. In limited mode, all control keys can still be used, but scrolling is not available.</p>
<dt>
<dd>
<dt><code>-p</code><i> list</i></p>
<dd> Process keywords/PIDs</p>
<dt>
<dd> Show only processes whose command line contains, anywhere within, one the specified keywords, or whose PID equals a specified value. For instance, the list 1,bash,X will show the init process, all instances of bash, and any running X servers (if X is within their command line). Note, processes with no open files that match any of the other criteria will still not be shown. See also &#8216;Show un-expanded procs&#8217; below.</p>
<dt>
<dd>
<dt><code>-P</code></p>
<dd> Show un-expanded procs</p>
<dt>
<dd> Show all processes. See also &#8216;Show un-expanded files&#8217; and &#8216;Process keywords/PIDs&#8217; above.</p>
<dt>
<dd>
<dt><code>-q</code></p>
<dd> Quit</p>
<dt>
<dd> Exit from ftop.</p>
<dt>
<dd>
<dt><code>-Q</code></p>
<dd> Hide tput &amp; est. time</p>
<dt>
<dd> Do not show any throughput or estimated time remaining calculations. This is useful when simply monitoring how far into files the processes are, especially if used with a very small delay (see &#8216;Delay&#8217; above).</p>
<dt>
<dd>
<dt><code>-r</code></p>
<dd> Refresh display</p>
<dt>
<dd> Force a refresh of the display.</p>
<dt>
<dd>
<dt><code>-t</code><i> list</i></p>
<dd> File types</p>
<dt>
<dd> Specify the type(s) of files to show. Valid types are all, or one or more of the following: f, d, c, b, p, s, x. Also allowed is r, an alias for f. The meaning of each is: f (regular file), d (directory), c (character device), b (block device), p (pipe/FIFO), s (socket), and x (miscellaneous &#8211; unknown or unclassifiable).</p>
<dt>
<dd>
<dt><code>-u</code><i> user</i></p>
<dd> User name/UID</p>
<dt>
<dd> Only show processes with the given real user id. The user can be specified either as a name or as a UID.</p>
<dt>
<dd>
<dt><code>-U</code></p>
<dd> Units in base 10</p>
<dt>
<dd> If this option is disabled, sizes and throughputs will be reported in units based on powers of 2. Specifically, M (megabyte) corresponds to 2 to the 20th power and G (gigabyte) corresponds to 2 to the 30th. If this option is enabled, the units e6 (million bytes) and e9 (billion bytes) will be used instead. Note, either form is always acceptable when entering size values, regardless of this setting.</p>
<dt>
<dd>
<dt><code>-v</code></p>
<dd> Version and license</p>
<dt>
<dd> Toggle the version and license screen.</p>
<dt>
<dd>
<dt><code>-x</code><i> num</i></p>
<dd> Max no-match iterations</p>
<dt>
<dd> Specify the number of iterations to remain running when there are no open files matching any of the other criteria. At least one match has to have been shown, and subsequently been closed, before the remaining iterations are counted. If during those iterations, another matching file is shown, the counter is reset. See also &#8216;Iterations&#8217; above.</p>
<dt>
<dd>
<dt><code>-y</code><i> list</i></p>
<dd> File system types</p>
<dt>
<dd> Show all mounted filesystems of the specified types. Valid types are all, or one or more of the types supported by the kernel (refer to /proc/filesystems). The display is updated to reflect the mounting or unmounting of matching file systems.</p>
<dt>
<dd>
<dt><code>-z</code><i> list</i></p>
<dd> File keywords &amp; sizes</p>
<dt>
<dd> Specify pre-determined final sizes to use for files opened for write access and for file systems (see &#8216;Additional files/fs&#8217; above). The values in the list must be of the form keyword=size, where keyword is applied as in &#8216;File keywords&#8217; (see above) and size is given in bytes, megabytes (or million bytes), or gigabytes (or billion bytes) with optional tenths value. See &#8216;Units in base 10&#8217; above. The following is an example of a valid list: data_out.bin=1.5G,/tmp/=700e6,some_file.copy=120000</dl>
<h2>NOTES</h2>
<p> The three characters displayed after a file&#8217;s descriptor represent the type of file and the access mode. See &#8216;File types&#8217; and &#8216;Access modes&#8217; for details on each. In the case of a file system, FS- will be displayed. If a file is opened in append mode, an uppercase W will be displayed instead of a lowercase w. </p>
<p> The two characters following the access mode represent activity. If &#8212; is displayed, there is no activity. If the position is advancing in a forward direction, then -&gt;, &gt;&gt;, or &gt;- will be displayed depending on how much progress is occurring. If the position is moving backward, then -&lt;, &lt;&lt;, or &lt;- will be displayed. If the position is moving in a somewhat random fashion, then &lt;&gt; will be displayed. Finally, any time a different file is open for the given descriptor, ** is displayed. </p>
<p> When monitoring additional files, only the current total size of the file can be obtained; no read or write position is available. Thus, for display purposes, the file is reported as being opened for write-only access, and the current file size is used as its position. If the ultimate size of the file is known, it can be supplied with &#8216;File keywords &amp; sizes&#8217; and that value will then be reported as the size. </p>
<p> For file systems, the amount of space currently consumed is used as the position. In both cases (additional files and file systems), the reported position value is still used in throughput calculations and remaining time estimates.</p>
<h2>EXAMPLES</h2>
<p> To see a real-time graphic representation of all mounted ext3 and nfs file systems: </p>
<p> ftop -QAy ext3,nfs </p>
<p> The following command provides very interesting feedback when working with large gzipped or bzip2&#8217;ed tar files. Note, the exact same command can be used to monitor both creating the archive file, and extracting its contents. The specified file system (/share/ in this example) should be where the file is being created, or where its contents are being placed (in which case multiple file systems may need to be given). Also, the delay time may need to be adjusted to achieve the desired effects. </p>
<p> ftop -d .1 -c 4 -p tar,gzip -t f,p -a /share/ </p>
<p> If a file /tmp/output.bin is to be created by another process, and it is known that its resulting size will be approximately 6.5GB, then the following command will monitor the progress for at most 60 seconds, but will exit earlier if the process completes early or the file is otherwised closed for more than 1 second. </p>
<p> ftop -f mp/outp -z output.bin=6.5G -n 60 -x 1 </p>
<p> If, in the example above, the file is being created by an NFS client, then the file will not be open locally. In this case, the command would be as follows: </p>
<p> ftop -Aa /tmp/output.bin -z output.bin=6.5G -n 60 -x 1 </p>
<p> It can be interesting to see disk access patterns in different operating systems as they boot and perform their duties (or as a system is booting from a CD or DVD). With an emulator or virtualization environment, and provided the emulator doesn&#8217;t do much caching of the virtualized disks, this behavior can be monitored for any number of disk image files with a command such as the following: </p>
<p> ftop -f cd.img,hdd.img -d 0.1 -QBED </p>
<p> To capture a log of progress&#8217;s activity for one iteration (useful if sending a bug report): </p>
<p> ftop -On 1 -l all 2&gt; log.txt</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-top/">top</a></code>(1) </p>
<h2>Index</h2>
