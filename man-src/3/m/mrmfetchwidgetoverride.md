---
title: "mrmfetchwidgetoverride(3)"
name: "mrmfetchwidgetoverride"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchwidgetoverride/"
description: "MrmFetchWidgetOverride — Fetches any indexed (UIL named) application widget. It overrides the arguments specified for this application widget in UIL"
---

<p><code>MrmFetchWidgetOverride</code> &#8212; Fetches any indexed (UIL named) application widget. It overrides the arguments specified for this application widget in UIL</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchWidgetOverride</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>String index</code>,
<code>Widget parent_widget</code>,
<code>String override_name</code>,
<code>ArgList override_args</code>,
<code>Cardinal override_num_args</code>,
<code>Widget *widget</code>,
<code>MrmType *class</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchWidgetOverride</code> function is the extended version of <code>MrmFetchWidget</code>. It is identical to <code>MrmFetchWidget</code>, except that it allows the caller to override the widget&#8217;s name and any arguments that <code>MrmFetchWidget</code> would otherwise retrieve from the UID file or one of the defaulting mechanisms. That is, the override argument list is not limited to those arguments in the UID file. </p>
<p> The override arguments apply only to the widget fetched and returned by this function. Its children (subtree) do not receive any override parameters.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the UID hierarchy that contains the interface definition. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>index</i></p>
<dd>Specifies the UIL name of the widget to fetch.</p>
<dt><i>parent_widget</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>override_name</i></p>
<dd>Specifies the name to override the widget name. Use a NULL value if you do not want to override the widget name.</p>
<dt><i>override_args</i></p>
<dd>Specifies the override argument list, exactly as given to <code>XtCreateWidget</code> (conversion complete and so forth). Use a NULL value if you do not want to override the argument list.</p>
<dt><i>override_num_args</i></p>
<dd>Specifies the number of arguments in <i>override_args</i>.</p>
<dt><i>widget</i></p>
<dd>Returns the widget ID of the created widget.</p>
<dt><i>class</i></p>
<dd>Returns the class code identifying MRM&#8217;s widget class. Literals identifying MRM widget class codes are defined in the include file <code>Mrm/MrmPublic.h</code>.</dl>
<h2>Return Value</h2>
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
<p><code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3), <code><a href="/docs/linux/man/3-mrmfetchwidget/">MrmFetchWidget</a></code>(3).</p>
