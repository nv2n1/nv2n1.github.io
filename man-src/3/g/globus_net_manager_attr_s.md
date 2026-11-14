---
title: "globus_net_manager_attr_s(3)"
name: "globus_net_manager_attr_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_attr_s/"
description: "globus_net_manager_attr_s –"
---

<h2 class="name">NAME</h2>
<p> globus_net_manager_attr_s &#8211; </p>
<p> Net Manager Attributes.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_net_manager_attr.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>scope</code> </p>
<p> char * <code>name</code> </p>
<p> char * <code>value</code> </p>
<h2>Detailed Description</h2>
<p> Net Manager Attributes. </p>
<p> The globus_net_manager_attr_t structure defines a scoped (attribute, value) tuple. The scope in most cases is either the name of the transport driver or the &#8216;globus_net_manager&#8217; scope, for attributes specific to the network manager implementation.</p>
<h2>Field Documentation</h2>
<h3>char* globus_net_manager_attr_s::name</h3>
<p> Name of the attribute</p>
<h3>char* globus_net_manager_attr_s::scope</h3>
<p> Scope of the attribute</p>
<h3>char* globus_net_manager_attr_s::value</h3>
<p> Value of the attribute </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_net_manager from the source code. </p>
<h2>Index</h2>
