---
title: "wmshell(3)"
name: "wmshell"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmshell/"
description: "WMShell – window-manager shell widget from the X toolkit"
---

<p>WMShell &#8211; window-manager shell widget from the X toolkit</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/Shell.h">X11/Shell.h</a>&gt;</code></p>
<h2>Description</h2>
<p>WMShell is a widget which is defined in the X Toolkit. We document its existence here for completeness. Please refer to the X Window System documentation for the real information regarding this widget.</p>
<h2>X Resources</h2>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Type</td>
<td>Default</td>
<td>Access
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XtNtitle</td>
<td>XtCTitle</td>
<td>String</td>
<td>(null)</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNtitleEncoding</td>
<td>XtCTitleEncoding</td>
<td>Atom</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwmTimeout</td>
<td>XtCWmTimeout</td>
<td>Int</td>
<td>5000</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwaitforwm</td>
<td>XtCWaitforwm</td>
<td>Boolean</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNtransient</td>
<td>XtCTransient</td>
<td>Boolean</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNbaseWidth</td>
<td>XtCBaseWidth</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNbaseHeight</td>
<td>XtCBaseHeight</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwinGravity</td>
<td>XtCWinGravity</td>
<td>Gravity</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNminWidth</td>
<td>XtCMinWidth</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNminHeight</td>
<td>XtCMinHeight</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNmaxWidth</td>
<td>XtCMaxWidth</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNmaxHeight</td>
<td>XtCMaxHeight</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwidthInc</td>
<td>XtCWidthInc</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNheightInc</td>
<td>XtCHeightInc</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNminAspectX</td>
<td>XtCMinAspectX</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNminAspectY</td>
<td>XtCMinAspectY</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNmaxAspectX</td>
<td>XtCMaxAspectX</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNmaxAspectY</td>
<td>XtCMaxAspectY</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNinput</td>
<td>XtCInput</td>
<td>Bool</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNinitialState</td>
<td>XtCInitialState</td>
<td>InitialState</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNiconPixmap</td>
<td>XtCIconPixmap</td>
<td>Bitmap</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNiconWindow</td>
<td>XtCIconWindow</td>
<td>Window</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNiconX</td>
<td>XtCIconX</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNiconY</td>
<td>XtCIconY</td>
<td>Int</td>
<td>135884268</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNiconMask</td>
<td>XtCIconMask</td>
<td>Bitmap</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwindowGroup</td>
<td>XtCWindowGroup</td>
<td>Window</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNclientLeader</td>
<td>XtCClientLeader</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNwindowRole</td>
<td>XtCWindowRole</td>
<td>String</td>
<td>(null)</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XtNurgency</td>
<td>XtCUrgency</td>
<td>Boolean</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
</table>
<p> <code>XtNtitle</code> </p>
<p> <code>XtNtitleEncoding</code> </p>
<p> <code>XtNwmTimeout</code> </p>
<p> <code>XtNwaitforwm</code> </p>
<p> <code>XtNtransient</code> </p>
<p> <code>XtNbaseWidth</code> </p>
<p> <code>XtNbaseHeight</code> </p>
<p> <code>XtNwinGravity</code> </p>
<p> <code>XtNminWidth</code> </p>
<p> <code>XtNminHeight</code> </p>
<p> <code>XtNmaxWidth</code> </p>
<p> <code>XtNmaxHeight</code> </p>
<p> <code>XtNwidthInc</code> </p>
<p> <code>XtNheightInc</code> </p>
<p> <code>XtNminAspectX</code> </p>
<p> <code>XtNminAspectY</code> </p>
<p> <code>XtNmaxAspectX</code> </p>
<p> <code>XtNmaxAspectY</code> </p>
<p> <code>XtNinput</code> </p>
<p> <code>XtNinitialState</code> </p>
<p> <code>XtNiconPixmap</code> </p>
<p> <code>XtNiconWindow</code> </p>
<p> <code>XtNiconX</code> </p>
<p> <code>XtNiconY</code> </p>
<p> <code>XtNiconMask</code> </p>
<p> <code>XtNwindowGroup</code> </p>
<p> <code>XtNclientLeader</code> </p>
<p> <code>XtNwindowRole</code> </p>
<p> <code>XtNurgency</code> </p>
<h2>Class Hierarchy</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3) <code><a href="/docs/linux/man/3-rect/">Rect</a></code>(3) <code><a href="/docs/linux/man/3-unnamedobj/">UnNamedObj</a></code>(3) <code><a href="/docs/linux/man/3-core/">Core</a></code>(3) <code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3) <code><a href="/docs/linux/man/3-shell/">Shell</a></code>(3) <code><a href="/docs/linux/man/3-wmshell/">WMShell</a></code>(3)</p>
<h2>Callbacks</h2>
<h2>Convenience Functions</h2>
<h2>See Also</h2>
