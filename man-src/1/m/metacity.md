---
title: "metacity(1)"
name: "metacity"
section: "1"
letter: "m"
url: "/docs/linux/man/1-metacity/"
description: "METACITY – minimal GTK2 Window Manager"
---

<h2 class="name">NAME</h2>
<p> METACITY &#8211; minimal GTK2 Window Manager </p>
<h2>SYNOPSIS</h2>
<p> <code>metacity</code> [&#8211;display=<i>DISPLAY</i>] [&#8211;replace] [&#8211;sm-client-id=<i>ID</i>] [&#8211;sm-disable] [&#8211;sm-save-file=<i>FILENAME</i>] [&#8211;sync] [&#8211;composite] [&#8211;no-composite] [&#8211;no-force-fullscreen] [&#8211;version] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly <code>metacity</code>. </p>
<p> <code>metacity</code> is a minimal X window manager aimed at nontechnical users and is designed to integrate well with the GNOME desktop. <code>metacity</code> lacks some features that may be expected by traditional UNIX or other technical users; these users may want to investigate other available window managers for use with GNOME or standalone.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> Connect to X display <i>DISPLAY</i>.</p>
<dt><code>&#8211;replace</code></p>
<dd> a window manager which is running is replaced by <code>metacity</code>. Users are encouraged to change the GNOME window manager by running the new WM with the &#8211;replace or -replace option, and subsequently saving the session.</p>
<dt><code>&#8211;sm-client-id=ID</code></p>
<dd> Specify a session management <i>ID</i>.</p>
<dt><code>&#8211;sm-disable</code></p>
<dd> Disable the session management.</p>
<dt><code>&#8211;sm-save-file=FILENAME</code></p>
<dd> Load a session from <i>FILENAME</i>.</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous</p>
<dt><code>&#8211;composite</code></p>
<dd> Turn compositing on</p>
<dt><code>&#8211;no-composite</code></p>
<dd> Turn compositing off</p>
<dt><code>&#8211;no-force-fullscreen</code></p>
<dd> Don&#8217;t make fullscreen windows that are maximized and have no decorations</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number.</p>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options.</dl>
<h2>CONFIGURATION</h2>
<p> <code>metacity</code> configuration can be found under <i>Preferences</i>-&gt;<i>Windows</i> and <i>Preferences</i>-&gt;<i>Keyboard Shortcuts</i> on the menu-panel. Advanced configuration can be achieved directly through gsettings.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-metacity-message/">metacity-message</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The original manual page was written by Thom May &lt;thom [at] debian.org&gt;. It was updated by Akira TAGOH &lt;tagoh [at] debian.org&gt; for the Debian GNU/Linux system (with permission to use by others), and then updated by Luke Morton and Philip O&#8217;Brien for inclusion in metacity. </p>
<h2>Index</h2>
