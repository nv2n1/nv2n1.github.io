---
title: "cmciclientft-getproperty(3)"
name: "cmciclientft-getproperty"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-getproperty/"
description: "CMCIClientFT.getProperty() – Get a named property value of an instance"
---

<p>CMCIClientFT.getProperty() &#8211; Get a named property value of an instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIData</code>
<code>CMCIClientFT.getProperty</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>const</code><i>char*</i><code>name,</code>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Get the named property value of an instance identified by reference <i>op</i>. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the namespace and classname to identify the instance, a pointer to a string with the property name to get in <i>name</i>, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.getProperty()</code> function returns a CMPIData object with the instance property value and sets a successful operation status code in <i>rc</i>. When unsuccessful it returns the CMPIStatus object with sets an operation status error code and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpidata/">CMPIData</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
