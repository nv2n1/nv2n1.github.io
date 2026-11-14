---
title: "xmgetsecondaryresourcedata(3)"
name: "xmgetsecondaryresourcedata"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetsecondaryresourcedata/"
description: "XmGetSecondaryResourceData — A function that provides access to secondary widget resource data"
---

<p><code>XmGetSecondaryResourceData</code> &#8212; A function that provides access to secondary widget resource data</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Cardinal XmGetSecondaryResourceData</code>(
<code>WidgetClass widget_class</code>,
<code>XmSecondaryResourceData **secondary_data_return</code>);</pre>
<h2>Description</h2>
<p>Some Motif widget classes (such as Gadget, Text, and VendorShell) have resources that are not accessible through the functions <code>XtGetResourceList</code> and <code>XtGetConstraintResourceList</code>. In order to retrieve the descriptions of these resources, an application must use <code>XmGetSecondaryResourceData</code>. </p>
<p> When a widget class has such resources, this function provides descriptions of the resources in one or more data structures. <code>XmGetSecondaryResourceData</code> takes a widget class argument and returns the number of these data structures associated with the widget class. If the return value is greater than 0 (zero), the function allocates and fills an array of pointers to the corresponding data structures. It returns this array at the address that is the value of the <i>secondary_data_return</i> argument. </p>
<p> The type <code>XmSecondaryResourceData</code> is a pointer to a structure with two members that are useful to an application: <i>resources</i>, of type <code>XtResourceList</code>, and <code>num_resources</code>, of type <code>Cardinal</code>. The <i>resources</i> member is a list of the widget resources that are not accessible using Xt functions. The <code>num_resources</code> member is the length of the <i>resources</i> list. </p>
<p> If the return value is greater than 0 (zero), <code>XmGetSecondaryResourceData</code> allocates memory that the application must free. Use <code>XtFree</code> to free the resource list in each structure (the value of the <i>resources</i> member), the structures themselves, and the array of pointers to the structures (the array whose address is <i>secondary_data_return</i>).</p>
<dl COMPACT>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class for which secondary resource data is to be retrieved.</p>
<dt><i>secondary_data_return</i></p>
<dd>Specifies a pointer to an array of <code>XmSecondaryResourceData</code> pointers to be returned by this function. If the widget class has no secondary resource data, for example, if the value returned by the function is 0 (zero), the function returns no meaningful value for this argument.</dl>
<h2>Return</h2>
<p>Returns the number of secondary resource data structures associated with this widget class.</p>
<h2>Example</h2>
<p>The following example uses <code>XmGetSecondaryResourceData</code> to print the names of the secondary resources of the Motif Text widget and then frees the data allocated by the function: </p>
<pre><tt>XmSecondaryResourceData * block_array;
Cardinal num_blocks, i, j;
if (num_blocks = XmGetSecondaryResourceData (xmTextWidgetClass,
 &amp;block_array)) {
 for (i = 0; i &lt; num_blocks; i++) {
 for (j = 0; j &lt; block_array[i]-&gt;num_resources; j++) {
 printf(&quot;%s
&quot;, block_array[i]-&gt;resources[j].resource_name);
 }
 XtFree((char*)block_array[i]-&gt;resources);
 XtFree((char*)block_array[i]);
 }
 XtFree((char*)block_array);
}</tt></pre>
