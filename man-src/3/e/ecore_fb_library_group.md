---
title: "ecore_fb_library_group(3)"
name: "ecore_fb_library_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_fb_library_group/"
description: "Framebuffer Library Functions – Functions used to set up and shut down the Ecore_Framebuffer functions."
---

<p>Framebuffer Library Functions &#8211; Functions used to set up and shut down the Ecore_Framebuffer functions. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_fb_init</code> (const char *name __UNUSED__)<br />
 <i>Sets up the Ecore_Fb library. </i><br />
 EAPI int <code>ecore_fb_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Fb library. </i></p>
<h2>Detailed Description</h2>
<p>Functions used to set up and shut down the Ecore_Framebuffer functions.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_fb_init (const char *name __UNUSED__)</h3>
<p>Sets up the Ecore_Fb library. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> device target name</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on failure. Otherwise, the number of times the library has been initialised without being shut down.</dl>
<p> References ecore_event_type_new(). </p>
<p> Referenced by ecore_evas_fb_new().</p>
<h3>EAPI int ecore_fb_shutdown (void)</h3>
<p>Shuts down the Ecore_Fb library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the system has been initialised without being shut down.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
