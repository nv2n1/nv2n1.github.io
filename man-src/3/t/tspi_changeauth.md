---
title: "tspi_changeauth(3)"
name: "tspi_changeauth"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_changeauth/"
description: "Tspi_ChangeAuth – change the authorization data of an entity."
---

<p>Tspi_ChangeAuth &#8211; change the authorization data of an entity.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_ChangeAuth(TSS_HOBJECT </code><i>hObjectToChange</i><code>, TSS_HOBJECT </code><i>hParentObject</i><code>,</code>
<code> TSS_HPOLICY </code><i>hNewPolicy</i><code> );</code></pre>
<h2>Description</h2>
<p><code>Tspi_ChangeAuth </code> changes the authorization data (secret) of an entity (object) and assigns the object to the policy object. All classes using secrets provide this method for changing their authorization data.</p>
<h2>Parameters</h2>
<h3>hObjectToChange</h3>
<p>Handle of the object to change authorization for. </p>
<h3>hParentObject</h3>
<p>Handle of the parent object wrapping the object addressed by hObjectToChange. </p>
<h3>hNewPolicy</h3>
<p>Handle of the policy object providing the new authorization data.</p>
<h2>Return Codes</h2>
<p><code>Tspi_ChangeAuth</code> returns TSS_SUCCESS on success,otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hObjectToChange</i>, or <i>hParentObject</i> are not a valid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_ChangeAuth</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_changeauthasym/">Tspi_ChangeAuthAsym</a></code>(3).</p>
