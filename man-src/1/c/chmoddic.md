---
title: "chmoddic(1)"
name: "chmoddic"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chmoddic/"
---

<h2>NAME</h2>

 <tt>chmoddic</tt> - change access rights for a directory

<h2>SYNOPSIS</h2>

 <pre><code>
chmoddic [{(-cs | - cannaserver} canna-server] {+ | -}{r|w|rw|wr} 
[-G] dicname
</code></pre>

<h2>DESCRIPTION</h2>

 Add and/or remove READ/WRITE rights for the dictionary <i>dicname</i>. The access rights for the dictionary cannot be changed if it is being used.

<h2>OPTION</h2>

<dl>
<dt><tt>-cs </tt><i>cannaserver</i> (or <tt>-cannaserver </tt><i>canna-server</i>)
</dt><dd> Specify the server machine which has a dictionary to be changed.
</dd><dt><tt>-</tt>
</dt><dd> Remove the following access rights.
</dd><dt><tt>+</tt>
</dt><dd> Add the following access rights.
</dd><dt><tt>r</tt>
</dt><dd> Change READ rights. w can be specified at the same time.
</dd><dt><tt>w</tt>
</dt><dd> Change WRITE rights. r can be specified at the same time.
</dd><dt><tt>-G</tt>
</dt><dd> Change the access rights for the user's own group dictionary.</dd></dl>

<h2>EXAMPLE</h2>

<dl>
<dt><tt>chmoddic -r +w test</tt>
</dt><dd> Remove READ rights from and add WRITE rights for user dictionary test.
</dd><dt><tt>chmoddic +wr -G test</tt>
</dt><dd> Add READ/WRITE rights to group dictionary test.</dd></dl>

<h2>SEE ALSO</h2>

 <tt><a HREF="/docs/linux/man/1-lsdic/">lsdic</a></tt>(1), <tt><a HREF="/docs/linux/man/1-mkdic/">mkdic</a></tt>(1) 

<h2>Index</h2>


