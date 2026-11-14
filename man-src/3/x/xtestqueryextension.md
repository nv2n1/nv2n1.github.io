---
title: "xtestqueryextension(3)"
name: "xtestqueryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtestqueryextension/"
description: "XTestQueryExtension, XTestCompareCursorWithWindow, XTestCompareCurrentCursorWithWindow, XTestFakeKeyEvent, XTestFakeButtonEvent, XTestFakeMotionEvent, XTestFakeRelativeMotionEvent, XTestGrabControl..."
---

<p>XTestQueryExtension, XTestCompareCursorWithWindow, XTestCompareCurrentCursorWithWindow, XTestFakeKeyEvent, XTestFakeButtonEvent, XTestFakeMotionEvent, XTestFakeRelativeMotionEvent, XTestGrabControl, XTestSetGContextOfGC, XTestSetVisualIDOfVisual, XTestDiscard &#8211; XTest extension functions </p>
<h2>Synopsis</h2>
<pre>cc [ flag ... ] file ... -lXtst [ library ... ]</pre>
<pre>#include &lt;X11/extensions/XTest.h&gt;</pre>
<dl COMPACT>
<dt> <code>Bool XTestQueryExtension(</code><i>display</i><code>, </code><i>event_base_return</i><code>, </code><i>error_base_return</i><code>, </code><i>major_version_return</i><code>, </code><i>minor_version_return</i><code>);</code> </p>
<pre> Display *display;
 int *event_base_return;
 int *error_base_return;
 int *major_version_return;
 int *minor_version_return;</pre>
<dt> <code>Bool XTestCompareCursorWithWindow(</code><i>display</i><code>, </code><i>window</i><code>, </code><i>cursor</i><code>);</code> </p>
<pre> Display *display;
 Window window;
 Cursor cursor;</pre>
<dt> <code>Bool XTestCompareCurrentCursorWithWindow(</code><i>display</i><code>, </code><i>window</i><code>);</code> </p>
<pre> Display *display;
 Window window;</pre>
<dt> <code>int XTestFakeKeyEvent(</code><i>display</i><code>, </code><i>keycode</i><code>, </code><i>is_press</i><code>, </code><i>delay</i><code>);</code> </p>
<pre> Display *display;
 unsigned int keycode;
 Bool is_press;
 unsigned long delay;</pre>
<dt> <code>int XTestFakeButtonEvent(</code><i>display</i><code>, </code><i>button</i><code>, </code><i>is_press</i><code>, </code><i>delay</i><code>);</code> </p>
<pre> Display *display;
 unsigned int button;
 Bool is_press;
 unsigned long delay;</pre>
<dt> <code>int XTestFakeMotionEvent(</code><i>display</i><code>, </code><i>screen_number</i><code>, </code><i>x</i><code>, </code><i>y</i><code>, </code><i>delay</i><code>);</code> </p>
<pre> Display *display;
 int screen_number;
 int x, y;
 unsigned long delay;</pre>
<dt> <code>int XTestFakeRelativeMotionEvent(</code><i>display</i><code>, </code><i>screen_number</i><code>, </code><i>x</i><code>, </code><i>y</i><code>, </code><i>delay</i><code>);</code> </p>
<pre> Display *display;
 int screen_number;
 int x, y;
 unsigned long delay;</pre>
<dt> <code>int XTestGrabControl(</code><i>display</i><code>, </code><i>impervious</i><code>);</code> </p>
<pre> Display *display;
 Bool impervious;</pre>
<dt> <code>void XTestSetGContextOfGC(</code><i>gc</i><code>, </code><i>gid</i><code>);</code> </p>
<pre> GC gc;
 GContext gid;</pre>
<dt> <code>void XTestSetVisualIDOfVisual(</code><i>visual</i><code>, </code><i>visualid</i><code>);</code> </p>
<pre> Visual *visual;
 VisualID visualid;</pre>
<dt> <code>Status XTestDiscard(</code><i>display</i><code>);</code> </p>
<pre> Display *display;</pre>
</dl>
<h2>Description</h2>
<dd>This extension is a minimal set of client and server extensions required to completely test the X11 server with no user intervention. This extension is not intended to support general journaling and playback of user actions. </p>
<p> The functions provided by this extension fall into two groups: </p>
<p> <code>Client Operations</code></p>
<dl COMPACT>
<dd>These routines manipulate otherwise hidden client-side behavior. The actual implementation will depend on the details of the actual language binding and what degree of request buffering, GContext caching, and so on, is provided. In the C binding, routines are provided to access the internals of two opaque data structures &#8212; GCs and Visuals &#8212; and to discard any requests pending within the output buffer of a connection. The exact details can be expected to differ for other language bindings.</dl>
<p> <code>Server Requests</code></p>
<dl COMPACT>
<dd>The first of these requests is similar to that provided in most extensions: it allows a client to specify a major and minor version number to the server and for the server to respond with major and minor versions of its own. The remaining two requests allow the following: </p>
<dl COMPACT>
<dd>&bull; Access to an otherwise <i>write-only</i> server resource: the cursor associated with a given window</dl>
<dl COMPACT>
<dd>&bull; Perhaps most importantly, limited synthesis of input device events, almost as if a cooperative user had moved the pointing device or pressed a key or button.</dl>
</dl>
<p> All XTEST extension functions and procedures, and all manifest constants and macros, will start with the string <i>XTest</i>. All operations are classified as server/client (Server) or client-only (Client). </p>
<p> <code>XTestQueryExtension</code> returns True if the specified display supports the XTEST extension, else False. If the extension is supported, *event_base would be set to the event number for the first event for this extension and *error_base would be set to the error number for the first error for this extension. As no errors or events are defined for this version of the extension, the values returned here are not defined (nor useful). If the extension is supported, *major_version and *minor_version are set to the major and minor version numbers of the extension supported by the display. Otherwise, none of the arguments are set. </p>
<p> If the extension is supported, <code>XTestCompareCursorWithWindow</code> performs a comparison of the cursor whose ID is specified by cursor (which may be <code>None</code>) with the cursor of the window specified by window returning True if they are the same and False otherwise. If the extension is not supported, then the request is ignored and zero is returned. </p>
<p> If the extension is supported, <code>XTestCompareCurrentCursorWithWindow</code> performs a comparison of the current cursor with the cursor of the specified window returning True if they are the same and False otherwise. If the extension is not supported, then the request is ignored and zero is returned. </p>
<p> If the extension is supported, <code>XTestFakeKeyEvent</code> requests the server to simulate either a <code>KeyPress</code> (if is_press is True) or a <code>KeyRelease</code> (if is_press is False) of the key with the specified keycode; otherwise, the request is ignored. </p>
<p> If the extension is supported, the simulated event will not be processed until delay milliseconds after the request is received (if delay is <code>CurrentTime</code>, then this is interpreted as no delay at all). No other requests from this client will be processed until this delay, if any, has expired and subsequent processing of the simulated event has been completed. </p>
<p> If the extension is supported, <code>XTestFakeButtonEvent</code> requests the server to simulate either a <code>ButtonPress</code> (if is_press is True) or a <code>ButtonRelease</code> (if is_press is False) of the logical button numbered by the specified button; otherwise, the request is ignored. </p>
<p> If the extension is supported, the simulated event will not be processed until delay milliseconds after the request is received (if delay is <code>CurrentTime</code>, then this is interpreted as no delay at all). No other requests from this client will be processed until this delay, if any, has expired and subsequent processing of the simulated event has been completed. </p>
<p> If the extension is supported, <code>XTestFakeMotionEvent</code> requests the server to simulate a movement of the pointer to the specified position (x, y) on the root window of screen_number; otherwise, the request is ignored. If screen_number is -1, the current screen (that the pointer is on) is used. </p>
<p> If the extension is supported, the simulated event will not be processed until delay milliseconds after the request is received (if delay is <code>CurrentTime</code>, then this is interpreted as no delay at all). No other requests from this client will be processed until this delay, if any, has expired and subsequent processing of the simulated event has been completed. </p>
<p> If the extension is supported, <code>XTestFakeRelativeMotionEvent</code> requests the server to simulate a movement of the pointer by the specified offsets (x, y) relative to the current pointer position on screen_number; otherwise, the request is ignored. If screen_number is -1, the current screen (that the pointer is on) is used. </p>
<p> If the extension is supported, the simulated event will not be processed until delay milliseconds after the request is received (if delay is <code>CurrentTime</code>, then this is interpreted as no delay at all). No other requests from this client will be processed until this delay, if any, has expired and subsequent processing of the simulated event has been completed. </p>
<p> If impervious is True, then the executing client becomes impervious to server grabs. If impervious is False, then the executing client returns to the normal state of being susceptible to server grabs. </p>
<p> <code>XTestSetGContextOfGC</code> sets the GContext within the opaque datatype referenced by gc to be that specified by gid. </p>
<p> <code>XTestSetVisualIDOfVisual</code> sets the VisualID within the opaque datatype referenced by visual to be that specified by visualid. </p>
<p> <code>XTestDiscard</code> discards any requests within the output buffer for the specified display. It returns True if any requests were discarded; otherwise, it returns False.</p>
<h2>Return Values</h2>
<p>All routines that have return type Status will return nonzero for success and zero for failure. Even if the XTEST extension is supported, the server may withdraw such facilities arbitrarily; in which case they will subsequently return zero.</p>
<h2>Author</h2>
<p><code>Kieron Drake</code><br />
 UniSoft Ltd.</p>
<dl COMPACT>
<dd>Author.</dl>
