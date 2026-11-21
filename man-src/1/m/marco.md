---

title: "marco(1)"
name: "marco"
section: "1"
letter: "m"
url: "/docs/linux/man/1-marco/"
description: "Marco – The MATE Window Manager"
---

<p> Marco &#8211; The MATE Window Manager </p>
<h2>SYNOPSIS</h2>
<p> <code>marco [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> Marco is a minimal X window manager that uses GTK+ for drawing window frames. It is aimed at non-technical users and is designed to integrate well with the MATE desktop. Marco is a plain window manager for the adult in you; Many window managers are like Marshmallow Froot Loops, Marco is like Cheerios. It lacks some features that may be expected by traditional UNIX or other technical users; these users may want to investigate other available window managers for use with MATE or as a standalone window manager. </p>
<p> Marco supports several somewhat advanced but common features such as Window Shading/Roll-Up, Window/Edge Snapping, Vertical and Horizontal Maximize, Always-On-Top, Sloppy/Mouse Focus and Raising, and many more&#8230; Well, not a lot, but some more. </p>
<p> This manual page documents the <code>marco</code> command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;display=DISPLAY</code></dt>
<dd> X display to use.</dd>
<dt><code>&#8211;sync</code></dt>
<dd>
 Make X calls synchronous.</dd>
<dt><code>&#8211;replace</code></dt>
<dd> Replace the currently running window manager with Marco.</dd>
<dt><code>&#8211;sm-disable</code></dt>
<dd> Disable the connection to the session manager.</dd>
<dt><code>&#8211;sm-client-id=ID</code></dt>
<dd> Specify a session management ID.</dd>
<dt><code>&#8211;sm-save-file=FILENAME</code></dt>
<dd> Restore from a session management savefile.<br />
 If no path is specified <code>marco</code> will look in ~/.config/mate-session/saved-session/</dd>
<dt><code>-c, &#8211;composite</code></dt>
<dd> Turn compositing ON. You may also use this option to start <code>marco</code> with composite &quot;true transparency&quot; effects.</dd>
<dt><code>&#8211;no-composite</code></dt>
<dd> Turn compositing OFF. You may also use this option to start <code>marco</code> without compositing effects.</dd>
<dt><code>&#8211;no-force-fullscreen</code></dt>
<dd> Do not create fullscreen windows without decorations.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print current version information and exit.</dd>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print standard command line options.</dd></dl>
<h2>CONFIGURATION</h2>
<p> Marco configuration can be found via the main MATE menus, under &quot;<i>System</i>-&gt;<i>Preferences</i>-&gt;<i>Windows</i>&quot; and &quot;<i>System</i>-&gt;<i>Preferences</i>-&gt;<i>Keyboard Shortcuts</i>&quot; or by running the commands <code>mate-window-properties</code> and <code>mate-keybinding-properties</code> respectively. Advanced configuration can also be achieved directly, via <code>dconf-editor</code> under &quot;/<i>org</i>/<i>mate</i>/<i>marco</i>/&quot;.</p>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/marco/issues">http://github.com/mate-desktop/marco/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been updated/re-written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<h3>Portions of this manual page were originally written by Luke Morton and Philip O&#8217;Brien (2006) for Metacity, but do not bear resemblance to preceding documentation.</h3>
<h2>SEE ALSO</h2>
<h3>Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></h3>
<p> <code><a href="/docs/linux/man/1-marco-message/">marco-message</a></code>(1), <code><a href="/docs/linux/man/1-marco-theme-viewer/">marco-theme-viewer</a></code>(1), <code><a href="/docs/linux/man/1-marco-window-demo/">marco-window-demo</a></code>(1) </p>
