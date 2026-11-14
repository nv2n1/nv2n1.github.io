---
title: "globus_callout(3)"
name: "globus_callout"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout/"
description: "Globus Callout API –"
---

<h2 class="name">NAME</h2>
<p> Globus Callout API &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code><br />
 <i>Callback API Activation. </i><br />
 <code>Callout Handle Operations</code><br />
 <i>Manage a Globus Callout Handle structure. </i><br />
 <code>Callout Configuration</code><br />
 <i>Register callouts. </i><br />
 <code>Callout Invocation</code><br />
 <i>Invoke callouts. </i><br />
 <code>Callout Constants</code><br />
 <i>Constants. </i></p>
<h2>Detailed Description</h2>
<p> This API is intended to ease integration of configurable callouts into the Globus Toolkit and to provide a platform independent way of dealing with runtime loadable functions. It (hopefully) achieves this goal by providing the following functionality: </p>
<dl>
<dt>&bull;</p>
<dd> It provides a function for reading callout configuration files. Files are assumed to have the following format:</p>
<dt> &bull;</p>
<dd> Anything after a # is assumed to be a comment</p>
<dt> &bull;</p>
<dd> Blanks lines are ignored</p>
<dt> &bull;</p>
<dd> Lines specifying callouts have the format</dl>
<pre>
      abstract type           library         symbol
</pre>
<p>&nbsp;<wbr>where&nbsp;<wbr><i>abstract type</i>&nbsp;<wbr>denotes the type of callout, e.g. globus_gram_jobmanager_authz,&nbsp;<wbr><i>library</i>&nbsp;<wbr>denotes the library the callout can be found in and&nbsp;<wbr><i>symbol</i>&nbsp;<wbr>denotes the function name of the callout. </p>
<dl>
<dt>&bull;</p>
<dd> It provides a API function for registering callouts</p>
<dt>&bull;</p>
<dd> All callouts are assumed to have the function signature globus_result_t callout_func(va_list ap)</p>
<dt>&bull;</p>
<dd> It provides a function for calling a callout given an abstract type. If multiple callouts are defined for the same abstract type then all callouts for the abstract type will be called. Implementers should not rely on any correlation between the order of configuration and the order of invocation of callouts of the same abstract type.</dl>
<p> Any program that uses Globus Callout functions must include the <code>globus_callout.h</code> header </p>
<p> Function Categories</p>
<dl>
<dt>&bull;</p>
<dd> <code>Activation</code></p>
<dt>&bull;</p>
<dd> <code>Callout Handle Operations</code></p>
<dt>&bull;</p>
<dd> <code>Callout Configuration</code></p>
<dt>&bull;</p>
<dd> <code>Callout Invocation</code></p>
<dt>&bull;</p>
<dd> <code>Callout Constants</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_callout from the source code. </p>
<h2>Index</h2>
