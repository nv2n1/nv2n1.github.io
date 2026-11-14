---
title: "sshmenu(1)"
name: "sshmenu"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshmenu/"
description: "sshmenu – GNOME applet for connecting to hosts using SSH."
---

<h2>NAME</h2>
<p> sshmenu &#8211; GNOME applet for connecting to hosts using SSH.</p>
<h2>DESCRIPTION</h2>
<p> The SSHMenu applet puts all your most frequently used SSH connections on a handy menu in your GNOME panel (see below for non-GNOME versions. Click on a host name to open a new gnome-terminal window with an ssh connection to the selected host. Set up SSH options (such as port forwarding etc) and select a gnome terminal profile (for colour schemes, font sizes etc) using the preferences dialog. </p>
<p> Add the applet to a GNOME panel in the normal way: right click on the panel, select &#8216;Add to Panel&#8217; and then select the SSH Menu Applet from the list. </p>
<p> Configure the applet using the &#8216;Preferences&#8217; option on the applet menu.</p>
<h2>STANDALONE VERSIONS</h2>
<p> The SSHMenu application uses the GTK GUI toolkit but is not dependent on the GNOME desktop environment. Two alternative wrapper scripts are provided: </p>
<p> sshmenu-gnome &#8211; provides all the functionality of the SSHMenu applet but in a standalone application window that could (for example) be swallowed into the panel of an alternative desktop environment. </p>
<p> sshmenu &#8211; provides similar functionality to sshmenu-gnome, but without any GNOME dependencies. Notably, xterm is used instead of gnome-terminal. </p>
<p> The Hacker&#8217;s Guide ( <a rel="nofollow" href="http://sshmenu.sourceforge.net/dev/hackers_guide.html">http://sshmenu.sourceforge.net/dev/hackers_guide.html</a> ) describes a number of ways in which the SSHMenu can be further customised.</p>
<h2>OPTIONS</h2>
<p> The applet is not invoked from the command-line however the standalone versions recognise the following options and can be extended to recognise more:</p>
<dl>
<dt><code>-c</code><i> FILE</i>, &#8211;config-file <i>FILE</i></p>
<dd> read and write config information to <i>FILE</i> instead of the default <code>$HOME/.sshmenu</code></p>
<dt><code>-d</code><i> NUM</i>, &#8211;debug <i>NUM</i></p>
<dd> set debug level to <i>NUM</i> (default: 0)</p>
<dt><code>-s</code><i> NUM</i>, &#8211;socket-window-id <i>NUM</i></p>
<dd> use the XEmbed protocol to embed the SSHMenu user interface in the window identified by <i>NUM</i> instead of creating a new, top-level window,</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> sshmenu-applet was written by Grant McLean &lt;grant [at] mclean.net.nz&gt; </p>
<h2>Index</h2>
