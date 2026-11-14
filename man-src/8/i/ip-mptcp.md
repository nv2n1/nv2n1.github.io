---
title: "ip-mptcp(8)"
name: "ip-mptcp"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-mptcp/"
description: "ip-mptcp – MPTCP path manager configuration"
---

<p>ip-mptcp &#8211; MPTCP path manager configuration</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

mptcp

{

    endpoint

    |

    limits

    |

    help

}
</code></pre>
<p> <code>ip mptcp endpoint add </code> <i>IFADDR</i> [ <code>port</code> <i>PORT</i> ] [ <code>dev</code> <i>IFNAME</i> ] [ <code>id</code> <i>ID</i> ] [ <i>FLAG-LIST</i> ]<br />
 <code>ip mptcp endpoint del id </code> <i>ID</i><br />
 <code>ip mptcp endpoint show </code> [ <code>id</code> <i>ID</i> ]<br />
 <code>ip mptcp endpoint flush</code> </p>
<pre><code>FLAG-LIST := [ FLAG-LIST ] FLAG
FLAG := [

signal

|

subflow

|

backup

]</code></pre>
<p> <code>ip mptcp limits set </code> [ <code>subflow</code> <i>SUBFLOW_NR</i> ] [ <code>add_addr_accepted</code> <i>ADD_ADDR_ACCEPTED_NR</i> ]<br />
 <code>ip mptcp limits show</code><br />
 <code>ip mptcp monitor</code> </p>
<h2>Description</h2>
<p>MPTCP is a transport protocol built on top of TCP that allows TCP connections to use multiple paths to maximize resource usage and increase redundancy. The ip-mptcp sub-commands allow configuring several aspects of the MPTCP path manager, which is in charge of subflows creation: The <code>endpoint</code> object specifies the IP addresses that will be used and/or announced for additional subflows: </p>
<table>
<tr VALIGN=top>
<td>ip mptcp endpoint add</td>
<td>add new MPTCP endpoint
</td>
</tr>
<tr VALIGN=top>
<td>ip mptcp endpoint delete</td>
<td>delete existing MPTCP endpoint
</td>
</tr>
<tr VALIGN=top>
<td>ip mptcp endpoint show</td>
<td>get existing MPTCP endpoint
</td>
</tr>
<tr VALIGN=top>
<td>ip mptcp endpoint flush</td>
<td>flush all existing MPTCP endpoints
</td>
</tr>
</table>
<dl>
<dt><i>PORT</i></p>
<dd>When a port number is specified, incoming MPTCP subflows for already established MPTCP sockets will be accepted on the specified port, regardless the original listener port accepting the first MPTCP subflow and/or this peer being actually on the client side. <i>ID</i> is a unique numeric identifier for the given endpoint</p>
<dt><code>signal</code></p>
<dd>the endpoint will be announced/signalled to each peer via an ADD_ADDR MPTCP sub-option</p>
<dt><code>subflow</code></p>
<dd>if additional subflow creation is allowed by MPTCP limits, the endpoint will be used as the source address to create an additional subflow after that the MPTCP connection is established.</p>
<dt><code>backup</code></p>
<dd>the endpoint will be announced as a backup address, if this is a <code>signal</code> endpoint, or the subflow will be created as a backup one if this is a <code>subflow</code> endpoint  The <code>limits</code> object specifies the constraints for subflow creations: </p>
<table>
<tr VALIGN=top>
<td>ip mptcp limits show</td>
<td>get current MPTCP subflow creation limits
</td>
</tr>
<tr VALIGN=top>
<td>ip mptcp limits set</td>
<td>change the MPTCP subflow creation limits
</td>
</tr>
</table>
<dl>
<dt><i>SUBFLOW_NR</i></p>
<dd>specifies the maximum number of additional subflows allowed for each MPTCP connection. Additional subflows can be created due to: incoming accepted ADD_ADDR option, local <code>subflow</code> endpoints, additional subflows started by the peer.</p>
<dt><i>ADD_ADDR_ACCEPTED_NR</i></p>
<dd>specifies the maximum number of ADD_ADDR suboptions accepted for each MPTCP connection. The MPTCP path manager will try to create a new subflow for each accepted ADD_ADDR option, respecting the <i>SUBFLOW_NR</i> limit.  <code>monitor</code> displays creation and deletion of MPTCP connections as well as addition or removal of remote addresses and subflows. </p>
<h2>Author</h2>
<p>Original Manpage by Paolo Abeni &lt;pabeni [at] redhat.com&gt;</p>
