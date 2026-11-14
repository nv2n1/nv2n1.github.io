---
title: "kstrtol(9)"
name: "kstrtol"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kstrtol/"
---

kstrtol - convert a string to a long

<h2>Synopsis</h2>

<pre><code>int kstrtol(const char *s, unsigned int base, long *res);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>The start of the string. The string must be null-terminated, and may also include a single newline before its terminating null. The first character may also be a plus sign or a minus sign.</dl>
 

 <i>base</i>
<dl><dd>The number base to use. The maximum supported base is 16. If base is given as 0, then the base of the string is automatically detected with the conventional semantics - If it begins with 0x the number will be parsed as a hexadecimal (case insensitive), if it otherwise begins with 0, it will be parsed as an octal number. Otherwise it will be parsed as a decimal.</dl>
 

 <i>res</i>
<dl><dd>Where to write the result of the conversion on success.</dl>

<h2>Description</h2>

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error. Used as a replacement for the obsolete simple_strtoull. Return code must be checked.

<h2>Copyright</h2>


