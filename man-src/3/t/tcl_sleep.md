---
title: "tcl_sleep(3)"
name: "tcl_sleep"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_sleep/"
description: "Tcl_Sleep – delay execution for a given number of milliseconds"
---

<p>Tcl_Sleep &#8211; delay execution for a given number of milliseconds </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_Sleep</code>(<i>ms</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>ms</i> (in) Number of milliseconds to sleep.
</dl>
<h2>Description</h2>
<p>This procedure delays the calling process by the number of milliseconds given by the <i>ms</i> parameter and returns after that time has elapsed. It is typically used for things like flashing a button, where the delay is short and the application need not do anything while it waits. For longer delays where the application needs to respond to other events during the delay, the procedure <code>Tcl_CreateTimerHandler</code> should be used instead of <code>Tcl_Sleep</code>.</p>
<h2>Keywords</h2>
<p>sleep, time, wait</p>
