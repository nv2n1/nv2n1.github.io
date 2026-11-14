---
title: "pmpost(1)"
name: "pmpost"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmpost/"
description: "pmpost – append messages to the Performance Co-Pilot notice board"
---

<h2>NAME</h2>
<p> <code>pmpost</code> &#8211; append messages to the Performance Co-Pilot notice board</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmpost</code> <i>message</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmpost</code> will append the text <i>message</i> to the end of the Performance Co-Pilot (PCP) notice board file (<code>$PCP_LOG_DIR/NOTICES</code>) in an atomic manner that guards against corruption of the notice board file by concurrent invocations of <code>pmpost</code>. </p>
<p> The PCP notice board is intended to be a persistent store and clearing house for important messages relating to the operation of the PCP and the notification of performance alerts from <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) when other notification options are either unavailable or unsuitable. </p>
<p> Before being written, messages are prefixed by the current time, and when the current day is different to the last time the notice board file was written, <code>pmpost</code> will prepend the message with the full date. </p>
<p> If the notice board file does not exist, <code>pmpost</code> will create it. <code>pmpost</code> would usually run from long-running PCP daemons executing under the (typically unprivileged) <code>$PCP_USER</code> and <code>$PCP_GROUP</code> accounts. The file should be owned by root, and group writable by the <code>$PCP_GROUP</code> group.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_LOG_DIR/NOTICES</code></p>
<dd> the PCP notice board file</dl>
<h2>PCP ENVIRONMENT</h2>
<p> The file <code>/etc/pcp.conf</code> contains the local values for PCP_ variables.</p>
<h2>UNIX SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1).</p>
<h2>WINDOWS SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp-eventlog/">pcp-eventlog</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
