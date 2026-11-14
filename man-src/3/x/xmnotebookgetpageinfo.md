---
title: "xmnotebookgetpageinfo(3)"
name: "xmnotebookgetpageinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmnotebookgetpageinfo/"
description: "XmNotebookGetPageInfo — A Notebook function that returns page information"
---

<p><code>XmNotebookGetPageInfo</code> &#8212; A Notebook function that returns page information</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Notebook.h&gt;
<code>XmNotebookPageStatus XmNotebookGetPageInfo</code>(
<code>Widget notebook</code>,
<code>int page_number</code>,
<code>XmNotebookPageInfo *page_info</code>);</pre>
<h2>Description</h2>
<p><code>XmNotebookGetPageInfo</code> returns status information for the specified Notebook page.</p>
<dl COMPACT>
<dt><i>notebook</i></p>
<dd>Specifies the Notebook widget.</p>
<dt><i>page_number</i></p>
<dd>Specifies the page number to be queried.</p>
<dt><i>page_info</i></p>
<dd>Points to the structure containing the page information. The structure has the following form:</dl>
<pre>typedef struct
{
 int <i>page_number</i>;
 Widget <i>page_widget</i>;
 Widget <i>status_area_widget</i>;
 Widget <i>major_tab_widget</i>;
 Widget <i>minor_tab_widget</i>;
} XmNotebookPageInfo;
(<code>void</code>)</pre>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>page_number</i></p>
<dd>Specifies the <i>page_number</i> passed to the function.</p>
<dt><i>page_widget</i></p>
<dd>Specifies a child widget of the Notebook with a <code>XmNchildType</code> of <code>XmPAGE</code> and a <code>XmNpageNumber</code> equal to <i>page_number</i> if one exists; otherwise set to NULL.</p>
<dt><i>status_area_widget</i></p>
<dd>Specifies a child widget of the Notebook with a <code>XmNchildType</code> of <code>XmSTATUS_AREA</code> and a <code>XmNpageNumber</code> equal to <i>page_number</i> if one exists; otherwise set to NULL.</p>
<dt><i>major_tab_widget</i></p>
<dd>Specifies a child widget of the Notebook with a <code>XmNchildType</code> of <code>XmMAJOR_TAB</code> and the nearest <code>XmNpageNumber</code> equal to or less than <i>page_number</i> if one exists; otherwise set to NULL.</p>
<dt><i>minor_tab_widget</i></p>
<dd>Specifies a child widget of the Notebook with a <code>XmNchildType</code> of <code>XmMINOR_TAB</code> and the nearest <code>XmNpageNumber</code> equal to or less than <i>page_number</i> if one exists; otherwise set to NULL.</dl>
</dl>
<p> For a complete definition of Notebook and its associated resources, see <code><a href="/docs/linux/man/3-xmnotebook/">XmNotebook</a></code>(3).</p>
<h2>Return</h2>
<p>Returns one of the following page status values:</p>
<dl COMPACT>
<dt><code>XmPAGE_FOUND</code></p>
<dd>The specified page was found.</p>
<dt><code>XmPAGE_INVALID</code></p>
<dd>The specified page number is out of the page number range.</p>
<dt><code>XmPAGE_EMPTY</code></p>
<dd>The specified page does not have a page widget.</p>
<dt><code>XmPAGE_DUPLICATED</code></p>
<dd>There is more than one page widget with the specified page number. The more recently managed page widget is used for the page information structure.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmnotebook/">XmNotebook</a></code>(3).</p>
