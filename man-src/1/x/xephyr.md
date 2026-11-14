---
title: "xephyr(1)"
name: "xephyr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xephyr/"
description: "Xephyr – X server outputting to a window on a pre-existing X display"
---

<p>Xephyr &#8211; X server outputting to a window on a pre-existing X display </p>
<h2>Synopsis</h2>
<p><code>Xephyr</code> [<code>:</code><i>display</i>] [<i>option</i> <i>&#8230;</i>]</p>
<h2>Description</h2>
<p><code>Xephyr</code> is a kdrive server that outputs to a window on a pre-existing &quot;host&quot; X display. Think <i>Xnest</i> but with support for modern extensions like composite, damage and randr. </p>
<p> Unlike <i>Xnest</i> which is an X proxy, i.e. limited to the capabilities of the host X server, <code>Xephyr</code> is a real X server which uses the host X server window as &quot;framebuffer&quot; via fast SHM XImages. </p>
<p> It also has support for &quot;visually&quot; debugging what the server is painting.</p>
<h2>Options</h2>
<p>The server accepts all the standard options of <a href="/docs/linux/man/1-xserver/">Xserver</a>(1) and the following additional options:</p>
<dl>
<dt><code>-screen</code><i> width</i><code>x</code><i>height</i></p>
<dd>sets the screen size.</p>
<dt><code>-parent</code><i> id</i></p>
<dd>uses existing window <i>id .</i> If a <code>-screen</code> argument follows a <code>-parent</code> argument, this screen is embedded into the given window.</p>
<dt><code>-host-cursor</code></p>
<dd>set &#8216;cursor acceleration&#8217;: The host&#8217;s cursor is reused. This is only really there to aid debugging by avoiding server paints for the cursor. Performance improvement is negligible.</p>
<dt><code>-resizeable</code></p>
<dd>Allow the Xephyr window to be resized, even if not embedded into a parent window. By default, the Xephyr window has a fixed size.</p>
<dt><code>-no-host-grab</code></p>
<dd>Disable grabbing the keyboard and mouse.</dl>
<h2>Signals</h2>
<p>Send a SIGUSR1 to the server (e.g. pkill -USR1 Xephyr) to toggle the debugging mode. In this mode red rectangles are painted to screen areas getting painted before painting the actual content. The delay between this can be altered by setting a XEPHYR_PAUSE env var to a value in micro seconds.</p>
<h2>Caveats</h2>
<dl>
<dt>&bull;</p>
<dd>Rotated displays are currently updated via full blits. This is slower than a normal orientated display. Debug mode will therefore not be of much use rotated.</p>
<dt>&bull;</p>
<dd>The &#8216;-host-cursor&#8217; cursor is static in its appearance.</p>
<dt>&bull;</p>
<dd>The build gets a warning about &#8216;nanosleep&#8217;. I think the various &#8216;-D&#8217; build flags are causing this. I haven&#8217;t figured as yet how to work round it. It doesn&#8217;t appear to break anything however.</p>
<dt>&bull;</p>
<dd>Keyboard handling is basic but works.</p>
<dt>&bull;</p>
<dd>Mouse button 5 probably won&#8217;t work.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1)</p>
<h2>Author</h2>
<p>Matthew Allum &lt;mallum [at] o-hand.com&gt; 2004</p>
