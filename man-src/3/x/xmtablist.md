---
title: "xmtablist(3)"
name: "xmtablist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablist/"
description: "XmTabList — Data type for a tab list"
---

<p><code>XmTabList</code> &#8212; Data type for a tab list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
XmTabList</pre>
<h2>Description</h2>
<p><code>XmTabList</code> is the data type for a tab list. A tab list consists of tab stop list entries (<code>XmTab</code>s). Whenever a tab component is encountered while an <code>XmString</code> is being rendered, the origin of the next X draw depends on the next <code>XmTab</code>. If a tab stop would cause text to overlap, the x position for the segment is reset to follow immediately after the end of the previous segment. </p>
<p> Tab lists are specified in resource files with the following syntax: </p>
<pre><i>resource_spec</i><code>:</code> <i>tab</i> WHITESPACE [, WHITESPACE <i>tab</i> ]*</pre>
<p>The resource value string consists of one or more tabs separated by commas. Each <i>tab</i> identifies the value of the tab, the unit type, and whether the offset is relative or absolute. For example: </p>
<pre><i>tab</i> := <i>float</i> [ WHITESPACE <i>units</i> ]
<i>float</i> := [ <i>sign</i> ] [[ DIGIT]*. ]DIGIT+
<i>sign</i> := +</pre>
<p>where the presence or absence of <i>sign</i> indicates, respectively, a relative offset or an absolute offset. Note that negative tab values are not allowed. <i>units</i> indicates the unitType to use as described in the <code>XmConvertUnits</code> reference page. </p>
<p> For example, the following specifies a tab list consisting of a one inch absolute tab followed by a one inch relative tab: </p>
<pre><tt>*tabList: 1in, +1in</tt></pre>
<p>For resources of type, dimension, or position, you can specify units as described in the <code>XmNunitType</code> resource of the <code>XmGadget</code>, <code>XmManager</code>, or <code>XmPrimitive</code> reference page.</p>
<h2>Related</h2>
<p>Refer to the <i>Motif Programmer&#8217;s Guide</i> for more information about tabs and tab lists. <code><a href="/docs/linux/man/3-xmtablistcopy/">XmTabListCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmtablistfree/">XmTabListFree</a></code>(3), <code><a href="/docs/linux/man/3-xmtablistgettab/">XmTabListGetTab</a></code>(3), <code><a href="/docs/linux/man/3-xmtablistinserttabs/">XmTabListInsertTabs</a></code>(3), <code><a href="/docs/linux/man/3-xmtablistremovetabs/">XmTabListRemoveTabs</a></code>(3), <code><a href="/docs/linux/man/3-xmtablistreplacepositions/">XmTabListReplacePositions</a></code>(3), and <code><a href="/docs/linux/man/3-xmtablisttabcount/">XmTabListTabCount</a></code>(3).</p>
