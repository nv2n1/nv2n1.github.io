---
title: "xmstringtableunparse(3)"
name: "xmstringtableunparse"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringtableunparse/"
description: "XmStringTableUnparse — A convenience function that converts a table of compound strings to an array of text"
---

<p><code>XmStringTableUnparse</code> &#8212; A convenience function that converts a table of compound strings to an array of text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XtPointer * XmStringTableUnparse</code>(
<code>XmStringTable table</code>,
<code>Cardinal count</code>,
<code>XmStringTag tag</code>,
<code>XmTextType tag_type</code>,
<code>XmTextType output_type</code>,
<code>XmParseTable parse</code>,
<code>Cardinal parse_count</code>,
<code>XmParseModel parse_model</code>);</pre>
<h2>Description</h2>
<p><code>XmStringTableUnparse</code> takes an array of compound strings, allocates a string array for the type of characters determined by <i>type</i> with an equal number of slots, calls <code>XmStringUnparse</code> on each compound string in <i>table</i>, and inserts the resulting string in the corresponding slot in the array.</p>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies an <code>XmStringTable</code> containing the compound string to be converted.</p>
<dt><i>count</i></p>
<dd>Specifies the number of compound strings in <i>table</i>.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to be used in matching with text segments. The two types of tag types are <code>XmFONTLIST_DEFAULT_TAG</code> and <code>_MOTIF_DEFAULT_LOCALE</code>. Only segments tagged with <i>tag</i> will be returned. If <i>tag</i> is NULL, all segments will be matched.</p>
<dt><i>tag_type</i></p>
<dd>Specifies the type of tag to be searched for. These types include <code>XmMULTIBYTE_TEXT</code>, <code>XmWIDECHAR_TEXT</code>, and <code>XmCHARSET_TEXT</code>.</p>
<dt><i>output_type</i></p>
<dd>Specifies the type of text to be generated. These types include <code>XmMULTIBYTE_TEXT</code>, <code>XmWIDECHAR_TEXT</code>, and <code>XmCHARSET_TEXT</code>.</p>
<dt><i>parse</i></p>
<dd>Specifies the parse table to be used.</p>
<dt><i>parse_count</i></p>
<dd>Specifies the number of items in <i>parse</i>.</p>
<dt><i>parse_model</i></p>
<dd>Specifies which non-text components to be considered in matching in <i>parse_table</i>. Possible values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOUTPUT_ALL</code></p>
<dd>Puts out all matching components.</p>
<dt><code>XmOUTPUT_BETWEEN</code></p>
<dd>Puts out only those matching components that are between two matching text components.</p>
<dt><code>XmOUTPUT_BEGINNING</code></p>
<dd>Puts out only those matching components that are at the beginning of a matching text component.</p>
<dt><code>XmOUTPUT_END</code></p>
<dd>Puts out only those matching components that are at the end of a matching text component.</p>
<dt><code>XmOUTPUT_BOTH</code></p>
<dd>Puts out only those matching components that are at the beginning or end of a matching text component.</dl>
</dl>
</dl>
<h2>Return</h2>
<p>Returns an allocated array of allocated strings. The application is responsible for managing the allocated space. The application can recover the allocated strings space by calling <code>XtFree</code> <i>count</i> times (that is, one time for each allocated string). The application can then recover the allocated array by calling <code>XtFree</code> on the allocated array itself.</p>
<h2>Related</h2>
<p><code>XmStringTab.</code></p>
