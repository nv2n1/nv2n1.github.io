---
title: "xmfileselectiondosearch(3)"
name: "xmfileselectiondosearch"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfileselectiondosearch/"
description: "XmFileSelectionDoSearch — A FileSelectionBox function that initiates a directory search"
---

<p><code>XmFileSelectionDoSearch</code> &#8212; A FileSelectionBox function that initiates a directory search</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/FileSB.h&gt;
<code>void XmFileSelectionDoSearch</code>(
<code>Widget widget</code>,
<code>XmString dirmask</code>);</pre>
<h2>Description</h2>
<p><code>XmFileSelectionDoSearch</code> initiates a directory and file search in a FileSelectionBox widget. For a description of the actions that the FileSelectionBox takes when doing a search, see <code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3).</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the FileSelectionBox widget ID.</p>
<dt><i>dirmask</i></p>
<dd>Specifies the directory mask used in determining the directories and files displayed in the FileSelectionBox lists. This value is used as the <i>mask</i> member of the input data <code>XmFileSelectionBoxCallbackStruct</code> structure passed to the FileSelectionBox&#8217;s <code>XmNqualifySearchDataProc</code>. The <i>dir</i> and <i>pattern</i> members of that structure are NULL.</dl>
<p> For a complete definition of FileSelectionBox and its associated resources, see <code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3).</p>
