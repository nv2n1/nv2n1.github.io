---
title: "cmpiargs(3)"
name: "cmpiargs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpiargs/"
description: "CMPIArgs – CMPIArgs class implementation"
---

<p>CMPIArgs &#8211; CMPIArgs class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p>int <code>void * hdl</code><br />
 Opaque pointer to class instance data.<br />
 <code>CMPIArgsFT</code> * <code>ft</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Methods</h2>
<p><code>CMPIStatus</code> <code>release</code> (<code>CMPIArgs</code> *args) </p>
<p> <code>CMPIArgs</code> * <code>clone</code> (<code>CMPIArgs</code> *args, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIStatus</code> <code>addArg</code> (<code>CMPIArgs</code> *args, char *name, <code>CMPIValue</code> *value, <code>CMPIType</code> type) </p>
<p> <code>CMPIData</code> <code>getArg</code> (<code>CMPIArgs</code> *args, char *name, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIData</code> <code>getArgAt</code> (<code>CMPIArgs</code> *args, unsigned int index, <code>CMPIString</code> **name, <code>CMPIStatus</code> *rc) </p>
<p> unsigned int <code>getArgCount</code> (<code>CMPIArgs</code> *args, <code>CMPIStatus</code> *rc) </p>
<h2>Description</h2>
<p>Native CMPIArgs implementation. </p>
<p> This is the native CMPIArgs implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIArgs object, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
