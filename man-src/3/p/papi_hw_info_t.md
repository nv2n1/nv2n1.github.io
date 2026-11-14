---
title: "papi_hw_info_t(3)"
name: "papi_hw_info_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_hw_info_t/"
description: "PAPI_hw_info_t –"
---

<p>PAPI_hw_info_t &#8211; </p>
<p> Hardware info structure.</p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>int <code>ncpu</code> </p>
<p> int <code>threads</code> </p>
<p> int <code>cores</code> </p>
<p> int <code>sockets</code> </p>
<p> int <code>nnodes</code> </p>
<p> int <code>totalcpus</code> </p>
<p> int <code>vendor</code> </p>
<p> char <code>vendor_string</code> [128] </p>
<p> int <code>model</code> </p>
<p> char <code>model_string</code> [128] </p>
<p> float <code>revision</code> </p>
<p> int <code>cpuid_family</code> </p>
<p> int <code>cpuid_model</code> </p>
<p> int <code>cpuid_stepping</code> </p>
<p> int <code>cpu_max_mhz</code> </p>
<p> int <code>cpu_min_mhz</code> </p>
<p> <code>PAPI_mh_info_t</code> <code>mem_hierarchy</code> </p>
<p> int <code>virtualized</code> </p>
<p> char <code>virtual_vendor_string</code> [128] </p>
<p> char <code>virtual_vendor_version</code> [128] </p>
<p> float <code>mhz</code> </p>
<p> int <code>clock_mhz</code> </p>
<p> int <code>reserved</code> [8] </p>
<h2>Field Documentation</h2>
<h3>int PAPI_hw_info_t::clock_mhz</h3>
<p>Deprecated</p>
<h3>int PAPI_hw_info_t::cores</h3>
<p>Number of cores per socket</p>
<h3>int PAPI_hw_info_t::cpu_max_mhz</h3>
<p>Maximum supported CPU speed</p>
<h3>int PAPI_hw_info_t::cpu_min_mhz</h3>
<p>Minimum supported CPU speed</p>
<h3>int PAPI_hw_info_t::cpuid_family</h3>
<p>cpuid family</p>
<h3>int PAPI_hw_info_t::cpuid_model</h3>
<p>cpuid model</p>
<h3>int PAPI_hw_info_t::cpuid_stepping</h3>
<p>cpuid stepping</p>
<h3><code>PAPI_mh_info_t</code> PAPI_hw_info_t::mem_hierarchy</h3>
<p>PAPI memory heirarchy description</p>
<h3>float PAPI_hw_info_t::mhz</h3>
<p>Deprecated</p>
<h3>int PAPI_hw_info_t::model</h3>
<p>Model number of CPU</p>
<h3>char PAPI_hw_info_t::model_string[128]</h3>
<p>Model string of CPU</p>
<h3>int PAPI_hw_info_t::ncpu</h3>
<p>Number of CPUs per NUMA Node</p>
<h3>int PAPI_hw_info_t::nnodes</h3>
<p>Total Number of NUMA Nodes</p>
<h3>float PAPI_hw_info_t::revision</h3>
<p>Revision of CPU</p>
<h3>int PAPI_hw_info_t::sockets</h3>
<p>Number of sockets</p>
<h3>int PAPI_hw_info_t::threads</h3>
<p>Number of hdw threads per core</p>
<h3>int PAPI_hw_info_t::totalcpus</h3>
<p>Total number of CPUs in the entire system</p>
<h3>int PAPI_hw_info_t::vendor</h3>
<p>Vendor number of CPU</p>
<h3>char PAPI_hw_info_t::vendor_string[128]</h3>
<p>Vendor string of CPU</p>
<h3>char PAPI_hw_info_t::virtual_vendor_string[128]</h3>
<p>Vendor for virtual machine</p>
<h3>char PAPI_hw_info_t::virtual_vendor_version[128]</h3>
<p>Version of virtual machine</p>
<h3>int PAPI_hw_info_t::virtualized</h3>
<p>Running in virtual machine </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
