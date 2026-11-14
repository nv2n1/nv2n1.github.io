---
title: "hx509_misc(3)"
name: "hx509_misc"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_misc/"
description: "hx509 misc functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 misc functions &#8211; </p>
<h3>Functions</h3>
<p> void <code>hx509_free_octet_string_list</code> (hx509_octet_string_list *list) </p>
<p> void <code>hx509_xfree</code> (void *ptr) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void hx509_free_octet_string_list (hx509_octet_string_list *list)</h3>
<p> Free a list of octet strings returned by another hx509 library function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>list</i> list to be freed.</dl>
<h3>void hx509_xfree (void *ptr)</h3>
<p> Free a data element allocated in the library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ptr</i> data to be freed.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
