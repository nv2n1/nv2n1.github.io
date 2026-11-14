---
title: "tcl_getindexfromobjstruct(3)"
name: "tcl_getindexfromobjstruct"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getindexfromobjstruct/"
description: "Tcl_GetIndexFromObj, Tcl_GetIndexFromObjStruct – lookup string in table of keywords"
---

<p>Tcl_GetIndexFromObj, Tcl_GetIndexFromObjStruct &#8211; lookup string in table of keywords </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_GetIndexFromObj</code>(<i>interp, objPtr, tablePtr, msg, flags,
indexPtr</i>)
int
<code>Tcl_GetIndexFromObjStruct</code>(<i>interp, objPtr, structTablePtr, offset,
 msg, flags, indexPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting; if NULL, then no message is provided on errors.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) The string value of this object is used to search through <i>tablePtr</i>. The internal representation is modified to hold the index of the matching table entry.</p>
<dd>const char <i>**tablePtr</i> (in) An array of null-terminated strings. The end of the array is marked by a NULL string pointer. Note that references to the <i>tablePtr</i> may be retained in the internal representation of <i>objPtr</i>, so this should represent the address of a statically-allocated array.</p>
<dd>const void <i>*structTablePtr</i> (in) An array of arbitrary type, typically some <code>struct</code> type. The first member of the structure must be a null-terminated string. The size of the structure is given by <i>offset</i>. Note that references to the <i>structTablePtr</i> may be retained in the internal representation of <i>objPtr</i>, so this should represent the address of a statically-allocated array of structures.</p>
<dd>int <i>offset</i> (in) The offset to add to structTablePtr to get to the next entry. The end of the array is marked by a NULL string pointer.</p>
<dd>const char <i>*msg</i> (in) Null-terminated string describing what is being looked up, such as <code>option</code>. This string is included in error messages.</p>
<dd>int <i>flags</i> (in) OR-ed combination of bits providing additional information for operation. The only bit that is currently defined is <code>TCL_EXACT</code>.</p>
<dd>int <i>*indexPtr</i> (out) The index of the string in <i>tablePtr</i> that matches the value of <i>objPtr</i> is returned here. </p>
</dl>
<h2>Description</h2>
<p>These procedures provide an efficient way for looking up keywords, switch names, option names, and similar things where the value of an object must be one of a predefined set of values. <code>Tcl_GetIndexFromObj</code> compares <i>objPtr</i> against each of the strings in <i>tablePtr</i> to find a match. A match occurs if <i>objPtr</i>&#8216;s string value is identical to one of the strings in <i>tablePtr</i>, or if it is a non-empty unique abbreviation for exactly one of the strings in <i>tablePtr</i> and the <code>TCL_EXACT</code> flag was not specified; in either case the index of the matching entry is stored at <i>*indexPtr</i> and <code>TCL_OK</code> is returned. </p>
<p> If there is no matching entry, <code>TCL_ERROR</code> is returned and an error message is left in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <i>Msg</i> is included in the error message to indicate what was being looked up. For example, if <i>msg</i> is <code>option</code> the error message will have a form like &#8220;<code>bad option &#34;firt&#34;: must be first, second, or third</code>&#8221;. </p>
<p> If <code>Tcl_GetIndexFromObj</code> completes successfully it modifies the internal representation of <i>objPtr</i> to hold the address of the table and the index of the matching entry. If <code>Tcl_GetIndexFromObj</code> is invoked again with the same <i>objPtr</i> and <i>tablePtr</i> arguments (e.g. during a reinvocation of a Tcl command), it returns the matching index immediately without having to redo the lookup operation. Note: <code>Tcl_GetIndexFromObj</code> assumes that the entries in <i>tablePtr</i> are static: they must not change between invocations. If the value of <i>objPtr</i> is the empty string, <code>Tcl_GetIndexFromObj</code> will treat it as a non-matching value and return <code>TCL_ERROR</code>. </p>
<p> <code>Tcl_GetIndexFromObjStruct</code> works just like <code>Tcl_GetIndexFromObj</code>, except that instead of treating <i>tablePtr</i> as an array of string pointers, it treats it as a pointer to the first string in a series of strings that have <i>offset</i> bytes between them (i.e. that there is a pointer to the first array of characters at <i>tablePtr</i>, a pointer to the second array of characters at <i>tablePtr</i>+<i>offset</i> bytes, etc.) This is particularly useful when processing things like <code>Tk_ConfigurationSpec</code>, whose string keys are in the same place in each of several array elements. </p>
<h2>See Also</h2>
<p>Tcl_WrongNumArgs </p>
<h2>Keywords</h2>
<p>index, object, table lookup</p>
