---
title: "papi_flops(3)"
name: "papi_flops"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_flops/"
description: "PAPI_flops –"
---

<p>PAPI_flops &#8211; </p>
<p> Simplified call to get Mflops/s (floating point operation rate), real and processor time.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface: </code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_flops( float *rtime, float *ptime, long long *flpops, float *mflops )</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*rtime</i> total realtime since the first call<br />
 <i>*ptime</i> total process time since the first call<br />
 <i>*flpops</i> total floating point operations since the first call<br />
 <i>*mflops</i> incremental (Mega) floating point operations per seconds since the last call</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> The counters were already started by something other than <code>PAPI_flops()</code>.<br />
 <i>PAPI_ENOEVNT</i> The floating point operations event does not exist.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.</dl>
<p> The first call to <code>PAPI_flops()</code> will initialize the PAPI High Level interface, set up the counters to monitor the PAPI_FP_OPS event and start the counters. </p>
<p> Subsequent calls will read the counters and return total real time, total process time, total floating point operations since the start of the measurement and the Mflop/s rate since latest call to <code>PAPI_flops()</code>. A call to <code>PAPI_stop_counters()</code> will stop the counters from running and then calls such as <code>PAPI_start_counters()</code> or other rate calls can safely be used. </p>
<p> <code>PAPI_flops</code> returns information related to theoretical floating point operations rather than simple instructions. It uses the PAPI_FP_OPS event which attempts to &#8216;correctly&#8217; account for, e.g., FMA undercounts and FP Store overcounts, etc. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_flips()</code> </p>
<p> <code>PAPI_ipc()</code> </p>
<p> <code>PAPI_epc()</code> </p>
<p> <code>PAPI_stop_counters()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
