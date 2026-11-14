---
title: "atop(1)"
name: "atop"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atop/"
description: "atop – Advanced System & Process Monitor"
---

<h2>NAME</h2>
<p> <code>atop </code> &#8211; Advanced System &amp; Process Monitor</p>
<h2>SYNOPSIS</h2>
<p> Interactive Usage: </p>
<p> <code>atop</code> [-g|-m|-d|-n|-u|-p|-s|-c|-v|-o|-y] [-C|-M|-D|-N|-A] [-afFG1xR] [-L linelen] [-Plabel[,label]&#8230;] [ <i>interval</i> [ <i>samples</i> ]] </p>
<p> Writing and reading raw logfiles: </p>
<p> <code>atop</code> -w <i>rawfile</i> [-a] [-S] [ <i>interval</i> [ <i>samples</i> ]]<br />
 <code>atop</code> -r [ <i>rawfile</i> ] [-b <i>hh:mm</i> ] [-e <i>hh:mm</i> ] [-g|-m|-d|-n|-u|-p|-s|-c|-v|-o|-y] [-C|-M|-D|-N|-A] [-fFG1xR] [-L linelen] [-Plabel[,label]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The program <i>atop</i> is an interactive monitor to view the load on a Linux system. It shows the occupation of the most critical hardware resources (from a performance point of view) on system level, i.e. cpu, memory, disk and network.<br />
 It also shows which processes are responsible for the indicated load with respect to cpu and memory load on process level. Disk load is shown per process if &quot;storage accounting&quot; is active in the kernel. Network load is shown per process if the kernel module `netatop&#8217; has been installed. </p>
<p> Every <i>interval</i> (default: 10 seconds) information is shown about the resource occupation on system level (cpu, memory, disks and network layers), followed by a list of processes which have been active during the last interval (note that all processes that were unchanged during the last interval are not shown, unless the key &#8216;a&#8217; has been pressed). If the list of active processes does not entirely fit on the screen, only the top of the list is shown (sorted in order of activity).<br />
 The intervals are repeated till the number of <i>samples</i> (specified as command argument) is reached, or till the key &#8216;q&#8217; is pressed in interactive mode. </p>
<p> When <i>atop</i> is started, it checks whether the standard output channel is connected to a screen, or to a file/pipe. In the first case it produces screen control codes (via the ncurses library) and behaves interactively; in the second case it produces flat ASCII-output. </p>
<p> In interactive mode, the output of <i>atop</i> scales dynamically to the current dimensions of the screen/window.<br />
 If the window is resized horizontally, columns will be added or removed automatically. For this purpose, every column has a particular weight. The columns with the highest weights that fit within the current width will be shown.<br />
 If the window is resized vertically, lines of the process/thread list will be added or removed automatically. </p>
<p> Furthermore in interactive mode the output of <i>atop</i> can be controlled by pressing particular keys. However it is also possible to specify such key as <code>flag</code> on the command line. In that case <i>atop</i> switches to the indicated mode on beforehand; this mode can be modified again interactively. Specifying such key as flag is especially useful when running <i>atop</i> with output to a pipe or file (non-interactively). These flags are the same as the keys that can be pressed in interactive mode (see section INTERACTIVE COMMANDS).<br />
 Additional flags are available to support storage of atop-data in raw format (see section RAW DATA STORAGE).</p>
<h2>PROCESS ACCOUNTING</h2>
<p> With every interval, <i>atop</i> reads the kernel administration to obtain information about all running processes. However, it is likely that during the interval also processes have terminated. These processes might have consumed system resources during this interval as well before they terminated. Therefor, <i>atop</i> tries to read the process accounting records that contain the accounting information of terminated processes and report these processes too. Only when the process accounting mechanism in the kernel is activated, the kernel writes such process accounting record to a file for every process that terminates. </p>
<p> There are various ways for <i>atop</i> to get access to the process accounting records (tried in this order): </p>
<dl>
<dt>1.</p>
<dd> When the environment variable ATOPACCT is set, it specifies the name of the process accounting file. In that case, process accounting for this file should have been activated on beforehand. Before opening this file for reading, <i>atop</i> drops its root privileges (if any).<br />
 When this environment variable is present but its contents is empty, process accounting will not be used at all.</dl>
<dl>
<dt>2.</p>
<dd> <code>This is the preferred way of handling process accounting records!</code><br />
 When the <i>atopacctd</i> daemon is active, it has activated the process accounting mechanism in the kernel and transfers to original accounting records to shadow files. In that case, <i>atop</i> drops its root privileges and opens the current shadow file for reading.<br />
 This way is preferred, because the <i>atopacctd</i> daemon maintains full control of the sizes of the original process accounting file (written by the kernel) and the shadow files (read by the <i>atop</i> processes). For further information, refer to the <code>atopacctd</code> man page.</dl>
<dl>
<dt>3.</p>
<dd> When the <i>atopacctd</i> daemon is not active, <i>atop</i> verifies if the process accounting mechanism has been switched on via the separate <code>psacct</code> package. In that case, the file <code>/var/account/pacct</code> is in use as process accounting file and <i>atop</i> opens this file for reading.</dl>
<dl>
<dt>4.</p>
<dd> As a last possibility, <i>atop</i> itself tries to activate the process accounting mechanism (requires root privileges) using the file <code>/tmp/atop.d/atop.acct</code> (to be written by the kernel, to be read by <i>atop</i> itself). Process accounting remains active as long as at least one <i>atop</i> process is alive. Whenever the last <i>atop</i> process stops (either by pressing `q&#8217; or by `kill -15&#8242;), it deactivates the process accounting mechanism again. Therefor you should never terminate <i>atop</i> by `kill -9&#8242;, because then it has no chance to stop process accounting. As a result, the accounting file may consume a lot of disk space after a while.<br />
 To avoid that the process accounting file consumes too much disk space, <i>atop</i> verifies at the end of every sample if the size of the process accounting file exceeds 200 MiB and if this <i>atop</i> process is the only one that is currently using the file. In that case the file is truncated to a size of zero. </p>
<p> Notice that root-privileges are required to switch on/off process accounting in the kernel. You can start <i>atop</i> as a root user or specify setuid-root privileges to the executable file. In the latter case, <i>atop</i> switches on process accounting and drops the root-privileges again.<br />
 If <i>atop</i> does not run with root-privileges, it does not show information about finished processes. It indicates this situation with the message message `no procacct` in the top-right corner (instead of the counter that shows the number of exited processes).</dl>
<p> When during one interval a lot of processes have finished, <i>atop</i> might grow tremendously in memory when reading all process accounting records at the end of the interval. To avoid such excessive growth, <i>atop</i> will never read more than 50 MiB with process information from the process accounting file per interval (approx. 70000 finished processes). In interactive mode a warning is given whenever processes have been skipped for this reason. </p>
<h2>COLORS</h2>
<p> For the resource consumption on system level, <i>atop</i> uses colors to indicate that a critical occupation percentage has been (almost) reached. A critical occupation percentage means that is likely that this load causes a noticeable negative performance influence for applications using this resource. The critical percentage depends on the type of resource: e.g. the performance influence of a disk with a busy percentage of 80% might be more noticeable for applications/user than a CPU with a busy percentage of 90%.<br />
 Currently <i>atop</i> uses the following default values to calculate a weighted percentage per resource: </p>
<dl>
<dt><code>&nbsp;<wbr>Processor</code></p>
<dd> A busy percentage of 90% or higher is considered `critical&#8217;.</p>
<dt><code>&nbsp;<wbr>Disk</code></p>
<dd> A busy percentage of 70% or higher is considered `critical&#8217;.</p>
<dt><code>&nbsp;<wbr>Network</code></p>
<dd> A busy percentage of 90% or higher for the load of an interface is considered `critical&#8217;.</p>
<dt><code>&nbsp;<wbr>Memory</code></p>
<dd> An occupation percentage of 90% is considered `critical&#8217;. Notice that this occupation percentage is the accumulated memory consumption of the kernel (including slab) and all processes; the memory for the page cache (`cache&#8217; and `buff&#8217; in the MEM-line) and the reclaimable part of the slab (`slrec`) is not implied!<br />
 If the number of pages swapped out (`swout&#8217; in the PAG-line) is larger than 10 per second, the memory resource is considered `critical&#8217;. A value of at least 1 per second is considered `almost critical&#8217;.<br />
 If the committed virtual memory exceeds the limit (`vmcom&#8217; and `vmlim&#8217; in the SWP-line), the SWP-line is colored due to overcommitting the system.</p>
<dt><code>&nbsp;<wbr>Swap</code></p>
<dd> An occupation percentage of 80% is considered `critical&#8217; because swap space might be completely exhausted in the near future; it is not critical from a performance point-of-view.</dl>
<p> These default values can be modified in the configuration file (see separate man-page of atoprc). </p>
<p> When a resource exceeds its critical occupation percentage, the concerning values in the screen line are colored red by default.<br />
 When a resource exceeded (default) 80% of its critical percentage (so it is almost critical), the concerning values in the screen line are colored cyan by default. This `almost critical percentage&#8217; (one value for all resources) can be modified in the configuration file (see separate man-page of atoprc).<br />
 The default colors red and cyan can be modified in the configuration file as well (see separate man-page of atoprc). </p>
<p> With the key &#8216;x&#8217; (or flag -x), the use of colors can be suppressed.</p>
<h2>NETATOP MODULE</h2>
<p> Per-process and per-thread network activity can be measured by the <i>netatop</i> kernel module. You can download this kernel module from the website (mentioned at the end of this manual page) and install it on your system if the kernel version is 2.6.24 or newer.<br />
 When <i>atop</i> gathers counters for a new interval, it verifies if the <i>netatop</i> module is currently active. If so, <i>atop</i> obtains the relevant network counters from this module and shows the number of sent and received packets per process/thread in the generic screen. Besides, detailed counters can be requested by pressing the `n&#8217; key.<br />
 When the <i>netatopd</i> daemon is running as well, <i>atop</i> also reads the network counters of exited processes that are logged by this daemon (comparable with process accounting). </p>
<p> More information about the optional <i>netatop</i> kernel module and the <i>netatopd</i> daemon can be found in the concerning man-pages and on the website mentioned at the end of this manual page.</p>
<h2>INTERACTIVE COMMANDS</h2>
<p> When running <i>atop</i> interactively (no output redirection), keys can be pressed to control the output. In general, lower case keys can be used to show other information for the active processes and upper case keys can be used to influence the sort order of the active process/thread list. </p>
<dl>
<dt><code>g</code></p>
<dd> Show generic output (default). </p>
<p> Per process the following fields are shown in case of a window-width of 80 positions: process-id, cpu consumption during the last interval in system and user mode, the virtual and resident memory growth of the process. </p>
<p> The subsequent columns depend on the used kernel:<br />
 When the kernel supports &quot;storage accounting&quot; (&gt;= 2.6.20), the data transfer for read/write on disk, the status and exit code are shown for each process. When the kernel does not support &quot;storage accounting&quot;, the username, number of threads in the thread group, the status and exit code are shown.<br />
 When the kernel module &#8216;netatop&#8217; is loaded, the data transfer for send/receive of network packets is shown for each process.<br />
 The last columns contain the state, the occupation percentage for the chosen resource (default: cpu) and the process name. </p>
<p> When more than 80 positions are available, other information is added.</dl>
<dl>
<dt><code>m</code></p>
<dd> Show memory related output. </p>
<p> Per process the following fields are shown in case of a window-width of 80 positions: process-id, minor and major memory faults, size of virtual shared text, total virtual process size, total resident process size, virtual and resident growth during last interval, memory occupation percentage and process name. </p>
<p> When more than 80 positions are available, other information is added.</dl>
<dl>
<dt><code>d</code></p>
<dd> Show disk-related output. </p>
<p> When &quot;storage accounting&quot; is active in the kernel, the following fields are shown: process-id, amount of data read from disk, amount of data written to disk, amount of data that was written but has been withdrawn again (WCANCL), disk occupation percentage and process name.</dl>
<dl>
<dt><code>n</code></p>
<dd> Show network related output. </p>
<p> Per process the following fields are shown in case of a window-width of 80 positions: process-id, thread-id, total bandwidth for received packets, total bandwidth for sent packets, number of received TCP packets with the average size per packet (in bytes), number of sent TCP packets with the average size per packet (in bytes), number of received UDP packets with the average size per packet (in bytes), number of sent UDP packets with the average size per packet (in bytes), the network occupation percentage and process name.<br />
 This information can only be shown when kernel module `netatop&#8217; is installed. </p>
<p> When more than 80 positions are available, other information is added.</dl>
<dl>
<dt><code>s</code></p>
<dd> Show scheduling characteristics. </p>
<p> Per process the following fields are shown in case of a window-width of 80 positions: process-id, number of threads in state &#8216;running&#8217; (R), number of threads in state &#8216;interruptible sleeping&#8217; (S), number of threads in state &#8216;uninterruptible sleeping&#8217; (D), scheduling policy (normal timesharing, realtime round-robin, realtime fifo), nice value, priority, realtime priority, current processor, status, exit code, state, the occupation percentage for the chosen resource and the process name. </p>
<p> When more than 80 positions are available, other information is added.</dl>
<dl>
<dt><code>v</code></p>
<dd> Show various process characteristics. </p>
<p> Per process the following fields are shown in case of a window-width of 80 positions: process-id, user name and group, start date and time, status (e.g. exit code if the process has finished), state, the occupation percentage for the chosen resource and the process name. </p>
<p> When more than 80 positions are available, other information is added.</dl>
<dl>
<dt><code>c</code></p>
<dd> Show the command line of the process. </p>
<p> Per process the following fields are shown: process-id, the occupation percentage for the chosen resource and the command line including arguments.</dl>
<dl>
<dt><code>o</code></p>
<dd> Show the user-defined line of the process. </p>
<p> In the configuration file the keyword <i>ownprocline</i> can be specified with the description of a user-defined output-line.<br />
 Refer to the man-page of <code>atoprc</code> for a detailed description.</dl>
<dl>
<dt><code>y</code></p>
<dd> Show the individual threads within a process (toggle). </p>
<p> Single-threaded processes are still shown as one line.<br />
 For multi-threaded processes, one line represents the process while additional lines show the activity per individual thread (in a different color). Depending on the option &#8216;a&#8217; (all or active toggle), all threads are shown or only the threads that were active during the last interval.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>u</code></p>
<dd> Show the process activity accumulated per user. </p>
<p> Per user the following fields are shown: number of processes active or terminated during last interval (or in total if combined with command `a&#8217;), accumulated cpu consumption during last interval in system and user mode, the current virtual and resident memory space consumed by active processes (or all processes of the user if combined with command `a&#8217;).<br />
 When &quot;storage accounting&quot; is active in the kernel, the accumulated read and write throughput on disk is shown. When the kernel module `netatop&#8217; has been installed, the number of received and sent network packets are shown.<br />
 The last columns contain the accumulated occupation percentage for the chosen resource (default: cpu) and the user name.</dl>
<dl>
<dt><code>p</code></p>
<dd> Show the process activity accumulated per program (i.e. process name). </p>
<p> Per program the following fields are shown: number of processes active or terminated during last interval (or in total if combined with command `a&#8217;), accumulated cpu consumption during last interval in system and user mode, the current virtual and resident memory space consumed by active processes (or all processes of the user if combined with command `a&#8217;).<br />
 When &quot;storage accounting&quot; is active in the kernel, the accumulated read and write throughput on disk is shown. When the kernel module `netatop&#8217; has been installed, the number of received and sent network packets are shown.<br />
 The last columns contain the accumulated occupation percentage for the chosen resource (default: cpu) and the program name.</dl>
<dl>
<dt><code>C </code></p>
<dd> Sort the current list in the order of cpu consumption (default). The one-but-last column changes to &#8220;CPU&#8221;.</dl>
<dl>
<dt><code>M </code></p>
<dd> Sort the current list in the order of resident memory consumption. The one-but-last column changes to &#8220;MEM&#8221;.</dl>
<dl>
<dt><code>D</code></p>
<dd> Sort the current list in the order of disk accesses issued. The one-but-last column changes to &#8220;DSK&#8221;.</dl>
<dl>
<dt><code>N</code></p>
<dd> Sort the current list in the order of network bandwidth (received and transmitted). The one-but-last column changes to &#8220;NET&#8221;.</dl>
<dl>
<dt><code>A</code></p>
<dd> Sort the current list automatically in the order of the most busy system resource during this interval. The one-but-last column shows either &#8220;ACPU&#8221;, &#8220;AMEM&#8221;, &#8220;ADSK&#8221; or &#8220;ANET&#8221; (the preceding &#8216;A&#8217; indicates automatic sorting-order). The most busy resource is determined by comparing the weighted busy-percentages of the system resources, as described earlier in the section COLORS.<br />
 This option remains valid until another sorting-order is explicitly selected again.<br />
 A sorting-order for disk is only possible when &quot;storage accounting&quot; is active. A sorting-order for network is only possible when the kernel module `netatop&#8217; is loaded.</dl>
<p> Miscellaneous interactive commands: </p>
<dl>
<dt><code>?</code></p>
<dd> Request for help information (also the key &#8216;h&#8217; can be pressed).</dl>
<dl>
<dt><code>V</code></p>
<dd> Request for version information (version number and date).</dl>
<dl>
<dt><code>R</code></p>
<dd> Gather and calculate the proportional set size of processes (toggle). Gathering of all values that are needed to calculate the PSIZE of a process is a relatively time-consuming task, so this key should only be active when analyzing the resident memory consumption of processes.</dl>
<dl>
<dt><code>x</code></p>
<dd> Suppress colors to highlight critical resources (toggle).<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>z</code></p>
<dd> The pause key can be used to freeze the current situation in order to investigate the output on the screen. While <i>atop</i> is paused, the keys described above can be pressed to show other information about the current list of processes. Whenever the pause key is pressed again, atop will continue with a next sample.</dl>
<dl>
<dt><code>i</code></p>
<dd> Modify the interval timer (default: 10 seconds). If an interval timer of 0 is entered, the interval timer is switched off. In that case a new sample can only be triggered manually by pressing the key &#8216;t&#8217;.</dl>
<dl>
<dt><code>t</code></p>
<dd> Trigger a new sample manually. This key can be pressed if the current sample should be finished before the timer has exceeded, or if no timer is set at all (interval timer defined as 0). In the latter case <i>atop</i> can be used as a stopwatch to measure the load being caused by a particular application transaction, without knowing on beforehand how many seconds this transaction will last. </p>
<p> When viewing the contents of a raw file, this key can be used to show the next sample from the file.</dl>
<dl>
<dt><code>T</code></p>
<dd> When viewing the contents of a raw file, this key can be used to show the previous sample from the file.</dl>
<dl>
<dt><code>b</code></p>
<dd> When viewing the contents of a raw file, this key can be used to branch to a certain timestamp within the file (either forward or backward).</dl>
<dl>
<dt><code>r</code></p>
<dd> Reset all counters to zero to see the system and process activity since boot again. </p>
<p> When viewing the contents of a raw file, this key can be used to rewind to the beginning of the file again.</dl>
<dl>
<dt><code>U</code></p>
<dd> Specify a search string for specific user names as a regular expression. From now on, only (active) processes will be shown from a user which matches the regular expression. The system statistics are still system wide. If the Enter-key is pressed without specifying a name, active processes of all users will be shown again.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>P</code></p>
<dd> Specify a search string for specific process names as a regular expression. From now on, only processes will be shown with a name which matches the regular expression. The system statistics are still system wide. If the Enter-key is pressed without specifying a name, all active processes will be shown again.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>S</code></p>
<dd> Specify search strings for specific logical volume names, specific disk names and specific network interface names. All search strings are interpreted as a regular expressions. From now on, only those system resources are shown that match the concerning regular expression. If the Enter-key is pressed without specifying a search string, all (active) system resources of that type will be shown again.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>a</code></p>
<dd> The `all/active&#8217; key can be used to toggle between only showing/accumulating the processes that were active during the last interval (default) or showing/accumulating all processes.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>G</code></p>
<dd> By default, <i>atop</i> shows/accumulates the processes that are alive and the processes that are exited during the last interval. With this key (toggle), showing/accumulating the processes that are exited can be suppressed.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>f</code></p>
<dd> Show a fixed (maximum) number of header lines for system resources (toggle). By default only the lines are shown about system resources (CPUs, paging, logical volumes, disks, network interfaces) that really have been active during the last interval. With this key you can force <i>atop</i> to show lines of inactive resources as well.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>F</code></p>
<dd> Suppress sorting of system resources (toggle). By default system resources (CPUs, logical volumes, disks, network interfaces) are sorted on utilization.<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>1</code></p>
<dd> Show relevant counters as an average per second (in the format `&#8230;./s&#8217;) instead of as a total during the interval (toggle).<br />
 Whether this key is active or not can be seen in the header line.</dl>
<dl>
<dt><code>l</code></p>
<dd> Limit the number of system level lines for the counters per-cpu, the active disks and the network interfaces. By default lines are shown of all CPUs, disks and network interfaces which have been active during the last interval. Limiting these lines can be useful on systems with huge number CPUs, disks or interfaces in order to be able to run <i>atop</i> on a screen/window with e.g. only 24 lines.<br />
 For all mentioned resources the maximum number of lines can be specified interactively. When using the flag <code>-l</code> the maximum number of per-cpu lines is set to 0, the maximum number of disk lines to 5 and the maximum number of interface lines to 3. These values can be modified again in interactive mode.</dl>
<dl>
<dt><code>k</code></p>
<dd> Send a signal to an active process (a.k.a. kill a process).</dl>
<dl>
<dt><code>q</code></p>
<dd> Quit the program.</dl>
<dl>
<dt><code>PgDn</code></p>
<dd> Show the next page of the process/thread list.<br />
 With the arrow-down key the list can be scrolled downwards with single lines.</dl>
<dl>
<dt><code>^F</code></p>
<dd> Show the next page of the process/thread list (forward).<br />
 With the arrow-down key the list can be scrolled downwards with single lines.</dl>
<dl>
<dt><code>PgUp</code></p>
<dd> Show the previous page of the process/thread list.<br />
 With the arrow-up key the list can be scrolled upwards with single lines.</dl>
<dl>
<dt><code>^B</code></p>
<dd> Show the previous page of the process/thread list (backward).<br />
 With the arrow-up key the list can be scrolled upwards with single lines.</dl>
<dl>
<dt><code>^L</code></p>
<dd> Redraw the screen.</dl>
<h2>RAW DATA STORAGE</h2>
<p> In order to store system and process level statistics for long-term analysis (e.g. to check the system load and the active processes running yesterday between 3:00 and 4:00 PM), <i>atop</i> can store the system and process level statistics in compressed binary format in a raw file with the flag <code>-w</code> followed by the filename. If this file already exists and is recognized as a raw data file, <i>atop</i> will append new samples to the file (starting with a sample which reflects the activity since boot); if the file does not exist, it will be created.<br />
 By default only processes which have been active during the interval are stored in the raw file. When the flag <code>-a</code> is specified, all processes will be stored.<br />
 The interval (default: 10 seconds) and number of samples (default: infinite) can be passed as last arguments. Instead of the number of samples, the flag <code>-S</code> can be used to indicate that <i>atop</i> should finish anyhow before midnight. </p>
<p> A raw file can be read and visualized again with the flag <code>-r</code> followed by the filename. If no filename is specified, the file <code>/var/log/atop/atop_</code><i>YYYYMMDD</i> is opened for input (where <i>YYYYMMDD</i> are digits representing the current date). If a filename is specified in the format YYYYMMDD (representing any valid date), the file <code>/var/log/atop/atop_</code><i>YYYYMMDD</i> is opened. If a filename with the symbolic name <code>y</code> is specified, yesterday&#8217;s daily logfile is opened (this can be repeated so &#8216;yyyy&#8217; indicates the logfile of four days ago).<br />
 The samples from the file can be viewed interactively by using the key &#8216;t&#8217; to show the next sample, the key &#8216;T&#8217; to show the previous sample, the key &#8216;b&#8217; to branch to a particular time or the key &#8216;r&#8217; to rewind to the begin of the file.<br />
 When output is redirected to a file or pipe, <code>atop</code> prints all samples in plain ASCII. The default line length is 80 characters in that case; with the flag <code>-L</code> followed by an alternate line length, more (or less) columns will be shown.<br />
 With the flag <code>-b</code> (begin time) and/or <code>-e</code> (end time) followed by a time argument of the form HH:MM, a certain time period within the raw file can be selected. </p>
<p> When <code>atop</code> is installed, the script <code>atop.daily</code> is stored in the <i>/etc/atop</i> directory. This scripts takes care that <code>atop</code> is activated every day at midnight to write compressed binary data to the file <code>/var/log/atop/atop_</code><i>YYYYMMDD</i> with an interval of 10 minutes.<br />
 Furthermore the script removes all raw files which are older than four weeks.<br />
 The script is activated via the <code>cron</code> daemon using the file <i>/etc/cron.d/atop</i> with the contents<br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 * * * root /etc/atop/atop.daily</code> </p>
<p> When the package <code>psacct</code> is installed, the process accounting is automatically restarted via the <code>logrotate</code> mechanism. The file <code>/etc/logrotate.d/psaccs_atop</code> takes care that <code>atop</code> is finished just before the rotation of the process accounting file and the file <code>/etc/logrotate.d/psaccu_atop</code> takes care that <code>atop</code> is restarted again after the rotation. When the package <code>psacct</code> is not installed, these logrotate-files have no effect.</p>
<h2>OUTPUT DESCRIPTION</h2>
<p> The first sample shows the system level activity since boot (the elapsed time in the header shows the time since boot). Note that particular counters could have reached their maximum value (several times) and started by zero again, so do not rely on these figures. </p>
<p> For every sample <i>atop</i> first shows the lines related to system level activity. If a particular system resource has not been used during the interval, the entire line related to this resource is suppressed. So the number of system level lines may vary for each sample.<br />
 After that a list is shown of processes which have been active during the last interval. This list is by default sorted on cpu consumption, but this order can be changed by the keys which are previously described. </p>
<p> If values have to be shown by <i>atop</i> which do not fit in the column width, another format is used. If e.g. a cpu-consumption of 233216 milliseconds should be shown in a column width of 4 positions, it is shown as `233s&#8217; (in seconds). For large memory figures, another unit is chosen if the value does not fit (Mb instead of Kb, Gb instead of Mb, Tb instead of Gb, &#8230;). For other values, a kind of exponent notation is used (value 123456789 shown in a column of 5 positions gives 123e6).</p>
<h2>OUTPUT DESCRIPTION &#8211; SYSTEM LEVEL</h2>
<p> The system level information consists of the following output lines: </p>
<dl>
<dt><code>PRC</code></p>
<dd> Process and thread level totals.<br />
 This line contains the total cpu time consumed in system mode (`sys&#8217;) and in user mode (`user&#8217;), the total number of processes present at this moment (`#proc&#8217;), the total number of threads present at this moment in state `running&#8217; (`#trun&#8217;), `sleeping interruptible&#8217; (`#tslpi&#8217;) and `sleeping uninterruptible&#8217; (`#tslpu&#8217;), the number of zombie processes (`#zombie&#8217;), the number of clone system calls (`clones&#8217;), and the number of processes that ended during the interval (`#exit&#8217;) when process accounting is used. Instead of `#exit` the last column may indicate that process accounting could not be activated (`no procacct`).<br />
 If the screen-width does not allow all of these counters, only a relevant subset is shown.</dl>
<dl>
<dt><code>CPU</code></p>
<dd> CPU utilization.<br />
 At least one line is shown for the total occupation of all CPUs together.<br />
 In case of a multi-processor system, an additional line is shown for every individual processor (with `cpu&#8217; in lower case), sorted on activity. Inactive CPUs will not be shown by default. The lines showing the per-cpu occupation contain the cpu number in the last field. </p>
<p> Every line contains the percentage of cpu time spent in kernel mode by all active processes (`sys&#8217;), the percentage of cpu time consumed in user mode (`user&#8217;) for all active processes (including processes running with a nice value larger than zero), the percentage of cpu time spent for interrupt handling (`irq&#8217;) including softirq, the percentage of unused cpu time while no processes were waiting for disk-I/O (`idle&#8217;), and the percentage of unused cpu time while at least one process was waiting for disk-I/O (`wait&#8217;).<br />
 In case of per-cpu occupation, the last column shows the cpu number and the wait percentage (`w&#8217;) for that cpu. The number of lines showing the per-cpu occupation can be limited. </p>
<p> For virtual machines the steal-percentage is shown (`steal&#8217;), reflecting the percentage of cpu time stolen by other virtual machines running on the same hardware.<br />
 For physical machines hosting one or more virtual machines, the guest-percentage is shown (`guest&#8217;), reflecting the percentage of cpu time used by the virtual machines. Notice that this percentage overlaps the user-percentage. </p>
<p> In case of frequency-scaling, all previously mentioned CPU-percentages are relative to the used scaling of the CPU during the interval. If a CPU has been active for e.g. 50% in user mode during the interval while the frequency-scaling of that CPU was 40%, only 20% of the full capacity of the CPU has been used in user mode.<br />
 In case that the kernel module `cpufreq_stats&#8217; is active (after issueing `modprobe cpufreq_stats&#8217;), the <i>average</i> frequency (`avgf&#8217;) and the <i>average</i> scaling percentage (`avgscal&#8217;) is shown. Otherwise the <i>current</i> frequency (`curf&#8217;) and the <i>current</i> scaling percentage (`curscal&#8217;) is shown at the moment that the sample is taken. </p>
<p> If the screen-width does not allow all of these counters, only a relevant subset is shown.</dl>
<dl>
<dt><code>CPL</code></p>
<dd> CPU load information.<br />
 This line contains the load average figures reflecting the number of threads that are available to run on a CPU (i.e. part of the runqueue) or that are waiting for disk I/O. These figures are averaged over 1 (`avg1&#8242;), 5 (`avg5&#8242;) and 15 (`avg15&#8242;) minutes.<br />
 Furthermore the number of context switches (`csw&#8217;), the number of serviced interrupts (`intr&#8217;) and the number of available CPUs are shown. </p>
<p> If the screen-width does not allow all of these counters, only a relevant subset is shown.</dl>
<dl>
<dt><code>MEM</code></p>
<dd> Memory occupation.<br />
 This line contains the total amount of physical memory (`tot&#8217;), the amount of memory which is currently free (`free&#8217;), the amount of memory in use as page cache including the total resident shared memory (`cache&#8217;), the amount of memory within the page cache that has to be flushed to disk (`dirty&#8217;), the amount of memory used for filesystem meta data (`buff&#8217;), the amount of memory being used for kernel mallocs (`slab&#8217;), the amount of slab memory that is reclaimable (`slrec&#8217;), the resident size of shared memory including tmpfs (`shmem`), the resident size of shared memory (`shrss`) the amount of shared memory that is currently swapped (`shswp`), the amount of memory that is currently claimed by vmware&#8217;s balloon driver (`vmbal`), the amount of memory that is claimed for huge pages (`hptot`), and the amount of huge page memory that is really in use (`hpuse`). </p>
<p> If the screen-width does not allow all of these counters, only a relevant subset is shown.</dl>
<dl>
<dt><code>SWP</code></p>
<dd> Swap occupation and overcommit info.<br />
 This line contains the total amount of swap space on disk (`tot&#8217;) and the amount of free swap space (`free&#8217;).<br />
 Furthermore the committed virtual memory space (`vmcom&#8217;) and the maximum limit of the committed space (`vmlim&#8217;, which is by default swap size plus 50% of memory size) is shown. The committed space is the reserved virtual space for all allocations of private memory space for processes. The kernel only verifies whether the committed space exceeds the limit if strict overcommit handling is configured (vm.overcommit_memory is 2).</dl>
<dl>
<dt><code>PAG</code></p>
<dd> Paging frequency.<br />
 This line contains the number of scanned pages (`scan&#8217;) due to the fact that free memory drops below a particular threshold and the number times that the kernel tries to reclaim pages due to an urgent need (`stall&#8217;).<br />
 Also the number of memory pages the system read from swap space (`swin&#8217;) and the number of memory pages the system wrote to swap space (`swout&#8217;) are shown.</dl>
<dl>
<dt><code>LVM/MDD/DSK</code></p>
<dd> Logical volume/multiple device/disk utilization.<br />
 Per active unit one line is produced, sorted on unit activity. Such line shows the name (e.g. VolGroup00-lvtmp for a logical volume or sda for a hard disk), the busy percentage i.e. the portion of time that the unit was busy handling requests (`busy&#8217;), the number of read requests issued (`read&#8217;), the number of write requests issued (`write&#8217;), the number of KiBytes per read (`KiB/r&#8217;), the number of KiBytes per write (`KiB/w&#8217;), the number of MiBytes per second throughput for reads (`MBr/s&#8217;), the number of MiBytes per second throughput for writes (`MBw/s&#8217;), the average queue depth (`avq&#8217;) and the average number of milliseconds needed by a request (`avio&#8217;) for seek, latency and data transfer.<br />
 If the screen-width does not allow all of these counters, only a relevant subset is shown. </p>
<p> The number of lines showing the units can be limited per class (LVM, MDD or DSK) with the &#8216;l&#8217; key or statically (see separate man-page of atoprc). By specifying the value 0 for a particular class, no lines will be shown any more for that class.</dl>
<dl>
<dt><code>NET</code></p>
<dd> Network utilization (TCP/IP).<br />
 One line is shown for activity of the transport layer (TCP and UDP), one line for the IP layer and one line per active interface.<br />
 For the transport layer, counters are shown concerning the number of received TCP segments including those received in error (`tcpi&#8217;), the number of transmitted TCP segments excluding those containing only retransmitted octets (`tcpo&#8217;), the number of UDP datagrams received (`udpi&#8217;), the number of UDP datagrams transmitted (`udpo&#8217;), the number of active TCP opens (`tcpao&#8217;), the number of passive TCP opens (`tcppo&#8217;), the number of TCP output retransmissions (`tcprs&#8217;), the number of TCP input errors (`tcpie&#8217;), the number of TCP output resets (`tcpor&#8217;), the number of UDP no ports (`udpnp&#8217;), and the number of UDP input errors (`udpie&#8217;).<br />
 If the screen-width does not allow all of these counters, only a relevant subset is shown.<br />
 These counters are related to IPv4 and IPv6 combined. </p>
<p> For the IP layer, counters are shown concerning the number of IP datagrams received from interfaces, including those received in error (`ipi&#8217;), the number of IP datagrams that local higher-layer protocols offered for transmission (`ipo&#8217;), the number of received IP datagrams which were forwarded to other interfaces (`ipfrw&#8217;), the number of IP datagrams which were delivered to local higher-layer protocols (`deliv&#8217;), the number of received ICMP datagrams (`icmpi&#8217;), and the number of transmitted ICMP datagrams (`icmpo&#8217;).<br />
 If the screen-width does not allow all of these counters, only a relevant subset is shown.<br />
 These counters are related to IPv4 and IPv6 combined. </p>
<p> For every active network interface one line is shown, sorted on the interface activity. Such line shows the name of the interface and its busy percentage in the first column. The busy percentage for half duplex is determined by comparing the interface speed with the number of bits transmitted and received per second; for full duplex the interface speed is compared with the highest of either the transmitted or the received bits. When the interface speed can not be determined (e.g. for the loopback interface), `&#8212;&#8216; is shown instead of the percentage.<br />
 Furthermore the number of received packets (`pcki&#8217;), the number of transmitted packets (`pcko&#8217;), the effective amount of bits received per second (`si&#8217;), the effective amount of bits transmitted per second (`so&#8217;), the number of collisions (`coll&#8217;), the number of received multicast packets (`mlti&#8217;), the number of errors while receiving a packet (`erri&#8217;), the number of errors while transmitting a packet (`erro&#8217;), the number of received packets dropped (`drpi&#8217;), and the number of transmitted packets dropped (`drpo&#8217;).<br />
 If the screen-width does not allow all of these counters, only a relevant subset is shown.<br />
 The number of lines showing the network interfaces can be limited.</dl>
<h2>OUTPUT DESCRIPTION &#8211; PROCESS LEVEL</h2>
<p> Following the system level information, the processes are shown from which the resource utilization has changed during the last interval. These processes might have used cpu time or issued disk or network requests. However a process is also shown if part of it has been paged out due to lack of memory (while the process itself was in sleep state). </p>
<p> Per process the following fields may be shown (in alphabetical order), depending on the current output mode as described in the section INTERACTIVE COMMANDS and depending on the current width of your window: </p>
<dl>
<dt><code>AVGRSZ</code></p>
<dd> The average size of one read-action on disk.</dl>
<dl>
<dt><code>AVGWSZ</code></p>
<dd> The average size of one write-action on disk.</dl>
<dl>
<dt><code>BANDWI</code></p>
<dd> Total bandwidth for received TCP and UDP packets consumed by this process (bits-per-second). This value can be compared with the value `si&#8217; on interface level (used bandwidth per interface).<br />
 This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>BANDWO</code></p>
<dd> Total bandwidth for sent TCP and UDP packets consumed by this process (bits-per-second). This value can be compared with the value `so&#8217; on interface level (used bandwidth per interface).<br />
 This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>CMD</code></p>
<dd> The name of the process. This name can be surrounded by &quot;less/greater than&quot; signs (`&lt;name&gt;&#8217;) which means that the process has finished during the last interval.<br />
 Behind the abbreviation `CMD&#8217; in the header line, the current page number and the total number of pages of the process/thread list are shown.</dl>
<dl>
<dt><code>COMMAND-LINE</code></p>
<dd> The full command line of the process (including arguments). If the length of the command line exceeds the length of the screen line, the arrow keys -&gt; and &lt;- can be used for horizontal scroll.<br />
 Behind the verb `COMMAND-LINE&#8217; in the header line, the current page number and the total number of pages of the process/thread list are shown.</dl>
<dl>
<dt><code>CPU</code></p>
<dd> The occupation percentage of this process related to the available capacity for this resource on system level.</dl>
<dl>
<dt><code>CPUNR</code></p>
<dd> The identification of the CPU the (main) thread is running on or has recently been running on.</dl>
<dl>
<dt><code>DSK</code></p>
<dd> The occupation percentage of this process related to the total load that is produced by all processes (i.e. total disk accesses by all processes during the last interval).<br />
 This information is shown when per process &quot;storage accounting&quot; is active in the kernel.</dl>
<dl>
<dt><code>EGID</code></p>
<dd> Effective group-id under which this process executes.</dl>
<dl>
<dt><code>ENDATE</code></p>
<dd> Date that the process has been finished. If the process is still running, this field shows `active&#8217;.</dl>
<dl>
<dt><code>ENTIME</code></p>
<dd> Time that the process has been finished. If the process is still running, this field shows `active&#8217;.</dl>
<dl>
<dt><code>ENVID</code></p>
<dd> Virtual environment identified (OpenVZ only).</dl>
<dl>
<dt><code>EUID</code></p>
<dd> Effective user-id under which this process executes.</dl>
<dl>
<dt><code>EXC</code></p>
<dd> The exit code of a terminated process (second position of column `ST&#8217; is E) or the fatal signal number (second position of column `ST&#8217; is S or C).</dl>
<dl>
<dt><code>FSGID</code></p>
<dd> Filesystem group-id under which this process executes.</dl>
<dl>
<dt><code>FSUID</code></p>
<dd> Filesystem user-id under which this process executes.</dl>
<dl>
<dt><code>MAJFLT</code></p>
<dd> The number of page faults issued by this process that have been solved by creating/loading the requested memory page.</dl>
<dl>
<dt><code>MEM</code></p>
<dd> The occupation percentage of this process related to the available capacity for this resource on system level.</dl>
<dl>
<dt><code>MINFLT</code></p>
<dd> The number of page faults issued by this process that have been solved by reclaiming the requested memory page from the free list of pages.</dl>
<dl>
<dt><code>NET</code></p>
<dd> The occupation percentage of this process related to the total load that is produced by all processes (i.e. consumed network bandwidth of all processes during the last interval).<br />
 This information will only be shown when kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>NICE</code></p>
<dd> The more or less static priority that can be given to a process on a scale from -20 (high priority) to +19 (low priority).</dl>
<dl>
<dt><code>NPROCS</code></p>
<dd> The number of active and terminated processes accumulated for this user or program.</dl>
<dl>
<dt><code>PID</code></p>
<dd> Process-id. If a process has been started and finished during the last interval, a `?&#8217; is shown because the process-id is not part of the standard process accounting record.</dl>
<dl>
<dt><code>POLI</code></p>
<dd> The policies &#8216;norm&#8217; (normal, which is SCHED_OTHER), &#8216;btch&#8217; (batch) and &#8216;idle&#8217; refer to timesharing processes. The policies &#8216;fifo&#8217; (SCHED_FIFO) and &#8216;rr&#8217; (round robin, which is SCHED_RR) refer to realtime processes.</dl>
<dl>
<dt><code>PPID</code></p>
<dd> Parent process-id. If a process has been started and finished during the last interval, value 0 is shown because the parent process-id is not part of the standard process accounting record.</dl>
<dl>
<dt><code>PRI</code></p>
<dd> The process&#8217; priority ranges from 0 (highest priority) to 139 (lowest priority). Priority 0 to 99 are used for realtime processes (fixed priority independent of their behavior) and priority 100 to 139 for timesharing processes (variable priority depending on their recent CPU consumption and the nice value).</dl>
<dl>
<dt><code>PSIZE</code></p>
<dd> The proportional memory size of this process (or user).<br />
 Every process shares resident memory with other processes. E.g. when a particular program is started several times, the code pages (text) are only loaded once in memory and shared by all incarnations. Also the code of shared libraries is shared by all processes using that shared library, as well as shared memory and memory-mapped files. For the PSIZE calculation of a process, the resident memory of a process that is shared with other processes is divided by the number of sharers. This means, that every process is accounted for a proportional part of that memory. Accumulating the PSIZE values of all processes in the system gives a reliable impression of the total resident memory consumed by all processes.<br />
 Since gathering of all values that are needed to calculate the PSIZE is a relatively time-consuming task, the &#8216;R&#8217; key (or &#8216;-R&#8217; flag) should be active. Gathering these values also requires superuser privileges (otherwise &#8216;?K&#8217; is shown in the output).<br />
 If a process has finished during the last interval, no value is shown since the proportional memory size is not part of the standard process accounting record.</dl>
<dl>
<dt><code>RDDSK </code></p>
<dd> When the kernel maintains standard io statistics (&gt;= 2.6.20):<br />
 The read data transfer issued physically on disk (so reading from the disk cache is not accounted for).<br />
 Unfortunately, the kernel aggregates the data tranfer of a process to the data transfer of its parent process when terminating, so you might see transfers for (parent) processes like cron, bash or init, that are not really issued by them.</dl>
<dl>
<dt><code>RGID</code></p>
<dd> The real group-id under which the process executes.</dl>
<dl>
<dt><code>RGROW </code></p>
<dd> The amount of resident memory that the process has grown during the last interval. A resident growth can be caused by touching memory pages which were not physically created/loaded before (load-on-demand). Note that a resident growth can also be negative e.g. when part of the process is paged out due to lack of memory or when the process frees dynamically allocated memory. For a process which started during the last interval, the resident growth reflects the total resident size of the process at that moment.<br />
 If a process has finished during the last interval, no value is shown since resident memory occupation is not part of the standard process accounting record.</dl>
<dl>
<dt><code>RNET </code></p>
<dd> The number of TCP- and UDP packets received by this process. This information will only be shown when kernel module `netatop&#8217; is installed.<br />
 If a process has finished during the last interval, no value is shown since network counters are not part of the standard process accounting record.</dl>
<dl>
<dt><code>RSIZE</code></p>
<dd> The total resident memory usage consumed by this process (or user). Notice that the RSIZE of a process includes all resident memory used by that process, even if certain memory parts are shared with other processes (see also the explanation of PSIZE).<br />
 If a process has finished during the last interval, no value is shown since resident memory occupation is not part of the standard process accounting record.</dl>
<dl>
<dt><code>RTPR</code></p>
<dd> Realtime priority according the POSIX standard. Value can be 0 for a timesharing process (policy &#8216;norm&#8217;, &#8216;btch&#8217; or &#8216;idle&#8217;) or ranges from 1 (lowest) till 99 (highest) for a realtime process (policy &#8216;rr&#8217; or &#8216;fifo&#8217;).</dl>
<dl>
<dt><code>RUID</code></p>
<dd> The real user-id under which the process executes.</dl>
<dl>
<dt><code>S</code></p>
<dd> The current state of the (main) thread: `R&#8217; for running (currently processing or in the runqueue), `S&#8217; for sleeping interruptible (wait for an event to occur), `D&#8217; for sleeping non-interruptible, `Z&#8217; for zombie (waiting to be synchronized with its parent process), `T&#8217; for stopped (suspended or traced), `W&#8217; for swapping, and `E&#8217; (exit) for processes which have finished during the last interval.</dl>
<dl>
<dt><code>SGID</code></p>
<dd> The saved group-id of the process.</dl>
<dl>
<dt><code>SNET </code></p>
<dd> The number of TCP and UDP packets transmitted by this process. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>ST</code></p>
<dd> The status of a process.<br />
 The first position indicates if the process has been started during the last interval (the value <i>N</i> means &#8216;new process&#8217;). </p>
<p> The second position indicates if the process has been finished during the last interval.<br />
 The value <i>E</i> means &#8216;exit&#8217; on the process&#8217; own initiative; the exit code is displayed in the column `EXC&#8217;.<br />
 The value <i>S</i> means that the process has been terminated unvoluntarily by a signal; the signal number is displayed in the in the column `EXC&#8217;.<br />
 The value <i>C</i> means that the process has been terminated unvoluntarily by a signal, producing a core dump in its current directory; the signal number is displayed in the column `EXC&#8217;.</dl>
<dl>
<dt><code>STDATE</code></p>
<dd> The start date of the process.</dl>
<dl>
<dt><code>STTIME</code></p>
<dd> The start time of the process.</dl>
<dl>
<dt><code>SUID</code></p>
<dd> The saved user-id of the process.</dl>
<dl>
<dt><code>SWAPSZ</code></p>
<dd> The swap space consumed by this process (or user).</dl>
<dl>
<dt><code>SYSCPU</code></p>
<dd> CPU time consumption of this process in system mode (kernel mode), usually due to system call handling.</dl>
<dl>
<dt><code>TCPRASZ</code></p>
<dd> The average size of a received TCP buffer in bytes. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>TCPRCV</code></p>
<dd> The number of TCP packets received for this process. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>TCPSASZ</code></p>
<dd> The average size of a transmitted TCP buffer in bytes. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>TCPSND</code></p>
<dd> The number of TCP packets transmitted for this process. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>THR</code></p>
<dd> Total number of threads within this process. All related threads are contained in a thread group, represented by <i>atop</i> as one line or as a separate line when the &#8216;y&#8217; key (or -y flag) is active. </p>
<p> On Linux 2.4 systems it is hardly possible to determine which threads (i.e. processes) are related to the same thread group. Every thread is represented by <i>atop</i> as a separate line.</dl>
<dl>
<dt><code>TID</code></p>
<dd> Thread-id. All threads within a process run with the same PID but with a different TID. This value is shown for individual threads in multi-threaded processes (when using the key &#8216;y&#8217;).</dl>
<dl>
<dt><code>TRUN</code></p>
<dd> Number of threads within this process that are in the state &#8216;running&#8217; (R).</dl>
<dl>
<dt><code>TSLPI</code></p>
<dd> Number of threads within this process that are in the state &#8216;interruptible sleeping&#8217; (S).</dl>
<dl>
<dt><code>TSLPU</code></p>
<dd> Number of threads within this process that are in the state &#8216;uninterruptible sleeping&#8217; (D).</dl>
<dl>
<dt><code>UDPRASZ</code></p>
<dd> The average size of a received UDP packet in bytes. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>UDPRCV</code></p>
<dd> The number of UDP packets received by this process. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>UDPSASZ</code></p>
<dd> The average size of a transmitted UDP packets in bytes. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>UDPSND</code></p>
<dd> The number of UDP packets transmitted by this process. This information will only be shown when the kernel module `netatop&#8217; is loaded.</dl>
<dl>
<dt><code>USRCPU</code></p>
<dd> CPU time consumption of this process in user mode, due to processing the own program text.</dl>
<dl>
<dt><code>VDATA</code></p>
<dd> The virtual memory size of the private data used by this process (including heap and shared library data).</dl>
<dl>
<dt><code>VGROW </code></p>
<dd> The amount of virtual memory that the process has grown during the last interval. A virtual growth can be caused by e.g. issueing a malloc() or attaching a shared memory segment. Note that a virtual growth can also be negative by e.g. issueing a free() or detaching a shared memory segment. For a process which started during the last interval, the virtual growth reflects the total virtual size of the process at that moment.<br />
 If a process has finished during the last interval, no value is shown since virtual memory occupation is not part of the standard process accounting record.</dl>
<dl>
<dt><code>VSIZE</code></p>
<dd> The total virtual memory usage consumed by this process (or user).<br />
 If a process has finished during the last interval, no value is shown since virtual memory occupation is not part of the standard process accounting record.</dl>
<dl>
<dt><code>VSLIBS</code></p>
<dd> The virtual memory size of the (shared) text of all shared libraries used by this process.</dl>
<dl>
<dt><code>VSTACK</code></p>
<dd> The virtual memory size of the (private) stack used by this process</dl>
<dl>
<dt><code>VSTEXT</code></p>
<dd> The virtual memory size of the (shared) text of the executable program.</dl>
<dl>
<dt><code>WRDSK </code></p>
<dd> When the kernel maintains standard io statistics (&gt;= 2.6.20):<br />
 The write data transfer issued physically on disk (so writing to the disk cache is not accounted for). This counter is maintained for the application process that writes its data to the cache (assuming that this data is physically transferred to disk later on). Notice that disk I/O needed for swapping is not taken into account.<br />
 Unfortunately, the kernel aggregates the data tranfer of a process to the data transfer of its parent process when terminating, so you might see transfers for (parent) processes like cron, bash or init, that are not really issued by them.</dl>
<dl>
<dt><code>WCANCL</code></p>
<dd> When the kernel maintains standard io statistics (&gt;= 2.6.20):<br />
 The write data transfer previously accounted for this process or another process that has been cancelled. Suppose that a process writes new data to a file and that data is removed again before the cache buffers have been flushed to disk. Then the original process shows the written data as WRDSK, while the process that removes/truncates the file shows the unflushed removed data as WCANCL.</dl>
<h2>PARSEABLE OUTPUT</h2>
<p> With the flag <code>-P</code> followed by a list of one or more labels (comma-separated), parseable output is produced for each sample. The labels that can be specified for system-level statistics correspond to the labels (first verb of each line) that can be found in the interactive output: &quot;CPU&quot;, &quot;cpu&quot; &quot;CPL&quot; &quot;MEM&quot;, &quot;SWP&quot;, &quot;PAG&quot;, &quot;LVM&quot;, &quot;MDD&quot;, &quot;DSK&quot; and &quot;NET&quot;.<br />
 For process-level statistics special labels are introduced: &quot;PRG&quot; (general), &quot;PRC&quot; (cpu), &quot;PRM&quot; (memory), &quot;PRD&quot; (disk, only if &quot;storage accounting&quot; is active) and &quot;PRN&quot; (network, only if the kernel module &#8216;netatop&#8217; has been installed).<br />
 With the label &quot;ALL&quot;, all system and process level statistics are shown. </p>
<p> For every interval all requested lines are shown whereafter <code>atop</code> shows a line just containing the label &quot;SEP&quot; as a separator before the lines for the next sample are generated.<br />
 When a sample contains the values since boot, <code>atop</code> shows a line just containing the label &quot;RESET&quot; before the lines for this sample are generated. </p>
<p> The first part of each output-line consists of the following six fields: <code>label</code> (the name of the label), <code>host</code> (the name of this machine), <code>epoch</code> (the time of this interval as number of seconds since 1-1-1970), <code>date</code> (date of this interval in format YYYY/MM/DD), <code>time</code> (time of this interval in format HH:MM:SS), and <code>interval</code> (number of seconds elapsed for this interval). </p>
<p> The subsequent fields of each output-line depend on the label: </p>
<dl>
<dt><code>CPU</code></p>
<dd> Subsequent fields: total number of clock-ticks per second for this machine, number of processors, consumption for all CPUs in system mode (clock-ticks), consumption for all CPUs in user mode (clock-ticks), consumption for all CPUs in user mode for niced processes (clock-ticks), consumption for all CPUs in idle mode (clock-ticks), consumption for all CPUs in wait mode (clock-ticks), consumption for all CPUs in irq mode (clock-ticks), consumption for all CPUs in softirq mode (clock-ticks), consumption for all CPUs in steal mode (clock-ticks), consumption for all CPUs in guest mode (clock-ticks) overlapping user mode, frequency of all CPUs and frequency percentage of all CPUs.</p>
<dt><code>cpu</code></p>
<dd> Subsequent fields: total number of clock-ticks per second for this machine, processor-number, consumption for this CPU in system mode (clock-ticks), consumption for this CPU in user mode (clock-ticks), consumption for this CPU in user mode for niced processes (clock-ticks), consumption for this CPU in idle mode (clock-ticks), consumption for this CPU in wait mode (clock-ticks), consumption for this CPU in irq mode (clock-ticks), consumption for this CPU in softirq mode (clock-ticks), consumption for this CPU in steal mode (clock-ticks), consumption for this CPU in guest mode (clock-ticks) overlapping user mode, frequency of this CPU and frequency percentage of this CPU.</p>
<dt><code>CPL</code></p>
<dd> Subsequent fields: number of processors, load average for last minute, load average for last five minutes, load average for last fifteen minutes, number of context-switches, and number of device interrupts.</p>
<dt><code>MEM</code></p>
<dd> Subsequent fields: page size for this machine (in bytes), size of physical memory (pages), size of free memory (pages), size of page cache (pages), size of buffer cache (pages), size of slab (pages), dirty pages in cache (pages), reclaimable part of slab (pages), size of vmware&#8217;s balloon pages (pages), total size of shared memory (pages), size of resident shared memory (pages), size of swapped shared memory (pages), huge page size (in bytes), total size of huge pages (huge pages), and size of free huge pages (huge pages).</p>
<dt><code>SWP</code></p>
<dd> Subsequent fields: page size for this machine (in bytes), size of swap (pages), size of free swap (pages), 0 (future use), size of committed space (pages), and limit for committed space (pages).</p>
<dt><code>PAG</code></p>
<dd> Subsequent fields: page size for this machine (in bytes), number of page scans, number of allocstalls, 0 (future use), number of swapins, and number of swapouts.</p>
<dt><code>LVM/MDD/DSK</code></p>
<dd> For every logical volume/multiple device/hard disk one line is shown.<br />
 Subsequent fields: name, number of milliseconds spent for I/O, number of reads issued, number of sectors transferred for reads, number of writes issued, and number of sectors transferred for write.</p>
<dt><code>NET</code></p>
<dd> First one line is produced for the upper layers of the TCP/IP stack.<br />
 Subsequent fields: the verb &quot;upper&quot;, number of packets received by TCP, number of packets transmitted by TCP, number of packets received by UDP, number of packets transmitted by UDP, number of packets received by IP, number of packets transmitted by IP, number of packets delivered to higher layers by IP, and number of packets forwarded by IP. </p>
<p> Next one line is shown for every interface.<br />
 Subsequent fields: name of the interface, number of packets received by the interface, number of bytes received by the interface, number of packets transmitted by the interface, number of bytes transmitted by the interface, interface speed, and duplex mode (0=half, 1=full).</p>
<dt><code>PRG</code></p>
<dd> For every process one line is shown.<br />
 Subsequent fields: PID (unique ID of task), name (between brackets), state, real uid, real gid, TGID (group number of related tasks/threads), total number of threads, exit code, start time (epoch), full command line (between brackets), PPID, number of threads in state &#8216;running&#8217; (R), number of threads in state &#8216;interruptible sleeping&#8217; (S), number of threads in state &#8216;uninterruptible sleeping&#8217; (D), effective uid, effective gid, saved uid, saved gid, filesystem uid, filesystem gid, elapsed time (hertz) and is_process (y/n).</p>
<dt><code>PRC</code></p>
<dd> For every process one line is shown.<br />
 Subsequent fields: PID, name (between brackets), state, total number of clock-ticks per second for this machine, CPU-consumption in user mode (clockticks), CPU-consumption in system mode (clockticks), nice value, priority, realtime priority, scheduling policy, current CPU, sleep average, TGID (group number of related tasks/threads) and is_process (y/n).</p>
<dt><code>PRM</code></p>
<dd> For every process one line is shown.<br />
 Subsequent fields: PID, name (between brackets), state, page size for this machine (in bytes), virtual memory size (Kbytes), resident memory size (Kbytes), shared text memory size (Kbytes), virtual memory growth (Kbytes), resident memory growth (Kbytes), number of minor page faults, number of major page faults, virtual library exec size (Kbytes), virtual data size (Kbytes), virtual stack size (Kbytes), swap space used (Kbytes), TGID (group number of related tasks/threads), is_process (y/n) and proportional set size (Kbytes) if in &#8216;R&#8217; option is specified.</p>
<dt><code>PRD</code></p>
<dd> For every process one line is shown.<br />
 Subsequent fields: PID, name (between brackets), state, obsoleted kernel patch installed (&#8216;n&#8217;), standard io statistics used (&#8216;y&#8217; or &#8216;n&#8217;), number of reads on disk, cumulative number of sectors read, number of writes on disk, cumulative number of sectors written, cancelled number of written sectors, TGID (group number of related tasks/threads) and is_process (y/n).<br />
 If the standard I/O statistics (&gt;= 2.6.20) are not used, the disk I/O counters per process are not relevant. The counters &#8216;number of reads on disk&#8217; and &#8216;number of writes on disk&#8217; are obsoleted anyhow.</p>
<dt><code>PRN</code></p>
<dd> For every process one line is shown.<br />
 Subsequent fields: PID, name (between brackets), state, kernel module &#8216;netatop&#8217; loaded (&#8216;y&#8217; or &#8216;n&#8217;), number of TCP-packets transmitted, cumulative size of TCP-packets transmitted, number of TCP-packets received, cumulative size of TCP-packets received, number of UDP-packets transmitted, cumulative size of UDP-packets transmitted, number of UDP-packets received, cumulative size of UDP-packets transmitted, number of raw packets transmitted (obsolete, always 0), number of raw packets received (obsolete, always 0), TGID (group number of related tasks/threads) and is_process (y/n).<br />
 If the kernel module is not active, the network I/O counters per process are not relevant.</dl>
<h2>EXAMPLES</h2>
<p> To monitor the current system load interactively with an interval of 5 seconds: </p>
<dl>
<dt><code>&nbsp;<wbr> atop 5</code></p>
<dd></dl>
<p> To monitor the system load and write it to a file (in plain ASCII) with an interval of one minute during half an hour with active processes sorted on memory consumption: </p>
<dl>
<dt><code>&nbsp;<wbr> atop -M 60 30 &gt; /log/atop.mem</code></p>
<dd></dl>
<p> Store information about the system and process activity in binary compressed form to a file with an interval of ten minutes during an hour: </p>
<dl>
<dt><code>&nbsp;<wbr> atop -w /tmp/atop.raw 600 6</code></p>
<dd></dl>
<p> View the contents of this file interactively: </p>
<p> <code>&nbsp;<wbr> atop -r /tmp/atop.raw</code> </p>
<p> View the processor and disk utilization of this file in parseable format: </p>
<p> <code>&nbsp;<wbr> atop -PCPU,DSK -r /tmp/atop.raw</code> </p>
<p> View the contents of today&#8217;s standard logfile interactively: </p>
<p> <code>&nbsp;<wbr> atop -r</code> </p>
<p> View the contents of the standard logfile of the day before yesterday interactively: </p>
<p> <code>&nbsp;<wbr> atop -r yy</code> </p>
<p> View the contents of the standard logfile of 2014, June 7 from 02:00 PM onwards interactively: </p>
<p> <code>&nbsp;<wbr> atop -r 20140607 -b 14:00</code> </p>
<h2>FILES</h2>
<dl>
<dt><code>/var/run/pacct_shadow.d/</code></p>
<dd> Directory containing the process accounting shadow files that are used by <i>atop</i> when the <i>atopacctd</i> daemon is active.</dl>
<dl>
<dt><code>/tmp/atop.d/atop.acct</code></p>
<dd> File in which the kernel writes the accounting records when <i>atop</i> itself has activated the process accounting mechanism.</dl>
<dl>
<dt><code>/etc/atoprc</code></p>
<dd> Configuration file containing system-wide default values. See related man-page.</dl>
<dl>
<dt><code>~/.atoprc</code></p>
<dd> Configuration file containing personal default values. See related man-page.</dl>
<dl>
<dt><code>/var/log/atop/atop_</code><i>YYYYMMDD</i></p>
<dd> Raw file, where <i>YYYYMMDD</i> are digits representing the current date. This name is used by the script <code>atop.daily</code> as default name for the output file, and by <code>atop</code> as default name for the input file when using the <code>-r</code> flag.<br />
 All binary system and process level data in this file has been stored in compressed format.</dl>
<dl>
<dt><code>/var/run/netatop.log</code></p>
<dd> File that contains the netpertask structs containing the network counters of exited processes. These structs are written by the <i>netatopd</i> daemon and read by <i>atop</i> after reading the standard process accounting records.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-atopsar/">atopsar</a>(1),</code> <code><a href="/docs/linux/man/5-atoprc/">atoprc</a>(5),</code> <code><a href="/docs/linux/man/8-atopacctd/">atopacctd</a>(8),</code> <code><a href="/docs/linux/man/4-netatop/">netatop</a>(4),</code> <code><a href="/docs/linux/man/8-netatopd/">netatopd</a>(8),</code> <code><a href="/docs/linux/man/8-logrotate/">logrotate</a>(8)</code><br />
 <code><a rel="nofollow" href="http://www.atoptool.nl">http://www.atoptool.nl</a></code></p>
<h2>AUTHOR</h2>
<p> Gerlof Langeveld (gerlof.langeveld [at] atoptool.nl)<br />
 JC van Winkel </p>
<h2>Index</h2>
