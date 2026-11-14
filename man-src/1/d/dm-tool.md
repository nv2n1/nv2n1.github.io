---
title: "dm-tool(1)"
name: "dm-tool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dm-tool/"
description: "dm-tool – a tool to control the display manager"
---

<h2>NAME</h2>
<p> dm-tool &#8211; a tool to control the display manager</p>
<h2>SYNOPSIS</h2>
<p> <code>dm-tool</code> [ <i>OPTIONS</i> ] <i>COMMAND</i> [ <i>ARGS</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>dm-tool</code> is a tool to communicate with the LightDM display manager.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;version</code></p>
<dd> Show release version</p>
<dt><code>&#8211;session-bus</code></p>
<dd> Attempt to connect to the display manager using the session bus. This is useful if you are running a display manager in a test mode. If this option is not present dm-tool will connect using the system bus.</p>
<dt>The following commands are available:</p>
<dd>
<dt><code>switch-to-greeter</code></p>
<dd> Switch to the greeter suitable for logging into a new session.</p>
<dt><code>switch-to-user USERNAME [SESSION]</code></p>
<dd> Switch to a user session. If this user is already logged in then the display manager will switch to that session, otherwise a new session is started. If authentication is required a greeter will start to collect this. If the session option is provided then this session type will be used, otherwise the default for this user is used.</p>
<dt><code>switch-to-guest [SESSION]</code></p>
<dd> Switch to a guest session. If the guest session is already active the display manager will switch to that session, otherwise the guest session is started. If the session option is provided then this session type will be used, otherwise the default for the guest user is used.</p>
<dt><code>lock</code></p>
<dd> Lock the current seat. This will switch to a greeter with a hint that the screen is locked. You can return to this session by authenticating in the greeter.</p>
<dt><code>list-seats</code></p>
<dd> List the active seats and sessions that are running.</p>
<dt><code>add-nested-seat</code></p>
<dd> Start an X server inside a session and connect it to a display manager.</p>
<dt><code>add-local-x-seat DISPLAY_NUMBER</code></p>
<dd> Connect an existing X server to the display manager.</p>
<dt><code>add-seat TYPE [NAME=VALUE&#8230;]</code></p>
<dd> Add a dynamic seat.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lightdm/">lightdm</a></code>(1) </p>
<h2>Index</h2>
