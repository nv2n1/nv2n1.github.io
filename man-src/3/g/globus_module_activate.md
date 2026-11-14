---
title: "globus_module_activate(3)"
name: "globus_module_activate"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_module_activate/"
description: "Module Activation Management –"
---

<h2 class="name">NAME</h2>
<p> Module Activation Management &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_module_descriptor_s</code><br />
 <i>Module Descriptor. </i></p>
<h3>Functions</h3>
<p> int <code>globus_module_activate</code> (<code>globus_module_descriptor_t</code> *module_descriptor)<br />
 <i>Activate a module. </i><br />
 int <code>globus_module_activate_array</code> (<code>globus_module_descriptor_t</code> *module_array[], <code>globus_module_descriptor_t</code> **failed_module)<br />
 <i>Activate a group of modules. </i><br />
 int <code>globus_module_deactivate</code> (<code>globus_module_descriptor_t</code> *module_descriptor)<br />
 <i>Deactivate a module. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int globus_module_activate (<code>globus_module_descriptor_t</code> *module_descriptor)</h3>
<p> Activate a module. Add a reference to the module named by module_descriptor to the list of activated modules. If this is the first reference to this module, its activation function will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>module_descriptor</i> Module to activate</dl>
<h3>int globus_module_activate_array (<code>globus_module_descriptor_t</code> *module_array[], <code>globus_module_descriptor_t</code> **failed_module)</h3>
<p> Activate a group of modules. Activate an NULL-terminated array of modules. If any fail to activate, all are deactivated and the error from the failed activation is returned. If nonzero is returned, and failed_module is non-NULL, it will be set to point to the 1st module which failed to activate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>module_array</i> NULL-terminated array of module descriptors to activate.<br />
 <i>failed_module</i> Pointer to set to the first module whose activation function failed.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
