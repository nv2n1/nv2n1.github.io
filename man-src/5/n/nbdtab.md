---
title: "nbdtab(5)"
name: "nbdtab"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nbdtab/"
description: "/etc/nbdtab – configuration file for nbd-client"
---

<p>/etc/nbdtab &#8211; configuration file for nbd-client</p>
<h2>Synopsis</h2>
<p><code>/etc/nbdtab </code> </p>
<h2>Description</h2>
<p>This file allows to configure predefined connections for nbd-client. It may contain multiple definitions, one per line, each of which contains four space-separated fields. </p>
<p> To connect a device specified in the nbdtab file, run <code><a href="/docs/linux/man/8-nbd-client/">nbd-client</a></code>(8) with the short name of that device as the sole argument. It will then look up the required information in <i>nbdtab</i>, and make the connection. </p>
<p> Fields are separated from one another by any number of space or tab characters; records are separated from one another by newline characters. The file may also contain any number of comments, which start with a &#8216;#&#8217; character and continue until the end of the line or the end of the file, whichever is first.</p>
<h3>Fields</h3>
<p>The file contains the following fields:</p>
<dl>
<dt>1.</p>
<dd>The short name of the device file. That is, it should contain the name of the device without the leading <i>/dev/</i> part; e.g., it could say <i>nbd0</i>.</p>
<dt>2.</p>
<dd>The hostname (in case of a TCP socket) or filename (in case of a unix domain socket) on which the server is listening.</p>
<dt>3.</p>
<dd>The name of the export as exported by <code>nbd-server</code>.</p>
<dt>4.</p>
<dd>Any extra options. This field is optional (no pun intended), and need not appear in a file if no options are necessary. The options recognized by <code><a href="/docs/linux/man/8-nbd-client/">nbd-client</a></code>(8) are specified below, in the section &quot;Options&quot;. Any unknown options in this field will produce a warning by <code>nbd-client</code>, unless they are prepended by an underscore (&#8216;_&#8217;) character; the underscore is specifically reserved for local use, or for distribution customization.</dl>
<h3>Options</h3>
<p>Every command-line <code>nbd-client</code> option has a corresponding option in the <i>nbdtab</i> file, and vice versa; where this isn&#8217;t the case, that is a bug. </p>
<p> Individual options in this field should be separated from one another by the comma character.</p>
<dl>
<dt><code>bs=</code><i>block size</i></p>
<dd>The block size for this export. If this option is not used, the kernel&#8217;s default will be used instead. </p>
<p> Corresponds to the <code>-b</code> option on the command line.</p>
<dt><code>port=</code><i>port number</i></p>
<dd>The port on which to communicate with the <code>nbd-server</code>. Defaults to the IANA-assigned port for NBD, 10809.</p>
<dt><code>timeout=</code><i>timeout</i></p>
<dd>The timeout. If this option is not specified, no timeout is configured. </p>
<p> Corresponds to the <code>-t</code> option on the command line.</p>
<dt><code>persist</code></p>
<dd>Persist the connection, using the semantics of the <code>-p</code> command-line option.</p>
<dt><code>swap</code></p>
<dd>Optimize for swap; <code>-s</code>.</p>
<dt><code>sdp</code></p>
<dd>Use the Socket Direct protocol; <code>-S</code>.</p>
<dt><code>unix</code></p>
<dd>Use a Unix Domain socket to connect to the server; <code>-u</code>.</dl>
<h2>See Also</h2>
<p>nbd-server (1), nbd-client (8), nbd-trdump (8)</p>
<h2>Author</h2>
<p>The NBD kernel module and the NBD tools were originally written by Pavel Machek (pavel [at] ucw.cz) </p>
<p> The Linux kernel module is now maintained by Paul Clements (Paul.Clements [at] steeleye.com), while the userland tools are maintained by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) </p>
<p> On The Hurd there is a regular translator available to perform the client side of the protocol, and the use of <code>nbd-client</code> is not required. Please see the relevant documentation for more information. </p>
<p> This manual page was written by Wouter Verhelst (&lt;wouter [at] debian.org&gt;). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation.</p>
<h2>Examples</h2>
<p>A simple <i>nbdtab</i> file could look like this: </p>
<pre># swap space, called &quot;swapexport&quot; on the server
# optimize for swap, and try to reconnect upon disconnect.
nbd0 nbdserver.example.com swapexport swap,persist
# other export, called &quot;data&quot; on the server. No options for this one.
nbd1 nbdserver.example.com data</pre>
