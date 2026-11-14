---
title: "xmcomboboxsetitem(3)"
name: "xmcomboboxsetitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcomboboxsetitem/"
description: "XmComboBoxSetItem — set an item in the XmComboBox list"
---

<p><code>XmComboBoxSetItem</code> &#8212; set an item in the XmComboBox list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>void XmComboBoxSetItem</code>(
<code>Widget w</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p>The <code>XmComboBoxSetItem</code> function selects an item in the XmList of the given XmComboBox widget and makes it the first visible item in the list. </p>
<p> The <i>w</i> argument specifies the XmComboBox widget ID. </p>
<p> The <i>item</i> argument specifies the <code>XmString</code> for the item to be set in the XmComboBox. If the <i>item</i> is not found on the list, <code>XmComboBoxSetItem</code> notifies the user via the <code>XtWarning</code> function.</p>
<h2>Return Value</h2>
<p>The <code>XmComboBoxSetItem</code> function returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmcomboboxadditem/">XmComboBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxdeletepos/">XmComboBoxDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxselectitem/">XmComboBoxSelectItem</a></code>(3); <code><a href="/docs/linux/man/3-xtwarning/">XtWarning</a></code>(3). in the CAE Specification, Window Management: X Toolkit Intrinsics.</p>
