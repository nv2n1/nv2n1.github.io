---
title: "ecore_config_app_lib_group(3)"
name: "ecore_config_app_lib_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_app_lib_group/"
description: "Ecore Config App Library Functions – Functions that are used to start up and shutdown the Enlightened Property Library when used directly by an application."
---

<p>Ecore Config App Library Functions &#8211; Functions that are used to start up and shutdown the Enlightened Property Library when used directly by an application. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_init</code> (const char *name)<br />
 <i>Initializes the Enlightened Property Library. </i><br />
 EAPI int <code>ecore_config_shutdown</code> (void)<br />
 <i>Frees memory and shuts down the library for an application. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to start up and shutdown the Enlightened Property Library when used directly by an application.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_init (const char * name)</h3>
<p>Initializes the Enlightened Property Library. </p>
<p> Either this function or <code>ecore_config_system_init</code> must be run before any other function in the Enlightened Property Library, even if you have run <code>ecore_init</code> . The name given is used to determine the default configuration to load. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Application name</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the library is successfully set up. ECORE_CONFIG_ERR_FAIL otherwise.</dl>
<p> References ecore_config_get(), ecore_config_string_default(), and ecore_config_theme_default_path_get().</p>
<h3>EAPI int ecore_config_shutdown (void)</h3>
<p>Frees memory and shuts down the library for an application. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_IGNORED .</dl>
<p> References ecore_config_system_shutdown().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
