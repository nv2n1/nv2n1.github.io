---
title: "tcl_updatelinkedvar(3)"
name: "tcl_updatelinkedvar"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_updatelinkedvar/"
description: "Tcl_LinkVar, Tcl_UnlinkVar, Tcl_UpdateLinkedVar – link Tcl variable to C variable"
---

<p>Tcl_LinkVar, Tcl_UnlinkVar, Tcl_UpdateLinkedVar &#8211; link Tcl variable to C variable </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_LinkVar</code>(<i>interp, varName, addr, type</i>)
<code>Tcl_UnlinkVar</code>(<i>interp, varName</i>)
<code>Tcl_UpdateLinkedVar</code>(<i>interp, varName</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter that contains <i>varName</i>. Also used by <code>Tcl_LinkVar</code> to return error messages.</p>
<dd>const char <i>*varName</i> (in) Name of global variable.</p>
<dd>char <i>*addr</i> (in) Address of C variable that is to be linked to <i>varName</i>.</p>
<dd>int <i>type</i> (in) Type of C variable. Must be one of <code>TCL_LINK_INT</code>, <code>TCL_LINK_UINT</code>, <code>TCL_LINK_CHAR</code>, <code>TCL_LINK_UCHAR</code>, <code>TCL_LINK_SHORT</code>, <code>TCL_LINK_USHORT</code>, <code>TCL_LINK_LONG</code>, <code>TCL_LINK_ULONG</code>, <code>TCL_LINK_WIDE_INT</code>, <code>TCL_LINK_WIDE_UINT</code>, <code>TCL_LINK_FLOAT</code>, <code>TCL_LINK_DOUBLE</code>, <code>TCL_LINK_BOOLEAN</code>, or <code>TCL_LINK_STRING</code>, optionally OR&#8217;ed with <code>TCL_LINK_READ_ONLY</code> to make Tcl variable read-only. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_LinkVar</code> uses variable traces to keep the Tcl variable named by <i>varName</i> in sync with the C variable at the address given by <i>addr</i>. Whenever the Tcl variable is read the value of the C variable will be returned, and whenever the Tcl variable is written the C variable will be updated to have the same value. <code>Tcl_LinkVar</code> normally returns <code>TCL_OK</code>; if an error occurs while setting up the link (e.g. because <i>varName</i> is the name of array) then <code>TCL_ERROR</code> is returned and the interpreter&#8217;s result contains an error message. </p>
<p> The <i>type</i> argument specifies the type of the C variable, and must have one of the following values, optionally OR&#8217;ed with <code>TCL_LINK_READ_ONLY</code>:</p>
<dl COMPACT>
<dt><code>TCL_LINK_INT</code></p>
<dd>The C variable is of type <code>int</code>. Any value written into the Tcl variable must have a proper integer form acceptable to <code>Tcl_GetIntFromObj</code>; attempts to write non-integer values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_UINT</code></p>
<dd>The C variable is of type <code>unsigned int</code>. Any value written into the Tcl variable must have a proper unsigned integer form acceptable to <code>Tcl_GetWideIntFromObj</code> and in the platform&#8217;s defined range for the <code>unsigned int</code> type; attempts to write non-integer values (or values outside the range) into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_CHAR</code></p>
<dd>The C variable is of type <code>char</code>. Any value written into the Tcl variable must have a proper integer form acceptable to <code>Tcl_GetIntFromObj</code> and be in the range of the <code>char</code> datatype; attempts to write non-integer or out-of-range values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_UCHAR</code></p>
<dd>The C variable is of type <code>unsigned char</code>. Any value written into the Tcl variable must have a proper unsigned integer form acceptable to <code>Tcl_GetIntFromObj</code> and in the platform&#8217;s defined range for the <code>unsigned char</code> type; attempts to write non-integer values (or values outside the range) into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_SHORT</code></p>
<dd>The C variable is of type <code>short</code>. Any value written into the Tcl variable must have a proper integer form acceptable to <code>Tcl_GetIntFromObj</code> and be in the range of the <code>short</code> datatype; attempts to write non-integer or out-of-range values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_USHORT</code></p>
<dd>The C variable is of type <code>unsigned short</code>. Any value written into the Tcl variable must have a proper unsigned integer form acceptable to <code>Tcl_GetIntFromObj</code> and in the platform&#8217;s defined range for the <code>unsigned short</code> type; attempts to write non-integer values (or values outside the range) into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_LONG</code></p>
<dd>The C variable is of type <code>long</code>. Any value written into the Tcl variable must have a proper integer form acceptable to <code>Tcl_GetLongFromObj</code>; attempts to write non-integer or out-of-range values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_ULONG</code></p>
<dd>The C variable is of type <code>unsigned long</code>. Any value written into the Tcl variable must have a proper unsigned integer form acceptable to <code>Tcl_GetWideIntFromObj</code> and in the platform&#8217;s defined range for the <code>unsigned long</code> type; attempts to write non-integer values (or values outside the range) into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_DOUBLE</code></p>
<dd>The C variable is of type <code>double</code>. Any value written into the Tcl variable must have a proper real form acceptable to <code>Tcl_GetDoubleFromObj</code>; attempts to write non-real values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_FLOAT</code></p>
<dd>The C variable is of type <code>float</code>. Any value written into the Tcl variable must have a proper real form acceptable to <code>Tcl_GetDoubleFromObj</code> and must be within the range acceptable for a <code>float</code>; attempts to write non-real values (or values outside the range) into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_WIDE_INT</code></p>
<dd>The C variable is of type <code>Tcl_WideInt</code> (which is an integer type at least 64-bits wide on all platforms that can support it.) Any value written into the Tcl variable must have a proper integer form acceptable to <code>Tcl_GetWideIntFromObj</code>; attempts to write non-integer values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_WIDE_UINT</code></p>
<dd>The C variable is of type <code>Tcl_WideUInt</code> (which is an unsigned integer type at least 64-bits wide on all platforms that can support it.) Any value written into the Tcl variable must have a proper unsigned integer form acceptable to <code>Tcl_GetWideIntFromObj</code> (it will be cast to unsigned); attempts to write non-integer values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_BOOLEAN</code></p>
<dd>The C variable is of type <code>int</code>. If its value is zero then it will read from Tcl as &#8220;0&#8221;; otherwise it will read from Tcl as &#8220;1&#8221;. Whenever <i>varName</i> is modified, the C variable will be set to a 0 or 1 value. Any value written into the Tcl variable must have a proper boolean form acceptable to <code>Tcl_GetBooleanFromObj</code>; attempts to write non-boolean values into <i>varName</i> will be rejected with Tcl errors.</p>
<dt><code>TCL_LINK_STRING</code></p>
<dd>The C variable is of type <code>char *</code>. If its value is not NULL then it must be a pointer to a string allocated with <code>Tcl_Alloc</code> or <code>ckalloc</code>. Whenever the Tcl variable is modified the current C string will be freed and new memory will be allocated to hold a copy of the variable&#8217;s new value. If the C variable contains a NULL pointer then the Tcl variable will read as &#8220;NULL&#8221;.</dl>
<p> If the <code>TCL_LINK_READ_ONLY</code> flag is present in <i>type</i> then the variable will be read-only from Tcl, so that its value can only be changed by modifying the C variable. Attempts to write the variable from Tcl will be rejected with errors. </p>
<p> <code>Tcl_UnlinkVar</code> removes the link previously set up for the variable given by <i>varName</i>. If there does not exist a link for <i>varName</i> then the procedure has no effect. </p>
<p> <code>Tcl_UpdateLinkedVar</code> may be invoked after the C variable has changed to force the Tcl variable to be updated immediately. In many cases this procedure is not needed, since any attempt to read the Tcl variable will return the latest value of the C variable. However, if a trace has been set on the Tcl variable (such as a Tk widget that wishes to display the value of the variable), the trace will not trigger when the C variable has changed. <code>Tcl_UpdateLinkedVar</code> ensures that any traces on the Tcl variable are invoked. </p>
<h2>Keywords</h2>
<p>boolean, integer, link, read-only, real, string, traces, variable</p>
