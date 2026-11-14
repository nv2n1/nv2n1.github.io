---
title: "papi_epc(3)"
name: "papi_epc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_epc/"
description: "PAPI_epc –"
---

<p>PAPI_epc &#8211; </p>
<p> Simplified call to get arbitrary events per cycle, real and processor time.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface: </code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_epc( int event, float *rtime, float *ptime, long long *ref, long long *core, long long *evt, float *epc )</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> event code to be measured (0 defaults to PAPI_TOT_INS)<br />
 <i>*rtime</i> total realtime since the first call<br />
 <i>*ptime</i> total process time since the first call<br />
 <i>*ref</i> incremental reference clock cycles since the last call<br />
 <i>*core</i> incremental core clock cycles since the last call<br />
 <i>*evt</i> total events since the first call<br />
 <i>*epc</i> incremental events per cycle since the last call</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> The counters were already started by something other than <code>PAPI_epc()</code>.<br />
 <i>PAPI_ENOEVNT</i> One of the requested events does not exist.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.</dl>
<p> The first call to <code>PAPI_epc()</code> will initialize the PAPI High Level interface, set up the counters to monitor the user specified event, PAPI_TOT_CYC, and PAPI_REF_CYC (if it exists) and start the counters. </p>
<p> Subsequent calls will read the counters and return total real time, total process time, total event counts since the start of the measurement and the core and reference cycle count and EPC rate since the latest call to <code>PAPI_epc()</code>. </p>
<p> A call to <code>PAPI_stop_counters()</code> will stop the counters from running and then calls such as <code>PAPI_start_counters()</code> or other rate calls can safely be used. </p>
<p> <code>PAPI_epc</code> can provide a more detailed look at algorithm efficiency in light of clock variability in modern cpus. MFLOPS is no longer an adequate description of peak performance if clock rates can arbitrarily speed up or slow down. By allowing a user specified event and reporting reference cycles, core cycles and real time, <code>PAPI_epc</code> provides the information to compute an accurate effective clock rate, and an accurate measure of computational throughput. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_flips()</code> </p>
<p> <code>PAPI_flops()</code> </p>
<p> <code>PAPI_ipc()</code> </p>
<p> <code>PAPI_stop_counters()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
