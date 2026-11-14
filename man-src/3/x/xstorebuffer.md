---
title: "xstorebuffer(3)"
name: "xstorebuffer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xstorebuffer/"
description: "XStoreBytes, XStoreBuffer, XFetchBytes, XFetchBuffer, XRotateBuffers – manipulate cut and paste buffers"
---

<p>XStoreBytes, XStoreBuffer, XFetchBytes, XFetchBuffer, XRotateBuffers &#8211; manipulate cut and paste buffers </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XStoreBytes(Display *<i>display</i>, char *<i>bytes</i>, int <i>nbytes</i>);</p>
<dd>int XStoreBuffer(Display *<i>display</i>, char *<i>bytes</i>, int <i>nbytes</i>, int <i>buffer</i>);</p>
<dd>char *XFetchBytes(Display *<i>display</i>, int *<i>nbytes_return</i>);</p>
<dd>char *XFetchBuffer(Display *<i>display</i>, int *<i>nbytes_return</i>, int <i>buffer</i>);</p>
<dd>int XRotateBuffers(Display *<i>display</i>, int <i>rotate</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>buffer</i></p>
<dd>Specifies the buffer in which you want to store the bytes or from which you want the stored data returned.</p>
<dt><i>bytes</i></p>
<dd>Specifies the bytes, which are not necessarily ASCII or null-terminated.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>nbytes</i></p>
<dd>Specifies the number of bytes to be stored.</p>
<dt><i>nbytes_return</i></p>
<dd>Returns the number of bytes in the buffer.</p>
<dt><i>rotate</i></p>
<dd>Specifies how much to rotate the cut buffers.</dl>
<h2>Description</h2>
<p>The data can have embedded null characters and need not be null-terminated. The cut buffer&#8217;s contents can be retrieved later by any client calling <code>XFetchBytes</code>. </p>
<p> <code>XStoreBytes</code> can generate a <code>BadAlloc</code> error. </p>
<p> If an invalid buffer is specified, the call has no effect. The data can have embedded null characters and need not be null-terminated. </p>
<p> <code>XStoreBuffer</code> can generate a <code>BadAlloc</code> error. </p>
<p> The <code>XFetchBytes</code> function returns the number of bytes in the nbytes_return argument, if the buffer contains data. Otherwise, the function returns NULL and sets nbytes to 0. The appropriate amount of storage is allocated and the pointer returned. The client must free this storage when finished with it by calling <code>XFree</code>. </p>
<p> The <code>XFetchBuffer</code> function returns zero to the nbytes_return argument if there is no data in the buffer or if an invalid buffer is specified. </p>
<p> <code>XFetchBuffer</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XRotateBuffers</code> function rotates the cut buffers, such that buffer 0 becomes buffer n, buffer 1 becomes n + 1 mod 8, and so on. This cut buffer numbering is global to the display. Note that <code>XRotateBuffers</code> generates <code>BadMatch</code> errors if any of the eight buffers have not been created. </p>
<p> <code>XRotateBuffers</code> can generate a <code>BadMatch</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
