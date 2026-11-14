---
title: "qacct(1)"
name: "qacct"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qacct/"
description: "qacct – report and account for xxQS_NAMExx usage"
---

<h2 class="name">NAME</h2>
<p> qacct &#8211; report and account for xxQS_NAMExx usage </p>
<h2>SYNOPSIS</h2>
<p> <code>qacct</code> [<code>-ar</code> [<i>ar_id</i>]] [<code>-A</code> <i>Account</i>] [<code>-b</code> <i>BeginTime</i>] [<code>-d</code> <i>Days</i>] [<code>-e</code> <i>EndTime</i>] [<code>-g</code> [<i>GroupId</i>|<i>GroupName</i>]] [<code>-h</code> [<i>HostName</i>]] [<code>-help</code>] [<code>-j</code> [<i>job_id</i>|<i>job_name</i>|<i>pattern</i>]] [<code>-l</code> <i>attr</i>=<i>val</i>,&#8230;] [<code>-m</code>] [<code>-o</code> [<i>Owner</i>]] [<code>-u</code> [<i>Owner</i>]] [<code>-pe</code> [<i>PEname</i>]] [<code>-q</code> [<i>wc_queue</i>]] [<code>-slots</code> [<i>SlotNumber</i>]] [<code>-t</code> <i>task_id_range_list</i>] [<code>-P</code> [<i>Project</i>]] [<code>-D</code> [<i>Department</i>]] [<code>-f</code> <i>AcctFileName</i>] [<code>-E</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>qacct</i> utility scans the accounting data file (see and produces a summary of information for wall-clock time, CPU time, and system time for the categories of host name, queue name, group name, owner name, job name, job ID, and for the queues meeting the resource requirements as specified with the <code>-l</code> switch. Combinations of each category are permitted. Alternatively, all or specific jobs can be listed with the <code>-j</code> switch. For example the search criteria could include summarizing for a queue and an owner, but not for two queues in the same request. </p>
<p> Note that results including parallel jobs depend on the value of <code>accounting_summary</code> in the parallel environment definition (see If it is false, there is an accounting record for slave tasks as well as master tasks so that, for example, there is a contribution to CPU time from each task. Note that the slot count reported for each task is the total for the job, not that allocated to the slave.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ar</code> [<i>ar_id</i>]</p>
<dd> The ID of the advance reservation for which usage is summarized. If <i>ar_id</i> is not given, accounting data are listed for each advance reservation separately.</p>
<dt><code>-A </code><i>Account</i></p>
<dd> The account for jobs to be summarized.</p>
<dt><code>-b</code> <i>BeginTime</i></p>
<dd> The earliest start time for jobs to be summarized, in the format [[<i>CC</i>]<i>YY</i>]<i>MMDDhhmm</i>[.<i>SS</i>]. See also the <code>-d</code> option. If <i>CC</i> is not specified, a <i>YY</i> of &lt;70 means 20<i>YY</i>. If the <code>-E</code> option is specified, this specifies the earliest job end time instead.</p>
<dt><code>-d</code> <i>Days</i></p>
<dd> The number of days for which to summarize and print accounting information. If used together with the <code>-b </code><i>BeginTime</i> option (see above), jobs started (or, with the <code>-E</code> option, finished) within <i>BeginTime</i> to <i>BeginTime</i>+<i>Days</i> are counted. If used together with <code>-e</code> <i>EndTime</i> (see below) option, selection is from <i>EndTime</i>&#8211;<i>Days</i>. With neither, consider the last <i>Days</i>.</p>
<dt><code>-e</code> <i>EndTime</i></p>
<dd> The latest start time for jobs to be summarized, in the format [[<i>CC</i>]<i>YY</i>]<i>MMDDhhmm</i>[.<i>SS</i>]. See also the <code>-d</code> option. If <i>CC</i> is not specified, a <i>YY</i> of &lt;70 means 20<i>YY</i>. If the <code>-E</code> option is specified, this specifies the latest job end time instead.</p>
<dt>[<code>-f</code> <i>AcctFileName</i>]</p>
<dd> The accounting file to be used. &quot;-&quot; means use standard input. If omitted, the system default accounting file is processed.</p>
<dt><code>-g</code> [<i>GroupId</i>|<i>GroupName</i>]</p>
<dd> The numeric system group id or the group alphanumeric name of the job owners to be included in the accounting. If <i>GroupId</i>/<i>GroupName</i> is omitted, all groups are accounted.</p>
<dt><code>-h</code> [<i>HostName</i>]</p>
<dd> The case-insensitive name of the host upon which accounting information is requested. If the name is omitted, totals for each host are listed separately.</p>
<dt><code>-help</code></p>
<dd> Display help information for the <i>qacct</i> command.</p>
<dt><code>-j</code> [<i>job_id</i>|<i>job_name</i>|<i>pattern</i>]</p>
<dd> The name, an expression for matching names, or ID of the job during execution for which accounting information is printed. If neither a name nor an ID is given, all jobs are listed.<br />
 This option changes the output format of <i>qacct</i>. If activated, CPU times are no longer accumulated but &quot;raw&quot; per-job accounting information is printed in a formatted form instead. CPU time (seconds), integrated memory usage (GB seconds), total i/o (bytes), i/o wait time (seconds), and maximum virtual memory (bytes).</p>
<dt><code>-l </code><i>attr</i>=<i>val</i>,&#8230;</p>
<dd> A resource requirement specification which must be met by the queues in which the jobs being accounted were executing. The resource request is very similar to the one described in</p>
<dt><code>-m</code></p>
<dd> Ignore slave tasks of parallel jobs. Only relevant when when <code>accounting_summary</code> is false, and probably only useful with <code>-j</code> to prune the output.</p>
<dt><code>-o</code> [<i>Owner</i>] | <code>-u</code> [<i>Owner</i>]</p>
<dd> The name of the owner of the jobs for which accounting statistics are assembled. If the optional <i>Owner</i> argument is omitted, a listing of the accounting statistics of all job owners present in the accounting file is produced. <code>-u</code> and <code>-o</code> are synonyms.</p>
<dt><code>-pe</code> [<i>PEname</i>]</p>
<dd> The name of the parallel environment for which usage is summarized. If <i>PEname</i> is not given, accounting data are listed for each parallel environment separately.</p>
<dt><code>-q</code> [<i>wc_queue_name</i>]</p>
<dd> An expression for queues for which usage is summarized. All queue instances matching the expression will be listed. If no expression is specified, a cluster queue summary will be given.</p>
<dt><code>-slots</code> [<i>SlotNumber</i>]</p>
<dd> The number of queue slots for which usage is summarized. If <i>SlotNumber</i> is not given, accounting data are listed for each number of queue slots separately.</p>
<dt><code>-t </code><i>task_id_range_list</i></p>
<dd> Only available together with the <code>-j</code> option described above. </p>
<p> The <code>-t</code> switch specifies the array job task range, for which accounting information should be printed. Syntax and semantics of <i>task_id_range_list</i> are identical to that one described under the <code>-t</code> option to Please see there also for further information on array jobs.</p>
<dt><code>-P</code> [<i>Project</i>]</p>
<dd> The name of the project for which usage is summarized. If <i>Project</i> is not given, accounting data are listed for each relevant project separately.</p>
<dt><code>-D</code> [<i>Department</i>]</p>
<dd> The name of the department for which usage is summarized. If <i>Department</i> is not given, accounting data are listed for each relevant department separately.</p>
<dt><code>-E</code></p>
<dd> When selecting times with <code>-b</code>, <code>-e</code>, <code>-d</code>, use the job end time rather than the start time to select. This may be useful because the accounting record is written at the job end.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qacct</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_EXECD_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_execd&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/accounting</i>
                          xxQS_NAMExx default accounting file
<i>&lt;xxqs_nam_sexx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
