---
title: "brlapi_handle_t(3)"
name: "brlapi_handle_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_handle_t/"
description: "BrlAPI handles –"
---

<h2 class="name">NAME</h2>
<p> BrlAPI handles &#8211; </p>
<h3>Typedefs</h3>
<p> typedef struct <code>brlapi_handle_t</code> <code>brlapi_handle_t</code> </p>
<h3>Functions</h3>
<p> size_t <code>BRLAPI_STDCALL</code> <code>brlapi_getHandleSize</code> (void) </p>
<h2>Detailed Description</h2>
<p> Each function provided by BrlAPI comes in two versions. </p>
<dl>
<dt>1.</p>
<dd> A version whose name is prefixed by brlapi_ for clients opening only one simultaneous connection with BrlAPI (most frequen case)</dl>
<dl>
<dt>2.</p>
<dd> A version whose name is prefixed by brlapi__ for use by clients wishing to open more than one connection to BrlAPI.</dl>
<p> A function called brlapi__foo is used in exactly the same way as its brlapi_foo counterpart, except that it takes an additional argument (the first one), which is a handle letting the client refer to a given connection in a similar manner to what file descriptors do. </p>
<p> In case you want to check that your code is not erroneously using brlapi_foo functions, define BRLAPI_NO_SINGLE_SESSION before including &lt;<code>brlapi.h</code>&gt;: that will disable the declaration of all single session functions.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>brlapi_handle_t</code> <code>brlapi_handle_t</code></h3>
<p> Type for BrlAPI hanles</p>
<h2>Function Documentation</h2>
<h3>size_t <code>BRLAPI_STDCALL</code> brlapi_getHandleSize (void)</h3>
<p> Returns the size of an object of type brlapi_handle_t in bytes</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for BrlAPI from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
