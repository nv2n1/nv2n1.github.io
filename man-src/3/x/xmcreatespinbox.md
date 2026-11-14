---
title: "xmcreatespinbox(3)"
name: "xmcreatespinbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatespinbox/"
description: "XmCreateSpinBox — The SpinBox creation function"
---

<p><code>XmCreateSpinBox</code> &#8212; The SpinBox creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SpinB.h&gt;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmCreateSpinBox</code> creates a SpinBox widget. </p>
<p> This function creates a SpinBox with two arrows, but without any traversable children (choices to spin). The application can create text children to go with this parent SpinBox using <code>XmCreateTextField</code> or <code>XmCreateText</code>.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of SpinBox and its associated resources, see <code><a href="/docs/linux/man/3-xmspinbox/">XmSpinBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the SpinBox widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmspinbox/">XmSpinBox</a></code>(3)</p>
