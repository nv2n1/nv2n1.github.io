---
title: "pmdaattribute(3)"
name: "pmdaattribute"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaattribute/"
description: "pmdaAttribute – informs a PMDA about client connection attributes"
---

<p><code>pmdaAttribute</code> &#8211; informs a PMDA about client connection attributes</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaAttribute(int </code><i>context</i>, int <i>key</i>, char *<i>value</i>, int <i>length</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaAttribute</code> is the generic callback for responding to client connection attributes. These attributes include client credential information, such as user ID and group ID. </p>
<p> A PMDA that supports connection attributes will provide a private <code>pmdaAttribute</code> callback by assignment to <i>version.six.attribute</i> of the <i>pmdaInterface</i> structure, and implement custom logic for any of the attribute <i>key</i>&#8211;<i>value</i> pairs of interest to it. </p>
<p> All attributes are associated with a specific client context, and these can be uniquely identified using the <i>ctx</i> first argument. The PMDA should track client connections, and disconnections using the <code><a href="/docs/linux/man/3-pmdasetendcontextcallback/">pmdaSetEndContextCallBack</a></code>(3) interface, as a result. The <code><a href="/docs/linux/man/3-pmdagetcontext/">pmdaGetContext</a></code>(3) interface may be particularly helpful also. </p>
<p> All attributes are passed as <i>key</i>&#8211;<i>value</i> pairs and the <i>value</i> is always passed as a null-terminated string of given <i>length</i>. This includes numeric attributes like the user ID. </p>
<p> The most commonly used attributes would be PCP_ATTR_USERID and PCP_ATTR_GROUPID but others may also be optionally passed (such as PCP_ATTR_USERNAME) if they are available. Some attributes will be consumed by <code>pmcd</code> and never through passed to PMDAs, such as PCP_ATTR_PASSWORD. A complete list of all possible attributes can be found in the headers listed above, all are prefixed by PCP_ATTR.</p>
<h2>Diagnostics</h2>
<p><code>pmdaAttribute</code> should return either zero on success, or a negative return code to indicate an error in handling the attribute. This return code cannot be used to indicate a client should be disallowed access &#8211; such functionality must be performed by the agent in response to callbacks for the client in question (using PM_ERR_PERMISSION for those specific callbacks, for that specific client. In other words, errors will be be passed to PMCD but there is no guarantee made that the error will be return to the client and result in termination of the client, for example.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_6 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdamain/">pmdaMain</a></code>(3) and <code><a href="/docs/linux/man/3-pmdagetcontext/">pmdaGetContext</a></code>(3). </p>
