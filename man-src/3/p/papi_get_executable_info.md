---
title: "papi_get_executable_info(3)"
name: "papi_get_executable_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_executable_info/"
description: "PAPI_get_executable_info –"
---

<p>PAPI_get_executable_info &#8211; </p>
<p> Get the executable&#8217;s address space info.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
const PAPI_exe_info_t *PAPI_get_executable_info( void );
This function returns a pointer to a structure containing information 
about the current program.
@param fullname
 Fully qualified path + filename of the executable.
@param name
 Filename of the executable with no path information.
@param text_start, text_end
 Start and End addresses of program text segment.
@param data_start, data_end
 Start and End addresses of program data segment.
@param bss_start, bss_end
 Start and End addresses of program bss segment.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* const PAPI_exe_info_t *prginfo = NULL;
* if ( ( prginfo = PAPI_get_executable_info( ) ) == NULL )
* exit( 1 );
* printf( &quot;Path+Program: %s, exeinfo-&gt;fullname );
* printf( &quot;Program: %s, exeinfo-&gt;address_info.name );
* printf( &quot;Text start: %p, Text end: %p, exeinfo-&gt;address_info.text_start, exeinfo-&gt;address_info.text_end) ;
* printf( &quot;Data start: %p, Data end: %p, exeinfo-&gt;address_info.data_start, exeinfo-&gt;address_info.data_end );
* printf( &quot;Bss start: %p, Bss end: %p, exeinfo-&gt;address_info.bss_start, exeinfo-&gt;address_info.bss_end );
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_opt</code> </p>
<p> <code>PAPI_get_hardware_info</code> </p>
<p> <code>PAPI_exe_info_t</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
