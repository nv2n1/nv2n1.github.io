---
title: "papi_enum_cmp_event(3)"
name: "papi_enum_cmp_event"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_enum_cmp_event/"
description: "PAPI_enum_cmp_event –"
---

<p>PAPI_enum_cmp_event &#8211; </p>
<p> Enumerate PAPI preset or native events for a given component.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_enum_cmp_event( int *EventCode, int modifer, int cidx );
Given an event code, PAPI_enum_event replaces the event 
code with the next available event.
The modifier argument affects which events are returned. 
For all platforms and event types, a value of PAPI_ENUM_ALL (zero) 
directs the function to return all possible events. @n
For native events, the effect of the modifier argument may be
 different on each platform. 
See the discussion below for platform-specific definitions.
@param *EventCode
 A defined preset or native event such as PAPI_TOT_INS.
@param modifier 
 Modifies the search logic. See below for full list.
 For native events, each platform behaves differently. 
 See platform-specific documentation for details.
 @param cidx
 Specifies the component to search in 
@retval PAPI_ENOEVNT 
 The next requested PAPI preset or native event is not available on 
 the underlying hardware.
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* // Scan for all supported native events on the first component
* printf( &quot;Name			 Code	 Description );
* do {
* retval = PAPI_get_event_info( i, &amp;info );
* if ( retval == PAPI_OK ) {
* printf( &quot;%-30s 0x%-10xs, info.symbol, info.event_code, info.long_descr );
* }
* } while ( PAPI_enum_cmp_event( &amp;i, PAPI_ENUM_ALL, 0 ) == PAPI_OK );
* </pre>
<p><code>Generic Modifiers</code></p>
<dl COMPACT>
<dd>The following values are implemented for preset events </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_ENUM_EVENTS &#8212; Enumerate all (default)</p>
<dt>&bull;</p>
<dd>PAPI_ENUM_FIRST &#8212; Enumerate first event (preset or native) preset/native chosen based on type of EventCode</dl>
</dl>
<p> <code>Native Modifiers</code></p>
<dl COMPACT>
<dd>The following values are implemented for native events </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_UMASKS &#8212; Given an event, iterate through possible umasks one at a time</p>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_UMASK_COMBOS &#8212; Given an event, iterate through all possible combinations of umasks. This is not implemented on libpfm4.</dl>
</dl>
<p> <code>Preset Modifiers</code></p>
<dl COMPACT>
<dd>The following values are implemented for preset events </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_AVAIL &#8212; enumerate only available presets</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_MSC &#8212; Miscellaneous preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_INS &#8212; Instruction related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_IDL &#8212; Stalled or Idle preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_BR &#8212; Branch related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_CND &#8212; Conditional preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_MEM &#8212; Memory related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_CACH &#8212; Cache related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_L1 &#8212; L1 cache related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_L2 &#8212; L2 cache related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_L3 &#8212; L3 cache related preset events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_TLB &#8212; Translation Lookaside Buffer events</p>
<dt>&bull;</p>
<dd>PAPI_PRESET_ENUM_FP &#8212; Floating Point related preset events</dl>
</dl>
<p> <code>ITANIUM Modifiers</code></p>
<dl COMPACT>
<dd>The following values are implemented for modifier on Itanium: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_IARR &#8211; Enumerate IAR (instruction address ranging) events</p>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_DARR &#8211; Enumerate DAR (data address ranging) events</p>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_OPCM &#8211; Enumerate OPC (opcode matching) events</p>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_IEAR &#8211; Enumerate IEAR (instr event address register) events</p>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_DEAR &#8211; Enumerate DEAR (data event address register) events</dl>
</dl>
<p> <code>POWER Modifiers</code></p>
<dl COMPACT>
<dd>The following values are implemented for POWER </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_NTV_ENUM_GROUPS &#8211; Enumerate groups to which an event belongs</dl>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>PAPI </p>
<p>&nbsp;<wbr>PAPIF&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_enum_event</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_get_event_info</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_event_name_to_code</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>PAPI_preset&nbsp;<wbr> </p>
<p>&nbsp;<wbr>PAPI_native&nbsp;<wbr></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
