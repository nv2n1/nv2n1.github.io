---
title: "cmciclientft-getclass(3)"
name: "cmciclientft-getclass"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-getclass/"
description: "CMCIClientFT.getClass() – Get class as reference"
---

<p>CMCIClientFT.getClass() &#8211; Get class as reference</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIConstClass</code><i>*</i>
<code>CMCIClientFT.getClass</code><i>(CMCIClient*</i><code>cl,</code>
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
<p>Get Class using <i>op</i> as reference. The content of the returned class structure can be controled using the <i>flags</i> parameter. </p>
<p> Arguments are the client object pointer <i>cl</i>, ObjectPath object pointer <i>op</i> that contains namespace and classname components, <i>flags</i> to affect the returned class structure content, <i>properties</i> array, where if not NULL the members of the array define one or more Property names, and <i>rc</i> the CMPI return status (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contain combinations of the following flags &#8211; CMPI_FLAG_LocalOnly, CMPI_FLAG_IncludeQualifiers and CMPI_FLAG_IncludeClassOrigin. </p>
<p> The <i>properties</i> array defines what properties should be returned for the class. If this argument is not NULL, only the class properties in the list are returned. If it&#8217;s NULL all class properties are returned. </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.getClass()</code> function returns a pointer to a CMPIConstClass object and sets a successful status code in <i>rc</i>. When unsuccessful it returns NULL and sets the <i>rc</i> argument with the error code and and corresponding error string.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<p>CMCIClient&nbsp;<wbr>*cc;<br />
CMPIObjectPath&nbsp;<wbr>*&nbsp;<wbr>objectpath;<br />
CMPIInstance&nbsp;<wbr>*&nbsp;<wbr>instance;<br />
CMPIEnumeration&nbsp;<wbr>*&nbsp;<wbr>enumeration;<br />
CMPIClass&nbsp;<wbr>*class;<br />
CMPIStatus status; </p>
<p>/*&nbsp;<wbr>Setup a conncetion to the CIMOM&nbsp;<wbr>*/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
cc&nbsp;<wbr>=&nbsp;<wbr>cmciConnect(&quot;localhost&quot;, NULL, NULL, NULL, NULL, NULL); </p>
<p>objectpath&nbsp;<wbr>=&nbsp;<wbr>newCMPIObjectPath(&quot;root/cimv2&quot;,&nbsp;<wbr>&quot;Linux_ComputerSystem&quot;, NULL);<br />
class&nbsp;<wbr>=&nbsp;<wbr>cc-&gt;ft-&gt;getClass(cc, objectpath, 0, NULL,&nbsp;<wbr>&amp;status); </p>
<p>if&nbsp;<wbr>(!status.rc)&nbsp;<wbr>{ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fprintf(stderr, &quot;operation error code %d description %s,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>status.rc, status.msg-&gt;hdl);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>abort();</p>
<p>}</p>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpiconstclass/">CMPIConstClass</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
