---

title: "globus_callout_register(3)"
name: "globus_callout_register"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout_register/"
description: "Callout Configuration –"
---

<p> Callout Configuration &#8211; </p>
<p> Register callouts.</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_callout_read_config</code> (<code>globus_callout_handle_t</code> handle, char *filename) </p>
<p> globus_result_t <code>globus_callout_register</code> (<code>globus_callout_handle_t</code> handle, char *type, char *library, char *symbol) </p>
<h2>Detailed Description</h2>
<p> Register callouts. </p>
<p> This section defines operations for registering callouts. Callouts may be registered either through a configuration file or through calls to globus_callout_register.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_callout_read_config (<code>globus_callout_handle_t</code>handle, char *filename)</h3>
<p> Read callout configuration from file. </p>
<p> This function read a configuration file with the following format:</p>
<dl>
<dt>&bull;</dt>
<dd> Anything after a <i>#</i> is assumed to be a comment</dd>
<dt>&bull;</dt>
<dd> Blanks lines are ignored</dd>
<dt>&bull;</dt>
<dd> Lines specifying callouts have the format</dd></dl>
<pre>
       abstract type           library         symbol
</pre>
<p>&nbsp;<wbr>where&nbsp;<wbr><i>abstract type</i>&nbsp;<wbr>denotes the type of callout, e.g. globus_gram_jobmanager_authz,&nbsp;<wbr><i>library</i>&nbsp;<wbr>denotes the library the callout can be found in and&nbsp;<wbr><i>symbol</i>&nbsp;<wbr>denotes the function name of the callout. The library argument can be specified in two forms, libfoo or libfoo_<i>flavor</i>. When using the former version the current flavor will automatically be added to the library name if needed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>handle</i> The handle that is to be configured<br />
 <i>filename</i> The file to read configuration from</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> This function returns GLOBUS_SUCCESS or a globus_result_t referring to an error object of one of the following types</dd></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
</dt><dd> <i>GLOBUS_CALLOUT_ERROR_OPENING_CONF_FILE</i> Error opening filename<br />
 <i>GLOBUS_CALLOUT_ERROR_PARSING_CONF_FILE</i> Error parsing file<br />
 <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory</dd></dl>
<h3>globus_result_t globus_callout_register (<code>globus_callout_handle_t</code>handle, char *type, char *library, char *symbol)</h3>
<p> Register callout configuration </p>
<p> This function registers a callout type in the given handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>handle</i> The handle that is to be configured<br />
 <i>type</i> The abstract type of the callout<br />
 <i>library</i> The location of the library containing the callout<br />
 <i>symbol</i> The symbol (ie function name) for the callout</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> This function returns GLOBUS_SUCCESS or a globus_result_t referring to an error object of one of the following types</dd></dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
</dt><dd> <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_callout from the source code. </p>
