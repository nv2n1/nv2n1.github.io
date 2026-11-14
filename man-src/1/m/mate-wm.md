---
title: "mate-wm(1)"
name: "mate-wm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-wm/"
description: "mate-wm – Start the window manager configured by the user"
---

<h2 class="name">NAME</h2>
<p> mate-wm &#8211; Start the window manager configured by the user </p>
<h2>SYNOPSIS</h2>
<p> <code>mate-wm [&#8211;default-wm=WINDOWMANAGER] [&#8211;sm-client-id=ID]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mate-wm</code> program starts the window manager configured by the user. If the user has not chosen a window manager it will launch a MATE compliant window manager.</p>
<h2>USAGE</h2>
<p> The user can define his preferred window manager with the <code>/</code><i>org</i><code>/</code><i>mate</i><code>/</code><i>desktop</i><code>/</code><i>session</i><code>/</code><i>required-components</i><code>/</code><i>windowmanager</i> dconf key. The value of this key should be the name of the desktop file of the desired window manager, without its <code>.desktop</code> extension. If this key is set to <code>mate-wm</code>, then <code>mate-wm</code> will simply look for an appropriate window manager. The user can also override the selection of a window manager by setting the <code>WINDOW_MANAGER</code> environment variable. </p>
<p> If the <code>&#8211;default-wm</code> option is used, <code>mate-wm</code> will use <code>WINDOWMANAGER</code> as window manager if the <code>WINDOW_MANAGER</code> environment variable is not set and if the <code>/</code><i>org</i><code>/</code><i>mate</i><code>/</code><i>desktop</i><code>/</code><i>session</i><code>/</code><i>required-components</i><code>/</code><i>windowmanager</i> dconf key does not define a specific window manager, or if the configured window manager cannot be found. </p>
<p> The <code>&#8211;sm-client-id</code> option is translated to an appropriate option depending on which window manager will be started.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>&#8211;default-wm=WINDOWMANAGER</code></p>
<dd> Define the default window manager to start if no window manager is configured, or if the configured window manager cannot be found.</p>
<dt><code>&#8211;sm-client-id=ID</code></p>
<dd> Specify the session management <i>ID</i> when connecting to the session manager.</dl>
<h2>ENVIRONMENT</h2>
<p> <i>mate-wm</i> uses the value of the <code>WINDOW_MANAGER</code> environment variable to let the user override the configured window manager.</p>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/mate-session/issues">http://github.com/mate-desktop/mate-session/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been updated for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<h3>This Manual was originally written for gnome-session by:</h3>
<pre><code>
Miguel de Icaza&lt;miguel[at] helixcode.com&gt;(2000)
    Vincent Untz&lt;vuntz[at] gnome.org&gt;(2009 - 2010)
</code></pre>
<h2>SEE ALSO</h2>
<h3>Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></h3>
<p> <code><a href="/docs/linux/man/1-mate-session-properties/">mate-session-properties</a>(1),</code> <code><a href="/docs/linux/man/1-mate-session-save/">mate-session-save</a>(1),</code> <code><a href="/docs/linux/man/1-mate-session/">mate-session</a>(1)</code> </p>
<h2>Index</h2>
