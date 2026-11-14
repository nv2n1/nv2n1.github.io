---
title: "tuned(8)"
name: "tuned"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tuned/"
description: "tuned – dynamic adaptive system tuning daemon"
---

<p>tuned &#8211; dynamic adaptive system tuning daemon</p>
<h2>Synopsis</h2>
<p><code>tuned</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>tuned</code> is a dynamic adaptive system tuning daemon that tunes system settings dynamically depending on usage. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> CONFFILE</i>, <i></i><code>&#8211;conffile=</code><i>CONFFILE</i></p>
<dd>Specify the name and path of the configuration file. By default the <code>/etc/tuned.conf</code> is used.</p>
<dt><code>-d</code><i></i>, <code>&#8211;daemon</code></p>
<dd>This options starts <code>tuned</code> as a daemon as opposed to in the foreground without forking at startup.</p>
<dt><code>-D</code><i></i>, <code>&#8211;debug</code></p>
<dd>Sets the highest logging level. This could be very useful when having trouble with <code>tuned</code>.</p>
<dt><code>-h</code><i></i>, <code>&#8211;help</code></p>
<dd>Show this help.</p>
<dt><code>-l</code><i> </i>[<i>LOG</i>], <code>&#8211;log</code><i></i>[<code>=</code><i>LOG</i>]</p>
<dd>Log to the file <i>LOG</i>. If no <i>LOG</i> file is specified <code>/var/log/tuned/tuned.log</code> is used.</p>
<dt><code>&#8211;no-dbus</code></p>
<dd>Do not attach to DBus.</p>
<dt><code>-P</code><i> </i>[<i>PID</i>], <code>&#8211;pid</code><i></i>[<code>=</code><i>PID</i>]</p>
<dd>Write process ID to the <code>PID</code> file. If no <i>PID</i> file is specified <code>/run/tuned/tuned.pid</code> is used.</p>
<dt><code>-p</code><i></i> <i>PROFILE</i><i></i>, <code>&#8211;profile</code><i></i> <i>PROFILE</i></p>
<dd>Tunning profile to be activated. It will override other settings (e.g. from <code>tuned-adm</code>). This is intended for debugging purposes.</p>
<dt><code>-v</code><i></i>, <code>&#8211;version</code></p>
<dd>Show version information.</dl>
<h2>Files</h2>
<p>/etc/tuned /usr/share/doc/tuned/README</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-tuned-conf/">tuned.conf</a>(5) <a href="/docs/linux/man/8-tuned-adm/">tuned-adm</a>(8)</p>
<h2>Author</h2>
<p>Jan Kaluža &lt;jkaluza [at] redhat.com&gt; Jan Včelák &lt;jvcelak [at] redhat.com&gt; Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt; Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://bugzilla.redhat.com/.">https://bugzilla.redhat.com/.</a></p>
