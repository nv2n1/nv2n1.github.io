---
title: "xmms2-launcher(1)"
name: "xmms2-launcher"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2-launcher/"
description: "xmms2-launcher – XMMS2 daemon launcher"
---

<h2>NAME</h2>
<p> xmms2-launcher &#8211; XMMS2 daemon launcher</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2-launcher</i> [ <code>-?</code> / <code>&#8211;help</code> ] <i>xmms2-launcher</i> [ <code>-l </code> logfile / <code>&#8211;logfile=</code> logfile] [ <code>-P </code> pidfile / <code>&#8211;pidfile=</code> pidfile]</p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2</code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organise your music. </p>
<p> <i>xmms2-launcher</i> starts <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1)</i> in the background. The main feature is that it does not exit until the IPC system of <code>XMMS2</code> is available, meaning that as soon as the <i>xmms2-launcher</i> process has exited successfully <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1)</i> is ready to accept commands. </p>
<p> <i>xmms2-launcher</i> includes command line options to change the way in which the daemon is invoked.</p>
<dl>
<dt><code>These</code>options<code>are</code>currently<code>recognised:</code></p>
<dd>
<dt><i>-l logfile / &#8211;logfile=logfile</i></p>
<dd> Write log file to <i>logfile</i> instead of the default log file location</p>
<dt><i>&#8211; P pidfile / &#8211;pidfile=pidfile</i></p>
<dd> Write the pid of <i>xmms2d</i> to the file specified by <i>pidfile</i></p>
<dt><i>-? / &#8211;help </i></p>
<dd> Show help options</dl>
<h2>FILES</h2>
<dl>
<dt><i>$XDG_CACHE_HOME/xmms2/xmms2d.log</i></p>
<dd> The default location for a file where the log output of <i><a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1)</i> is redirected. Usually ~/.cache/xmms2/xmms2d.log.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xmms2d/">xmms2d</a>(1), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributers from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
<h2>Index</h2>
