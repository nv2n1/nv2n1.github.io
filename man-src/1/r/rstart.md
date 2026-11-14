---
title: "rstart(1)"
name: "rstart"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rstart/"
description: "rstart – a sample implementation of a Remote Start client"
---

<h2 class="name">NAME</h2>
<p> rstart &#8211; a sample implementation of a Remote Start client </p>
<h2>SYNOPSIS</h2>
<p> <code>rstart</code> [-c <i>context</i>] [-g] [-l <i>username</i>] [-v] <i>hostname</i> <i>command args &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Rstart</i> is a simple implementation of a Remote Start client as defined in &quot;A Flexible Remote Execution Protocol Based on <code>rsh</code>&quot;. It uses <i>rsh</i> as its underlying remote execution mechanism.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>context</i></p>
<dd> This option specifies the <i>context</i> in which the command is to be run. A <i>context</i> specifies a general environment the program is to be run in. The details of this environment are host-specific; the intent is that the client need not know how the environment must be configured. If omitted, the context defaults to <code>X</code>. This should be suitable for running X programs from the host&#8217;s &quot;usual&quot; X installation.</p>
<dt><code>-g</code></p>
<dd> Interprets <i>command</i> as a <i>generic command</i>, as discussed in the protocol document. This is intended to allow common applications to be invoked without knowing what they are called on the remote system. Currently, the only generic commands defined are <code>Terminal</code>, <code>LoadMonitor</code>, <code>ListContexts</code>, and <code>ListGenericCommands</code>.</p>
<dt><code>-l </code><i>username</i></p>
<dd> This option is passed to the underlying <i>rsh</i>; it requests that the command be run as the specified user.</p>
<dt><code>-v</code></p>
<dd> This option requests that <i>rstart</i> be verbose in its operation. Without this option, <i>rstart</i> discards output from the remote&#8217;s <i>rstart</i> helper, and directs the <i>rstart</i> helper to detach the program from the <i>rsh</i> connection used to start it. With this option, responses from the helper are displayed and the resulting program is not detached from the connection.</dl>
<h2>NOTES</h2>
<p> This is a trivial implementation. Far more sophisticated implementations are possible and should be developed. </p>
<p> Error handling is nonexistent. Without <code>-v</code>, error reports from the remote are discarded silently. With <code>-v</code>, error reports are displayed. </p>
<p> The $DISPLAY environment variable is passed. If it starts with a colon, the local hostname is prepended. The local domain name should be appended to unqualified host names, but isn&#8217;t. </p>
<p> The $SESSION_MANAGER environment variable should be passed, but isn&#8217;t. </p>
<p> X11 authority information is passed for the current display. </p>
<p> ICE authority information should be passed, but isn&#8217;t. It isn&#8217;t completely clear how <i>rstart</i> should select what ICE authority information to pass. </p>
<p> Even without <code>-v</code>, the sample <i>rstart</i> helper will leave a shell waiting for the program to complete. This causes no real harm and consumes relatively few resources, but if it is undesirable it can be avoided by explicitly specifying the &quot;exec&quot; command to the shell, eg </p>
<pre>
rstart somehost exec xterm
</pre>
<p> This is obviously dependent on the command interpreter being used on the remote system; the example given will work for the Bourne and C shells.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rstartd/">rstartd</a>(1), <a href="/docs/linux/man/1-rsh/">rsh</a>(1), A Flexible Remote Execution Protocol Based on <code>rsh</code></p>
<h2>AUTHOR</h2>
<p> Jordan Brown, Quarterdeck Office Systems </p>
<h2>Index</h2>
