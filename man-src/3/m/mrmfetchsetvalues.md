---
title: "mrmfetchsetvalues(3)"
name: "mrmfetchsetvalues"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmfetchsetvalues/"
description: "MrmFetchSetValues — Fetches the values to be set from literals stored in UID files"
---

<p><code>MrmFetchSetValues</code> &#8212; Fetches the values to be set from literals stored in UID files</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmFetchSetValues</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>Widget widget</code>,
<code>ArgList args</code>,
<code>Cardinal num_args</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmFetchSetValues</code> function is similar to <code>XtSetValues</code>, except that the values to be set are defined by the UIL named values that are stored in the UID hierarchy. <code>MrmFetchSetValues</code> fetches the values to be set from literals stored in UID files.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the ID of the UID hierarchy that contains the specified literal. The value of <i>hierarchy_id</i> was returned in a previous call to <code>MrmOpenHierarchyPerDisplay</code>.</p>
<dt><i>widget</i></p>
<dd>Specifies the widget that is modified.</p>
<dt><i>args</i></p>
<dd>Specifies an argument list that identifies the widget arguments to be modified as well as the index (UIL name) of the literal that defines the value for that argument. The name part of each argument (<i>args[n].name</i>) must begin with the string <code>XmN</code> followed by the name that uniquely identifies this attribute tag. For example, <code>XmNwidth</code> is the attribute name associated with the core argument <i>width</i>. The value part (<i>args[n].value</i>) must be a string that gives the index (UIL name) of the literal. You must define all literals in UIL as exported values.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of entries in <i>args</i>.</dl>
<p> This function sets the values on a widget, evaluating the values as public literal resource references resolvable from a UID hierarchy. Each literal is fetched from the hierarchy, and its value is modified and converted as required. This value is then placed in the argument list and used as the actual value for an <code>XtSetValues</code> call. <code>MrmFetchSetValues</code> allows a widget to be modified after creation using UID file values the same way creation values are used in <code>MrmFetchWidget</code>. </p>
<p> As in <code>MrmFetchWidget</code>, each argument whose value can be evaluated from the UID hierarchy is set in the widget. Values that are not found or values in which conversion errors occur are not modified. </p>
<p> Each entry in the argument list identifies an argument to be modified in the widget. The name part identifies the tag, which begins with <code>XmN</code>. The value part must be a string whose value is the index of the literal. Thus, the following code would modify the label resource of the widget to have the value of the literal accessed by the index <code>OK_button_label</code> in the hierarchy: </p>
<pre><tt>args[n].name = XmNlabel;
args[n].value = &quot;OK_button_label&quot;;</tt></pre>
<h2>Return Value</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmPARTIAL_SUCCESS</code></p>
<dd>At least one literal was successfully fetched.</p>
<dt><code>MrmBAD_HIERARCHY</code></p>
<dd>The hierarchy ID was invalid.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-mrmopenhierarchyperdisplay/">MrmOpenHierarchyPerDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xtsetvalues/">XtSetValues</a></code>(3).</p>
