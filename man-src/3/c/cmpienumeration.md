---
title: "cmpienumeration(3)"
name: "cmpienumeration"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpienumeration/"
description: "CMPIEnumeration – CMPIEnumeration class implementation"
---

<p>CMPIEnumeration &#8211; CMPIEnumeration class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p>int <code>void * hdl</code><br />
 Opaque pointer to class instance data.<br />
 <code>CMPIEnumerationFT</code> * <code>ft</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Methods</h2>
<p><code>CMPIStatus</code>(* <code>release</code> )(<code>CMPIEnumeration</code> *en)<br />
 <i>The Enumeration object will not be used any further and may be freed by CMPI run time system. </i><br />
 <code>CMPIEnumeration</code> *(* <code>clone</code> )(<code>CMPIEnumeration</code> *en, <code>CMPIStatus</code> *rc)<br />
 <i>Create an independent copy of this Enumeration object. </i><br />
 <code>CMPIData</code>(* <code>getNext</code> )(<code>CMPIEnumeration</code> *en, <code>CMPIStatus</code> *rc)<br />
 <i>Get the next element of this Enumeration. </i><br />
 <code>CMPIBoolean</code>(* <code>hasNext</code> )(<code>CMPIEnumeration</code> *en, <code>CMPIStatus</code> *rc)<br />
 <i>Test for any elements left in this Enumeration. </i><br />
 <code>CMPIArray</code> *(* <code>toArray</code> )(<code>CMPIEnumeration</code> *en, <code>CMPIStatus</code> *rc)<br />
 <i>Convert this Enumeration into an Array. </i></p>
<h2>Description</h2>
<p>Native CMPIEnumeration implementation. </p>
<p> This is the native CMPIEnumeration implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIEnumeration, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
