---
title: "globus_error_api(3)"
name: "globus_error_api"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_api/"
description: "Globus Error API –"
---

<h2 class="name">NAME</h2>
<p> Globus Error API &#8211; </p>
<h3>Modules</h3>
<p> <code>Globus Errno Error API</code> </p>
<p> <code>Globus Generic Error API</code> </p>
<h2>Detailed Description</h2>
<p> Intended use: </p>
<p> If a function needs to return an error it should do the following: </p>
<dl>
<dt>&bull;</p>
<dd> External errors, such as error returns from system calls and GSSAPI errors, should be wrapped using the appropriate error type.</p>
<dt>&bull;</p>
<dd> The wrapped external error should then be passed as the cause of a globus error.</p>
<dt>&bull;</p>
<dd> External error types are expected to provide a utility function to combine the above two steps.</p>
<dt>&bull;</p>
<dd> The globus error should then be returned from the function.</dl>
<p> Notes on how to generate globus errors: </p>
<dl>
<dt>&bull;</p>
<dd> Module specific error types should be greater or equal to 1024 (to leave some space for global error types).</p>
<dt>&bull;</p>
<dd> You may wish to generate a mapping from error types to format strings for use in short descriptions.</p>
<dt>&bull;</p>
<dd> You may also wish to generate a common prefix for all of the above fromat strings. The suggested prefix is &#8216;Function: %s Line:<br />
&nbsp;<wbr>&nbsp;<wbr>%s&nbsp;<wbr>&#8216;.&nbsp;<wbr></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
