---

title: "gfls(1)"
name: "gfls"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfls/"
description: "gfls – manual page for gfls (glusterfs-coreutils) 0.2.0"
---

<h2>NAME</h2>
<p> gfls &#8211; manual page for gfls (glusterfs-coreutils) 0.2.0</p>
<p> <code>gfls</code> [<i>OPTION</i>]&#8230; <i>URL</i></p>
<p> list directory contents</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> do not ignore entries starting with .</dd>
<dt><code>-h</code>, <code>&#8211;human-readable</code></dt>
<dd> with <code>-l</code>, print sizes in human readable format (e.g., 1K 234M 2G)</dd>
<dt><code>-l</code></dt>
<dd> use a long listing format</dd>
<dt><code>-R</code>, <code>&#8211;recursive</code></dt>
<dd> list subdirectories recursively</dd>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></dt>
<dd> specify the port on which to connect</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> gfls <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></dd>
<dt>
</dt><dd> List the contents of /directory on the Gluster volume root on host localhost.</dd>
<dt>
</dt><dd> gfls -l <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></dd>
<dt>
</dt><dd> List the contents of /directory on the Gluster volume root on host localhost using the long listing format.</dd>
<dt>
</dt><dd> gfls -Rl <a href="glfs://localhost/groot/directory">glfs://localhost/groot/directory</a></dd>
<dt>
</dt><dd> Recursively list the contents of /directory on the Gluster volume groot on host localhost using the long listing format.</dd>
<dt>
</dt><dd> gfcli (localhost/groot)&gt; ls /</dd>
<dt>
</dt><dd> List the contents of the root of the connected Gluster volume.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Craig Cabrey.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Facebook, Inc. License GPLv3: GNU GPL version 3 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-3.0.en.html">http://www.gnu.org/licenses/gpl-3.0.en.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gfcli/">gfcli</a>(1) </p>
