---
title: "xanyevent(3)"
name: "xanyevent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xanyevent/"
description: "XAnyEvent, XEvent – generic X event structures"
---

<p>XAnyEvent, XEvent &#8211; generic X event structures </p>
<h2>Structures</h2>
<p>All the event structures declared in have the following common members: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long serial;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of last request processed by server&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool send_event;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;true if this came from a SendEvent request&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Display&nbsp;*display;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Display the event was read from&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window window; } XAnyEvent; </p>
<p> The type member is set to the event type constant name that uniquely identifies it. For example, when the X server reports a <code>GraphicsExpose</code> event to a client application, it sends an <code>XGraphicsExposeEvent</code> structure with the type member set to <code>GraphicsExpose</code>. The display member is set to a pointer to the display the event was read on. The send_event member is set to <code>True</code> if the event came from a <code>SendEvent</code> protocol request. The serial member is set from the serial number reported in the protocol but expanded from the 16-bit least-significant bits to a full 32-bit value. The window member is set to the window that is most useful to toolkit dispatchers. </p>
<p> The <code>XEvent</code> structure is a union of the individual structures declared for each event type: typedef union _XEvent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;must not be changed&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XAnyEvent xany;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XKeyEvent xkey;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XButtonEvent xbutton;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XMotionEvent xmotion;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XCrossingEvent xcrossing;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XFocusChangeEvent xfocus;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XExposeEvent xexpose;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XGraphicsExposeEvent xgraphicsexpose;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XNoExposeEvent xnoexpose;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XVisibilityEvent xvisibility;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XCreateWindowEvent xcreatewindow;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XDestroyWindowEvent xdestroywindow;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XUnmapEvent xunmap;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XMapEvent xmap;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XMapRequestEvent xmaprequest;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XReparentEvent xreparent;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XConfigureEvent xconfigure;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XGravityEvent xgravity;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XResizeRequestEvent xresizerequest;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XConfigureRequestEvent xconfigurerequest;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XCirculateEvent xcirculate;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XCirculateRequestEvent xcirculaterequest;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XPropertyEvent xproperty;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XSelectionClearEvent xselectionclear;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XSelectionRequestEvent xselectionrequest;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XSelectionEvent xselection;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XColormapEvent xcolormap;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XClientMessageEvent xclient;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XMappingEvent xmapping;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XErrorEvent xerror;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XKeymapEvent xkeymap;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long pad[24]; } XEvent; </p>
<p> An <code>XEvent</code> structure&#8217;s first entry always is the type member, which is set to the event type. The second member always is the serial number of the protocol request that generated the event. The third member always is send_event, which is a <code>Bool</code> that indicates if the event was sent by a different client. The fourth member always is a display, which is the display that the event was read from. Except for keymap events, the fifth member always is a window, which has been carefully selected to be useful to toolkit dispatchers. To avoid breaking toolkits, the order of these first five entries is not to change. Most events also contain a time member, which is the time at which an event occurred. In addition, a pointer to the generic event must be cast before it is used to access any other information in the structure.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xbuttonevent/">XButtonEvent</a>(3), <a href="/docs/linux/man/3-xcreatewindowevent/">XCreateWindowEvent</a>(3), <a href="/docs/linux/man/3-xcirculateevent/">XCirculateEvent</a>(3), <a href="/docs/linux/man/3-xcirculaterequestevent/">XCirculateRequestEvent</a>(3), <a href="/docs/linux/man/3-xcolormapevent/">XColormapEvent</a>(3), <a href="/docs/linux/man/3-xconfigureevent/">XConfigureEvent</a>(3), <a href="/docs/linux/man/3-xconfigurerequestevent/">XConfigureRequestEvent</a>(3), <a href="/docs/linux/man/3-xcrossingevent/">XCrossingEvent</a>(3), <a href="/docs/linux/man/3-xdestroywindowevent/">XDestroyWindowEvent</a>(3), <a href="/docs/linux/man/3-xerrorevent/">XErrorEvent</a>(3), <a href="/docs/linux/man/3-xexposeevent/">XExposeEvent</a>(3), <a href="/docs/linux/man/3-xfocuschangeevent/">XFocusChangeEvent</a>(3), <a href="/docs/linux/man/3-xgraphicsexposeevent/">XGraphicsExposeEvent</a>(3), <a href="/docs/linux/man/3-xgravityevent/">XGravityEvent</a>(3), <a href="/docs/linux/man/3-xkeymapevent/">XKeymapEvent</a>(3), <a href="/docs/linux/man/3-xmapevent/">XMapEvent</a>(3), <a href="/docs/linux/man/3-xmaprequestevent/">XMapRequestEvent</a>(3), <a href="/docs/linux/man/3-xpropertyevent/">XPropertyEvent</a>(3), <a href="/docs/linux/man/3-xreparentevent/">XReparentEvent</a>(3), <a href="/docs/linux/man/3-xresizerequestevent/">XResizeRequestEvent</a>(3), <a href="/docs/linux/man/3-xselectionclearevent/">XSelectionClearEvent</a>(3), <a href="/docs/linux/man/3-xselectionevent/">XSelectionEvent</a>(3), <a href="/docs/linux/man/3-xselectionrequestevent/">XSelectionRequestEvent</a>(3), <a href="/docs/linux/man/3-xunmapevent/">XUnmapEvent</a>(3), <a href="/docs/linux/man/3-xvisibilityevent/">XVisibilityEvent</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
