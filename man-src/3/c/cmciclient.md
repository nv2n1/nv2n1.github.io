---
title: "cmciclient(3)"
name: "cmciclient"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclient/"
description: "CMCIClient – CIMOM Client Library object"
---

<p>CMCIClient &#8211; CIMOM Client Library object</p>
<h2>Synopsis</h2>
<pre>#include &lt;cmci.h&gt;</pre>
<h3>Public Attributes</h3>
<p>void * <code>hdl</code><br />
 <i>Opaque pointer to specific implementation data. </i> </p>
<p> <code>CMCIClientFT</code> * <code>ft</code><br />
 <i>Pointer to the Args Function Table. </i></p>
<h2>Class methods</h2>
<p><code>CMPIEnumeration</code> * <code>enumInstanceNames</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIInstance</code> * <code>getInstance</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIFlags</code> flags, char **properties, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIObjectPath</code> * <code>createInstance</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIInstance</code> *inst, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIStatus</code> <code>setInstance</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIInstance</code> *inst, <code>CMPIFlags</code> flags, char **properties) </p>
<p> <code>CMPIStatus</code> <code>deleteInstance</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop) </p>
<p> <code>CMPIEnumeration</code> * <code>execQuery</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *query, const char *lang, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>enumInstances</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIFlags</code> flags, char **properties, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>associators</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *assocClass, const char *resultClass, const char *role, const char *resultRole, <code>CMPIFlags</code> flags, char **properties, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>associatorNames</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *assocClass, const char *resultClass, const char *role, const char *resultRole, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>references</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *resultClass, const char *role, <code>CMPIFlags</code> flags, char **properties, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>referenceNames</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *resultClass, const char *role, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIData</code> <code>invokeMethod</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *method, <code>CMPIArgs</code> *in, <code>CMPIArgs</code> *out, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIStatus</code> <code>setProperty</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *name, <code>CMPIValue</code> *value, <code>CMPIType</code> type) </p>
<p> <code>CMPIData</code> <code>getProperty</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, const char *name, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIConstClass</code> * <code>getClass</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIFlags</code> flags, char **properties, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>enumClassNames</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIFlags</code> flags, <code>CMPIStatus</code> *rc) </p>
<p> <code>CMPIEnumeration</code> * <code>enumClasses</code> (<code>CMCIClient</code> *mb, <code>CMPIObjectPath</code> *cop, <code>CMPIFlags</code> flags, <code>CMPIStatus</code> *rc) </p>
<h2>Description</h2>
<p>Client library class that provides the methods for connecting to and accessing the CIMOM.</p>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclientft-associatornames/">CMCIClientFT.associatorNames</a>(3), <a href="/docs/linux/man/3-cmciclientft-associators/">CMCIClientFT.associators</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-createinstance/">CMCIClientFT.createInstance</a>(3), <a href="/docs/linux/man/3-cmciclientft-deleteinstance/">CMCIClientFT.deleteInstance</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-enumclasses/">CMCIClientFT.enumClasses</a>(3), <a href="/docs/linux/man/3-cmciclientft-enumclassnames/">CMCIClientFT.enumClassNames</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-enuminstancenames/">CMCIClientFT.enumInstanceNames</a>(3), <a href="/docs/linux/man/3-cmciclientft-enuminstances/">CMCIClientFT.enumInstances</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-execquery/">CMCIClientFT.execQuery</a>(3), <a href="/docs/linux/man/3-cmciclientft-getclass/">CMCIClientFT.getClass</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-getinstance/">CMCIClientFT.getInstance</a>(3), <a href="/docs/linux/man/3-cmciclientft-getproperty/">CMCIClientFT.getProperty</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-invokemethod/">CMCIClientFT.invokeMethod</a>(3), <a href="/docs/linux/man/3-cmciclientft-referencenames/">CMCIClientFT.referenceNames</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-references/">CMCIClientFT.references</a>(3), <a href="/docs/linux/man/3-cmciclientft-setinstance/">CMCIClientFT.setInstance</a>(3),<br />
 <a href="/docs/linux/man/3-cmciclientft-setproperty/">CMCIClientFT.setProperty</a>(3), <a href="/docs/linux/man/3-cmciconnect/">cmciConnect</a>(3)</p>
