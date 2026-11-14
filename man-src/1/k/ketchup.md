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
<dt> <code>-a</code> <code>&#8211;archive</code> (/home/baruch/.ketchup)</p>
<dt>
<dd>
<dd>cache directory</p>
<dt> <code>-d</code> <code>&#8211;directory</code> (.)</p>
<dt>
<dd>
<dd>directory to update</p>
<dt> <code>-f</code> <code>&#8211;full-tarball</code></p>
<dt>
<dd>
<dd>if unpacking a tarball, download the latest</p>
<dt> <code>-g</code> <code>&#8211;gpg-path</code> (/usr/bin/gpg)</p>
<dt>
<dd>
<dd>path for GnuPG</p>
<dt> <code>-G</code> <code>&#8211;no-gpg</code></p>
<dt>
<dd>
<dd>disable GPG signature verification</p>
<dt> <code>-k</code> <code>&#8211;kernel-url</code> (<a rel="nofollow" href="http://www.kernel.org/pub/linux/kernel)">http://www.kernel.org/pub/linux/kernel)</a></p>
<dt>
<dd>
<dd>base url for kernel.org mirror</p>
<dt> <code>-l</code> <code>&#8211;list-trees</code></p>
<dt>
<dd>
<dd>list supported trees</p>
<dt> <code>-m</code> <code>&#8211;show-makefile</code></p>
<dt>
<dd>
<dd>output version in makefile &lt;arg&gt;</p>
<dt> <code>-n</code> <code>&#8211;dry-run</code></p>
<dt>
<dd>
<dd>don&#8217;t download or apply patches</p>
<dt> <code>-p</code> <code>&#8211;show-previous</code></p>
<dt>
<dd>
<dd>output version previous to &lt;arg&gt;</p>
<dt> <code>-q</code> <code>&#8211;quiet</code></p>
<dt>
<dd>
<dd>reduce output</p>
<dt> <code>-r</code> <code>&#8211;rename-directory</code></p>
<dt>
<dd>
<dd>rename updated directory to linux-&lt;v&gt;</p>
<dt> <code>-s</code> <code>&#8211;show-latest</code></p>
<dt>
<dd>
<dd>output the latest version of &lt;arg&gt;</p>
<dt> <code>-u</code> <code>&#8211;show-url</code></p>
<dt>
<dd>
<dd>output URL for &lt;arg&gt;</p>
<dt> <code>-w</code> <code>&#8211;wget</code> (/usr/bin/wget)</p>
<dt>
<dd>
<dd>command to use for wget</dl>
<h2>CONFIGURATION</h2>
<p> Ketchup will read files named <i>.ketchuprc</i> in $HOME and in the target kernel directory, with the kernel directory taking precedence. </p>
<p> A <i>.ketchuprc</i> file uses the Python syntax and may set the following variables:</p>
<dl>
<dt> <code>default_tree</code></p>
<dt>
<dd>
<dd>The <code>default_tree</code> option specifies the kernel version to work with if one is not given on the command line.</p>
<dt> <code>precommand</code></p>
<dt>
<dd>
<dd>The <code>precommand</code> option specifies a command to run before synchronising the kernel tree to the required version.</p>
<dt> <code>postcommand</code></p>
<dt>
<dd>
<dd>The <code>postcommand</code> option specifies a command to run after synchronising the kernel tree to the required version.</dl>
<h2>AUTHOR</h2>
<p> ketchup was written by Matt Mackall &lt;mpm [at] selenic.com&gt;. </p>
<p> This manual page was written by Baruch Even &lt;baruch [at] debian.org&gt;, for the Debian project (but may be used by others). Description text taken from a former packaging attempt of Jack Wasey &lt;debian [at] jackwasey.com&gt;. </p>
<h2>Index</h2>
