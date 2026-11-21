---

title: "grmiregistry(1)"
name: "grmiregistry"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grmiregistry/"
description: "grmiregistry – – Remote object registry"
---

<p> grmiregistry &#8211; &#8211; Remote object registry </p>
<h2>SYNOPSIS</h2>
<p> grmiregistry [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>PORT</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> <code>grmiregistry</code> starts a remote object registry on the current host. If no port number is specified, then port 1099 is used.</p>
<h2>OPTIONS</h2>
<p> Registry process control:</p>
<dl>
<dt><code>-restart</code></dt>
<dd> Restart <font SIZE="-1">RMI</font> naming service, clearing persistent naming database, if any.</dd>
<dt><code>-stop</code></dt>
<dd> Stop <font SIZE="-1">RMI</font> naming service.</dd></dl>
<p> Persistence:</p>
<dl>
<dt><code>-persistent</code></dt>
<dd> Make <font SIZE="-1">RMI</font> naming service persistent.</dd>
<dt><code>-directory</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></dt>
<dd> Directory in which to store persistent data.</dd></dl>
<p> Debugging:</p>
<dl>
<dt><code>-verbose</code></dt>
<dd> Log binding events to standard out.</dd></dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></dt>
<dd> Print help text, then exit.</dd>
<dt><code>-version</code></dt>
<dd> Print version number, then exit.</dd>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></dt>
<dd> Pass argument to the Java runtime.</dd></dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-java/">java</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
