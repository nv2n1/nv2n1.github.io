---
title: "ndb_waiter(1)"
name: "ndb_waiter"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_waiter/"
description: "ndb_waiter – wait for MySQL Cluster to reach a given status"
---

<h2 class="name">NAME</h2>
<p> ndb_waiter &#8211; wait for MySQL Cluster to reach a given status </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_waiter </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_waiter</code></p>
<dd>repeatedly (each 100 milliseconds) prints out the status of all cluster data nodes until either the cluster reaches a given status or the <code>&#8211;timeout</code> limit is exceeded, then exits. By default, it waits for the cluster to achieve STARTED status, in which all nodes have started and connected to the cluster. This can be overridden using the <code>&#8211;no-contact</code> and <code>&#8211;not-started</code> options (see Additional Options). </p>
<p> The node states reported by this utility are as follows: </p>
<dl>
<dt>
<dd> * NO_CONTACT: The node cannot be contacted.</dl>
<dl>
<dt>
<dd> * UNKNOWN: The node can be contacted, but its status is not yet known. Usually, this means that the node has received a START or RESTART command from the management server, but has not yet acted on it.</dl>
<dl>
<dt>
<dd> * NOT_STARTED: The node has stopped, but remains in contact with the cluster. This is seen when restarting the node using the management client&#8217;s RESTART command.</dl>
<dl>
<dt>
<dd> * STARTING: The node&#8217;s <code>ndbd</code> process has started, but the node has not yet joined the cluster.</dl>
<dl>
<dt>
<dd> * STARTED: The node is operational, and has joined the cluster.</dl>
<dl>
<dt>
<dd> * SHUTTING_DOWN: The node is shutting down.</dl>
<dl>
<dt>
<dd> * SINGLE USER MODE: This is shown for all cluster data nodes when the cluster is in single user mode.</dl>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_waiter [-c <i>connect_string</i>]
</pre>
</dl>
<p> <code>Additional Options</code>: </p>
<dl>
<dt>
<dd> * <code>&#8211;no-contact</code>, <code>-n</code> </p>
<p> Instead of waiting for the STARTED state, <code>ndb_waiter</code> continues running until the cluster reaches NO_CONTACT status before exiting.</dl>
<dl>
<dt>
<dd> * <code>&#8211;not-started</code> </p>
<p> Instead of waiting for the STARTED state, <code>ndb_waiter</code> continues running until the cluster reaches NOT_STARTED status before exiting.</dl>
<dl>
<dt>
<dd> * <code>&#8211;timeout=</code><i>seconds</i>, <code>-t </code><i>seconds</i> </p>
<p> Time to wait. The program exits if the desired state is not achieved within this number of seconds. The default is 120 seconds (1200 reporting cycles).</dl>
<dl>
<dt>
<dd> * <code>&#8211;single-user</code> </p>
<p> The program waits for the cluster to enter single user mode.</dl>
<dl>
<dt>
<dd> * <code>&#8211;nowait-nodes=</code><i>list</i> </p>
<p> When this option is used, ndb_waiter does not wait for the nodes whose IDs are listed. The list is comma-delimited; ranges can be indicated by dashes, as shown here: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ndb_waiter --nowait-nodes=1,3,7-9</code>
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font><br />
 Do <i>not</i> use this option together with the <code>&#8211;wait-nodes</code> option. </p>
</dl>
<p> This option was added in MySQL Cluster NDB 6.2.1.</dl>
<dl>
<dt>
<dd> * <code>&#8211;wait-nodes=</code><i>list</i>, <code>-w </code><i>list</i> </p>
<p> When this option is used, <code>ndb_waiter</code> waits only for the nodes whose IDs are listed. The list is comma-delimited; ranges can be indicated by dashes, as shown here: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>ndb_waiter --wait-nodes=2,4-6,10</code>
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font><br />
 Do <i>not</i> use this option together with the <code>&#8211;nowait-nodes</code> option. </p>
</dl>
<p> This option was added in MySQL Cluster NDB 6.3.34, 7.0.15, and 7.1.4.</dl>
<p> <code>Sample Output</code>. Shown here is the output from <code>ndb_waiter</code> when run against a 4-node cluster in which two nodes have been shut down and then started again manually. Duplicate reports (indicated by lq&#8230;rq) are omitted. </p>
<dl>
<dt>
<dd>
<pre><code>
shell &gt;./ ndb_waiter - c localhost
                           Connecting to mgmsrv
                           at(localhost)
State node 1 STARTED
State node 2 NO_CONTACT
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 UNKNOWN
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 UNKNOWN
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 STARTING
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 STARTED
State node 3 STARTED
State node 4 STARTING
Waiting for cluster enter state STARTED
...
State node 1 STARTED
State node 2 STARTED
State node 3 STARTED
State node 4 STARTED
Waiting for cluster enter state STARTED
NDBT_ProgramExit: 0 - OK
</code></pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> If no connectstring is specified, then <code>ndb_waiter</code> tries to connect to a management on localhost, and reports Connecting to mgmsrv at (null). </p>
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
