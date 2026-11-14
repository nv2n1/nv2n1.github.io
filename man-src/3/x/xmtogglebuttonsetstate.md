---
title: "xmtogglebuttonsetstate(3)"
name: "xmtogglebuttonsetstate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtogglebuttonsetstate/"
description: "XmToggleButtonSetState — A ToggleButton function that sets or changes the current state"
---

<p><code>XmToggleButtonSetState</code> &#8212; A ToggleButton function that sets or changes the current state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ToggleB.h&gt;
<code>void XmToggleButtonSetState</code>(
<code>Widget widget</code>,
<code>Boolean state</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmToggleButtonSetState</code> sets or changes the ToggleButton&#8217;s current state.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ToggleButton widget ID.</p>
<dt><i>state</i></p>
<dd>Specifies a Boolean value that indicates whether the ToggleButton state is selected or unselected. If the value is True, the button state is selected; if it is False, the button state is unselected.</p>
<dt><i>notify</i></p>
<dd>Indicates whether <code>XmNvalueChangedCallback</code> is called; it can be either True or False. The <code>XmNvalueChangedCallback</code> is only called when this function changes the state of the ToggleButton. When this argument is True and the ToggleButton is a child of a RowColumn widget whose <code>XmNradioBehavior</code> is True, setting the ToggleButton causes other ToggleButton and ToggleButtonGadget children of the RowColumn to be unselected.</dl>
<p> For a complete definition of ToggleButton and its associated resources, see <code><a href="/docs/linux/man/3-xmtogglebutton/">XmToggleButton</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtogglebutton/">XmToggleButton</a></code>(3).</p>
