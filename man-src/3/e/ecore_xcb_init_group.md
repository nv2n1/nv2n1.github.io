---
title: "ecore_xcb_init_group(3)"
name: "ecore_xcb_init_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_xcb_init_group/"
description: "X Library Init and Shutdown Functions – Functions that start and shut down the Ecore X Library."
---

<p>X Library Init and Shutdown Functions &#8211; Functions that start and shut down the Ecore X Library. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_init</code> (const char *name)<br />
 <i>Initialize the X display connection to the given display. </i><br />
 EAPI int <code>ecore_x_shutdown</code> (void)<br />
 <i>Shuts down the Ecore X library. </i><br />
 EAPI int <code>ecore_x_disconnect</code> (void)<br />
 <i>Shuts down the Ecore X library. </i></p>
<h2>Detailed Description</h2>
<p>Functions that start and shut down the Ecore X Library.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_disconnect (void)</h3>
<p>Shuts down the Ecore X library. </p>
<p> As ecore_xcb_shutdown, except do not close Display, only connection.</p>
<h3>EAPI int ecore_x_init (const char * name)</h3>
<p>Initialize the X display connection to the given display. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Display target name. If NULL, the default display is assumed.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the library has been initialized without being shut down. 0 is returned if an error occurs.</dl>
<p> References ecore_event_filter_add(), ecore_event_type_new(), ECORE_FD_READ, ecore_main_fd_handler_add(), ECORE_X_NET_WM_PROTOCOL_PING, ECORE_X_NET_WM_PROTOCOL_SYNC_REQUEST, ecore_x_netwm_init(), ecore_x_window_override_new(), ECORE_X_WM_PROTOCOL_DELETE_REQUEST, and ECORE_X_WM_PROTOCOL_TAKE_FOCUS.</p>
<h3>EAPI int ecore_x_shutdown (void)</h3>
<p>Shuts down the Ecore X library. </p>
<p> In shutting down the library, the X display connection is terminated and any event handlers for it are removed. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the library has been initialized without being shut down.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
