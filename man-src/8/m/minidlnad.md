---
title: "minidlnad(8)"
name: "minidlnad"
section: "8"
letter: "m"
url: "/docs/linux/man/8-minidlnad/"
description: "minidlnad – MiniDLNA DLNA/UPnP-AV Server"
---

<p>minidlnad &#8211; MiniDLNA DLNA/UPnP-AV Server</p>
<h2>Synopsis</h2>
<p>minidlnad options </p>
<h2>Description</h2>
<p><code>minidlna</code> is a lightweight but very functional DLNA/UPnP-AV server allowing easy sharing of your media files including pictures to any capable device or client on your local wired and wireless network. Common PC software like totem is a good lightweight and fast choice for Linux/BSD; more fully featured software for Linux, Windows and MAC is XBMC, also Mediahouse on Android, and any media sharing capable DVR/TV etc. </p>
<h2>Options</h2>
<p><code>minidlna&#8217;s </code> options are normally set from the global /etc/minidlna.conf file. </p>
<pre>But there may be times when you need to temporarily alter some of these options,
you can do this by running minidlna with the following command line switches.</pre>
<dl>
<dt><code>-R</code> <i>Rescan</i></p>
<dd>This forces minidlna to rescan all of the media_dir directories. </p>
<dt><code>-f</code> <i>config_file</i></p>
<dd>Run minidlna with a different configuration file than the global default. </p>
<dt><code>-p</code> <i>port</i></p>
<dd>Allows to run minidlna on a different port. </p>
<dt><code>-w</code> <i>presentation_url</i></p>
<dd>Change the default presentation url address. </p>
<dt><code>-d</code> <i>debug</i></p>
<dd>minidlna will run in the foreground with debug output. </p>
<dt><code>-P</code> <i>pid_filename</i></p>
<dd>Specify a location for the PID file. </p>
<dt><code>-m</code> <i>model</i></p>
<dd>Force minidlna to report a specific model number. </p>
<dt><code>-s</code> <i>serial</i></p>
<dd>Force minidlna to report a specific serial number. </p>
<dt><code>-t</code> <i>notify_interval</i></p>
<dd>Change the notify interval, in seconds. Defaults to 895 seconds. </p>
<dt><code>-h</code> <i>help</i></p>
<dd>Show basic switch options for running minidlna. </p>
<dt><code>-V</code> <i>Version</i></p>
<dd>Shows the program version number and exits. </p>
</dl>
<h2>Version</h2>
<p>This man page corresponds to minidlna version 1.1.0</p>
<h2>Author</h2>
<pre>minidlna developed by Justin Maggard <a rel="nofollow" href="https://sourceforge.net/projects/minidlna/">https://sourceforge.net/projects/minidlna/</a>
man page written by Noel Butler &lt;noelb [at] ausics.net&gt;</pre>
<h2>Files</h2>
<p>/usr/sbin/minidlnad</p>
<h2>See Also</h2>
<p>&nbsp;<wbr><a href="/docs/linux/man/5-minidlna-conf/">minidlna.conf</a>(5) </p>
