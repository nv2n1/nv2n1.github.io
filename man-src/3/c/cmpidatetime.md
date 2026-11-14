---
title: "cmpidatetime(3)"
name: "cmpidatetime"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpidatetime/"
description: "CMPIDateTime – CMPIDateTime class implementation"
---

<p>CMPIDateTime &#8211; CMPIDateTime class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<h2>Methods</h2>
<p>int <code>void * hdl;</code><br />
 <i>Opaque pointer to class instance data. </i><br />
 <code>CMPIDateTimeFT</code> * <code>ft;</code><br />
 <i>Pointer to the Function Table. </i></p>
<h2>Methods</h2>
<p>void (<code>CMPIType</code> type, <code>CMPIDateTime</code> *val) </p>
<p> <code>CMPIDateTime</code> <code>native_clone_CMPIDateTime</code> (<code>CMPIType</code> type, <code>CMPIDateTime</code> *val, <code>CMPIStatus</code> *rc) </p>
<p> char * <code>pathToChars</code> (<code>CMPIObjectPath</code> *cop, <code>CMPIStatus</code> *rc, char *str, int uri) </p>
<p> char * <code>value2CharsUri</code> (<code>CMPIType</code> type, <code>CMPIDateTime</code> *value, int uri) </p>
<p> char * <code>value2Chars</code> (<code>CMPIType</code> type, <code>CMPIDateTime</code> *value) </p>
<p> char * <code>keytype2Chars</code> (<code>CMPIType</code> type) </p>
<p> <code>CMPIDateTime</code> * <code>getKeyValueTypePtr</code> (char *type, char *value, <code>XtokValueReference</code> *ref, <code>CMPIDateTime</code> *val, <code>CMPIType</code> *typ) </p>
<p> <code>CMPIType</code> <code>guessType</code> (char *val) </p>
<p> <code>CMPIDateTime</code> <code>str2CMPIDateTime</code> (<code>CMPIType</code> type, char *val, <code>XtokValueReference</code> *ref) </p>
<h2>Description</h2>
<p>CMPIDateTime class implementation, representing the Encapsulated value objects. </p>
<p> This is the native CMPIDateTime implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIDateTime, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
