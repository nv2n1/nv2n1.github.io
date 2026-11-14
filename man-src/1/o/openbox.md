---
title: "openbox(1)"
name: "openbox"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openbox/"
description: "openbox — A minimalistic, highly configurable, next generation window manager with extensive standards support."
---

<h2>NAME</h2>
<p> openbox &#8212; A minimalistic, highly configurable, next generation window manager with extensive standards support.</p>
<h2>SYNOPSIS</h2>
<p> <code>openbox</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;replace</code>] [<code>&#8211;reconfigure</code>] [<code>&#8211;restart</code>] [<code>&#8211;sm-disable</code>] [<code>&#8211;sync</code>] [<code>&#8211;debug</code>] [<code>&#8211;debug-focus</code>] [<code>&#8211;debug-xinerama</code>]</p>
<h2>DESCRIPTION</h2>
<p> Openbox is minimalistic, highly configurable, next generation window manager with extensive standards support. </p>
<p> You can start Openbox in three ways: </p>
<p> If you run a display manager such as GDM, you will find 3 entries in the login session type menu for Openbox: <code>GNOME/Openbox</code>, <code>KDE/Openbox</code> and <code>Openbox</code>. If you want to use Openbox within GNOME or KDE, you can choose the appropriate entry, and it will launch GNOME or KDE with Openbox as the window manager. </p>
<p> The third option at log in, which is <code>Openbox</code> without a session manager, uses the <code>openbox-session</code> command to start Openbox. On log in, <code>openbox</code> will run the ~/.config/openbox/autostart.sh script if it exists, and will run the system-wide script /etc/xdg/openbox/autostart.sh otherwise. You may place anything you want to run automatically in those files, for example:<br />
&nbsp;<wbr> </p>
<dl>
<dt>
<dd>
<pre>
xsetroot -solid grey &amp; 
gnome-settings-daemon &amp; 
</pre>
</dl>
<p> Make sure that each line is followed by a &quot;&amp;&quot; or else the script will stop there and further commands will not be executed. You can use the /etc/xdg/openbox/autostart.sh file as an example for creating your own. </p>
<p> The default /etc/xdg/openbox/autostart.sh runs a number of things with Openbox. </p>
<p> Lastly, if you use <code>startx</code> to launch your X session, you can set up a ~/.xinitrc file to run <code>openbox-session</code> and follow the same directions as above regarding the autostart.sh file. </p>
<p> You can use the <code>obconf</code> tool to configure Openbox easily with a graphical interface, however more in-depth configuration is possible by editing the configuration files by hand. </p>
<p> The default configuration and menu files are installed in /etc/xdg/openbox/, and the user configuration is placed in ~/.config/openbox/. You can copy the default configuration and menus to ~/.config/openbox and edit it to your liking.</p>
<h2>OPTIONS</h2>
<p> These are the possible options that <code>openbox</code> accepts:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the command line options available and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version of the program and exit.</p>
<dt><code>&#8211;replace</code></p>
<dd> Replace the currently running window manager.</p>
<dt><code>&#8211;config-file FILE</code></p>
<dd> Specify the path to the config file to use.</p>
<dt><code>&#8211;reconfigure</code></p>
<dd> If Openbox is already running on the display, tell it to reload its configuration.</p>
<dt><code>&#8211;restart</code></p>
<dd> If Openbox is already running on the display, tell it to restart. This is useful if you have upgraded Openbox and don&#8217;t want to restart X.</p>
<dt><code>&#8211;exit</code></p>
<dd> Exit Openbox.</p>
<dt><code>&#8211;sm-disable</code></p>
<dd> Do not connect to the session manager.</p>
<dt><code>&#8211;sync</code></p>
<dd> Run in synchronous mode (for debugging).</p>
<dt><code>&#8211;startup CMD</code></p>
<dd> Run CMD after starting.</p>
<dt><code>&#8211;debug</code></p>
<dd> Display debugging output.</p>
<dt><code>&#8211;debug-focus</code></p>
<dd> Display debugging output for focus handling.</p>
<dt><code>&#8211;debug-session</code></p>
<dd> Display debugging output for session management.</p>
<dt><code>&#8211;debug-xinerama</code></p>
<dd> Split the display into two fake xinerama regions, if xinerama is not already enabled. This is for debugging xinerama support.</dl>
<h2>SEE ALSO</h2>
<p> obconf (1), <a href="/docs/linux/man/1-openbox-session/">openbox-session</a>(1), <a href="/docs/linux/man/1-openbox-gnome-session/">openbox-gnome-session</a>(1), <a href="/docs/linux/man/1-openbox-kde-session/">openbox-kde-session</a>(1). </p>
<p> The program&#8217;s full documentation is available on the website: <code><a rel="nofollow" href="http://openbox.org/">http://openbox.org/</a></code> </p>
<p> Please report bugs to: <code><a rel="nofollow" href="http://bugzilla.icculus.org/">http://bugzilla.icculus.org/</a> </code> </p>
<h2>Index</h2>
