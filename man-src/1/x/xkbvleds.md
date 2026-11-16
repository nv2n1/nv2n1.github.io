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
<dt><code>-indpy &lt;name&gt;</code></dt>
<dd> Mask of LEDs to watch</dd>
<dt><code>-watch &lt;leds&gt;</code></dt>
<dd> turn on synchronization</dd></dl>
<dl>
<dt><code>-+automatic</code></dt>
<dd> (Don&#8217;t) watch automatic LEDs</dd></dl>
<dl>
<dt><code>-+explicit</code></dt>
<dd> (Don&#8217;t) watch explicit LEDs</dd></dl>
<dl>
<dt><code>-+name</code></dt>
<dd> (Don&#8217;t) watch named LEDs</dd></dl>
<dl>
<dt><code>-+real</code></dt>
<dd> (Don&#8217;t) watch real LEDs</dd></dl>
<dl>
<dt><code>-+virtual</code></dt>
<dd> (Don&#8217;t) watch virtual LEDs</dd></dl>
<dl>
<dt><code>-intersection</code></dt>
<dd> Watch only LEDs in all desired sets</dd></dl>
<dl>
<dt><code>-union</code></dt>
<dd> Watch LEDs in any desired sets</dd></dl>
<dl>
<dt><code>-help</code></dt>
<dd> print list of options and exit</dd></dl>
<dl>
<dt><code>-version</code></dt>
<dd> print program version and exit </dd>
</dl>
<h2>Index</h2>
