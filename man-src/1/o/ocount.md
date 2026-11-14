---
title: "ocount(1)"
name: "ocount"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocount/"
description: "ocount – Event counting tool for Linux"
---

<h2>NAME</h2>
<p> ocount &#8211; Event counting tool for Linux </p>
<h2>SYNOPSIS</h2>
<p> <code>ocount</code> [ <i>options</i> ] [ &#8211;system-wide | &#8211;process-list &lt;pids&gt; | &#8211;thread-list &lt;tids&gt; | &#8211;cpu-list &lt;cpus&gt; [ command [ args ] ] ] </p>
<h2>DESCRIPTION</h2>
<p> <code>ocount</code> is an OProfile tool that can be used to count native hardware events occurring in either a given application, a set of processes or threads, a subset of active system processors, or the entire system. The data collected during a counting session is displayed to stdout by default or, optionally, to a file. </p>
<p> When counting multiple events, the kernel may not be able to count all events simultaneously and, thus, may need to multiplex the counting of the events. If this happens, the &quot;Percent time enabled&quot; column in the <code>ocount</code> output will be less than 100, but counts are scaled up to a 100% estimated value. </p>
<h2>RUN MODES</h2>
<p> One (and only one) of the following <font SIZE="-1"><code>run modes</code></font> must be specified. If you run <code>ocount</code> using a run mode other than <code>command </code><i>[args]</i> , press Ctrl-c to stop <code>ocount</code> when finished counting (e.g., when the monitored process ends). If you background <code>ocount</code> (i.e., with &#8216;&amp;&#8217;) while using one these run modes, you <code>must</code> stop it in a controlled manner so that the data collection process can be shut down cleanly and final results can be displayed. Use <code>kill</code> <code>-SIGINT</code> <code>&lt;ocount-PID&gt;</code> for this purpose.</p>
<dl>
<dt><code>command </code><i>[args]</i></p>
<dd> The <i>command</i> is the application for which to count events. <i>args</i> are the input arguments required by the application. The <i>command</i> and its arguments <code>must</code> be positioned at the end of the command line, after all ocount options. </p>
<dt><code>&#8211;process-list / -p </code><i>pids</i></p>
<dd> Use this option to count events for one or more already-running applications, specified via a comma-separated list ( <i>pids</i> ). Event counts will be collected for all children of the passed process(es) as well. </p>
<dt><code>&#8211;thread-list / -r </code><i>tids</i></p>
<dd> Use this option to count events for one or more already-running threads, specified via a comma-separated list ( <i>tids</i> ). Event counts will <code>not</code> be collected for any children of the passed thread(s). </p>
<dt><code>&#8211;system-wide / -s</code></p>
<dd> This option is for counting events for all processes running on your system. You must have root authority to run ocount in this mode. </p>
<dt><code>&#8211;cpu-list / -C </code><i>cpus</i></p>
<dd> This option is for counting events on a subset of processors on your system. You must have root authority to run ocount in this mode. This is a comma-separated list, where each element in the list may be either a single processor number or a range of processor numbers; for example: &#8216;-C 2,3,4-11,15&#8217;. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>&#8211;events / -e </code><i>event1[,event2[,&#8230;]]</i></p>
<dd> This option is for passing a comma-separated list of event specifications for counting. Each event spec is of the form:<br />
 <i> name[:unitmask[:kernel[:user]]]</i><br />
 <code>Note:</code> Do <code>not</code> include a <i>count</i> value in the event spec, as that parameter is only need when profiling.</dl>
<dl>
<dt>
<dd> You can specify unit mask values using either a numerical value (hex values <i>must</i> begin with &quot;0x&quot;) or a symbolic name (if the <i>name=&lt;um_name&gt;</i> field is shown in the <code>ophelp</code> output). For some named unit masks, the hex value is not unique; thus, OProfile tools enforce specifying such unit masks value by name. If no unit mask is specified, the default unit mask value for the event is used. </p>
<p> Event names for certain processor types include a <i>_GRP&lt;n&gt;</i> suffix. For such cases, the <i>&#8211;events</i> option may be specified with or without the <i>_GRP&lt;n&gt;</i> suffix. </p>
<p> When no event specification is given, the default event for the running processor type will be used for counting. Use <code>ophelp</code> to list the available events for your processor type.</dl>
<dl>
<dt><code>&#8211;separate-thread / -t</code></p>
<dd> This option can be used in conjunction with either the <i>&#8211;process-list</i> or <i>&#8211;thread-list</i> option to display event counts on a per-thread (per-process) basis. Without this option, all counts are aggregated.</dl>
<dl>
<dt>
<dd> <code>NOTE:</code> If new threads are started by the process(es) being monitored after counting begins, the counts for those threads are aggregated with their parent&#8217;s counts.</dl>
<dl>
<dt><code>&#8211;separate-cpu / -c</code></p>
<dd> This option can be used in conjunction with either the <i>&#8211;system-wide</i> or <i>&#8211;cpu-list</i> option to display event counts on a per-cpu basis. Without this option, all counts are aggregated. </p>
<dt><code>&#8211;time-interval / -i </code><i>num_seconds[:num_intervals]</i></p>
<dd> Results collected for each time interval are printed every <i>num_seconds</i> instead of the default of one dump of cumulative event counts at the end of the run. If <i>num_intervals</i> is specified, <code>ocount</code> exits after the specified number of intervals occur. </p>
<dt><code>&#8211;brief-format / -b</code></p>
<dd> Use this option to print results in the following brief format: </p>
<p>&nbsp;<wbr>[optional cpu or thread,]&lt;event_name&gt;,&lt;count&gt;,&lt;percent_time_enabled&gt; </p>
<p>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;int&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>,]&lt;&nbsp;<wbr>&nbsp;<wbr>string&nbsp;<wbr>&nbsp;<wbr>&gt;,&lt;&nbsp;<wbr>u64&nbsp;<wbr>&gt;,&lt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>double&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&gt;</dl>
<dl>
<dt>
<dd> If <i>&#8211;timer-interval</i> is specified, a separate line formatted as </p>
<p>&nbsp;<wbr>timestamp,&lt;num_seconds_since_epoch&gt;<br />
 is printed ahead of each dump of event counts.</dl>
<dl>
<dt><code>&#8211;output-file / -f </code><i>outfile_name</i></p>
<dd> Results are written to <i>outfile_name</i> instead of interactively to the terminal. </p>
<dt><code>&#8211;verbose / -V</code></p>
<dd> Use this option to increase the verbosity of the output. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show ocount version. </p>
<dt><code>&#8211;help / -h</code></p>
<dd> Display brief usage message. </p>
<dt><code>&#8211;usage / -u</code></p>
<dd> Display brief usage message. </p>
</dl>
<h2>EXAMPLE</h2>
<p> $ ocount make </p>
<h2>VERSION</h2>
<p> This man page is current for oprofile-0.9.9. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-operf/">operf</a>(1). </p>
<h2>Index</h2>
