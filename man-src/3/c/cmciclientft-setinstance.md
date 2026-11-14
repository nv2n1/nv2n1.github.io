---
title: "cmciclientft-setinstance(3)"
name: "cmciclientft-setinstance"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-setinstance/"
description: "CMCIClientFT.setInstance() – Replace class instance"
---

<p>CMCIClientFT.setInstance() &#8211; Replace class instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIStatus</code><i>*</i>
<code>CMCIClientFT.setInstance</code><i>(CMCIClient*</i><code>cl,</code>
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
<p>Replace a class instance with <i>inst</i> using <i>op</i> as reference. The content of the returned class instance structure can be controled using the <i>flags</i> parameter. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>flags</i> to affect the returned class instance structure content,<br />
&nbsp;<wbr><i>properties</i>&nbsp;<wbr>array, and&nbsp;<wbr><i>rc</i>&nbsp;<wbr>which returns the operation status&nbsp;<wbr> (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contain the following flag &#8211; <i>CMPI_FLAG_IncludeQualifiers</i>. </p>
<p> The <i>properties</i> array defines what properties should be returned for the class. If this argument is not NULL, only the class properties in the list are returned. If it&#8217;s NULL all class properties are returned. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.setInstance()</code> function returns a CMPIStatus object with a successful operation status code. When unsuccessful it returns the operation error code and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3)</p>
