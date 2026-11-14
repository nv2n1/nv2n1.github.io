---
title: "ecore_imf_lib_group(3)"
name: "ecore_imf_lib_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_imf_lib_group/"
description: "Ecore Input Method Library Functions – Utility functions that set up and shut down the Ecore Input Method library."
---

<p>Ecore Input Method Library Functions &#8211; Utility functions that set up and shut down the Ecore Input Method library. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_imf_init</code> (void)<br />
 <i>Initialises the Ecore_IMF library. </i><br />
 EAPI int <code>ecore_imf_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_IMF library. </i></p>
<h2>Detailed Description</h2>
<p>Utility functions that set up and shut down the Ecore Input Method library.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_imf_init (void)</h3>
<p>Initialises the Ecore_IMF library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_event_type_new().</p>
<h3>EAPI int ecore_imf_shutdown (void)</h3>
<p>Shuts down the Ecore_IMF library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
