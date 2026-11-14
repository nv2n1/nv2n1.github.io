---
title: "cryptdir(1)"
name: "cryptdir"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cryptdir/"
description: "cryptdir – encrypt/decrypt all files in a directory"
---

<h2 class="name">NAME</h2>
<p> cryptdir &#8211; encrypt/decrypt all files in a directory </p>
<h2>SYNOPSIS</h2>
<p> <code>cryptdir</code> [ <i>dir</i> ]<br />
 <code>decryptdir</code> [ <i>dir</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>cryptdir</code> encrypts all files in the current directory (or the given directory if one is provided as an argument). When called as decryptdir (i.e., same program, different name), all files are decrypted. </p>
<h2>NOTES</h2>
<p> When encrypting, you are prompted twice for the password as a precautionary measure. It would be a disaster to encrypt files with a password that wasn&#8217;t what you intended. </p>
<p> In contrast, when decrypting, you are only prompted once. If it&#8217;s the wrong password, no harm done. </p>
<p> Encrypted files have the suffix .crypt appended. This prevents files from being encrypted twice. The suffix is removed upon decryption. Thus, you can easily add files to an encrypted directory and run cryptdir on it without worrying about the already encrypted files.</p>
<h2>BUGS</h2>
<p> The man page is longer than the program. </p>
<h2>SEE ALSO</h2>
<p> <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<h2>Index</h2>
