---
title: "xmscrollbarsetvalues(3)"
name: "xmscrollbarsetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrollbarsetvalues/"
description: "XmScrollBarSetValues — A ScrollBar function that changes ScrollBar’s increment values and the slider’s size and position"
---

<p><code>XmScrollBarSetValues</code> &#8212; A ScrollBar function that changes ScrollBar&#8217;s increment values and the slider&#8217;s size and position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrollBar.h&gt;
void XmScrollBarSetValues (<i>widget, value, slider_size, increment, page_increment,
notify</i>)
 Widget <i>widget</i>;
 int <i>value</i>;
 int <i>slider_size</i>;
 int <i>increment</i>;
 int <i>page_increment</i>;
 Boolean <i>notify</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmSetScrollBarValues</code> changes the ScrollBar&#8217;s increment values and the slider&#8217;s size and position. The scroll region is overlaid with a slider bar that is adjusted in size and position using the main ScrollBar or set slider function attributes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ScrollBar widget ID.</p>
<dt><i>value</i></p>
<dd>Specifies the ScrollBar&#8217;s slider position. Refer to the <code>XmNvalue</code> resource described on <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
<dt><i>slider_size</i></p>
<dd>Specifies the size of the slider. Refer to the <code>XmNsliderSize</code> resource described on <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3). This argument sets that resource. Specify a value of 0 (zero) if you do not want to change the value.</p>
<dt><i>increment</i></p>
<dd>Specifies the amount of button increment and decrement. Refer to the <code>XmNincrement</code> resource described on <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3). This argument sets that resource. Specify a value of 0 (zero) if you do not want to change the value.</p>
<dt><i>page_increment</i></p>
<dd>Specifies the amount of page increment and decrement. Refer to the <code>XmNpageIncrement</code> resource described on <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3). This argument sets that resource. Specify a value of 0 (zero) if you do not want to change the value.</p>
<dt><i>notify</i></p>
<dd>Specifies a Boolean value that, when True, indicates a change in the ScrollBar value and also specifies that the ScrollBar widget automatically activates the <code>XmNvalueChangedCallback</code> with the recent change. If it is set to False, it specifies any change that has occurred in the ScrollBar&#8217;s value, but does not activate <code>XmNvalueChangedCallback</code>.</dl>
<p> For a complete definition of ScrollBar and its associated resources, see <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3).</p>
