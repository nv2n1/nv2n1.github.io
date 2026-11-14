---
title: "ecore_string_group(3)"
name: "ecore_string_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_string_group/"
description: "String Instance Functions – These functions allow you to store one copy of a string, and use it throughout your program."
---

<p>String Instance Functions &#8211; These functions allow you to store one copy of a string, and use it throughout your program. </p>
<h3>Functions</h3>
<p>EAPI const char * <code>ecore_string_instance</code> (const char *string)<br />
 <i>Retrieves an instance of a string for use in an ecore program. </i><br />
 EAPI void <code>ecore_string_release</code> (const char *string)<br />
 <i>Notes that the given string has lost an instance. </i></p>
<h2>Detailed Description</h2>
<p>These functions allow you to store one copy of a string, and use it throughout your program. </p>
<p> This is a method to reduce the number of duplicated strings kept in memory. It&#8217;s pretty common for the same strings to be dynamically allocated repeatedly between applications and libraries, especially in circumstances where you could have multiple copies of a structure that allocates the string. So rather than duplicating and freeing these strings, you request a read-only pointer to an existing string and only incur the overhead of a hash lookup. </p>
<p> It sounds like micro-optimizing, but profiling has shown this can have a significant impact as you scale the number of copies up. It improves string creation/destruction speed, reduces memory use and decreases memory fragmentation, so a win all-around.</p>
<h2>Function Documentation</h2>
<h3>EAPI const char* ecore_string_instance (const char * string)</h3>
<p>Retrieves an instance of a string for use in an ecore program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>string</i> The string to retrieve an instance of.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an instance of the string on success. NULL on failure.</dl>
<p> References ecore_hash_get(), and ecore_hash_set().</p>
<h3>EAPI void ecore_string_release (const char * string)</h3>
<p>Notes that the given string has lost an instance. </p>
<p> It will free the string if no other instances are left. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>string</i> The given string.</dl>
<p> References ecore_hash_get(), and ecore_hash_remove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
