---
title: "pmsignal(1)"
name: "pmsignal"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmsignal/"
description: "pmsignal – send a signal to one or more processes"
---

<h2>NAME</h2>
<p> <code>pmsignal</code> &#8211; send a signal to one or more processes</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmsignal</code> [<code>-alnp</code>] [<code>-s</code> <i>signal</i>] [<i>PID</i> &#8230;|<i>name</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmsignal</code> provides a cross-platform event signalling mechanism for use with tools from the Performance Co-Pilot toolkit. It can be used to send a named <i>signal</i> (only HUP, USR1, TERM, and KILL are accepted) to one or more processes. </p>
<p> The processes are specified directly using PIDs or as program names (with either the <code>-a</code>/<code>&#8211;all</code> or <code>-p</code>/<code>&#8211;program</code> options). In the <code>all</code> case, the set of all running processes is searched for a <code><a href="/docs/linux/man/1-basename/">basename</a></code>(1) match on <i>name</i>. In the <code>program</code> case, process identifiers are extracted from files in the $PCP_RUN_DIR directrory where file names are matched on <i>name</i>.pid. </p>
<p> The <code>-n</code>/<code>&#8211;dry-run</code> option reports the list of process identifiers that would have been signalled, but no signals are actually sent. </p>
<p> If a <i>signal</i> is not specified, then the TERM signal will be sent. The list of supported signals is reported when using the <code>-l</code>/<code>&#8211;list</code> option. </p>
<p> On Linux and UNIX platforms, <i>pmsignal</i> is a simple wrapper around the <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1) command. On Windows, the is no direct equivalent to this mechanism, and so an alternate mechanism has been implemented &#8211; this is only honoured by PCP tools, however, not all Windows utilities.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-basename/">basename</a></code>(1), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
