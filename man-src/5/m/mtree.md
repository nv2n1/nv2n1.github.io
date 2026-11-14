---
title: "mtree(5)"
name: "mtree"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mtree/"
description: "mtree – format of mtree dir hierarchy files"
---

<p><code>mtree</code> &#8211; format of mtree dir hierarchy files</p>
<h2>Description</h2>
<p>The format is a textual format that describes a collection of filesystem objects. Such files are typically used to create or verify directory hierarchies.</p>
<h3>General Format</h3>
<p>An file consists of a series of lines, each providing information about a single filesystem object. Leading whitespace is always ignored. When encoding file or pathnames, any backslash character or character outside of the 95 printable ASCII characters must be encoded as a a backslash followed by three octal digits. When reading mtree files, any appearance of a backslash followed by three octal digits should be converted into the corresponding character. Each line is interpreted independently as one of the following types:</p>
<dl>
<dt><code>Signature</code></p>
<dd>The first line of any mtree file must begin with &#8220;#mtree&#8221; If a file contains any full path entries, the first line should begin with &#8220;#mtree v2.0&#8221; otherwise, the first line should begin with &#8220;#mtree v1.0&#8221;</p>
<dt><code>Blank</code></p>
<dd>Blank lines are ignored.</p>
<dt><code>Comment</code></p>
<dd>Lines beginning with <code>#</code> are ignored.</p>
<dt><code>Special</code></p>
<dd>Lines beginning with <code>/</code> are special commands that influence the interpretation of later lines.</p>
<dt><code>Relative</code></p>
<dd>If the first whitespace-delimited word has no <code>/</code> characters, it is the name of a file in the current directory. Any relative entry that describes a directory changes the current directory.</p>
<dt><code>dot-dot</code></p>
<dd>As a special case, a relative entry with the filename .. changes the current directory to the parent directory. Options on dot-dot entries are always ignored.</p>
<dt><code>Full</code></p>
<dd>If the first whitespace-delimited word has a <code>/</code> character after the first character, it is the pathname of a file relative to the starting directory. There can be multiple full entries describing the same file.</dl>
<p> Some tools that process files may require that multiple lines describing the same file occur consecutively. It is not permitted for the same file to be mentioned using both a relative and a full file specification.</p>
<h3>Special commands</h3>
<p>Two special commands are currently defined:</p>
<dl>
<dt><code>/set</code></p>
<dd>This command defines default values for one or more keywords. It is followed on the same line by one or more whitespace-separated keyword definitions. These definitions apply to all following files that do not specify a value for that keyword.</p>
<dt><code>/unset</code></p>
<dd>This command removes any default value set by a previous <code>/set</code> command. It is followed on the same line by one or more keywords separated by whitespace.</dl>
<h3>Keywords</h3>
<p>After the filename, a full or relative entry consists of zero or more whitespace-separated keyword definitions. Each such definition consists of a key from the following list immediately followed by an &#8216;=&#8217; sign and a value. Software programs reading mtree files should warn about unrecognized keywords. Currently supported keywords are as follows:</p>
<dl>
<dt><code>cksum</code></p>
<dd>The checksum of the file using the default algorithm specified by the <a href="/docs/linux/man/1-cksum/">cksum</a>(1) utility.</p>
<dt><code>contents</code></p>
<dd>The full pathname of a file that holds the contents of this file.</p>
<dt><code>flags</code></p>
<dd>The file flags as a symbolic name. See <a href="/docs/linux/man/1-chflags/">chflags</a>(1) for information on these names. If no flags are to be set the string &#8220;none&#8221; may be used to override the current default.</p>
<dt><code>gid</code></p>
<dd>The file group as a numeric value.</p>
<dt><code>gname</code></p>
<dd>The file group as a symbolic name.</p>
<dt><code>ignore</code></p>
<dd>Ignore any file hierarchy below this file.</p>
<dt><code>link</code></p>
<dd>The target of the symbolic link when type=link.</p>
<dt><code>md5</code></p>
<dd>The MD5 message digest of the file.</p>
<dt><code>md5digest</code></p>
<dd>A synonym for <code>md5</code></p>
<dt><code>mode</code></p>
<dd>The current file&#8217;s permissions as a numeric (octal) or symbolic value.</p>
<dt><code>nlink</code></p>
<dd>The number of hard links the file is expected to have.</p>
<dt><code>nochange</code></p>
<dd>Make sure this file or directory exists but otherwise ignore all attributes.</p>
<dt><code>ripemd160digest</code></p>
<dd>The <code>RIPEMD160</code> message digest of the file.</p>
<dt><code>rmd160</code></p>
<dd>A synonym for <code>ripemd160digest</code></p>
<dt><code>rmd160digest</code></p>
<dd>A synonym for <code>ripemd160digest</code></p>
<dt><code>sha1</code></p>
<dd>The <code>FIPS</code> 160-1 (&#8220;<code>SHA-1</code> &#8221; ) message digest of the file.</p>
<dt><code>sha1digest</code></p>
<dd>A synonym for <code>sha1</code></p>
<dt><code>sha256</code></p>
<dd>The <code>FIPS</code> 180-2 (&#8220;<code>SHA-256</code> &#8221; ) message digest of the file.</p>
<dt><code>sha256digest</code></p>
<dd>A synonym for <code>sha256</code></p>
<dt><code>size</code></p>
<dd>The size, in bytes, of the file.</p>
<dt><code>time</code></p>
<dd>The last modification time of the file.</p>
<dt><code>type</code></p>
<dd>The type of the file; may be set to any one of the following: </p>
<dt><code>block</code></p>
<dd>block special device</p>
<dt><code>char</code></p>
<dd>character special device</p>
<dt><code>dir</code></p>
<dd>directory</p>
<dt><code>fifo</code></p>
<dd>fifo</p>
<dt><code>file</code></p>
<dd>regular file</p>
<dt><code>link</code></p>
<dd>symbolic link</p>
<dt><code>socket</code></p>
<dd>socket</dl>
<dt><code>uid</code></p>
<dd>The file owner as a numeric value.</p>
<dt><code>uname</code></p>
<dd>The file owner as a symbolic name.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cksum/">cksum</a>(1), <a href="/docs/linux/man/1-find/">find</a>(1), <a href="/docs/linux/man/8-mtree/">mtree</a>(8)</p>
<h2>Bugs</h2>
<p>The Fx implementation of mtree does not currently support the 2.0 format. The requirement for a &#8220;#mtree&#8221; signature line is new and not yet widely implemented.</p>
<h2>History</h2>
<p>The utility appeared in BSD 4.3 Reno The <code>MD5</code> digest capability was added in Fx 2.1 , in response to the widespread use of programs which can spoof <a href="/docs/linux/man/1-cksum/">cksum</a>(1). The <code>SHA-1</code> and <code>RIPEMD160</code> digests were added in Fx 4.0 , as new attacks have demonstrated weaknesses in <code>MD5</code> The <code>SHA-256</code> digest was added in Fx 6.0 . Support for file flags was added in Fx 4.0 , and mostly comes from Nx . The &#8220;full&#8221; entry format was added by Nx .</p>
