---
title: "ndbd(8)"
name: "ndbd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ndbd/"
description: "ndbd – the MySQL Cluster data node daemon"
---

<p>ndbd &#8211; the MySQL Cluster data node daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ndbd </code><i>options</i></dl>
<h2>Description</h2>
<p><code>ndbd</code></p>
<dd>is the process that is used to handle all the data in tables using the NDB Cluster storage engine. This is the process that empowers a data node to accomplish distributed transaction handling, node recovery, checkpointing to disk, online backup, and related tasks. In a MySQL Cluster, a set of <code>ndbd</code> processes cooperate in handling data. These processes can execute on the same computer (host) or on different computers. The correspondences between data nodes and Cluster hosts is completely configurable. The following table includes command options specific to the MySQL Cluster data node program <code>ndbd</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 All of these options also apply to the multi-threaded version of this program &#8212; <code>ndbmtd</code>, which is available in MySQL Cluster NDB 7.0 &#8212; and you may substitute lq<code>ndbmtd</code>rq for lq<code>ndbd</code>rq wherever the latter occurs in this section.  For options common to all NDBCLUSTER programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq.</p>
<dl>
<dd>* <code>&#8211;bind-address</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.12
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;bind-address=name
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> Causes <code>ndbd</code> to bind to a specific network interface (host name or IP address). This option has no default value. This option was added in MySQL 5.1.12.</dl>
<dl>
<dd>* <code>&#8211;daemon</code>, <code>-d</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;daemon
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> TRUE </td>
</tr>
</table>
<p> Instructs <code>ndbd</code> to execute as a daemon process. This is the default behavior. <code>&#8211;nodaemon</code> can be used to prevent the process from running as a daemon. This option has no effect when running <code>ndbd</code> or <code>ndbmtd</code> on Windows platforms.</dl>
<dl>
<dd>* <code>&#8211;initial</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;initial
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
</table>
<p> Instructs <code>ndbd</code> to perform an initial start. An initial start erases any files created for recovery purposes by earlier instances of <code>ndbd</code>. It also re-creates recovery log files. Note that on some operating systems this process can take a substantial amount of time. An <code>&#8211;initial</code> start is to be used <i>only</i> when starting the <code>ndbd</code> process under very special circumstances; this is because this option causes all files to be removed from the Cluster file system and all redo log files to be re-created. These circumstances are listed here:</p>
<dl>
<dd>* When performing a software upgrade which has changed the contents of any files.</dl>
<dl>
<dd>* When restarting the node with a new version of <code>ndbd</code>.</dl>
<dl>
<dd>* As a measure of last resort when for some reason the node restart or system restart repeatedly fails. In this case, be aware that this node can no longer be used to restore data due to the destruction of the data files.</dl>
<dl>
<dd>Use of this option prevents the StartPartialTimeout and StartPartitionedTimeout configuration parameters from having any effect.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 This option does <i>not</i> affect either of the following:</p>
<dl>
<dd>* Backup files that have already been created by the affected node</dl>
<dl>
<dd>* MySQL Cluster Disk Data files (see Section 17.5.10, lqMySQL Cluster Disk Data Tablesrq).</dl>
<dl>
<dd>This option also has no effect on recovery of data by a data node that is just starting (or restarting) from data nodes that are already running. This recovery of data occurs automatically, and requires no user intervention in a MySQL Cluster that is running normally.</dl>
<p> It is permissible to use this option when starting the cluster for the very first time (that is, before any data node files have been created); however, it is <i>not</i> necessary to do so.</dl>
<dl>
<dd>* <code>&#8211;initial-start</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.11
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;initial-start
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
</table>
<p> This option is used when performing a partial initial start of the cluster. Each node should be started with this option, as well as <code>&#8211;nowait-nodes</code>. Suppose that you have a 4-node cluster whose data nodes have the IDs 2, 3, 4, and 5, and you wish to perform a partial initial start using only nodes 2, 4, and 5 &#8212; that is, omitting node 3:</p>
<dl>
<dd>
<pre>shell&gt; <code>ndbd --ndb-nodeid=2 --nowait-nodes=3 --initial-start</code>
shell&gt; <code>ndbd --ndb-nodeid=4 --nowait-nodes=3 --initial-start</code>
shell&gt; <code>ndbd --ndb-nodeid=5 --nowait-nodes=3 --initial-start</code></pre>
</dl>
<p> Prior to MySQL 5.1.19, it was not possible to perform DDL operations involving Disk Data tables on a partially started cluster. (See m[blue]<code>Bug#24631</code>m[]<font SIZE="-2">[1]</font>.) When using this option, you must also specify the node ID for the data node being started with the <code>&#8211;ndb-nodeid</code> option. This option was added in MySQL 5.1.11.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 Do not confuse this option with the <code>&#8211;nowait-nodes</code> option added for <code>ndb_mgmd</code> in MySQL Cluster NDB 7.0.10, which can be used to allow a cluster configured with multiple management servers to be started without all management servers being online. </p>
<dl>
<dd>* <code>&#8211;nowait-nodes=</code><i>node_id_1</i><code>[, </code><i>node_id_2</i><code>[, &#8230;]]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.9
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;nowait-nodes=list
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> string </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
</table>
<p> This option takes a list of data nodes which for which the cluster will not wait for before starting. This can be used to start the cluster in a partitioned state. For example, to start the cluster with only half of the data nodes (nodes 2, 3, 4, and 5) running in a 4-node cluster, you can start each <code>ndbd</code> process with <code>&#8211;nowait-nodes=3,5</code>. In this case, the cluster starts as soon as nodes 2 and 4 connect, and does <i>not</i> wait StartPartitionedTimeout milliseconds for nodes 3 and 5 to connect as it would otherwise. If you wanted to start up the same cluster as in the previous example without one <code>ndbd</code> &#8212; say, for example, that the host machine for node 3 has suffered a hardware failure &#8212; then start nodes 2, 4, and 5 with <code>&#8211;nowait-nodes=3</code>. Then the cluster will start as soon as nodes 2, 4, and 5 connect and will not wait for node 3 to start. This option was added in MySQL 5.1.9.</dl>
<dl>
<dd>* <code>&#8211;nodaemon</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;nodaemon
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> (windows) </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> TRUE </td>
</tr>
</table>
<p> Instructs <code>ndbd</code> not to start as a daemon process. This is useful when <code>ndbd</code> is being debugged and you want output to be redirected to the screen. As of MySQL Cluster NDB 7.0.8, the default behavior for <code>ndbd</code> and <code>ndbmtd</code> on Windows is to run in the foreground, making this option unnecessary on Windows platforms. (m[blue]<code>Bug#45588</code>m[]<font SIZE="-2">[2]</font>)</dl>
<dl>
<dd>* <code>&#8211;nostart</code>, <code>-n</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;nostart
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> boolean </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> FALSE </td>
</tr>
</table>
<p> Instructs <code>ndbd</code> not to start automatically. When this option is used, <code>ndbd</code> connects to the management server, obtains configuration data from it, and initializes communication objects. However, it does not actually start the execution engine until specifically requested to do so by the management server. This can be accomplished by issuing the proper START command in the management client (see Section 17.5.2, lqCommands in the MySQL Cluster Management Clientrq).</dl>
<p> <code>ndbd</code> generates a set of log files which are placed in the directory specified by DataDir in the config.ini configuration file. These log files are listed below. <i>node_id</i> is the node&#8217;s unique identifier. Note that <i>node_id</i> represents the node&#8217;s unique identifier. For example, ndb_2_error.log is the error log generated by the data node whose node ID is 2.</p>
<dl>
<dd>* ndb_<i>node_id</i>_error.log is a file containing records of all crashes which the referenced <code>ndbd</code> process has encountered. Each record in this file contains a brief error string and a reference to a trace file for this crash. A typical entry in this file might appear as shown here:</p>
<dl>
<dd>
<pre>Date/Time: Saturday 30 July 2004 - 00:20:01
Type of error: error
Message: Internal program error (failed ndbrequire)
Fault ID: 2341
Problem data: DbtupFixAlloc.cpp
Object of reference: DBTUP (Line: 173)
ProgramName: NDB Kernel
ProcessID: 14909
TraceFile: ndb_2_trace.log.2
***EOM***</pre>
</dl>
<p> Listings of possible <code>ndbd</code> exit codes and messages generated when a data node process shuts down prematurely can be found in m[blue]<code>ndbd Error Messages</code>m[]<font SIZE="-2">[3]</font>.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 <i>The last entry in the error log file is not necessarily the newest one</i> (nor is it likely to be). Entries in the error log are <i>not</i> listed in chronological order; rather, they correspond to the order of the trace files as determined in the ndb_<i>node_id</i>_trace.log.next file (see below). Error log entries are thus overwritten in a cyclical and not sequential fashion. </p>
<dl>
<dd>* ndb_<i>node_id</i>_trace.log.<i>trace_id</i> is a trace file describing exactly what happened just before the error occurred. This information is useful for analysis by the MySQL Cluster development team. It is possible to configure the number of these trace files that will be created before old files are overwritten. <i>trace_id</i> is a number which is incremented for each successive trace file.</dl>
<dl>
<dd>* ndb_<i>node_id</i>_trace.log.next is the file that keeps track of the next trace file number to be assigned.</dl>
<dl>
<dd>* ndb_<i>node_id</i>_out.log is a file containing any data output by the <code>ndbd</code> process. This file is created only if <code>ndbd</code> is started as a daemon, which is the default behavior.</dl>
<dl>
<dd>* ndb_<i>node_id</i>.pid is a file containing the process ID of the <code>ndbd</code> process when started as a daemon. It also functions as a lock file to avoid the starting of nodes with the same identifier.</dl>
<dl>
<dd>* ndb_<i>node_id</i>_signal.log is a file used only in debug versions of <code>ndbd</code>, where it is possible to trace all incoming, outgoing, and internal messages with their data in the <code>ndbd</code> process.</dl>
<p> It is recommended not to use a directory mounted through NFS because in some environments this can cause problems whereby the lock on the .pid file remains in effect even after the process has terminated. To start <code>ndbd</code>, it may also be necessary to specify the host name of the management server and the port on which it is listening. Optionally, one may also specify the node ID that the process is to use. </p>
<pre><code>shell&gt; ndbd --connect-string=&quot;nodeid=2;host=ndb_mgmd.mysql.com:1186&quot;</code></pre>
<p> See Section 17.3.2.3, lqThe MySQL Cluster Connectstringrq, for additional information about this issue. <code><a href="/docs/linux/man/8-ndbd/">ndbd</a></code>(8), describes other options for <code>ndbd</code>. When <code>ndbd</code> starts, it actually initiates two processes. The first of these is called the lqangel processrq; its only job is to discover when the execution process has been completed, and then to restart the <code>ndbd</code> process if it is configured to do so. Thus, if you attempt to kill <code>ndbd</code> via the Unix <code>kill</code> command, it is necessary to kill both processes, beginning with the angel process. The preferred method of terminating an <code>ndbd</code> process is to use the management client and stop the process from there. The execution process uses one thread for reading, writing, and scanning data, as well as all other activities. This thread is implemented asynchronously so that it can easily handle thousands of concurrent actions. In addition, a watch-dog thread supervises the execution thread to make sure that it does not hang in an endless loop. A pool of threads handles file I/O, with each thread able to handle one open file. Threads can also be used for transporter connections by the transporters in the <code>ndbd</code> process. In a multi-processor system performing a large number of operations (including updates), the <code>ndbd</code> process can consume up to 2 CPUs if permitted to do so. For a machine with many CPUs it is possible to use several <code>ndbd</code> processes which belong to different node groups; however, such a configuration is still considered experimental and is not supported for MySQL 5.1 in a production setting. See Section 17.1.5, lqKnown Limitations of MySQL Clusterrq.</dl>
</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Bug#24631</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.mysql.com/bug.php?id=24631">http://bugs.mysql.com/bug.php?id=24631</a></dl>
<dt> 2.</p>
<dd>Bug#45588</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.mysql.com/bug.php?id=45588">http://bugs.mysql.com/bug.php?id=45588</a></dl>
<dt> 3.</p>
<dd>ndbd Error Messages</p>
<dl>
<dd><a rel="nofollow" href="http://dev.mysql.com/doc/ndbapi/en/ndbd-error-messages.html">http://dev.mysql.com/doc/ndbapi/en/ndbd-error-messages.html</a></dl>
</dl>
<h2>See Also</h2>
<p>For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>Author</h2>
<p>Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).</p>
