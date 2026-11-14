---
title: "mrmfetchwidget(3)"
name: "mrmfetchwidget"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchwidget/"
description: "MrmFetchWidget — Fetches and creates an indexed (UIL named) application widget and its children"
---

<p><code>MrmFetchWidget</code> &#8212; Fetches and creates an indexed (UIL named) application widget and its children</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchWidget</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>String index</code>,
<code>Widget parent_widget</code>,
<code>Widget *widget</code>,
<code>MrmType *class</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchWidget</code> function fetches and creates an indexed application widget and its children. The indexed application widget is any widget that is named in UIL. In fetch operations, the fetched widget&#8217;s subtree is also fetched and created. This widget must not appear as the child of a widget within its own subtree. <code>MrmFetchWidget</code> does not execute <code>XtManageChild</code> for the newly created widget. </p>
<p> All widgets fetched by a call to <code>MrmFetchWidget</code> are not managed at the time of their creation callbacks.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the <code>UID</code> hierarchy that contains the interface definition. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the UIL name of the widget to fetch.</p>
<dt><i>parent_widget</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>widget</i></p>
<dd>Returns the widget ID of the created widget.</p>
<dt><i>class</i></p>
<dd>This argument must be set to an actual pointer; it cannot be a NULL pointer. <code>MrmFetchWidget</code> sets this argument to an implementation dependent value.</dl>
<p> An application can fetch any named widget in the <code>UID</code> hierarchy using <code>MrmFetchWidget</code>. <code>MrmFetchWidget</code> can be called at any time to fetch a widget that was not fetched at application startup. <code>MrmFetchWidget</code> can be used to defer fetching pop-up widgets until they are first referenced (presumably in a callback), and then used to fetch them once. </p>
<p> <code>MrmFetchWidget</code> can also create multiple instances of a widget (and its subtree). In this case, the <code>UID</code> definition functions as a template; a widget definition can be fetched any number of times. An application can use this template to make multiple instances of a widget, for example, in a dialog box box or menu. </p>
<p> The index (UIL name) that identifies the widget must be known to the application.</p>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmNOT_FOUND</code></p>
<dd>The widget was not found in UID hierarchy.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchwidgetoverride/">MrmFetchWidgetOverride</a></code>(3).</p>
