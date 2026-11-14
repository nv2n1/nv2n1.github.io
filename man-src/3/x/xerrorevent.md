---
title: "xerrorevent(3)"
name: "xerrorevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xerrorevent/"
description: "XErrorEvent – X error event structure"
---

<p>XErrorEvent &#8211; X error event structure </p>
<h2>Structures</h2>
<p>The <code>XErrorEvent</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display the event was read from&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XID resourceid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;resource id&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;serial number of failed request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char error_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;error code of failed request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char request_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Major op-code of failed request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char minor_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Minor op-code of failed request&nbsp;*/ } XErrorEvent; </p>
<p> When you receive this event, the structure members are set as follows. </p>
<p> The serial member is the number of requests, starting from one, sent over the network connection since it was opened. It is the number that was the value of <code>NextRequest</code> immediately before the failing call was made. The request_code member is a protocol request of the procedure that failed, as defined in</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-xanyevent/">XAnyEvent</a>(3), <a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xcreatewindowevent/">XCreateWindowEvent</a>(3), <a href="/docs/linux/man/3-xcirculateevent/">XCirculateEvent</a>(3), <a href="/docs/linux/man/3-xcirculaterequestevent/">XCirculateRequestEvent</a>(3), <a href="/docs/linux/man/3-xcolormapevent/">XColormapEvent</a>(3), <a href="/docs/linux/man/3-xconfigureevent/">XConfigureEvent</a>(3), <a href="/docs/linux/man/3-xconfigurerequestevent/">XConfigureRequestEvent</a>(3), <a href="/docs/linux/man/3-xcrossingevent/">XCrossingEvent</a>(3), <a href="/docs/linux/man/3-xdestroywindowevent/">XDestroyWindowEvent</a>(3), <a href="/docs/linux/man/3-xexposeevent/">XExposeEvent</a>(3), <a href="/docs/linux/man/3-xfocuschangeevent/">XFocusChangeEvent</a>(3), <a href="/docs/linux/man/3-xgraphicsexposeevent/">XGraphicsExposeEvent</a>(3), <a href="/docs/linux/man/3-xgravityevent/">XGravityEvent</a>(3), <a href="/docs/linux/man/3-xkeymapevent/">XKeymapEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xmaprequestevent/">XMapRequestEvent</a>(3), <a href="/docs/linux/man/3-xpropertyevent/">XPropertyEvent</a>(3), <a href="/docs/linux/man/3-xreparentevent/">XReparentEvent</a>(3), <a href="/docs/linux/man/3-xresizerequestevent/">XResizeRequestEvent</a>(3), <a href="/docs/linux/man/3-xselectionclearevent/">XSelectionClearEvent</a>(3), <a href="/docs/linux/man/3-xselectionevent/">XSelectionEvent</a>(3), <a href="/docs/linux/man/3-xselectionrequestevent/">XSelectionRequestEvent</a>(3), <a href="/docs/linux/man/3-xunmapevent/">XUnmapEvent</a>(3), <a href="/docs/linux/man/3-xvisibilityevent/">XVisibilityEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
