---
title: "cmpiobjectpath(3)"
name: "cmpiobjectpath"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpiobjectpath/"
description: "CMPIObjectPath – CMPIObjectPath class implementation"
---

<p>CMPIObjectPath &#8211; CMPIObjectPath class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p>int <code>void * hdl</code><br />
 Opaque pointer to class instance data.<br />
 <code>CMPIObjectPathFT</code> * <code>ft</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Methods</h2>
<p><code>CMPIStatus</code>(* <code>release</code> )(<code>CMPIObjectPath</code> *op)<br />
 <i>The ObjectPath object will not be used any further and may be freed by CMPI run time system. </i><br />
 <code>CMPIObjectPath</code> *(* <code>clone</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Create an independent copy of this ObjectPath object. </i><br />
 <code>CMPIStatus</code>(* <code>setNameSpace</code> )(<code>CMPIObjectPath</code> *op, const char *ns)<br />
 <i>Set/replace the namespace component. </i><br />
 <code>CMPIString</code> *(* <code>getNameSpace</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Get the namespace component. </i><br />
 <code>CMPIStatus</code>(* <code>setHostname</code> )(<code>CMPIObjectPath</code> *op, const char *hn)<br />
 <i>Set/replace the hostname component. </i><br />
 <code>CMPIString</code> *(* <code>getHostname</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Get the hostname component. </i><br />
 <code>CMPIStatus</code>(* <code>setClassName</code> )(<code>CMPIObjectPath</code> *op, const char *cn)<br />
 <i>Set/replace the classname component. </i><br />
 <code>CMPIString</code> *(* <code>getClassName</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Get the classname component. </i><br />
 <code>CMPIStatus</code>(* <code>addKey</code> )(<code>CMPIObjectPath</code> *op, const char *name, <code>CMPIValue</code> *value, <code>CMPIType</code> type)<br />
 <i>Adds/replaces a named key property. </i><br />
 <code>CMPIData</code>(* <code>getKey</code> )(<code>CMPIObjectPath</code> *op, const char *name, <code>CMPIStatus</code> *rc)<br />
 <i>Gets a named key property value. </i><br />
 <code>CMPIData</code>(* <code>getKeyAt</code> )(<code>CMPIObjectPath</code> *op, unsigned int index, <code>CMPIString</code> **name, <code>CMPIStatus</code> *rc)<br />
 <i>Gets a key property value defined by its index. </i><br />
 unsigned int(* <code>getKeyCount</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Gets the number of key properties contained in this ObjectPath. </i><br />
 <code>CMPIStatus</code>(* <code>setNameSpaceFromObjectPath</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIObjectPath</code> *src)<br />
 <i>Set/replace namespace and classname components from &lt;src&gt;. </i><br />
 <code>CMPIStatus</code>(* <code>setHostAndNameSpaceFromObjectPath</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIObjectPath</code> *src)<br />
 <i>Set/replace hostname, namespace and classname components from &lt;src&gt;. </i><br />
 <code>CMPIData</code>(* <code>getClassQualifier</code> )(<code>CMPIObjectPath</code> *op, const char *qName, <code>CMPIStatus</code> *rc)<br />
 <i>Get class qualifier value. </i><br />
 <code>CMPIData</code>(* <code>getPropertyQualifier</code> )(<code>CMPIObjectPath</code> *op, const char *pName, const char *qName, <code>CMPIStatus</code> *rc)<br />
 <i>Get property qualifier value. </i><br />
 <code>CMPIData</code>(* <code>getMethodQualifier</code> )(<code>CMPIObjectPath</code> *op, const char *methodName, const char *qName, <code>CMPIStatus</code> *rc)<br />
 <i>Get method qualifier value. </i><br />
 <code>CMPIData</code>(* <code>getParameterQualifier</code> )(<code>CMPIObjectPath</code> *op, const char *mName, const char *pName, const char *qName, <code>CMPIStatus</code> *rc)<br />
 <i>Get method parameter quailifier value. </i><br />
 <code>CMPIString</code> *(* <code>toString</code> )(<code>CMPIObjectPath</code> *op, <code>CMPIStatus</code> *rc)<br />
 <i>Generates a well formed string representation of this ObjectPath. </i></p>
<h2>Description</h2>
<p>Native CMPIObjectPath implementation. </p>
<p> This is the native CMPIObjectPath implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIObjectPath, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>Examples</h2>
<p><code>CMPIString * namespace = objpath-&gt;ft-&gt;getNameSpace(objectpath, NULL);</code><br />
 <code>CMPIString * classname = objpath-&gt;ft-&gt;getClassName(objectpath, NULL);</code><br />
 <code>int numkeys = objectpath-&gt;ft-&gt;getKeyCount(objectpath, NULL);</code> </p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
