---
title: "ecore_config_file_group(3)"
name: "ecore_config_file_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_file_group/"
description: "Ecore Config File Functions – Functions that are used to load and save properties from and to files."
---

<p>Ecore Config File Functions &#8211; Functions that are used to load and save properties from and to files. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_load</code> (void)<br />
 <i>Loads the default configuration. </i><br />
 EAPI int <code>ecore_config_save</code> (void)<br />
 <i>Saves the current configuration to the default file. </i><br />
 EAPI int <code>ecore_config_file_load</code> (const char *file)<br />
 <i>Load the given configuration file to the local configuration. </i><br />
 EAPI int <code>ecore_config_file_save</code> (const char *file)<br />
 <i>Saves the local configuration to the given file. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to load and save properties from and to files.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_file_load (const char * file)</h3>
<p>Load the given configuration file to the local configuration. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> Name of the file to load.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_NODATA is returned if the file cannot be loaded.</dl>
<p> Referenced by ecore_config_load().</p>
<h3>EAPI int ecore_config_file_save (const char * file)</h3>
<p>Saves the local configuration to the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> Name of the file to save to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC is returned on success. ECORE_CONFIG_ERR_FAIL is returned if the data cannot be saved.</dl>
<p> Referenced by ecore_config_save().</p>
<h3>EAPI int ecore_config_load (void)</h3>
<p>Loads the default configuration. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_NODATA is returned if the file cannot be loaded.</dl>
<p> References ecore_config_file_load().</p>
<h3>EAPI int ecore_config_save (void)</h3>
<p>Saves the current configuration to the default file. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC is returned on success. ECORE_CONFIG_ERR_FAIL is returned if the data cannot be saved.</dl>
<p> References ecore_config_file_save().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
