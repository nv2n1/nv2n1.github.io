---
title: "bcrypt(1)"
name: "bcrypt"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcrypt/"
description: "bcrypt – blowfish file encryption"
---

<h2>NAME</h2>
<p> bcrypt &#8211; blowfish file encryption</p>
<h2>SYNOPSIS</h2>
<p> <code>bcrypt</code> [-orc]<code>[-s</code>N] <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bcrypt</code> encrypts and decrypts files using the <i>blowfish </i> algorithm. </p>
<p> Encrypted files will be saved with an extension of <code>.bfe</code>. Any files ending in <code>.bfe</code> will be assumed to be encrypted with <code>bcrypt</code> and will attempt to decrypt them. Any other input files will be encrypted. If more than one type of file is given, <code>bcrypt</code> will process all files which are the same as the first filetype given. </p>
<p> By default, <code>bcrypt</code> will compress input files before encryption, remove input files after they are processed (assuming they are processed successfully) and overwrite input files with random data to prevent data recovery. </p>
<p> Passphrases may be between 8 and 56 characters. Regardless of the passphrase size, the key is hashed internally to 448 bits &#8211; the largest keysize supported by the <i>blowfish</i> algorithm. However, it is still wise to use a strong passphrase.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code></p>
<dd> print output to standard out. Implies -r.</p>
<dt><code>-c</code></p>
<dd> DO NOT compress files before encryption.</p>
<dt><code>-r</code></p>
<dd> DO NOT remove input files after processing</p>
<dt><code>-s</code><i>N</i></p>
<dd> How many times to overwrite input files with random data before deleting. The default number of overwrites is 3. Use -s0 to disable this feature. No effect if -r is supplied.</dl>
<h2>NOTES</h2>
<p> <code>The</code> -o ,<code>-r </code>,and<code> -c </code>options each have the opposite effects if the appropriate settings are altered from the defaults in config.h. To determine what effect each of these have on your system, run <code>bcrypt</code> without any options. </p>
<p> Encrypted files should be compatible between most systems. Binary compatibility has been tested on all supported systems. There is a list of supported systems in the README file that was included with this software.</p>
<h2>BUGS</h2>
<p> Probably. If you find that it will not compile and run on your system, or that encrypted files are not compatible with other platforms, its probably because I don&#8217;t have access to the platform in question. Patches or access to an unsupported machine are welcome.</p>
<h2>AUTHOR</h2>
<dl>
<dt>johnny shelley</p>
<dd> &lt;jshelley [at] cahaus.com&gt;, &lt;jshelley [at] ictransnet.com&gt;</dl>
<h2>DISTRIBUTION</h2>
<p> <code>bcrypt</code> includes Paul Kocher&#8217;s implementation of the <i>blowfish</i> algorithm. The version distributed with <code>bcrypt</code> has been altered. Original sources are available from <a rel="nofollow" href="http://www.counterpane.com/bfsh-koc.zip">http://www.counterpane.com/bfsh-koc.zip</a> </p>
<h2>Index</h2>
