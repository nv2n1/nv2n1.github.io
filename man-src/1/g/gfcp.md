---

title: "gfcp(1)"
name: "gfcp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfcp/"
description: "gfcp – manual page for gfcp (glusterfs-coreutils) 0.2.0"
---

<p> gfcp &#8211; manual page for gfcp (glusterfs-coreutils) 0.2.0</p>
<h2>SYNOPSIS</h2>
<p> <code>gfcp</code> [<i>OPTION</i>]&#8230; <i>SOURCE DEST</i></p>
<h2>DESCRIPTION</h2>
<p> Copy SOURCE to DEST; one of local to remote, remote to local, or remote to remote.</p>
<dl>
<dt><code>-o</code>, <code>&#8211;xlator-option</code>=<i>OPTION</i></dt>
<dd> specify a translator option for the connection. Multiple options are supported and take the form xlator.key=value. In the case of both the source and the destination being Gluster URLs, the options will be applied to both connections.</dd>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></dt>
<dd> specify the port on which to connect</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> gfcp ./file <a href="glfs://localhost/groot/remote_file">glfs://localhost/groot/remote_file</a></dd>
<dt>
</dt><dd> Copies the local file &#8216;file&#8217; to the destination file &#8216;remote_file&#8217; on the remote Gluster volume of groot on the host localhost.</dd>
<dt>
</dt><dd> gfcp <a href="glfs://localhost/groot/remote_file">glfs://localhost/groot/remote_file</a> ./file</dd>
<dt>
</dt><dd> Copies the file &#8216;remote_file&#8217; on the remote Gluster gluster volume of groot on the host localhost to the local file &#8216;file&#8217;.</dd>
<dt>
</dt><dd> gfcp <a href="glfs://localhost/groot/remote_file">glfs://localhost/groot/remote_file</a> <a href="glfs://remote_host/groot/file">glfs://remote_host/groot/file</a></dd>
<dt>
</dt><dd> Copies the file &#8216;remote_file&#8217; on the remote Gluster gluster volume of groot on the host localhost to a second remote Gluster volume of groot on the host remote_host to the file &#8216;file&#8217;.</dd>
<dt>
</dt><dd> gfcli (localhost/groot)&gt; cp /example file://example</dd>
<dt>
</dt><dd> Copy the file example relative to the root of the connected Gluster volume to a local file called example.</dd>
<dt>
</dt><dd> gfcli (localhost/groot)&gt; cp file://example <a href="glfs://host/volume/example">glfs://host/volume/example</a></dd>
<dt>
</dt><dd> Copy the local file example to a remote Gluster volume on the host &#8216;host&#8217;.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
