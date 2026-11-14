---
title: "oclock(1)"
name: "oclock"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oclock/"
description: "oclock – round X clock"
---

<h2 class="name">NAME</h2>
<p> oclock &#8211; round X clock </p>
<h2>SYNOPSIS</h2>
<p> <code>oclock</code> [-option &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Oclock</i> simply displays the current time on an analog display.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fg </code><i>color</i></p>
<dd> choose a different color for the both hands and the jewel of the clock</p>
<dt><code>-bg </code><i>color</i></p>
<dd> choose a different color for the background.</p>
<dt><code>-jewel </code><i>color</i></p>
<dd> choose a different color for the jewel on the clock.</p>
<dt><code>-minute </code><i>color</i></p>
<dd> choose a different color for the minute hand of the clock.</p>
<dt><code>-hour </code><i>color</i></p>
<dd> choose a different color for the hour hand of the clock.</p>
<dt><code>-backing </code><i>{ WhenMapped Always NotUseful }</i></p>
<dd> selects an appropriate level of backing store.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> define the initial window geometry; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</p>
<dt><code>-display </code><i>display</i></p>
<dd> specify the display to use; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</p>
<dt><code>-bd </code><i>color</i></p>
<dd> choose a different color for the window border.</p>
<dt><code>-bw </code><i>width</i></p>
<dd> choose a different width for the window border. As the Clock widget changes its border around quite a bit, this is most usefully set to zero.</p>
<dt><code>-shape</code></p>
<dd> causes the clock to use the Shape extension to create an oval window. This is the default unless the shapeWindow resource is set to false.</p>
<dt><code>-noshape</code></p>
<dd> causes the clock to not reshape itself and ancestors to exactly fit the outline of the clock.</p>
<dt><code>-transparent</code></p>
<dd> causes the clock to consist only of the jewel, the hands, and the border.</dl>
<h2>COLORS</h2>
<p> If you would like your clock to be viewable in color, include the following in the #ifdef COLOR section you read with xrdb: </p>
<p> *customization: -color </p>
<p> This will cause oclock to pick up the colors in the app-defaults color customization file: /usr/lib/X11/app-defaults/Clock-color. Below are the default colors: </p>
<p> Clock*Background: grey<br />
 Clock*BorderColor: light blue<br />
 Clock*hour: yellow<br />
 Clock*jewel: yellow<br />
 Clock*minute: yellow</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), X Toolkit documentation</p>
<h2>AUTHOR</h2>
<p> Keith Packard, MIT X Consortium </p>
<h2>Index</h2>
