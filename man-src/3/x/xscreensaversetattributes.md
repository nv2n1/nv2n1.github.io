---
title: "xscreensaversetattributes(3)"
name: "xscreensaversetattributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xscreensaversetattributes/"
description: "XScreenSaver – X11 Screen Saver extension client library"
---

<p>XScreenSaver &#8211; X11 Screen Saver extension client library</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/scrnsaver.h&gt;</code> </p>
<pre>typedef struct {
 Window window; /* screen saver window */
 int state; /* ScreenSaver{Off,On,Disabled} */
 int kind; /* ScreenSaver{Blanked,Internal,External} */
 unsigned long til_or_since; /* milliseconds */
 unsigned long idle; /* milliseconds */
 unsigned long eventMask; /* events */
<br>
} XScreenSaverInfo;
typedef struct {
 int type; /* of event */
 unsigned long serial; /* # of last request processed by server */
 Bool send_event; /* true if this came frome a SendEvent request */
 Display *display; /* Display the event was read from */
 Window window; /* screen saver window */
 Window root; /* root window of event screen */
 int state; /* ScreenSaver{Off,On,Cycle} */
 int kind; /* ScreenSaver{Blanked,Internal,External} */
 Bool forced; /* extents of new region */
 Time time; /* event timestamp */
<br>
} XScreenSaverNotifyEvent;</pre>
<dl COMPACT>
<dd>Bool XScreenSaverQueryExtension(Display *<i>dpy</i>, int *<i>event_base_return</i>, int *<i>error_base_return</i>);</p>
<dd>Status XScreenSaverQueryVersion(Display *<i>dpy</i>, int *<i>major_version_return</i>, int *<i>minor_version_return</i>);</p>
<dd>XScreenSaverInfo *XScreenSaverAllocInfo(void);</p>
<dd>Status XScreenSaverQueryInfo(Display *<i>dpy</i>, Drawable <i>drawable</i>, XScreenSaverInfo *<i>saver_info</i>);</p>
<dd>void XScreenSaverSelectInput(Display *<i>dpy</i>, Drawable <i>drawable</i>, unsigned long <i>mask</i>);</p>
<dd>void XScreenSaverSetAttributes(Display *<i>dpy</i>, Drawable <i>drawable</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int <i>border_width</i>, int <i>depth</i>, unsigned int <i>class</i>, Visual *<i>visual</i>, unsigned long <i>valuemask</i>, XSetWindowAttributes *<i>attributes</i>);</p>
<dd>void XScreenSaverUnsetAttributes(Display *<i>dpy</i>, Drawable <i>drawable</i>);</p>
<dd>void XScreenSaverSaverRegister(Display *<i>dpy</i>, int <i>screen</i>, XID <i>xid</i>, Atom <i>type</i>);</p>
<dd>Status XScreenSaverUnregister(Display *<i>dpy</i>, int <i>screen</i>);</p>
<dd>Status XScreenSaverGetRegistered(Display *<i>dpy</i>, int <i>screen</i>, XID *<i>xid</i>, Atom *<i>type</i>);</p>
<dd>void XScreenSaverSuspend(Display *<i>dpy</i>, Bool <i>suspend</i>);</dl>
<h2>Description</h2>
<p>The X Window System provides support for changing the image on a display screen after a user-settable period of inactivity to avoid burning the cathode ray tube phosphors. However, no interfaces are provided for the user to control the image that is drawn. This extension allows an external &#8220;screen saver&#8221; client to detect when the alternate image is to be displayed and to provide the graphics. </p>
<p> Current X server implementations typically provide at least one form of &#8220;screen saver&#8221; image. Historically, this has been a copy of the X logo drawn against the root background pattern. However, many users have asked for the mechanism to allow them to write screen saver programs that provide capabilities similar to those provided by other window systems. In particular, such users often wish to be able to display corporate logos, instructions on how to reactivate the screen, and automatic screen-locking utilities. This extension provides a means for writing such clients.</p>
<h3>Assumptions</h3>
<p>This extension exports the notion of a special screen saver window that is mapped above all other windows on a display. This window has the <i>override-redirect</i> attribute set so that it is not subject to manipulation by the window manager. Furthermore, the X identifier for the window is never returned by <code>QueryTree</code> requests on the root window, so it is typically not visible to other clients. </p>
<p> <code>XScreenSaverQueryExtension</code> returns <code>True</code> if the <i>XScreenSaver</i> extension is available on the given display. A client must call <code>XScreenSaverQueryExtension</code> before calling any other XScreenSaver function in order to negotiate a compatible protocol version; otherwise the client will get undefined behavior (XScreenSaver may or may not work). </p>
<p> If the extension is supported, the event number for <i>ScreenSaverNotify</i> events is returned in the value pointed to by <i>event_base</i>. Since no additional errors are defined by this extension, the results of <i>error_base</i> are not defined. </p>
<p> <code>XScreenSaverQueryVersion</code> returns <code>True</code> if the request succeeded; the values of the major and minor protocol versions supported by the server are returned in <i>major_version_return</i> and <i>minor_version_return .</i> </p>
<p> <code>XScreenSaverAllocInfo</code> allocates and returns an <code>XScreenSaverInfo</code> structure for use in calls to <code>XScreenSaverQueryInfo</code>. All fields in the structure are initialized to zero. If insufficient memory is available, NULL is returned. The results of this routine can be released using <i>XFree</i>. </p>
<p> <code>XScreenSaverQueryInfo</code> returns information about the current state of the screen server in <i>saver_info</i> and a non-zero value is returned. If the extension is not supported, <i>saver_info</i> is not changed and 0 is returned. </p>
<p> The <i>state</i> field specifies whether or not the screen saver is currently active and how the <i>til-or-since</i> value should be interpreted:</p>
<dl COMPACT>
<dt><i>Off</i></p>
<dd>The screen is not currently being saved; <i>til-or-since</i> specifies the number of milliseconds until the screen saver is expected to activate.</p>
<dt><i>On</i></p>
<dd>The screen is currently being saved; <i>til-or-since</i> specifies the number of milliseconds since the screen saver activated.</p>
<dt><i>Disabled</i></p>
<dd>The screen saver is currently disabled; <i>til-or-since</i> is zero.</dl>
<p> The <i>kind</i> field specifies the mechanism that either is currently being used or would have been were the screen being saved:</p>
<dl COMPACT>
<dt><i>Blanked</i></p>
<dd>The video signal to the display monitor was disabled.</p>
<dt><i>Internal</i></p>
<dd>A server-dependent, built-in screen saver image was displayed; either no client had set the screen saver window attributes or a different client had the server grabbed when the screen saver activated.</p>
<dt><i>External</i></p>
<dd>The screen saver window was mapped with attributes set by a client using the <code>ScreenSaverSetAttributes</code> request.</dl>
<p> The <i>idle</i> field specifies the number of milliseconds since the last input was received from the user on any of the input devices.<br />
 The <i>event-mask</i> field specifies which, if any, screen saver events this client has requested using <code>ScreenSaverSelectInput</code>. </p>
<p> <code>XScreenSaverSelectInput</code> asks that events related to the screen saver be generated for this client. If no bits are set in <i>event-mask</i>, then no events will be generated. Otherwise, any combination of the following bits may be set:</p>
<dl COMPACT>
<dt><code>ScreenSaverNotify</code></p>
<dd>If this bit is set, <code>ScreenSaverNotify</code> events are generated whenever the screen saver is activated or deactivated.</p>
<dt><code>ScreenSaverCycle</code></p>
<dd>If this bit is set, <code>ScreenSaverNotify</code> events are generated whenever the screen saver cycle interval passes.</dl>
<p> <code>XScreenSaverSetAttributes</code> sets the attributes to be used the next time the external screen saver is activated. If another client currently has the attributes set, a BadAccess error is generated and the request is ignored.<br />
 Otherwise, the specified window attributes are checked as if they were used in a core <code>CreateWindow</code> request whose parent is the root. The <i>override-redirect</i> field is ignored as it is implicitly set to True. If the window attributes result in an error according to the rules for <code>CreateWindow</code>, the request is ignored.<br />
 Otherwise, the attributes are stored and will take effect on the next activation that occurs when the server is not grabbed by another client. Any resources specified for the <i>background-pixmap</i> or <i>cursor</i> attributes may be freed immediately. The server is free to copy the <i>background-pixmap</i> or <i>cursor</i> resources or to use them in place; therefore, the effect of changing the contents of those resources is undefined. If the specified <i>colormap</i> no longer exists when the screen saver activates, the parent&#8217;s colormap is used instead. If no errors are generated by this request, any previous screen saver window attributes set by this client are released.<br />
 When the screen saver next activates and the server is not grabbed by another client, the screen saver window is created, if necessary, and set to the specified attributes and events are generated as usual. The colormap associated with the screen saver window is installed. Finally, the screen saver window is mapped.<br />
 The window remains mapped and at the top of the stacking order until the screen saver is deactivated in response to activity on any of the user input devices, a <code>ForceScreenSaver</code> request with a value of Reset, or any request that would cause the window to be unmapped.<br />
 If the screen saver activates while the server is grabbed by another client, the internal saver mechanism is used. The <code>ForceScreenSaver</code> request may be used with a value of Active to deactivate the internal saver and activate the external saver.<br />
 If the screen saver client&#8217;s connection to the server is broken while the screen saver is activated and the client&#8217;s close down mode has not been RetainPermanent or RetainTemporary, the current screen saver is deactivated and the internal screen saver is immediately activated.<br />
 When the screen saver deactivates, the screen saver window&#8217;s colormap is uninstalled and the window is unmapped (except as described below). The screen saver XID is disassociated with the window and the server may, but is not required to, destroy the window along with any children.<br />
 When the screen saver is being deactivated and then immediately reactivated (such as when switching screen savers), the server may leave the screen saver window mapped (typically to avoid generating exposures). </p>
<p> <code>XScreenSaverUnsetAttributes</code> instructs the server to discard any previous screen saver window attributes set by this client. </p>
<p> <code>XScreenSaverRegister</code> stores the given <i>XID</i> in the <code>_SCREEN_SAVER_ID</code> property (of the given <i>type</i>) on the root window of the specified <i>screen</i>. It returns zero if an error is encountered and the property is not changed, otherwise it returns non-zero. </p>
<p> <code>XScreenSaverUnregister</code> removes any <code>_SCREEN_SAVER_ID</code> from the root window of the specified <i>screen</i>. It returns zero if an error is encountered and the property is changed, otherwise it returns non-zero. </p>
<p> <code>XScreenSaverGetRegistered</code> returns the <i>XID</i> and <i>type</i> stored in the <code>_SCREEN_SAVER_ID</code> property on the root window of the specified <i>screen</i>. It returns zero if an error is encountered or if the property does not exist or is not of the correct format; otherwise it returns non-zero. </p>
<p> <code>XScreenSaverSuspend</code> temporarily suspends the screensaver and DPMS timer if <i>suspend</i> is &#8216;True&#8217;, and restarts the timer if <i>suspend</i> is &#8216;False&#8217;.<br />
 This function should be used by applications that don&#8217;t want the screensaver or DPMS to become activated while they&#8217;re for example in the process of playing a media sequence, or are otherwise continuously presenting visual information to the user while in a non-interactive state. This function is not intended to be called by an external screensaver application.<br />
 If <code>XScreenSaverSuspend</code> is called multiple times with <i>suspend</i> set to &#8216;True&#8217;, it must be called an equal number of times with <i>suspend</i> set to &#8216;False&#8217; in order for the screensaver timer to be restarted. This request has no affect if a client tries to resume the screensaver without first having suspended it. <code>XScreenSaverSuspend</code> can thus not be used by one client to resume the screensaver if it&#8217;s been suspended by another client.<br />
 If a client that has suspended the screensaver becomes disconnected from the X server, the screensaver timer will automatically be restarted, unless it&#8217;s still suspended by another client. Suspending the screensaver timer doesn&#8217;t prevent the screensaver from being forceably activated with the <code>ForceScreenSaver</code> request, or a DPMS mode from being set with the <code>DPMSForceLevel</code> request.<br />
 <code>XScreenSaverSuspend</code> also doesn&#8217;t deactivate the screensaver or DPMS if either is active at the time the request to suspend them is received by the X server. But once they&#8217;ve been deactivated, they won&#8217;t automatically be activated again, until the client has canceled the suspension.</p>
<h2>Errors</h2>
<p><code>XScreenSaverSelectInput,</code> <code>XScreenSaverQueryInfo,</code> <code>XScreenSaverSetAttributes</code> and <code>XScreenSaverUnsetAttributes</code> will generate a <i>BadDrawable</i> error if <i>drawable</i> is not a valid drawable identifier. If any undefined bits are set in <i>event-mask</i>, a BadValue error is generated by <code>XScreenSaverSelectInput .</code> </p>
<h2>Availability</h2>
<p><code>XScreenSaverSuspend</code> is available in version 1.1 and later versions of the X Screen Saver Extension. Version 1.1 was first released with X11R7.1. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>Authors</h2>
<p>Jim Fulton and Keith Packard.</p>
<h2>Stability</h2>
<p>This API is considered as experimental. The Xss library major revision may be incremented whenever incompatible changes are done to the API without notice. Use with care.</p>
