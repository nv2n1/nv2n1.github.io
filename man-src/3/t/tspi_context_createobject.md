---
title: "tspi_context_createobject(3)"
name: "tspi_context_createobject"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_context_createobject/"
description: "Tspi_Context_CreateObject – create an empty object and return a handle to that object."
---

<p>Tspi_Context_CreateObject &#8211; create an empty object and return a handle to that object.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Context_CreateObject(TSS_HCONTEXT </code><i>hContext</i><code>, TSS_FLAG </code><i>objectType</i><code>,</code>
<code> TSS_FLAG </code><i>initFlags</i><code>, TSS_HOBJECT* </code><i>phObject</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Context_CreateObject</code> creates and initializes an empty object of the specified type and returns a handle addressing that object. The object is bound to an already opened context <i>hContext</i>.</p>
<h2>Parameters</h2>
<h3>hContext</h3>
<p>The handle of the context object. </p>
<h3>objectType</h3>
<p>Flag indicating the object type to create. Possible types are:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_OBJECT_TYPE_POLICY &#8211; a policy object.</font></p>
<dd>
<dt><font SIZE="-1">TSS_OBJECT_TYPE_ENCDATA &#8211; an encrypted data object (either sealed or bound data).</font></p>
<dd>
<dt><font SIZE="-1">TSS_OBJECT_TYPE_RSAKEY &#8211; an RSA key.</font></p>
<dd>
<dt><font SIZE="-1">TSS_OBJECT_TYPE_PCRS &#8211; a PCR composite object.</font></p>
<dd>
<dt><font SIZE="-1">TSS_OBJECT_TYPE_HASH &#8211; a hash object.</font></p>
<dd></dl>
<h3>initFlags</h3>
<p>Flag indicating the default attributes of the object. Attributes for each type of object are:</p>
<dl COMPACT>
<dt><font SIZE="-1">Policy:</font></p>
<dd>&nbsp;<wbr><code>TSS_POLICY_USAGE</code>&nbsp;<wbr>&#8211; a usage policy&nbsp;<wbr>(for authorization to use an object).<br />
&nbsp;<wbr><code>TSS_POLICY_MIGRATION</code>&nbsp;<wbr>&#8211; a migration policy.</p>
<dt><font SIZE="-1">Encrypted data objects:</font></p>
<dd>&nbsp;<wbr><code>TSS_ENCDATA_SEAL</code>&nbsp;<wbr>&#8211; A data object used for a Seal operation.<br />
&nbsp;<wbr><code>TSS_ENCDATA_BIND</code>&nbsp;<wbr>&#8211; A data object used for a Bind operation.<br />
&nbsp;<wbr><code>TSS_ENCDATA_LEGACY</code>&nbsp;<wbr>&#8211; A data object for a bind operation using a legacy key.</p>
<dt><font SIZE="-1">RSA Keys:</font></p>
<dd>&nbsp;<wbr><code>TSS_KEY_SIZE_DEFAULT</code>&nbsp;<wbr>&#8211; Use the default key size of the TCS you&#8217;re connected to.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_512</code>&nbsp;<wbr>&#8211; Create a 512 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_1024</code>&nbsp;<wbr>&#8211; Create a 1024 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_2048</code>&nbsp;<wbr>&#8211; Create a 2048 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_4096</code>&nbsp;<wbr>&#8211; Create a 4096 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_8192</code>&nbsp;<wbr>&#8211; Create a 8192 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_SIZE_16384</code>&nbsp;<wbr>&#8211; Create a 16384 bit key.<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_STORAGE</code>&nbsp;<wbr>&#8211; Create a storage key.&nbsp;<wbr>(Used to wrap other keys).<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_SIGNING</code>&nbsp;<wbr>&#8211; Create a signing key.<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_BIND</code>&nbsp;<wbr>&#8211; Create a binding key.&nbsp;<wbr>(Used to encrypt data).<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_IDENTITY</code>&nbsp;<wbr>&#8211; Create an identity key.&nbsp;<wbr>(Used for an identity).<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_LEGACY</code>&nbsp;<wbr>&#8211; Create a legacy key.&nbsp;<wbr>(Can be used for signing and binding, created from data external to a TSS).<br />
&nbsp;<wbr><code>TSS_KEY_TYPE_AUTHCHANGE</code>&nbsp;<wbr>&#8211; Create an ephemeral key used to change authorization values.<br />
&nbsp;<wbr><code>TSS_KEY_VOLATILE</code>&nbsp;<wbr>&#8211; Create a volatile key.&nbsp;<wbr>(Must be unloaded at startup).<br />
&nbsp;<wbr><code>TSS_KEY_NON_VOLATILE</code>&nbsp;<wbr>&#8211; Create a non-volatile key.&nbsp;<wbr>(May be unloaded at startup).<br />
&nbsp;<wbr><code>TSS_KEY_MIGRATABLE</code>&nbsp;<wbr>&#8211; Create a migratable key.<br />
&nbsp;<wbr><code>TSS_KEY_NOT_MIGRATABLE</code>&nbsp;<wbr>&#8211; Create a non-migratable key.&nbsp;<wbr>[DEFAULT]<br />
&nbsp;<wbr><code>TSS_KEY_AUTHORIZATION</code>&nbsp;<wbr>&#8211; Key will require authorization.<br />
&nbsp;<wbr><code>TSS_KEY_NO_AUTHORIZATION</code>&nbsp;<wbr>&#8211; Key will not require authorization.&nbsp;<wbr>[DEFAULT]<br />
&nbsp;<wbr><code>TSS_KEY_EMPTY_KEY</code>&nbsp;<wbr>&#8211; Key template which will be returned as an object with very few attributes. </p>
<dt><font SIZE="-1">PCR composite objects:</font></p>
<dd>&nbsp;<wbr>None.</p>
<dt><font SIZE="-1">Hash objects:</font></p>
<dd>&nbsp;<wbr><code>TSS_HASH_SHA1</code>&nbsp;<wbr>&#8211; a hash object of type SHA-1.<br />
&nbsp;<wbr><code>TSS_HASH_OTHER</code>&nbsp;<wbr>&#8211; a hash object of type other than SHA-1.</dl>
<h3>phObject</h3>
<p>The handle of the object to be created. </p>
<h2>Return Codes</h2>
<p><code>Tspi_Context_CreateObject</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hContext</i> or <i>phObject</i> is an invalid handle. </font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Context_CreateObject</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_context_closeobject/">Tspi_Context_CloseObject</a></code>(3).</p>
