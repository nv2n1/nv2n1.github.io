---
title: "cmciclientft-enuminstancenames(3)"
name: "cmciclientft-enuminstancenames"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-enuminstancenames/"
description: "CMCIClientFT.enumInstanceNames() – Enumerate instance names of a class"
---

<p>CMCIClientFT.enumInstanceNames() &#8211; Enumerate instance names of a class</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.enumInstanceNames</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Enumerate Instance Names of the class (and subclasses) defined by <i>op</i>. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the reference that contains namespace and classname components, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.enumInstanceNames()</code> function returns a pointer to a CMPIEnumeration object that contains strings for each instance name found for the class and sets a successful operation status code in <i>rc</i>. When unsuccessful it returns a NULL pointer and sets the operation status error code and corresponding error string in <i>rc</i>.</p>
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
enumeration&nbsp;<wbr>=&nbsp;<wbr>cc-&gt;ft-&gt;enumInstanceNames(cc, objectpath,&nbsp;<wbr>&amp;status); </p>
<p>if&nbsp;<wbr>(!status.rc)&nbsp;<wbr>{ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fprintf(stderr, &quot;operation error code %d description %s,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>status.rc, status.msg-&gt;hdl);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>abort();</p>
<p>}</p>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
