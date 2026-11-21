---
title: "hx509_xfree(3)"
name: "hx509_xfree"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_xfree/"
description: "hx509 misc functions –"
---

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
</dt><dd> <i>list</i> list to be freed.</dd></dl>
<h3>void hx509_xfree (void *ptr)</h3>
<p> Free a data element allocated in the library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>ptr</i> data to be freed.</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
