---
title: "grmid(1)"
name: "grmid"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grmid/"
description: "grmid – – RMI activation system daemon"
---

<h2 class="name">NAME</h2>
<p> grmid &#8211; &#8211; RMI activation system daemon </p>
<h2>SYNOPSIS</h2>
<p> grmid [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>rmiregistry</code> starts a remote object registry on the current host. If no port number is specified, then port 1099 is used.</p>
<h2>OPTIONS</h2>
<p> Activation process control:</p>
<dl>
<dt><code>-port</code> <i></i><font SIZE="-1"><i>PORT</i></font><i></i></p>
<dd> Port on which activation system is to be started.</p>
<dt><code>-restart</code></p>
<dd> Restart activation system, clearing persistent naming database, if any.</p>
<dt><code>-stop</code></p>
<dd> Stop activation system.</dl>
<p> Persistence:</p>
<dl>
<dt><code>-persistent</code></p>
<dd> Make activation system persistent.</p>
<dt><code>-directory</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Directory in which to store persistent data.</dl>
<p> Debugging:</p>
<dl>
<dt><code>-verbose</code></p>
<dd> Log binding events to standard out.</dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></p>
<dd> Print help text, then exit.</p>
<dt><code>-version</code></p>
<dd> Print version number, then exit.</p>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></p>
<dd> Pass argument to the Java runtime.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-java/">java</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
<h2>Index</h2>
