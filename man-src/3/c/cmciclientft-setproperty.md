---
title: "cmciclientft-setproperty(3)"
name: "cmciclientft-setproperty"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-setproperty/"
description: "CMCIClientFT.setProperty() – Set a named property value of an instance"
---

<p>CMCIClientFT.setProperty() &#8211; Set a named property value of an instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIStatus</code>
<code>CMCIClientFT.setProperty</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>const</code><i>char*</i><code>name,</code>
<br>
<code>CMPIValue*</code><i>value,</i>
<br>
<code>CMPIType</code><i>type);</i>
<br></pre>
<h2>Description</h2>
<p>Set the named property value of an instance identified by reference <i>op</i>. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the namespace and classname to identify the instance, a pointer to a string with the property name to set in <i>name</i>, a pointer to the CMPIValue with the value to set in <i>value</i>, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.setProperty()</code> function returns a CMPIStatus object with a successful operation status code set. When unsuccessful it returns the CMPIStatus object with the error code and corresponding error string set.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpivalue/">CMPIValue</a>(3), <a href="/docs/linux/man/3-cmpitype/">CMPIType</a>(3)</p>
