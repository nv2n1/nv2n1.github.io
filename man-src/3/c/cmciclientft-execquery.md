---
title: "cmciclientft-execquery(3)"
name: "cmciclientft-execquery"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmciclientft-execquery/"
description: "CMCIClientFT.execQuery() – Query the enumeration of instances of a class"
---

<p>CMCIClientFT.execQuery() &#8211; Query the enumeration of instances of a class</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;cmci.h&gt;</code>
<code>CMPIEnumeration</code><i>*</i>
<code>CMCIClientFT.execQuery</code><i>(CMCIClient*</i><code>cl,</code>
<br>
<code>CMPIObjectPath*</code><i>op,</i>
<br>
<code>const</code><i>char*</i><code>query,</code>
<br>
<code>const</code><i>char*</i><code>lang,</code>
<br>
<code>CMPIStatus*</code><i>rc);</i>
<br></pre>
<h2>Description</h2>
<p>Query the enumeration of instances of the class (and subclasses) defined by reference <i>op</i> using the <i>query</i> expression. </p>
<p> Arguments are the client object pointer <i>cl</i>, an ObjectPath object pointer <i>op</i> with the reference that contains namespace and classname components, the query expression string pointer in <i>query</i>, the query language identifier string pointer in <i>lang</i>, and <i>rc</i> which returns the operation status (suppressed when NULL). </p>
<h2>Return Value</h2>
<p>When successful the <code>CMCIClientFT.execQuery()</code> function returns a pointer to a CMPIEnumeration object that contains the class instances that match the query and sets a successful operation status code. When unsuccessful it returns a NULL pointer and sets the operation status error code and corresponding error string in <i>rc</i>.</p>
<h2>Errors</h2>
<h2>Examples</h2>
<h2>Conforming To</h2>
<h2>See Also</h2>
<p>Common Manageability Programming Interface (CMPI) &#8211; OpenGroup,<br />
 <a href="/docs/linux/man/3-cmciclient/">CMCIClient</a>(3), <a href="/docs/linux/man/3-cmpienumeration/">CMPIEnumeration</a>(3), <a href="/docs/linux/man/3-cmpiobjectpath/">CMPIObjectPath</a>(3), <a href="/docs/linux/man/3-cmpistatus/">CMPIStatus</a>(3)</p>
