---
title: "pbs_sched_basl(8)"
name: "pbs_sched_basl"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbs_sched_basl/"
description: "pbs_sched_basl – pbs BASL scheduler"
---

<p>pbs_sched_basl &#8211; pbs BASL scheduler</p>
<h2>Synopsis</h2>
<p>pbs_sched&nbsp;<wbr>[-d home] [-L logfile] [-p print_file] [-a alarm] [-S port] [-c configfile]</p>
<h2>Description</h2>
<p>The <code>pbs_sched</code> command starts the operation of a batch scheduler on the local host. It runs in conjunction with the PBS server. It queries the server about the state of PBS and communicates with <code>pbs_mom</code> to get information about the status of running jobs, memory available etc. It then makes decisions as to what jobs to run. </p>
<p> Typically, this command will be in a local boot file such as <i>/etc/rc.local .</i> </p>
<p> pbs_sched must be executed with root permission.</p>
<h2>Options</h2>
<dl>
<dt>-d home</p>
<dd>Specifies the name of the PBS home directory, PBS_HOME. If not specified, the value of $PBS_SERVER_HOME as defined at compile time is used. Also see the -L option.</p>
<dt>-L logfile</p>
<dd>Specifies an absolute path name of the file to use as the log file. If not specified, the scheduler will open a file named for the current date in the PBS_HOME/sched_logs directory. See the -d option.</p>
<dt>-p print_file</p>
<dd>This specifies the &quot;print&quot; file. Any output from the scheduler code which is written to standard out or standard error will be written to this file. If this option is not given, the file used will be $PBS_HOME/sched_priv/sched_out. See the -d option.</p>
<dt>-a alarm</p>
<dd>This specifies the time in seconds to wait for a schedule run to finish. If a scheduling iteration takes too long to finish, an alarm signal is sent, and the scheduler is restarted. If a core file does not exist in the current directory, abort() is called and a core file is generated. The default for alarm is 180 seconds.</p>
<dt>-S port</p>
<dd>Specifies a port on which to talk to the server. This option is not required. It merely overides the default PBS scheduler port.</p>
<dt>-c configfile</p>
<dd>Specify a configuration file, see description below. If this is a relative file name it will be relative to PBS_HOME/sched_priv, see the -d option. If the -c option is not supplied, pbs_sched will not attempt to open a configuration file. In BASL, this config file is almost always needed because it is where the list of servers, nodes, and host resource queries are specified by the administrator.</dl>
<h2>Usage</h2>
<p>This version of the scheduler requires knowledge of the BASL language. The site must first write a function called <i>sched_main()</i> (and all functions supporting it) using BASL constructs, and then translate the functions into C using the BASL compiler <i>basl2c,</i> which would also attach a main program to the resulting code. This main program performs general initialization and housekeeping chores such as setting up local socket to communicate with the server running on the same machine, cd-ing to the priv directory, opening log files, opening configuration file (if any), setting up locks, forking the child to become a daemon, initializing a scheduling cycle (i.e. get node attributes that are static in nature), setting up the signal handlers, executing global initialization assignment statements specified by the scheduler writer, and finally sitting on a loop waiting for a scheduling command from the server. When the server sends the scheduler an appropriate scheduling command <font SIZE="-1"><code>{SCH_SCHEDULE_NEW, SCH_SCHEDULE_TERM, SCH_SCHEDULE_TIME, SCH_SCHEDULE_RECYC, SCH_SCHEDULE_CMD, SCH_SCHEDULE_FIRST,}</code></font> information about server(s), jobs, queues, and execution host(s) are obtained, and then <i>sched_main()</i> is called.</p>
<h2>Scheduling Language</h2>
<p>The BAtch Scheduling Language (BASL) is a C-like procedural language. It provides a number of constructs and predefined functions that facilitate dealing with scheduling issues. Information about a PBS server, the queues that it owns, jobs residing on each queue, and the computational nodes where jobs can be run, are accessed via the BASL data types Server, Que, Job, CNode, Set Server, Set Que, Set Job, and Set CNode. </p>
<p> The following simple sched_main() will cause the server to run all queued jobs on the local server:</p>
<dl>
<dd>
<pre>sched_main()
{
 Server s;
 Que q;
 Job j;
 Set Que queues;
 Set Job jobs;
 s = AllServersLocalHostGet(); // get local server
 queues = ServerQueuesGet(s);
 foreach( q in queues ) {
 jobs = QueJobsGet(q);
 foreach( j in jobs ) {
 JobAction(j, SYNCRUN, NULLSTR);
 }
 }
 
}</pre>
</dl>
<p> For a more complete discussion of the Batch Scheduler Language, see <code><a href="//www.systutorials.com/docs/linux/man/1B-basl2c/">basl2c</a>(1B).</code></p>
<h2>Configuration File</h2>
<p>A configuration file may be specified with the -c option. This file is used to specify the (1) hosts which are allowed to connect to pbs_sched, (2) the list of server hosts for which the scheduler writer wishes the system to periodically check for status, queues, and jobs info, (3) list of execution hosts for which the scheduler writer wants the system to periodically check for information like state, property, and so on, and (4) various queries to send to each execution host.</p>
<dl>
<dt>(1) specifying client hosts:</p>
<dd>The hosts allowed to connect to pbs_sched are specified in the configuration file in a manner identical to that used in pbs_mom. There is one line per host using the syntax: </p>
<p> <code> </p>
<p> where and are separated by white space. Two host names are always allowed to connection to pbs_sched: &quot;localhost&quot; and the name returned to pbs_sched by the system call gethostname(). These names need not be specified in the configuration file.</p>
<dt>(2) specifying list of servers:</p>
<dd>The list of servers is specified in a one host per line manner, using the syntax: </p>
<p> or where and are separated by white space. </p>
<p> If is 0, then the default PBS server port will be used. </p>
<p> Regardless of what has been specified in the file, the list of servers will always include the local server &#8211; one running on the same host where the scheduler is running. </p>
<p> Within the BASL code, access to data of the list of servers is done by calling </code><i>AllServersGet(),</i> or <i>AllServersLocalHostGet()</i> which returns the local server on the list.</p>
<dt>(3) specifying the list of execution hosts:</p>
<dd>The list of execution hosts (nodes), whose MOMs are to be queried from the scheduler, is specified in a one host per line manner, using the syntax: </p>
<p> <code> </p>
<p> where and are separated by white space. </p>
<p> If is 0, then the default PBS MOM port will be used. </p>
<p> The BASL function </code><i>AllNodesGet()</i> , or <i>ServerNodesGet(AllServersLocalHostGet())</i> is available for getting the list of nodes known to the local system.</p>
<dt>(4) specifying the list of host resources:</p>
<dd>For specifying the list of host resource queries to send to each execution host&#8217;s MOM, the following syntax is used: </p>
<p> <code> </p>
<p> should be the same hostname string that was specified in a line. A value of &quot;*&quot; (wildcard) means to match any node. </p>
<p> Please consult section 9 of the PBS ERS (Resource Monitor/Resources) for a list of possible values to parameter. </p>
<p> refers to the actual function name that is called from the scheduler code to obtain the return values to host resource queries. The list of function names that can appear in the configuration file are: </code></p>
<pre> STATIC: 
 ================================
 CNodePropertiesGet
 CNodeVendorGet
 CNodeNumCpusGet
 CNodeOsGet
 CNodeMemTotalGet[type]
 CNodeNetworkBwGet[type]
 CNodeSwapSpaceTotalGet[name]
 CNodeDiskSpaceTotalGet[name]
 CNodeDiskInBwGet[name]
 CNodeDiskOutBwGet[name]
 CNodeTapeSpaceTotalGet[name]
 CNodeTapeInBwGet[name]
 CNodeTapeOutBwGet[name]
 CNodeSrfsSpaceTotalGet[name]
 CNodeSrfsInBwGet[name]
 CNodeSrfsOutBwGet[name]
 DYNAMIC:
 ================================
 CNodeIdletimeGet
 CNodeLoadAveGet
 CNodeMemAvailGet[type]
 CNodeSwapSpaceAvailGet[name]
 CNodeSwapInBwGet[name]
 CNodeSwapOutBwGet[name]
 CNodeDiskSpaceReservedGet[name]
 CNodeDiskSpaceAvailGet[name]
 CNodeTapeSpaceAvailGet[name]
 CNodeSrfsSpaceReservedGet[name]
 CNodeSrfsSpaceAvailGet[name]
 CNodeCpuPercentIdleGet
 CNodeCpuPercentSysGet
 CNodeCpuPercentUserGet
 CNodeCpuPercentGuestGet</pre>
<p>STATIC function names return values that are obtained only during the first scheduling cycle, or when the scheduler is instructed to reconfig; whereas, DYNAMIC function names return attribute values that are taken at every subsequent scheduling cycle. </p>
<p> <code>name</code> and <code>type</code> are arbitrarily defined. For example, you can choose to have <code>name</code> defined as &quot;$FASTDIR&quot; for the CNodeSrfs* calls, and a sample configuration file entry would look like: </p>
<pre> $node unicos8 CNodeSrfsSpaceAvailGet[$FASTDIR]
 quota[type=ares_avail,dir=$FASTDIR]</pre>
<p>So in a BASL code, if you call CNodeSrfsSpaceAvailGet(node, &quot;$FASTDIR&quot;), then it will return the value to the query &quot;quota[type=ares_avail,dir=$FASTDIR]&quot; (3rd parameter) as sent to the node&#8217;s MOM. </p>
<p> By default, the scheduler has already internally defined the following mappings, which can be overriden in the configuration file: </p>
<pre>keyword node_name CNode..Get host_resource
======= ========= ================ =============
$node * CNodeOsGet arch
$node * CNodeLoadAveGet loadave
$node * CNodeIdletimeGet idletime</pre>
<p>The above means that for all declared nodes (via $momhost), the host queries <code> and will be sent to each node&#8217;s MOM. The value to is obtained internally by the system during the first scheduling cycle because it falls under STATIC category, while values to and are taken at every scheduling iteration because they fall under the DYNAMIC category. Access to the return values is done by calling </code><i> and respectively. The following are some sample $node arguments that you may put in the configuration file. </i></p>
<pre>node_name CNode..Get host res
================== ========================= ==========
&lt;sunos4_nodename&gt; CNodeIdletimeGet idletime
&lt;sunos4_nodename&gt; CNodeLoadAveGet loadave
&lt;sunos4_nodename&gt; CNodeMemTotalGet[real] physmem
&lt;sunos4_nodename&gt; CNodeMemTotalGet[virtual] totmem
&lt;sunos4_nodename&gt; CNodeMemAvailGet[virtual] availmem
&lt;irix5_nodename&gt; CNodeNumCpusGet ncpus
&lt;irix5_nodename&gt; CNodeMemTotalGet[real] physmem
&lt;irix5_nodename&gt; CNodeMemTotalGet[virtual] totmem
&lt;irix5_nodename&gt; CNodeIdletimeGet idletime
&lt;irix5_nodename&gt; CNodeLoadAveGet loadave
&lt;irix5_nodename&gt; CNodeMemAvailGet[virtual] availmem
&lt;linux_nodename&gt; CNodeNumCpusGet ncpus
&lt;linux_nodename&gt; CNodeMemTotalGet[real] physmem
&lt;linux_nodename&gt; CNodeMemTotalGet[virtual] totmem
&lt;linux_nodename&gt; CNodeIdletimeGet idletime
&lt;linux_nodename&gt; CNodeLoadAveGet loadave
&lt;linux_nodename&gt; CNodeMemAvailGet[virtual] availmem
&lt;solaris5_nodename&gt; CNodeIdletimeGet idletime
&lt;solaris5_nodename&gt; CNodeLoadAveGet loadave
&lt;solaris5_nodename&gt; CNodeNumCpusGet ncpus
&lt;solaris5_nodename&gt; CNodeMemTotalGet[real] physmem
&lt;aix4_nodename&gt; CNodeIdletimeGet idletime
&lt;aix4_nodename&gt; CNodeLoadAveGet loadave
&lt;aix4_nodename&gt; CNodeMemTotalGet[virtual] totmem
&lt;aix4_nodename&gt; CNodeMemAvailGet[virtual] availmem
&lt;unicos8_nodename&gt; CNodeIdletimeGet idletime
&lt;unicos8_nodename&gt; CNodeLoadAveGet loadave
&lt;unicos8_nodename&gt; CNodeNumCpusGet ncpus
&lt;unicos8_nodename&gt; CNodeMemTotalGet[real] physme
&lt;unicos8_nodename&gt; CNodeMemAvailGet[virtual] availmem
&lt;unicos8_nodename&gt; CNodeSwapSpaceTotalGet[primary] swaptotal
&lt;unicos8_nodename&gt; CNodeSwapSpaceAvailGet[primary] swapavail
&lt;unicos8_nodename&gt; CNodeSwapInBwGet[primary] swapinrate
&lt;unicos8_nodename&gt; CNodeSwapOutBwGet[primary] swapoutrate
&lt;unicos8_nodename&gt; CNodePercentIdleGet cpuidle
&lt;unicos8_nodename&gt; CNodePercentSysGet cpuunix
&lt;unicos8_nodename&gt; CNodePercentGuestGet cpuguest
&lt;unicos8_nodename&gt; CNodePercentUsrGet cpuuser
&lt;unicos8_nodename&gt; CNodeSrfsSpaceAvailGet[$FASTDIR] quota[type
 =ares_avail,
 dir=$FASTDIR]
&lt;unicos8_nodename&gt; CNodeSrfsSpaceAvailGet[$BIGDIR] quota[type
 =ares_avail,
 dir=$BIGDIR]
&lt;unicos8_nodename&gt; CNodeSrfsSpaceAvailGet[$WRKDIR] quota[type
 =ares_avail,
 dir=$WRKDIR]
&lt;sp2_nodename&gt; CNodeLoadAveGet loadave</pre>
<p>Suppose you have an execution host that is of irix5 os type, then the &lt;irix5_node_name&gt; entries will be consulted by the scheduler. The initial scheduling cycle would involve sending the STATIC queries <code> to the execution host&#8217;s MOM, and access to return values of the queries is done via respectively, where node is the CNode representation of the execution host. The subsequent scheduling cycles will only send DYNAMIC queries and and access to the return values of the queries is done via respectively.</dl>
<p> &quot;Later&quot; entries in the config file take precedence. </p>
<p> The configuration file must be &quot;secure&quot;. It must be owned by a user id and group id less than 10 and not be world writable. </p>
<p> On receipt of a SIGHUP signal, the scheduler will close and reopen its log file and reread its configuration file (if any). </p>
<p> </code></p>
<h2>Files</h2>
<dl>
<dt>$PBS_SERVER_HOME/sched_priv</p>
<dd>the default directory for configuration files, typically (/usr/spool/pbs)/sched_priv.</dl>
<h2>Signal Handling</h2>
<p>A C based scheduler will handle the following signals:</p>
<dl>
<dt>SIGHUP</p>
<dd>The server will close and reopen its log file and reread the config file if one exists.</p>
<dt>SIGALRM</p>
<dd>If the site supplied scheduling module exceeds the time limit, the Alarm will cause the scheduler to attempt to core dump and restart itself.</p>
<dt>SIGINT and SIGTERM</p>
<dd>Will result in an orderly shutdown of the scheduler.</dl>
<p> All other signals have the default action installed.</p>
<h2>Exit Status</h2>
<p>Upon normal termination, an exit status of zero is returned.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-basl2c/">basl2c</a>(1B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched_tcl/">pbs_sched_tcl</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B).<br />
 PBS Internal Design Specification </p>
