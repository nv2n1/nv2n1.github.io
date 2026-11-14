---
title: "xputbackevent(3)"
name: "xputbackevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xputbackevent/"
description: "XPutBackEvent – put events back on the queue"
---

<p>XPutBackEvent &#8211; put events back on the queue </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XPutBackEvent(Display *<i>display</i>, XEvent *<i>event</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event</i></p>
<dd>Specifies the event.</dl>
<h2>Description</h2>
<p>The <code>XPutBackEvent</code> function pushes an event back onto the head of the display&#8217;s event queue by copying the event into the queue. This can be useful if you read an event and then decide that you would rather deal with it later. There is no limit to the number of times in succession that you can call <code>XPutBackEvent</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xifevent/">XIfEvent</a>(3), <a href="/docs/linux/man/3-xnextevent/">XNextEvent</a>(3), <a href="/docs/linux/man/3-xsendevent/">XSendEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
