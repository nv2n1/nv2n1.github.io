---
title: "xmparsemapping(3)"
name: "xmparsemapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsemapping/"
description: "XmParseMapping — Data type for a compound string parse mapping"
---

<p><code>XmParseMapping</code> &#8212; Data type for a compound string parse mapping</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmParseMapping</code> is an opaque data type for a parse mapping used by <code>XmStringParseText</code> to create a compound string. A parse mapping contains a pattern to be matched in text being parsed to create a compound string. It also contains a compound string, or a function to be invoked to provide a compound string, to be included in the compound string being created whenever the pattern is matched. </p>
<p> An application uses a resource-style interface to specify components for an <code>XmParseMapping</code>. <code>XmParseMappingCreate</code> creates a parse mapping, using a resource-style argument list. <code>XmParseMappingGetValues</code> and <code>XmParseMappingSetValues</code> retrieve and set the components of a parse mapping. <code>XmParseMappingFree</code> recovers memory used by a parse mapping. <code>XmParseTable</code> is an array of <code>XmParseMapping</code> objects. </p>
<p> The <code>XmNinvokeParseProc</code> resource is a function of type <code>XmParseProc</code>, which is defined as follows: </p>
<pre>XmIncludeStatus (*XmParseProc) (<i>text_in_out, text_end, type, tag, entry, pattern_length,
str_include, call_data</i>)
 XtPointer *<i>text_in_out</i>;
 XtPointer <i>text_end</i>;
 XmTextType <i>type</i>;
 XmStringTag <i>tag</i>;
 XmParseMapping <i>entry</i>;
 int <i>pattern_length</i>;
 XmString *<i>str_include</i>;
 XtPointer <i>call_data</i>;</pre>
<p>A parse procedure provides an escape mechanism for arbitrarily complex parsing. This procedure is invoked when a pattern in the input text is matched with a pattern in a parse mapping whose <code>XmNincludeStatus</code> is <code>XmINVOKE</code>. </p>
<p> The input text is a pointer to the first byte of the pattern that was matched to trigger the call to the parse procedure. The parse procedure consumes as many bytes of the input string as it needs and sets the input text pointer to the following byte. It returns a compound string to be included in the compound string being constructed, and it also returns an <code>XmIncludeStatus</code> indicating how the returned compound string should be handled. If the parse procedure does not set the input text pointer ahead by at least one byte, the parsing routine continues trying to match the input text with the patterns in the remaining parse mappings in the parse table. Otherwise, the parsing routine begins with the new input text pointer and tries to match the input text with patterns in the parse mappings starting at the beginning of the parse table.</p>
<dl COMPACT>
<dt><i>text_in_out</i></p>
<dd>Specifies the text being parsed. The value is a pointer to the first byte of text matching the pattern that triggered the call to the parse procedure. When the parse procedure returns, this argument is set to the position in the text where parsing should resume&#8212;that is, to the byte following the last character parsed by the parse procedure.</p>
<dt><i>text_end</i></p>
<dd>Specifies a pointer to the end of the <i>text_in_out</i> string. If <i>text_end</i> is NULL, the string is scanned until a NULL character is found. Otherwise, the string is scanned up to but not including the character whose address is <i>text_end</i>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of text and the tag type. If a locale tag should be created, <i>type</i> has a value of either <code>XmMULTIBYTE_TEXT</code> or <code>XmWIDECHAR_TEXT</code>. If a charset should be created, <i>type</i> has a value of <code>XmCHARSET_TEXT</code>.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in creating the result. The type of string tag created (charset or locale) depends on the text type and the passed in <i>tag</i> value. If the <i>tag</i> value is NULL and if <i>type</i> indicates that a charset string tag should be created, the string tag has the value that is the result of mapping <code>XmSTRING_DEFAULT_CHARSET</code>. If <i>type</i> indicates a locale string tag, the string tag has the value <code>_MOTIF_DEFAULT_LOCALE</code>.</p>
<dt><i>entry</i></p>
<dd>Specifies the parse mapping that triggered the call to the parse procedure.</p>
<dt><i>pattern_length</i></p>
<dd>Specifies the number of bytes in the input text, following <i>text_in_out</i>, that constitute the matched pattern.</p>
<dt><i>str_include</i></p>
<dd>Specifies a pointer to a compound string. The parse procedure creates a compound string to be included in the compound string being constructed. The parse procedure then returns the compound string in this argument.</p>
<dt><i>call_data</i></p>
<dd>Specifies data passed by the application to the parsing routine.</dl>
<p> The parse procedure returns an <code>XmIncludeStatus</code> indicating how <i>str_include</i> is to be included in the compound string being constructed. Following are the possible values:</p>
<dl COMPACT>
<dt><code>XmINSERT</code></p>
<dd>Concatenate the result to the compound string being constructed and continue parsing.</p>
<dt><code>XmTERMINATE</code></p>
<dd>Concatenate the result to the compound string being constructed and terminate parsing.</dl>
<h3>New Resources</h3>
<p>The following table defines a set of resources used by the programmer to specify data. The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XmParseMappingSetValues</code> (S), retrieved by using <code>XmParseMappingGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmParseMapping Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNclientData</td>
<td></td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNincludeStatus</td>
<td></td>
<td>XmIncludeStatus</td>
<td>XmINSERT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinvokeParseProc</td>
<td></td>
<td>XmParseProc</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpattern</td>
<td></td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpatternType</td>
<td></td>
<td>XmTextType</td>
<td>XmCHARSET_TEXT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsubstitute</td>
<td></td>
<td>XmString</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNclientData</code></p>
<dd>Specifies data to be used by the parse procedure.</p>
<dt><code>XmNincludeStatus</code></p>
<dd>Specifies how the result of the mapping is to be included in the compound string being constructed. Unless the value is <code>XmINVOKE</code>, the result of the mapping is the value of <code>XmNsubstitute</code>. Following are the possible values for <code>XmNincludeStatus</code>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmINSERT</code></p>
<dd>Concatenate the result to the compound string being constructed and continue parsing.</p>
<dt><code>XmINVOKE</code></p>
<dd>Invoke the <code>XmNinvokeParseProc</code> on the text being parsed and use the returned compound string instead of <code>XmNsubstitute</code> as the result to be inserted into the compound string being constructed. The include status returned by the parse procedure (<code>XmINSERT</code> or <code>XmTERMINATE</code>) determines how the returned compound string is included.</p>
<dt><code>XmTERMINATE</code></p>
<dd>Concatenate the result to the compound string being constructed and terminate parsing.</dl>
</dl>
<dt><code>XmNinvokeParseProc</code></p>
<dd>Specifies the parse procedure to be invoked when <code>XmNincludeStatus</code> is <code>XmINVOKE</code>.</p>
<dt><code>XmNpattern</code></p>
<dd>Specifies a pattern to be matched in the text being parsed. This is a maximum of one character.</p>
<dt><code>XmNpatternType</code></p>
<dd>Specifies the type of the pattern that is the value of <code>XmNpattern</code>. Following are the possible values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmCHARSET_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmMULTIBYTE_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmWIDECHAR_TEXT</code></dl>
</dl>
<dt><code>XmNsubstitute</code></p>
<dd>Specifies the compound string to be included in the compound string being constructed when <code>XmNincludeStatus</code> is <code>XmINSERT</code> or <code>XmTERMINATE</code>.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsemappingcreate/">XmParseMappingCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingfree/">XmParseMappingFree</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappinggetvalues/">XmParseMappingGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsemappingsetvalues/">XmParseMappingSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
