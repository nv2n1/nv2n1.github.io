---
title: "gridftpd(8)"
name: "gridftpd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gridftpd/"
description: "gridftpd – ARC GridFTP Server"
---

<p>gridftpd &#8211; ARC GridFTP Server</p>
<h2>Synopsis</h2>
<p><code>gridftpd</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>gridftpd is the daemon running the ARC GridFTP server. This server has plugins to allow job submission from Grid clients and to expose a local filesystem as a Grid Storage Element. For more information see &quot;The ARC Computing Element System Administrator Guide&quot; (NORDUGRID-MANUAL-20).</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>display help text</p>
<dt><code>-p</code> <i>number</i></p>
<dd>port on which to listen</p>
<dt><code>-c</code> <i>path</i></p>
<dd>full path to config file</p>
<dt><code>-n</code> <i>number</i></p>
<dd>maximum number of connections allowed</p>
<dt><code>-b</code> <i>number</i></p>
<dd>default buffer size</p>
<dt><code>-B</code> <i>number</i></p>
<dd>maximum buffer size</p>
<dt><code>-F</code></p>
<dd>run daemon in foreground</p>
<dt><code>-U</code> <i>user[:group]</i></p>
<dd>user (and group) name to switch to after starting</p>
<dt><code>-L</code> <i>path</i></p>
<dd>path to log file</p>
<dt><code>-P</code> <i>path</i></p>
<dd>path to pid file</p>
<dt><code>-d</code> <i>number</i></p>
<dd>debug level, from 0 (lowest verbosity) to 5 (highest verbosity) </p>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.nordugrid.org/">http://bugzilla.nordugrid.org/</a></p>
<h2>Copyright</h2>
<p>APACHE LICENSE Version 2.0</p>
<h2>Files</h2>
<p><code>/etc/arc.conf</code></p>
<h2>Author</h2>
<p>David Cameron &lt;d.g.cameron [at] fys.uio.no&gt;</p>
