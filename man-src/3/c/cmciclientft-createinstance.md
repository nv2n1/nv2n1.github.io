---
title: "cmciclientft-createinstance(3)"
name: "cmciclientft-createinstance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-createinstance/"
description: "CMCIClientFT.createInstance() – Create class instance"
---

<p>CMCIClientFT.createInstance() &#8211; Create class instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIObjectPath</code><i>*</i>
<code>CMCIClientFT.createInstance</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>CMPIInstance*</code><i>inst,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Create class instance using <i>op</i> as reference. </p>
<p> Arguments are the client object pointer <i>cl</i>, ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>inst</i> is a complete instance object pointer, and <i>rc</i> the CMPI operation status (suppressed when NULL). </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.createInstance()</code> function returns a pointer to a CMPIObjectPath object with the new instance reference and sets a successful status code for <i>rc</i>. When unsuccessful it returns NULL and sets the <i>rc</i> argument with the error code and and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiinstance/">CMPIInstance</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
