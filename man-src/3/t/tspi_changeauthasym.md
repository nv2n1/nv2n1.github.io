---
title: "tspi_changeauthasym(3)"
name: "tspi_changeauthasym"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tspi_changeauthasym/"
description: "Tspi_ChangeAuthAsym – change the authorization data of an entity using asymmetric change protocol."
---

<p>Tspi_ChangeAuthAsym &#8211; change the authorization data of an entity using asymmetric change protocol.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tss/platform.h&gt;</code>
<code>#include &lt;tss/tcpa_defines.h&gt;</code>
<code>#include &lt;tss/tcpa_typedef.h&gt;</code>
<code>#include &lt;tss/tcpa_struct.h&gt;</code>
<code>#include &lt;tss/tss_typedef.h&gt;</code>
<code>#include &lt;tss/tss_structs.h&gt;</code>
<code>#include &lt;tss/tspi.h&gt;</code>
<code>TSS_RESULT Tspi_ChangeAuthAsym(TSS_HOBJECT </code><i>hObjectToChange</i><code>, TSS_HOBJECT </code><i>hParentObject</i><code>,</code>
<code> TSS_HKEY </code><i>hIdentKey</i><code>, TSS_HPOLICY </code><i>hNewPolicy</i><code>);</code></pre>
<h2>Description</h2>
<p><code>Tspi_ChangeAuthAsym</code> changes the authorization data (secret) of an entity (object) utilizing the asymmetric change protocol and assigns the object to the policy object. All classes using secrets provide this method for changing their authorization data. This method changes the authorization data of an object ensuring that the parent of the object does not get knowledge of the new secret.</p>
<h2>Parameters</h2>
<h3>hObjectToChange</h3>
<p>Handle of the object the authorization data should be changed. </p>
<h3>hParentObject</h3>
<p>Handle of the parent object wrapping the object addressed by <i>hObjectToChange</i>. </p>
<h3>hIdentKey</h3>
<p>Handle of the identity key object required to proof the internally created temporary key. </p>
<h3>hNewPolicy</h3>
<p>Handle of the policy object providing the new authorization data.</p>
<h2>Return Codes</h2>
<p><code>Tspi_ChangeAuthAsym</code> returns TSS_SUCCESS on success, otherwise one of the following values are returned:</p>
<dl COMPACT>
<dt><font SIZE="-1">TSS_E_INVALID_HANDLE &#8211; Either <i>hObjectToChange</i>, <i>hParentObject</i>, or <i>hIdentKey</i> is an invalid handle.</font></p>
<dd>
<dt><font SIZE="-1">TSS_E_INTERNAL_ERROR &#8211; An error occurred internal to the TSS.</font></p>
<dd></dl>
<h2>Conforming To</h2>
<p><code>Tspi_ChangeAuthAsym</code> conforms to the Trusted Computing Group Software Specification version 1.1 Golden</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tspi_changeauth/">Tspi_ChangeAuth</a></code>(3).</p>
