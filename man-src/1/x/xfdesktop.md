---
title: "xfdesktop(1)"
name: "xfdesktop"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfdesktop/"
description: "xfdesktop – The Xfce 4 Desktop Environment’s desktop manager"
---

<h2>SYNOPSIS</h2>
<p> <code>xfdesktop</code><br />
 <code>xfdesktop</code> <i>[options]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xfdesktop</code> manages the desktop itself in the Xfce 4 Desktop Environment. This includes drawing the desktop backdrop and providing a right-click applications menu and middle-click window list menu, as well as drawing icons on the desktop. Only one instance of xfdesktop can be running at a time, and should be started by running <code>xfdesktop</code> without any arguments. </p>
<h2>OPTIONS</h2>
<h3>HELP OPTIONS:</h3>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd>
<dt><code>&#8211;help-sm-client</code></dt>
<dd> Show session management options </dd>
</dl>
<h3>APPLICATION OPTIONS:</h3>
<dl>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display version information</dd>
<dt><code>-R, &#8211;reload</code></dt>
<dd> Causes an already-running instance of <code>xfdesktop</code> to reload all its settings and redraws the desktop background.</dd>
<dt><code>-N, &#8211;next</code></dt>
<dd> Causes an already-running instance of <code>xfdesktop</code> to advance to the next wallpaper on the current workspace.</dd>
<dt><code>-M, &#8211;menu</code></dt>
<dd> Causes an already-running instance of <code>xfdesktop</code> to pop up the applications menu at the current position of the mouse cursor.</dd>
<dt><code>-W, &#8211;windowlist</code></dt>
<dd> Causes an already-running instance of <code>xfdesktop</code> to pop up the window list menu at the current position of the mouse cursor.</dd>
<dt><code>-A, &#8211;arrange</code></dt>
<dd> Automatically arrange all the icons on the desktop</dd>
<dt><code>-D, &#8211;disable-wm-check</code></dt>
<dd> Do not wait for a window manager on startup</dd>
<dt><code>-e, &#8211;enable-debug</code></dt>
<dd> Enable debug messages</dd>
<dt><code>-d, &#8211;disable-debug</code></dt>
<dd> Disable debug messages</dd>
<dt><code>-Q, &#8211;quit</code></dt>
<dd> Cause <code>xfdesktop</code> to quit</dd>
<dt><code>&#8211;display=[DISPLAY]</code></dt>
<dd> X display to use </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> <code>xfdesktop</code>&#8216;s behavior is affected by the following environment variables. </p>
<dl>
<dt><code>XDG_CONFIG_HOME</code></dt>
<dd> Specifies the root for all user-specific configuration files. If this environment variable is not present, it defaults to <i>~/.config</i></dd>
<dt><code>XDG_CONFIG_DIRS</code></dt>
<dd> Specifies a colon-separated list of system directories in which to search for configuration data. If this environment variable is not present, it defaults to <i>/etc/xdg</i> </dd>
</dl>
<h2>FILES</h2>
<p> <code>xfdesktop</code> searches for a menu description file in <i>$XDG_CONFIG_DIRS/menus/xfce-applications.menu</i>. <code>xfdesktop</code> can also use a user-customized menu in <i>$XDG_CONFIG_HOME/menus/</i>. </p>
<h2>BUGS</h2>
<p> Please report any bugs to <i><a rel="nofollow" href="https://bugzilla.xfce.org/">https://bugzilla.xfce.org/</a></i>.<br />
 Development discussion should be conducted on the <i>xfce4-dev [at] xfce.org</i> mailing list.<br />
 Usage-related questions should be directed to the <i>xfce [at] xfce.org</i> mailing list. </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="https://xfce.org/">https://xfce.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> Jasper Huijsmans &lt;huysmans [at] users.sourceforge.net&gt;, Benedikt Meurer &lt;benny [at] xfce.org&gt;, Brian Tarricone &lt;bjt23 [at] cornell.edu&gt;, and Eric Koegel &lt;eric [at] xfce.org&gt;. </p>
<p> This manual page was originally written by Brian Tarricone &lt;bjt23 [at] cornell.edu&gt;. </p>
