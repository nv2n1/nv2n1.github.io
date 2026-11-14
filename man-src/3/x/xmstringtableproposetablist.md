---
title: "xmstringtableproposetablist(3)"
name: "xmstringtableproposetablist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringtableproposetablist/"
description: "XmStringTableProposeTablist — A convenience function that returns a tab list"
---

<p><code>XmStringTableProposeTablist</code> &#8212; A convenience function that returns a tab list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTabList XmStringTableProposeTablist</code>(
<code>XmStringTable strings</code>,
<code>Cardinal num_strings</code>,
<code>Widget widget</code>,
<code>float pad_value</code>,
<code>XmOffsetModel offset_model</code>);</pre>
<h2>Description</h2>
<p><code>XmStringTableProposeTablist</code> takes an <code>XmStringTable</code> structure containing tabbed compound strings, information on padding between columns, and rendering information and returns a tab list that, if used to render the strings in the table, would cause the strings to line up in columns with no overlap and with the specified amount of padding between the widest item in each column and the start of the next column. Each tab in the tablist would have the same unit type as <i>units</i>, an offset model of <i>offset_model</i>, and an alignment type of <code>XmALIGNMENT_BEGINNING</code>.</p>
<dl COMPACT>
<dt><i>strings</i></p>
<dd>Specifies an array of compound strings.</p>
<dt><i>num_strings</i></p>
<dd>Specifies the number of compound strings in <i>strings</i>.</p>
<dt><i>widget</i></p>
<dd>Specifies the widget used for deriving any necessary information for creating the rendition. In particular, the <code>XmNunitType</code> of <i>widget</i> will be used to specify the unit type to be used in determining the amount of padding separating columns and for the tabs in the proposed tab list. Also, <i>widget</i>&#8216;s render table will be used in interpreting rendition tags within the strings.</p>
<dt><i>pad_value</i></p>
<dd>Specifies the value of the amount of padding to be used to separate columns. The units for this parameter are specified as the <code>XmNunitType</code> set for the <i>widget</i> parameter. Refer to the <code>XmNunitType</code> resource of the <code>XmGadget</code>, <code>XmManager</code>, or <code>XmPrimitive</code> reference page.</p>
<dt><i>offset_model</i></p>
<dd>Specifies the offset model to be used in creating the tabs. Can be <code>XmABSOLUTE</code> or <code>XmRELATIVE</code>.</dl>
<h2>Return</h2>
<p>Returns a new <code>XmTabList</code>. The function allocates space to hold the returned tab list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmTabListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3) and <code><a href="/docs/linux/man/3-xmtablistfree/">XmTabListFree</a></code>(3).</p>
