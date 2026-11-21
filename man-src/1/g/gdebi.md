---

title: "gdebi(1)"
name: "gdebi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdebi/"
description: "gdebi – Simple tool to install deb files"
---

<p> <code>gdebi</code> [<i>package.deb</i>]&#8230;</p>
<p> gdebi lets you install local deb packages resolving and installing its dependencies. apt does the same, but only for remote (http, ftp) located packages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show this help message and exit.</dd>
<dt><code>&#8211;n</code>, <code>&#8211;non-interactive</code></dt>
<dd> Run non-interactive (dangerous!).</dd>
<dt><code>&#8211;o</code> <i>APT_OPTS</i>, <code>&#8211;option=</code><i>APT_OPTS</i></dt>
<dd> Set an APT configuration option.</dd>
<dt><code>&#8211;q</code>, <code>&#8211;quiet</dt>
<dd> Do not show progress information.</dd>
<dt>&#8211;apt-line</code></dt>
<dd> Simulate only and print a apt-get install compatible line to stderr.</dd>
<dt><code>&#8211;root=</code><i>ROOTDIR</i></dt>
<dd> Use alternative root dir.</dd>
<dt></dt></dl>
<h2>SEE ALSO</h2>
<dd> Homepage: &lt;<a rel="nofollow" href="https://launchpad.net/gdebi/">https://launchpad.net/gdebi/</a>&gt;</dd>
<h2>AUTHOR</h2>
<p> This manual page was written by Gustavo Franco &lt;stratus [at] debian.org&gt; and Kartik Mistry &lt;kartik [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
