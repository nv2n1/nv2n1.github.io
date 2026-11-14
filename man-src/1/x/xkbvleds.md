---
title: "xkbvleds(1)"
name: "xkbvleds"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbvleds/"
description: "xkbvleds – XKB extension user utility"
---

<h2 class="name">NAME</h2>
<p> xkbvleds &#8211; XKB extension user utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xkbvleds</code> [-indpy &lt;name&gt;] [-watch &lt;leds&gt;] [[-+]automatic] [[-+]explicit] [[-+]name] [[-+]real] [[-+]virtual] [-intersection] [-union]</p>
<h2>DESCRIPTION</h2>
<p> This program is used to display the state of LEDs on an XKB keyboard. It reports the changes in the fundamental components of the XKB state which includes the effective compatibility state. The default set of LEDs is -union +name +automatic +real.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-indpy &lt;name&gt;</code></p>
<dd> Mask of LEDs to watch</p>
<dt><code>-watch &lt;leds&gt;</code></p>
<dd> turn on synchronization</dl>
<dl>
<dt><code>-+automatic</code></p>
<dd> (Don&#8217;t) watch automatic LEDs</dl>
<dl>
<dt><code>-+explicit</code></p>
<dd> (Don&#8217;t) watch explicit LEDs</dl>
<dl>
<dt><code>-+name</code></p>
<dd> (Don&#8217;t) watch named LEDs</dl>
<dl>
<dt><code>-+real</code></p>
<dd> (Don&#8217;t) watch real LEDs</dl>
<dl>
<dt><code>-+virtual</code></p>
<dd> (Don&#8217;t) watch virtual LEDs</dl>
<dl>
<dt><code>-intersection</code></p>
<dd> Watch only LEDs in all desired sets</dl>
<dl>
<dt><code>-union</code></p>
<dd> Watch LEDs in any desired sets</dl>
<dl>
<dt><code>-help</code></p>
<dd> print list of options and exit</dl>
<dl>
<dt><code>-version</code></p>
<dd> print program version and exit </p>
</dl>
<h2>Index</h2>
