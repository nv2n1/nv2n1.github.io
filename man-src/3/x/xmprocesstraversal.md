---
title: "xmprocesstraversal(3)"
name: "xmprocesstraversal"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprocesstraversal/"
description: "XmProcessTraversal — A function that determines which component receives keyboard events when a widget has the focus"
---

<p><code>XmProcessTraversal</code> &#8212; A function that determines which component receives keyboard events when a widget has the focus</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmProcessTraversal</code>(
<code>Widget widget</code>,
<code>XmTraversalDirection direction</code>);</pre>
<h2>Description</h2>
<p><code>XmProcessTraversal</code> determines which component of a hierarchy receives keyboard events when the hierarchy that contains the given widget has keyboard focus. </p>
<p> <code>XmProcessTraversal</code> changes focus only when the keyboard focus policy of the widget hierarchy is explicit. If the <code>XmNkeyboardFocusPolicy</code> of the nearest shell ancestor of the given widget is not <code>XmEXPLICIT</code>, <code>XmProcessTraversal</code> returns False without making any focus changes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget ID of the widget whose hierarchy is to be traversed</p>
<dt><i>direction</i></p>
<dd>Specifies the direction of traversal</dl>
<h3>Definitions</h3>
<p>In order to be eligible to receive keyboard focus when the shell&#8217;s <code>XmNkeyboardFocusPolicy</code> is <code>XmEXPLICIT</code>, a widget or gadget must meet the following conditions:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The widget and its ancestors are not in the process of being destroyed.</p>
<dt> &bull;</p>
<dd>The widget and its ancestors are <i>sensitive</i>. A widget is sensitive when its <code>XmNsensitive</code> and <code>XmNancestorSensitive</code> resources are both True.</p>
<dt> &bull;</p>
<dd>The <code>XmNtraversalOn</code> resource for the widget and its ancestors is True.</p>
<dt> &bull;</p>
<dd>The widget is viewable. This means that the widget and its ancestors are managed, realized, and (except for gadgets) mapped. Furthermore, in general, some part of the widget&#8217;s rectangular area must be unobscured by the widget&#8217;s ancestors. If an application unmaps a widget that has its <code>XmNmappedWhenManaged</code> resource set to True, the result is undefined.</p>
<dd>In a ScrolledWindow with an <code>XmNscrollingPolicy</code> of <code>XmAUTOMATIC</code>, a widget that is obscured because it is not within the clip window may be able to receive focus if some part of the widget is within the work area and if an <code>XmNtraverseObscuredCallback</code> routine can make the widget at least partially visible by scrolling the window.</dl>
<p> In general only primitives, gadgets, and Drawing Area are eligible to receive focus. Most managers cannot receive focus even if they meet all these conditions. </p>
<p> The <i>direction</i> argument identifies the kind of traversal action to take. The descriptions of these actions below refer to traversable non-tab-group widgets and traversable tab groups.</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>A traversable non-tab-group widget is a widget that is not a tab group and that meets all the conditions for receiving focus described above.</p>
<dt> &bull;</p>
<dd>A traversable tab group widget is a tab group widget that meets the same conditions, except that a manager that is a tab group and meets the other conditions is also eligible for traversal as long as it contains a descendant that can receive focus.</dl>
<p> A tab group is a widget whose <code>XmNnavigationType</code> is:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmTAB_GROUP</code> or <code>XmSTICKY_TAB_GROUP</code>, if the hierarchy (up to the nearest shell ancestor) that contains the widget has no widget whose <code>XmNnavigationType</code> is <code>XmEXCLUSIVE_TAB_GROUP</code></p>
<dt> &bull;</p>
<dd><code>XmEXCLUSIVE_TAB_GROUP</code> or <code>XmSTICKY_TAB_GROUP</code>, if the hierarchy (up to the nearest shell ancestor) that contains the widget has any widget whose <code>XmNnavigationType</code> is <code>XmEXCLUSIVE_TAB_GROUP</code></dl>
<h3>Traversal Actions</h3>
<p>The hierarchy to be traversed is that containing the <i>widget</i> argument. This hierarchy is traversed only up to the nearest shell; <code>XmProcessTraversal</code> does not move focus from one shell to another. If the shell containing <i>widget</i> does not currently have the focus, any change that <code>XmProcessTraversal</code> makes to the element with focus within that shell does not take effect until the next time the shell receives focus. </p>
<p> <code>XmProcessTraversal</code> begins the traversal action from the widget in the hierarchy that currently has keyboard focus or that last had focus when the user traversed away from the shell hierarchy. </p>
<p> The value of the <i>direction</i> argument determines which of three kinds of traversal action to take:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Traversal to a non-tab-group widget. This kind of traversal is possible only when the widget that currently has focus is not a tab group; otherwise, <code>XmProcessTraversal</code> returns False for these actions.</p>
<dd>These actions do not move focus from one tab group to another. The actions first determine the containing tab group. This is the tab group containing the widget that currently has focus. The actions traverse only to a non-tab-group widget within the containing tab group.</p>
<dd>A non-tab-group widget is eligible for this kind of traversal if the widget is traversable and has no tab group ancestors up to the containing tab group. If the tab group contains no traversable non-tab-group widgets, <code>XmProcessTraversal</code> returns False.</p>
<dd>Following are the possible values of the <i>direction</i> argument. Note that when actions wrap, wrapping occurs in the traversal direction. The following describes what happens in a left to right environment:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_RIGHT</code>&#8212;If the <code>XmNnavigationType</code> of the containing tab group is not <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget to the right of the widget that currently has focus. In a left to right environment, at the right side of the tab group this action wraps to the non-tab-group widget at the left side and next toward the bottom. At the rightmost widget in the bottom row of the tab group this action wraps to the non-tab-group widget at the leftmost widget in the upper row.</p>
<dd>In a right to left environment, at the right side of the tab group, this action wraps to the non-tab-group widget at the left side and next toward the top. At the rightmost widget in the upper row of the tab group this action wraps to the non-tab-group widget at the leftmost widget in the bottom row.</p>
<dd>If the <code>XmNnavigationType</code> of the containing tab group is <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget in the tab group, proceeding in the order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the last widget in the tab group, this action wraps to the first non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_LEFT</code>&#8212;If the <code>XmNnavigationType</code> of the containing tab group is not <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget to the left of the widget that currently has focus. In a left to right environment, at the left side of the tab group this action wraps to the non-tab-group widget at the right side and next toward the top. At the leftmost widget in the upper row of the tab group this action wraps to the non-tab-group widget at the rightmost widget in the bottom row.</p>
<dd>In a right to left environment, at the left side of the tab group this action wraps to the non-tab-group widget at the right side and next toward the bottom. At the leftmost widget in the bottom row of the tab group this action wraps to the non-tab-group widget at the rightmost widget in the upper row.</p>
<dd>If the <code>XmNnavigationType</code> of the containing tab group is <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the previous traversable non-tab-group widget in the tab group, proceeding in the reverse order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the first widget in the tab group, this action wraps to the last non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_DOWN</code>&#8212;If the <code>XmNnavigationType</code> of the containing tab group is not <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget below the widget that currently has focus. In a left to right environment, at the bottom of the tab group this action wraps to the non-tab-group widget at the top and next toward the right. At the bottom widget in the rightmost column of the tab group this action wraps to the non-tab-group widget at the top widget in the leftmost column.</p>
<dd>In a right to left environment, at the bottom of the tab group this action wraps to the non-tab-group widget at the top and next toward the left. At the bottom widget of the leftmost widget of the tab group this action wraps to the non-tab-group widget at the top widget of the rightmost column.</p>
<dd>If the <code>XmNnavigationType</code> of the containing tab group is <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget in the tab group, proceeding in the order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the last widget in the tab group, this action wraps to the first non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_UP</code>&#8212;If the <code>XmNnavigationType</code> of the containing tab group is not <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the next traversable non-tab-group widget above the widget that currently has focus. In a left to right environment, at the top of the tab group this action wraps to the non-tab-group widget at the bottom and next toward the left. At the top widget of the leftmost column of the tab group this action wraps to the non-tab-group widget at the bottom widget of the rightmost column.</p>
<dd>In a right to left environment, at the top of the tab group this action wraps to the non-tab-group widget at the bottom and next toward the right. At the top widget of the right most column of the tab group this action wraps to the non-tab-group widget at the bottom widget of the leftmost column.</p>
<dd>If the <code>XmNnavigationType</code> of the containing tab group is <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the previous traversable non-tab-group widget in the tab group, proceeding in the reverse order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the first widget in the tab group, this action wraps to the last non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_NEXT</code>&#8212;Focus moves to the next traversable non-tab-group widget in the tab group, proceeding in the order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the last widget in the tab group, this action wraps to the first non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_PREV</code>&#8212;Focus moves to the previous traversable non-tab-group widget in the tab group, proceeding in the reverse order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists. After the first widget in the tab group, this action wraps to the last non-tab-group widget.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_HOME</code>&#8212;If the <code>XmNnavigationType</code> of the containing tab group is not <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the first traversable non-tab-group widget at the initial focus of the tab group.</p>
<dd>If the <code>XmNnavigationType</code> of the containing tab group is <code>XmEXCLUSIVE_TAB_GROUP</code>, focus moves to the first traversable non-tab-group widget in the tab group, according to the order in which the widgets appear in their parents&#8217; <code>XmNchildren</code> lists.</dl>
</dl>
<dt> &bull;</p>
<dd>Traversal to a tab group. These actions first determine the current widget hierarchy and the containing tab group. The current widget hierarchy is the widget hierarchy whose root is the nearest shell ancestor of the widget that currently has focus. The containing tab group is is the tab group containing the widget that currently has focus. If the current widget hierarchy contains no traversable tab groups, <code>XmProcessTraversal</code> returns False.</p>
<dd>Following are the possible values of the <i>direction</i> argument. If any tab group in the current widget hierarchy has an <code>XmNnavigationType</code> of <code>XmEXCLUSIVE_TAB_GROUP</code>, traversal of tab groups in the hierarchy proceeds to widgets in the order in which their <code>XmNnavigationType</code> resources were specified as <code>XmEXCLUSIVE_TAB_GROUP</code> or <code>XmSTICKY_TAB_GROUP</code>.:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_NEXT_TAB_GROUP</code>&#8212;Finds the hierarchy that contains <i>widget</i>, finds the active tab group (if any), and makes the next tab group the active tab group in the hierarchy.</p>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_PREV_TAB_GROUP</code>&#8212;Finds the hierarchy that contains <i>widget</i>, finds the active tab group (if any), and makes the previous tab group the active tab group in the hierarchy.</dl>
</dl>
<dt> &bull;</p>
<dd>Traversal to any widget. In this case the <i>widget</i> argument is the widget to which <code>XmProcessTraversal</code> tries to give focus. If the widget is not traversable, <code>XmProcessTraversal</code> returns False.</p>
<dd>Following are the possible values of the <i>direction</i> argument:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmTRAVERSE_CURRENT</code>&#8212;Finds the hierarchy and the tab group that contain <i>widget</i>. If this tab group is not the active tab group, this action makes it the active tab group. If <i>widget</i> is an item in the active tab group, this action makes it the active item. If <i>widget</i> is the active tab group, this action makes the first traversable item in the tab group the active item.</dl>
</dl>
</dl>
<h3>Cautions</h3>
<p>Using <code>XmProcessTraversal</code> to traverse to MenuBars, Pulldown menu panes, or Popup menu panes is not supported. </p>
<p> <code>XmProcessTraversal</code> cannot be called recursively. In particular, an application cannot call this routine from an <code>XmNfocusCallback</code> or <code>XmNlosingFocusCallback</code> procedure.</p>
<h2>Return</h2>
<p>Returns True if the traversal action succeeded. Returns False if the <code>XmNkeyboardFocusPolicy</code> of the nearest shell ancestor of <i>widget</i> is not <code>XmEXPLICIT</code>, if the traversal action finds no traversable widget to receive focus, or if the call to the routine has invalid arguments.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmgetvisibility/">XmGetVisibility</a></code>(3) and <code><a href="/docs/linux/man/3-xmistraversable/">XmIsTraversable</a></code>(3).</p>
