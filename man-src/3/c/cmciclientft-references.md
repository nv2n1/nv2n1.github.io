---
title: "cmciclientft-references(3)"
name: "cmciclientft-references"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-references/"
description: "CMCIClientFT.references() – Enumerate association instances for a class instance"
---

<p>CMCIClientFT.references() &#8211; Enumerate association instances for a class instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.references</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>const</code><i>char</i><code>*resultClass,</code>
<br>
<code>const</code><i>char</i><code>*role,</code>
<br>
<code>CMPIFlags</code><i>flags,</i>
<br>
<code>char**</code><i>properties,</i>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Enumerate association instances that refer to the Instance defined by the <i>op</i> reference. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the reference that contains namespace and classname components, <i>resultClass</i>, where if it&#8217;s not NULL is a valid class name that is used to filter the returned set of Objects by eliminating objects that aren&#8217;t an Instance of this Class or one of its subclasses, <i>role</i>, where if it&#8217;s not NULL is a valid property name that is used to filter the returned set of instance objects by eliminating objects that aren&#8217;t associated to the source object by an association where the source object plays the specified role, i.e. the name of the property in the association class that refers to the source object has to match the value of this parameter, <i>flags</i> that affect the content of the returned class instance structures, a <i>properties</i> array, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<p> The <i>flags</i> argument is a bit mask that can contains the following flags &#8211; <i>CMPI_FLAG_IncludeQualifiers</i> and <i>CMPI_FLAG_IncludeClassOrigin</i>.</p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.references()</code> function returns a pointer to a CMPIEnumeration object that contains the class association instance objects found that match the association criteria, and sets a successful operation status code in <i>rc</i>. When unsuccessful it returns a NULL pointer and sets the operation status error code and corresponding error string in <i>rc</i>.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpiflags/">CMPIFlags</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
