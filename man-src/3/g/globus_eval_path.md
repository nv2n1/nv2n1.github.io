---
title: "globus_eval_path(3)"
name: "globus_eval_path"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_eval_path/"
description: "Globus Common API –"
---

<h2 class="name">NAME</h2>
<p> Globus Common API &#8211; </p>
<p> Common Data Structures and Functions.</p>
<h3>Modules</h3>
<p> <code>Globus Callback</code><br />
 <i>Globus Callback Function Interface. </i><br />
 <code>Globus Error API</code> </p>
<p> <code>FIFO Queue</code><br />
 <i>FIFO Queue Implementation. </i><br />
 <code>Handle Table for Reference Counting Data</code> </p>
<p> <code>Hash Table</code> </p>
<p> <code>Linked List</code> </p>
<p> <code>Memory Pool</code> </p>
<p> <code>Module Activation Management</code> </p>
<p> <code>Priority Queue</code> </p>
<p> <code>Threading</code><br />
 <i>Portable Thread Abstraction. </i><br />
 <code>Thread Pooling</code> </p>
<p> <code>URL String Parser</code> </p>
<p> <code>Globus UUID Generator</code><br />
 <i>UUIDs. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_COMMON_MODULE</code> (&amp;globus_i_common_module)<br />
 <i>Globus Common Module Descriptor. </i><br />
 #define <code>GLOBUS_TILDE_EXPAND</code><br />
 <i>Expand ~. </i><br />
 #define <code>GLOBUS_TILDE_USER_EXPAND</code><br />
 <i>Expand ~user. </i><br />
 #define <code>GLOBUS_TRUE</code> 1<br />
 <i>True value for globus_bool_t. </i><br />
 #define <code>GLOBUS_FALSE</code> 0<br />
 <i>False value for globus_bool_t. </i><br />
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
<h3>Functions</h3>
<p> <code>globus_result_t</code> <code>globus_eval_path</code> (const char *pathstring, char **bufp) </p>
<p> int <code>globus_tilde_expand</code> (unsigned long options, <code>globus_bool_t</code> url_form, char *inpath, char **outpath)<br />
 <i>Expand ~ and/or ~user in path strings. </i></p>
<h2>Detailed Description</h2>
<p> Common Data Structures and Functions. </p>
<h2>Container Data Types</h2>
<dl>
<dt>&bull;</p>
<dd> <code>Linked List</code></p>
<dt>&bull;</p>
<dd> <code>FIFO Queue</code></p>
<dt>&bull;</p>
<dd> <code>Handle Table for Reference Counting Data</code></p>
<dt>&bull;</p>
<dd> <code>Hash Table</code></p>
<dt>&bull;</p>
<dd> <code>Priority Queue</code></dl>
<h2>Common Runtime Components</h2>
<dl>
<dt>&bull;</p>
<dd> <code>Threading</code></p>
<dt>&bull;</p>
<dd> <code>Globus Callback</code></p>
<dt>&bull;</p>
<dd> <code>Memory Pool</code></p>
<dt>&bull;</p>
<dd> <code>Module Activation Management</code></dl>
<h2>Error Handling</h2>
<dl>
<dt>&bull;</p>
<dd> <code>Globus Error API</code></dl>
<h2>Miscellaneous Utilities</h2>
<dl>
<dt>&bull;</p>
<dd> <code>Globus UUID Generator</code></p>
<dt>&bull;</p>
<dd> <code>URL String Parser</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef int <code>globus_bool_t</code></h3>
<p> Boolean type. Set values to either the constant GLOBUS_TRUE and GLOBUS_FALSE</p>
<h3>typedef uint32_t <code>globus_result_t</code></h3>
<p> Weak pointer to a Globus Error object, or the special value GLOBUS_SUCCESS</p>
<h3>typedef socklen_t <code>globus_socklen_t</code></h3>
<p> Size of a socket length parameter. The globus_socklen_t type is part of the POSIX socket interface and is also available in winsock2.h. In older UNIX implementations, this was variously a size_t or an int.</p>
<h2>Function Documentation</h2>
<h3><code>globus_result_t</code> globus_eval_path (const char *pathstring, char **bufp)</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>pathstring</i> A string containing any number of variable path references using the syntax ${PATH-NAME} Supported path elements are</p>
<dl>
<dt>&bull;</p>
<dd> prefix</p>
<dt>&bull;</p>
<dd> exec_prefix</p>
<dt>&bull;</p>
<dd> sbindir</p>
<dt>&bull;</p>
<dd> bindir</p>
<dt>&bull;</p>
<dd> libdir</p>
<dt>&bull;</p>
<dd> libexecdir</p>
<dt>&bull;</p>
<dd> includedir</p>
<dt>&bull;</p>
<dd> datarootdir</p>
<dt>&bull;</p>
<dd> datadir</p>
<dt>&bull;</p>
<dd> mandir</p>
<dt>&bull;</p>
<dd> sysconfdir</p>
<dt>&bull;</p>
<dd> sharedstatedir</p>
<dt>&bull;</p>
<dd> localstatedir</p>
<dt>&bull;</p>
<dd> perlmoduledir These strings are based on the parameters passed to this package configure script, but modified so that if GLOBUS_LOCATION is set in the environment, it is used instead of the configured path.</dl>
<p> <i>bufp</i> Pointer to be set to a newly allocated string that has recursively resolved all substitution paths.</dl>
<h3>int globus_tilde_expand (unsigned longoptions, <code>globus_bool_t</code>url_form, char *inpath, char **outpath)</h3>
<p> Expand ~ and/or ~user in path strings. Expand the leading ~ (or ~user) characters from inpath to the home directory path of the current user (or user specified in ~user); the result is stored in a newly allocated buffer *outpath (which will need to be freed by a call to globus_free.) The string following the ~/or ~user/ is copied verbatim to the output string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>options</i> The expansion is conditioned by the options as defined in <code>globus_tilde_expand.h</code>:</p>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_TILDE_EXPAND: expand ~</p>
<dt>&bull;</p>
<dd> GLOBUS_TILDE_USER_EXPAND: expand ~user Otherwise, the corresponding form is not expanded (just copied int the output path)</dl>
<p> <i>url_form</i> True if the inpath follows an URL format (/~) Used when expanding an url (for : &lt;scheme&gt;://host[:port][/path] were /path can be of the form /~[user][/&#8230;]. Otherwise, the form ~[user][/&#8230;] is expected.<br />
 <i>inpath</i> Input string to expand.<br />
 <i>outpath</i> Output string; Need to be freed when not used anymore.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAP">Function Documentation</a></p>
<dd>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
