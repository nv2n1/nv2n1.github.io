---
title: "xmwidgetgetbaselines(3)"
name: "xmwidgetgetbaselines"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmwidgetgetbaselines/"
description: "XmWidgetGetBaselines — Retrieves baseline information for a widget"
---

<p><code>XmWidgetGetBaselines</code> &#8212; Retrieves baseline information for a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmWidgetGetBaselines</code>(
<code>Widget widget</code>,
<code>Dimension **baselines</code>,
<code>int *line_count</code>);</pre>
<h2>Description</h2>
<p><code>XmWidgetGetBaselines</code> returns an array that contains one or more baseline values associated with the specified widget. The baseline of any given line of text is a vertical offset in pixels from the origin of the widget&#8217;s bounding box to the given baseline.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget for which baseline values are requested</p>
<dt><i>baselines</i></p>
<dd>Returns an array that contains the value of each baseline of text in the widget. The function allocates space to hold the returned array. The application is responsible for managing the allocated space. The application can recover this allocated space by calling <code>XtFree</code>.</p>
<dt><i>line_count</i></p>
<dd>Returns the number of lines in the widget</dl>
<h2>Return</h2>
<p>Returns a Boolean value that indicates whether the widget contains a baseline. If the value is True, the function returns a value for each baseline of text. If it is False, the function was unable to return a baseline value.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmwidgetgetdisplayrect/">XmWidgetGetDisplayRect</a></code>(3).</p>
