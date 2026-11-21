---

title: "ckeygen(1)"
name: "ckeygen"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ckeygen/"
description: "ckeygen – manipulate public/private keys"
---

<p> ckeygen &#8211; manipulate public/private keys</p>
<h2>SYNOPSIS</h2>
<p> <code>ckeygen [-b </code><i>bits</i>] [-f <i>filename</i>] [-t <i>type</i>] <code>[-C </code><i>comment</i>] [-N <i>new passphrase</i>] [-P <i>old passphrase</i>] <code>[-l] [-p] [-q] [-y]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;bits</code> &lt;bits&gt;</dt>
<dd> Number of bits in the key to create (default: 1024)</dd>
<dt><code>-f</code>, <code>&#8211;filename</code> &lt;file name&gt;</dt>
<dd> Filename of the key file.</dd>
<dt><code>-t</code>, <code>&#8211;type</code> &lt;type&gt;</dt>
<dd> Type of key (rsa or dsa).</dd>
<dt><code>-C</code>, <code>&#8211;comment</code> &lt;comment&gt;</dt>
<dd> Provide a new comment.</dd>
<dt><code>-N</code>, <code>&#8211;newpass</code> &lt;pass phrase&gt;</dt>
<dd> Provide new passphrase.</dd>
<dt><code>-P</code>, <code>&#8211;pass</code> &lt;pass phrase&gt;</dt>
<dd> Provide old passphrase.</dd>
<dt><code>-l</code>, <code>&#8211;fingerprint</code></dt>
<dd> Show fingerprint of key file.</dd>
<dt><code>-p</code>, <code>&#8211;changepass</code></dt>
<dd> Change passphrase of private key file.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Be quiet.</dd>
<dt><code>&#8211;no-passphrase</code></dt>
<dd> Create the key with no passphrase.</dd>
<dt><code>-y</code>, <code>&#8211;showpub</code></dt>
<dd> Read private key file and print public key.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display version number only.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Manipulate public/private keys in various ways. If no filename is given, a file name will be requested interactively.</p>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on ckeygen&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2011 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), <a href="/docs/linux/man/1-conch/">conch</a>(1) </p>
