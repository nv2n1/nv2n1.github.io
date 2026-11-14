---
title: "fwcscmpi(3)"
name: "fwcscmpi"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fwcscmpi/"
---

<h2>NAME</h2>

 fwcscmpi - fuzzy comparison of two wide-character strings

<h2>SYNOPSIS</h2>

 #include &lt;fstrcmp.h&gt; 

 #define FSTRCMPI_IDENTICAL 
 #define FSTRCMPI_THRESHOLD 
 #define FSTRCMPI_ERROR 

 int fwcscmpi(const wchar_t *string1, const wchar_t *string2);

<h2>DESCRIPTION</h2>

 The fwcscmpi() function compares the two wide-character strings, string1 and string2.

<h2>RETURN VALUE</h2>

 The fwcscmpi function returns an int value between 0 and FSTRCMPI_IDENTICAL. A value of 0 means the two wide-character strings are utterly un-alike. A value of FSTRCMPI_IDENTICAL means the two wide-character strings are identical. A value of more than FSTRCMPI_THRESHOLD (it lies between 0 and FSTRCMPI_IDENTICAL) would be considered &quot;similar&quot; by most people. 

 A value of FSTRCMPI_ERROR (always negative) indicates a <a HREF="/docs/linux/man/3-malloc/">malloc</a>(3) failure.

<h2>SEE ALSO</h2>

<dl>
<dt><a HREF="/docs/linux/man/3-fstrcmp/">fstrcmp</a>(3)
<dd> fuzzy comparison of two strings
<dt><a HREF="/docs/linux/man/3-fwcscmp/">fwcscmp</a>(3)
<dd> fuzzy comparison of two wide-character strings
<dt><a HREF="/docs/linux/man/3-wcscmp/">wcscmp</a>(3)
<dd> compare two wide-character strings</dl>

<h2>COPYRIGHT</h2>

 fstrcmp version 0.7 
 Copyright (C) 2009 Peter Miller 
 Peter Miller &lt;pmiller [at] opensource.org.au&gt; 

 The comparison code is derived from the fuzzy comparison functions in GNU Gettext 0.17. The GNU Gettext comparison functions were, in turn, derived from GNU Diff 2.7. 

 Copyright (C) 1988-2009 Free Software Foundation 

<h2>Index</h2>


