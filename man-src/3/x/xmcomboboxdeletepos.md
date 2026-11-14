---
title: "xmcomboboxdeletepos(3)"
name: "xmcomboboxdeletepos"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcomboboxdeletepos/"
description: "XmComboBoxDeletePos — Delete a XmComboBox item"
---

<p><code>XmComboBoxDeletePos</code> &#8212; Delete a XmComboBox item</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>void XmComboBoxDeletePos</code>(
<code>Widget w</code>,
<code>int pos</code>);</pre>
<h2>Description</h2>
<p>The <code>XmComboBoxDeletePos</code> function deletes a specified item from a XmComboBox widget. </p>
<p> The <i>w</i> argument specifies the XmComboBox widget ID. </p>
<p> The <i>pos</i> argument specifies the position of the item to be deleted.</p>
<h2>Return Value</h2>
<p>The <code>XmComboBoxDeletePos</code> function returns no value.</p>
<h2>Application Usage</h2>
<p>The functions <code>XmComboBoxAddItem</code> and <code>XmComboBoxDeletePos</code> have different naming conventions (Item versus Pos) because of the objects they are manipulating. The Item is a string to be added, the Pos is a numeric position number.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmcomboboxadditem/">XmComboBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxsetitem/">XmComboBoxSetItem</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxselectitem/">XmComboBoxSelectItem</a></code>(3).</p>
