---
title: "gpgtar(1)"
name: "gpgtar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgtar/"
description: "gpgtar – Encrypt or sign files into an archive"
---

<h2 class="name">NAME</h2>
<p> <code>gpgtar</code> &#8211; Encrypt or sign files into an archive </p>
<h2>SYNOPSIS</h2>
<p> <code>gpgtar</code> [<i>options</i>] <i>filename1</i> <i>[ filename2, &#8230; ]</i> <i>directory1</i> <i>[ directory2, &#8230; ]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gpgtar</code> encrypts or signs files into an archive. It is an gpg-ized tar using the same format as used by PGP&#8217;s PGP Zip. </p>
<h2>OPTIONS</h2>
<p> <code>gpgtar</code> understands these options: </p>
<dl>
<dt><code>&#8211;create</code></p>
<dd> Put given files and directories into a vanilla &#8220;ustar&#8221; archive. </p>
<dt><code>&#8211;extract</code></p>
<dd> Extract all files from a vanilla &#8220;ustar&#8221; archive. </p>
<dt><code>&#8211;encrypt</code></p>
<dd> <code>-e</code> Encrypt given files and directories into an archive. This option may be combined with option <code>&#8211;symmetric</code> for an archive that may be decrypted via a secret key or a passphrase. </p>
<dt><code>&#8211;decrypt</code></p>
<dd> <code>-d</code> Extract all files from an encrypted archive. </p>
<dt><code>&#8211;sign</code></p>
<dd> <code>-s</code> Make a signed archive from the given files and directories. This can be combined with option <code>&#8211;encrypt</code> to create a signed and then encrypted archive. </p>
<dt><code>&#8211;list-archive</code></p>
<dd> <code>-t</code> List the contents of the specified archive. </p>
<dt><code>&#8211;symmetric</code></p>
<dd> <code>-c</code> Encrypt with a symmetric cipher using a passphrase. The default symmetric cipher used is AES-128, but may be chosen with the <code>&#8211;cipher-algo</code> option to <code>gpg</code>. </p>
<dt><code>&#8211;recipient </code><i>user</i></p>
<dd> <code>-r </code><i>user</i> Encrypt for user id <i>user</i>. For details see <code>gpg</code>. </p>
<dt><code>&#8211;local-user </code><i>user</i></p>
<dd> <code>-u </code><i>user</i> Use <i>user</i> as the key to sign with. For details see <code>gpg</code>. </p>
<dt><code>&#8211;output </code><i>file</i></p>
<dd> <code>-o </code><i>file</i> Write the archive to the specified file <i>file</i>. </p>
<dt><code>&#8211;verbose</code></p>
<dd> <code>-v</code> Enable extra informational output. </p>
<dt><code>&#8211;quiet</code></p>
<dd> <code>-q</code> Try to be as quiet as possible. </p>
<dt><code>&#8211;skip-crypto</code></p>
<dd> Skip all crypto operations and create or extract vanilla &#8220;ustar&#8221; archives. </p>
<dt><code>&#8211;dry-run</code></p>
<dd> Do not actually output the extracted files. </p>
<dt><code>&#8211;directory </code><i>dir</i></p>
<dd> <code>-C </code><i>dir</i> Extract the files into the directory <i>dir</i>. The default is to take the directory name from the input filename. If no input filename is known a directory named &#8216;<i>GPGARCH</i>&#8216; is used. For tarball creation, switch to directory <i>dir</i> before performing any operations. </p>
<dt><code>&#8211;files-from </code><i>file</i></p>
<dd> <code>-T </code><i>file</i> Take the file names to work from the file <i>file</i>; one file per line. </p>
<dt><code>&#8211;null</code></p>
<dd> Modify option <code>&#8211;files-from</code> to use a binary nul instead of a linefeed to separate file names. </p>
<dt><code>&#8211;utf8-strings</code></p>
<dd> Assume that the file names read by <code>&#8211;files-from</code> are UTF-8 encoded. This option has an effect only on Windows where the active code page is otherwise assumed. </p>
<dt><code>&#8211;openpgp</code></p>
<dd> This option has no effect because OpenPGP encryption and signing is the default. </p>
<dt><code>&#8211;cms</code></p>
<dd> This option is reserved and shall not be used. It will eventually be used to encrypt or sign using the CMS protocol; but that is not yet implemented. </p>
<dt><code>&#8211;set-filename </code><i>file</i></p>
<dd> Use the last component of <i>file</i> as the output directory. The default is to take the directory name from the input filename. If no input filename is known a directory named &#8216;<i>GPGARCH</i>&#8216; is used. This option is deprecated in favor of option <code>&#8211;directory</code>. </p>
<dt><code>&#8211;gpg </code><i>gpgcmd</i></p>
<dd> Use the specified command <i>gpgcmd</i> instead of <code>gpg</code>. </p>
<dt><code>&#8211;gpg-args </code><i>args</i></p>
<dd> Pass the specified extra options to <code>gpg</code>. </p>
<dt><code>&#8211;tar-args </code><i>args</i></p>
<dd> Assume <i>args</i> are standard options of the command <code>tar</code> and parse them. The only supported tar options are &quot;&#8211;directory&quot;, &quot;&#8211;files-from&quot;, and &quot;&#8211;null&quot; This is an obsolete options because those supported tar options can also be given directly. </p>
<dt><code>&#8211;version</code></p>
<dd> Print version of the program and exit. </p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help page and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Encrypt the contents of directory &#8216;<i>mydocs</i>&#8216; for user Bob to file &#8216;<i>test1</i>&#8216;: </p>
<dl>
<dt>
<dd>
<pre>
gpgtar --encrypt --output test1 -r Bob mydocs
</pre>
</dl>
<p> List the contents of archive &#8216;<i>test1</i>&#8216;: </p>
<dl>
<dt>
<dd>
<pre>
gpgtar --list-archive test1
</pre>
</dl>
<h2>DIAGNOSTICS</h2>
<p> The program returns 0 if everything was fine, 1 otherwise. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
