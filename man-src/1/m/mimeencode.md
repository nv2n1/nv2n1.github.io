---
title: "mimeencode(1)"
name: "mimeencode"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimeencode/"
---

<h2 class="name">NAME</h2>
 

 mimeencode - encode a file 

<h2>SYNOPSIS</h2>

 <pre>
    mimeencode
        Give usage.
     
    mimeencode [-d] encoding &lt;infile &gt;outfile
        Encode/decode stdin to stdout.
</pre>

<h2>DESCRIPTION</h2>

 Encode (or, with -d, decode) stdin with the given encoding, writing results to stdout. 

 This does not do <font SIZE="-1">MIME</font> parsing; it merely exercises the decoder modules.

<h2>AUTHOR</h2>

 Eryq, eryq [at] zeegee.com 

<h2>Index</h2>


