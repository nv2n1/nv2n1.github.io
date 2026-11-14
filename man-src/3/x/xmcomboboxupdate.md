---
title: "xmcomboboxupdate(3)"
name: "xmcomboboxupdate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcomboboxupdate/"
description: "XmComboBoxUpdate — A ComboBox function that resynchronizes data"
---

<p><code>XmComboBoxUpdate</code> &#8212; A ComboBox function that resynchronizes data</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>void XmComboBoxUpdate</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmComboBoxUpdate</code> resynchronizes the internal data structures of a specified ComboBox widget. This function is useful when an application manipulates ComboBox&#8217;s child widgets, possibly changing data structures. For example, you might want to use the <code>XmComboBoxUpdate</code> function after a ComboBox List child selection has been changed without notification.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ComboBox widget ID.</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3).</p>
