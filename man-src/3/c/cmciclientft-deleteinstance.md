---
title: "cmciclientft-deleteinstance(3)"
name: "cmciclientft-deleteinstance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-deleteinstance/"
description: "CMCIClientFT.deleteInstance() – Delete class instance"
---

<p>CMCIClientFT.deleteInstance() &#8211; Delete class instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIStatus</code>
<code>CMCIClientFT.deleteInstance</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op);</i>
<br></pre>
<h2>Description</h2>
<p>Delete a class instance using <i>op</i> as the instance reference. </p>
<p> Arguments are the client object pointer <i>cl</i> and an ObjectPath object pointer <i>op</i> that contains namespace and classname components. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.deleteInstance()</code> function returns a CMPIStatus object with a successful operation status code. When unsuccessful it returns the operation error code and corresponding error string in the CMPIStatus object.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3)</p>
