---
title: "xmdatafieldxytopos(3)"
name: "xmdatafieldxytopos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldxytopos/"
description: "XmDataFieldXYToPos — A DataField function that accesses the character position nearest an x and y position"
---

<p><code>XmDataFieldXYToPos</code> &#8212; A DataField function that accesses the character position nearest an x and y position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>XmTextPosition XmDataFieldXYToPos</code>(
<code>Widget widget</code>,
<code>Position x</code>,
<code>Position y</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldXYToPos</code> accesses the character position nearest to the specified <i>x</i> and <i>y</i> position, relative to the upper left corner of the DataField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>x</i></p>
<dd>Specifies the <i>x</i> position, relative to the upper left corner of the widget.</p>
<dt><i>y</i></p>
<dd>Specifies the <i>y</i> position, relative to the upper left corner of the widget.</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the character position in the text nearest the <i>x</i> and <i>y</i> position specified. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
