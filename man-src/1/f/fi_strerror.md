---
title: "fi_strerror(1)"
name: "fi_strerror"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fi_strerror/"
---

<h2 class="name">NAME</h2>
 

 

 fi_strerror - display libfabric error strings 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre>
fi_strerror FI_ERROR_CODE
</pre></dl>

<h2>DESCRIPTION</h2>

 

 Display the error string for the given numeric FI_ERROR_CODE. FI_ERROR_CODE may be a hexadecimal, octal, or decimal constant. Although the <a HREF="/docs/linux/man/3-fi_strerror/">fi_strerror</a>(3) library function only accepts positive error values, for convenience this utility accepts both positive and negative error values. 

 This is primarily a convenience tool for developers.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/7-fabric/">fabric</a>(7) <a HREF="/docs/linux/man/3-fi_errno/">fi_errno</a>(3)

<h2>AUTHORS</h2>

 OpenFabrics. 

<h2>Index</h2>


