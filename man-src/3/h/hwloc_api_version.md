---
title: "hwloc_api_version(3)"
name: "hwloc_api_version"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_api_version/"
description: "hwlocality_api_version – API version"
---

<p>hwlocality_api_version &#8211; API version </p>
<h3>Macros</h3>
<p>#define <code>HWLOC_API_VERSION</code> 0x00010b00 </p>
<p> #define <code>HWLOC_COMPONENT_ABI</code> 4 </p>
<h3>Functions</h3>
<p>unsigned <code>hwloc_get_api_version</code> (void) </p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define HWLOC_API_VERSION 0x00010b00</h3>
<p>Indicate at build time which hwloc API version is being used.</p>
<h3>#define HWLOC_COMPONENT_ABI 4</h3>
<p>Current component and plugin ABI version (see <code>hwloc/plugins.h</code>)</p>
<h2>Function Documentation</h2>
<h3>unsigned hwloc_get_api_version (void)</h3>
<p>Indicate at runtime which hwloc API version was used at build time. Should be <code>HWLOC_API_VERSION</code> if running on the same version.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code.</p>
