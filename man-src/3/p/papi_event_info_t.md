---
title: "papi_event_info_t(3)"
name: "papi_event_info_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_event_info_t/"
description: "PAPI_event_info_t –"
---

<p>PAPI_event_info_t &#8211; </p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>unsigned int <code>event_code</code> </p>
<p> char <code>symbol</code> [1024] </p>
<p> char <code>short_descr</code> [64] </p>
<p> char <code>long_descr</code> [1024] </p>
<p> int <code>component_index</code> </p>
<p> char <code>units</code> [64] </p>
<p> int <code>location</code> </p>
<p> int <code>data_type</code> </p>
<p> int <code>value_type</code> </p>
<p> int <code>timescope</code> </p>
<p> int <code>update_type</code> </p>
<p> int <code>update_freq</code> </p>
<p> unsigned int <code>count</code> </p>
<p> unsigned int <code>event_type</code> </p>
<p> char <code>derived</code> [64] </p>
<p> char <code>postfix</code> [256] </p>
<p> unsigned int <code>code</code> [12] </p>
<p> char <code>name</code> [12][256] </p>
<p> char <code>note</code> [1024] </p>
<h2>Field Documentation</h2>
<h3>unsigned int PAPI_event_info_t::code[12]</h3>
<p>array of values that further describe the event:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>presets: native event_code values</p>
<dt>&bull;</p>
<dd>native:, register values(?)</dl>
<h3>int PAPI_event_info_t::component_index</h3>
<p>component this event belongs to</p>
<h3>unsigned int PAPI_event_info_t::count</h3>
<p>number of terms (usually 1) in the code and name fields</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>presets: these are native events</p>
<dt>&bull;</p>
<dd>native: these are unused</dl>
<h3>int PAPI_event_info_t::data_type</h3>
<p>data type returned by PAPI</p>
<h3>char PAPI_event_info_t::derived[64]</h3>
<p>name of the derived type</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>presets: usually NOT_DERIVED</p>
<dt>&bull;</p>
<dd>native: empty string</dl>
<h3>unsigned int PAPI_event_info_t::event_code</h3>
<p>preset (0x8xxxxxxx) or native (0x4xxxxxxx) event code</p>
<h3>unsigned int PAPI_event_info_t::event_type</h3>
<p>event type or category for preset events only</p>
<h3>int PAPI_event_info_t::location</h3>
<p>location event applies to</p>
<h3>char PAPI_event_info_t::long_descr[1024]</h3>
<p>a longer description: typically a sentence for presets, possibly a paragraph from vendor docs for native events</p>
<h3>char PAPI_event_info_t::name[12][256]</h3>
<p>&lt; names of code terms: &#8211; presets: native event names,</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>native: descriptive strings for each register value(?)</dl>
<h3>char PAPI_event_info_t::note[1024]</h3>
<pre> an optional developer note 
 supplied with a preset event
 to delineate platform specific </pre>
<p>&nbsp;<wbr>anomalies or restrictions&nbsp;<wbr></p>
<h3>char PAPI_event_info_t::postfix[256]</h3>
<p>string containing postfix operations; only defined for preset events of derived type DERIVED_POSTFIX</p>
<h3>char PAPI_event_info_t::short_descr[64]</h3>
<p>a short description suitable for use as a label</p>
<h3>char PAPI_event_info_t::symbol[1024]</h3>
<p>name of the event</p>
<h3>int PAPI_event_info_t::timescope</h3>
<p>from start, etc.</p>
<h3>char PAPI_event_info_t::units[64]</h3>
<p>units event is measured in</p>
<h3>int PAPI_event_info_t::update_freq</h3>
<p>how frequently event is updated</p>
<h3>int PAPI_event_info_t::update_type</h3>
<p>how event is updated</p>
<h3>int PAPI_event_info_t::value_type</h3>
<p>sum or absolute </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
