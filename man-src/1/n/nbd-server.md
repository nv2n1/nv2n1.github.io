---
title: "nbd-server(1)"
name: "nbd-server"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nbd-server/"
description: "nbd-server – serve a file as a block device to other computers running the GNU/Linux(tm) or GNU/Hurd Operating System"
---

<h2 class="name">NAME</h2>
<p> nbd-server &#8211; serve a file as a block device to other computers running the GNU/Linux(tm) or GNU/Hurd Operating System </p>
<h2>SYNOPSIS</h2>
<p> <code>nbd-server </code> <i>[ip@]port</i> <i>filename</i> [ <i>size</i> ] [ <code>-r</code> ] [ <code>-m</code> ] [ <code>-c</code> ] [ <code>-l </code><i>host list filename</i> ] [ <code>-o </code><i>section name</i> ] [ <code>-C </code><i>config file</i> ] [ <code>-M </code><i>max connections</i> ] [ <code>-V</code> ] [ <code>-d</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>nbd-server</code> is the server for the Linux Network Block Device (NBD). With NBD, a client can use a file, exported over the network from a server, as a block device. It can then be used for whatever purpose a normal block device (harddisk, CD-ROM, &#8230;) can be used for. </p>
<p> NBD can be useful for diskless clients that need swapspace, but you can also create a filesystem on it and use it as though it were a local filesystem. </p>
<p> <code>nbd-server</code> implements some security through a file called &quot;/etc/nbd-server/allow&quot; (by default; a different file can be chosen with the &#8216;-l&#8217; option or through a config file specification). This file must list the IP-addresses or network masks of clients that are allowed to connect. If it does not exist, all clients are able to connect. If the file is empty, no clients can connect. </p>
<p> Note that while the command line allows for specifying an export, the use of this option is deprecated. It is preferred to make use of a configuration file instead, the format of which is defined in <a href="/docs/linux/man/5-nbd-server/">nbd-server</a>(5). </p>
<p> While nbd-server is running, new exports can be added by re-writing configuration files and then sending SIGHUP to nbd-server. SIGHUP causes nbd-server to re-read its configuration files and to start serving all new exports which were not served earlier. Reconfiguration does not modify any existing export, it only appends new ones.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>ip</code></p>
<dd> The ip address the server should listen on. This may be an IPv4 address, an IPv6 address, or a hostname. In the latter case, nbd-server will do a hostname lookup for the name specified, and will listen on the first address that is returned. For compatibility with past versions of nbd-server, if an IPv4 address is specified, the @ sign that serves as separator between the address and port may be replaced by a colon. </p>
<p> If this parameter is not specified, nbd-server will listen on all local addresses on both IPv4 and IPv6. To limit to IPv4, specify the address as 0.0.0.0; to limit to IPv6, specify it as ::.</p>
<dt><code>port </code></p>
<dd> The port the server should listen to. A valid port is any number between 1 and 65536; if 0 is used, nbd-server will listen on stdin (so that nbd-server can be ran from inetd)</p>
<dt><code>filename</code></p>
<dd> The filename of the file that should be exported. This can be any file, including &quot;real&quot; blockdevices (i.e. a file from /dev). If the filename includes the literal string &quot;%s&quot;, then this %s will be substituded with the IP-address of the client trying to connect.</p>
<dt><code>size</code></p>
<dd> The size of the block device at the client side. This is especially useful in conjunction with the -m option </p>
<p> Can optionally be followed by one of K,k,M or m, in which case the size will be multiplied by 1024 (K or k) or 1048576 (M or m)</p>
<dt><code>-r</code></p>
<dd> Export the file read-only. If a client tries to write to a read-only exported file, it will receive an error, but the connection will stay up.</p>
<dt><code>-m</code></p>
<dd> Work with multiple files. This can be used to export blockdevices that are larger than the maximum allowed filesize on a given filesystem; i.e. when the filesystem does not allow files larger than 2GB (which is true for Linux 2.2 and below), you can use this option to store the data in multiple files and export a larger filesystem, if needed. </p>
<p> To use this option, you must create a number of files with names in the format &quot;name.X&quot;, where &quot;name&quot; is given as the filename argument to nbd-server, and &quot;X&quot; is a number starting by 0 and going up for each file. </p>
<p> Allowing more flexibility for this option is planned for future versions.</p>
<dt><code>-c</code></p>
<dd> Copy on write. When this option is provided, write-operations are not done to the exported file, but to a separate file. This separate file is removed when the connection is closed, which means that serving this way will make nbd-server slow down (especially on large block devices with lots of writes), and that after disconnecting and reconnecting the client or the server, all changes are lost.</p>
<dt><code>-C</code></p>
<dd> Specify configuration file. The default configuration file, if this parameter is not specified, is <i>/etc/nbd-server/config</i>. </p>
<p> Note that the configuration file is always parsed and the entries in the file used, even if an extra server is specified on the command line. To disable the configuration file entirely, either move it away or use the -C option to point <code><a href="/docs/linux/man/1-nbd-server/">nbd-server</a></code>(1) to a non-existing or empty configuration file. </p>
<p> Also note that if an empty, incomplete, or invalid configuration file is specified, nbd-server will produce a warning about failure to parse the config file. If the command line contains a fully specified configuration, this warning is harmless and may be ignored.</p>
<dt><code>-M</code></p>
<dd> Specify the maximum number of opened connections. If this parameter is not specified, no limit is set.</p>
<dt><code>-V</code></p>
<dd> Output the version of nbd-server, and exit.</p>
<dt><code>-d</code></p>
<dd> Do not fork. Useful for debugging.</p>
<dt><code>host list filename</code></p>
<dd> This argument should contain a list of IP-addresses for hosts that may connect to the server. Wildcards are <code>not</code> allowed. If the file does not exist, it is ignored (and any host can connect); If the file does exist, but is empty, no host can connect. By default, the name &#8216;nbd_server.allow&#8217; is used, and looked for in the current directory, unless nbd-server is compiled as a daemon, in which case it is looked for in the root-directory.</p>
<dt><code>section name</code></p>
<dd> If the <code>-o</code> argument is given on the command line, then nbd-server will output a configuration file section with this as the header that is functionally equivalent to the other options specified on the command line, and exit. This is useful for migrating pre-2.9 nbd-server initscript configuration files to the new format.</dl>
<h2>EXAMPLES</h2>
<p> Some examples of nbd-server usage:</p>
<dl>
<dt>&bull;</p>
<dd> To export a file /export/nbd/exp-bl-dev on port 2000: </p>
<p> <code>nbd-server 2000 /export/nbd/exp-bl-dev</code></p>
<dt>&bull;</p>
<dd> To export a the same file read-only: </p>
<p> <code>nbd-server 2000 /export/nbd/exp-bl-dev -r</code></p>
<dt>&bull;</p>
<dd> To export the same file read-write, but make sure changes are lost after restarting the client or the server: </p>
<p> <code>nbd-server 2000 /export/nbd/exp-bl-dev -c</code></dl>
<h2>SEE ALSO</h2>
<p> nbd-client (8), nbd-server (5), nbd-trdump (8)</p>
<h2>AUTHOR</h2>
<p> The NBD kernel module and the NBD tools were originally written by Pavel Machek (pavel [at] ucw.cz) </p>
<p> The Linux kernel module is now maintained by Paul Clements (Paul.Clements [at] steeleye.com), while the userland tools are maintained by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) </p>
<p> On The Hurd there is a regular translator available to perform the client side of the protocol, and the use of <code>nbd-client</code> is not required. Please see the relevant documentation for more information. </p>
<p> This manual page was written by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) for the Debian GNU/Linux system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<h2>Index</h2>
