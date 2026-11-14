---
title: "fstrcolli(3)"
name: "fstrcolli"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fstrcolli/"
---

<h2>NAME</h2>

 fstrcolli - fuzzy comparison of two strings using the current locale

<h2>SYNOPSIS</h2>

 #include &lt;fstrcmp.h&gt; 

 #define FSTRCMP_IDENTICAL 
 #define FSTRCMP_THRESHOLD 
 #define FSTRCMP_ERROR 

 int fstrcolli(const char *string1, const char *string2);

<h2>DESCRIPTION</h2>

 The strcolli() function compares the two strings sting1 and string2. The comparison is based on strings interpreted as appropriate for the program's current locale for category LC_CTYPE.

<h2>RETURN VALUE</h2>

 The fstrcolli function returns an int value between 0 and FSTRCMPI_IDENTICAL. A value of 0 means the strings are utterly un-alike. A value of FSTRCMPI_IDENTICAL means the strings are identical. A value of more than FSTRCMPI_THRESHOLD (it lies between 0 and FSTRCMPI_IDENTICAL) would be considered &quot;similar&quot; by most people. 

 A value of FSTRCMPI_ERROR (always negative) indicates a <a HREF="/docs/linux/man/3-malloc/">malloc</a>(3) or <a HREF="/docs/linux/man/3-mbstowcs/">mbstowcs</a>(3) failure.

<h2>SEE ALSO</h2>

<dl>
<dt><a HREF="/docs/linux/man/3-fstrcmpi/">fstrcmpi</a>(3)
<dd> fuzzy comparison of two strings
<dt><a HREF="/docs/linux/man/3-fstrcoll/">fstrcoll</a>(3)
<dd> fuzzy comparison of two strings using the current locale
<dt><a HREF="/docs/linux/man/3-strcoll/">strcoll</a>(3)
<dd> compare two strings using the current locale
<dt><a HREF="/docs/linux/man/3-mbstowcs/">mbstowcs</a>(3)
<dd> convert a multibyte string to a wide-character string</dl>

<h2>COPYRIGHT</h2>

 fstrcmp version 0.7 
 Copyright (C) 2009 Peter Miller 
 Peter Miller &lt;pmiller [at] opensource.org.au&gt; 

 The comparison code is derived from the fuzzy comparison functions in GNU Gettext 0.17. The GNU Gettext comparison functions were, in turn, derived from GNU Diff 2.7. 

 Copyright (C) 1988-2009 Free Software Foundation 

<h2>Index</h2>


