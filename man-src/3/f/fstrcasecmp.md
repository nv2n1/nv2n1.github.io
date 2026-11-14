---
title: "fstrcasecmp(3)"
name: "fstrcasecmp"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fstrcasecmp/"
---

<h2>NAME</h2>

 fstrcasecmp - fuzzy comparison of two strings ignoring case

<h2>SYNOPSIS</h2>

 #include &lt;fstrcmp.h&gt; 

 #define FSTRCMP_IDENTICAL 
 #define FSTRCMP_THRESHOLD 
 #define FSTRCMP_ERROR 

 double fstrcasecmp(const char *string1, const char *string2);

<h2>DESCRIPTION</h2>

 The fstrcmp() function compares the two strings, string1 and string2, ignoring case.

<h2>RETURN VALUE</h2>

 The fstrcasecmp function returns a floating point value between 0.0 and FSTRCMP_IDENTICAL. A value of 0.0 means the strings are utterly un-alike. A value of FSTRCMP_IDENTICAL means the strings are identical. A value of more than FSTRCMP_THRESHOLD (it lies between 0.0 and FSTRCMP_IDENTICAL) would be considered &quot;similar&quot; by most people. 

 A value of FSTRCMP_ERROR (always negative) indicates a <a HREF="/docs/linux/man/3-malloc/">malloc</a>(3) failure.

<h2>SEE ALSO</h2>

<dl>
<dt><a HREF="/docs/linux/man/3-fmemcmp/">fmemcmp</a>(3)
<dd> fuzzy comparison of two memory areas
<dt><a HREF="/docs/linux/man/3-fstrcasecmpi/">fstrcasecmpi</a>(3)
<dd> fuzzy comparison of two strings ignoring case
<dt><a HREF="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3)
<dd> fuzzy comparison of two strings
<dt><a HREF="/docs/linux/man/3-strcasecmp/">strcasecmp</a>(3)
<dd> compare two strings ignoring case</dl>

<h2>COPYRIGHT</h2>

 fstrcmp version 0.7 
 Copyright (C) 2009 Peter Miller 
 Peter Miller &lt;pmiller [at] opensource.org.au&gt; 

 The comparison code is derived from the fuzzy comparison functions in GNU Gettext 0.17. The GNU Gettext comparison functions were, in turn, derived from GNU Diff 2.7. 

 Copyright (C) 1988-2009 Free Software Foundation 

<h2>Index</h2>


