---
title: "xmtablistreplacepositions(3)"
name: "xmtablistreplacepositions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtablistreplacepositions/"
description: "XmTabListReplacePositions — A convenience function that creates a new tab list with replacement tabs"
---

<p><code>XmTabListReplacePositions</code> &#8212; A convenience function that creates a new tab list with replacement tabs</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmTabList XmTabListReplacePositions</code>(
<code>XmTabList oldlist</code>,
<code>Cardinal *position_list</code>,
<code>XmTab *tabs</code>,
<code>Cardinal tab_count</code>);</pre>
<h2>Description</h2>
<p><code>XmTabListReplacePositions</code> creates a new tab list that contains the contents of <i>oldlist</i>, but with the tabs at the positions in <i>position_list</i> replaced with copies of the corresponding tabs in <i>tabs</i>. A warning message is displayed if a specified position is invalid; for example, if the value is a number greater than the number of tabs in the tab list. </p>
<p> This function deallocates the original tab list after extracting the required information. It is the caller&#8217;s responsibility to free the tabs in <i>tabs</i> by using the <code>XmTabFree</code> function.</p>
<dl COMPACT>
<dt><i>oldlist</i></p>
<dd>Specifies the tab list. The function deallocates the tab list after extracting the required information.</p>
<dt><i>position_list</i></p>
<dd>Specifies an array of positions of the tabs to be replaced. The position of the first tab is 0 (zero), the position of the second tab is 1, and so on.</p>
<dt><i>tabs</i></p>
<dd>Specifies an array of the replacement tabs.</p>
<dt><i>tab_count</i></p>
<dd>Specifies the number of elements in <i>position_list</i> and <i>tabs</i>.</dl>
<h2>Return</h2>
<p>If <i>tabs</i>, <i>oldlist</i>, or <i>position_list</i> is NULL, or <i>tab_count</i> is 0 (zero), returns <i>oldlist</i>. Otherwise, this function returns the new tab list. The function allocates space to hold the returned tab list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmTabListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtablist/">XmTabList</a></code>(3).</p>
