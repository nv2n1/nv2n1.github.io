---
title: "cmciclientft-getinstance(3)"
name: "cmciclientft-getinstance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-getinstance/"
description: "CMCIClientFT.getInstance() – Get class instance"
---

<p>CMCIClientFT.getInstance() &#8211; Get class instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIInstance</code><i>*</i>
<code>CMCIClientFT.getInstance</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>CMPIFlags</code><i>flags,</i>
<br>
<code>char**</code><i>properties,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Get class instance using <i>op</i> as reference. The content of the returned class instance structure can be controled using the <i>flags</i> parameter. </p>
<p> Arguments are the client object pointer <i>cl</i>, ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>flags</i> to affect the returned class instance structure content,<br />
&nbsp;<wbr><i>properties</i>&nbsp;<wbr>array, and&nbsp;<wbr><i>rc</i>&nbsp;<wbr>which returns the operation status&nbsp;<wbr> (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contain combinations of the following flags &#8211; <i>CMPI_FLAG_LocalOnly</i>, <i>CMPI_FLAG_IncludeQualifiers</i>, and <i>CMPI_FLAG_IncludeClassOrigin</i>. </p>
<p> The <i>properties</i> array defines what properties should be returned for the class. If this argument is not NULL, only the class properties in the list are returned. If it&#8217;s NULL all class properties are returned. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.getInstance()</code> function returns a pointer to a CMPIInstance object and sets a successful status code for <i>rc</i>. When unsuccessful it returns NULL and sets the <i>rc</i> argument with the error code and and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpiinstance/">CMPIInstance</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
