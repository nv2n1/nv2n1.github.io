---
title: "ecore_con_lib_group(3)"
name: "ecore_con_lib_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_con_lib_group/"
description: "Ecore Connection Library Functions – Utility functions that set up and shut down the Ecore Connection library."
---

<p>Ecore Connection Library Functions &#8211; Utility functions that set up and shut down the Ecore Connection library. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_con_init</code> (void)<br />
 <i>Initialises the Ecore_Con library. </i><br />
 EAPI int <code>ecore_con_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Con library. </i></p>
<h2>Detailed Description</h2>
<p>Utility functions that set up and shut down the Ecore Connection library.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_con_init (void)</h3>
<p>Initialises the Ecore_Con library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_event_type_new(), and ecore_list_new(). </p>
<p> Referenced by ecore_ipc_init().</p>
<h3>EAPI int ecore_con_shutdown (void)</h3>
<p>Shuts down the Ecore_Con library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_list_destroy(), ecore_list_empty_is(), and ecore_list_first_remove(). </p>
<p> Referenced by ecore_ipc_shutdown().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
