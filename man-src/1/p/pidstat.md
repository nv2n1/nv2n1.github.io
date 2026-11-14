---
title: "pidstat(1)"
name: "pidstat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidstat/"
description: "pidstat – Report statistics for Linux tasks."
---

<h2 class="name">NAME</h2>
<p> pidstat &#8211; Report statistics for Linux tasks.</p>
<h2>SYNOPSIS</h2>
<p> <code>pidstat [ -d ] [ -H ] [ -h ] [ -I ] [ -l ] [ -R ] [ -r ] [ -s ] [ -t ] [ -U [</code> <i>username </i><code>] ] [ -u ] [ -V ] [ -v ] [ -w ] [ -C </code><i>comm </i><code>] [ -G </code><i>process_name</i> <code>] [ &#8211;dec={ 0 | 1 | 2 } ] [ &#8211;human ] [ -p { </code><i>pid</i><code>[,&#8230;]</code> <code>| SELF | ALL } ] [ -T { TASK | CHILD | ALL } ] [</code> <i>interval </i><code>[ </code><i>count </i><code>] ] [ -e </code><i>program</i> <i>args </i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>pidstat</code> command is used for monitoring individual tasks currently being managed by the Linux kernel. It writes to standard output activities for every task selected with option <code>-p</code> or for every task managed by the Linux kernel if option <code>-p ALL</code> has been used. Not selecting any tasks is equivalent to specifying <code>-p ALL</code> but only active tasks (tasks with non-zero statistics values) will appear in the report. </p>
<p> The <code>pidstat</code> command can also be used for monitoring the child processes of selected tasks. Read about option <code>-T </code>below. </p>
<p> The <i>interval</i> parameter specifies the amount of time in seconds between each report. A value of 0 (or no parameters at all) indicates that tasks statistics are to be reported for the time since system startup (boot). The <i>count </i>parameter can be specified in conjunction with the <i>interval </i>parameter if this one is not set to zero. The value of <i>count </i>determines the number of reports generated at <i>interval </i>seconds apart. If the <i>interval </i>parameter is specified without the <i>count</i> parameter, the <code>pidstat</code> command generates reports continuously. </p>
<p> You can select information about specific task activities using flags. Not specifying any flags selects only CPU activity. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C </code><i>comm</i></p>
<dd> Display only tasks whose command name includes the string <i>comm</i>. This string can be a regular expression.</p>
<dt><code>-d</code></p>
<dd> Report I/O statistics (kernels 2.6.20 and later only). The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>kB_rd/s</p>
<dd> Number of kilobytes the task has caused to be read from disk per second.</p>
<dt>kB_wr/s</p>
<dd> Number of kilobytes the task has caused, or shall cause to be written to disk per second.</p>
<dt>kB_ccwr/s</p>
<dd> Number of kilobytes whose writing to disk has been cancelled by the task. This may occur when the task truncates some dirty pagecache. In this case, some IO which another task has been accounted for will not be happening.</p>
<dt>iodelay</p>
<dd> Block I/O delay of the task being monitored, measured in clock ticks. This metric includes the delays spent waiting for sync block I/O completion and for swapin block I/O completion.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></p>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</p>
<dt><code>-e </code><i>program args</i></p>
<dd> Execute <i>program</i> with given arguments <i>args</i> and monitor it with <code>pidstat</code>. <code>pidstat </code>stops when <i>program </i>terminates.</p>
<dt><code>-G </code><i>process_name</i></p>
<dd> Display only processes whose command name includes the string <i>process_name</i>. This string can be a regular expression. If option <code>-t </code>is used together with option <code>-G</code> then the threads belonging to that process are also displayed (even if their command name doesn&#8217;t include the string <i>process_name</i>).</p>
<dt><code>-H</code></p>
<dd> Display timestamp in seconds since the epoch.</p>
<dt><code>-h</code></p>
<dd> Display all activities horizontally on a single line, with no average statistics at the end of the report. This is intended to make it easier to be parsed by other programs.</p>
<dt><code>&#8211;human</code></p>
<dd> Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g. kilobytes, sectors&#8230;) associated with the metrics.</p>
<dt><code>-I</code></p>
<dd> In an SMP environment, indicate that tasks CPU usage (as displayed by option <code>-u</code>) should be divided by the total number of processors.</p>
<dt><code>-l</code></p>
<dd> Display the process command name and all its arguments.</p>
<dt><code>-p { </code><i>pid</i><code>[,&#8230;] | SELF | ALL }</code></p>
<dd> Select tasks (processes) for which statistics are to be reported. <i>pid</i> is the process identification number. The <code>SELF</code> keyword indicates that statistics are to be reported for the <code>pidstat </code>process itself, whereas the <code>ALL</code> keyword indicates that statistics are to be reported for all the tasks managed by the system.</p>
<dt><code>-R</code></p>
<dd> Report realtime priority and scheduling policy information. The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>prio</p>
<dd> The realtime priority of the task being monitored.</p>
<dt>policy</p>
<dd> The scheduling policy of the task being monitored.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt><code>-r</code></p>
<dd> Report page faults and memory utilization. </p>
<p> When reporting statistics for individual tasks, the following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>minflt/s</p>
<dd> Total number of minor faults the task has made per second, those which have not required loading a memory page from disk.</p>
<dt>majflt/s</p>
<dd> Total number of major faults the task has made per second, those which have required loading a memory page from disk.</p>
<dt>VSZ</p>
<dd> Virtual Size: The virtual memory usage of entire task in kilobytes.</p>
<dt>RSS</p>
<dd> Resident Set Size: The non-swapped physical memory used by the task in kilobytes.</p>
<dt>%MEM</p>
<dd> The tasks&#8217;s currently used share of available physical memory.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt>
<dd> When reporting global statistics for tasks and all their children, the following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task which is being monitored together with its children.</p>
<dt>USER</p>
<dd> The name of the real user owning the task which is being monitored together with its children.</p>
<dt>PID</p>
<dd> The identification number of the task which is being monitored together with its children.</p>
<dt>minflt-nr</p>
<dd> Total number of minor faults made by the task and all its children, and collected during the interval of time.</p>
<dt>majflt-nr</p>
<dd> Total number of major faults made by the task and all its children, and collected during the interval of time.</p>
<dt>Command</p>
<dd> The command name of the task which is being monitored together with its children.</dl>
</dl>
<dt><code>-s</code></p>
<dd> Report stack utilization. The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>StkSize</p>
<dd> The amount of memory in kilobytes reserved for the task as stack, but not necessarily used.</p>
<dt>StkRef</p>
<dd> The amount of memory in kilobytes used as stack, referenced by the task.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt><code>-T { TASK | CHILD | ALL }</code></p>
<dd> This option specifies what has to be monitored by the <code>pidstat </code>command. The <code>TASK</code> keyword indicates that statistics are to be reported for individual tasks (this is the default option) whereas the <code>CHILD</code> keyword indicates that statistics are to be globally reported for the selected tasks and all their children. The <code>ALL</code> keyword indicates that statistics are to be reported for individual tasks and globally for the selected tasks and their children. </p>
<p> Note: Global statistics for tasks and all their children are not available for all options of <code>pidstat.</code> Also these statistics are not necessarily relevant to current time interval: The statistics of a child process are collected only when it finishes or it is killed.</p>
<dt><code>-t</code></p>
<dd> Also display statistics for threads associated with selected tasks. </p>
<p> This option adds the following values to the reports:</p>
<dl>
<dt>
<dd>
<dl>
<dt>TGID</p>
<dd> The identification number of the thread group leader.</p>
<dt>TID</p>
<dd> The identification number of the thread being monitored.</dl>
</dl>
<dt><code>-U [ </code><i>username </i><code>]</code></p>
<dd> Display the real user name of the tasks being monitored instead of the UID. If <i>username</i> is specified, then only tasks belonging to the specified user are displayed.</p>
<dt><code>-u</code></p>
<dd> Report CPU utilization. </p>
<p> When reporting statistics for individual tasks, the following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>%usr</p>
<dd> Percentage of CPU used by the task while executing at the user level (application), with or without nice priority. Note that this field does NOT include time spent running a virtual processor.</p>
<dt>%system</p>
<dd> Percentage of CPU used by the task while executing at the system level (kernel).</p>
<dt>%guest</p>
<dd> Percentage of CPU spent by the task in virtual machine (running a virtual processor).</p>
<dt>%wait</p>
<dd> Percentage of CPU spent by the task while waiting to run.</p>
<dt>%CPU</p>
<dd> Total percentage of CPU time used by the task. In an SMP environment, the task&#8217;s CPU usage will be divided by the total number of CPU&#8217;s if option <code>-I</code> has been entered on the command line.</p>
<dt>CPU</p>
<dd> Processor number to which the task is attached.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt>
<dd> When reporting global statistics for tasks and all their children, the following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task which is being monitored together with its children.</p>
<dt>USER</p>
<dd> The name of the real user owning the task which is being monitored together with its children.</p>
<dt>PID</p>
<dd> The identification number of the task which is being monitored together with its children.</p>
<dt>usr-ms</p>
<dd> Total number of milliseconds spent by the task and all its children while executing at the user level (application), with or without nice priority, and collected during the interval of time. Note that this field does NOT include time spent running a virtual processor.</p>
<dt>system-ms</p>
<dd> Total number of milliseconds spent by the task and all its children while executing at the system level (kernel), and collected during the interval of time.</p>
<dt>guest-ms</p>
<dd> Total number of milliseconds spent by the task and all its children in virtual machine (running a virtual processor).</p>
<dt>Command</p>
<dd> The command name of the task which is being monitored together with its children.</dl>
</dl>
<dt><code>-V</code></p>
<dd> Print version number then exit.</p>
<dt><code>-v</code></p>
<dd> Report values of some kernel tables. The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>threads</p>
<dd> Number of threads associated with current task.</p>
<dt>fd-nr</p>
<dd> Number of file descriptors associated with current task.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
<dt><code>-w</code></p>
<dd> Report task switching activity (kernels 2.6.23 and later only). The following values may be displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UID</p>
<dd> The real user identification number of the task being monitored.</p>
<dt>USER</p>
<dd> The name of the real user owning the task being monitored.</p>
<dt>PID</p>
<dd> The identification number of the task being monitored.</p>
<dt>cswch/s</p>
<dd> Total number of voluntary context switches the task made per second. A voluntary context switch occurs when a task blocks because it requires a resource that is unavailable.</p>
<dt>nvcswch/s</p>
<dd> Total number of non voluntary context switches the task made per second. A involuntary context switch takes place when a task executes for the duration of its time slice and then is forced to relinquish the processor.</p>
<dt>Command</p>
<dd> The command name of the task.</dl>
</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>pidstat</code> command takes into account the following environment variables:</p>
<dl>
<dt><code>S_COLORS</code></p>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <i>never</i>, <i>always </i>or <i>auto</i> (the latter is equivalent to the default settings).<br />
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</p>
<dt><code>S_COLORS_SGR</code></p>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>H=31;1:I=32;22:M=35;1:N=34;1:Z=34;22</code>. Supported capabilities are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>H=</code></p>
<dd> SGR (Select Graphic Rendition) substring for percentage values greater than or equal to 75%.</p>
<dt><code>I=</code></p>
<dd> SGR substring for item values like PID, UID or CPU number.</p>
<dt><code>M=</code></p>
<dd> SGR substring for percentage values in the range from 50% to 75%.</p>
<dt><code>N=</code></p>
<dd> SGR substring for non-zero statistics values and for tasks names.</p>
<dt><code>Z=</code></p>
<dd> SGR substring for zero values and for threads names.</dl>
</dl>
<dt><code>S_TIME_FORMAT</code></p>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>pidstat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp will also be compliant with ISO 8601 format. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>pidstat 2 5</code></p>
<dd> Display five reports of CPU statistics for every active task in the system at two second intervals.</p>
<dt><code>pidstat -r -p 1643 2 5</code></p>
<dd> Display five reports of page faults and memory statistics for PID 1643 at two second intervals.</p>
<dt><code>pidstat -C fox|bird -r -p ALL</code></p>
<dd> Display global page faults and memory statistics for all the processes whose command name includes the string &quot;fox&quot; or &quot;bird&quot;.</p>
<dt><code>pidstat -T CHILD -r 2 5</code></p>
<dd> Display five reports of page faults statistics at two second intervals for the child processes of all tasks in the system. Only child processes with non-zero statistics values are displayed. </p>
</dl>
<h2>BUGS</h2>
<p> <i>/proc </i>filesystem must be mounted for the <code>pidstat </code>command to work. </p>
<p> Although <code>pidstat</code> speaks of kilobytes (kB), megabytes (MB)&#8230;, it actually uses kibibytes (kiB), mebibytes (MiB)&#8230; A kibibyte is equal to 1024 bytes, and a mebibyte is equal to 1024 kibibytes. </p>
<h2>FILES</h2>
<p> <i>/proc </i>contains various files with system statistics. </p>
<h2>AUTHOR</h2>
<p> Sebastien Godard (sysstat &lt;at&gt; orange.fr) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-mpstat/">mpstat</a></code>(1), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8) </p>
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
