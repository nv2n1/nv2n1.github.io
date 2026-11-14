---
title: "pbsnodes(8)"
name: "pbsnodes"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbsnodes/"
description: "pbsnodes – pbs node manipulation"
---

<p>pbsnodes &#8211; pbs node manipulation</p>
<h2>Synopsis</h2>
<p>pbsnodes [-{a|x}] [-q] [-s server] [node|:property]<br />
 pbsnodes -l [-q] [-s server] [state] [nodename|:property &#8230;]<br />
 pbsnodes [-{c|d|o|r}] [-q] [-s server] [-n] [-N &quot;note&quot;] [node|:property] </p>
<h2>Description</h2>
<p>The <code>pbsnodes</code> command is used to mark nodes down, free or offline. It can also be used to list nodes and their state. Node information is obtained by sending a request to the PBS job server. Sets of nodes can be operated on at once by specifying a node property prefixed by a colon.<br />
 Nodes do not exist in a single state, but actually have a set of states. For example, a node can be simultaneously &quot;busy&quot; and &quot;offline&quot;. The &quot;free&quot; state is the absence of all other states and so is never combined with other states. </p>
<p> In order to execute pbsnodes with other than the <code>-a</code> or <code>-l</code> options, the user must have PBS Manager or Operator privilege.</p>
<h2>Options</h2>
<dl>
<dt>-a</p>
<dd>All attributes of a node or all nodes are listed. This is the default if no flag is given.</p>
<dt>-x</p>
<dd>Same as -a, but the output has an XML-like format.</p>
<dt>-c</p>
<dd>Clear OFFLINE from listed nodes.</p>
<dt>-d</p>
<dd>Print MOM diagnosis on the listed nodes. Not yet implemented. Use momctl instead.</p>
<dt>-o</p>
<dd>Add the OFFLINE state. This is different from being marked DOWN. OFFLINE prevents new jobs from running on the specified nodes. This gives the administrator a tool to hold a node out of service without changing anything else. The OFFLINE state will never be set or cleared automatically by pbs_server; it is purely for the manager or operator.</p>
<dt>-p</p>
<dd>Purge the node record from pbs_server. Not yet implemented.</p>
<dt>-r</p>
<dd>Reset the listed nodes by clearing OFFLINE and adding DOWN state. pbs_server will ping the node and, if they communicate correctly, free the node.</p>
<dt>-l</p>
<dd>List node names and their state. If no state is specified, only nodes in the DOWN, OFFLINE, or UNKNOWN states are listed. Specifying a state string acts as an output filter. Valid state strings are &quot;free&quot;, &quot;offline&quot;, &quot;down&quot;, &quot;reserve&quot;, &quot;job-exclusive&quot;, &quot;job-sharing&quot;, &quot;busy&quot;, &quot;time-shared&quot;, or &quot;state-unknown&quot;.</p>
<dt>-N</p>
<dd>Specify a &quot;note&quot; attribute. This allows an administrator to add an arbitrary annotation to the listed nodes. To clear a note, use -N &quot;&quot; or -N n.</p>
<dt>-n</p>
<dd>Show the &quot;note&quot; attribute for nodes that are DOWN, OFFLINE, or UNKNOWN. This option requires -l.</p>
<dt>-q</p>
<dd>Supress all error messages.</p>
<dt>-s</p>
<dd>Specify the PBS server&#8217;s hostname or IP address.</dl>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B) and the PBS External Reference Specification </p>
