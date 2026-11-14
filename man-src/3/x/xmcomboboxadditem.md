---
title: "xmcomboboxadditem(3)"
name: "xmcomboboxadditem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcomboboxadditem/"
description: "XmComboBoxAddItem — add an item to the ComboBox widget"
---

<p><code>XmComboBoxAddItem</code> &#8212; add an item to the ComboBox widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>void XmComboBoxAddItem</code>(
<code>Widget w</code>,
<code>XmString item</code>,
<code>int pos</code>,
<code>Boolean unique</code>);</pre>
<h2>Description</h2>
<p>The <code>XmComboBoxAddItem</code> function adds the given item to the XmComboBox at the given position. </p>
<p> The <i>w</i> argument specifies the XmComboBox widget ID. </p>
<p> The <i>item</i> argument specifies the <code>XmString</code> for the new item. </p>
<p> The <i>pos</i> argument specifies the position of the new item. </p>
<p> The <i>unique</i> argument specifies if this item should duplicate an identical item or not.</p>
<h2>Return Value</h2>
<p>The <code>XmComboBoxAddItem</code> function returns no value.</p>
<h2>Application Usage</h2>
<p>The functions <code>XmComboBoxAddItem</code> and <code>XmComboBoxDeletePos</code> have different naming conventions (Item versus Pos) because of the objects they are manipulating. The Item is a string to be added, the Pos is a numeric position number.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmcomboboxdeletepos/">XmComboBoxDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxsetitem/">XmComboBoxSetItem</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxselectitem/">XmComboBoxSelectItem</a></code>(3).</p>
