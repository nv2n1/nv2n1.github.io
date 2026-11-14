---
title: "xpp_blink(8)"
name: "xpp_blink"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xpp_blink/"
---

xpp_blink - Blink the leds of a specified XPD

<h2>Synopsis</h2>

xpp_blink {on|off|bzzt} {span &lt;number&gt; | chan &lt;number&gt; | xpd &lt;bus num&gt; [&lt;xpd num&gt; [&lt;lineno&gt;]]}

<h2>Description</h2>

Blink all the leds of an <font SIZE="-1">XPD</font>.

<h2>Blink mode:</h2>

<dl><dt>on
<dd>Turn on constant blink
<dt>off
<dd>Turn off blink
<dt>bzzt
<dd>Blink briefly for 1 second.</dl>

<h2>Selector:</h2>

<dl><dt>span
<dd>Select by span number. This only work for <font SIZE="-1">XPD</font> registered to dahdi. 

 will also print the dahdi channels of the span and the xbus/xpd this span represents.
<dt>chan
<dd>Select by channel number. This only work for <font SIZE="-1">XPD</font> registered to dahdi.
<dt>xpd
<dd>Select by xbus + xpd numbers. If only xbus number is given, all the XPDs of the selected xbus (Astribank) are blinked.
<dt>label
<dd>Select by xbus label. Affect the whole Astribank.</dl>

<h2>Examples</h2>

<pre> $ xpp_blink bzzt span 2
 Using XBUS-04/XPD-10 (connected via usb-0000:00:1d.7-1): channels 15 16 17 18 19 20 21 22
 $ xpp_blink bzzt chan 18
 $ xpp_blink on xpd 0 1 5
 $ xpp_blink off xpd 0
 $ xpp_blink bzzt label 'usb:00000238'</pre>
