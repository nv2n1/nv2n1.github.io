---
title: "pmdaeventclients(3)"
name: "pmdaeventclients"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaeventclients/"
description: "pmdaEventNewClient, pmdaEventEndClient, pmdaEventClients – client context tracking interfaces for event queues"
---

<p><code>pmdaEventNewClient</code>, <code>pmdaEventEndClient</code>, <code>pmdaEventClients</code> &#8211; client context tracking interfaces for event queues</p>
<h2>C Synopsis</h2>
<pre>#include &lt;pcp/pmapi.h&gt;
#include &lt;pcp/impl.h&gt;
#include &lt;pcp/pmda.h&gt;</pre>
<p>int pmdaEventNewClient(int <i>context</i>); </p>
<p> int pmdaEventEndClient(int <i>context</i>); </p>
<p> int pmdaEventClients(pmAtomValue *<i>avp</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>A Performance Metrics Domain Agent (PMDA) that exports event records needs to track which clients are connected to it, in order that it can track which events have been sent to which clients so far. Only once an event has been sent to all monitoring tools that registered an interest can the event be discarded and any memory reclaimed. </p>
<p> The <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) library provides callback routines for PMDA developers to provide custom handling of client connections and disconnections. If the PMDA is making use of the event queueing mechanism provided by <code><a href="/docs/linux/man/3-pmdaeventnewqueue/">pmdaEventNewQueue</a></code>(3) and friends, client connections and disconnections must be tracked via calls to <code>pmdaEventNewClient</code> and <code>pmdaEventEndClient</code> respectively. This allows the library to keep track of when events can be discarded from a queue, for example, for the <i>context</i> specified. This parameter is passed into the e_endCallBack function directly, and for other callback functions is available via the e_context field of the pmdaExt structure. Additionally, it can be queried at any time using <code><a href="/docs/linux/man/3-pmdagetcontext/">pmdaGetContext</a></code>(3). </p>
<p> Sometimes it is useful for the PMDA to export a metric indicating the current count of attached clients &#8211; this is available using the <code>pmdaEventClients</code> routine, which will fill in the <i>avp</i> pmAtomValue structure on behalf of a PMDA fetch callback routine.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmdaeventnewarray/">pmdaEventNewArray</a></code>(3), <code><a href="/docs/linux/man/3-pmdaeventnewqueue/">pmdaEventNewQueue</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) and <code><a href="/docs/linux/man/3-pmeventflagsstr/">pmEventFlagsStr</a></code>(3). </p>
