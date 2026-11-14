---
title: "slv2(3)"
name: "slv2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2/"
description: "SLV2 – SLV2 is written in standard C99, and depends only on the Redland RDF library ("
---

<p>SLV2 &#8211; SLV2 is written in standard C99, and depends only on the Redland RDF library (</p>
<p><a rel="nofollow" href="http://librdf.org">http://librdf.org</a>). It should be portable to any system with Redland, and is tested on various GNU/Linux distributions (often), and MacOS X (occasionally). The data (RDF) and code (shared library) functionality in SLV2 is strictly separated so it is simple to control where each is used (e.g. it is possible to discover/investigate plugins and related data without loading any shared libraries, avoiding the associated risks). The SLV2 documentation is broken into several pages:</p>
<dl>
<dt>&bull;</p>
<dd><code>slv2_world </code> &#8211; Global library initialisation, state, plugin discovery, etc.</dl>
<dl>
<dt>&bull;</p>
<dd><code>slv2_util </code> &#8211; Generally useful utility functions</dl>
<dl>
<dt>&bull;</p>
<dd><code>slv2_collections </code> &#8211; Collections of values (literals and URIs) and objects</dl>
<dl>
<dt>&bull;</p>
<dd><code>slv2_data </code> &#8211; Access to plugin RDF data</dl>
<dl>
<dt>&bull;</p>
<dd><code>slv2_library </code> &#8211; Access to plugin shared libraries</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
