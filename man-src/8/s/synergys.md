---
title: "synergys(8)"
name: "synergys"
section: "8"
letter: "s"
url: "/docs/linux/man/8-synergys/"
description: "synergys – manual page for synergys 1.5.0, protocol version 1.3"
---

<p>synergys &#8211; manual page for synergys 1.5.0, protocol version 1.3</p>
<h2>Synopsis</h2>
<p><code>synergys</code> [<i>&#8211;address &lt;address&gt;</i>] [<i>&#8211;config &lt;pathname&gt;</i>] [<i>&#8211;daemon|&#8211;no-daemon</i>] [<i>&#8211;name &lt;screen-name&gt;</i>] [<i>&#8211;restart|&#8211;no-restart</i>] [<i>&#8211;debug &lt;level&gt;</i>]</p>
<h2>Description</h2>
<p>Start the synergy mouse/keyboard sharing server.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;address</code> &lt;address&gt;</dt>
<dd>listen for clients on the given address.</dd>
<dt><code>-c</code>, <code>&#8211;config</code> &lt;pathname&gt;</dt>
<dd>use the named configuration file instead.</dd>
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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>display this help and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd>display version information and exit.</dd></dl>
<p> * marks defaults. </p>
<p> The argument for <code>&#8211;address</code> is of the form: [&lt;hostname&gt;][:&lt;port&gt;]. The hostname must be the address or hostname of an interface on the system. The default is to listen on all interfaces. The port overrides the default port, 24800. </p>
<p> If no configuration file pathname is provided then the first of the following to load successfully sets the configuration:</p>
<dl>
<dd>$HOME/.synergy.conf /etc/synergy.conf</dd></dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2010 Chris Schoeneman, Nick Bolton, Sorin Sbarnea</p>
