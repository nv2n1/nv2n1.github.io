---

title: "pidstat(1)"
name: "pidstat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidstat/"
description: "pidstat – Report statistics for Linux tasks."
---

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
<dt><code>-C </code><i>comm</i></dt>
<dd> Display only tasks whose command name includes the string <i>comm</i>. This string can be a regular expression.</dd>
<dt><code>-d</code></dt>
<dd> Report I/O statistics (kernels 2.6.20 and later only). The following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>kB_rd/s</dt>
<dd> Number of kilobytes the task has caused to be read from disk per second.</dd>
<dt>kB_wr/s</dt>
<dd> Number of kilobytes the task has caused, or shall cause to be written to disk per second.</dd>
<dt>kB_ccwr/s</dt>
<dd> Number of kilobytes whose writing to disk has been cancelled by the task. This may occur when the task truncates some dirty pagecache. In this case, some IO which another task has been accounted for will not be happening.</dd>
<dt>iodelay</dt>
<dd> Block I/O delay of the task being monitored, measured in clock ticks. This metric includes the delays spent waiting for sync block I/O completion and for swapin block I/O completion.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></dt>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</dd>
<dt><code>-e </code><i>program args</i></dt>
<dd> Execute <i>program</i> with given arguments <i>args</i> and monitor it with <code>pidstat</code>. <code>pidstat </code>stops when <i>program </i>terminates.</dd>
<dt><code>-G </code><i>process_name</i></dt>
<dd> Display only processes whose command name includes the string <i>process_name</i>. This string can be a regular expression. If option <code>-t </code>is used together with option <code>-G</code> then the threads belonging to that process are also displayed (even if their command name doesn&#8217;t include the string <i>process_name</i>).</dd>
<dt><code>-H</code></dt>
<dd> Display timestamp in seconds since the epoch.</dd>
<dt><code>-h</code></dt>
<dd> Display all activities horizontally on a single line, with no average statistics at the end of the report. This is intended to make it easier to be parsed by other programs.</dd>
<dt><code>&#8211;human</code></dt>
<dd> Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g. kilobytes, sectors&#8230;) associated with the metrics.</dd>
<dt><code>-I</code></dt>
<dd> In an SMP environment, indicate that tasks CPU usage (as displayed by option <code>-u</code>) should be divided by the total number of processors.</dd>
<dt><code>-l</code></dt>
<dd> Display the process command name and all its arguments.</dd>
<dt><code>-p { </code><i>pid</i><code>[,&#8230;] | SELF | ALL }</code></dt>
<dd> Select tasks (processes) for which statistics are to be reported. <i>pid</i> is the process identification number. The <code>SELF</code> keyword indicates that statistics are to be reported for the <code>pidstat </code>process itself, whereas the <code>ALL</code> keyword indicates that statistics are to be reported for all the tasks managed by the system.</dd>
<dt><code>-R</code></dt>
<dd> Report realtime priority and scheduling policy information. The following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>prio</dt>
<dd> The realtime priority of the task being monitored.</dd>
<dt>policy</dt>
<dd> The scheduling policy of the task being monitored.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt><code>-r</code></dt>
<dd> Report page faults and memory utilization. </dd>
<p> When reporting statistics for individual tasks, the following values may be displayed:</p>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>minflt/s</dt>
<dd> Total number of minor faults the task has made per second, those which have not required loading a memory page from disk.</dd>
<dt>majflt/s</dt>
<dd> Total number of major faults the task has made per second, those which have required loading a memory page from disk.</dd>
<dt>VSZ</dt>
<dd> Virtual Size: The virtual memory usage of entire task in kilobytes.</dd>
<dt>RSS</dt>
<dd> Resident Set Size: The non-swapped physical memory used by the task in kilobytes.</dd>
<dt>%MEM</dt>
<dd> The tasks&#8217;s currently used share of available physical memory.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt>
</dt><dd> When reporting global statistics for tasks and all their children, the following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task which is being monitored together with its children.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task which is being monitored together with its children.</dd>
<dt>PID</dt>
<dd> The identification number of the task which is being monitored together with its children.</dd>
<dt>minflt-nr</dt>
<dd> Total number of minor faults made by the task and all its children, and collected during the interval of time.</dd>
<dt>majflt-nr</dt>
<dd> Total number of major faults made by the task and all its children, and collected during the interval of time.</dd>
<dt>Command</dt>
<dd> The command name of the task which is being monitored together with its children.</dd></dl>
</dl>
<dt><code>-s</code></dt>
<dd> Report stack utilization. The following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>StkSize</dt>
<dd> The amount of memory in kilobytes reserved for the task as stack, but not necessarily used.</dd>
<dt>StkRef</dt>
<dd> The amount of memory in kilobytes used as stack, referenced by the task.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt><code>-T { TASK | CHILD | ALL }</code></dt>
<dd> This option specifies what has to be monitored by the <code>pidstat </code>command. The <code>TASK</code> keyword indicates that statistics are to be reported for individual tasks (this is the default option) whereas the <code>CHILD</code> keyword indicates that statistics are to be globally reported for the selected tasks and all their children. The <code>ALL</code> keyword indicates that statistics are to be reported for individual tasks and globally for the selected tasks and their children. </dd>
<p> Note: Global statistics for tasks and all their children are not available for all options of <code>pidstat.</code> Also these statistics are not necessarily relevant to current time interval: The statistics of a child process are collected only when it finishes or it is killed.</p>
<dt><code>-t</code></dt>
<dd> Also display statistics for threads associated with selected tasks. </dd>
<p> This option adds the following values to the reports:</p>
<dl>
<dl>
<dt>TGID</dt>
<dd> The identification number of the thread group leader.</dd>
<dt>TID</dt>
<dd> The identification number of the thread being monitored.</dd></dl>
</dl>
<dt><code>-U [ </code><i>username </i><code>]</code></dt>
<dd> Display the real user name of the tasks being monitored instead of the UID. If <i>username</i> is specified, then only tasks belonging to the specified user are displayed.</dd>
<dt><code>-u</code></dt>
<dd> Report CPU utilization. </dd>
<p> When reporting statistics for individual tasks, the following values may be displayed:</p>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>%usr</dt>
<dd> Percentage of CPU used by the task while executing at the user level (application), with or without nice priority. Note that this field does NOT include time spent running a virtual processor.</dd>
<dt>%system</dt>
<dd> Percentage of CPU used by the task while executing at the system level (kernel).</dd>
<dt>%guest</dt>
<dd> Percentage of CPU spent by the task in virtual machine (running a virtual processor).</dd>
<dt>%wait</dt>
<dd> Percentage of CPU spent by the task while waiting to run.</dd>
<dt>%CPU</dt>
<dd> Total percentage of CPU time used by the task. In an SMP environment, the task&#8217;s CPU usage will be divided by the total number of CPU&#8217;s if option <code>-I</code> has been entered on the command line.</dd>
<dt>CPU</dt>
<dd> Processor number to which the task is attached.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt>
</dt><dd> When reporting global statistics for tasks and all their children, the following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task which is being monitored together with its children.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task which is being monitored together with its children.</dd>
<dt>PID</dt>
<dd> The identification number of the task which is being monitored together with its children.</dd>
<dt>usr-ms</dt>
<dd> Total number of milliseconds spent by the task and all its children while executing at the user level (application), with or without nice priority, and collected during the interval of time. Note that this field does NOT include time spent running a virtual processor.</dd>
<dt>system-ms</dt>
<dd> Total number of milliseconds spent by the task and all its children while executing at the system level (kernel), and collected during the interval of time.</dd>
<dt>guest-ms</dt>
<dd> Total number of milliseconds spent by the task and all its children in virtual machine (running a virtual processor).</dd>
<dt>Command</dt>
<dd> The command name of the task which is being monitored together with its children.</dd></dl>
</dl>
<dt><code>-V</code></dt>
<dd> Print version number then exit.</dd>
<dt><code>-v</code></dt>
<dd> Report values of some kernel tables. The following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>threads</dt>
<dd> Number of threads associated with current task.</dd>
<dt>fd-nr</dt>
<dd> Number of file descriptors associated with current task.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
<dt><code>-w</code></dt>
<dd> Report task switching activity (kernels 2.6.23 and later only). The following values may be displayed:</dd>
<dl>
<dl>
<dt>UID</dt>
<dd> The real user identification number of the task being monitored.</dd>
<dt>USER</dt>
<dd> The name of the real user owning the task being monitored.</dd>
<dt>PID</dt>
<dd> The identification number of the task being monitored.</dd>
<dt>cswch/s</dt>
<dd> Total number of voluntary context switches the task made per second. A voluntary context switch occurs when a task blocks because it requires a resource that is unavailable.</dd>
<dt>nvcswch/s</dt>
<dd> Total number of non voluntary context switches the task made per second. A involuntary context switch takes place when a task executes for the duration of its time slice and then is forced to relinquish the processor.</dd>
<dt>Command</dt>
<dd> The command name of the task.</dd></dl>
</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>pidstat</code> command takes into account the following environment variables:</p>
<dl>
<dt><code>S_COLORS</code></dt>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <i>never</i>, <i>always </i>or <i>auto</i> (the latter is equivalent to the default settings).<br/>
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</dd>
<dt><code>S_COLORS_SGR</code></dt>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>H=31;1:I=32;22:M=35;1:N=34;1:Z=34;22</code>. Supported capabilities are:</dd>
<dl>
<dl>
<dt><code>H=</code></dt>
<dd> SGR (Select Graphic Rendition) substring for percentage values greater than or equal to 75%.</dd>
<dt><code>I=</code></dt>
<dd> SGR substring for item values like PID, UID or CPU number.</dd>
<dt><code>M=</code></dt>
<dd> SGR substring for percentage values in the range from 50% to 75%.</dd>
<dt><code>N=</code></dt>
<dd> SGR substring for non-zero statistics values and for tasks names.</dd>
<dt><code>Z=</code></dt>
<dd> SGR substring for zero values and for threads names.</dd></dl>
</dl>
<dt><code>S_TIME_FORMAT</code></dt>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>pidstat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp will also be compliant with ISO 8601 format. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>pidstat 2 5</code></dt>
<dd> Display five reports of CPU statistics for every active task in the system at two second intervals.</dd>
<dt><code>pidstat -r -p 1643 2 5</code></dt>
<dd> Display five reports of page faults and memory statistics for PID 1643 at two second intervals.</dd>
<dt><code>pidstat -C fox|bird -r -p ALL</code></dt>
<dd> Display global page faults and memory statistics for all the processes whose command name includes the string &quot;fox&quot; or &quot;bird&quot;.</dd>
<dt><code>pidstat -T CHILD -r 2 5</code></dt>
<dd> Display five reports of page faults statistics at two second intervals for the child processes of all tasks in the system. Only child processes with non-zero statistics values are displayed. </dd>
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
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br/>
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
