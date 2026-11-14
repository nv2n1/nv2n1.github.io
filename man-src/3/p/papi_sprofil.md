---
title: "papi_sprofil(3)"
name: "papi_sprofil"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_sprofil/"
description: "PAPI_sprofil –"
---

<p>PAPI_sprofil &#8211; </p>
<p> Generate PC histogram data from multiple code regions where hardware counter overflow occurs.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_sprofil(&nbsp;<wbr>PAPI_sprofil_t&nbsp;<wbr>*&nbsp;<wbr>prof, int profcnt, int EventSet, int EventCode, int threshold, int flags&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*prof</i> pointer to an array of <code>PAPI_sprofil_t</code> structures. Each copy of the structure contains the following: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>buf &#8212; pointer to a buffer of bufsiz bytes in which the histogram counts are stored in an array of unsigned short, unsigned int, or unsigned long long values, or &#8216;buckets&#8217;. The size of the buckets is determined by values in the flags argument.</p>
<dt>&bull;</p>
<dd>bufsiz &#8212; the size of the histogram buffer in bytes. It is computed from the length of the code region to be profiled, the size of the buckets, and the scale factor as discussed below.</p>
<dt>&bull;</p>
<dd>offset &#8212; the start address of the region to be profiled.</p>
<dt>&bull;</p>
<dd>scale &#8212; broadly and historically speaking, a contraction factor that indicates how much smaller the histogram buffer is than the region to be profiled. More precisely, scale is interpreted as an unsigned 16-bit fixed-point fraction with the decimal point implied on the left. Its value is the reciprocal of the number of addresses in a subdivision, per counter of histogram buffer.</dl>
<p> <i>profcnt</i> number of structures in the prof array for hardware profiling.<br />
 <i>EventSet</i> The PAPI EventSet to profile. This EventSet is marked as profiling-ready, but profiling doesn&#8217;t actually start until a <code>PAPI_start()</code> call is issued.<br />
 <i>EventCode</i> Code of the Event in the EventSet to profile. This event must already be a member of the EventSet.<br />
 <i>threshold</i> minimum number of events that must occur before the PC is sampled. If hardware overflow is supported for your component, this threshold will trigger an interrupt when reached. Otherwise, the counters will be sampled periodically and the PC will be recorded for the first sample that exceeds the threshold. If the value of threshold is 0, profiling will be disabled for this event.<br />
 <i>flags</i> bit pattern to control profiling behavior. Defined values are given in a table in the documentation for PAPI_pofil<br />
&nbsp;<wbr><br />
&nbsp;<wbr></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>Return</i> values for <code>PAPI_sprofil()</code> are identical to those for <code>PAPI_profil</code>. Please refer to that page for further details.<br />
&nbsp;<wbr><br />
&nbsp;<wbr></dl>
<p> <code>PAPI_sprofil()</code> is a structure driven profiler that profiles one or more disjoint regions of code in a single call. It accepts a pointer to a preinitialized array of sprofil structures, and initiates profiling based on the values contained in the array. Each structure in the array defines the profiling parameters that are normally passed to <code>PAPI_profil()</code>. For more information on profiling, <code>PAPI_profil</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr> </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int retval;
* unsigned long length;
* PAPI_exe_info_t *prginfo;
* unsigned short *profbuf1, *profbuf2, profbucket;
* PAPI_sprofil_t sprof[3];
*
* prginfo = PAPI_get_executable_info();
* if (prginfo == NULL) handle_error( NULL );
* length = (unsigned long)(prginfo-&gt;text_end - prginfo-&gt;text_start);
* // Allocate 2 buffers of equal length
* profbuf1 = (unsigned short *)malloc(length);
* profbuf2 = (unsigned short *)malloc(length);
* if ((profbuf1 == NULL) || (profbuf2 == NULL))
* handle_error( NULL );
* memset(profbuf1,0x00,length);
* memset(profbuf2,0x00,length);
* // First buffer
* sprof[0].pr_base = profbuf1;
* sprof[0].pr_size = length;
* sprof[0].pr_off = (caddr_t) DO_FLOPS;
* sprof[0].pr_scale = 0x10000;
* // Second buffer
* sprof[1].pr_base = profbuf2;
* sprof[1].pr_size = length;
* sprof[1].pr_off = (caddr_t) DO_READS;
* sprof[1].pr_scale = 0x10000;
* // Overflow bucket
* sprof[2].pr_base = profbucket;
* sprof[2].pr_size = 1;
* sprof[2].pr_off = 0;
* sprof[2].pr_scale = 0x0002;
* retval = PAPI_sprofil(sprof, EventSet, PAPI_FP_INS, 1000000,
* PAPI_PROFIL_POSIX | PAPI_PROFIL_BUCKET_16)) != PAPI_OK)
* if ( retval != PAPI_OK ) handle_error( retval );
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_overflow</code> </p>
<p> <code>PAPI_get_executable_info</code> </p>
<p> <code>PAPI_profil</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
