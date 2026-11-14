---
title: "glusterd(8)"
name: "glusterd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glusterd/"
description: "Glusterd – Gluster elastic volume management daemon"
---

<p>Glusterd &#8211; Gluster elastic volume management daemon</p>
<h2>Synopsis</h2>
<p><code>glusterd</code> <i>[OPTION&#8230;]</i></p>
<h2>Description</h2>
<p>The glusterd daemon is used for elastic volume management. The daemon must be run on all export servers. </p>
<h2>Options</h2>
<h3>Basic options</h3>
<dl>
<dd><code>-l &lt;LOGFILE&gt;, &#8211;log-file=&lt;LOGFILE&gt;</code> File to use for logging.</p>
<dt><code>-L &lt;LOGLEVEL&gt;, &#8211;log-level=&lt;LOGLEVEL&gt;</code></p>
<dd>Logging severity. Valid options are TRACE, DEBUG, INFO, WARNING, ERROR and CRITICAL (the default is INFO).</p>
<dt><code>&#8211;debug</code></p>
<dd>Run the program in debug mode. This option sets <code>&#8211;no-daemon</code>, <code>&#8211;log-level</code> to DEBUG and <code>&#8211;log-file</code> to console.</p>
<dt><code>-N, &#8211;no-daemon</code></p>
<dd>Run the program in the foreground. </p>
</dl>
<h3>Miscellaneous Options:</h3>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd>Display this help.</p>
<dt><code>&#8211;usage</code></p>
<dd>Display a short usage message.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the program version. </p>
</dl>
<h2>Files</h2>
<p>/var/lib/glusterd/*</p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/1-fusermount/">fusermount</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/8-mount.glusterfs/">mount.glusterfs</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-glusterfs/">glusterfs</a></code>(8), <code><a href="//www.systutorials.com/docs/linux/man/8-gluster/">gluster</a></code>(8)</pre>
<h2>Copyright</h2>
<pre>Copyright(c) 2006-2011 Gluster, Inc. &lt;<a rel="nofollow" href="http://www.gluster.com">http://www.gluster.com</a>&gt;</pre>
