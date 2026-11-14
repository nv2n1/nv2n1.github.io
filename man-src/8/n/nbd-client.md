---
title: "nbd-client(8)"
name: "nbd-client"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nbd-client/"
description: "nbd-client – connect to a server running"
---

<p>nbd-client &#8211; connect to a server running </p>
<p><a href="/docs/linux/man/1-nbd-server/">nbd-server</a>(1), to use its exported block device</p>
<h2>Synopsis</h2>
<p><code>nbd-client</code> <i>host</i> [ <i>port</i> ] <i>nbd-device</i> [ <code>-sdp</code> ] [ <code>-swap</code> ] [ <code>-persist</code> ] [ <code>-nofork</code> ] [ <code>-systemd-mark</code> ] [ <code>-block-size </code><i>block size</i> ] [ <code>-timeout </code><i>seconds</i> ] [ <code>-name </code><i>name</i> ] <code>nbd-client</code> <code>-unix </code><i>path</i> <i>nbd-device</i> [ <code>-sdp</code> ] [ <code>-swap</code> ] [ <code>-persist</code> ] [ <code>-nofork</code> ] [ <code>-systemd-mark</code> ] [ <code>-block-size </code><i>block size</i> ] [ <code>-timeout </code><i>seconds</i> ] [ <code>-name </code><i>name</i> ] <code>nbd-client</code> <i>nbd-device</i> <code>nbd-client</code> <code>-d </code><i>nbd-device</i> <code>nbd-client</code> <code>-c </code><i>nbd-device</i> <code>nbd-client</code> <code>-l </code><i>host</i> [ <code>port</code> ] </p>
<h2>Description</h2>
<p>With <code>nbd-client</code>, you can connect to a server running <code>nbd-server</code>, thus using raw diskspace from that server as a blockdevice on the local client. </p>
<p> To do this, support from the Linux Kernel is necessary, in the form of the Network Block Device (NBD). When you have that, either in the kernel, or as a module, you can connect to an NBD server and use its exported file through a block special file with major mode 43. </p>
<p> Optionally, long options can also be specified with two leading dashes.</p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><code>-block-size </code><i>block size</i></p>
<dd>
<dt><code>-b</code></p>
<dd>Use a blocksize of &quot;block size&quot;. Default is 1024; allowed values are either 512, 1024, 2048 or 4096</p>
<dt><code>host</code></p>
<dd>The hostname or IP address of the machine running <code>nbd-server</code>. Since 2.9.15, the NBD utilities support IPv6.</p>
<dt><code>-timeout </code><i>seconds</i></p>
<dd>
<dt><code>-t</code></p>
<dd>Set the connection timeout to &quot;seconds&quot;. For this to work, you need a kernel with support for the NBD_SET_TIMEOUT ioctl; this was introduced into Linus&#8217; tree on 2007-10-11, and will be part of kernel 2.6.24.</p>
<dt><code>port</code></p>
<dd>The TCP port on which <code>nbd-server</code> is running at the server. </p>
<p> The port number defaults to 10809, the IANA-assigned port number for the NBD protocol. </p>
<p> Previous versions of the nbd tools supported an older version of the negotiation protocol known as &quot;oldstyle&quot;. This protocol version is no longer supported as of version 3.11 of the nbd support tools.</p>
<dt><code>nbd-device</code></p>
<dd>The block special file (<i>/dev</i> entry) which this nbd-client should connect to, specified as a full path. </p>
<p> When the mode is used wherein no hostname or export name is specified, nbd-client will look up the necessary configuration in the <i>nbdtab</i> file. For more information, see <a href="/docs/linux/man/5-nbdtab/">nbdtab</a>(5).</p>
<dt><code>-check</code></p>
<dd>
<dt><code>-c</code></p>
<dd>Check whether the specified nbd device is connected. </p>
<p> If the device is connected, nbd-client will exit with an exit state of 0 and print the PID of the nbd-client instance that connected it to stdout. </p>
<p> If the device is not connected or does not exist (for example because the nbd module was not loaded), nbd-client will exit with an exit state of 1 and not print anything on stdout. </p>
<p> If an error occurred, nbd-client will exit with an exit state of 2, and not print anything on stdout either.</p>
<dt><code>-disconnect</code></p>
<dd>
<dt><code>-d</code></p>
<dd>Disconnect the specified nbd device from the server</p>
<dt><code>-list</code></p>
<dd>
<dt><code>-l</code></p>
<dd>Ask the server for a list of available exports. If the server is exporting over IPv6 as well as over IPv4, this will list all exports twice; otherwise, it should list them all only once. </p>
<p> Note that this option <code>only</code> works with nbd-server processes running version 3.1 or above, and must be enabled in server configuration (with the &quot;allowlist&quot; option) before it can be used.</p>
<dt><code>-persist</code></p>
<dd>
<dt><code>-p</code></p>
<dd>When this option is specified, nbd-client will immediately try to reconnect an nbd device if the connection ever drops unexpectedly due to a lost server or something similar.</p>
<dt><code>-sdp</code></p>
<dd>
<dt><code>-S</code></p>
<dd>Connect to the server using the Socket Direct Protocol (SDP), rather than IP. See <a href="/docs/linux/man/5-nbd-server/">nbd-server</a>(5) for details.</p>
<dt><code>-swap</code></p>
<dd>
<dt><code>-s</code></p>
<dd>Specifies that this NBD device will be used as swapspace. This option attempts to prevent deadlocks by performing mlockall() and adjusting the oom-killer score at an appropriate time. It does not however guarantee that such deadlocks can be avoided.</p>
<dt><code>-systemd-mark</code></p>
<dd>
<dt><code>-m</code></p>
<dd>The systemd init system requires that processes which should not be killed at shutdown time be marked appropriately by replacing the first letter of their argv[0] with an &#8216;@&#8217; sign. </p>
<p> This option will cause nbd-client to do so. </p>
<p> Note that this only works if nbd-client is run from an initrd; i.e., systemd will ignore such a mark if run from a systemd unit file or from the command line.</p>
<dt><code>-nofork</code></p>
<dd>
<dt><code>-n</code></p>
<dd>Specifies that the NBD client should not detach and daemonize itself. This is mostly useful for debugging. </p>
<p> Note that nbd-client will still fork once to trigger an update to the device node&#8217;s partition table. It is not possible to disable this.</p>
<dt><code>-name</code></p>
<dd>
<dt><code>-N</code></p>
<dd>Specifies the name of the export that we want to use. If not specified, nbd-client will ask for a &quot;default&quot; export, if one exists on the server.</p>
<dt><code>-unix</code></p>
<dd>
<dt><code>-u</code></p>
<dd>Connect to the server over a unix domain socket at <i>path</i>, rather than to a server over a TCP socket. The server must be listening on the given socket.</dl>
<h2>Examples</h2>
<p>Some examples of nbd-client usage:</p>
<dl>
<dt>&bull;</p>
<dd>To connect to a server running on port 2000 at host &quot;server.domain.com&quot;, using the client&#8217;s block special file &quot;/dev/nbd0&quot;: </p>
<p> <code>nbd-client server.domain.com 2000 /dev/nbd0</code></p>
<dt>&bull;</p>
<dd>To connect to a server running on port 2001 at host &quot;swapserver.domain.com&quot;, using the client&#8217;s block special file &quot;/dev/nbd1&quot;, for swap purposes: </p>
<p> <code>nbd-client swapserver.domain.com 2001 /dev/nbd1 -swap</code></p>
<dt>&bull;</p>
<dd>To disconnect the above connection again (after making sure the block special file is not in use anymore): </p>
<p> <code>nbd-client -d /dev/nbd1</code></dl>
<h2>See Also</h2>
<p>nbd-server (1).</p>
<h2>Author</h2>
<p>The NBD kernel module and the NBD tools have been written by Pavel Macheck (pavel [at] ucw.cz). </p>
<p> The kernel module is now maintained by Paul Clements (Paul.Clements [at] steeleye.com), while the userland tools are maintained by Wouter Verhelst (wouter [at] debian.org) </p>
<p> This manual page was written by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) for the Debian GNU/Linux system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation.</p>
