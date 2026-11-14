---
title: "ndb_mgmd(8)"
name: "ndb_mgmd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ndb_mgmd/"
description: "ndb_mgmd – the MySQL Cluster management server daemon"
---

<p>ndb_mgmd &#8211; the MySQL Cluster management server daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ndb_mgmd </code><i>options</i></dl>
<h2>Description</h2>
<dd>The management server is the process that reads the cluster configuration file and distributes this information to all nodes in the cluster that request it. It also maintains a log of cluster activities. Management clients can connect to the management server and check the cluster&#8217;s status. </p>
<p> The following table includes options that are specific to the MySQL Cluster management server program <code>ndb_mgmd</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<dl>
<dd>* <code>&#8211;bind-address=</code><i>host</i><code>[:</code><i>port</i><code>]</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.22-ndb-6.3.2
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;bind-address
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
<td> [none] </td>
</tr>
</table>
<p> When specified, this option limits management server connections by management clients to clients at the specified host name or IP address (and possibly port, if this is also specified). In such cases, a management client attempting to connect to the management server from any other address fails with the error Unable to setup port: <i>host</i>:<i>port</i>! </p>
<p> If the <i>port</i> is not specified, the management client attempts to use port 1186. </p>
<p> This option was added in MySQL Cluster NDB 6.2.5 and MySQL Cluster NDB 6.3.2.</dl>
<dl>
<dd>* <code>&#8211;configdir=</code><i>directory</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.30-ndb-6.4.0
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;configdir=directory
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> filename </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> $INSTALLDIR/mysql-cluster </td>
</tr>
</table>
<p> Beginning with MySQL Cluster NDB 6.4.0, configuration data is cached internally rather than being read from the cluster global configuration file each time the management server is started (see Section 17.3.2, lqMySQL Cluster Configuration Filesrq). This option instructs the management server to its configuration cache in the <i>directory</i> indicated. By default, this is a directory named mysql-cluster in the MySQL installation directory &#8212; for example, if you compile and install MySQL Cluster on a Unix system using the default location, this is /usr/local/mysql-cluster. </p>
<p> This behavior can be overridden using the <code>&#8211;initial</code> or <code>&#8211;reload</code> option for <code>ndb_mgmd</code>. Each of these options is described elsewhere in this section. </p>
<p> This option is available beginning with MySQL Cluster NDB 6.4.0. </p>
<p> Beginning with MySQL Cluster NDB 7.0.8, <code>&#8211;config-dir</code> is accepted as an alias for <code>&#8211;configdir</code>.</dl>
<dl>
<dd>* <code>&#8211;config-file=</code><i>filename</i>, <code>-f </code><i>filename</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> -c
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> filename </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> ./config.ini </td>
</tr>
</table>
<p> Instructs the management server as to which file it should use for its configuration file. By default, the management server looks for a file named config.ini in the same directory as the <code>ndb_mgmd</code> executable; otherwise the file name and location must be specified explicitly. </p>
<p> Beginning with MySQL Cluster NDB 6.4.0, this option is ignored unless the management server is forced to read the configuration file, either because <code>ndb_mgmd</code> was started with the <code>&#8211;reload</code> or <code>&#8211;initial</code> option, or because the management server could not find any configuration cache. See Section 17.3.2, lqMySQL Cluster Configuration Filesrq, for more information.</dl>
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
<p> Instructs <code>ndb_mgmd</code> to start as a daemon process. This is the default behavior. </p>
<p> This option has no effect when running <code>ndb_mgmd</code> on Windows platforms.</dl>
<dl>
<dd>* <code>&#8211;initial</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.30-ndb-6.4.0
</td>
</tr>
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
<p> Beginning with MySQL Cluster NDB 6.4.0, configuration data is cached internally rather than being read from the cluster global configuration file each time the management server is started (see Section 17.3.2, lqMySQL Cluster Configuration Filesrq). Using this option overrides this behavior, by forcing the management server to delete any existing cache files, and then to re-read the configuration data from the cluster configuration file and to build a new cache. </p>
<p> This differs in two ways from the <code>&#8211;reload</code> option. First, <code>&#8211;reload</code> forces the server to check the configuration file against the cache and reload its data only if the contents of the file are different from the cache. Second, <code>&#8211;reload</code> does not delete any existing cache files. </p>
<p> If <code>ndb_mgmd</code> is invoked with <code>&#8211;initial</code> but cannot find a global configuration file, the management server cannot start. </p>
<p> This option was introduced in MySQL Cluster NDB 6.4.0.</dl>
<dl>
<dd>* <code>&#8211;log-name=</code><i>name</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.37-ndb-7.0.8
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;log-name=
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
<td> MgmtSrvr </td>
</tr>
</table>
<p> Provides a name to be used for this node in the cluster log. </p>
<p> This option was added in MySQL Cluster NDB 7.0.8.</dl>
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
<p> Instructs <code>ndb_mgmd</code> not to start as a daemon process. </p>
<p> As of MySQL Cluster NDB 7.0.8, the default behavior for <code>ndb_mgmd</code> on Windows is to run in the foreground, making this option unnecessary on Windows platforms. (m[blue]<code>Bug#45588</code>m[]<font SIZE="-2">[1]</font>)</dl>
<dl>
<dd>* <code>&#8211;print-full-config</code>, <code>-P</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;print-full-config
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
<p> Shows extended information regarding the configuration of the cluster. With this option on the command line the <code>ndb_mgmd</code> process prints information about the cluster setup including an extensive list of the cluster configuration sections as well as parameters and their values. Normally used together with the <code>&#8211;config-file</code> (<code>-f</code>) option.</dl>
<dl>
<dd>* <code>&#8211;reload</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.30-ndb-6.4.0
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;reload
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
<p> Beginning with MySQL Cluster NDB 6.4.0, configuration data is stored internally rather than being read from the cluster global configuration file each time the management server is started (see Section 17.3.2, lqMySQL Cluster Configuration Filesrq). Using this option forces the management server to check its internal data store against the cluster configuration file and to reload the configuration if it finds that the configuration file does not match the cache. Existing configuration cache files are preserved, but not used. </p>
<p> This differs in two ways from the <code>&#8211;initial</code> option. First, <code>&#8211;initial</code> causes all cache files to be deleted. Second, <code>&#8211;initial</code> forces the management server to re-read the global configuration file and construct a new cache. </p>
<p> If the management server cannot find a global configuration file, then the <code>&#8211;reload</code> option is ignored. </p>
<p> This option was introduced in MySQL Cluster NDB 6.4.0.</dl>
<dl>
<dd>* <code>&#8211;nowait-nodes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.39-ndb-7.1.0
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
<td> numeric </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
<tr VALIGN=top>
<td> <code>Range</code> </td>
<td> 1-255 </td>
</tr>
</table>
<p> When starting a MySQL Cluster is configured with two management nodes and running MySQL Cluster NDB 7.0 and later, each management server normally checks to see whether the other <code>ndb_mgmd</code> is also operational and whether the other management server&#8217;s configuration is identical to its own. However, it is sometimes desirable to start the cluster with only one management node (and perhaps to allow the other <code>ndb_mgmd</code> to be started later). This option causes the management node to bypass any checks for any other management nodes whose node IDs are passed to this option, allowing the cluster to start as though configured to use only the management node that was started. </p>
<p> For purposes of illustration, consider the following portion of a config.ini file (where we have omitted most of the configuration parameters that are not relevant to this example): </p>
<dl>
<dd>
<pre>[ndbd]
NodeId = 1
HostName = 192.168.0.101
[ndbd]
NodeId = 2
HostName = 192.168.0.102
[ndbd]
NodeId = 3
HostName = 192.168.0.103
[ndbd]
NodeId = 4
HostName = 192.168.0.104
[mgm]
NodeId = 10
HostName = 192.168.0.150
[mgm]
NodeId = 11
HostName = 192.168.0.151
[api]
NodeId = 20
HostName = 192.168.0.200
[api]
NodeId = 21
HostName = 192.168.0.201</pre>
</dl>
<p> Assume that you wish to start this cluster using only the management server having node ID 10 and running on the host having the IP address 192.168.0.150. (Suppose, for example, that the host computer on which you intend to the other management server is temporarily unavailable due to a hardware failure, and you are waiting for it to be repaired.) To start the cluster in this way, use a command line on the machine at 192.168.0.150 to enter the following command: </p>
<dl>
<dd>
<pre>shell&gt; <code>ndb_mgmd --ndb-nodeid=10 --nowait-nodes=11</code></pre>
</dl>
<p> As shown in the preceding example, when using <code>&#8211;nowait-nodes</code>, you must also use the <code>&#8211;ndb-nodeid</code> option to specify the node ID of this <code>ndb_mgmd</code> process. </p>
<p> You can then start each of the cluster&#8217;s data nodes in the usual way. If you wish to start and use the second management server in addition to the first management server at a later time without restarting the data nodes, you must start each data node with a connectstring that references both management servers, like this: </p>
<dl>
<dd>
<pre>shell&gt; <code>ndbd -c 192.168.0.150,192.168.0.151</code></pre>
</dl>
<p> The same is true with regard to the connectstring used with any <code>mysqld</code> processes that you wish to start as MySQL Cluster SQL nodes connected to this cluster. See Section 17.3.2.3, lqThe MySQL Cluster Connectstringrq, for more information. </p>
<p> When used with <code>ndb_mgmd</code>, this option affects the behavior of the management node with regard to other management nodes only. Do not confuse it with the <code>&#8211;nowait-nodes</code> option used with <code>ndbd</code> (or <code>ndbmtd</code> in MySQL Cluster NDB 7.0 and later) to allow a cluster to start with fewer than its full complement of data nodes; when used with data nodes, this option affects their behavior only with regard to other data nodes. </p>
<p> Multiple management node IDs may be passed to this option as a comma-separated list. Each node ID must be no less than 1 and no greater than 255. In practice, it is quite rare to use more than two management servers for the same MySQL Cluster (or to have any need for doing so); in most cases you need to pass to this option only the single node ID for the one management server that you do not wish to use when starting the cluster. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 When you later start the lqmissingrq management server, its configuration must match that of the management server that is already in use by the cluster. Otherwise, it fails the configuration check performed by the existing management server, and does not start. </p>
</dl>
<p> This option was introduced in MySQL Cluster NDB 7.0.10.</dl>
<p> It is not strictly necessary to specify a connectstring when starting the management server. However, if you are using more than one management server, a connectstring should be provided and each node in the cluster should specify its node ID explicitly. </p>
<p> See Section 17.3.2.3, lqThe MySQL Cluster Connectstringrq, for information about using connectstrings. <code><a href="/docs/linux/man/8-ndb_mgmd/">ndb_mgmd</a></code>(8), describes other options for <code>ndb_mgmd</code>. </p>
<p> The following files are created or used by <code>ndb_mgmd</code> in its starting directory, and are placed in the DataDir as specified in the config.ini configuration file. In the list that follows, <i>node_id</i> is the unique node identifier. </p>
<dl>
<dd>* config.ini is the configuration file for the cluster as a whole. This file is created by the user and read by the management server. Section 17.3, lqMySQL Cluster Configurationrq, discusses how to set up this file.</dl>
<dl>
<dd>* ndb_<i>node_id</i>_cluster.log is the cluster events log file. Examples of such events include checkpoint startup and completion, node startup events, node failures, and levels of memory usage. A complete listing of cluster events with descriptions may be found in Section 17.5, lqManagement of MySQL Clusterrq. </p>
<p> When the size of the cluster log reaches one million bytes, the file is renamed to ndb_<i>node_id</i>_cluster.log.<i>seq_id</i>, where <i>seq_id</i> is the sequence number of the cluster log file. (For example: If files with the sequence numbers 1, 2, and 3 already exist, the next log file is named using the number 4.)</dl>
<dl>
<dd>* ndb_<i>node_id</i>_out.log is the file used for stdout and stderr when running the management server as a daemon.</dl>
<dl>
<dd>* ndb_<i>node_id</i>.pid is the process ID file used when running the management server as a daemon.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Bug#45588</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.mysql.com/bug.php?id=45588">http://bugs.mysql.com/bug.php?id=45588</a></dl>
</dl>
<h2>See Also</h2>
<p>For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>Author</h2>
<p>Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>).</p>
