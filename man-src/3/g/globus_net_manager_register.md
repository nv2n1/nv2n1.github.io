---
title: "globus_net_manager_register(3)"
name: "globus_net_manager_register"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_register/"
description: "Net Manager –"
---

<h2 class="name">NAME</h2>
<p> Net Manager &#8211; </p>
<p> Net Manager API.</p>
<h3>Modules</h3>
<p> <code>Attributes</code><br />
 <i>Net Manager Attribute Management Functions. </i><br />
 <code>Context</code><br />
 <i>Net Manager Context Management Functions. </i><br />
 <code>Function Signatures</code><br />
 <i>Net Manager Function Signatures</i> </p>
<p> Function signatures for the Net Manager interface. <code>Net Manager Implementation Tutorial</code>. &quot;<br />
 <code>Python Module</code><br />
 <i>Net Manager Python Module. </i><br />
 <code>Globus XIO Net Manager Driver</code><br />
 <i>Net Manager XIO Driver. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_NET_MANAGER_MODULE</code><br />
 <i>Module descriptor. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_net_manager_register</code> (<code>globus_net_manager_t</code> *manager, globus_module_descriptor_t *module)<br />
 <i>Register a network manager. </i><br />
 globus_result_t <code>globus_net_manager_unregister</code> (<code>globus_net_manager_t</code> *manager)<br />
 <i>Unregister a network manager. </i></p>
<h2>Detailed Description</h2>
<p> Net Manager API. </p>
<p> This API defines the plug-in points for network manager functionality, as well as functions for registering a particular network manager implementation so that it can be invoked during network events. </p>
<p> To implement a network manager, define a struct <code>globus_net_manager_s</code> with the functions you want called, and register it by calling <code>globus_net_manager_register()</code>. More details are included in <code>Net Manager Implementation Tutorial</code></p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_NET_MANAGER_MODULE</h3>
<p> Module descriptor. The Globus Net Manager uses Globus Toolkit module activation and deactivation. Before any Net Manager functions can be called, the module must be activated, like this: </p>
<pre>
globus_module_activate(GLOBUS_NET_MANAGER_MODULE);
</pre>
<p> This function returns GLOBUS_SUCCESS if the library is successfully initialized. Otherwise, an error code is returned, and Net Manager functions should not be subsequently called. </p>
<p> Activations are reference counted, so it is safe to activate the module multiple times or in different modules. </p>
<p> To deactivate Net Manager, call </p>
<pre>
globus_module_deactivate(GLOBUS_NET_MANAGER_MODULE);
</pre>
<p> This function should be done once for each time the Net Manager was activated.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_net_manager_register (<code>globus_net_manager_t</code> *manager, globus_module_descriptor_t *module)</h3>
<p> Register a network manager. The <code>globus_net_manager_register()</code> function adds this network manager to those which will be called by the network manager interface when network events occur. This is typically called by the network manager when its module is activated. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Manager information to register.<br />
 <i>module</i> Module descriptor to register. Use GlobusExtensionMyModule(module name)</dl>
<h3>globus_result_t globus_net_manager_unregister (<code>globus_net_manager_t</code> *manager)</h3>
<p> Unregister a network manager. The <code>globus_net_manager_unregister()</code> function removes this network manager from those which will be called by the network manager interface when network events occur. This is typically called by the network manager when its module is deactivated. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>manager</i> Manager information to unregister.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
