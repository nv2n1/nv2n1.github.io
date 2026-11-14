---
title: "brlapi__getdisplaysize(3)"
name: "brlapi__getdisplaysize"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi__getdisplaysize/"
description: "Getting Terminal information –"
---

<p>Getting Terminal information &#8211; </p>
<p> How to get information about the connected Terminal.</p>
<h3>Macros</h3>
<p>#define <code>BRLAPI_MAXNAMELENGTH</code> 31 </p>
<h3>Functions</h3>
<p>int <code>BRLAPI_STDCALL</code> <code>brlapi_getDriverName</code> (char *buffer, size_t size) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__getDriverName</code> (<code>brlapi_handle_t</code> *handle, char *buffer, size_t size) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi_getDisplaySize</code> (unsigned int *x, unsigned int *y) </p>
<p> int <code>BRLAPI_STDCALL</code> <code>brlapi__getDisplaySize</code> (<code>brlapi_handle_t</code> *handle, unsigned int *x, unsigned int *y) </p>
<h2>Detailed Description</h2>
<p>Before using Raw mode or key codes, the application should always check the type of the connected terminal, to be sure it is really the one it expects. </p>
<p> One should also check for display size, so as to adjust further displaying on it.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_MAXNAMELENGTH 31</h3>
<p>Maximum name length for names embeded in BrlAPI packets, not counting any termination 
