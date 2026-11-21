---
title: "mate-session(1)"
name: "mate-session"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-session/"
description: "mate-session – Start the MATE Desktop Environment."
---

<h2 class="name">NAME</h2>
<p> mate-session &#8211; Start the MATE Desktop Environment. </p>
<h2>SYNOPSIS</h2>
<p> <code>mate-session [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mate-session</code> program starts up the MATE desktop environment. This command is typically executed by your Login/Display Manager (like GDM, LXDM, XDM, SLiM, or from your X startup scripts like .xinitrc). It will load either your saved session, or it will provide a default session for the user as defined by the system administrator (or the default MATE installation on your system). </p>
<p> The default session is defined in the dconf keys under <code>/</code><i>org</i><code>/</code><i>mate</i><code>/</code><i>desktop</i><code>/</code><i>session</i><code>/</code><br />
 When saving a session, <code>mate-session</code> saves the currently running applications in the <code>~/.config/mate-session/saved-session</code> directory of the users /home. </p>
<p> <code>mate-session</code> is an X11 session manager. It can manage MATE applications as well as any other X11 SM compliant ones. </p>
<h2>OPTIONS</h2>
<h3>The following options are supported:</h3>
<dl>
<dt><code>-a, &#8211;autostart=DIR</code></dt>
<dd> Start all applications defined in &quot;<code>DIR</code>&quot;, instead of starting the applications defined in <code>/</code><i>org</i><code>/</code><i>mate</i><code>/</code><i>desktop</i><code>/</code><i>session</i><code>/</code><i>default-session</i><br />
 Multiple <code>&#8211;autostart</code> options can be passed.</dd>
<dt><code>-f, &#8211;failsafe</code></dt>
<dd> Run in fail-safe mode. User-specified applications will not be started.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable debugging code.</dd>
<dt><code>&#8211;display=DISPLAY</code></dt>
<dd> X display to use.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Output version information and exit.</dd>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print standard command line options.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Print all command line options. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<h3><code>mate-session</code> sets several environment variables for the use of its child processes:</h3>
<p> <code>SESSION_MANAGER</code></p>
<dl>
<dt>
</dt><dd> This variable is used by session-manager aware clients to contact mate-session.</dd></dl>
<p> <code>DISPLAY</code></p>
<dl>
<dt>
</dt><dd> This variable is set to the X display being used by <code>mate-session</code>. Note that if the &#8211;display option is used this might be different from the setting of the environment variable when mate-session is invoked. </dd>
</dl>
<h2>FILES</h2>
<pre>
<code>~/.config/autostart</code>
<code>/usr/share/autostart</code>
<code>/usr/share/mate/autostart</code>
</pre>
<dl>
<dt>
</dt><dd> The applications defined in the above directories will be started on login. <code><a href="/docs/linux/man/1-mate-session-properties/">mate-session-properties</a>(1)</code> can be used to easily configure them.</dd></dl>
<p> <code>~/.config/mate-session/saved-session</code></p>
<dl>
<dt>
</dt><dd> This directory contains the list of applications of the saved session.</dd></dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/mate-session/issues">http://github.com/mate-desktop/mate-session/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Manual page was originally written for gnome-session by:</h3>
<pre><code>
Miguel de Icaza&lt;miguel[at] helixcode.com&gt;(2000)
    Vincent Untz&lt;vuntz[at] gnome.org&gt;(2009 - 2010)
</code></pre>
<h3>It has been updated for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>SEE ALSO</h2>
<h3>Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></h3>
<p> <code><a href="/docs/linux/man/1-mate-session-properties/">mate-session-properties</a>(1),</code> <code><a href="/docs/linux/man/1-mate-session-save/">mate-session-save</a>(1),</code> <code><a href="/docs/linux/man/1-mate-wm/">mate-wm</a>(1)</code> </p>
