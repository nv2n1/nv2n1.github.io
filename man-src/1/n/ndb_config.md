---
title: "ndb_config(1)"
name: "ndb_config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_config/"
description: "ndb_config – extract MySQL Cluster configuration information"
---

<h2 class="name">NAME</h2>
<p> ndb_config &#8211; extract MySQL Cluster configuration information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_config </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<dd>This tool extracts current configuration information for data nodes, SQL nodes, and API nodes from a cluster management node (and possibly its config.ini file). Beginning with MySQL Cluster NDB 6.3.25 and MySQL Cluster NDB 7.0.6, it can also provide an offline dump (in text or XML format) of all configuration parameters which can be used, along with their default, maximum, and minimum values and other information (see the discussion of the <code>&#8211;configinfo</code> and <code>&#8211;xml</code> options later in this section). </p>
<p> The following table includes options that are specific to <code>ndb_config</code>. Additional descriptions follow the table. For options common to all MySQL Cluster programs, see Section 17.4.2, lqOptions Common to MySQL Cluster Programsrq. </p>
<dl>
<dt>
<dd> * <code>&#8211;usage</code>, <code>&#8211;help</code>, or <code>-?</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;help
</td>
</tr>
</table>
<p> Causes <code>ndb_config</code> to print a list of available options, and then exit.</dl>
<dl>
<dt>
<dd> * <code>&#8211;version</code>, <code>-V</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> -V
</td>
</tr>
</table>
<p> Causes <code>ndb_config</code> to print a version information string, and then exit.</dl>
<dl>
<dt>
<dd> * <code>&#8211;ndb-connectstring=</code><i>connect_string</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;ndb-connectstring=name
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
<td> localhost:1186 </td>
</tr>
</table>
<p> Specifies the connectstring to use in connecting to the management server. The format for the connectstring is the same as described in Section 17.3.2.3, lqThe MySQL Cluster Connectstringrq, and defaults to localhost:1186. </p>
<p> The use of <code>-c</code> as a short version for this option is supported for <code>ndb_config</code> beginning with MySQL 5.1.12.</dl>
<dl>
<dt>
<dd> * <code>&#8211;config-file=</code><i>path-to-file</i> </p>
<p> Gives the path to the management server&#8217;s configuration file (config.ini). This may be a relative or absolute path. If the management node resides on a different host from the one on which <code>ndb_config</code> is invoked, then an absolute path must be used.</dl>
<dl>
<dt>
<dd> * <code>&#8211;query=</code><i>query-options</i>, <code>-q</code> <i>query-options</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;query=string
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
<p> This is a comma-delimited list of query options &#8212; that is, a list of one or more node attributes to be returned. These include id (node ID), type (node type &#8212; that is, ndbd, mysqld, or ndb_mgmd), and any configuration parameters whose values are to be obtained. </p>
<p> For example, <code>&#8211;query=id,type,indexmemory,datamemory</code> would return the node ID, node type, DataMemory, and IndexMemory for each node. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If a given parameter is not applicable to a certain type of node, than an empty string is returned for the corresponding value. See the examples later in this section for more information. </p>
</dl>
</dl>
<dl>
<dt>
<dd> * <code>&#8211;host=</code><i>hostname</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;host=name
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
<p> Specifies the host name of the node for which configuration information is to be obtained. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 While the hostname localhost usually resolves to the IP address 127.0.0.1, this may not necessarily be true for all operating platforms and configurations. This means that it is possible, when localhost is used in config.ini, for <code>ndb_config </code><code>&#8211;host=localhost</code> to fail if <code>ndb_config</code> is run on a different host where localhost resolves to a different address (for example, on some versions of SUSE Linux, this is 127.0.0.2). In general, for best results, you should use numeric IP addresses for all MySQL Clustewr configuration values relating to hosts, or verify that all MySQL Cluster hosts handle localhost in the same fashion. </p>
</dl>
</dl>
<dl>
<dt>
<dd> * <code>&#8211;id=</code><i>node_id</i>, <code>&#8211;nodeid=</code><i>node_id</i> </p>
<p> Used to specify the node ID of the node for which configuration information is to be obtained.</dl>
<dl>
<dt>
<dd> * <code>&#8211;nodes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;nodes
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
<p> (Tells <code>ndb_config</code> to print information from parameters defined in [ndbd] sections only. Currently, using this option has no affect, since these are the only values checked, but it may become possible in future to query parameters set in [tcp] and other sections of cluster configuration files.)</dl>
<dl>
<dt>
<dd> * <code>&#8211;type=</code><i>node_type</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;type=name
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> &nbsp;<wbr> </td>
<td COLSPAN=2> <code>Permitted Values </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Type</code> </td>
<td> enumeration </td>
</tr>
<tr VALIGN=top>
<td> <code>Default</code> </td>
<td> </td>
</tr>
<tr VALIGN=top>
<td> <code>Valid Values</code> </td>
<td> ndbd, mysqld, ndb_mgmd </td>
</tr>
</table>
<p> Filters results so that only configuration values applying to nodes of the specified <i>node_type</i> (ndbd, mysqld, or ndb_mgmd) are returned.</dl>
<dl>
<dt>
<dd> * <code>&#8211;fields=</code><i>delimiter</i>, <code>-f</code> <i>delimiter</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;fields=string
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
<p> Specifies a <i>delimiter</i> string used to separate the fields in the result. The default is lq,rq (the comma character). </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If the <i>delimiter</i> contains spaces or escapes (such as 
 for the linefeed character), then it must be quoted. </p>
</dl>
</dl>
<dl>
<dt>
<dd> * <code>&#8211;rows=</code><i>separator</i>, <code>-r</code> <i>separator</i> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;rows=string
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
<p> Specifies a <i>separator</i> string used to separate the rows in the result. The default is a space character. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If the <i>separator</i> contains spaces or escapes (such as 
 for the linefeed character), then it must be quoted. </p>
</dl>
</dl>
<dl>
<dt>
<dd> * <code>&#8211;configinfo</code> </p>
<p> The <code>&#8211;configinfo</code> option, added in MySQL Cluster NDB 6.3.25 and MySQL Cluster NDB 7.0.6, causes <code>ndb_config</code> to dump a list of each MySQL Cluster configuration parameter supported by the MySQL Cluster distribution of which <code>ndb_config</code> is a part, including the following information: </p>
<dl>
<dt>
<dd> * A brief description of each parameter&#8217;s purpose, effects, and usage</dl>
<dl>
<dt>
<dd> * The section of the config.ini file where the parameter may be used</dl>
<dl>
<dt>
<dd> * The parameter&#8217;s data type or unit of measurement</dl>
<dl>
<dt>
<dd> * Where applicable, the parameter&#8217;s default, minimum, and maximum values</dl>
<dl>
<dt>
<dd> * A brief description of the parameter&#8217;s purpose, effects, and usage</dl>
<dl>
<dt>
<dd> * MySQL Cluster release version and build information</dl>
<dl>
<dt>
<dd> By default, this output is in text format. Part of this output is shown here: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ndb_config --configinfo</code>
****** SYSTEM ******
Name (String)
Name of system (NDB Cluster)
MANDATORY
PrimaryMGMNode (Non-negative Integer)
Node id of Primary ndb_mgmd(MGM) node
Default: 0 (Min: 0, Max: 4294967039)
ConfigGenerationNumber (Non-negative Integer)
Configuration generation number
Default: 0 (Min: 0, Max: 4294967039)
****** DB ******
MaxNoOfSubscriptions (Non-negative Integer)
Max no of subscriptions (default 0 == MaxNoOfTables)
Default: 0 (Min: 0, Max: 4294967039)
MaxNoOfSubscribers (Non-negative Integer)
Max no of subscribers (default 0 == 2 * MaxNoOfTables)
Default: 0 (Min: 0, Max: 4294967039)
...
</pre>
</dl>
<p> <code>&#8211;configinfo</code> <code>&#8211;xml</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> <code>Version Introduced</code> </td>
<td COLSPAN=2> 5.1.34-ndb-7.0.6
</td>
</tr>
<tr VALIGN=top>
<td> <code>Command-Line Format</code> </td>
<td COLSPAN=2> &#8211;configinfo &#8211;xml
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
<td> false </td>
</tr>
</table>
<p> You can obtain the output of <code>ndb_config</code> <code>&#8211;configinfo</code> as XML by adding the <code>&#8211;xml</code> option (like the <code>&#8211;configinfo</code> option, available beginning with MySQL Cluster NDB 6.3.25 and MySQL Cluster NDB 7.0.6). A portion of the resulting output is shown in this example: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt; ndb_config-- configinfo-- xml&lt;configvariables protocolversion = "1" ndbversionstring = "mysql-5.1.34 ndb-7.0.6" ndbversion = "458758" ndbversionmajor = "7" ndbversionminor = "0" ndbversionbuild = "6"&gt;
    &lt;section name = "SYSTEM"&gt;
    &lt;param name = "Name" comment = "Name of system (NDB Cluster)" type = "string" mandatory = "true" /&gt;
    &lt;param name = "PrimaryMGMNode" comment = "Node id of Primary ndb_mgmd(MGM) node" type = "unsigned" default = "0" min = "0" max = "4294967039" /&gt;
    &lt;param name = "ConfigGenerationNumber" comment = "Configuration generation number" type = "unsigned" default = "0" min = "0" max = "4294967039" /&gt;
    &lt;/ section&gt;
    &lt;section name = "NDBD"&gt;
    &lt;param name = "MaxNoOfSubscriptions" comment = "Max no of subscriptions (default 0 == MaxNoOfTables)" type = "unsigned" default = "0" min = "0" max = "4294967039" /&gt;
    &lt;param name = "MaxNoOfSubscribers" comment = "Max no of subscribers (default 0 == 2 * MaxNoOfTables)" type = "unsigned" default = "0" min = "0" max = "4294967039" /&gt;...&lt;/ section&gt;...&lt;/ configvariables&gt;
</code></pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Normally, the XML output produced by <code>ndb_config</code> <code>&#8211;configinfo</code> <code>&#8211;xml</code> is formatted using one line per element; we have added extra whitespace in the previous example, as well as the next one, for reasons of legibility. This should not make any difference to applications using this output, since most XML processors either ignore nonessential whitespace as a matter of course, or can be instructed to do so. </p>
</dl>
<p> Beginning with MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10, the XML output also indicates when changing a given parameter requires that nodes be restarted using the <code>&#8211;initial</code> option. This is shown by the presence of an initial=&quot;true&quot; attribute in the corresponding &lt;param&gt; element. In addition (also beginning with MySQL Cluster NDB 6.3.29 and MySQL Cluster NDB 7.0.10), the restart type (system or node) is also shown; if a given parameter requires a system restart, this is indicated by the presence of a restart=&quot;system&quot; attribute in the corresponding &lt;param&gt; element. For example, the Diskless parameter requires a system initial restart, as shown here (with the restart and initial attributes highlighted for visibility): </p>
<dl>
<dt>
<dd>
<pre>
&lt;param name=&quot;Diskless&quot; comment=&quot;Run wo/ disk&quot; type=&quot;bool&quot; default=&quot;false&quot; 
          <i>restart=&quot;system&quot; initial=&quot;true&quot;</i>/&gt;
</pre>
</dl>
<p> Currently, no initial attribute is included in the XML output for &lt;param&gt; elements corresponding to parameters which do not require initial restarts; in other words, initial=&quot;false&quot; is the default, and the value false should be assumed if the attribute is not present. Similarly, the default restart type is node (that is, an online or lqrollingrq restart of the cluster), but the restart attribute is included only if the restart type is system (meaning that all cluster nodes must be shut down at the same time, then restarted). </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font><br />
 The <code>&#8211;xml</code> option can be used only with the <code>&#8211;configinfo</code> option. Using <code>&#8211;xml</code> without <code>&#8211;configinfo</code> fails with an error. </p>
</dl>
<p> Unlike the options used with this program to obtain current configuration data, <code>&#8211;configinfo</code> and <code>&#8211;xml</code> use information obtained from the MySQL Cluster sources when <code>ndb_config</code> was compiled. For this reason, no connection to a running MySQL Cluster or access to a config.ini or my.cnf file is required for these two options. </p>
<p> Combining other <code>ndb_config</code> options (such as <code>&#8211;query</code> or <code>&#8211;type</code>) with <code>&#8211;configinfo</code> or <code>&#8211;xml</code> is not supported. If you attempt to do so, the usual (current) result is that all other options besides <code>&#8211;configinfo</code> or <code>&#8211;xml</code> are simply ignored. However, this behavior is not guaranteed and is subject to change at any time. In addition, since <code>ndb_config</code> when used with the <code>&#8211;configinfo</code> option does not access the MySQL Cluster or read any files, trying to specify additional options such as <code>&#8211;ndb-connectstring</code> or <code>&#8211;config-file</code> with <code>&#8211;configinfo</code> serves no purpose.</dl>
<p> <code>Examples</code>: </p>
<dl>
<dt>
<dd> 1. To obtain the node ID and type of each node in the cluster: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>./ndb_config --query=id,type --fields=':' --rows='
'</code>
1:ndbd
2:ndbd
3:ndbd
4:ndbd
5:ndb_mgmd
6:mysqld
7:mysqld
8:mysqld
9:mysqld
</pre>
</dl>
<p> In this example, we used the <code>&#8211;fields</code> options to separate the ID and type of each node with a colon character (:), and the <code>&#8211;rows</code> options to place the values for each node on a new line in the output.</dl>
<dl>
<dt>
<dd> 2. To produce a connectstring that can be used by data, SQL, and API nodes to connect to the management server: </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt;./ ndb_config-- config - file = usr / local / mysql / cluster - data / config.ini-- query = hostname, portnumber-- fields = : --rows =, --type = ndb_mgmd 192.168.0.179 : 1186
</code></pre>
</dl>
</dl>
<dl>
<dt>
<dd> 3. This invocation of <code>ndb_config</code> checks only data nodes (using the <code>&#8211;type</code> option), and shows the values for each node&#8217;s ID and host name, and its DataMemory, IndexMemory, and DataDir parameters: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>./ndb_config --type=ndbd --query=id,host,datamemory,indexmemory,datadir -f ' : ' -r '
'</code>
1 : 192.168.0.193 : 83886080 : 18874368 : /usr/local/mysql/cluster-data
2 : 192.168.0.112 : 83886080 : 18874368 : /usr/local/mysql/cluster-data
3 : 192.168.0.176 : 83886080 : 18874368 : /usr/local/mysql/cluster-data
4 : 192.168.0.119 : 83886080 : 18874368 : /usr/local/mysql/cluster-data
</pre>
</dl>
<p> In this example, we used the short options <code>-f</code> and <code>-r</code> for setting the field delimiter and row separator, respectively.</dl>
<dl>
<dt>
<dd> 4. To exclude results from any host except one in particular, use the <code>&#8211;host</code> option: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>./ndb_config --host=192.168.0.176 -f : -r '
' -q id,type</code>
3:ndbd
5:ndb_mgmd
</pre>
</dl>
<p> In this example, we also used the short form <code>-q</code> to determine the attributes to be queried. </p>
<p> Similarly, you can limit results to a node with a specific ID using the <code>&#8211;id</code> or <code>&#8211;nodeid</code> option.</dl>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2010, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
