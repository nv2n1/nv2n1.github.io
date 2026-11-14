---
title: "cacertdir_rehash(8)"
name: "cacertdir_rehash"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cacertdir_rehash/"
description: "cacertdir_rehash – simple script to create or update hash links to certificate files in a directory"
---

<p>cacertdir_rehash &#8211; simple script to create or update hash links to certificate files in a directory</p>
<h2>Synopsis</h2>
<p><code>cacertdir_rehash</code> &lt;directory&gt;</p>
<h2>Description</h2>
<p><code>cacertdir_rehash</code> is a simple shell script that is called by <code>authconfig</code> and <code>authconfig-gtk</code>. It uses <code>openssl</code> command line utility to create hash symbolic links of certificate files in the specified directory. </p>
<h2>Notes</h2>
<p>The script is internal to <code>authconfig</code> and its functionality and command line options might be changed in future. </p>
<h2>Return Codes</h2>
<p><code>cacertdir_rehash</code> returns 0 on success, non-zero on error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-authconfig/">authconfig</a>(8), <a href="/docs/linux/man/8-authconfig-gtk/">authconfig-gtk</a>(8), <a href="/docs/linux/man/1-openssl/">openssl</a>(1) </p>
<h2>Authors</h2>
<pre>Tomas Mraz &lt;tmraz [at] redhat.com&gt;</pre>
