---
title: "papi_overflow(3)"
name: "papi_overflow"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_overflow/"
description: "PAPI_overflow –"
---

<p>PAPI_overflow &#8211; </p>
<p> Set up an event set to begin registering overflows.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>PAPI_overflow()</code> marks a specific EventCode in an EventSet to generate an overflow signal after every threshold events are counted. More than one event in an event set can be used to trigger overflows. In such cases, the user must call this function once for each overflowing event. To turn off overflow on a specified event, call this function with a threshold value of 0. </p>
<p> Overflows can be implemented in either software or hardware, but the scope is the entire event set. PAPI defaults to hardware overflow if it is available. In the case of software overflow, a periodic timer interrupt causes PAPI to compare the event counts against the threshold values and call the overflow handler if one or more events have exceeded their threshold. In the case of hardware overflow, the counters are typically set to the negative of the threshold value and count up to 0. This zero-crossing triggers a hardware interrupt that calls the overflow handler. Because of this counter interrupt, the counter values for overflowing counters may be very small or even negative numbers, and cannot be relied upon as accurate. In such cases the overflow handler can approximate the counts by supplying the threshold value whenever an overflow occurs. </p>
<p> _papi_overflow_handler() is a placeholder for a user-defined function to process overflow events. A pointer to this function is passed to the <code>PAPI_overflow</code> routine, where it is invoked whenever a software or hardware overflow occurs. This handler receives the EventSet of the overflowing event, the Program Counter address when the interrupt occured, an overflow_vector that can be processed to determined which event(s) caused the overflow, and a pointer to the machine context, which can be used in a platform-specific manor to extract register information about what was happening when the overflow occured. </p>
<p> <code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_overflow</code>&nbsp;<wbr>(int EventSet, int EventCode, int threshold, int flags, PAPI_overflow_handler_t handler&nbsp;<wbr>);&nbsp;<wbr> </p>
<p>&nbsp;<wbr>(*PAPI_overflow_handler_t)&nbsp;<wbr>_papi_overflow_handler&nbsp;<wbr>(int EventSet, void&nbsp;<wbr>*address, long_long overflow_vector, void&nbsp;<wbr>*context&nbsp;<wbr>);</dl>
<p> <code>Fortran Interface:</code></p>
<dl COMPACT>
<dd>Not implemented</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle to a PAPI event set as created by <code>PAPI_create_eventset</code><br />
 <i>EventCode</i> &#8212; the preset or native event code to be set for overflow detection. This event must have already been added to the EventSet.<br />
 <i>threshold</i> &#8212; the overflow threshold value for this EventCode.<br />
 <i>flags</i> &#8212; bitmap that controls the overflow mode of operation. Set to PAPI_OVERFLOW_FORCE_SW to force software overflowing, even if hardware overflow support is available. If hardware overflow support is available on a given system, it will be the default mode of operation. There are situations where it is advantageous to use software overflow instead. Although software overflow is inherently less accurate, with more latency and processing overhead, it does allow for overflowing on derived events, and for the accurate recording of overflowing event counts. These two features are typically not available with hardware overflow. Only one type of overflow is allowed per event set, so setting one event to hardware overflow and another to forced software overflow will result in an error being returned.<br />
 <i>handler</i> &#8212; pointer to the user supplied handler function to call upon overflow<br />
 <i>address</i> &#8212; the Program Counter address at the time of the overflow<br />
 <i>overflow_vector</i> &#8212; a long long word containing flag bits to indicate which hardware counter(s) caused the overflow<br />
 <i>*context</i> &#8212; pointer to a machine specific structure that defines the register context at the time of overflow. This parameter is often unused and can be ignored in the user function.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i> On success, <code>PAPI_overflow</code> returns PAPI_OK.<br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid. Most likely a bad threshold value.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> The EventSet is currently counting events.<br />
 <i>PAPI_ECNFLCT</i> The underlying counter hardware cannot count this event and other events in the EventSet simultaneously. Also can happen if you are trying to overflow both by hardware and by forced software at the same time.<br />
 <i>PAPI_ENOEVNT</i> The PAPI event is not available on the underlying hardware.</dl>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>* // Define a simple overflow handler:
* void handler(int EventSet, void *address, long_long overflow_vector, void *context)
* {
* fprintf(stderr,* address,overflow_vector);
* }
*
* // Call PAPI_overflow for an EventSet containing PAPI_TOT_INS,
* // setting the threshold to 100000. Use the handler defined above.
* retval = PAPI_overflow(EventSet, PAPI_TOT_INS, 100000, 0, handler);
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_overflow_event_index</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
