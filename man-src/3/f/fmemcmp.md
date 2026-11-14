---
title: "fmemcmp(3)"
name: "fmemcmp"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmemcmp/"
---

<h2>NAME</h2>

 fmemcmp - fuzzy comparison of two memory areas

<h2>SYNOPSIS</h2>

 #include &lt;fstrcmp.h&gt; 

 #define FSTRCMP_IDENTICAL 
 #define FSTRCMP_THRESHOLD 
 #define FSTRCMP_ERROR 

 double fmemcmp(const void *data1, size_t size1, const void *data2, size_t size2);

<h2>DESCRIPTION</h2>

 The fmemcmp() function compares the two memory areas, the size1 bytes pointed to by data1 and the size2 bytes pointed to by data2.

<h2>RETURN VALUE</h2>

 The fmemcmp function returns a floating point value between 0.0 and FSTRCMP_IDENTICAL. A value of 0.0 means the memory areas are utterly un-alike. A value of FSTRCMP_IDENTICAL means the memory areas are identical. A value of more than FSTRCMP_THRESHOLD (it lies between 0.0 and FSTRCMP_IDENTICAL) would be considered &quot;similar&quot; by most people. 

 A value of FSTRCMP_ERROR (always negative) indicates a <a HREF="/docs/linux/man/3-malloc/">malloc</a>(3) failure.

<h2>SEE ALSO</h2>

<dl>
<dt><a HREF="/docs/linux/man/3-fmemcmpi/">fmemcmpi</a>(3)
<dd> fuzzy comparison of two memory areas
<dt><a HREF="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3)
<dd> fuzzy comparison of two strings
<dt><a HREF="/docs/linux/man/3-memcmp/">memcmp</a>(3)
<dd> compare memory areas</dl>

<h2>COPYRIGHT</h2>

 fstrcmp version 0.7 
 Copyright (C) 2009 Peter Miller 
 Peter Miller &lt;pmiller [at] opensource.org.au&gt; 

 The comparison code is derived from the fuzzy comparison functions in GNU Gettext 0.17. The GNU Gettext comparison functions were, in turn, derived from GNU Diff 2.7. 

 Copyright (C) 1988-2009 Free Software Foundation 

<h2>Index</h2>


