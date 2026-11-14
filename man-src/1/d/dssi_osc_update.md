---
title: "dssi_osc_update(1)"
name: "dssi_osc_update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dssi_osc_update/"
description: "dssi_osc_update – send a DSSI `update’ OSC request"
---

<h2 class="name">NAME</h2>
<p> dssi_osc_update &#8211; send a DSSI `update&#8217; OSC request </p>
<h2>SYNOPSIS</h2>
<p> <code>dssi_osc_update</code> <i>&lt;OSC URL&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dssi_osc_update</code> sends a DSSI `update&#8217; OSC request to a DSSI host, then waits for OSC responses from the host, writes any responses received to stdout, and exits when it has not received anything for five seconds. DSSI hosts should respond to an `update&#8217; request by sending the complete state of the plugin; this program can be used to retrieve and display that state.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&lt;OSC URL&gt;</code></p>
<dd> The URL specifying the host and plugin, to which the request is sent. This is typically obtained from the host, perhaps from startup messages or the host&#8217;s `About&#8217; dialog. For example:<br />
&nbsp;<wbr>&nbsp;<wbr>osc.<a href="udp://localhost:19383/dssi/test.1">udp://localhost:19383/dssi/test.1</a><br />
&nbsp;<wbr>&nbsp;<wbr>osc.<a href="udp://my.host.org:10886/dssi/xsynth-dssi/Xsynth/chan00">udp://my.host.org:10886/dssi/xsynth-dssi/Xsynth/chan00</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dssi_osc_send/">dssi_osc_send</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was originally created by Mark Hymers from the help text of the application, for the Debian project (but may be freely used by others). </p>
<h2>Index</h2>
