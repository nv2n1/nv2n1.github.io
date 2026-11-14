---
title: "mrmregisterclass(3)"
name: "mrmregisterclass"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmregisterclass/"
description: "MrmRegisterClass — Saves the information needed for MRM to access the widget creation function for user-defined widgets"
---

<p><code>MrmRegisterClass</code> &#8212; Saves the information needed for MRM to access the widget creation function for user-defined widgets</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmRegisterClass</code>(
<code>MrmType class_code</code>,
<code>String class_name</code>,
<code>String create_name</code>,
<code>Widget (*create_proc</code>) (),
<code>WidgetClass class_record</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmRegisterClass</code> function allows MRM to access user-defined widget classes. This function registers the necessary information for MRM to create widgets of this class. You must call <code>MrmRegisterClass</code> prior to fetching any user-defined class widget. </p>
<p> <code>MrmRegisterClass</code> saves the information needed to access the widget creation function and to do type conversion of argument lists by using the information in MRM databases.</p>
<dl COMPACT>
<dt><i>class_code</i></p>
<dd>This argument is ignored; it is present for compatibility with previous releases.</p>
<dt><code>class_name</code></p>
<dd>This argument is ignored; it is present for compatibility with previous releases.</p>
<dt><i>create_name</i></p>
<dd>Specifies the case-sensitive name of the low-level widget creation function for the class. An example from the Motif Toolkit is <code>XmCreateLabel</code>. Arguments are <i>parent_widget</i>, <i>name</i>, <i>override_arglist</i>, and <i>override_argcount</i>.</p>
<dd>For user-defined widgets, <i>create_name</i> is the creation procedure in the UIL that defines this widget.</p>
<dt><code>create_proc</code></p>
<dd>Specifies the address of the creation function that you named in <i>create_name</i>.</p>
<dt><i>class_record</i></p>
<dd>Specifies a pointer to the class record.</dl>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed. </p>
</dl>
