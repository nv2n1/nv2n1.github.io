---
title: "papi_get_shared_lib_info(3)"
name: "papi_get_shared_lib_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_shared_lib_info/"
description: "PAPI_get_shared_lib_info –"
---

<p>PAPI_get_shared_lib_info &#8211; </p>
<p> Get address info about the shared libraries used by the process.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p>In C, this function returns a pointer to a structure containing information about the shared library used by the program. There is no Fortran equivalent call. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This data will be incorporated into the <code>PAPI_get_executable_info</code> call in the future. <code>PAPI_get_shared_lib_info</code> will be deprecated and should be used with caution.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_shlib_info_t</code> </p>
<p> <code>PAPI_get_hardware_info</code> </p>
<p> <code>PAPI_get_executable_info</code> </p>
<p> <code>PAPI_get_dmem_info</code> </p>
<p> <code>PAPI_get_opt</code> <code>PAPI_library_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
