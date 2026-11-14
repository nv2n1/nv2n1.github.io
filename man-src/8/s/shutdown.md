---
title: "shutdown(8)"
name: "shutdown"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shutdown/"
description: "shutdown – Halt, power-off or reboot the machine"
---

<p>shutdown &#8211; Halt, power-off or reboot the machine</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>shutdown</code> [OPTIONS&#8230;] [TIME] [WALL&#8230;]</dl>
<h2>Description</h2>
<p><code>shutdown</code></p>
<dd>may be used to halt, power-off or reboot the machine. </p>
<p> The first argument may be a time string (which is usually &quot;now&quot;). Optionally, this may be followed by a wall message to be sent to all logged-in users before going down. </p>
<p> The time string may either be in the format &quot;hh:mm&quot; for hour/minutes specifying the time to execute the shutdown at, specified in 24h clock format. Alternatively it may be in the syntax &quot;+m&quot; referring to the specified number of minutes m from now. &quot;now&quot; is an alias for &quot;+0&quot;, i.e. for triggering an immediate shutdown. If no time argument is specified, &quot;+1&quot; is implied. </p>
<p> Note that to specify a wall message you must specify a time argument, too. </p>
<p> If the time argument is used, 5 minutes before the system goes down the /run/nologin file is created to ensure that further logins shall not be allowed.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>-H</code>, <code>&#8211;halt</code></p>
<dl>
<dd>Halt the machine.</dl>
<p> <code>-P</code>, <code>&#8211;poweroff</code></p>
<dl>
<dd>Power-off the machine (the default).</dl>
<p> <code>-r</code>, <code>&#8211;reboot</code></p>
<dl>
<dd>Reboot the machine.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Equivalent to <code>&#8211;poweroff</code>, unless <code>&#8211;halt</code> is specified.</dl>
<p> <code>-k</code></p>
<dl>
<dd>Do not halt, power-off, reboot, just write wall message.</dl>
<p> <code>&#8211;no-wall</code></p>
<dl>
<dd>Do not send wall message before halt, power-off, reboot.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Cancel a pending shutdown. This may be used to cancel the effect of an invocation of <code>shutdown</code> with a time argument that is not &quot;+0&quot; or &quot;now&quot;.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1) </p>
