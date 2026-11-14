---
title: "ilmid(8)"
name: "ilmid"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ilmid/"
description: "ilmid – Integrated Local Management Interface Daemon"
---

<p>ilmid &#8211; Integrated Local Management Interface Daemon</p>
<h2>Synopsis</h2>
<p><code>ilmid</code> [ <code>-b</code> ] [ <code>-d</code> ] [ <code>-v</code> ] [ <code>-l&nbsp;<wbr></code><i>logfile</i> ] [ <code>-x</code> ] [ <code>-q&nbsp;<wbr></code><i>qos</i> ] [ <code>-i&nbsp;<wbr></code><i>local_ip</i> ] [ <code>-u&nbsp;<wbr></code><i>uni</i> ] &lt;interface&gt;</p>
<h2>Parameters</h2>
<dl>
<dt><code>-b</code></p>
<dd>Puts the process in the background.</p>
<dt><code>-d</code></p>
<dd>Turn on debugging output.</p>
<dt><code>-v</code></p>
<dd>Verbose.</p>
<dt><code>-l&nbsp;<wbr></code><i>logfile</i></p>
<dd>Set the location of the log file.</p>
<dt><code>-x</code></p>
<dd>No var bindings?</p>
<dt><code>-q&nbsp;<wbr></code><i>qos</i></p>
<dd>Set the qos parameters to use on the ilmi VC.</p>
<dt><code>-i&nbsp;<wbr></code><i>local_ip</i></p>
<dd>the address that should be used by the switch for network management.</p>
<dt><code>-u&nbsp;<wbr></code><i>uni</i></p>
<dd>uni version. This can be 3.0, 3.1 or 4.0.</dl>
<h2>Description</h2>
<p>ilmid implements SNMP on an ATM PVC. It is used to negotiate operating parameters with a switch.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-atmsigd/">atmsigd</a></code>(8) </p>
