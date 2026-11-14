---
title: "xcompositequeryversion(3)"
name: "xcompositequeryversion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcompositequeryversion/"
description: "Xcomposite – X Composite Extension library"
---

<p>Xcomposite &#8211; X Composite Extension library </p>
<h2>Synopsis</h2>
<pre>#include &lt;X11/extensions/Xcomposite.h&gt;</pre>
<dl COMPACT>
<dt> <code>Bool XCompositeQueryExtension(Display&nbsp;*</code><i>dpy</i><code>, int&nbsp;*</code><i>event_base_return</i><code>, int&nbsp;*</code><i>error_base_return</i><code>);</code></p>
<dt> <code>Status XCompositeQueryVersion(Display&nbsp;*</code><i>dpy</i><code>, int&nbsp;*</code><i>major_version_return</i><code>, int&nbsp;*</code><i>minor_version_return</i><code>);</code></p>
<dt> <code>int XCompositeVersion(void);</code></p>
<dt> <code>void XCompositeRedirectWindow(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>, int&nbsp;</code><i>update</i><code>);</code></p>
<dt> <code>void XCompositeRedirectSubwindows(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>, int&nbsp;</code><i>update</i><code>);</code></p>
<dt> <code>void XCompositeUnredirectWindow(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>, int&nbsp;</code><i>update</i><code>);</code></p>
<dt> <code>void XCompositeUnredirectSubwindows(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>, int&nbsp;</code><i>update</i><code>);</code></p>
<dt> <code>XserverRegion XCompositeCreateRegionFromBorderClip(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>);</code></p>
<dt> <code>Pixmap XCompositeNameWindowPixmap(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>);</code></p>
<dt> <code>Window XCompositeGetOverlayWindow(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>);</code></p>
<dt> <code>void XCompositeReleaseOverlayWindow(Display&nbsp;*</code><i>dpy</i><code>, Window&nbsp;</code><i>window</i><code>);</code></dl>
<h2>Description</h2>
<dd>The composite extension provides several related mechanisms: </p>
<p> Per-hierarchy storage</p>
<dl COMPACT>
<dd>The rendering of an entire hierarchy of windows is redirected to off-screen storage. The pixels of that hierarchy are available whenever it is viewable. Storage is automatically reallocated when the top level window changes size. Contents beyond the geometry of the top window are not preserved.</dl>
<p> Automatic shadow update</p>
<dl COMPACT>
<dd>When a hierarchy is rendered off-screen, the X server provides an automatic mechanism for presenting those contents within the parent window. The implementation is free to make this update lag behind actual rendering operations by an unspecified amount of time. This automatic update mechanism may be disabled so that the parent window contents can be completely determined by an external application.</dl>
<p> Composite Overlay Window</p>
<dl COMPACT>
<dd>Version 0.3 of the protocol adds the Composite Overlay Window, which provides compositing managers with a surface on which to draw without interference. This window is always above normal windows and is always below the screen saver window. It is an InputOutput window whose width and height are the screen dimensions. Its visual is the root visual and its border width is zero. Attempts to redirect it using the composite extension are ignored. This window does not appear in the reply of the QueryTree request. It is also an override redirect window. These last two features make it invisible to window managers and other X11 clients. The only way to access the XID of this window is via the CompositeGetOverlayWindow request. Initially, the Composite Overlay Window is unmapped.</dl>
<p> Parent window clipping</p>
<dl COMPACT>
<dd>Version 0.4 of the protocol modifies the semantics of parent window clipping in the presence of manual redirected children. With this version, the area in the parent covered by manual redirected children is left in the parent clip list instead of being removed as in older versions.</dl>
<p> Per-hierarchy storage may be created for individual windows or for all children of a window. Manual shadow update may be selected by only a single application for each window; manual update may also be selected on a per-window basis or for each child of a window. Detecting when to update may be done with the Damage extension. </p>
<p> The off-screen storage includes the window contents, its borders and the contents of all descendants.</p>
<h2>Arguments</h2>
<p><i>display</i></p>
<dl COMPACT>
<dd>Pointer to the <code>Display</code> structure returned from <code>XOpenDisplay</code> for the connection to the X server.</dl>
<p> <i>event_base_return</i></p>
<dl COMPACT>
<dd>Pointer to integer where the base value for Composite Extension events will be stored.</dl>
<p> <i>error_base_return</i></p>
<dl COMPACT>
<dd>Pointer to integer where the base value for Composite Extension errors will be stored.</dl>
<p> <i>major_version_return</i></p>
<dl COMPACT>
<dd>Pointer to integer where the major version of the Composite Extension supported by the X server will be stored.</dl>
<p> <i>minor_version_return</i></p>
<dl COMPACT>
<dd>Pointer to integer where the minor version of the Composite Extension supported by the X server will be stored.</dl>
<p> <i>window</i></p>
<dl COMPACT>
<dd>Specifies the window ID to operate on.</dl>
<p> <i>update</i></p>
<dl COMPACT>
<dd>Specifies the mode for updating the window contents. Must be either <code>CompositeRedirectAutomatic</code> or <code>CompositeRedirectManual</code>.</dl>
<h2>Functions</h2>
<p><code>XCompositeQueryExtension</code></p>
<dl COMPACT>
<dd><code>XCompositeQueryExtension</code> determines if the Composite Extension is available on the given display. It returns <code>True</code> if the extension is supported, otherwise <code>False</code>. If the extension is present, the base values for events and errors are returned, and can be used to decode incoming event and error values.</dl>
<p> <code>XCompositeQueryVersion</code></p>
<dl COMPACT>
<dd><code>XCompositeQueryVersion</code> determines if the X Server supports a version of the X Composite Extension which is compatible with the client library. A non-zero Status is returned if a compatible version of the extension is supported, otherwise a zero Status is returned. If the extension is supported, the major and minor version numbers are returned to indicate the level of Composite Extension support. No other XComposite functions (except XCompositeQueryExtension) may be called before this function. If a client violates this rule, the effects of all subsequent XComposite calls that it makes are undefined.</dl>
<p> <code>XCompositeVersion</code></p>
<dl COMPACT>
<dd><code>XCompositeVersion</code> returns the version of the X Composite library. The version number is encoded as: (major * 10000) + (minor * 100) + revision </p>
<p> For example, version 1.4.6 would be encoded as the integer 10406.</dl>
<p> <code>XCompositeRedirectWindow</code></p>
<dl COMPACT>
<dd><code>XCompositeRedirectWindow</code> requests the X server to direct the hierarchy starting at <i>window</i> to off-screen storage. The <i>update</i> argument specifies whether the contents are mirrored to the parent window automatically or not. Only one client at a time may specify an update type of <code>CompositeRedirectManual</code>, another attempt will result in a BadAccess error. When all clients enabling redirection terminate, the redirection will automatically be disabled. </p>
<p> The root window may not be redirected. Doing so results in a BadMatch error. Specifying an invalid window id will result in a BadWindow error.</dl>
<p> <code>XCompositeRedirectSubwindows</code></p>
<dl COMPACT>
<dd><code>XCompositeRedirectSubwindows</code> requests the X server to redirect hierarchies starting at all current and future children of <i>window</i> as in <code>XCompositeRedirectWindow</code>. If <i>update</i> is <code>CompositeRedirectManual</code>, then painting of the window background during window manipulation and ClearArea requests is inhibited.</dl>
<p> <code>XCompositeUnredirectWindow</code></p>
<dl COMPACT>
<dd><code>XCompositeUnredirectWindow</code> requests the X server to terminate redirection of <i>window</i>. If the specified window was not selected for redirection by the current client, a BadValue error results.</dl>
<p> <code>XCompositeUnredirectSubwindows</code></p>
<dl COMPACT>
<dd><code>XCompositeUnredirectWindow</code> requests the X server to terminate redirection of all children of <i>window</i>. If the specified window was not selected for sub-redirection by the current client, a BadValue error results.</dl>
<p> <code>XCompositeCreateRegionFromBorderClip</code></p>
<dl COMPACT>
<dd><code>XCompositeCreateRegionFromBorderClip</code> creates a region containing the &quot;usual&quot; border clip value; that is the area of the window clipped against siblings and the parent. This region can be used to restrict rendering to suitable areas while updating only a single window. The region is copied at the moment the request is executed; future changes to the window hierarchy will not be reflected in this region.</dl>
<p> <code>XCompositeNameWindowPixmap</code></p>
<dl COMPACT>
<dd><code>XCompositeNameWindowPixmap</code> creates and returns a pixmap id that serves as a reference to the off-screen storage for <i>window</i>. This pixmap will remain allocated until freed, even if the window is unmapped, reconfigured or destroyed. However, the window will get a new pixmap allocated each time it is mapped or resized, so this function will need to be reinvoked for the client to continue to refer to the storage holding the current window contents. Generates a BadMatch error if <i>window</i> is not redirected or is not visible. </p>
<p> The X server must support at least version 0.2 of the Composite Extension for <code>XCompositeNameWindowPixmap</code>.</dl>
<p> <code>XCompositeGetOverlayWindow</code></p>
<dl COMPACT>
<dd><code>XCompositeGetOverlayWindow</code> returns the window ID of the Composite Overlay Window for the screen specified by the argument <i>window</i>. This function notifies the X server that the client wishes to use the Composite Overlay Window of this screen. If this Composite Overlay Window has not yet been mapped, it is mapped by this request. </p>
<p> The Composite Overlay Window for a particular screen will be unmapped when all clients who have called this function have either called <code>XCompositeReleaseOverlayWindow</code> for that screen, or terminated their connection to the X server. </p>
<p> The X server must support at least version 0.3 of the Composite Extension for <code>XCompositeGetOverlayWindow</code>.</dl>
<p> <code>XCompositeReleaseOverlayWindow</code></p>
<dl COMPACT>
<dd>This request specifies that the client is no longer using the Composite Overlay Window on the screen specified by the argument <i>window</i>. A screen&#8217;s Composite Overlay Window is unmapped when there are no longer any clients using it. </p>
<p> The X server must support at least version 0.3 of the Composite Extension for <code>XCompositeReleaseOverlayWindow</code>.</dl>
<h2>Authors</h2>
<p><code>Keith Packard</code> &lt;keithp [at] keithp.com&gt;</p>
<dl COMPACT>
<dd>Extension specification and implementation</dl>
<p> <code>Deron Johnson</code> &lt;deron.johnson [at] sun.com&gt;</p>
<dl COMPACT>
<dd>Overlay Window specification and implementation</dl>
