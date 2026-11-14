---
title: "usbmuxd(8)"
name: "usbmuxd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usbmuxd/"
description: "usbmuxd – Expose a socket to multiplex connections from and to iOS devices."
---

<p>usbmuxd &#8211; Expose a socket to multiplex connections from and to iOS devices.</p>
<h2>Synopsis</h2>
<p><code>usbmuxd</code> [OPTIONS] </p>
<h2>Description</h2>
<p>usbmuxd stands for &quot;USB multiplexing daemon&quot;. This daemon is in charge of multiplexing connections over USB to an iOS device. To users, it means you can sync your music, contacts, photos, etc. over USB. To developers, it means you can connect to any listening localhost socket on the device. usbmuxd is not used for tethering data transfer which uses a dedicated USB interface as a virtual network device. Multiple connections to different TCP ports can happen in parallel. The higher-level layers are handled by libimobiledevice. When usbmuxd is running (normally started, or stopped as a result of &quot;udev&quot; auto-insertion messages or by systemd) it provides a socket interface in &quot;/var/run/usbmuxd&quot; that is designed to be compatible with the socket interface that is provided on Mac OS X. You should also create a &quot;usbmux&quot; user that has access to USB devices on your system. Alternatively, you can pass a different username using the -U argument. Due to iOS 7 the daemon now also manages pairing records with iOS devices and the host in &quot;/var/lib/lockdown&quot; (Linux) or &quot;/var/db/lockdown&quot; (Mac OS X). Ensure proper permissions are setup for the daemon to access the directory. </p>
<h2>Options</h2>
<dl>
<dt><code>-U, &#8211;user USER</code></p>
<dd>Change to this user after startup (needs USB privileges).</p>
<dt><code>-f, &#8211;foreground</code></p>
<dd>Do not daemonize (implies one -v).</p>
<dt><code>-n, &#8211;disable-hotplug</code></p>
<dd>Disables automatic discovery of devices on hotplug. Starting another instance will trigger discovery instead.</p>
<dt><code>-z, &#8211;enable-exit</code></p>
<dd>Enable &quot;&#8211;exit&quot; request from other instances and exit automatically if no device is attached.</p>
<dt><code>-u, &#8211;udev</code></p>
<dd>Run in udev operation mode (implies -n and -z).</p>
<dt><code>-s, &#8211;systemd</code></p>
<dd>Run in systemd operation mode (implies -z and -f).</p>
<dt><code>-x, &#8211;exit</code></p>
<dd>Notify a running instance to exit if there are no devices connected (sends SIGUSR1 to running instance) and exit.</p>
<dt><code>-X, &#8211;force-exit</code></p>
<dd>Notify a running instance to exit even if there are still devices connected (always works) and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>be verbose (use twice or more to increase verbose level).</p>
<dt><code>-V, &#8211;version</code></p>
<dd>print version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>prints usage information. </p>
</dl>
<h2>Author</h2>
<p>The first usbmuxd daemon implementation was authored by Hector Martin. </p>
<p> Now mainly developed by Nikias Bassen, Martin Szulecki and contributors (see AUTHORS file).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-idevice_id/">idevice_id</a>(1), <a href="/docs/linux/man/1-iproxy/">iproxy</a>(1). </p>
<h2>On The Web</h2>
<p><a rel="nofollow" href="https://libimobiledevice.org">https://libimobiledevice.org</a> </p>
<p> <a rel="nofollow" href="https://github.com/libimobiledevice/usbmuxd">https://github.com/libimobiledevice/usbmuxd</a></p>
