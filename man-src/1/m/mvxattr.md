---

title: "mvxattr(1)"
name: "mvxattr"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mvxattr/"
description: "mvxattr – Recursively rename extended attributes"
---

<p> mvxattr &#8211; Recursively rename extended attributes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
</dt><dd>mvxattr {-s STRING, &#8211;from=STRING} {-d STRING, &#8211;to=STRING} [-l, &#8211;follow-symlinks] [-p, &#8211;print] [-v, &#8211;verbose] [-f, &#8211;force] {PATH&nbsp;<wbr>[PATH &#8230;]}</dd></dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code>samba</code>(1) suite. </p>
<p> mvxattr is a simple utility to recursively rename extended attributes. </p>
<p> By default all symlinks are ignored, use <code>-l</code> to follow them.</p>
<h2>OPTIONS</h2>
<p> -s STRING, &#8211;from=STRING</p>
<dl>
<dt>
</dt><dd> Source xattr name</dd></dl>
<p> -d STRING, &#8211;to=STRING</p>
<dl>
<dt>
</dt><dd> Destination xattr name</dd></dl>
<p> -l, &#8211;follow-symlinks</p>
<dl>
<dt>
</dt><dd> Follow symlinks, the default is to ignore them.</dd></dl>
<p> -p, &#8211;print</p>
<dl>
<dt>
</dt><dd> Print files where the xattr got renamed.</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Print files as they are checked.</dd></dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
</dt><dd> Force overwriting of destination xattr.</dd></dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The mvxattr manpage was written by Ralph Boehme. </p>
