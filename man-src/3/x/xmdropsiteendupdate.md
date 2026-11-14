---
title: "xmdropsiteendupdate(3)"
name: "xmdropsiteendupdate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteendupdate/"
description: "XmDropSiteEndUpdate — A Drag and Drop function that facilitates processing updates to multiple drop sites"
---

<p><code>XmDropSiteEndUpdate</code> &#8212; A Drag and Drop function that facilitates processing updates to multiple drop sites</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteEndUpdate</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteEndUpdate</code> is used in conjunction with <code>XmDropSiteStartUpdate</code> to process updates to multiple drop sites within the same hierarchy. <code>XmDropSiteStartUpdate</code> and <code>XmDropSiteEndUpdate</code> signal the beginning and the end respectively of a series of calls to <code>XmDropSiteUpdate</code>. Calls to <code>XmDropSiteStartUpdate</code> and <code>XmDropSiteEndUpdate</code> can be recursively stacked. Using these routines optimizes the processing of update information.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of any widget within a given hierarchy. The function uses this widget to identify the shell that contains the drop sites.</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsitestartupdate/">XmDropSiteStartUpdate</a></code>(3) and <code><a href="/docs/linux/man/3-xmdropsiteupdate/">XmDropSiteUpdate</a></code>(3).</p>
