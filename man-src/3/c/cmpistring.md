---
title: "cmpistring(3)"
name: "cmpistring"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpistring/"
description: "CMPIString – CMPIString class implementation"
---

<p>CMPIString &#8211; CMPIString class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p>int <code>void * hdl;</code><br />
 <i>Opaque pointer to class instance data. </i><br />
 <code>CMPIStringFT</code> * <code>ft;</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Methods</h2>
<p><code>CMPIStatus</code> <code>release</code> (<code>CMPIString</code> *string) </p>
<p> <code>CMPIString</code> * <code>clone</code> (<code>CMPIString</code> *string, <code>CMPIStatus</code> *rc) </p>
<p> char * <code>getCharPtr</code> (<code>CMPIString</code> *string, <code>CMPIStatus</code> *rc) </p>
<h2>Description</h2>
<p>CMPIString class implementation, representing the Encapsulated String object. </p>
<p> This is the native CMPIString implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIString, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
