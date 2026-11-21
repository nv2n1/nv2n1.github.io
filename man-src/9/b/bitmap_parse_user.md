---
title: "bitmap_parse_user(9)"
name: "bitmap_parse_user"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_parse_user/"
description: "bitmap_parse_user – convert an ASCII hex string in a user buffer into a bitmap"
---
<p>bitmap_parse_user &#8211; convert an ASCII hex string in a user buffer into a bitmap </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>int bitmap_parse_user(const char&nbsp;<wbr>__user&nbsp;<wbr>*&nbsp;<wbr></code><i>ubuf</i><code>, unsigned int&nbsp;<wbr></code><i>ulen</i><code>, unsigned long&nbsp;<wbr>*&nbsp;<wbr></code><i>maskp</i><code>, int&nbsp;<wbr></code><i>nmaskbits</i><code>);</code></dt>
</dl>
<h2>ARGUMENTS</h2>
<p> <i>ubuf</i> </p>
<dl>
<dd>  </dd>
<dd> <p> pointer to user buffer containing string. </p>
 </dd></dl>
<p> <i>ulen</i> </p>
<dl>
<dd> <p> buffer size in bytes. If string is smaller than this then it must be terminated with a \0. </p>
 </dd></dl>
<p> <i>maskp</i> </p>
<dl>
<dd> <p> pointer to bitmap array that will contain result. </p>
 </dd></dl>
<p> <i>nmaskbits</i> </p>
<dl>
<dd> <p> size of bitmap, in bits. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p>Wrapper for <code>__bitmap_parse</code>, providing it with user buffer. </p>
<p>We cannot have this as an inline function in bitmap.h because it needs linux/uaccess.h to get the <code>access_ok</code> declaration and this causes cyclic dependencies.  </p>
<h2>COPYRIGHT</h2>
<p> <br />
 </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">ARGUMENTS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COPYRIGHT</a></dt>
<dd>  </dd></dl>
