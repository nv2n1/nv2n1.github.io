---

title: "gpg-zip(1)"
name: "gpg-zip"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-zip/"
description: "gpg-zip – encrypt or sign files into an archive"
---

<p> <code>gpg-zip</code> [<code>OPTIONS</code>] <i>filename1</i> [<i>filename2, &#8230;</i>] <i>directory1</i> [<i>directory2, &#8230;</i>] </p>
<p> This manual page documents briefly the <code>gpg-zip</code> command. </p>
<p> <code>gpg-zip</code> IS DEPRECATED. PLEASE USE <a href="/docs/linux/man/1-gpgtar/">gpgtar</a>(1) instead. </p>
<p> <code>gpg-zip</code> encrypts or signs files into an archive. It is an gpg-ized tar using the same format as PGP&#8217;s PGP Zip. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code>, <code>&#8211;encrypt</code></dt>
<dd> Encrypt data. This option may be combined with <code>&#8211;symmetric</code> (for output that may be decrypted via a secret key or a passphrase).</dd>
<dt><code>-d</code>, <code>&#8211;decrypt</code></dt>
<dd> Decrypt data.</dd>
<dt><code>-c</code>, <code>&#8211;symmetric</code></dt>
<dd> Encrypt with a symmetric cipher using a passphrase. The default symmetric cipher used is CAST5, but may be chosen with the <code>&#8211;cipher-algo</code> option to <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1).</dd>
<dt><code>-s</code>, <code>&#8211;sign</code></dt>
<dd> Make a signature. See <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1).</dd>
<dt><code>-r</code>, <code>&#8211;recipient</code> <i>USER</i></dt>
<dd> Encrypt for user id <i>USER</i>. See <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1).</dd>
<dt><code>-u</code>, <code>&#8211;local-user</code> <i>USER</i></dt>
<dd> Use <i>USER</i> as the key to sign with. See <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1).</dd>
<dt><code>&#8211;list-archive</code></dt>
<dd> List the contents of the specified archive.</dd>
<dt><code>-o</code>, <code>&#8211;output</code> <i>FILE</i></dt>
<dd> Write output to specified file <i>FILE</i>.</dd>
<dt><code>&#8211;gpg</code><i> GPG</i></dt>
<dd> Use the specified command instead of <code>gpg</code>.</dd>
<dt><code>&#8211;gpg-args</code><i> ARGS</i></dt>
<dd> Pass the specified options to <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1).</dd>
<dt><code>&#8211;tar</code><i> TAR</i></dt>
<dd> Use the specified command instead of <code>tar</code>.</dd>
<dt><code>&#8211;tar-args</code><i> ARGS</i></dt>
<dd> Pass the specified options to <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1).</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Output a short usage information.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Output the program version. </dd>
</dl>
<h2>DIAGNOSTICS</h2>
<p> The program returns <code>0</code> if everything was fine, <code>1</code> otherwise. </p>
<h2>EXAMPLES</h2>
<p> Encrypt the contents of directory <i>mydocs</i> for user Bob to file <i>test1</i>:</p>
<dl>
<dt>
</dt><dd> <code>gpg-zip &#8211;encrypt &#8211;output test1 &#8211;gpg-args -r Bob mydocs</code></dd></dl>
<p> List the contents of archive <i>test1</i>:</p>
<dl>
<dt>
</dt><dd> <code>gpg-zip &#8211;list-archive test1</code> </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpgtar/">gpgtar</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2005 Free Software Foundation, Inc. Please report bugs to &lt;bug-gnupg [at] gnu.org&gt;. </p>
<p> This manpage was written by <code>Colin Tuckley</code> &lt;colin [at] tuckley.org&gt; and <code>Daniel Leidert</code> &lt;daniel.leidert [at] wgdd.de&gt; for the Debian distribution (but may be used by others). </p>
