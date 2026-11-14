---
title: "papi_flips(3)"
name: "papi_flips"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_flips/"
description: "PAPI_flips –"
---

<p>PAPI_flips &#8211; </p>
<p> Simplified call to get Mflips/s (floating point instruction rate), real and processor time.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface: </code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_flips( float *rtime, float *ptime, long long *flpins, float *mflips )</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*rtime</i> total realtime since the first call<br />
 <i>*ptime</i> total process time since the first call<br />
 <i>*flpins</i> total floating point instructions since the first call<br />
 <i>*mflips</i> incremental (Mega) floating point instructions per seconds since the last call</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> The counters were already started by something other than <code>PAPI_flips()</code>.<br />
 <i>PAPI_ENOEVNT</i> The floating point instructions event does not exist.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.</dl>
<p> The first call to <code>PAPI_flips()</code> will initialize the PAPI High Level interface, set up the counters to monitor the PAPI_FP_INS event and start the counters. </p>
<p> Subsequent calls will read the counters and return total real time, total process time, total floating point instructions since the start of the measurement and the Mflip/s rate since latest call to <code>PAPI_flips()</code>. A call to <code>PAPI_stop_counters()</code> will stop the counters from running and then calls such as <code>PAPI_start_counters()</code> or other rate calls can safely be used. </p>
<p> <code>PAPI_flips</code> returns information related to floating point instructions using the PAPI_FP_INS event. This is intended to measure instruction rate through the floating point pipe with no massaging. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_flops()</code> </p>
<p> <code>PAPI_ipc()</code> </p>
<p> <code>PAPI_epc()</code> </p>
<p> <code>PAPI_stop_counters()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
