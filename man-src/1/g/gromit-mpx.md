---
title: "gromit-mpx(1)"
name: "gromit-mpx"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gromit-mpx/"
description: "Gromit-MPX – Presentation helper to make annotations on screen"
---

<h2 class="name">NAME</h2>
<p> Gromit-MPX &#8211; Presentation helper to make annotations on screen </p>
<h2>SYNOPSIS</h2>
<p> <code>gromit-mpx</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Gromit-MPX</code> enables you to make multi-pointer annotations on your screen. It can run in the background and be activated on demand to let you draw over all your currently running applications. The drawing will stay on screen as long as you want, you can continue to use your applications while the drawing is visible.<br />
 <code>Gromit-MPX</code> is XInput-Aware, so if you have a graphic tablet you can draw lines with different strength, colour, erase things, etc.<br />
 Since you typically want to use the program you are demonstrating and highlighting something is a short interruption of you workflow, Gromit-MPX is activated by either a hotkey or a repeated invocation of Gromit-MPX (the latter can e.g. used by other applications or your windowmanager). </p>
<h2>KEYBOARD CONTROL</h2>
<p> By default, Gromit-MPX grabs the &quot;F9&quot; key (this can be changed using the &quot;&#8211;key&quot; option), making it unavailable to other application. The available shortcuts are:</p>
<dl>
<dt><code>F9</code></p>
<dd> toggle painting</p>
<dt><code>SHIFT-F9</code></p>
<dd> clear screen</p>
<dt><code>CTRL-F9</code></p>
<dd> toggle visibility</p>
<dt><code>ALT-F9</code></p>
<dd> quit Gromit-MPX</dl>
<h2>OPTIONS (STARTUP)</h2>
<p> A short summary of the available commandline arguments for invoking Gromit-MPX, see below for the options to control an already running Gromit-MPX process:</p>
<dl>
<dt><code>-a, &#8211;active</code></p>
<dd> start Gromit-MPX and immediately activate it.</p>
<dt><code>-k &lt;keysym&gt;, &#8211;key &lt;keysym&gt;</code></p>
<dd> will change the key used to grab the mouse. &lt;keysym&gt; can e.g. be &quot;F9&quot;, &quot;F12&quot;, &quot;Control_R&quot; or &quot;Print&quot;. To determine the keysym for different keys you can use the <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1) command. You can specify &quot;none&quot; to prevent Gromit-MPX from grabbing a key.</p>
<dt><code>-K &lt;keycode&gt;, &#8211;keycode &lt;keycode&gt;</code></p>
<dd> will change the key used to grab the mouse. Under rare circumstances identifying the key with the keysym can fail. You can then use the keycode to specify the key uniquely. To determine the keycode for different keys you can use the <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1) command.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> gives some debug output.</dl>
<h2>OPTIONS (CONTROL)</h2>
<p> A sort summary of the available commandline arguments to control an already running Gromit-MPX process, see above for the options available to start Gromit-MPX.</p>
<dl>
<dt><code>-q, &#8211;quit</code></p>
<dd> will cause the main Gromit-MPX process to quit.</p>
<dt><code>-t, &#8211;toggle</code></p>
<dd> will toggle the grabbing of the cursor.</p>
<dt><code>-v, &#8211;visibility</code></p>
<dd> will toggle the visibility of the window.</p>
<dt><code>-c, &#8211;clear</code></p>
<dd> will clear the screen.</dl>
<h2>BUGS</h2>
<p> When there is no compositing manager such as Compiz or xcompmgr running, Gromit-MPX falls back to a legacy drawing mode. This may drastically slow down your X-Server, especially when you draw very thin lines. It makes heavy use of the shape extension, which is quite expensive if you paint a complex pattern on screen. Especially terminal-programs tend to scroll incredibly slow if something is painted over their window.</p>
<h2>AUTHORS</h2>
<p> Simon Budig &lt;simon [at] gimp.org&gt; Christian Beier &lt;dontmind [at] freeshell.org&gt; </p>
<p> This manual page was written by Pierre Chifflier &lt;chifflier [at] cpe.fr&gt; and Simon Budig for the original Gromit and extended for Gromit-MPX by Christian Beier. </p>
<h2>Index</h2>
