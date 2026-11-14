---
title: "cmpiinstance(3)"
name: "cmpiinstance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmpiinstance/"
description: "CMPIInstance – CMPIInstance class implementation"
---

<p>CMPIInstance &#8211; CMPIInstance class implementation</p>
<h2>Synopsis</h2>
<h3>Public Attributes</h3>
<p>int <code>void * hdl</code><br />
 Opaque pointer to class instance data.<br />
 <code>CMPIInstanceFT</code> * <code>ft</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Methods</h2>
<p><code>CMPIStatus</code>(* <code>release</code> )(<code>CMPIInstance</code> *inst)<br />
 <i>The Instance object will not be used any further and may be freed by CMPI run time system. </i><br />
 <code>CMPIInstance</code> *(* <code>clone</code> )(<code>CMPIInstance</code> *inst, <code>CMPIStatus</code> *rc)<br />
 <i>Create an independent copy of this Instance object. </i><br />
 <code>CMPIData</code>(* <code>getProperty</code> )(<code>CMPIInstance</code> *inst, const char *name, <code>CMPIStatus</code> *rc)<br />
 <i>Gets a named property value. </i><br />
 <code>CMPIData</code>(* <code>getPropertyAt</code> )(<code>CMPIInstance</code> *inst, unsigned int index, <code>CMPIString</code> **name, <code>CMPIStatus</code> *rc)<br />
 <i>Gets a Property value defined by its index. </i><br />
 unsigned int(* <code>getPropertyCount</code> )(<code>CMPIInstance</code> *inst, <code>CMPIStatus</code> *rc)<br />
 <i>Gets the number of properties contained in this Instance. </i><br />
 <code>CMPIStatus</code>(* <code>setProperty</code> )(<code>CMPIInstance</code> *inst, const char *name, <code>CMPIValue</code> *value, <code>CMPIType</code> type)<br />
 <i>Adds/replaces a named Property. </i><br />
 <code>CMPIObjectPath</code> *(* <code>getObjectPath</code> )(<code>CMPIInstance</code> *inst, <code>CMPIStatus</code> *rc)<br />
 <i>Generates an ObjectPath out of the namespace, classname and key propeties of this Instance. </i><br />
 <code>CMPIStatus</code>(* <code>setPropertyFilter</code> )(<code>CMPIInstance</code> *inst, char **propertyList, char **keys)<br />
 <i>Directs CMPI to ignore any setProperty operations for this instance for any properties not in this list. </i></p>
<h2>Description</h2>
<p>Native CMPIInstance implementation. </p>
<p> This is the native CMPIInstance implementation as used for remote providers. It reflects the well-defined interface of a regular CMPIInstance, however, it works independently from the management broker. </p>
<p> It is part of a native broker implementation that simulates CMPI data types rather than interacting with the entities in a full-grown CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup</p>
