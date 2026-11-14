---
title: "globus_generic_error_api(3)"
name: "globus_generic_error_api"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_generic_error_api/"
description: "Globus Generic Error API –"
---

<h2 class="name">NAME</h2>
<p> Globus Generic Error API &#8211; </p>
<h3>Modules</h3>
<p> <code>Error Construction</code> </p>
<p> <code>Error Data Accessors and Modifiers</code> </p>
<p> <code>Error Handling Helpers</code> </p>
<h2>Detailed Description</h2>
<p> These globus_error functions are motivated by the desire to provide a easier way of generating new error types, while at the same time preserving all features (e.g. memory management, chaining) of the current error handling framework. It does this by defining a generic error type for globus which in turn contains a integer in it&#8217;s instance data which is used for carrying the actual error type information. </p>
<p> Any program that uses Globus Generic Error functions must include &#8216;globus_common.h&#8217;.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
