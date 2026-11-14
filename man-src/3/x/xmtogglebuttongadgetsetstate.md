---
title: "xmtogglebuttongadgetsetstate(3)"
name: "xmtogglebuttongadgetsetstate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtogglebuttongadgetsetstate/"
description: "XmToggleButtonGadgetSetState — A ToggleButtonGadget function that sets or changes the current state"
---

<p><code>XmToggleButtonGadgetSetState</code> &#8212; A ToggleButtonGadget function that sets or changes the current state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ToggleBG.h&gt;
<code>void XmToggleButtonGadgetSetState</code>(
<code>Widget widget</code>,
<code>Boolean state</code>,
<code>Boolean notify</code>);</pre>
<h2>Description</h2>
<p><code>XmToggleButtonGadgetSetState</code> sets or changes the ToggleButtonGadget&#8217;s current state.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ToggleButtonGadget widget ID.</p>
<dt><i>state</i></p>
<dd>Specifies a Boolean value that indicates whether the ToggleButtonGadget state is selected or unselected. If the value is True, the button state is selected; if it is False, the button state is unselected.</p>
<dt><i>notify</i></p>
<dd>Indicates whether <code>XmNvalueChangedCallback</code> is called; it can be either True or False. The <code>XmNvalueChangedCallback</code> is only called when this function changes the state of the ToggleButtonGadget. When this argument is True and the ToggleButtonGadget is a child of a RowColumn widget whose <code>XmNradioBehavior</code> is True, setting the ToggleButtonGadget causes other ToggleButton and ToggleButtonGadget children of the RowColumn to be unselected.</dl>
<p> For a complete definition of ToggleButtonGadget and its associated resources, see <code><a href="/docs/linux/man/3-xmtogglebuttongadget/">XmToggleButtonGadget</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtogglebuttongadget/">XmToggleButtonGadget</a></code>(3).</p>
