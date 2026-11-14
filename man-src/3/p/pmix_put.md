---
title: "pmix_put(3)"
name: "pmix_put"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmix_put/"
---

PMIx_Put - Push a value into the client's namespace

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix.h&gt;

pmix_status_t PMIx_Init(pmix_scope_t scope, const char key[], pmix_value_t *val);</code></pre>

<h2>Arguments</h2>

scope : Defines a scope for data &quot;put&quot; by PMI per the following:
<dl><dd><pre>*&nbsp;<wbr>PMI_LOCAL - the data is intended only for other application
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>processes on the same node. Data marked in this way
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>will not be included in data packages sent to remote requestors
*&nbsp;<wbr>PMI_REMOTE - the data is intended solely for applications processes on
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remote nodes. Data marked in this way will not be shared with
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>other processes on the same node
*&nbsp;<wbr>PMI_GLOBAL - the data is to be shared with all other requesting processes,
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>regardless of location</pre></dl>
 

 key String key identifying the information. This can be either one of the PMIx defined attributes, or a user-defined value 

 val Pointer to a pmix_value_t structure containing the data to be pushed along with the type of the provided data.

<h2>Description</h2>

Push a value into the client's namespace. The client library will cache the information locally until PMIxCommit_ is called. The provided scope value is passed to the local PMIx server, which will distribute the data as directed.

<h2>Return Value</h2>

Returns PMIX_SUCCESS on success. On error, a negative value corresponding to a PMIx errno is returned.

<h2>Errors</h2>

PMIx errno values are defined in pmix_common.h.

<h2>Notes</h2>

See 'pmix_common.h' for definition of the pmix_value_t structure.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-pmix_constants/">PMIx_Constants</a>(7), <a HREF="/docs/linux/man/7-pmix_structures/">PMIx_Structures</a>(7)

<h2>Authors</h2>

PMIx.
