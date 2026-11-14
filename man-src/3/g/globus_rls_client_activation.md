---
title: "globus_rls_client_activation(3)"
name: "globus_rls_client_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<p> This module must be activated before any functions in this API may be used.</p>
<h3>Defines</h3>
<p> #define <code>GLOBUS_RLS_CLIENT_MODULE</code> (&amp;<code>globus_rls_client_module</code>) </p>
<h3>Variables</h3>
<p> globus_module_descriptor_t <code>globus_rls_client_module</code> </p>
<h2>Detailed Description</h2>
<p> This module must be activated before any functions in this API may be used. </p>
<p> This module depends on other Globus modules GLOBUS_COMMON_MODULE and GLOBUS_IO_MODULE, which should be activated first: </p>
<pre><code>
globus_module_activate(GLOBUS_COMMON_MODULE);
globus_module_activate(GLOBUS_IO_MODULE);
globus_module_activate(GLOBUS_RLS_CLIENT_MODULE);
</code></pre>
<p>&nbsp;<wbr>When finished modules should be deactivated in reverse order.&nbsp;<wbr></p>
<h2>Define Documentation</h2>
<h3>#define GLOBUS_RLS_CLIENT_MODULE (&amp;<code>globus_rls_client_module</code>)</h3>
<p> RLS Module Name.</p>
<h2>Variable Documentation</h2>
<h3>globus_module_descriptor_t <code>globus_rls_client_module</code></h3>
<p> RLS module.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Variable Documentation</a></p>
<dd>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
