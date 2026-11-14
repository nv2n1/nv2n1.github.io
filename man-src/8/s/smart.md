---
title: "smart(8)"
name: "smart"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smart/"
description: "smart – The Smart Package Manager"
---

<p>smart &#8211; The Smart Package Manager</p>
<h2>Synopsis</h2>
<p><code>smart</code> command [options] [arguments]</p>
<h2>Description</h2>
<p>The <code>Smart</code> Package Manager project has the ambitious objective of creating smart and portable algorithms for solving adequately the problem of managing software upgrading and installation. This tool works in all major distributions, and will bring notable advantages over native tools currently in use (APT, APT-RPM, YUM, URPMI, etc).</p>
<h2>Action commands</h2>
<pre>update
install
reinstall
upgrade
remove
check
fix
download
clean</pre>
<h2>Setup commands</h2>
<pre>channel
priority
mirror
flag</pre>
<h2>Query commands</h2>
<pre>search
query
info
stats</pre>
<p>Run &quot;smart command &#8211;help&quot; for more information.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Show program&#8217;s version number and exit</p>
<dt><code>&#8211;config-file=FILE</code></p>
<dd>Configuration file (default is &lt;data-dir&gt;/config)</p>
<dt><code>&#8211;data-dir=DIR</code></p>
<dd>Specifies the config file location &#8211; can take http, ftp urls and local file Data directory (default is /var/lib/smart/)</p>
<dt><code>&#8211;log-level=LEVEL</code></p>
<dd>Set the log level to level (debug, info, warning, error)</p>
<dt><code>&#8211;gui</code></p>
<dd>Use the default graphic interface</p>
<dt><code>&#8211;shell</code></p>
<dd>Use the default shell interface</p>
<dt><code>&#8211;interface=NAME</code></p>
<dd>Use the given interface</p>
<dt><code>&#8211;ignore-locks</code></p>
<dd>Don&#8217;t respect locking</p>
<dt><code>-o OPT, &#8211;option=OPT</code></p>
<dd>Set the option given by a name=value pair</dl>
<h2>Examples</h2>
<pre>smart install --help
smart install pkgname
smart --gui
smart --gui install pkgname
smart --shell</pre>
<h2>Files</h2>
<pre>/etc/smart/
/var/lib/smart/
/usr/lib/smart/
/usr/lib/smart/plugins/</pre>
<h2>See Also</h2>
<pre><a rel="nofollow" href="http://labix.org/smart">http://labix.org/smart</a></pre>
<h2>Author</h2>
<pre>Gustavo Niemeyer &lt;gustavo [at] niemeyer.net&gt;</pre>
