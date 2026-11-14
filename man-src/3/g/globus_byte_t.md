---
title: "globus_byte_t(3)"
name: "globus_byte_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_byte_t/"
description: "globus_types.h –"
---

<h2 class="name">NAME</h2>
<p> globus_types.h &#8211; </p>
<p> Common Primitive Types.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_config.h&#8217;<br />
 #include &lt;stdlib.h&gt;<br />
 #include &lt;stdint.h&gt;<br />
 #include &lt;sys/types.h&gt;<br />
 #include &lt;sys/socket.h&gt; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_TRUE</code> 1<br />
 <i>True value for globus_bool_t. </i><br />
 #define <code>GLOBUS_FALSE</code> 0<br />
 <i>False value for globus_bool_t. </i><br />
 #define <code>GLOBUS_NULL</code> NULL<br />
 <i>NULL value. </i><br />
 #define <code>GLOBUS_SUCCESS</code> 0<br />
 <i>Generic success result</i> </p>
<p> Most Globus API functions return this value to indicate success, or some error constant or globus_result_t to indicate an error. &quot;<br />
 #define <code>GLOBUS_FAILURE</code> -1<br />
 <i>Generic failure result</i> </p>
<p> Some Globus API functions without good error handling return this value to indicate some undetermined error occurred. &quot;</p>
<h3>Typedefs</h3>
<p> typedef size_t <code>globus_size_t</code><br />
 <i>Standard size of memory object</i> </p>
<p> The globus_size_t is the size of a memory object. It is identical to size_t in all cases and doesn&#8217;t need to be used ever. &quot;<br />
 typedef socklen_t <code>globus_socklen_t</code><br />
 <i>Size of a socket length parameter. </i><br />
 typedef unsigned char <code>globus_byte_t</code><br />
 <i>Unsigned byte datatype</i> </p>
<p> This is used for byte-addressable arrays of arbitrary data which is not subject to sign extension. &quot;<br />
 typedef int <code>globus_bool_t</code><br />
 <i>Boolean type. </i><br />
 typedef uint32_t <code>globus_result_t</code> </p>
<h2>Detailed Description</h2>
<p> Common Primitive Types. </p>
<p> Defines the macros and typedefs common to all globus_common components.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_NULL NULL</h3>
<p> NULL value. From back long ago before NULL was standardized? No reason to use this on any modern system.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
