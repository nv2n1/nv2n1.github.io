---
title: "papif_get_exe_info(3)"
name: "papif_get_exe_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papif_get_exe_info/"
description: "PAPIF_get_exe_info –"
---

<p>PAPIF_get_exe_info &#8211; </p>
<p> get information about the dynamic memory usage of the current program</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Fortran Interface:</code></p>
<dl COMPACT>
<dd>#include &#8216;fpapi.h&#8217;<br />
 <code>PAPIF_get_exe_info</code>( C_STRING fullname, C_STRING name, </p>
<p>&nbsp;<wbr>C_LONG_LONG text_start, C_LONG_LONG text_end,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>C_LONG_LONG data_start, C_LONG_LONG data_end,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>C_LONG_LONG bss_start, C_LONG_LONG bss_end, C_INT check&nbsp;<wbr>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_executable_info</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
