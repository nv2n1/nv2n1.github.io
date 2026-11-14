---
title: "urxvt256c-ml-tabbed(1)"
name: "urxvt256c-ml-tabbed"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-tabbed/"
description: "tabbed – tabbed interface to urxvt"
---

<h2 class="name">NAME</h2>
<p> tabbed &#8211; tabbed interface to urxvt </p>
<h2>DESCRIPTION</h2>
<p> This transforms the terminal into a tabbar with additional terminals, that is, it implements what is commonly referred to as &#8220;tabbed terminal&#8221;. The topmost line displays a &#8220;[<font SIZE="-1">NEW</font>]&#8221; button, which, when clicked, will add a new tab, followed by one button per tab. </p>
<p> Clicking a button will activate that tab. Pressing <code>Shift-Left</code> and <code>Shift-Right</code> will switch to the tab left or right of the current one, while <code>Shift-Down</code> creates a new tab. Pressing <code>Ctrl-Left</code> and <code>Ctrl-Right</code> will renumber the current tab by moving it to the left or to the right. </p>
<p> The tabbar itself can be configured similarly to a normal terminal, but with a resource class of <tt>&quot;URxvt.tabbed&quot;</tt>. In addition, it supports the following four resources (shown with defaults): </p>
<pre>
   URxvt.tabbed.tabbar-fg: &lt;colour-index, default 3&gt;
   URxvt.tabbed.tabbar-bg: &lt;colour-index, default 0&gt;
   URxvt.tabbed.tab-fg:    &lt;colour-index, default 0&gt;
   URxvt.tabbed.tab-bg:    &lt;colour-index, default 1&gt;
</pre>
<p> See <i></i><font SIZE="-1"><i>COLOR AND GRAPHICS</i></font><i></i> in the @@RXVT_NAME@@(1) manpage for valid indices. </p>
<h2>Index</h2>
