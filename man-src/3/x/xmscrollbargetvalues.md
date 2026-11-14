---
title: "xmscrollbargetvalues(3)"
name: "xmscrollbargetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrollbargetvalues/"
description: "XmScrollBarGetValues — A ScrollBar function that returns the ScrollBar’s increment values"
---

<p><code>XmScrollBarGetValues</code> &#8212; A ScrollBar function that returns the ScrollBar&#8217;s increment values</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrollBar.h&gt;
void XmScrollBarGetValues (<i>widget, value_return, slider_size_return,
increment_return, page_increment_return</i>)
 Widget <i>widget</i>;
 int <i>* value_return</i>;
 int <i>* slider_size_return</i>;
 int <i>* increment_return</i>;
 int <i>* page_increment_return</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmScrollBarGetValues</code> returns the the ScrollBar&#8217;s increment values. The scroll region is overlaid with a slider bar that is adjusted in size and position using the main ScrollBar or set slider function attributes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ScrollBar widget ID.</p>
<dt><i>value_return</i></p>
<dd>Returns the ScrollBar&#8217;s slider position between the <code>XmNminimum</code> and <code>XmNmaximum</code> resources. Specify NULL to prevent the return of a particular value.</p>
<dt><i>slider_size_return</i></p>
<dd>Returns the size of the slider as a value between 0 (zero) and the absolute value of <code>XmNmaximum</code> minus <code>XmNminimum</code>. The size of the slider varies, depending on how much of the slider scroll area it represents.</p>
<dt><i>increment_return</i></p>
<dd>Returns the amount of increment and decrement.</p>
<dt><i>page_increment_return</i></p>
<dd>Returns the amount of page increment and decrement.</dl>
<p> For a complete definition of ScrollBar and its associated resources, see <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ScrollBar&#8217;s increment values.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
