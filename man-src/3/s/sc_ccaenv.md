---
title: "sc_ccaenv(3)"
name: "sc_ccaenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ccaenv/"
description: "sc::CCAEnv –"
---

<p>sc::CCAEnv &#8211; </p>
<p> The <code>CCAEnv</code> class handles embedded CCA frameworks.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;ccaenv.h&gt;

Static Public Member Functions
static void init (std::string &amp;args)


Initialize the framework.


static int initialized ()


Return nonzero if CCAEnv has been initialized.


static ccaffeine::AbstractFramework * get_framework ()


Returns pointer to framework.


static gov::cca::Services * get_services ()


Returns pointer to Services object.


static gov::cca::ports::BuilderService * get_builder_service ()


Returns pointer to BuilderService object.


static gov::cca::TypeMap * get_type_map ()


Returns pointer to type map.


static gov::cca::ComponentID * get_component_id ()


Returns pointer to 'uber' component's ComponentID.</code></pre>
<h2>Detailed Description</h2>
<p>The <code>CCAEnv</code> class handles embedded CCA frameworks.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
