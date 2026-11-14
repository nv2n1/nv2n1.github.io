---
title: "cmpistatus(3)"
name: "cmpistatus"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpistatus/"
description: "CMPIStatus – CMPIStatus class implementation"
---

<p>CMPIStatus &#8211; CMPIStatus class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p><code>CMPIrc</code> <code>rc;</code><br />
 <i>status code for operation. </i> </p>
<p> <code>CMPIString</code> * <code>msg;</code><br />
 <i>String description for status code, when errors occur. </i></p>
<h2>Methods</h2>
<h2>Description</h2>
<p>Native CMPIStatus implementation. </p>
<p> This is the native CMPIStatus implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIStatus object, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
