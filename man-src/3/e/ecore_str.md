---
title: "ecore_str(3)"
name: "ecore_str"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_str/"
description: "Ecore_Str.h – Contains useful C string functions."
---

<p>Ecore_Str.h &#8211; Contains useful C string functions. </p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p>EAPI size_t <code>ecore_strlcpy</code> (char *dst, const char *src, size_t siz)<br />
 <i>copy a c-string </i><br />
 EAPI size_t <code>ecore_strlcat</code> (char *dst, const char *src, size_t siz)<br />
 <i>append a c-string </i><br />
 EAPI int <code>ecore_str_has_prefix</code> (const char *str, const char *prefix)<br />
 <i>checks if the string has the given prefix </i><br />
 EAPI int <code>ecore_str_has_suffix</code> (const char *str, const char *suffix)<br />
 <i>checks if the string has the given suffix </i><br />
 EAPI int <code>ecore_str_has_extension</code> (const char *str, const char *ext)<br />
 <i>This function does the same like </i><code>ecore_str_has_suffix()</code>, but with a case insensitive compare.<br />
 EAPI char ** <code>ecore_str_split</code> (const char *string, const char *delimiter, int max_tokens)<br />
 <i>Splits a string into a maximum of max_tokens pieces, using the given delimiter. </i></p>
<h2>Detailed Description</h2>
<p>Contains useful C string functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_str_has_extension (const char * str, const char * ext)</h3>
<p>This function does the same like <code>ecore_str_has_suffix()</code>, but with a case insensitive compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> the string to work with<br />
 <i>ext</i> the extension to check for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if str has the given extension checks if the string has the given extension</dl>
<h3>EAPI int ecore_str_has_prefix (const char * str, const char * prefix)</h3>
<p>checks if the string has the given prefix </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> the string to work with<br />
 <i>prefix</i> the prefix to check for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if str has the given prefix</dl>
<h3>EAPI int ecore_str_has_suffix (const char * str, const char * suffix)</h3>
<p>checks if the string has the given suffix </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> the string to work with<br />
 <i>suffix</i> the suffix to check for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if str has the given suffix</dl>
<h3>EAPI char** ecore_str_split (const char * str, const char * delim, int max_tokens)</h3>
<p>Splits a string into a maximum of max_tokens pieces, using the given delimiter. </p>
<p> If max_tokens is reached, the final string in the returned string array contains the remainder of string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> A string to split.<br />
 <i>delim</i> A string which specifies the places at which to split the string. The delimiter is not included in any of the resulting strings, unless max_tokens is reached.<br />
 <i>max_tokens</i> The maximum number of strings to split string into. If this is less than 1, the string is split completely.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly-allocated NULL-terminated array of strings. To free it: free the first element of the array and the array itself.</dl>
<h3>EAPI size_t ecore_strlcat (char * dst, const char * src, size_t siz)</h3>
<p>append a c-string </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dst</i> the destination<br />
 <i>src</i> the source<br />
 <i>siz</i> the size of the destination</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the length of the source string plus MIN(siz, strlen(initial dst)) Appends src to string dst of size siz (unlike strncat, siz is the full size of dst, not space left). At most siz-1 characters will be copied. Always NUL terminates (unless siz &lt;= strlen(dst)). Returns strlen(src) + MIN(siz, strlen(initial dst)). If retval &gt;= siz, truncation occurred.</dl>
<h3>EAPI size_t ecore_strlcpy (char * dst, const char * src, size_t siz)</h3>
<p>copy a c-string </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dst</i> the destination<br />
 <i>src</i> the source<br />
 <i>siz</i> the size of the destination</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the length of the source string Copy src to string dst of size siz. At most siz-1 characters will be copied. Always NUL terminates (unless siz == 0). Returns strlen(src); if retval &gt;= siz, truncation occurred.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
