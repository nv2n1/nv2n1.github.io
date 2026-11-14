---
title: "globus_gsi_sysconfig(3)"
name: "globus_gsi_sysconfig"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig/"
description: "Globus GSI System Config API –"
---

<h2 class="name">NAME</h2>
<p> Globus GSI System Config API &#8211; </p>
<h3>Modules</h3>
<p> <code>Defines</code> </p>
<p> <code>Functions for UNIX platforms</code> </p>
<p> <code>Functions for Win32 platforms</code> </p>
<p> <code>Functions for all platforms</code> </p>
<p> <code>Activation</code> </p>
<p> <code>Data Types</code> </p>
<h2>Detailed Description</h2>
<p> This API provides helper functions for detecting installation and environment specific settings applicable to GSI. It also servers as a abstraction layer for OS specific programming details. The public interface for this library consists of the GLOBUS_GSI_SYSCONFIG_* macros that point at the resolve to platform specific functions. <code>You should never use the platform specific functions directly.</code>. </p>
<p> Any program that uses Globus GSI System Config functions must include the <code>globus_gsi_system_config.h</code> header.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_sysconfig from the source code. </p>
<h2>Index</h2>
