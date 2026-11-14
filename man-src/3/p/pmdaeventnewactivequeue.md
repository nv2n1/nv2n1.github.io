---
title: "pmdaeventnewactivequeue(3)"
name: "pmdaeventnewactivequeue"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaeventnewactivequeue/"
description: "pmdaEventNewQueue, pmdaEventNewActiveQueue, pmdaEventQueueHandle, pmdaEventQueueAppend, pmdaEventQueueShutdown, pmdaEventQueueRecords, pmdaEventQueueClients, pmdaEventQueueCounter, pmdaEventQueueBy..."
---

<p><code>pmdaEventNewQueue</code>, <code>pmdaEventNewActiveQueue</code>, <code>pmdaEventQueueHandle</code>, <code>pmdaEventQueueAppend</code>, <code>pmdaEventQueueShutdown</code>, <code>pmdaEventQueueRecords</code>, <code>pmdaEventQueueClients</code>, <code>pmdaEventQueueCounter</code>, <code>pmdaEventQueueBytes</code>, <code>pmdaEventQueueMemory</code> &#8211; utilities for PMDAs managing event queues</p>
<h2>C Synopsis</h2>
<pre>#include &lt;pcp/pmapi.h&gt;
#include &lt;pcp/pmda.h&gt;</pre>
<p>int pmdaEventNewQueue(const char *<i>name</i>, size_t <i>maxmem</i>); </p>
<p> int pmdaEventNewActiveQueue(const char *<i>name</i>, size_t <i>maxmem</i>, int <i>nclients</i>); </p>
<p> int pmdaEventQueueHandle(const char *<i>name</i>); </p>
<p> int pmdaEventQueueAppend(int <i>handle</i>, void *<i>buffer</i>, size_t <i>bytes</i>, struct timeval *<i>tv</i>); </p>
<p> int pmdaEventQueueShutdown(int <i>handle</i>); </p>
<p> typedef int (*pmdaEventDecodeCallBack)(int, void *, int, struct timeval *, void *); </p>
<p> int pmdaEventQueueRecords(int <i>handle</i>, pmAtomValue *<i>avp</i>, int <i>context</i>, pmdaEventDecodeCallBack <i>decoder</i>, void *<i>data</i>); </p>
<p> int pmdaEventQueueClients(int <i>handle</i>, pmAtomValue *<i>avp</i>); </p>
<p> int pmdaEventQueueCounter(int <i>handle</i>, pmAtomValue *<i>avp</i>); </p>
<p> int pmdaEventQueueBytes(int <i>handle</i>, pmAtomValue *<i>avp</i>); </p>
<p> int pmdaEventQueueMemory(int <i>handle</i>, pmAtomValue *<i>avp</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>A Performance Metrics Domain Agent (PMDA) that exports event records must effectively act an event multiplexer. Events consumed by the PMDA may have to be forwarded on to any number of monitoring tools (or &quot;client contexts&quot;). These tools may be requesting events at different sampling intervals, and are very unlikely to request an event at the exact moment it arrives at the PMDA, making some form of event buffering and queueing scheme a necessity. Events must be held by the PMDA until either all registered clients have been sent them, or until a memory limit has been reached by the PMDA at which point it must discard older events as new ones arrive. </p>
<p> The routines described here are designed to assist the PMDA developer in managing both client contexts and queues of events at a high level. These fit logically above lower level primitives, such as those described in <code><a href="/docs/linux/man/3-pmdaeventnewarray/">pmdaEventNewArray</a></code>(3), and shield the average PMDA from the details of directly building event record arrays for individual client contexts. </p>
<p> The PMDA registers a new queue of events using either <code>pmdaEventNewQueue</code> or <code>pmdaEventNewActiveQueue</code>. These are passed an identifying <i>name</i> (for diagnostic purposes, and for subsequent lookup by <code>pmdaEventQueueLookup</code>) and <i>maxmem</i>, an upper bound on the memory (in bytes) that can be consumed by events in this queue, before beginning to discard them (resulting in &quot;missed&quot; events for any client that has not kept up). If a queue is dynamically allocated (such that the PMDA may already have clients connected) the <code>pmdaEventNewActiveQueue</code> interface should be used, with the additional <i>numclients</i> parameter indicating the count of active client connections. The return is a negative error code on failure, suitable for decoding by the <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) routine. Any non-negative value indicates success, and provides a <i>handle</i> suitable for passing into the other API routines. </p>
<p> For each new event received by the PMDA, the <code>pmdaEventQueueAppend</code> routine should be called, placing that event into the queue identified by <i>handle</i>. The event itself must be contained in the passed in <i>buffer</i>, having <i>bytes</i> length. The timestamp associated with the event (time at which the event occurred) is passed in via the final <i>tv</i> parameter. </p>
<p> In the PMDAs specific implementation of its fetch callback, when values for an event metric have been requested, the <code>pmdaEventQueueRecords</code> routine should be used. It is passed the queue <i>handle</i> and the <i>avp</i> pmAtomValue structure to fill with event records, for the client making that fetch request (identified by the <i>context</i> parameter). Finally, the PMDA must also pass in an event decoding routine, which is responsible for decoding the fields of a single event into the individual event parameters of that event. The <i>data</i> parameter is an opaque cookie that can be used to pass situation-specific information into each <i>decoder</i> invocation. </p>
<p> Under some situations it is useful for the PMDA to export state about the queues under its control. The accessor routines &#8211; <code>pmdaEventQueueClients</code>, <code>pmdaEventQueueCounter</code>, <code>pmdaEventQueueBytes</code> and <code>pmdaEventQueueMemory</code> provide a mechanism for querying a queue by its <i>handle</i> and filling in a <code>pmAtomValue</code> structure that the <code>pmdaFetchCallBack</code> method should return.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdaeventnewclient/">pmdaEventNewClient</a></code>(3) and <code><a href="/docs/linux/man/3-pmdaeventnewarray/">pmdaEventNewArray</a></code>(3). </p>
