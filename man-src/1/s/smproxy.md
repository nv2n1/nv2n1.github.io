---
title: "smproxy(1)"
name: "smproxy"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smproxy/"
description: "smproxy – Session Manager Proxy"
---

<h2 class="name">NAME</h2>
<p> smproxy &#8211; Session Manager Proxy </p>
<h2>SYNOPSIS</h2>
<p> <code>smproxy</code> [-clientId id] [-restore saveFile] [-version]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-clientId </code><i>id</i></p>
<dd> Specifies the session ID used by <i>smproxy</i> in the previous session.</p>
<dt><code>-restore </code><i>saveFile</i></p>
<dd> Specifies the file used by <i>smproxy</i> to save state in the previous session.</p>
<dt><code>-version</code></p>
<dd> Prints the program version and exits.</dl>
<h2>DESCRIPTION</h2>
<p> <i>smproxy</i> allows X applications that do not support X11R6 session management to participate in an X11R6 session. </p>
<p> In order for <i>smproxy</i> to act as a proxy for an X application, one of the following must be true: </p>
<p> &#8211; The application maps a top level window containing the <code>WM_CLIENT_LEADER</code> property. This property provides a pointer to the client leader window which contains the <code>WM_CLASS</code>, <code>WM_NAME</code>, <code>WM_COMMAND</code>, and <code>WM_CLIENT_MACHINE</code> properties. </p>
<p> or &#8230; </p>
<p> &#8211; The application maps a top level window which does not contain the <code>WM_CLIENT_LEADER</code> property. However, this top level window contains the <code>WM_CLASS</code>, <code>WM_NAME</code>, <code>WM_COMMAND</code>, and <code>WM_CLIENT_MACHINE</code> properties. </p>
<p> An application that support the <code>WM_SAVE_YOURSELF</code> protocol will receive a <code>WM_SAVE_YOURSELF</code> client message each time the session manager issues a checkpoint or shutdown. This allows the application to save state. If an application does not support the <code>WM_SAVE_YOURSELF</code> protocol, then the proxy will provide enough information to the session manager to restart the application (using <code>WM_COMMAND</code>), but no state will be restored.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xsm/">xsm</a>(1)</p>
<h2>AUTHOR</h2>
<p> Ralph Mor, X Consortium </p>
<h2>Index</h2>
