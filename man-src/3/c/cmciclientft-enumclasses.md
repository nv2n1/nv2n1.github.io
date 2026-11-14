---
title: "cmciclientft-enumclasses(3)"
name: "cmciclientft-enumclasses"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-enumclasses/"
description: "CMCICLientFT.enumClasses() – Enumerate classes and subclasss"
---

<p>CMCICLientFT.enumClasses() &#8211; Enumerate classes and subclasss</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.enumClasses</code><i>(CMCIClient*</i><code>cl,</code>
<br>
 CMPIObjectPath* op,
<br>
 CMPIFlags flags,
<br>
 CMPIStatus* rc);
<br></pre>
<h2>Description</h2>
<p>Enumerate Classies using <i>op</i> as reference. The content of the returned classes can be controled using the <i>flags</i> parameter. </p>
<p> Arguments are the client object pointer <i>cl</i>, ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>flags</i> to affect the returned class structure content, and <i>rc</i> the CMPI return status (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contain the flags <i>CMPI_FLAG_LocalOnly</i>, <i>CMPI_FLAG_DeepInheritance</i>, <i>CMPI_FLAG_IncludeQualifiers</i>, and <i>CMPI_FLAG_IncludeClassOrigin</i>. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.enumClasses()</code> function returns a pointer to a CMPIEnumeration object that contains each enumerated class and sets a successful status code in <i>rc</i>. When unsuccessful it returns NULL and sets the <i>rc</i> argument with the error code and and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<p>CMCIClient&nbsp;<wbr>*cc;<br />
CMPIObjectPath&nbsp;<wbr>*&nbsp;<wbr>objectpath;<br />
CMPIInstance&nbsp;<wbr>*&nbsp;<wbr>instance;<br />
CMPIEnumeration&nbsp;<wbr>*&nbsp;<wbr>enumeration;<br />
CMPIStatus status; </p>
<p>/*&nbsp;<wbr>Setup a conncetion to the CIMOM&nbsp;<wbr>*/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
cc&nbsp;<wbr>=&nbsp;<wbr>cmciConnect(&quot;localhost&quot;, NULL, NULL, NULL, NULL, NULL); </p>
<p>objectpath&nbsp;<wbr>=&nbsp;<wbr>newCMPIObjectPath(&quot;root/cimv2&quot;, NULL, NULL);<br />
enumeration&nbsp;<wbr>=&nbsp;<wbr>cc-&gt;ft-&gt;enumClasses(cc, objectpath, 0,&nbsp;<wbr>&amp;status); </p>
<p>if&nbsp;<wbr>(!status.rc)&nbsp;<wbr>{ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fprintf(stderr, &quot;operation error code %d description %s,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>status.rc, status.msg-&gt;hdl);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>abort();</p>
<p>}</p>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
