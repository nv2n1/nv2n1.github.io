---
title: "cmciclientft-invokemethod(3)"
name: "cmciclientft-invokemethod"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-invokemethod/"
description: "CMCIClientFT.invokeMethod() – Invoke a named method of an instance"
---

<p>CMCIClientFT.invokeMethod() &#8211; Invoke a named method of an instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.invokeMethod</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>const</code><i>char*</i><code>method,</code>
<br>
<code>CMPIArgs*</code><i>in,</i>
<br>
<code>CMPIArgs*</code><i>out,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Invoke a named method of an instance defined by the <i>op</i> reference. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the reference that contains namespace and classname components, <i>method</i> pointer to string that identifies the class method, <i>in</i> pointer to the input arguments, <i>out</i> pointer to the output parameters, and <i>rc</i> which returns the operation status (suppressed when NULL).</p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.invokeMethod()</code> function returns the CMPIData value returned by the method invoked and sets a successful operation status code in <i>rc</i>. When unsuccessful it returns a NULL pointer and sets the operation status error code and corresponding error string in <i>rc</i>.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiargs/">CMPIArgs</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
