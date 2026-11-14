---
title: "dlm_tool(8)"
name: "dlm_tool"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dlm_tool/"
description: "dlm_tool – a utility for the dlm and dlm_controld daemon"
---

<p>dlm_tool &#8211; a utility for the dlm and dlm_controld daemon</p>
<h2>Synopsis</h2>
<p><code>dlm_tool</code> [COMMAND] [OPTIONS] [ <i>name</i> ] </p>
<h2>Commands</h2>
<p><code>ls</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Display dlm_controld internal lockspace state.</p>
<p> <code>status</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Dump dlm_controld daemon state.</p>
<p> <code>dump</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Dump dlm_controld debug buffer.</p>
<p> <code>dump_config</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Dump dlm_controld config settings.</p>
<p> <code>fence_ack</code><i> nodeid</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Quit trying to fence a node.</p>
<p> <code>log_plock</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Dump dlm_controld plock debug buffer.</p>
<p> <code>plocks</code><i> name</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Dump posix locks from dlm_controld for the lockspace.</p>
<p> <code>join</code><i> name</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Join a lockspace.</p>
<p> <code>leave</code><i> name</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Leave a lockspace.</p>
<p> <code>lockdebug</code><i> name</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Complete display of locks from the lockspace.</p>
<p> <code>lockdump</code><i> name</i><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Minimal display of locks from the lockspace (deprecated).</p>
<h2>Options</h2>
<p><code>-n</code> Show all node information in ls. </p>
<p> <code>-d</code> 0|1 Resource directory off/on in join, default 0 </p>
<p> <code>-e</code> 0|1 Exclusive create off/on in join, default 0 </p>
<p> <code>-f</code> 0|1 FS (filesystem) flag off/on in join, default 0 </p>
<p> <code>-m</code><i> mode</i> Permission mode for lockspace device (octal), default 0600 </p>
<p> <code>-s</code> Summary following lockdebug output (experiemental) </p>
<p> <code>-v</code> Verbose lockdebug output </p>
<p> <code>-w</code> Wide lockdebug output </p>
<p> <code>-M</code> Include MSTCPY locks in lockdump output </p>
<p> <code>-h</code> Print help, then exit </p>
<p> <code>-V</code> Print program version information, then exit</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a></code>(5) </p>
