---
title: "wl_argument(3)"
name: "wl_argument"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_argument/"
description: "wl_argument –"
---

<p>wl_argument &#8211; </p>
<p> A union representing all of the basic data types that can be passed along the wayland wire format.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-util.h&gt;

Public Attributes</code></pre>
<p> int32_t <code>i</code> </p>
<p> uint32_t <code>u</code> </p>
<p> wl_fixed_t <code>f</code> </p>
<p> const char * <code>s</code> </p>
<p> struct <code>wl_object</code> * <code>o</code> </p>
<p> uint32_t <code>n</code> </p>
<p> struct <code>wl_array</code> * <code>a</code> </p>
<p> int32_t <code>h</code></p>
<h2>Detailed Description</h2>
<p>A union representing all of the basic data types that can be passed along the wayland wire format. </p>
<p> This union represents all of the basic data types that can be passed in the wayland wire format. It is used by dispatchers and runtime-friendly versions of the event and request marshaling functions.</p>
<h2>Member Data Documentation</h2>
<h3>struct <code>wl_array</code>* wl_argument::a</h3>
<p>array</p>
<h3>wl_fixed_t wl_argument::f</h3>
<p>fixed point</p>
<h3>int32_t wl_argument::h</h3>
<p>file descriptor</p>
<h3>int32_t wl_argument::i</h3>
<p>signed integer</p>
<h3>uint32_t wl_argument::n</h3>
<p>new_id</p>
<h3>struct <code>wl_object</code>* wl_argument::o</h3>
<p>object</p>
<h3>const char* wl_argument::s</h3>
<p>string</p>
<h3>uint32_t wl_argument::u</h3>
<p>unsigned integer</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
