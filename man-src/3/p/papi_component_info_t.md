---
title: "papi_component_info_t(3)"
name: "papi_component_info_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_component_info_t/"
description: "PAPI_component_info_t –"
---

<p>PAPI_component_info_t &#8211; </p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>char <code>name</code> [128] </p>
<p> char <code>short_name</code> [64] </p>
<p> char <code>description</code> [128] </p>
<p> char <code>version</code> [64] </p>
<p> char <code>support_version</code> [64] </p>
<p> char <code>kernel_version</code> [64] </p>
<p> char <code>disabled_reason</code> [128] </p>
<p> int <code>disabled</code> </p>
<p> int <code>CmpIdx</code> </p>
<p> int <code>num_cntrs</code> </p>
<p> int <code>num_mpx_cntrs</code> </p>
<p> int <code>num_preset_events</code> </p>
<p> int <code>num_native_events</code> </p>
<p> int <code>default_domain</code> </p>
<p> int <code>available_domains</code> </p>
<p> int <code>default_granularity</code> </p>
<p> int <code>available_granularities</code> </p>
<p> int <code>hardware_intr_sig</code> </p>
<p> int <code>component_type</code> </p>
<p> int <code>reserved</code> [8] </p>
<p> unsigned int <code>hardware_intr</code>:1 </p>
<p> unsigned int <code>precise_intr</code>:1 </p>
<p> unsigned int <code>posix1b_timers</code>:1 </p>
<p> unsigned int <code>kernel_profile</code>:1 </p>
<p> unsigned int <code>kernel_multiplex</code>:1 </p>
<p> unsigned int <code>fast_counter_read</code>:1 </p>
<p> unsigned int <code>fast_real_timer</code>:1 </p>
<p> unsigned int <code>fast_virtual_timer</code>:1 </p>
<p> unsigned int <code>attach</code>:1 </p>
<p> unsigned int <code>attach_must_ptrace</code>:1 </p>
<p> unsigned int <code>cntr_umasks</code>:1 </p>
<p> unsigned int <code>cpu</code>:1 </p>
<p> unsigned int <code>inherit</code>:1 </p>
<p> unsigned int <code>reserved_bits</code>:12 </p>
<h2>Detailed Description</h2>
<h2>Field Documentation</h2>
<h3>unsigned int PAPI_component_info_t::attach</h3>
<p>Supports attach</p>
<h3>unsigned int PAPI_component_info_t::attach_must_ptrace</h3>
<p>Attach must first ptrace and stop the thread/process</p>
<h3>int PAPI_component_info_t::available_domains</h3>
<p>Available domains</p>
<h3>int PAPI_component_info_t::available_granularities</h3>
<p>Available granularities</p>
<h3>int PAPI_component_info_t::CmpIdx</h3>
<p>Index into the vector array for this component; set at init time</p>
<h3>unsigned int PAPI_component_info_t::cntr_umasks</h3>
<p>counters have unit masks</p>
<h3>int PAPI_component_info_t::component_type</h3>
<p>Type of component</p>
<h3>unsigned int PAPI_component_info_t::cpu</h3>
<p>Supports specifying cpu number to use with event set</p>
<h3>int PAPI_component_info_t::default_domain</h3>
<p>The default domain when this component is used</p>
<h3>int PAPI_component_info_t::default_granularity</h3>
<p>The default granularity when this component is used</p>
<h3>char PAPI_component_info_t::description[128]</h3>
<p>Description of the component</p>
<h3>int PAPI_component_info_t::disabled</h3>
<p>0 if enabled, otherwise error code from initialization</p>
<h3>char PAPI_component_info_t::disabled_reason[128]</h3>
<p>Reason for failure of initialization</p>
<h3>unsigned int PAPI_component_info_t::fast_counter_read</h3>
<p>Supports a user level PMC read instruction</p>
<h3>unsigned int PAPI_component_info_t::fast_real_timer</h3>
<p>Supports a fast real timer</p>
<h3>unsigned int PAPI_component_info_t::fast_virtual_timer</h3>
<p>Supports a fast virtual timer</p>
<h3>unsigned int PAPI_component_info_t::hardware_intr</h3>
<p>hw overflow intr, does not need to be emulated in software</p>
<h3>int PAPI_component_info_t::hardware_intr_sig</h3>
<p>Signal used by hardware to deliver PMC events</p>
<h3>unsigned int PAPI_component_info_t::inherit</h3>
<p>Supports child processes inheriting parents counters</p>
<h3>unsigned int PAPI_component_info_t::kernel_multiplex</h3>
<p>In kernel multiplexing</p>
<h3>unsigned int PAPI_component_info_t::kernel_profile</h3>
<p>Has kernel profiling support (buffered interrupts or sprofil-like)</p>
<h3>char PAPI_component_info_t::kernel_version[64]</h3>
<p>Version of the kernel PMC support driver</p>
<h3>char PAPI_component_info_t::name[128]</h3>
<p>Name of the component we&#8217;re using</p>
<h3>int PAPI_component_info_t::num_cntrs</h3>
<p>Number of hardware counters the component supports</p>
<h3>int PAPI_component_info_t::num_mpx_cntrs</h3>
<p>Number of hardware counters the component or PAPI can multiplex supports</p>
<h3>int PAPI_component_info_t::num_native_events</h3>
<p>Number of native events the component supports</p>
<h3>int PAPI_component_info_t::num_preset_events</h3>
<p>Number of preset events the component supports</p>
<h3>unsigned int PAPI_component_info_t::posix1b_timers</h3>
<p>Using POSIX 1b interval timers (timer_create) instead of setitimer</p>
<h3>unsigned int PAPI_component_info_t::precise_intr</h3>
<p>Performance interrupts happen precisely</p>
<h3>char PAPI_component_info_t::short_name[64]</h3>
<pre> Short name of component,</pre>
<p>&nbsp;<wbr>to be prepended to event names&nbsp;<wbr></p>
<h3>char PAPI_component_info_t::support_version[64]</h3>
<p>Version of the support library</p>
<h3>char PAPI_component_info_t::version[64]</h3>
<p>Version of this component </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
