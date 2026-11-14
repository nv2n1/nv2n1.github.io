---
title: "xmcontainerpaste(3)"
name: "xmcontainerpaste"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainerpaste/"
description: "XmContainerPaste — Container widget function to insert items from the clipboard"
---

<p><code>XmContainerPaste</code> &#8212; Container widget function to insert items from the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>Boolean XmContainerPaste</code>(
<code>Widget container</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerPaste</code> requests data transfer from the clipboard selection to the Container. This routine calls the widget&#8217;s <code>XmNdestinationCallback</code> procedures with the <i>selection</i> member of the <code>XmDestinationCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>operation</i> member set to <code>XmCOPY</code>. The Container widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the clipboard selection and for taking any related actions.</p>
<dl COMPACT>
<dt><i>container</i></p>
<dd>Specifies the Container widget ID.</dl>
<p> For a complete definition of Container and its associated resources, see <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
<h2>Return</h2>
<p>The function returns False if no data transfer takes place. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
