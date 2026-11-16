---
title: "synergyc(8)"
name: "synergyc"
section: "8"
letter: "s"
url: "/docs/linux/man/8-synergyc/"
description: "synergyc – manual page for synergyc 1.5.0, protocol version 1.3"
---

<p>synergyc &#8211; manual page for synergyc 1.5.0, protocol version 1.3</p>
<h2>Synopsis</h2>
<p><code>synergyc</code> [<i>&#8211;yscroll &lt;delta&gt;</i>] [<i>&#8211;daemon|&#8211;no-daemon</i>] [<i>&#8211;name &lt;screen-name&gt;</i>] [<i>&#8211;restart|&#8211;no-restart</i>] [<i>&#8211;debug &lt;level&gt;</i>] <i>&lt;server-address&gt;</i></p>
<h2>Description</h2>
<p>Connect to a synergy mouse/keyboard sharing server.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code> &lt;level&gt;</dt>
<dd>filter out log messages with priority below level. level may be: FATAL, ERROR, WARNING, NOTE, INFO, DEBUG, DEBUGn (1-5).</dd>
<dt><code>-n</code>, <code>&#8211;name</code> &lt;screen-name&gt; use screen-name instead the hostname to identify</dt>
<dd>this screen in the configuration.</dd>
<dt><code>-1</code>, <code>&#8211;no-restart</code></dt>
<dd>do not try to restart on failure.</dd></dl>
<p> * <code>&#8211;restart</code> restart the server automatically if it fails.</p>
<dl>
<dt><code>-l</code> <code>&#8211;log</code> &lt;file&gt;</dt>
<dd>write log messages to file.</dd>
<dt><code>-f</code>, <code>&#8211;no-daemon</code></dt>
<dd>run in the foreground.</dd></dl>
<p> * <code>&#8211;daemon</code> run as a daemon.</p>
<dl>
<dt><code>&#8211;yscroll</code> &lt;delta&gt;</dt>
<dd>defines the vertical scrolling delta, which is</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>display this help and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd>display version information and exit.</dd></dl>
<p> * marks defaults. </p>
<p> The server address is of the form: [&lt;hostname&gt;][:&lt;port&gt;]. The hostname must be the address or hostname of the server. The port overrides the default port, 24800.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2010 Chris Schoeneman, Nick Bolton, Sorin Sbarnea</p>
