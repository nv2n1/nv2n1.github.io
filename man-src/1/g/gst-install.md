---
title: "gst-install(1)"
name: "gst-install"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-install/"
description: "gst-install – installs missing GStreamer plugins"
---

<h2 class="name">NAME</h2>
<p> gst-install &#8211; installs missing GStreamer plugins </p>
<h2>SYNOPSIS</h2>
<p> <code>gst-install</code> [<i>OPTIONS</i>] plugin <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Gst-install</code> makes use of the PackageKit session D-Bus interface to install missing GStreamer plugins, e.g. encoders, decoders or URI handlers. It isn&#8217;t supposed to be executed directly but instead by the <code>gst_install_plugins_async</code> and <code>gst_install_plugins</code> functions of the GStreamer base library <code>gstpbutilsinstallplugins</code>. </p>
<p> PackageKit or the alternative session-installer implementation will handle the complete installation process with confirmation, progress and error dialogs. </p>
<p> See the documentation of <code>gstpbutilsinstallplugins</code> for the argument construction and exit states.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;transient-for</p>
<dd> The X Window ID of the window which should be used as parents for the dialogs</dl>
<h2>DIAGNOSTICS</h2>
<p> None yet.</p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://launchpad.net/sessioninstaller">https://launchpad.net/sessioninstaller</a></p>
<h2>BUGS</h2>
<p> You can report bugs at the Launchpad site of aptdaemon: <a rel="nofollow" href="https://bugs.launchpad.net/sessioninstaller/+filebug">https://bugs.launchpad.net/sessioninstaller/+filebug</a></p>
<h2>AUTHOR</h2>
<p> Sebastian Heinlein &lt;devel at glatzor dot de&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptd/">aptd</a></code>(1)<code> <a href="/docs/linux/man/1-session-installer/">session-installer</a></code>(1) </p>
<h2>Index</h2>
