---
title: "htop(1)"
name: "htop"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htop/"
description: "htop – interactive process viewer"
---

<h2>SYNOPSIS</h2>
<p> <code>htop</code> [<code>-dCFhpustvH</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>htop</code> is a cross-platform ncurses-based process viewer. </p>
<p> It is similar to <code>top</code>, but allows you to scroll vertically and horizontally, and interact using a pointing device (mouse). You can observe all processes running on the system, along with their command line arguments, as well as view them in a tree format, select multiple processes and acting on them all at once. </p>
<p> Tasks related to processes (killing, renicing) can be done without entering their PIDs. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d &#8211;delay=DELAY</code></dt>
<dd> Delay between updates, in tenths of seconds. If the delay value is less than 1 it is increased to 1, i.e. 1/10 second. If the delay value is greater than 100, it is decreased to 100, i.e. 10 seconds.</dd>
<dt><code>-C &#8211;no-color &#8211;no-colour</code></dt>
<dd> Start <code>htop</code> in monochrome mode</dd>
<dt><code>-F &#8211;filter=FILTER</dt>
<dd> Filter processes by command</dd>
<dt>-h &#8211;help</dt>
<dd> Display a help message and exit</dd>
<dt>-p &#8211;pid=PID,PID&#8230;</code></dt>
<dd> Show only the given PIDs</dd>
<dt><code>-s &#8211;sort-key COLUMN</code></dt>
<dd> Sort by this column (use &#8211;sort-key help for a column list). This will force a list view unless you specify -t at the same time.</dd>
<dt><code>-u &#8211;user=USERNAME</code></dt>
<dd> Show only the processes of a given user</dd>
<dt><code>-U &#8211;no-unicode</code></dt>
<dd> Do not use unicode but ASCII characters for graph meters</dd>
<dt><code>-M &#8211;no-mouse</code></dt>
<dd> Disable support of mouse control</dd>
<dt><code>-V &#8211;version</dt>
<dd> Output version information and exit</dd>
<dt>-t &#8211;tree</dt>
<dd> Show processes in tree view. This can be used to force a tree view when requesting a sort order with -s.</dd>
<dt>-H &#8211;highlight-changes=DELAY</code></dt>
<dd> Highlight new and old processes</dd></dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> The following commands are supported while in <code>htop</code>:</p>
<dl>
<dt><code>Up, Alt-k</code></dt>
<dd> Select (highlight) the previous process in the process list. Scroll the list if necessary.</dd>
<dt><code>Down, Alt-j</code></dt>
<dd> Select (highlight) the next process in the process list. Scroll the list if necessary.</dd>
<dt><code>Left, Alt-h</code></dt>
<dd> Scroll the process list left.</dd>
<dt><code>Right, Alt-l</code></dt>
<dd> Scroll the process list right.</dd>
<dt><code>PgUp, PgDn</code></dt>
<dd> Scroll the process list up or down one window.</dd>
<dt><code>Home</code></dt>
<dd> Scroll to the top of the process list and select the first process.</dd>
<dt><code>End</code></dt>
<dd> Scroll to the bottom of the process list and select the last process.</dd>
<dt><code>Ctrl-A, ^</code></dt>
<dd> Scroll left to the beginning of the process entry (i.e. beginning of line).</dd>
<dt><code>Ctrl-E, $</code></dt>
<dd> Scroll right to the end of the process entry (i.e. end of line).</dd>
<dt><code>Space</code></dt>
<dd> Tag or untag a process. Commands that can operate on multiple processes, like &quot;kill&quot;, will then apply over the list of tagged processes, instead of the currently highlighted one.</dd>
<dt><code>c</code></dt>
<dd> Tag the current process and its children. Commands that can operate on multiple processes, like &quot;kill&quot;, will then apply over the list of tagged processes, instead of the currently highlighted one.</dd>
<dt><code>U</code></dt>
<dd> Untag all processes (remove all tags added with the Space or c keys).</dd>
<dt><code>s</code></dt>
<dd> Trace process system calls: if <a href="/docs/linux/man/1-strace/">strace</a>(1) is installed, pressing this key will attach it to the currently selected process, presenting a live update of system calls issued by the process.</dd>
<dt><code>l</code></dt>
<dd> Display open files for a process: if lsof(1) is installed, pressing this key will display the list of file descriptors opened by the process.</dd>
<dt><code>w</code></dt>
<dd> Display the command line of the selected process in a separate screen, wrapped onto multiple lines as needed.</dd>
<dt><code>x</code></dt>
<dd> Display the active file locks of the selected process in a separate screen.</dd>
<dt><code>F1, h, ?</code></dt>
<dd> Go to the help screen</dd>
<dt><code>F2, S</code></dt>
<dd> Go to the setup screen, where you can configure the meters displayed at the top of the screen, set various display options, choose among color schemes, and select which columns are displayed, in which order.</dd>
<dt><code>F3, /</code></dt>
<dd> Incrementally search the command lines of all the displayed processes. The currently selected (highlighted) command will update as you type. While in search mode, pressing F3 will cycle through matching occurrences. Pressing Shift-F3 will cycle backwards. </dd>
<p> Alternatively the search can be started by simply typing the command you are looking for, although for the first character normal key bindings take precedence.</p>
<dt><code>F4, \</code></dt>
<dd> Incremental process filtering: type in part of a process command line and only processes whose names match will be shown. To cancel filtering, enter the Filter option again and press Esc.</dd>
<dt><code>F5, t</code></dt>
<dd> Tree view: organize processes by parenthood, and layout the relations between them as a tree. Toggling the key will switch between tree and your previously selected sort view. Selecting a sort view will exit tree view.</dd>
<dt><code>F6, &lt;, &gt;</code></dt>
<dd> Selects a field for sorting, also accessible through &lt; and &gt;. The current sort field is indicated by a highlight in the header.</dd>
<dt><code>F7, ]</code></dt>
<dd> Increase the selected process&#8217;s priority (subtract from &#8216;nice&#8217; value). This can only be done by the superuser.</dd>
<dt><code>F8, [</code></dt>
<dd> Decrease the selected process&#8217;s priority (add to &#8216;nice&#8217; value)</dd>
<dt><code>F9, k</code></dt>
<dd> &quot;Kill&quot; process: sends a signal which is selected in a menu, to one or a group of processes. If processes were tagged, sends the signal to all tagged processes. If none is tagged, sends to the currently selected process.</dd>
<dt><code>F10, q</code></dt>
<dd> Quit</dd>
<dt><code>I</code></dt>
<dd> Invert the sort order: if sort order is increasing, switch to decreasing, and vice-versa.</dd>
<dt><code>+, &#8211;</code></dt>
<dd> When in tree view mode, expand or collapse subtree. When a subtree is collapsed a &quot;+&quot; sign shows to the left of the process name.</dd>
<dt><code>a (on multiprocessor machines)</code></dt>
<dd> Set CPU affinity: mark which CPUs a process is allowed to use.</dd>
<dt><code>u</code></dt>
<dd> Show only processes owned by a specified user.</dd>
<dt><code>N</code></dt>
<dd> Sort by PID.</dd>
<dt><code>M</code></dt>
<dd> Sort by memory usage (top compatibility key).</dd>
<dt><code>P</code></dt>
<dd> Sort by processor usage (top compatibility key).</dd>
<dt><code>T</code></dt>
<dd> Sort by time (top compatibility key).</dd>
<dt><code>F</code></dt>
<dd> &quot;Follow&quot; process: if the sort order causes the currently selected process to move in the list, make the selection bar follow it. This is useful for monitoring a process: this way, you can keep a process always visible on screen. When a movement key is used, &quot;follow&quot; loses effect.</dd>
<dt><code>K</code></dt>
<dd> Hide kernel threads: prevent the threads belonging the kernel to be displayed in the process list. (This is a toggle key.)</dd>
<dt><code>H</code></dt>
<dd> Hide user threads: on systems that represent them differently than ordinary processes (such as recent NPTL-based systems), this can hide threads from userspace processes in the process list. (This is a toggle key.)</dd>
<dt><code>p</code></dt>
<dd> Show full paths to running programs, where applicable. (This is a toggle key.)</dd>
<dt><code>Z</code></dt>
<dd> Pause/resume process updates.</dd>
<dt><code>m</code></dt>
<dd> Merge exe, comm and cmdline, where applicable. (This is a toggle key.)</dd>
<dt><code>Ctrl-L</code></dt>
<dd> Refresh: redraw screen and recalculate values.</dd>
<dt><code>Numbers</code></dt>
<dd> PID search: type in process ID and the selection highlight will be moved to it.</dd></dl>
<h2>COLUMNS</h2>
<p> The following columns can display data about each process. A value of &#8216;-&#8216; in all the rows indicates that a column is unsupported on your system, or currently unimplemented in <code>htop</code>. The names below are the ones used in the &quot;Available Columns&quot; section of the setup screen. If a different name is shown in <code>htop</code>&#8216;s main screen, it is shown below in parenthesis.</p>
<dl>
<dt><code>Command</code></dt>
<dd> The full command line of the process (i.e. program name and arguments). If the option &#8216;Merge exe, comm and cmdline in Command&#8217; (toggled by the &#8216;m&#8217; key) is set, and if readable, the executable path (/proc/[pid]/exe) and the command name (/proc/[pid]/comm) are also shown merged with the command line.</dd>
<dt><code>Comm</code></dt>
<dd> The command name of the process obtained from /proc/[pid]/comm, if readable.</dd>
<dt><code>Exe</code></dt>
<dd> The abbreviated basename of the executable of the process, obtained from /proc/[pid]/exe, if readable. htop is able to read this file on linux for ALL the processes only if it has the capability CAP_SYS_PTRACE or root privileges.</dd>
<dt><code>PID</code></dt>
<dd> The process ID.</dd>
<dt><code>STATE (S)</code></dt>
<dd> The state of the process:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>S</code>&nbsp;for sleeping&nbsp;(idle)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;for running<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>D</code>&nbsp;for disk sleep&nbsp;(uninterruptible)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Z</code>&nbsp;for zombie&nbsp;(waiting for parent to read its exit status)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>T</code>&nbsp;for traced or suspended&nbsp;(e.g by SIGTSTP)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>W</code>&nbsp;for paging</dd>
<dt><code>PPID</code></dt>
<dd> The parent process ID.</dd>
<dt><code>PGRP</code></dt>
<dd> The process&#8217;s group ID.</dd>
<dt><code>SESSION (SID)</code></dt>
<dd> The process&#8217;s session ID.</dd>
<dt><code>TTY_NR (TTY)</code></dt>
<dd> The controlling terminal of the process.</dd>
<dt><code>TPGID</code></dt>
<dd> The process ID of the foreground process group of the controlling terminal.</dd>
<dt><code>MINFLT</code></dt>
<dd> The number of page faults happening in the main memory.</dd>
<dt><code>CMINFLT</code></dt>
<dd> The number of minor faults for the process&#8217;s waited-for children (see MINFLT above).</dd>
<dt><code>MAJFLT</code></dt>
<dd> The number of page faults happening out of the main memory.</dd>
<dt><code>CMAJFLT</code></dt>
<dd> The number of major faults for the process&#8217;s waited-for children (see MAJFLT above).</dd>
<dt><code>UTIME (UTIME+)</code></dt>
<dd> The user CPU time, which is the amount of time the process has spent executing on the CPU in user mode (i.e. everything but system calls), measured in clock ticks.</dd>
<dt><code>STIME (STIME+)</code></dt>
<dd> The system CPU time, which is the amount of time the kernel has spent executing system calls on behalf of the process, measured in clock ticks.</dd>
<dt><code>CUTIME (CUTIME+)</code></dt>
<dd> The children&#8217;s user CPU time, which is the amount of time the process&#8217;s waited-for children have spent executing in user mode (see UTIME above).</dd>
<dt><code>CSTIME (CSTIME+)</code></dt>
<dd> The children&#8217;s system CPU time, which is the amount of time the kernel has spent executing system calls on behalf of all the process&#8217;s waited-for children (see STIME above).</dd>
<dt><code>PRIORITY (PRI)</code></dt>
<dd> The kernel&#8217;s internal priority for the process, usually just its nice value plus twenty. Different for real-time processes.</dd>
<dt><code>NICE (NI)</code></dt>
<dd> The nice value of a process, from 19 (low priority) to -20 (high priority). A high value means the process is being nice, letting others have a higher relative priority. The usual OS permission restrictions for adjusting priority apply.</dd>
<dt><code>STARTTIME (START)</code></dt>
<dd> The time the process was started.</dd>
<dt><code>PROCESSOR (CPU)</code></dt>
<dd> The ID of the CPU the process last executed on.</dd>
<dt><code>M_VIRT (VIRT)</code></dt>
<dd> The size of the virtual memory of the process.</dd>
<dt><code>M_RESIDENT (RES)</code></dt>
<dd> The resident set size (text + data + stack) of the process (i.e. the size of the process&#8217;s used physical memory).</dd>
<dt><code>M_SHARE (SHR)</code></dt>
<dd> The size of the process&#8217;s shared pages.</dd>
<dt><code>M_TRS (CODE)</code></dt>
<dd> The text resident set size of the process (i.e. the size of the process&#8217;s executable instructions).</dd>
<dt><code>M_DRS (DATA)</code></dt>
<dd> The data resident set size (data + stack) of the process (i.e. the size of anything except the process&#8217;s executable instructions).</dd>
<dt><code>M_LRS (LIB)</code></dt>
<dd> The library size of the process.</dd>
<dt><code>M_DT (DIRTY)</code></dt>
<dd> The size of the dirty pages of the process.</dd>
<dt><code>M_SWAP (SWAP)</code></dt>
<dd> The size of the process&#8217;s swapped pages.</dd>
<dt><code>M_PSS (PSS)</code></dt>
<dd> The proportional set size, same as M_RESIDENT but each page is divided by the number of processes sharing it.</dd>
<dt><code>M_M_PSSWP (PSSWP)</code></dt>
<dd> The proportional swap share of this mapping, unlike M_SWAP this does not take into account swapped out page of underlying shmem objects.</dd>
<dt><code>ST_UID (UID)</code></dt>
<dd> The user ID of the process owner.</dd>
<dt><code>PERCENT_CPU (CPU%)</code></dt>
<dd> The percentage of the CPU time that the process is currently using.</dd>
<dt><code>PERCENT_MEM (MEM%)</code></dt>
<dd> The percentage of memory the process is currently using (based on the process&#8217;s resident memory size, see M_RESIDENT above).</dd>
<dt><code>USER</code></dt>
<dd> The username of the process owner, or the user ID if the name can&#8217;t be determined.</dd>
<dt><code>TIME (TIME+)</code></dt>
<dd> The time, measured in clock ticks that the process has spent in user and system time (see UTIME, STIME above).</dd>
<dt><code>NLWP</code></dt>
<dd> The number of threads in the process.</dd>
<dt><code>TGID</code></dt>
<dd> The thread group ID.</dd>
<dt><code>CTID</code></dt>
<dd> OpenVZ container ID, a.k.a virtual environment ID.</dd>
<dt><code>VPID</code></dt>
<dd> OpenVZ process ID.</dd>
<dt><code>VXID</code></dt>
<dd> VServer process ID.</dd>
<dt><code>RCHAR (RD_CHAR)</code></dt>
<dd> The number of bytes the process has read.</dd>
<dt><code>WCHAR (WR_CHAR)</code></dt>
<dd> The number of bytes the process has written.</dd>
<dt><code>SYSCR (RD_SYSC)</code></dt>
<dd> The number of <a href="/docs/linux/man/2-read/">read</a>(2) syscalls for the process.</dd>
<dt><code>SYSCW (WR_SYSC)</code></dt>
<dd> The number of <a href="/docs/linux/man/2-write/">write</a>(2) syscalls for the process.</dd>
<dt><code>RBYTES (IO_RBYTES)</code></dt>
<dd> Bytes of <a href="/docs/linux/man/2-read/">read</a>(2) I/O for the process.</dd>
<dt><code>WBYTES (IO_WBYTES)</code></dt>
<dd> Bytes of <a href="/docs/linux/man/2-write/">write</a>(2) I/O for the process.</dd>
<dt><code>CNCLWB (IO_CANCEL)</code></dt>
<dd> Bytes of cancelled <a href="/docs/linux/man/2-write/">write</a>(2) I/O.</dd>
<dt><code>IO_READ_RATE (DISK READ)</code></dt>
<dd> The I/O rate of <a href="/docs/linux/man/2-read/">read</a>(2) in bytes per second, for the process.</dd>
<dt><code>IO_WRITE_RATE (DISK WRITE)</code></dt>
<dd> The I/O rate of <a href="/docs/linux/man/2-write/">write</a>(2) in bytes per second, for the process.</dd>
<dt><code>IO_RATE (DISK R/W)</code></dt>
<dd> The I/O rate, IO_READ_RATE + IO_WRITE_RATE (see above).</dd>
<dt><code>CGROUP</code></dt>
<dd> Which cgroup the process is in.</dd>
<dt><code>OOM</code></dt>
<dd> OOM killer score.</dd>
<dt><code>CTXT</code></dt>
<dd> Incremental sum of voluntary and nonvoluntary context switches.</dd>
<dt><code>IO_PRIORITY (IO)</code></dt>
<dd> The I/O scheduling class followed by the priority if the class supports it:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;for Realtime<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>B</code>&nbsp;for Best-effort<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>id</code>&nbsp;for Idle</dd>
<dt><code>PERCENT_CPU_DELAY (CPUD%)</code></dt>
<dd> The percentage of time spent waiting for a CPU (while runnable). Requires CAP_NET_ADMIN.</dd>
<dt><code>PERCENT_IO_DELAY (IOD%)</code></dt>
<dd> The percentage of time spent waiting for the completion of synchronous block I/O. Requires CAP_NET_ADMIN.</dd>
<dt><code>PERCENT_SWAP_DELAY (SWAPD%)</code></dt>
<dd> The percentage of time spent swapping in pages. Requires CAP_NET_ADMIN.</dd>
<dt><code>COMM</code></dt>
<dd> The command name for the process. Requires Linux kernel 2.6.33 or newer.</dd>
<dt><code>EXE</code></dt>
<dd> The executable file of the process as reported by the kernel. Requires CAP_SYS_PTRACE and PTRACE_MODE_READ_FSCRED.</dd>
<dt><code>All other flags</code></dt>
<dd> Currently unsupported (always displays &#8216;-&#8216;).</dd></dl>
<h2>EXTERNAL LIBRARIES</h2>
<p> While <code>htop</code> depends on most of the libraries it uses at build time there are two noteworthy exceptions to this rule. These exceptions both relate to data displayed in meters displayed in the header of <code>htop</code> and were intentionally created as optional runtime dependencies instead. These exceptions are described below:</p>
<dl>
<dt><code>libsystemd</code></dt>
<dd> The bindings for libsystemd are used in the SystemD meter to determine the number of active services and the overall system state. Looking for the functions to determine these information at runtime allows for builds to support these meters without forcing the package manager to install these libraries on systems that otherwise don&#8217;t use systemd. </dd>
<p> Summary: no build time dependency, optional runtime dependency on <code>libsystemd</code> via dynamic loading, with <code><a href="/docs/linux/man/1-systemctl/">systemctl</a>(1)</code> fallback.</p>
<dt><code>libsensors</code></dt>
<dd> The bindings for libsensors are used for the CPU temperature readings in the CPU usage meters if displaying the temperature is enabled through the setup screen. In order for <code>htop</code> to show these temperatures correctly though, a proper configuration of libsensors through its usual configuration files is assumed and that all CPU cores correspond to temperature sensors from the <code>coretemp</code> driver with core 0 corresponding to a sensor labelled &quot;Core 0&quot;. The package temperature may be given as &quot;Package id 0&quot;. If missing it is inferred as the maximum value from the available per-core readings. </dd>
<p> Summary: build time dependency on <code><a href="/docs/linux/man/3-libsensors/">libsensors</a>(3)</code> C header files, optional runtime dependency on <code><a href="/docs/linux/man/3-libsensors/">libsensors</a>(3)</code> via dynamic loading.</dl>
<h2>CONFIG FILE</h2>
<p> By default <code>htop</code> reads its configuration from the XDG-compliant path <i>~/.config/htop/htoprc</i>. The configuration file is overwritten by <code>htop</code>&#8216;s in-program Setup configuration, so it should not be hand-edited. If no user configuration exists <code>htop</code> tries to read the system-wide configuration from <i>/etc/htoprc</i> and as a last resort, falls back to its hard coded defaults. </p>
<p> You may override the location of the configuration file using the $HTOPRC environment variable (so you can have multiple configurations for different machines that share the same home directory, for example).</p>
<h2>MEMORY SIZES</h2>
<p> Memory sizes in <code>htop</code> are displayed in a human-readable form. Sizes are printed in powers of 1024. (e.g., 1023M = 1072693248 Bytes) </p>
<p> The decision to use this convention was made in order to conserve screen space and make memory size representations consistent throughout <code>htop</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1) and <code><a href="/docs/linux/man/5-limits-conf/">limits.conf</a></code>(5).</p>
<h2>AUTHORS</h2>
<p> <code>htop</code> was originally developed by Hisham Muhammad. Nowadays it is maintained by the community at &lt;htop [at] groups.io&gt;. </p>
