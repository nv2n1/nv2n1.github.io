---
title: "papi_get_hardware_info(3)"
name: "papi_get_hardware_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_hardware_info/"
description: "PAPI_get_hardware_info –"
---

<p>PAPI_get_hardware_info &#8211; </p>
<p> get information about the system hardware</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>In C, this function returns a pointer to a structure containing information about the hardware on which the program runs. 
 In Fortran, the values of the structure are returned explicitly.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.</pre>
<pre>@note The C structure contains detailed information about cache and TLB sizes. 
 This information is not available from Fortran.
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> const PAPI_hw_info_t *hwinfo = NULL;
 if (PAPI_library_init(PAPI_VER_CURRENT) != PAPI_VER_CURRENT) 
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if ((hwinfo = PAPI_get_hardware_info()) == NULL)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 printf(&quot;%d CPUs at %f Mhz.
&quot;,hwinfo-&gt;totalcpus,hwinfo-&gt;mhz);
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_hw_info_t</code> </p>
<p> <code>PAPI_get_executable_info</code>, <code>PAPI_get_opt</code>, <code>PAPI_get_dmem_info</code>, <code>PAPI_library_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
