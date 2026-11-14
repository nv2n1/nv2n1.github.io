---
title: "cmciclientft-enuminstances(3)"
name: "cmciclientft-enuminstances"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-enuminstances/"
description: "CMCIClientFT.enumInstances() – Enumerate instances of a class"
---

<p>CMCIClientFT.enumInstances() &#8211; Enumerate instances of a class</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.enumInstances</code><i>(CMCIClient*</i><code>cl,</code>
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
<p>Enumerate Instances of the class (and subclasses) defined by <i>op</i>. The instance structure and inheritance scope can be controled using the <i>flags</i> argument. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the reference that contains namespace and classname components, <i>flags</i> that affect the content of the returned class instance structures, a <i>properties</i> array, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contains the following flags &#8211; <i>CMPI_FLAG_LocalOnly</i>, <i>CMPI_FLAG_DeepInheritance</i>, <i>CMPI_FLAG_IncludeQualifiers</i> and <i>CMPI_FLAG_IncludeClassOrigin</i>.</p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.enumInstances()</code> function returns a pointer to a CMPIEnumeration object that contains the class instances found for the class and sets a successful operation status code in <i>rc</i>. When unsuccessful it returns a NULL pointer and sets the operation status error code and corresponding error string in <i>rc</i>.</p>
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
enumeration&nbsp;<wbr>=&nbsp;<wbr>cc-&gt;ft-&gt;enumInstances(cc, objectpath, 0, NULL,&nbsp;<wbr>&amp;status); </p>
<p>if&nbsp;<wbr>(!status.rc)&nbsp;<wbr>{ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fprintf(stderr, &quot;operation error code %d description %s,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>status.rc, status.msg-&gt;hdl);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>abort();</p>
<p>}</p>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
