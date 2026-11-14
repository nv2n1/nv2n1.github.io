---
title: "onnode(1)"
name: "onnode"
section: "1"
letter: "o"
url: "/docs/linux/man/1-onnode/"
description: "onnode – run commands on CTDB cluster nodes"
---

<h2 class="name">NAME</h2>
<p> onnode &#8211; run commands on CTDB cluster nodes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>onnode</code> [<i>OPTION</i>&#8230;] {<i>NODES</i>} {<i>COMMAND</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>onnode is a utility to run commands on a specific node of a CTDB cluster, or on all nodes. </p>
<p> <i>NODES</i> specifies which node(s) to run a command on. See section NODES SPECIFICATION for details. </p>
<p> <i>COMMAND</i> can be any shell command. The onnode utility uses ssh or rsh to connect to the remote nodes and run the command.</p>
<h2>OPTIONS</h2>
<p> -c</p>
<dl>
<dt>
<dd> Execute COMMAND in the current working directory on the specified nodes.</dl>
<p> -f <i>FILENAME</i></p>
<dl>
<dt>
<dd> Specify an alternative nodes FILENAME to use instead of the default. This option overrides the CTDB_NODES_FILE and CTDB_NODES variables. See the discussion of /etc/ctdb/nodes in the FILES section for more details.</dl>
<p> -i</p>
<dl>
<dt>
<dd> Keep standard input open, allowing data to be piped to onnode. Normally onnode closes stdin to avoid surprises when scripting. Note that this option is ignored when using <code>-p</code> or if <code>SSH</code> is set to anything other than &quot;ssh&quot;.</dl>
<p> -n</p>
<dl>
<dt>
<dd> Allow nodes to be specified by name rather than node numbers. These nodes don&#8217;t need to be listed in the nodes file. You can avoid the nodes file entirely by combining this with -f /dev/null.</dl>
<p> -o <i>PREFIX</i></p>
<dl>
<dt>
<dd> Causes standard output from each node to be saved into a file with name PREFIX.<i>IP</i>.</dl>
<p> -p</p>
<dl>
<dt>
<dd> Run COMMAND in parallel on the specified nodes. The default is to run COMMAND sequentially on each node.</dl>
<p> -P</p>
<dl>
<dt>
<dd> Push files to nodes. Names of files to push are specified rather than the usual command. Quoting is fragile/broken &#8211; filenames with whitespace in them are not supported.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Do not print node addresses. Normally, onnode prints informational node addresses if more than one node is specified. This overrides -v.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Print node addresses even if only one node is specified. Normally, onnode prints informational node addresses when more than one node is specified.</dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Show a short usage guide.</dl>
<h2>NODES SPECIFICATION</h2>
<p> Nodes can be specified via numeric node numbers (from 0 to N-1) or mnemonics. Multiple nodes are specified using lists of nodes, separated by commas, and ranges of numeric node numbers, separated by dashes. If nodes are specified multiple times then the command will be executed multiple times on those nodes. The order of nodes is significant. </p>
<p> The following mnemonics are available: </p>
<p> all</p>
<dl>
<dt>
<dd> All nodes.</dl>
<p> any</p>
<dl>
<dt>
<dd> A node where ctdbd is running. This semi-random but there is a bias towards choosing a low numbered node.</dl>
<p> ok | healthy</p>
<dl>
<dt>
<dd> All nodes that are not disconnected, banned, disabled or unhealthy.</dl>
<p> con | connected</p>
<dl>
<dt>
<dd> All nodes that are not disconnected.</dl>
<p> lvs | lvsmaster</p>
<dl>
<dt>
<dd> The current LVS master.</dl>
<p> natgw | natgwlist</p>
<dl>
<dt>
<dd> The current NAT gateway.</dl>
<p> rm | recmaster</p>
<dl>
<dt>
<dd> The current recovery master.</dl>
<h2>EXAMPLES</h2>
<p> The following command would show the process ID of ctdbd on all nodes </p>
<dl>
<dt>
<dd>
<pre>
      onnode all ctdb getpid
    
</pre>
</dl>
<p> The following command would show the last 5 lines of log on each node, preceded by the node&#8217;s hostname </p>
<dl>
<dt>
<dd>
<pre>
      onnode all &quot;hostname; tail -5 /var/log/log.ctdb&quot;
    
</pre>
</dl>
<p> The following command would restart the ctdb service on all nodes, in parallel. </p>
<dl>
<dt>
<dd>
<pre>
      onnode -p all service ctdb restart
    
</pre>
</dl>
<p> The following command would run ./foo in the current working directory, in parallel, on nodes 0, 2, 3 and 4. </p>
<dl>
<dt>
<dd>
<pre>
      onnode -c -p 0,2-4 ./foo
    
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> <code>CTDB_BASE</code></p>
<dl>
<dt>
<dd> Directory containing CTDB configuration files. The default is /etc/ctdb.</dl>
<p> <code>CTDB_NODES_FILE</code></p>
<dl>
<dt>
<dd> Name of alternative nodes file to use instead of the default. See the FILES section for more details.</dl>
<h2>FILES</h2>
<p> /etc/ctdb/nodes</p>
<dl>
<dt>
<dd> Default file containing a list of each node&#8217;s IP address or hostname. </p>
<p> As above, a file specified via the <code>-f</code> or <code>CTDB_NODES_FILE</code> is given precedence. If a relative path is specified and no corresponding file exists relative to the current directory then the file is also searched for in the $CTDB_BASE directory. </p>
<p> If <code>CTDB_NODES_FILE</code> is not set and <code>CTDB_NODES</code> is set in configuration then the file pointed to by <code>CTDB_NODES</code> is used. </p>
<p> Otherwise the default is $CTDB_BASE/nodes, where <code>CTDB_BASE</code> defaults to /etc/ctdb.</dl>
<p> /etc/ctdb/onnode.conf</p>
<dl>
<dt>
<dd> If this file exists it is sourced by onnode. The main purpose is to allow the administrator to set <code>SSH</code> to something other than &quot;ssh&quot;. In this case the -t option is ignored. For example, the administrator may choose to use use rsh instead of ssh.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Andrew Tridgell, Martin Schwenke</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg<br />
 Copyright &#169; 2008 Martin Schwenke </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
