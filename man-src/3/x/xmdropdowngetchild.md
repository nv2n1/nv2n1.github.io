---
title: "xmdropdowngetchild(3)"
name: "xmdropdowngetchild"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropdowngetchild/"
description: "XmDropDownGetChild — A DropDown function that is used to access a component"
---

<p><code>XmDropDownGetChild</code> &#8212; A DropDown function that is used to access a component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DropDown.h&gt;
<code>Widget XmDropDownGetChild</code>(
<code>Widget widget</code>,
<code>int child</code>);</pre>
<h2>Description</h2>
<p><code>XmDropDownGetChild</code> is used to access a component within a DropDown. The parameters given to the function are the DropDown widget and a value indicating which component to access.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DropDown widget ID.</p>
<dt><i>child</i></p>
<dd>Specifies a component within the DropDown. The following are legal values for this parameter:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmDROPDOWN_LABEL</code></p>
<dt> &bull;</p>
<dd><code>XmDROPDOWN_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmDROPDOWN_ARROW_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDROPDOWN_LIST</code></dl>
</dl>
</dl>
<p> For a complete definition of DropDown and its associated resources, see <code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the specified DropDown component. An application should not assume that the returned widget will be of any particular class.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropdown/">XmDropDown</a></code>(3).</p>
