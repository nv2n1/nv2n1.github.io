---
title: "tiptop(1)"
name: "tiptop"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tiptop/"
description: "tiptop – display hardware performance counters for Linux tasks"
---

<h2 class="name">NAME</h2>
<p> tiptop &#8211; display hardware performance counters for Linux tasks</p>
<h2>SYNOPSIS</h2>
<p> <code>tiptop</code> [OPTION] </p>
<p> <code>tiptop</code> [OPTION] &#8212; command (EXPERIMENTAL) </p>
<p> <code>ptiptop</code> PATTERN [OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> The <code>tiptop</code> program provides a dynamic real-time view of the tasks running in the system. tiptop is very similar to top (1), but the information displayed comes from hardware counters. </p>
<p> tiptop has two running <i>modes</i>: live-mode and batch-mode. In both modes, the system is periodically queried for the values of hardware counters, and various ratios are printed for each task. In live-mode, the display is regularly updated with new values at constant time intervals. In batch-mode, the same information is emitted to stdout. Batch-mode is appropriate for saving to a file or for further processing. No interaction is possible in batch-mode. </p>
<p> Unless tiptop is run by root, or the executable is setuid-root, a user can only monitor the tasks it owns. </p>
<p> The results produced by tiptop are organized in <i>screens</i>. A screen consists in rows representing tasks, and columns reporting various values and ratios collected from hardware counters. Many screens can be defined. Only one screen is displayed at a time. The default screen (number 0) reports target independent values as defined in the file /usr/include/linux/event_counter.h. Other screens may rely on target-dependent counters. </p>
<p> When an expression would result in a division by zero, a &#8216;-&#8216; sign is printed. When a counter involved in an expression could not be read, a &#8216;?&#8217; sign is printed. </p>
<p> If &#8212; appears in the command line, tiptop treats the rest of the line as a command. A new process is forked, and hardware counters are attached just before execvp is called. This makes it possible to trace an application from the first instruction. Only the child is traced, and idle-mode is enabled (in live mode, this can be overridden by hitting keys &#8216;p&#8217; and &#8216;i&#8217;). This is commonly used in combination with sticky mode to track a command from start to finish. This is experimental! </p>
<p> ptiptop is simply a shortcut for tiptop -p. </p>
<p> tiptop requires Linux 2.6.31+. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> Command line options with a parameter override values specified in the configuration file. Toggles set the value or invert the value read in the configuration file (if any). </p>
<dl>
<dt>&#8211;<code>b</code></p>
<dd> Start tiptop in batch-mode. Output is sent to stdout, and no interactive command is accepted. tiptop will run forever, or until the number of iterations specified by <code>-n</code>. </p>
<dt>&#8211;<code>c</code></p>
<dd> display the command line of the task instead of its name. (toggle) </p>
<dt>&#8212;<code>cpu-min</code> VALUE</p>
<dd> %CPU activity threshold. Below this value, a task is considered<br />
&nbsp;<wbr>idle and is not reported&nbsp;<wbr>(unless idle-mode is on, see flag -i). </p>
<dt>&#8211;<code>d</code> VALUE</p>
<dd> Specify the delay between refreshes. VALUE can be fractional. It must be larger than 0.01. </p>
<dt>&#8211;<code>E</code> FILENAME</p>
<dd> Specify file where errors are logged. By default errors are logged to stderr in batch-mode, and a temporary file in live-mode. </p>
<dt>&#8212;<code>epoch</code></p>
<dd> Print the Epoch at each refresh. In batch-mode, it is printed at the beginning of each row. In live-mode, it is at the bottom of the display. (toggle) </p>
<dt>&#8211;<code>h &#8211;help</code></p>
<dd> Print a brief help message and exit. </p>
<dt>&#8211;<code>H</code></p>
<dd> Show threads. (toggle) </p>
<dt>&#8211;<code>i</code></p>
<dd> Show idle tasks. (toggle) </p>
<dt>&#8211;<code>K &#8211;kernel</code></p>
<dd> Include kernel activity in the reported values. This is only possible is the user is root, the tiptop executable is setuid root, or the paranoia level is low enough. (toggle) </p>
<pre>
See file /proc/sys/kernel/perf_event_paranoid
(perf_counter_paranoid on Linux 2.6.31).
</pre>
<dt>&#8212;<code>list-screens</code></p>
<dd> List available screens and exit. </p>
<dt>&#8211;<code>n</code> VALUE</p>
<dd> Automatically exit after VALUE iterations. </p>
<dt>&#8212;<code>no-collect</code></p>
<dd> By default, when the maximum number of open files is reached, and new processes appear, tiptop searches for idle processes and closes the files in order to make room for the new ones. This flag disables this behavior: in case of file shortage, new processes will not get more chances than older ones. </p>
<dt>&#8211;<code>o</code> FILENAME</p>
<dd> Specify the filename for the output of batch mode. </p>
<dt>&#8212;<code>only-conf</code></p>
<dd> Only screens defined in configuration file displayed (no default). </p>
<dt>&#8211;<code>p &#8211;pid</code> VALUE</p>
<dd> Filters processes according to VALUE. VALUE can be either the numeric value PID, or a string. In case of a string, all tasks whose names or command lines (depending on the display, see -c) contain VALUE are reported. </p>
<dt>&#8211;<code>S</code> VALUE</p>
<dd> Start tiptop with screen number VALUE if VALUE is an integer. Otherwise looks for the first screen whose name contains VALUE. </p>
<dt>&#8212;<code>sticky</code></p>
<dd> Start in sticky mode: tasks stay in the list after they die. In live-mode, they appear in a different color (when supported). In batch-mode, the word DEAD is appended. (toggle) </p>
<dt>&#8212;<code>timestamp</code></p>
<dd> Print a timestamp at the beginning of each row. The timestamp is the number of refreshes so far. In batch-mode, it is printed at the beginning of each row. In live-mode, it is at the bottom of the display. (toggle) </p>
<dt>&#8211;<code>u</code> USER</p>
<dd> Only show tasks owned by USER. USER can be either a login name, or the numeric value UID. </p>
<dt>&#8211;<code>U</code></p>
<dd> Show the owner of each task. (toggle) </p>
<dt>&#8211;<code>v</code></p>
<dd> Display build information and exit. </p>
<dt>&#8212;<code>version</code></p>
<dd> Display version information and disclaimer and exit. </p>
<dt>&#8211;<code>w</code> VALUE</p>
<dd> Watch the task specified by VALUE. VALUE can be either the numeric value PID, or a string. In case of a string, all tasks whose names or command lines (depending on the display, see -c) contain VALUE are reported. In live-mode, watched tasks are shown in a different color (when supported). In batch-mode, an ASCII arrow points to the watched tasks. </p>
<dt>&#8211;<code>W</code> PATH</p>
<dd> Directory where the configuration file is located. </p>
</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> In live-mode, tiptop accepts single-key commands. </p>
<dl>
<dt><code>LEFT</code>, <code>RIGHT</code></p>
<dd> Rotate through available screens. </p>
<dt><code>&lt;</code>, <code>&gt;</code></p>
<dd> Change the reference column for sorting to the left or to the right. </p>
<dt><code>c</code></p>
<dd> Toggle between showing task names and command lines. </p>
<dt><code>d</code></p>
<dd> Change the refresh interval. The new value is queried. Fractional values larger than 0.01 are accepted. </p>
<dt><code>e</code></p>
<dd> Display the errors encoutered so far. Scroll with UP, DOWN, PAGE_UP, PAGE_DOWN, HOME and END. </p>
<dt><code>h</code></p>
<dd> Display a brief description of the screen and each column. </p>
<dt><code>H</code></p>
<dd> Toggle between showing individual threads and accumulating values per process. </p>
<dt><code>i</code></p>
<dd> Toggle between showing only active tasks and showing also idle tasks. </p>
<dt><code>K</code></p>
<dd> Toggle between showing kernel activity and only user activity. Kernel mode is only available to root. Switching to and from kernel mode resets all counters. </p>
<dt><code>k</code></p>
<dd> Kill a process. The user is asked for the PID, and the signal to send. </p>
<dt><code>p</code></p>
<dd> Filter tasks by name or PID. The user is asked for a PID or string. In case a string is entered, only the tasks whose name or command line contain the string are displayed. Changing the filter resets all counters. </p>
<dt><code>q</code></p>
<dd> Quit. </p>
<dt><code>R</code></p>
<dd> Change sorting order: ascending or descending. </p>
<dt><code>S</code></p>
<dd> Toggle sticky mode. </p>
<dt><code>s</code></p>
<dd> Same as d. </p>
<dt><code>u</code></p>
<dd> Filter tasks by user. The user name or PID is queried. Note that, unless tiptop is run by root or setuid root, tasks owned by somebody else cannot be monitored. Changing the filter resets all counters. </p>
<dt><code>U</code></p>
<dd> Toggle displaying each task&#8217;s owner. </p>
<dt><code>w</code></p>
<dd> Used to track a particular task. The user is asked for a PID or string. In case a string is entered, all tasks whose name or command line contain the string are highlighted. </p>
<dt><code>W</code></p>
<dd> Writes a configuration file for the current state in the current directory. </p>
</dl>
<h2>FILES</h2>
<p> During startup, <code>tiptop</code> attempts to read a configuration file. The file must be named <code>.tiptoprc</code>. This file is first searched in the current directory, then in the directory defined by the environment variable <code>TIPTOP</code> if it exists, finally in the user&#8217;s home. </p>
<h3>Syntax</h3>
<p> The file is structured in XML. The syntax is as follows. </p>
<dl>
<dt>Root of tree</p>
<dd> The root of the xml tree is tiptop. &lt;tiptop&gt; &#8230; &lt;/tiptop&gt; </p>
<dt>Options</p>
<dd> Options can be specified on an &lt;options&gt; block. </p>
<p> &lt;options&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;option name=&quot;option1&quot;&nbsp;<wbr>value=&quot;value_option1&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;option name=&quot;option2&quot;&nbsp;<wbr>value=&quot;value_option2&quot;/&gt;<br />
&nbsp;<wbr>&#8230; &lt;/options&gt; </p>
<p> Recognized options listed below, with their corresponding command line option. </p>
<p> cpu_threshold (&#8211;cpu-min), delay (-d), idle (-i), max_iter (-n), show_cmdline (-c), show_epoch (&#8211;epoch), show_kernel (-K), show_timestamp (&#8211;timestamp), show_threads (-H), show_user (-U), watch_name (-w), sticky (&#8211;sticky), watch_uid (-w) </p>
<dt>Screens</p>
<dd> Screens are defined inside a &lt;screen&gt; block. A screen is made of counters and columns. A screen has a name and an optional description. </p>
<p> &lt;screen name=&quot;my_screen&quot; desc=&quot;what this screen is about&quot;&gt;<br />
&nbsp;<wbr>&#8230;. &lt;/screen&gt; </p>
<p> Counters must provide an alias (used for further reference) and a configuration. The configuration is either a predefined value, or the actual value that must be provided to the perf_even_open system call (typically found in vendor architecture manuals). </p>
<p> Predefined values are: CPU_CYCLES, INSTRUCTIONS, CACHE_REFERENCES, CACHE_MISSES, BRANCH_INSTRUCTIONS, BRANCH_MISSES, and BUS_CYCLES. </p>
<pre>
&lt;counter alias=&quot;instr&quot; config=&quot;INSTRUCTIONS&quot; /&gt;
</pre>
<p> For non-predefined configs, a type must be provided. Currently, only RAW and HW_CACHE are supported. </p>
<p> Optionally, a counter may be restricted to a specific architecture (such as &quot;x86&quot;), and a model. The definition of the model is architecture-dependent. For x86, it is defined as DisplayFamily_DisplayModel as computed by the instruction CPUID. A counter for issued micro-ops on Sandy Bridge may look like the following: </p>
<pre>
&lt;counter alias=&quot;uops_issued&quot; config=&quot;0x010e&quot;
         type=&quot;RAW&quot; arch=&quot;x86&quot; model=&quot;06_2A&quot; /&gt;
</pre>
<p> For the x86 architecture, a single counter can be valid for several models. </p>
<pre>
&lt;counter alias=&quot;uOP&quot; config=&quot;0x1c2&quot; type=&quot;RAW&quot;
         arch=&quot;x86&quot; model=&quot;06_1A;06_1E;06_1F;06_2E&quot; /&gt;
</pre>
<p> When the type is HW_CACHE, the config is specified by shifting and ORing predefined values. The 8 least significant bits represent the cache level (possible values L1D, L1I, LL, DTLB, ITLB, BPU). The next 8 bits represent the type of access (OP_READ, OP_WRITE, OP_PREFETCH). The last 8 bits represent are one of RESULT_ACCESS or RESULT_MISS. </p>
<p> Note that &quot;shift left&quot; is expressed as shl (the usual &lt;&lt; does not fit well in xml). </p>
<pre>
&lt;counter alias=&quot;L1Rmiss&quot; type=&quot;HW_CACHE&quot;
         config=&quot;L1D | (OP_READ shl 8) | (RESULT_MISS shl 16)&quot; /&gt;
</pre>
<p> See also /usr/include/linux/perf_events.h for more on config and type. </p>
<p> A column defines its header, the printf-like format for values, and an expression. Expressions evaluate as double precision. A description is optional. </p>
<pre>
&lt;counter alias=&quot;instr&quot; config=&quot;INSTRUCTIONS&quot; /&gt;
&lt;counter alias=&quot;cycle&quot; config=&quot;CPU_CYCLES&quot; /&gt;
&lt;column header=&quot; IPC&quot; format=&quot;%4.2f&quot;
        desc=&quot;Total instructions per cycle&quot;
        expr=&quot;instr/cycle&quot;/&gt;
&lt;column header=&quot; ipc&quot; format=&quot;%4.2f&quot;
        desc=&quot;Total instructions per cycle&quot;
        expr=&quot;instr/cycle&quot; /&gt;
</pre>
<p> The syntax of expressions supports basic arithmetic (+ &#8211; * / parentheses and constants). The special notation &quot;delta(counter)&quot; evaluates as the variation of the counter between refreshes. Expressions can also refer to predefined variables such as CPU_TOT (CPU usage), CPU_SYS (system CPU usage), CPU_USER (user CPU usage), PROC_ID (processor where the process was last seen). </p>
<pre>
&lt;column header=&quot; ipc&quot; format=&quot;%4.2f&quot;
      desc=&quot;Average IPC over last period&quot;
      expr=&quot;delta(instr) / delta(cycle)&quot; /&gt;
</pre>
<dt>Sample config file</p>
<dd>
<pre>
&lt;tiptop&gt;
  &lt;options&gt;
    &lt;option name=&quot;delay&quot; value=&quot;2.0&quot; /&gt;
    &lt;option name=&quot;stick&quot; value=&quot;1&quot; /&gt;
  &lt;/options&gt;
  &lt;screen name=&quot;example&quot; desc=&quot;Sample config file&quot;&gt;
    &lt;counter alias=&quot;cycle&quot; config=&quot;CPU_CYCLES&quot;  /&gt;
    &lt;counter alias=&quot;instr&quot; config=&quot;INSTRUCTIONS&quot; /&gt;
    &lt;counter alias=&quot;miss&quot; config=&quot;CACHE_MISSES&quot; /&gt;
    &lt;counter alias=&quot;br_miss&quot; config=&quot;BRANCH_MISSES&quot; /&gt;
    &lt;!-- Sandy Bridge only --&gt;
    &lt;counter alias=&quot;uops_issued&quot; config=&quot;0x010e&quot;
             type=&quot;RAW&quot; arch=&quot;x86&quot; model=&quot;06_2A&quot; /&gt;
    &lt;column header=&quot; %CPU&quot; format=&quot;%5.1f&quot;
            desc=&quot;CPU usage&quot; expr=&quot;CPU_TOT&quot; /&gt;
    &lt;column header=&quot;   P&quot; format=&quot;  %2.0f&quot;
            desc=&quot;Processor where last seen&quot; expr=&quot;PROC_ID&quot; /&gt;
    &lt;column header=&quot;  Mcycle&quot; format=&quot;%8.2f&quot;
            desc=&quot;Cycles (millions)&quot;
            expr=&quot;delta(cycle) / 1e6&quot; /&gt;
    &lt;column header=&quot;  Minstr&quot; format=&quot;%8.2f&quot;
            desc=&quot;Instructions (millions)&quot;
            expr=&quot;delta(instr) / 1e6&quot; /&gt;
    &lt;column header=&quot; IPC&quot; format=&quot;%4.2f&quot;
            desc=&quot;Executed instructions per cycle&quot;
            expr=&quot;delta(instr) / delta(cycle)&quot; /&gt;
    &lt;column header=&quot; %MISS&quot; format=&quot;%6.2f&quot;
            desc=&quot;Cache miss per instructions (in %)&quot;
            expr=&quot;100 * delta(miss) / delta(instr)&quot; /&gt;
    &lt;column header=&quot; %BMIS&quot; format=&quot;%6.2f&quot;
            desc=&quot;Branch misprediction per instruction (in %)&quot;
            expr=&quot;100 * delta(br_miss) / delta(instr)&quot; /&gt;
    &lt;column header=&quot;uops/inst&quot; format=&quot;     %4.1f&quot;
            desc=&quot;Number of issued uops per instruction&quot;
            expr=&quot;delta(uops_issued) / delta(instr)&quot; /&gt;
  &lt;/screen&gt;
&lt;/tiptop&gt;
</pre>
</dl>
<h2>CAVEATS</h2>
<p> tiptop does not seem to work within a virtualized environment. </p>
<p> Attaching counters to processes may fail for various reasons, such as asking for more than available in hardware (tiptop does not implement sampling), or reaching the maximum number of open files. In these cases, you may consider filtering the processes (see flags -u, -p). </p>
<p> To mitigate the limitation of the maximum number of open files, tiptop tries to close the events attached to idle processes. If this is a problem, see the flag &#8211;no-collect. </p>
<h2>BUGS</h2>
<p> Send bug reports to:<br />
Erven Rohou&nbsp;<wbr>&lt;erven.rohou [at] inria.fr&gt; </p>
<h2>AUTHOR</h2>
<p> Written by Erven Rohou. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) </p>
<pre>
/usr/include/linux/perf_counter.h (Linux 2.6.31)
/usr/include/linux/event_counter.h (Linux 2.6.32+)
</pre>
<h2>Index</h2>
