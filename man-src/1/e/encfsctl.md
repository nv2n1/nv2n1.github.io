---
title: "encfsctl(1)"
name: "encfsctl"
section: "1"
letter: "e"
url: "/docs/linux/man/1-encfsctl/"
description: "encfsctl – administrative tool for working with EncFS filesystems"
---

<h2 class="name">NAME</h2>
<p> encfsctl &#8211; administrative tool for working with EncFS filesystems </p>
<h2>SYNOPSIS</h2>
<p> <code>encfsctl</code> [<i>command</i> <i>command_args</i>] </p>
<p> <code>encfsctl</code> [info] <i>rootdir</i> </p>
<p> <code>encfsctl</code> passwd <i>rootdir</i> </p>
<p> <code>encfsctl</code> showcruft <i>rootdir</i> </p>
<p> <code>encfsctl</code> decode [&#8211;extpass=prog] <i>rootdir</i> [encoded name &#8230;] </p>
<p> <code>encfsctl</code> encode [&#8211;extpass=prog] <i>rootdir</i> [plaintext name &#8230;] </p>
<p> <code>encfsctl</code> cat [&#8211;extpass=prog] [&#8211;reverse] <i>rootdir</i> &lt;(cipher|plain) filename&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>encfsctl</code> is an administrative tool for working with EncFS filesystems. It is capable of changing the user supplied password, displaying basic information about an encrypted volume, and other related operations.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>info</code></p>
<dd> Display basic information about the filesystem. Takes a single argument, <i>rootdir</i>, which is the root directory of the encrypted filesystem. The filesystem need not be mounted. <code>Info</code> is also the default command if only a root directory is provided on the command line.</p>
<dt><code>passwd</code></p>
<dd> Allows changing the password of the encrypted filesystem. The user will be prompted for the existing password and the new password.</p>
<dt><code>showcruft</code></p>
<dd> Recursively search through the entire volume and display all files which are not decodable (only checks filename encoding, not block <font SIZE="-1">MAC</font> headers). This might be useful for cleanup in case you&#8217;ve made use of features which create files which are not decodable under the primary key.</p>
<dt><code>decode</code></p>
<dd> Allows you to specify an encoded name on the command line, and displays decoded version. This is mostly useful for debugging, as debug messages always display encrypted filenames (to avoid leaking sensitive data through the debug channels). So this command provides a way to decode the filenames. </p>
<p> The <code>&#8211;extpass</code> option can be used to specify the program which returns the password &#8211; just like with encfs. </p>
<p> If no names are specified on the command line, then a list of filenames will be read from stdin and decoded.</p>
<dt><code>encode</code></p>
<dd> Allows you to specify a filename on the command line, and displays its encoded version. This is useful if e.g. you are taking a backup of an encrypted directory and would like to exclude some files. </p>
<p> The <code>&#8211;extpass</code> option can be used to specify the program which returns the password &#8211; just like with encfs. </p>
<p> If no names are specified on the command line, then a list of filenames will be read from stdin and encoded.</p>
<dt><code>cat</code></p>
<dd> Decodes and <code>cat</code>s the content of an encrypted file. The filename can be given in a plain or ciphered form. With <code>&#8211;reverse</code> The file content will instead be encrypted.</dl>
<h2>EXAMPLES</h2>
<p> Show information about an encrypted filesystem: </p>
<pre>
 % encfsctl info ~/.crypt
 Version 5 configuration; created by EncFS 1.1 (revision 20040504)
 Filesystem cipher: &quot;ssl/aes&quot; , version 2:1:1
 Filename encoding: &quot;nameio/block&quot; , version 3:0:1
 Key Size: 192 bits
 Block Size: 512 bytes
 Each file contains 8 byte header with unique IV data.
 Filesname encoded using IV chaining mode.
</pre>
<h2>DISCLAIMER</h2>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> Please refer to the &#8220;<font SIZE="-1">COPYING&#8221;</font> file distributed with <code>encfs</code> for complete details.</p>
<h2>AUTHORS</h2>
<p> <code>EncFS</code> was written by <code>Valient Gough &lt;vgough [at] pobox.com&gt;</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-encfs/">encfs</a></code>(1) </p>
<h2>Index</h2>
