---
title: "cmciclientft-enumclassnames(3)"
name: "cmciclientft-enumclassnames"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-enumclassnames/"
description: "CMCICLientFT.enumClassNames() – Enumerate class names"
---

<p>CMCICLientFT.enumClassNames() &#8211; Enumerate class names</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.enumClassNames</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>CMPIFlags</code><i>flags,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Get Class using <i>op</i> as reference. The content of the returned class structure can be controled using the <i>flags</i> parameter. </p>
<p> Arguments are the client object pointer <i>cl</i>, ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>flags</i> to affect the returned class structure content, and <i>rc</i> the CMPI return status (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contain the flag <i>CMPI_FLAG_DeepInheritance</i>. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.enumClassNames()</code> function returns a pointer to a CMPIEnumeration object that contains each class name found and sets a successful status code in <i>rc</i>. When unsuccessful it returns NULL and sets the <i>rc</i> argument with the error code and and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<pre> CMCIClient *cc;
 CMPIObjectPath * objectpath;
 CMPIEnumeration * enumeration;
 CMPIStatus status;
 /* Setup a conncetion to the CIMOM */ 
 cc = cmciConnect(&quot;localhost&quot;, NULL, NULL, NULL, NULL, NULL);
 objectpath = newCMPIObjectPath(&quot;root/cimv2&quot;, NULL, NULL);
 enumeration = cc-&gt;ft-&gt;enumClassNames(cc, objectpath, 0, &amp;status);
 if (!status.rc) {
 fprintf(stderr, &quot;op error code %d description %s,
 status.rc, status.msg-&gt;hdl);
 abort();
 }</pre>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
