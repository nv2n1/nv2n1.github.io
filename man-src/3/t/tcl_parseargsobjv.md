---
title: "tcl_parseargsobjv(3)"
name: "tcl_parseargsobjv"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_parseargsobjv/"
description: "Tcl_ParseArgsObjv – parse arguments according to a tabular description"
---

<p>Tcl_ParseArgsObjv &#8211; parse arguments according to a tabular description </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_ParseArgsObjv</code>(<i>interp, argTable, objcPtr, objv, remObjv</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (out) Where to store error messages.</p>
<dd>const Tcl_ArgvInfo <i>*argTable</i> (in) Pointer to array of option descriptors.</p>
<dd>int <i>*objcPtr</i> (in/out) A pointer to variable holding number of arguments in <i>objv</i>. Will be modified to hold number of arguments left in the unprocessed argument list stored in <i>remObjv</i>.</p>
<dd>Tcl_Obj *const <i>*objv</i> (in) The array of arguments to be parsed.</p>
<dd>Tcl_Obj <i>***remObjv</i> (out) Pointer to a variable that will hold the array of unprocessed arguments. Should be NULL if no return of unprocessed arguments is required. If <i>objcPtr</i> is updated to a non-zero value, the array returned through this must be deallocated using <code>ckfree</code>.
</dl>
<h2>Description</h2>
<p>The <code>Tcl_ParseArgsObjv</code> function provides a system for parsing argument lists of the form &#8220;<code>-someName </code><i>someValue</i> &#8230;&#8221;. Such argument lists are commonly found both in the arguments to a program and in the arguments to an individual Tcl command. This parser assumes that the order of the arguments does not matter, other than in so far as later copies of a duplicated option overriding earlier ones. </p>
<p> The argument array is described by the <i>objcPtr</i> and <i>objv</i> parameters, and an array of unprocessed arguments is returned through the <i>objcPtr</i> and <i>remObjv</i> parameters; if no return of unprocessed arguments is desired, the <i>remObjv</i> parameter should be NULL. If any problems happen, including if the &#8220;generate help&#8221; option is selected, an error message is left in the interpreter result and TCL_ERROR is returned. Otherwise, the interpreter result is left unchanged and TCL_OK is returned. </p>
<p> The collection of arguments to be parsed is described by the <i>argTable</i> parameter. This points to a table of descriptor structures that is terminated by an entry with the <i>type</i> field set to TCL_ARGV_END. As convenience, the following prototypical entries are provided:</p>
<dl COMPACT>
<dt><code>TCL_ARGV_AUTO_HELP</code></p>
<dd>Enables the argument processor to provide help when passed the argument &#8220;<code>-help</code>&#8221;.</p>
<dt><code>TCL_ARGV_AUTO_REST</code></p>
<dd>Instructs the argument processor that arguments after &#8220;<code>&#8212;</code>&#8221; are to be unprocessed.</p>
<dt><code>TCL_ARGV_TABLE_END</code></p>
<dd>Marks the end of the table of argument descriptors.</dl>
<h3>Argument Descriptor Entries</h3>
<p>Each entry of the argument descriptor table must be a structure of type <code>Tcl_ArgvInfo</code>. The structure is defined as this: </p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 int <i>type</i>;
 const char *<i>keyStr</i>;
 void *<i>srcPtr</i>;
 void *<i>dstPtr</i>;
 const char *<i>helpStr</i>;
 ClientData <i>clientData</i>;
} <code>Tcl_ArgvInfo</code>;</pre>
</dl>
<p> The <i>keyStr</i> field contains the name of the option; by convention, this will normally begin with a &#8220;<code>&#8211;</code>&#8221; character. The <i>type</i>, <i>srcPtr</i>, <i>dstPtr</i> and <i>clientData</i> fields describe the interpretation of the value of the argument, as described below. The <i>helpStr</i> field gives some text that is used to provide help to users when they request it. </p>
<p> As noted above, the <i>type</i> field is used to describe the interpretation of the argument&#8217;s value. The following values are acceptable values for <i>type</i>:</p>
<dl COMPACT>
<dt><code>TCL_ARGV_CONSTANT</code></p>
<dd>The argument does not take any following value argument. If this argument is present, the int pointed to by the <i>srcPtr</i> field is copied to the <i>dstPtr</i> field. The <i>clientData</i> field is ignored.</p>
<dt><code>TCL_ARGV_END</code></p>
<dd>This value marks the end of all option descriptors in the table. All other fields are ignored.</p>
<dt><code>TCL_ARGV_FLOAT</code></p>
<dd>This argument takes a following floating point value argument. The value (once parsed by <code>Tcl_GetDoubleFromObj</code>) will be stored as a double-precision value in the variable pointed to by the <i>dstPtr</i> field. The <i>srcPtr</i> and <i>clientData</i> fields are ignored.</p>
<dt><code>TCL_ARGV_FUNC</code></p>
<dd>This argument optionally takes a following value argument; it is up to the handler callback function passed in <i>srcPtr</i> to decide. That function will have the following signature:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>
<pre>typedef int (<code>Tcl_ArgvFuncProc</code>)(
 ClientData <i>clientData</i>,
 Tcl_Obj *<i>objPtr</i>,
 void *<i>dstPtr</i>);</pre>
</dl>
<p> The result is a boolean value indicating whether to consume the following argument. The <i>clientData</i> is the value from the table entry, the <i>objPtr</i> is the value that represents the following argument or NULL if there are no following arguments at all, and the <i>dstPtr</i> argument to the <code>Tcl_ArgvFuncProc</code> is the location to write the parsed value to.</dl>
<dt><code>TCL_ARGV_GENFUNC</code></p>
<dd>This argument takes zero or more following arguments; the handler callback function passed in <i>srcPtr</i> returns how many (or a negative number to signal an error, in which case it should also set the interpreter result). The function will have the following signature:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>
<pre>typedef int (<code>Tcl_ArgvGenFuncProc</code>)(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>objc</i>,
 Tcl_Obj *const *<i>objv</i>,
 void *<i>dstPtr</i>);</pre>
</dl>
<p> The <i>clientData</i> is the value from the table entry, the <i>interp</i> is where to store any error messages, the <i>keyStr</i> is the name of the argument, <i>objc</i> and <i>objv</i> describe an array of all the remaining arguments, and <i>dstPtr</i> argument to the <code>Tcl_ArgvGenFuncProc</code> is the location to write the parsed value (or values) to.</dl>
<dt><code>TCL_ARGV_HELP</code></p>
<dd>This special argument does not take any following value argument, but instead causes <code>Tcl_ParseArgsObjv</code> to generate an error message describing the arguments supported. All other fields except the <i>helpStr</i> field are ignored.</p>
<dt><code>TCL_ARGV_INT</code></p>
<dd>This argument takes a following integer value argument. The value (once parsed by <code>Tcl_GetIntFromObj</code>) will be stored as an int in the variable pointed to by the <i>dstPtr</i> field. The <i>srcPtr</i> field is ignored.</p>
<dt><code>TCL_ARGV_REST</code></p>
<dd>This special argument does not take any following value argument, but instead marks all following arguments to be left unprocessed. The <i>srcPtr</i>, <i>dstPtr</i> and <i>clientData</i> fields are ignored.</p>
<dt><code>TCL_ARGV_STRING</code></p>
<dd>This argument takes a following string value argument. A pointer to the string will be stored at <i>dstPtr</i>; the string inside will have a lifetime linked to the lifetime of the string representation of the argument value that it came from, and so should be copied if it needs to be retained. The <i>srcPtr</i> and <i>clientData</i> fields are ignored.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_getindexfromobj/">Tcl_GetIndexFromObj</a>(3), <a href="/docs/linux/man/3-tcl_main/">Tcl_Main</a>(3), <a href="/docs/linux/man/3-tcl_createobjcommand/">Tcl_CreateObjCommand</a>(3)</p>
<h2>Keywords</h2>
<p>argument, parse</p>
