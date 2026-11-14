---
title: "hx509_name_free(3)"
name: "hx509_name_free"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_name_free/"
description: "hx509 name functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 name functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_general_name_unparse</code> (GeneralName *, char **) </p>
<p> int <code>hx509_name_binary</code> (const hx509_name, heim_octet_string *) </p>
<p> int <code>hx509_name_cmp</code> (hx509_name, hx509_name) </p>
<p> int <code>hx509_name_copy</code> (hx509_context, const hx509_name, hx509_name *) </p>
<p> int <code>hx509_name_expand</code> (hx509_context, hx509_name, hx509_env) </p>
<p> void <code>hx509_name_free</code> (hx509_name *) </p>
<p> int <code>hx509_name_is_null_p</code> (const hx509_name) </p>
<p> int <code>hx509_name_to_Name</code> (const hx509_name, Name *) </p>
<p> int <code>hx509_name_to_string</code> (const hx509_name, char **) </p>
<p> int <code>hx509_parse_name</code> (hx509_context, const char *, hx509_name *) </p>
<p> int <code>hx509_unparse_der_name</code> (const void *, size_t, char **) </p>
<h2>Detailed Description</h2>
<p> See the <code>PKIX/X.509 Names</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_general_name_unparse (GeneralName *name, char **str)</h3>
<p> Unparse the hx509 name in name into a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> the name to print<br />
 <i>str</i> an allocated string returns the name in string form</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_name_binary (const hx509_namename, heim_octet_string *os)</h3>
<p> Convert a hx509_name object to DER encoded name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> name to concert<br />
 <i>os</i> data to a DER encoded name, free the resulting octet string with hx509_xfree(os-&gt;data).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_name_cmp (hx509_namen1, hx509_namen2)</h3>
<p> Compare to hx509 name object, useful for sorting. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>n1</i> a hx509 name object.<br />
 <i>n2</i> a hx509 name object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 the objects are the same, returns &gt; 0 is n2 is &#8216;larger&#8217; then n2, &lt; 0 if n1 is &#8216;smaller&#8217; then n2.</dl>
<h3>int hx509_name_copy (hx509_contextcontext, const hx509_namefrom, hx509_name *to)</h3>
<p> Copy a hx509 name object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 cotext.<br />
 <i>from</i> the name to copy from<br />
 <i>to</i> the name to copy to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_name_expand (hx509_contextcontext, hx509_namename, hx509_envenv)</h3>
<p> Expands variables in the name using env. Variables are on the form ${name}. Useful when dealing with certificate templates. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 cotext.<br />
 <i>name</i> the name to expand.<br />
 <i>env</i> environment variable to expand.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<p> Only UTF8String rdnSequence names are allowed</p>
<h3>void hx509_name_free (hx509_name *name)</h3>
<p> Free a hx509 name object, upond return *name will be NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> a hx509 name object to be freed.</dl>
<h3>int hx509_name_is_null_p (const hx509_namename)</h3>
<p> Unparse the hx509 name in name into a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> the name to check if its empty/null.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> non zero if the name is empty/null.</dl>
<h3>int hx509_name_to_Name (const hx509_namefrom, Name *to)</h3>
<p> Convert a hx509_name into a Name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>from</i> the name to copy from<br />
 <i>to</i> the name to copy to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_name_to_string (const hx509_namename, char **str)</h3>
<p> Convert the hx509 name object into a printable string. The resulting string should be freed with free(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> name to print<br />
 <i>str</i> the string to return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_parse_name (hx509_contextcontext, const char *str, hx509_name *name)</h3>
<p> Parse a string into a hx509 name object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>str</i> a string to parse.<br />
 <i>name</i> the resulting object, NULL in case of error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_unparse_der_name (const void *data, size_tlength, char **str)</h3>
<p> Convert a DER encoded name info a string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> data to a DER/BER encoded name<br />
 <i>length</i> length of data<br />
 <i>str</i> the resulting string, is NULL on failure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
