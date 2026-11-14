---
title: "qemu-nbd(8)"
name: "qemu-nbd"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qemu-nbd/"
description: "qemu-nbd – QEMU Disk Network Block Device Server"
---

<p>qemu-nbd &#8211; QEMU Disk Network Block Device Server</p>
<h2>Synopsis</h2>
<p><code>qemu-nbd</code> [<font SIZE="-1">OPTION</font>]&#8230; <i>filename</i> </p>
<p> <code>qemu-nbd</code> <code>-d</code> <i>dev</i></p>
<h2>Description</h2>
<p>Export a <font SIZE="-1">QEMU</font> disk image using the <font SIZE="-1">NBD</font> protocol.</p>
<h2>Options</h2>
<p><i>filename</i> is a disk image filename, or a set of block driver options if <i>&#8211;image-opts</i> is specified. </p>
<p> <i>dev</i> is an <font SIZE="-1">NBD</font> device.</p>
<dl>
<dt><code>&#8211;object type,id=</code><i>id</i><code>,&#8230;props&#8230;</code></p>
<dd>Define a new instance of the <i>type</i> object class identified by <i>id</i>. See the <tt><a href="/docs/linux/man/1-qemu/">qemu</a>(1)</tt> manual page for full details of the properties supported. The common object types that it makes sense to define are the <tt>&quot;secret&quot;</tt> object, which is used to supply passwords and/or encryption keys, and the <tt>&quot;tls-creds&quot;</tt> object, which is used to supply <font SIZE="-1">TLS</font> credentials for the qemu-nbd server.</p>
<dt><code>-p, &#8211;port=</code><i>port</i></p>
<dd>The <font SIZE="-1">TCP</font> port to listen on (default <code>10809</code>)</p>
<dt><code>-o, &#8211;offset=</code><i>offset</i></p>
<dd>The offset into the image</p>
<dt><code>-b, &#8211;bind=</code><i>iface</i></p>
<dd>The interface to bind to (default <code>0.0.0.0</code>)</p>
<dt><code>-k, &#8211;socket=</code><i>path</i></p>
<dd>Use a unix socket with path <i>path</i></p>
<dt><code>&#8211;image-opts</code></p>
<dd>Treat <i>filename</i> as a set of image options, instead of a plain filename. If this flag is specified, the <i>-f</i> flag should not be used, instead the &#8216;<tt>&quot;format=&quot;</tt>&#8216; option should be set.</p>
<dt><code>-f, &#8211;format=</code><i>fmt</i></p>
<dd>Force the use of the block driver for format <i>fmt</i> instead of auto-detecting</p>
<dt><code>-r, &#8211;read-only</code></p>
<dd>Export the disk as read-only</p>
<dt><code>-P, &#8211;partition=</code><i>num</i></p>
<dd>Only expose partition <i>num</i></p>
<dt><code>-s, &#8211;snapshot</code></p>
<dd>Use <i>filename</i> as an external snapshot, create a temporary file with backing_file=<i>filename</i>, redirect the write to the temporary one</p>
<dt><code>-l, &#8211;load-snapshot=</code><i>snapshot_param</i></p>
<dd>Load an internal snapshot inside <i>filename</i> and export it as an read-only device, <i>snapshot_param</i> format is &#8216;snapshot.id=[<font SIZE="-1">ID</font>],snapshot.name=[<font SIZE="-1">NAME</font>]&#8217; or &#8216;[<font SIZE="-1">ID_OR_NAME</font>]&#8217;</p>
<dt><code>-n, &#8211;nocache</code></p>
<dd>
<dt><code>&#8211;cache=</code><i>cache</i></p>
<dd>The cache mode to be used with the file. See the documentation of the emulator&#8217;s <tt>&quot;-drive cache=...&quot;</tt> option for allowed values.</p>
<dt><code>&#8211;aio=</code><i>aio</i></p>
<dd>Set the asynchronous I/O mode between <code>threads</code> (the default) and <code>native</code> (Linux only).</p>
<dt><code>&#8211;discard=</code><i>discard</i></p>
<dd>Control whether <i>discard</i> (also known as <i>trim</i> or <i>unmap</i>) requests are ignored or passed to the filesystem. <i>discard</i> is one of <code>ignore</code> (or <code>off</code>), <code>unmap</code> (or <code>on</code>). The default is <code>ignore</code>.</p>
<dt><code>&#8211;detect-zeroes=</code><i>detect-zeroes</i></p>
<dd>Control the automatic conversion of plain zero writes by the <font SIZE="-1">OS</font> to driver-specific optimized zero write commands. <i>detect-zeroes</i> is one of <code>off</code>, <code>on</code> or <code>unmap</code>. <code>unmap</code> converts a zero write to an unmap operation and can only be used if <i>discard</i> is set to <code>unmap</code>. The default is <code>off</code>.</p>
<dt><code>-c, &#8211;connect=</code><i>dev</i></p>
<dd>Connect <i>filename</i> to <font SIZE="-1">NBD</font> device <i>dev</i></p>
<dt><code>-d, &#8211;disconnect</code></p>
<dd>Disconnect the device <i>dev</i></p>
<dt><code>-e, &#8211;shared=</code><i>num</i></p>
<dd>Allow up to <i>num</i> clients to share the device (default <code>1</code>)</p>
<dt><code>-t, &#8211;persistent</code></p>
<dd>Don&#8217;t exit on the last connection</p>
<dt><code>-x, &#8211;export-name=</code><i>name</i></p>
<dd>Set the <font SIZE="-1">NBD</font> volume export name. This switches the server to use the new style <font SIZE="-1">NBD</font> protocol negotiation</p>
<dt><code>-D, &#8211;description=</code><i>description</i></p>
<dd>Set the <font SIZE="-1">NBD</font> volume export description, as a human-readable string. Requires the use of <code>-x</code></p>
<dt><code>&#8211;tls-creds=ID</code></p>
<dd>Enable mandatory <font SIZE="-1">TLS</font> encryption for the server by setting the <font SIZE="-1">ID</font> of the <font SIZE="-1">TLS</font> credentials object previously created with the &#8211;object option.</p>
<dt><code>&#8211;fork</code></p>
<dd>Fork off the server process and exit the parent once the server is running.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Display extra debugging information</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display this help and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Display version information and exit</p>
<dt><code>-T, &#8211;trace [[enable=]</code><i>pattern</i><code>][,events=</code><i>file</i><code>][,file=</code><i>file</i><code>]</code></p>
<dd>Specify tracing options.</p>
<dl>
<dd>
<dl>
<dt><code>[enable=]</code><i>pattern</i></p>
<dd>Immediately enable events matching <i>pattern</i>. The file must contain one event name (as listed in the <i>trace-events-all</i> file) per line; globbing patterns are accepted too. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend. To specify multiple events or patterns, specify the <code>-trace</code> option multiple times. </p>
<p> Use <tt>&quot;-trace help&quot;</tt> to print a list of names of trace points.</p>
<dt><code>events=</code><i>file</i></p>
<dd>Immediately enable events listed in <i>file</i>. The file must contain one event name (as listed in the <i>trace-events-all</i> file) per line; globbing patterns are accepted too. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i>, <i>log</i> or <i>ftrace</i> tracing backend.</p>
<dt><code>file=</code><i>file</i></p>
<dd>Log output traces to <i>file</i>. This option is only available if <font SIZE="-1">QEMU</font> has been compiled with the <i>simple</i> tracing backend.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-qemu/">qemu</a></i>(1), <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1)</p>
<h2>Author</h2>
<p>Copyright (C) 2006 Anthony Liguori &lt;anthony [at] codemonkey.ws&gt;. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font></p>
