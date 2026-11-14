---
title: "tcl_concat(3)"
name: "tcl_concat"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_concat/"
description: "Tcl_Concat – concatenate a collection of strings"
---

<p>Tcl_Concat &#8211; concatenate a collection of strings </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
const char *
<code>Tcl_Concat</code>(<i>argc, argv</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>argc</i> (in) Number of strings.</p>
<dd>const char *const <i>argv[]</i> (in) Array of strings to concatenate. Must have <i>argc</i> entries. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_Concat</code> is a utility procedure used by several of the Tcl commands. Given a collection of strings, it concatenates them together into a single string, with the original strings separated by spaces. This procedure behaves differently than <code>Tcl_Merge</code>, in that the arguments are simply concatenated: no effort is made to ensure proper list structure. However, in most common usage the arguments will all be proper lists themselves; if this is true, then the result will also have proper list structure. </p>
<p> <code>Tcl_Concat</code> eliminates leading and trailing white space as it copies strings from <code>argv</code> to the result. If an element of <code>argv</code> consists of nothing but white space, then that string is ignored entirely. This white-space removal was added to make the output of the <code>concat</code> command cleaner-looking. </p>
<p> The result string is dynamically allocated using <code>Tcl_Alloc</code>; the caller must eventually release the space by calling <code>Tcl_Free</code>.</p>
<h2>See Also</h2>
<p>Tcl_ConcatObj</p>
<h2>Keywords</h2>
<p>concatenate, strings</p>
