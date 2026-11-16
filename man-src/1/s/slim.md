---
title: "slim(1)"
name: "slim"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slim/"
description: "slim – Simple LogIn Manager"
---

<h2>NAME</h2>
<p> <code>slim </code>&#8211; Simple LogIn Manager</p>
<h2>SYNOPSIS</h2>
<pre><code>
slim[options][&lt;arguments&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> SLiM is a lightweight login manager for X11, allowing the initialization of a graphical session by entring username and password in a login screen.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></dt>
<dd> run as a daemon</dd>
<dt><code>-p</code> /path/to/theme</dt>
<dd> display a preview of the theme. An already running X11 session is required for theme preview.</dd>
<dt><code>-h</code></dt>
<dd> display a brief help message</dd>
<dt><code>-v</code></dt>
<dd> display version information</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>slim</code> <code>-d</code></dt>
<dd> run <code>slim</code> in daemon mode</dd>
<dt><code>slim</code> <code>-p</code> /usr/share/<code>slim</code>/themes/default</dt>
<dd> preview of the default theme</dd></dl>
<h2>STARTING SLIM AT BOOT</h2>
<p> Please refer to documentation of your Operating System to make <code>slim</code> automatically startup after the system boots.</p>
<h2>CONFIGURATION</h2>
<p> Global configuration is stored in the /etc/slim.conf file. See the comments inside the file for a detailed explanation of the <i>options</i>.</p>
<h2>USAGE AND SPECIAL USERNAMES</h2>
<p> When started, <code>slim</code> will show a login panel; enter the username and password of the user you want to login as. </p>
<p> Special usernames:</p>
<dl>
<dt><code>console</code></dt>
<dd> open a xterm console</dd>
<dt><code>exit</code></dt>
<dd> quit <code>slim</code></dd>
<dt><code>halt</code></dt>
<dd> shutdown the machine</dd>
<dt><code>reboot</code></dt>
<dd> reboot the machine</dd>
<dt><code>suspend</code></dt>
<dd> power-suspend the machine</dd></dl>
<p> See the configuration file for customizing the above commands. The &#8216;halt&#8217; and &#8216;reboot&#8217; commands need the root password, this may change in future releases. </p>
<p> Shortcuts:</p>
<dl>
<dt><code>F11</code></dt>
<dd> executes a custom command (by default takes a screenshot)</dd>
<dt><code>F1</code></dt>
<dd> choose session type (see configuration file and xinitrc.sample)</dd></dl>
<h2>AUTHORS</h2>
<p> Simone Rota &lt;sip [at] varlock.com&gt; </p>
<p> Johannes Winkelmann &lt;jw [at] tks6.net&gt;</p>
<h2>SEE ALSO</h2>
<p> See the online documentation at the SLiM web site for further information on themes, FAQs, etc. </p>
<h2>Index</h2>
