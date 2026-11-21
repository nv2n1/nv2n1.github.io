---

title: "xeyes(1)"
name: "xeyes"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xeyes/"
description: "xeyes – a follow the mouse X demo"
---

<p> xeyes &#8211; a follow the mouse X demo </p>
<h2>SYNOPSIS</h2>
<p> <code>xeyes</code> [-option &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xeyes</i> watches what you do and reports to the Boss.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fg </code><i>foreground color</i></dt>
<dd> choose a different color for the pupil of the eyes.</dd>
<dt><code>-bg </code><i>background color</i></dt>
<dd> choose a different color for the background.</dd>
<dt><code>-outline </code><i>outline color</i></dt>
<dd> choose a different color for the outline of the eyes.</dd>
<dt><code>-center </code><i>center color</i></dt>
<dd> choose a different color for the center of the eyes.</dd>
<dt><code>-backing </code><i>{ WhenMapped Always NotUseful }</i></dt>
<dd> selects an appropriate level of backing store.</dd>
<dt><code>-geometry </code><i>geometry</i></dt>
<dd> define the initial window geometry; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dd>
<dt><code>-display </code><i>display</i></dt>
<dd> specify the display to use; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dd>
<dt><code>-bd </code><i>border color</i></dt>
<dd> choose a different color for the window border.</dd>
<dt><code>-bw </code><i>border width</i></dt>
<dd> choose a different width for the window border.</dd>
<dt><code>-shape</code></dt>
<dd> uses the SHAPE extension to shape the window. This is the default.</dd>
<dt><code>+shape</code></dt>
<dd> disables use of the SHAPE extension to shape the window.</dd>
<dt><code>-render</code></dt>
<dd> uses Xrender to draw anti-aliased eyes. This is the default if <i>xeyes</i> has been compiled with Xrender support.</dd>
<dt><code>+render</code></dt>
<dd> disables Xrender and draws traditional eyes.</dd>
<dt><code>-distance</code></dt>
<dd> uses an alternative mapping, as if the eyes were set back from the screen, thus following the mouse more precisely.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), X Toolkit documentation<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Keith Packard, MIT X Consortium<br />
 Copied from the NeWS version written (apparently) by Jeremy Huxtable as seen at SIGGRAPH &#8217;88 </p>
