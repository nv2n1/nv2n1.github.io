---
title: "xmcomboboxselectitem(3)"
name: "xmcomboboxselectitem"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcomboboxselectitem/"
description: "XmComboBoxSelectItem — select a XmComboBox item"
---

<p><code>XmComboBoxSelectItem</code> &#8212; select a XmComboBox item</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;
<code>void XmComboBoxSelectItem</code>(
<code>Widget w</code>,
<code>XmString item</code>);</pre>
<h2>Description</h2>
<p>The <code>XmComboBoxSelectItem</code> function selects an item in the XmList of the XmComboBox widget. </p>
<p> The <i>w</i> argument specifies the XmComboBox widget ID. </p>
<p> The <i>item</i> argument specifies the <code>XmString</code> of the item to be selected. If the <i>item</i> is not found on the list, <code>XmComboBoxSelectItem</code> notifies the user via the <code>XtWarning</code> function.</p>
<h2>Return Value</h2>
<p>The <code>XmComboBoxSelectItem</code> function returns no value.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmcomboboxadditem/">XmComboBoxAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxdeletepos/">XmComboBoxDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmcomboboxsetitem/">XmComboBoxSetItem</a></code>(3); <code><a href="/docs/linux/man/3-xtwarning/">XtWarning</a></code>(3). in the CAE Specification, Window Management: X Toolkit Intrinsics.</p>
