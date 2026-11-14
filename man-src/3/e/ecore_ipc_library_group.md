---
title: "ecore_ipc_library_group(3)"
name: "ecore_ipc_library_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_ipc_library_group/"
description: "IPC Library Functions – Functions that set up and shut down the Ecore IPC Library."
---

<p>IPC Library Functions &#8211; Functions that set up and shut down the Ecore IPC Library. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_ipc_init</code> (void)<br />
 <i>Initialises the Ecore IPC library. </i><br />
 EAPI int <code>ecore_ipc_shutdown</code> (void)<br />
 <i>Shuts down the Ecore IPC library. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set up and shut down the Ecore IPC Library.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_ipc_init (void)</h3>
<p>Initialises the Ecore IPC library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_con_init(), ecore_event_handler_add(), and ecore_event_type_new().</p>
<h3>EAPI int ecore_ipc_shutdown (void)</h3>
<p>Shuts down the Ecore IPC library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of times the library has been initialised without being shut down.</dl>
<p> References ecore_con_shutdown(), ecore_event_handler_del(), and ecore_ipc_server_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
