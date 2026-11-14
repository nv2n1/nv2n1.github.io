---
title: "cmpivalue(3)"
name: "cmpivalue"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpivalue/"
description: "CMPIValue – CMPIValue class implementation"
---

<p>CMPIValue &#8211; CMPIValue class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p><code>CMPIUint64</code> <code>uint64</code> </p>
<p> <code>CMPIUint32</code> <code>uint32</code> </p>
<p> <code>CMPIUint16</code> <code>uint16</code> </p>
<p> <code>CMPIUint8</code> <code>uint8</code> </p>
<p> <code>CMPISint64</code> <code>sint64</code> </p>
<p> <code>CMPISint32</code> <code>sint32</code> </p>
<p> <code>CMPISint16</code> <code>sint16</code> </p>
<p> <code>CMPISint8</code> <code>sint8</code> </p>
<p> <code>CMPIReal64</code> <code>real64</code> </p>
<p> <code>CMPIReal32</code> <code>real32</code> </p>
<p> <code>CMPIBoolean</code> <code>boolean</code> </p>
<p> <code>CMPIChar16</code> <code>char16</code> </p>
<p> <code>CMPIInstance</code> * <code>inst</code> </p>
<p> <code>CMPIObjectPath</code> * <code>ref</code> </p>
<p> <code>CMPIArgs</code> * <code>args</code> </p>
<p> <code>CMPIEnumeration</code> * <code>Enum</code> </p>
<p> <code>CMPIArray</code> * <code>array</code> </p>
<p> <code>CMPIString</code> * <code>string</code> </p>
<p> char * <code>chars</code> </p>
<p> <code>CMPIDateTime</code> * <code>dateTime</code> </p>
<p> <code>CMPIValuePtr</code> <code>dataPtr</code> </p>
<p> <code>CMPISint8</code> <code>Byte</code> </p>
<p> <code>CMPISint16</code> <code>Short</code> </p>
<p> <code>CMPISint32</code> <code>Int</code> </p>
<p> <code>CMPISint64</code> <code>Long</code> </p>
<p> <code>CMPIReal32</code> <code>Float</code> </p>
<p> <code>CMPIReal64</code> <code>Double</code> </p>
<h2>Methods</h2>
<p>void <code>native_release_CMPIValue</code> (<code>CMPIType</code> type, <code>CMPIValue</code> *val) </p>
<p> <code>CMPIValue</code> <code>native_clone_CMPIValue</code> (<code>CMPIType</code> type, <code>CMPIValue</code> *val, <code>CMPIStatus</code> *rc) </p>
<p> char * <code>pathToChars</code> (<code>CMPIObjectPath</code> *cop, <code>CMPIStatus</code> *rc, char *str, int uri) </p>
<p> char * <code>value2CharsUri</code> (<code>CMPIType</code> type, <code>CMPIValue</code> *value, int uri) </p>
<p> char * <code>value2Chars</code> (<code>CMPIType</code> type, <code>CMPIValue</code> *value) </p>
<p> char * <code>keytype2Chars</code> (<code>CMPIType</code> type) </p>
<p> <code>CMPIValue</code> * <code>getKeyValueTypePtr</code> (char *type, char *value, <code>XtokValueReference</code> *ref, <code>CMPIValue</code> *val, <code>CMPIType</code> *typ) </p>
<p> <code>CMPIType</code> <code>guessType</code> (char *val) </p>
<p> <code>CMPIValue</code> <code>str2CMPIValue</code> (<code>CMPIType</code> type, char *val, <code>XtokValueReference</code> *ref) </p>
<h2>Description</h2>
<p>CMPIValue class implementation, representing the Encapsulated value objects. </p>
<p> This is the native CMPIValue implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIValue, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
