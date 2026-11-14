---
title: "htop(1)"
name: "htop"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htop/"
description: "htop – interactive process viewer"
---

<h2 class="name">NAME</h2>
<p> htop &#8211; interactive process viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>htop</code> [<code>-dCFhpustvH</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>htop</code> is a cross-platform ncurses-based process viewer. </p>
<p> It is similar to <code>top</code>, but allows you to scroll vertically and horizontally, and interact using a pointing device (mouse). You can observe all processes running on the system, along with their command line arguments, as well as view them in a tree format, select multiple processes and acting on them all at once. </p>
<p> Tasks related to processes (killing, renicing) can be done without entering their PIDs. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-d &#8211;delay=DELAY</code></p>
<dd> Delay between updates, in tenths of seconds. If the delay value is less than 1 it is increased to 1, i.e. 1/10 second. If the delay value is greater than 100, it is decreased to 100, i.e. 10 seconds.</p>
<dt><code>-C &#8211;no-color &#8211;no-colour</code></p>
<dd> Start <code>htop</code> in monochrome mode</p>
<dt><code>-F &#8211;filter=FILTER</p>
<dd> Filter processes by command</p>
<dt>-h &#8211;help</p>
<dd> Display a help message and exit</p>
<dt>-p &#8211;pid=PID,PID&#8230;</code></p>
<dd> Show only the given PIDs</p>
<dt><code>-s &#8211;sort-key COLUMN</code></p>
<dd> Sort by this column (use &#8211;sort-key help for a column list). This will force a list view unless you specify -t at the same time.</p>
<dt><code>-u &#8211;user=USERNAME</code></p>
<dd> Show only the processes of a given user</p>
<dt><code>-U &#8211;no-unicode</code></p>
<dd> Do not use unicode but ASCII characters for graph meters</p>
<dt><code>-M &#8211;no-mouse</code></p>
<dd> Disable support of mouse control</p>
<dt><code>-V &#8211;version</p>
<dd> Output version information and exit</p>
<dt>-t &#8211;tree</p>
<dd> Show processes in tree view. This can be used to force a tree view when requesting a sort order with -s.</p>
<dt>-H &#8211;highlight-changes=DELAY</code></p>
<dd> Highlight new and old processes</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> The following commands are supported while in <code>htop</code>:</p>
<dl>
<dt><code>Up, Alt-k</code></p>
<dd> Select (highlight) the previous process in the process list. Scroll the list if necessary.</p>
<dt><code>Down, Alt-j</code></p>
<dd> Select (highlight) the next process in the process list. Scroll the list if necessary.</p>
<dt><code>Left, Alt-h</code></p>
<dd> Scroll the process list left.</p>
<dt><code>Right, Alt-l</code></p>
<dd> Scroll the process list right.</p>
<dt><code>PgUp, PgDn</code></p>
<dd> Scroll the process list up or down one window.</p>
<dt><code>Home</code></p>
<dd> Scroll to the top of the process list and select the first process.</p>
<dt><code>End</code></p>
<dd> Scroll to the bottom of the process list and select the last process.</p>
<dt><code>Ctrl-A, ^</code></p>
<dd> Scroll left to the beginning of the process entry (i.e. beginning of line).</p>
<dt><code>Ctrl-E, $</code></p>
<dd> Scroll right to the end of the process entry (i.e. end of line).</p>
<dt><code>Space</code></p>
<dd> Tag or untag a process. Commands that can operate on multiple processes, like &quot;kill&quot;, will then apply over the list of tagged processes, instead of the currently highlighted one.</p>
<dt><code>c</code></p>
<dd> Tag the current process and its children. Commands that can operate on multiple processes, like &quot;kill&quot;, will then apply over the list of tagged processes, instead of the currently highlighted one.</p>
<dt><code>U</code></p>
<dd> Untag all processes (remove all tags added with the Space or c keys).</p>
<dt><code>s</code></p>
<dd> Trace process system calls: if <a href="/docs/linux/man/1-strace/">strace</a>(1) is installed, pressing this key will attach it to the currently selected process, presenting a live update of system calls issued by the process.</p>
<dt><code>l</code></p>
<dd> Display open files for a process: if <a href="/docs/linux/man/1-lsof/">lsof</a>(1) is installed, pressing this key will display the list of file descriptors opened by the process.</p>
<dt><code>w</code></p>
<dd> Display the command line of the selected process in a separate screen, wrapped onto multiple lines as needed.</p>
<dt><code>x</code></p>
<dd> Display the active file locks of the selected process in a separate screen.</p>
<dt><code>F1, h, ?</code></p>
<dd> Go to the help screen</p>
<dt><code>F2, S</code></p>
<dd> Go to the setup screen, where you can configure the meters displayed at the top of the screen, set various display options, choose among color schemes, and select which columns are displayed, in which order.</p>
<dt><code>F3, /</code></p>
<dd> Incrementally search the command lines of all the displayed processes. The currently selected (highlighted) command will update as you type. While in search mode, pressing F3 will cycle through matching occurrences. Pressing Shift-F3 will cycle backwards. </p>
<p> Alternatively the search can be started by simply typing the command you are looking for, although for the first character normal key bindings take precedence.</p>
<dt><code>F4, \</code></p>
<dd> Incremental process filtering: type in part of a process command line and only processes whose names match will be shown. To cancel filtering, enter the Filter option again and press Esc.</p>
<dt><code>F5, t</code></p>
<dd> Tree view: organize processes by parenthood, and layout the relations between them as a tree. Toggling the key will switch between tree and your previously selected sort view. Selecting a sort view will exit tree view.</p>
<dt><code>F6, &lt;, &gt;</code></p>
<dd> Selects a field for sorting, also accessible through &lt; and &gt;. The current sort field is indicated by a highlight in the header.</p>
<dt><code>F7, ]</code></p>
<dd> Increase the selected process&#8217;s priority (subtract from &#8216;nice&#8217; value). This can only be done by the superuser.</p>
<dt><code>F8, [</code></p>
<dd> Decrease the selected process&#8217;s priority (add to &#8216;nice&#8217; value)</p>
<dt><code>F9, k</code></p>
<dd> &quot;Kill&quot; process: sends a signal which is selected in a menu, to one or a group of processes. If processes were tagged, sends the signal to all tagged processes. If none is tagged, sends to the currently selected process.</p>
<dt><code>F10, q</code></p>
<dd> Quit</p>
<dt><code>I</code></p>
<dd> Invert the sort order: if sort order is increasing, switch to decreasing, and vice-versa.</p>
<dt><code>+, &#8211;</code></p>
<dd> When in tree view mode, expand or collapse subtree. When a subtree is collapsed a &quot;+&quot; sign shows to the left of the process name.</p>
<dt><code>a (on multiprocessor machines)</code></p>
<dd> Set CPU affinity: mark which CPUs a process is allowed to use.</p>
<dt><code>u</code></p>
<dd> Show only processes owned by a specified user.</p>
<dt><code>N</code></p>
<dd> Sort by PID.</p>
<dt><code>M</code></p>
<dd> Sort by memory usage (top compatibility key).</p>
<dt><code>P</code></p>
<dd> Sort by processor usage (top compatibility key).</p>
<dt><code>T</code></p>
<dd> Sort by time (top compatibility key).</p>
<dt><code>F</code></p>
<dd> &quot;Follow&quot; process: if the sort order causes the currently selected process to move in the list, make the selection bar follow it. This is useful for monitoring a process: this way, you can keep a process always visible on screen. When a movement key is used, &quot;follow&quot; loses effect.</p>
<dt><code>K</code></p>
<dd> Hide kernel threads: prevent the threads belonging the kernel to be displayed in the process list. (This is a toggle key.)</p>
<dt><code>H</code></p>
<dd> Hide user threads: on systems that represent them differently than ordinary processes (such as recent NPTL-based systems), this can hide threads from userspace processes in the process list. (This is a toggle key.)</p>
<dt><code>p</code></p>
<dd> Show full paths to running programs, where applicable. (This is a toggle key.)</p>
<dt><code>Z</code></p>
<dd> Pause/resume process updates.</p>
<dt><code>m</code></p>
<dd> Merge exe, comm and cmdline, where applicable. (This is a toggle key.)</p>
<dt><code>Ctrl-L</code></p>
<dd> Refresh: redraw screen and recalculate values.</p>
<dt><code>Numbers</code></p>
<dd> PID search: type in process ID and the selection highlight will be moved to it.</dl>
<h2>COLUMNS</h2>
<p> The following columns can display data about each process. A value of &#8216;-&#8216; in all the rows indicates that a column is unsupported on your system, or currently unimplemented in <code>htop</code>. The names below are the ones used in the &quot;Available Columns&quot; section of the setup screen. If a different name is shown in <code>htop</code>&#8216;s main screen, it is shown below in parenthesis.</p>
<dl>
<dt><code>Command</code></p>
<dd> The full command line of the process (i.e. program name and arguments). If the option &#8216;Merge exe, comm and cmdline in Command&#8217; (toggled by the &#8216;m&#8217; key) is set, and if readable, the executable path (/proc/[pid]/exe) and the command name (/proc/[pid]/comm) are also shown merged with the command line.</p>
<dt><code>Comm</code></p>
<dd> The command name of the process obtained from /proc/[pid]/comm, if readable.</p>
<dt><code>Exe</code></p>
<dd> The abbreviated basename of the executable of the process, obtained from /proc/[pid]/exe, if readable. htop is able to read this file on linux for ALL the processes only if it has the capability CAP_SYS_PTRACE or root privileges.</p>
<dt><code>PID</code></p>
<dd> The process ID.</p>
<dt><code>STATE (S)</code></p>
<dd> The state of the process:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>S</code>&nbsp;for sleeping&nbsp;(idle)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;for running<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>D</code>&nbsp;for disk sleep&nbsp;(uninterruptible)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Z</code>&nbsp;for zombie&nbsp;(waiting for parent to read its exit status)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>T</code>&nbsp;for traced or suspended&nbsp;(e.g by SIGTSTP)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>W</code>&nbsp;for paging</p>
<dt><code>PPID</code></p>
<dd> The parent process ID.</p>
<dt><code>PGRP</code></p>
<dd> The process&#8217;s group ID.</p>
<dt><code>SESSION (SID)</code></p>
<dd> The process&#8217;s session ID.</p>
<dt><code>TTY_NR (TTY)</code></p>
<dd> The controlling terminal of the process.</p>
<dt><code>TPGID</code></p>
<dd> The process ID of the foreground process group of the controlling terminal.</p>
<dt><code>MINFLT</code></p>
<dd> The number of page faults happening in the main memory.</p>
<dt><code>CMINFLT</code></p>
<dd> The number of minor faults for the process&#8217;s waited-for children (see MINFLT above).</p>
<dt><code>MAJFLT</code></p>
<dd> The number of page faults happening out of the main memory.</p>
<dt><code>CMAJFLT</code></p>
<dd> The number of major faults for the process&#8217;s waited-for children (see MAJFLT above).</p>
<dt><code>UTIME (UTIME+)</code></p>
<dd> The user CPU time, which is the amount of time the process has spent executing on the CPU in user mode (i.e. everything but system calls), measured in clock ticks.</p>
<dt><code>STIME (STIME+)</code></p>
<dd> The system CPU time, which is the amount of time the kernel has spent executing system calls on behalf of the process, measured in clock ticks.</p>
<dt><code>CUTIME (CUTIME+)</code></p>
<dd> The children&#8217;s user CPU time, which is the amount of time the process&#8217;s waited-for children have spent executing in user mode (see UTIME above).</p>
<dt><code>CSTIME (CSTIME+)</code></p>
<dd> The children&#8217;s system CPU time, which is the amount of time the kernel has spent executing system calls on behalf of all the process&#8217;s waited-for children (see STIME above).</p>
<dt><code>PRIORITY (PRI)</code></p>
<dd> The kernel&#8217;s internal priority for the process, usually just its nice value plus twenty. Different for real-time processes.</p>
<dt><code>NICE (NI)</code></p>
<dd> The nice value of a process, from 19 (low priority) to -20 (high priority). A high value means the process is being nice, letting others have a higher relative priority. The usual OS permission restrictions for adjusting priority apply.</p>
<dt><code>STARTTIME (START)</code></p>
<dd> The time the process was started.</p>
<dt><code>PROCESSOR (CPU)</code></p>
<dd> The ID of the CPU the process last executed on.</p>
<dt><code>M_VIRT (VIRT)</code></p>
<dd> The size of the virtual memory of the process.</p>
<dt><code>M_RESIDENT (RES)</code></p>
<dd> The resident set size (text + data + stack) of the process (i.e. the size of the process&#8217;s used physical memory).</p>
<dt><code>M_SHARE (SHR)</code></p>
<dd> The size of the process&#8217;s shared pages.</p>
<dt><code>M_TRS (CODE)</code></p>
<dd> The text resident set size of the process (i.e. the size of the process&#8217;s executable instructions).</p>
<dt><code>M_DRS (DATA)</code></p>
<dd> The data resident set size (data + stack) of the process (i.e. the size of anything except the process&#8217;s executable instructions).</p>
<dt><code>M_LRS (LIB)</code></p>
<dd> The library size of the process.</p>
<dt><code>M_DT (DIRTY)</code></p>
<dd> The size of the dirty pages of the process.</p>
<dt><code>M_SWAP (SWAP)</code></p>
<dd> The size of the process&#8217;s swapped pages.</p>
<dt><code>M_PSS (PSS)</code></p>
<dd> The proportional set size, same as M_RESIDENT but each page is divided by the number of processes sharing it.</p>
<dt><code>M_M_PSSWP (PSSWP)</code></p>
<dd> The proportional swap share of this mapping, unlike M_SWAP this does not take into account swapped out page of underlying shmem objects.</p>
<dt><code>ST_UID (UID)</code></p>
<dd> The user ID of the process owner.</p>
<dt><code>PERCENT_CPU (CPU%)</code></p>
<dd> The percentage of the CPU time that the process is currently using.</p>
<dt><code>PERCENT_MEM (MEM%)</code></p>
<dd> The percentage of memory the process is currently using (based on the process&#8217;s resident memory size, see M_RESIDENT above).</p>
<dt><code>USER</code></p>
<dd> The username of the process owner, or the user ID if the name can&#8217;t be determined.</p>
<dt><code>TIME (TIME+)</code></p>
<dd> The time, measured in clock ticks that the process has spent in user and system time (see UTIME, STIME above).</p>
<dt><code>NLWP</code></p>
<dd> The number of threads in the process.</p>
<dt><code>TGID</code></p>
<dd> The thread group ID.</p>
<dt><code>CTID</code></p>
<dd> OpenVZ container ID, a.k.a virtual environment ID.</p>
<dt><code>VPID</code></p>
<dd> OpenVZ process ID.</p>
<dt><code>VXID</code></p>
<dd> VServer process ID.</p>
<dt><code>RCHAR (RD_CHAR)</code></p>
<dd> The number of bytes the process has read.</p>
<dt><code>WCHAR (WR_CHAR)</code></p>
<dd> The number of bytes the process has written.</p>
<dt><code>SYSCR (RD_SYSC)</code></p>
<dd> The number of <a href="/docs/linux/man/2-read/">read</a>(2) syscalls for the process.</p>
<dt><code>SYSCW (WR_SYSC)</code></p>
<dd> The number of <a href="/docs/linux/man/2-write/">write</a>(2) syscalls for the process.</p>
<dt><code>RBYTES (IO_RBYTES)</code></p>
<dd> Bytes of <a href="/docs/linux/man/2-read/">read</a>(2) I/O for the process.</p>
<dt><code>WBYTES (IO_WBYTES)</code></p>
<dd> Bytes of <a href="/docs/linux/man/2-write/">write</a>(2) I/O for the process.</p>
<dt><code>CNCLWB (IO_CANCEL)</code></p>
<dd> Bytes of cancelled <a href="/docs/linux/man/2-write/">write</a>(2) I/O.</p>
<dt><code>IO_READ_RATE (DISK READ)</code></p>
<dd> The I/O rate of <a href="/docs/linux/man/2-read/">read</a>(2) in bytes per second, for the process.</p>
<dt><code>IO_WRITE_RATE (DISK WRITE)</code></p>
<dd> The I/O rate of <a href="/docs/linux/man/2-write/">write</a>(2) in bytes per second, for the process.</p>
<dt><code>IO_RATE (DISK R/W)</code></p>
<dd> The I/O rate, IO_READ_RATE + IO_WRITE_RATE (see above).</p>
<dt><code>CGROUP</code></p>
<dd> Which cgroup the process is in.</p>
<dt><code>OOM</code></p>
<dd> OOM killer score.</p>
<dt><code>CTXT</code></p>
<dd> Incremental sum of voluntary and nonvoluntary context switches.</p>
<dt><code>IO_PRIORITY (IO)</code></p>
<dd> The I/O scheduling class followed by the priority if the class supports it:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>R</code>&nbsp;for Realtime<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>B</code>&nbsp;for Best-effort<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>id</code>&nbsp;for Idle</p>
<dt><code>PERCENT_CPU_DELAY (CPUD%)</code></p>
<dd> The percentage of time spent waiting for a CPU (while runnable). Requires CAP_NET_ADMIN.</p>
<dt><code>PERCENT_IO_DELAY (IOD%)</code></p>
<dd> The percentage of time spent waiting for the completion of synchronous block I/O. Requires CAP_NET_ADMIN.</p>
<dt><code>PERCENT_SWAP_DELAY (SWAPD%)</code></p>
<dd> The percentage of time spent swapping in pages. Requires CAP_NET_ADMIN.</p>
<dt><code>COMM</code></p>
<dd> The command name for the process. Requires Linux kernel 2.6.33 or newer.</p>
<dt><code>EXE</code></p>
<dd> The executable file of the process as reported by the kernel. Requires CAP_SYS_PTRACE and PTRACE_MODE_READ_FSCRED.</p>
<dt><code>All other flags</code></p>
<dd> Currently unsupported (always displays &#8216;-&#8216;).</dl>
<h2>EXTERNAL LIBRARIES</h2>
<p> While <code>htop</code> depends on most of the libraries it uses at build time there are two noteworthy exceptions to this rule. These exceptions both relate to data displayed in meters displayed in the header of <code>htop</code> and were intentionally created as optional runtime dependencies instead. These exceptions are described below:</p>
<dl>
<dt><code>libsystemd</code></p>
<dd> The bindings for libsystemd are used in the SystemD meter to determine the number of active services and the overall system state. Looking for the functions to determine these information at runtime allows for builds to support these meters without forcing the package manager to install these libraries on systems that otherwise don&#8217;t use systemd. </p>
<p> Summary: no build time dependency, optional runtime dependency on <code>libsystemd</code> via dynamic loading, with <code><a href="/docs/linux/man/1-systemctl/">systemctl</a>(1)</code> fallback.</p>
<dt><code>libsensors</code></p>
<dd> The bindings for libsensors are used for the CPU temperature readings in the CPU usage meters if displaying the temperature is enabled through the setup screen. In order for <code>htop</code> to show these temperatures correctly though, a proper configuration of libsensors through its usual configuration files is assumed and that all CPU cores correspond to temperature sensors from the <code>coretemp</code> driver with core 0 corresponding to a sensor labelled &quot;Core 0&quot;. The package temperature may be given as &quot;Package id 0&quot;. If missing it is inferred as the maximum value from the available per-core readings. </p>
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
<h2>Index</h2>
