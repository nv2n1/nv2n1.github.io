---
title: "tspi_policy_setsecret(3)"
name: "tspi_policy_setsecret"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_policy_setsecret/"
description: "Tspi_Policy_SetSecret – set the authorization data of a policy object and define the handling of its retrieval"
---

<p>Tspi_Policy_SetSecret &#8211; set the authorization data of a policy object and define the handling of its retrieval</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_Policy_SetSecret(TSS_HPOLICY </code><i>hPolicy</i><code>, TSS_FLAG </code><i>secretMode</i><code>,</code>
<code> UINT32 </code><i>ulSecretLength</i><code>, BYTE* </code><i>rgbSecret</i><code>);</code></pre>
<h2>Description</h2>
<p><code>TSS_Policy_SetSecret</code> sets the authorization data for an object. This mthod also defines the handling of its retrieving. There are mand different paths as specified by the secretMode Flag.</p>
<h2>Parameters</h2>
<h3>hPolicy</h3>
<p>The handle of the policy object. </p>
<h3>secretMode</h3>
<p>Flag indicating the policy secret mode to set. Possible values are:<br />
&nbsp;<wbr><code>TSS_SECRET_MODE_SHA1</code>&nbsp;<wbr>&#8211; Secret in the form of 20 bytes of SHA-1 data. The secret will not be touched by the TSP.<br />
&nbsp;<wbr><code>TSS_SECRET_MODE_PLAIN</code>&nbsp;<wbr>&#8211; The data passed in will be hashed by the TSP using SHA-1.<br />
&nbsp;<wbr><code>TSS_SECRET_MODE_POPUP</code>&nbsp;<wbr>&#8211; The TSP will ask for a secret by displaying a GUI pop-up window.<br />
&nbsp;<wbr><code>TSS_SECRET_MODE_CALLBACK</code>&nbsp;<wbr>&#8211; The application will provide a callback function for authorization data.<br />
&nbsp;<wbr><code>TSS_SECRET_MODE_NONE</code>&nbsp;<wbr>&#8211;&nbsp;<wbr><i>ulSecretLen</i>&nbsp;<wbr>and&nbsp;<wbr><i>rgbSecret</i>&nbsp;<wbr>are ignored and any object requiring auth assigned this policy will return an error. </p>
<h3>ulSecretLength</h3>
<p>The length (in bytes) of the rgbSecret parameter. </p>
<h3>rgbSecret</h3>
<p>The secret data blob.</p>
<h2>Return Codes</h2>
<p><code>Tspi_Policy_SetSecret</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; hPolicy is an invalid parameter.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_Policy_SetSecret</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_policy_flushsecret/">Tspi_Policy_FlushSecret</a></code>(3).</p>
