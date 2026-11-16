---
title: "globus_callout_error_type_not_registered(3)"
name: "globus_callout_error_type_not_registered"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout_error_type_not_registered/"
description: "Callout Constants –"
---

<p>Callout Constants &#8211; </p>
<p> Constants.</p>
<h3>Enumerations</h3>
<p>enum <code>globus_callout_error_t</code> { <code>GLOBUS_CALLOUT_ERROR_SUCCESS</code> = 0, <code>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</code> = 1, <code>GLOBUS_CALLOUT_ERROR_OPENING_CONF_FILE</code> = 2, <code>GLOBUS_CALLOUT_ERROR_PARSING_CONF_FILE</code> = 3, <code>GLOBUS_CALLOUT_ERROR_WITH_DL</code> = 4, <code>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</code> = 5, <code>GLOBUS_CALLOUT_ERROR_TYPE_NOT_REGISTERED</code> = 6, <code>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR</code> = 7, <code>GLOBUS_CALLOUT_ERROR_LAST</code> = 8 } </p>
<h2>Detailed Description</h2>
<p>Constants. </p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_callout_error_t</code></h3>
<p>Globus Callout Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_CALLOUT_ERROR_SUCCESS </i></dt>
<dd>Success &#8211; never used</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE </i></dt>
<dd>Hash table operation failed</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_OPENING_CONF_FILE </i></dt>
<dd>Failed to open configuration file</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_PARSING_CONF_FILE </i></dt>
<dd>Failed to parse configuration file</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_WITH_DL </i></dt>
<dd>Dynamic library operation failed</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY </i></dt>
<dd>Out of memory</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_TYPE_NOT_REGISTERED </i></dt>
<dd>The abstract type could not be found</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR </i></dt>
<dd>The callout itself returned a error</dd>
<dt><i>GLOBUS_CALLOUT_ERROR_LAST </i></dt>
<dd>Last marker &#8211; never used</dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_callout from the source code.</p>
