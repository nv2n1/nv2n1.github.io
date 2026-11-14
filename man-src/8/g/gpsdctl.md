---
title: "gpsdctl(8)"
name: "gpsdctl"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpsdctl/"
description: "gpsdctl – tool for sending commands to gpsd over its control socket"
---

<p>gpsdctl &#8211; tool for sending commands to gpsd over its control socket</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gpdsctl</code> <i>action</i> <i>device</i></dl>
<h2>Description</h2>
<dd>This is a tool for sending an instance of gpsd commands over its control socket to add or remove devices from the daemon&#8217;s device list. It is not intended to be called by users, but rather by the Linux hotplug system and similar facilities. </p>
<p> The action argument may be &quot;add&quot; or &quot;remove&quot;. If no daemon instance is running when an add is requested, this program will launch one. </p>
<p> The &quot;device&quot; argument should be the pathname of a device. A device on the list will be opened to read sensor data whenever a client requests a watch. </p>
<p> Two environment variables are interpreted. <code>GPSD_SOCKET</code> sets the location of the control socket. It defaults to /var/run/gpsd.sock if the effective user ID of this program is root, /tmp/gpsd.sock otherwise. </p>
<p> <code>GPSD_OPTIONS</code> may be a list of options to be passed to gpsd when this tool launches it. It defaults to an empty string.</p>
<h2>Return Values</h2>
<p>1 if the action was unknown or the write to the control socket failed, 0 otherwise</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1).</p>
<h2>Author</h2>
<p>Eric S. Raymond &lt;esr [at] thyrsus.com&gt;.</p>
