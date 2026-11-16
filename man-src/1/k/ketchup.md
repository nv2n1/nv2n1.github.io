---
title: "ketchup(1)"
name: "ketchup"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ketchup/"
description: "ketchup – Utility to update the kernel source"
---

<h2 class="name">NAME</h2>
<p> ketchup &#8211; Utility to update the kernel source </p>
<h2>SYNOPSIS</h2>
<p> <code>ketchup</code> [<i>options</i>] <i>&lt;ver&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> This tool synchronises a local kernel tree with a desired kernel version and patch set from a kernel.org mirror. The default requires a GPG key on your keyring, to verify the identity of the patches and source archives. Entire kernel images are not downloaded unless necessary, so bandwidth is saved. Patches are applied and removed as necessary to attain the requested version.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>-a</code> <code>&#8211;archive</code> (/home/baruch/.ketchup)</dt>
<dd>cache directory</dd>
<dt> <code>-d</code> <code>&#8211;directory</code> (.)</dt>
<dd>directory to update</dd>
<dt> <code>-f</code> <code>&#8211;full-tarball</code></dt>
<dd>if unpacking a tarball, download the latest</dd>
<dt> <code>-g</code> <code>&#8211;gpg-path</code> (/usr/bin/gpg)</dt>
<dd>path for GnuPG</dd>
<dt> <code>-G</code> <code>&#8211;no-gpg</code></dt>
<dd>disable GPG signature verification</dd>
<dt> <code>-k</code> <code>&#8211;kernel-url</code> (<a rel="nofollow" href="http://www.kernel.org/pub/linux/kernel)">http://www.kernel.org/pub/linux/kernel)</a></dt>
<dd>base url for kernel.org mirror</dd>
<dt> <code>-l</code> <code>&#8211;list-trees</code></dt>
<dd>list supported trees</dd>
<dt> <code>-m</code> <code>&#8211;show-makefile</code></dt>
<dd>output version in makefile &lt;arg&gt;</dd>
<dt> <code>-n</code> <code>&#8211;dry-run</code></dt>
<dd>don&#8217;t download or apply patches</dd>
<dt> <code>-p</code> <code>&#8211;show-previous</code></dt>
<dd>output version previous to &lt;arg&gt;</dd>
<dt> <code>-q</code> <code>&#8211;quiet</code></dt>
<dd>reduce output</dd>
<dt> <code>-r</code> <code>&#8211;rename-directory</code></dt>
<dd>rename updated directory to linux-&lt;v&gt;</dd>
<dt> <code>-s</code> <code>&#8211;show-latest</code></dt>
<dd>output the latest version of &lt;arg&gt;</dd>
<dt> <code>-u</code> <code>&#8211;show-url</code></dt>
<dd>output URL for &lt;arg&gt;</dd>
<dt> <code>-w</code> <code>&#8211;wget</code> (/usr/bin/wget)</dt>
<dd>command to use for wget</dd></dl>
<h2>CONFIGURATION</h2>
<p> Ketchup will read files named <i>.ketchuprc</i> in $HOME and in the target kernel directory, with the kernel directory taking precedence. </p>
<p> A <i>.ketchuprc</i> file uses the Python syntax and may set the following variables:</p>
<dl>
<dt> <code>default_tree</code></dt>
<dd>The <code>default_tree</code> option specifies the kernel version to work with if one is not given on the command line.</dd>
<dt> <code>precommand</code></dt>
<dd>The <code>precommand</code> option specifies a command to run before synchronising the kernel tree to the required version.</dd>
<dt> <code>postcommand</code></dt>
<dd>The <code>postcommand</code> option specifies a command to run after synchronising the kernel tree to the required version.</dd></dl>
<h2>AUTHOR</h2>
<p> ketchup was written by Matt Mackall &lt;mpm [at] selenic.com&gt;. </p>
<p> This manual page was written by Baruch Even &lt;baruch [at] debian.org&gt;, for the Debian project (but may be used by others). Description text taken from a former packaging attempt of Jack Wasey &lt;debian [at] jackwasey.com&gt;. </p>
<h2>Index</h2>
