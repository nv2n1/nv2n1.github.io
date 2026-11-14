---
title: "xfce4-power-manager-settings(1)"
name: "xfce4-power-manager-settings"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-power-manager-settings/"
description: "xfce4-power-manager-settings – Settings dialog for the Xfce 4 Power manager"
---

<h2 class="name">NAME</h2>
<p> xfce4-power-manager-settings &#8211; Settings dialog for the Xfce 4 Power manager</p>
<h2>SYNOPSIS</h2>
<p> <code>xfce4-power-manager-settings</code> <i>[options]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xfce4-power-manager-settings</code> is a utility that comes with the Xfce4 power manager to access/change its configuration. It is a separate program that uses xfconf to load/save settings according to the user&#8217;s choices. <code>xfce4-power-manager-settings</code> requires the Xfce4 power manager to be running because it connects to it via DBus and gets information about which settings should and should not be displayed; for example, the <code>xfce4-power-manager-settings</code> utility will not show the LCD brightness settings if no device was detected by the running instance of the Xfce4 power manager. </p>
<p> You can run <code>xfce4-power-manager-settings</code> from the command line without specifying any extra arguments. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Have the power manager print debug messages to the console; useful if you have to send in a bug report.</p>
<dt><code>&#8211;socket-id=SOCKET ID</code></p>
<dd> Settings manager socket, used when <code>xfce4-power-manager-settings</code> is embedded in the settings manager.</p>
<dt><code>&#8211;device-id=UpDevice object path</code></p>
<dd> Display a specific device by a specific UPower UpDevice object path. </p>
</dl>
<h2>BUGS</h2>
<p> Please report any bugs to <i><a rel="nofollow" href="http://bugzilla.xfce.org/">http://bugzilla.xfce.org/</a></i>. Development discussion should be conducted on the <i>xfce4-dev [at] xfce.org</i> mailing list. Usage related questions should be directed to the <i>xfce [at] xfce.org</i> mailing list. See: <i><a rel="nofollow" href="https://mail.xfce.org/mailman/listinfo/">https://mail.xfce.org/mailman/listinfo/</a></i> </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="http://goodies.xfce.org/">http://goodies.xfce.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> Ali Abdallah &lt;aliov [at] xfce.org&gt;, Eric Koegel &lt;eric [at] xfce.org&gt;, Simon Steinbeiss &lt;simon [at] xfce.org&gt;, Harald Judt &lt;h.judt [at] gmx.at&gt; </p>
<h2>MANPAGE AUTHORS</h2>
<p> Ali Abdallah &lt;aliov [at] xfce.org&gt;, Robby Workman &lt;rworkman [at] slackware.com&gt;, Eric Koegel &lt;eric [at] xfce.org&gt;. </p>
<h2>Index</h2>
