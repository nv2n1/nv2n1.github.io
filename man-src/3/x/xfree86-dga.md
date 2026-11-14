---
title: "xfree86-dga(3)"
name: "xfree86-dga"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfree86-dga/"
description: "XDGA – Client library for the XFree86-DGA extension."
---

<p>XDGA &#8211; Client library for the XFree86-DGA extension.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/xf86dga.h&gt;</code></p>
<dl COMPACT>
<dd>Bool <code>XDGAQueryExtension</code>(<br />
 Display *<i>dpy</i>,<br />
 int *<i>eventBase</i>,<br />
 int *<i>errorBase</i>)</p>
<dd>Bool <code>XDGAQueryVersion</code>(<br />
 Display *<i>dpy</i>,<br />
 int *<i>majorVersion</i>,<br />
 int *<i>minorVersion</i>)</p>
<dd>XDGAMode *<code>XDGAQueryModes</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int *<i>num</i>)</p>
<dd>XDGADevice *<code>XDGASetMode</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int <i>mode</i>)</p>
<dd>Bool <code>XDGAOpenFramebuffer</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>)</p>
<dd>void <code>XDGACloseFramebuffer</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>)</p>
<dd>void <code>XDGASetViewport</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int <i>x</i>,<br />
 int <i>y</i>,<br />
 int <i>flags</i>)</p>
<dd>void <code>XDGAInstallColormap</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 Colormap <i>cmap</i>)</p>
<dd>Colormap <code>XDGACreateColormap</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 XDGADevice *<i>device</i>,<br />
 int <i>alloc</i>)</p>
<dd>void <code>XDGASelectInput</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 long <i>event_mask</i>)</p>
<dd>void <code>XDGAFillRectangle</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int <i>x</i>,<br />
 int <i>y</i>,<br />
 unsigned int <i>width</i>,<br />
 unsigned int <i>height</i>,<br />
 unsigned long <i>color</i>)</p>
<dd>void <code>XDGACopyArea</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int <i>srcx</i>,<br />
 int <i>srcy</i>,<br />
 unsigned int <i>width</i>,<br />
 unsigned int <i>height</i>,<br />
 int <i>dstx</i>,<br />
 int <i>dsty</i>)</p>
<dd>void <code>XDGACopyTransparentArea</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int <i>srcx</i>,<br />
 int <i>srcy</i>,<br />
 unsigned int <i>width</i>,<br />
 unsigned int <i>height</i>,<br />
 int <i>dstx</i>,<br />
 int <i>dsty</i>,<br />
 unsigned long <i>key</i>)</p>
<dd>int <code>XDGAGetViewportStatus</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>)</p>
<dd>void <code>XDGASync</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>)</p>
<dd>Bool <code>XDGASetClientVersion</code>(<br />
 Display *<i>dpy</i>)</p>
<dd>void <code>XDGAChangePixmapMode</code>(<br />
 Display *<i>dpy</i>,<br />
 int <i>screen</i>,<br />
 int *<i>x</i>,<br />
 int *<i>y</i>,<br />
 int <i>mode</i>)</p>
<dd>void <code>XDGAKeyEventToXKeyEvent</code>(<br />
 XDGAKeyEvent *<i>dk</i>,<br />
 XKeyEvent *<i>xk</i>) </p>
</dl>
<h2>Description</h2>
<p>The <code>XFree86-DGA</code> extension is an X server extension for allowing client programs direct access to the video frame buffer. This is a brief description of the programming interface for version 2.0 of the <code>XFree86-DGA</code> extension. </p>
<p> <code>XFree86-DGA</code> is not intended as a direct rendering API, but rather, as a mechanism to &quot;get the X Server out of the way&quot; so that some other direct rendering API can have full access to the hardware. With this in mind, DGA does provide clients some direct access to the hardware without requiring a separate rendering API, but this access is limited to direct linear framebuffer access. </p>
<p> Most of the reasons for the <code>XFree86-DGA</code> extension&#8217;s existence are now better served in other ways. Further development of this extension is not expected, and it may be deprecated in a future release. The features that continue to be useful will either be provided through other existing mechanisms, or through an extension that address those needs more specifically. </p>
<p> <code>XFree86-DGA</code> is initialized by passing a number corresponding to a valid <i>XDGAMode</i> to <code>XDGASetMode</code>(). Clients can get a list of valid modes from <code>XDGAQueryModes</code>(). Each <i>XDGAMode</i> corresponds to a different framebuffer layout. </p>
<p> <code>XDGAQueryModes</code>() returns a pointer to an array of <i>XDGAMode</i>s which are valid for the given screen. <i>num</i> is the number of elements in the array. The returned array can be freed with <a href="/docs/linux/man/3-xfree/">XFree</a>(3). The <i>XDGAMode</i> structure is as follows: </p>
<pre>typedef struct {
 int num;
 char *name;
 float verticalRefresh;
 int flags;
 int imageWidth;
 int imageHeight;
 int pixmapWidth;
 int pixmapHeight;
 int bytesPerScanline;
 int byteOrder;
 int depth;
 int bitsPerPixel;
 unsigned long redMask;
 unsigned long greenMask;
 unsigned long blueMask;
 short visualClass;
 int viewportWidth;
 int viewportHeight;
 int xViewportStep;
 int yViewportStep;
 int maxViewportX;
 int maxViewportY;
 int viewportFlags;
 int reserved1;
 int reserved2;
<br>
} XDGAMode;</pre>
<dl COMPACT>
<dt><i>num</i></p>
<dd>A unique identifying number (<i>num</i> &gt; 0) for the mode. This is the number referenced when initializing the mode.</p>
<dt><i>name</i></p>
<dd>The name of the corresponding modeline as given in the xorg.conf file.</p>
<dt><i>verticalRefresh</i></p>
<dd>The vertical refresh rate for the modeline (in Hz).</p>
<dt><i>flags</i></p>
<dd>Any of the following may be OR&#8217;d together:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XDGAConcurrentAccess</code></p>
<dd>Indicates that concurrent client/server access to the framebuffer is possible. If this flag is not set it is very important to call <code>XDGASync</code>() before directly accessing the framebuffer if a call to <code>XDGAFillRectangle</code>(), <code>XDGACopyArea</code>() or <code>XDGACopyTransparentArea</code>() or any Xlib rendering function has been made prior to such accesses.</p>
<dt><code>XDGASolidFillRect</code></p>
<dd>Indicates that <code>XDGAFillRectangle</code>() is supported.</p>
<dt><code>XDGABlitRect</code></p>
<dd>Indicates that <code>XDGACopyArea</code>() is supported.</p>
<dt><code>XDGABlitTransRect</code></p>
<dd>Indicates that <code>XDGACopyTransparentArea</code>() is supported.</p>
<dt><code>XDGAPixmap</code></p>
<dd>Indicates that a Pixmap will be returned when the mode is initialized. This means that rendering with Xlib is possible for this mode.</p>
<dt><code>XDGAInterlaced</code></p>
<dd>
<dt><code>XDGADoublescan</code></p>
<dd>Indicates that the mode is an interlaced or doublescan mode.</dl>
</dl>
<dt><i>imageWidth</i></p>
<dd>
<dt><i>imageHeight</i></p>
<dd>The width and height of the framebuffer area accessible by the client. This rectangle is always justified to the upper left-hand corner.</p>
<dt><i>pixmapWidth</i></p>
<dd>
<dt><i>pixmapHeight</i></p>
<dd>The width and height of the framebuffer area accessible by Xlib. This rectangle is always justified to the upper left-hand corner. These fields are only valid if the <code>XDGAPixmap</code> flag is set in the <i>flags</i> field.</p>
<dt><i>bytesPerScanline</i></p>
<dd>The pitch of the framebuffer in bytes.</p>
<dt><i>byteOrder</i></p>
<dd><code>MSBFirst</code> or <code>LSBFirst</code>.</p>
<dt><i>depth</i></p>
<dd>The number of bits in each pixel which contain usable data.</p>
<dt><i>bitsPerPixel</i></p>
<dd>The number of bits taken up by each pixel.</p>
<dt><i>redMask</i></p>
<dd>
<dt><i>greenMask</i></p>
<dd>
<dt><i>blueMask</i></p>
<dd>The RGB masks. These do not apply to color-indexed modes.</p>
<dt><i>visualClass</i></p>
<dd><code>TrueColor</code>, <code>PseudoColor</code>, <code>DirectColor</code>, etc.</p>
<dt><i>viewportWidth</i></p>
<dd>
<dt><i>viewportHeight</i></p>
<dd>The dimensions of the portion of the framebuffer which will be displayed on the screen.</p>
<dt><i>xViewportStep</i></p>
<dd>
<dt><i>yViewportStep</i></p>
<dd>The granularity of the x,y viewport positioning possible with the <code>XDGASetViewport</code>() function.</p>
<dt><i>maxViewportX</i></p>
<dd>
<dt><i>maxViewportY</i></p>
<dd>The maximum x and y positions possible with the <code>XDGASetViewport</code>() function.</p>
<dt><i>viewportFlags</i></p>
<dd>Any of the following may be OR&#8217;d together</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XDGAFlipRetrace</code></p>
<dd>Indicates that the hardware can switch viewports during the vertical retrace.</p>
<dt><code>XDGAFlipImmediate</code></p>
<dd>Indicates that the hardware can switch viewports immediately without waiting for the vertical retrace.</dl>
</dl>
</dl>
<p> <code>XDGASetMode</code>() initialises the <i>XDGAMode</i> corresponding to <i>num</i>. To exit DGA mode and return to normal server operation, call <code>XDGASetMode</code>() with <i>num</i> set to zero. <code>XDGASetMode</code>() returns a pointer to an <i>XDGADevice</i> if successful. The XDGADevice can be freed with <a href="/docs/linux/man/3-xfree/">XFree</a>(3). The <i>XDGADevice</i> structure is as follows: </p>
<pre>typedef struct {
 XDGAMode mode;
 unsigned char *data;
 Pixmap pixmap;
<br>
} XDGADevice;</pre>
<dl COMPACT>
<dt><i>mode</i></p>
<dd>The <i>XDGAMode</i> structure, identical to the information returned by <code>XDGAQueryModes</code>().</p>
<dt><i>data</i></p>
<dd>If direct framebuffer access is desired and possible, this field will contain a pointer to the mapped framebuffer memory. Generally, this field will be zero unless a call to <code>XDGAOpenFramebuffer</code>() is made prior to initialization of the mode.</p>
<dt><i>pixmap</i></p>
<dd>If the mode supports Xlib rendering as indicated by <code>XDGAPixmap</code> in the <i>flags</i> field, this will contain a Pixmap handle suitable for passing as the drawable argument to Xlib functions. This field will be zero if Xlib rendering is not supported.</dl>
<p> <code>XDGAQueryExtension</code>() checks for the presence of the extension and returns the event and error bases. </p>
<p> <code>XDGAQueryVersion</code>() returns the <code>XFree86-DGA</code> major and minor version numbers. </p>
<p> <code>XDGAOpenFramebuffer</code>() maps the framebuffer memory. The client needs sufficient privileges to be able to do this. <code>XDGAOpenFramebuffer</code>() should be called prior to initializing a DGA mode if direct framebuffer access is desired for that mode. <code>XDGAOpenFramebuffer</code>() does not need to be called if direct framebuffer access is not required. If the framebuffer is opened, </p>
<p> <code>XDGACloseFramebuffer</code>() should be called prior to client exit to unmap the memory. </p>
<p> <code>XDGAChangePixmapMode</code>() can be used to change between two pixmap sizes in cases where a Pixmap is available for Xlib rendering. The following values for the <i>mode</i> parameter are available:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XDGAPixmapModeLarge</code></p>
<dd>The pixmap size is defined by the <i>pixmapWidth</i> and <i>pixmapHeight</i> fields in the <i>XDGAMode</i> structure. The <i>x</i> and <i>y</i> values are ignored in this case.</p>
<dt><code>XDGAPixmapModeSmall</code></p>
<dd>The pixmap size is defined by the <i>viewportWidth</i> and <i>viewportHeight</i> fields in the <i>XDGAMode</i> structure. In this mode, the <i>x</i> and <i>y</i> values specify where in the framebuffer this pixmap rectangle is located. It may be placed anywhere within the Xlib renderable region described by the <i>pixmapWidth</i> and <i>pixmapHeight</i> fields in the <i>XDGAMode</i>. The <i>x</i> and <i>y</i> values returned are the resultant location of the pixmap and may be different from the requested x,y location due to platform specific alignment constraints. All Xlib rendering is clipped to this pixmap rectangle.</dl>
</dl>
<p> <code>XDGASetViewport</code>() sets the upper left-hand corner of the rectangle of framebuffer that is to be displayed on the screen. Not all locations may be supported by the hardware and requested locations will be adjusted according to the <i>xViewportStep</i> and <i>yViewportStep</i> fields in the <i>XDGAMode</i>. </p>
<p> <i>flags</i> can be <code>XDGAFlipRetrace</code> or <code>XDGAFlipImmediate</code> to adjust the viewport location at the next vertical retrace or immediately. Values other than the supported values advertised in the mode&#8217;s <i>viewportFlags</i> field will result in hardware-specific default behavior. <code>XDGAFlipImmediate</code> will block until the flip is completed. <code>XDGAFlipRetrace</code> will generally NOT block so it is necessary to monitor the viewport status with <code>XDGAGetViewportStatus</code>(). <code>XDGAFlipImmediate</code> requests during pending <code>XDGAFlipRetrace</code> requests will be ignored. </p>
<p> <code>XDGAGetViewportStatus</code>() keeps track of the <code>XDGASetViewport</code>() requests still pending. The return value of the function will have consecutive bits set (LSB justified), each bit representing a pending viewport change. For example: </p>
<pre> while(XDGAGetViewportStatus(dpy, screen));</pre>
<p>waits for all pending viewport changes to finish. </p>
<pre> while(0x2 &amp; XDGAGetViewportStatus(dpy, screen));</pre>
<p>waits until all but the last viewport changes have completed. </p>
<p> <code>XDGACreateColormap</code>() is similar to the Xlib function <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3) except that it takes an <i>XDGADevice</i> as an argument instead of a Window and Visual. Though <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3) may create usable colormaps in some cases, <code>XDGACreateColormap</code>() is the preferred method for creating colormaps in DGA since there may not be an advertised visual compatible with the DGA device. </p>
<p> <code>XDGAInstallColormap</code>() must be used to install colormaps in DGA mode. <a href="/docs/linux/man/3-xinstallcolormap/">XInstallColormap</a>(3) will not work. </p>
<p> <code>XDGASelectInput</code>() enables DGA&#8217;s own event mechanism. This function is similar to <a href="/docs/linux/man/3-xselectinput/">XSelectInput</a>(3), and all Xlib Key, Button and Motion masks are supported. The following DGA events are defined: </p>
<pre>typedef struct {
 int type; /* ButtonPress or ButtonRelease + the DGA event base*/
 unsigned long serial; /* # or last request processed by the server */
 Display *display; /* Display the event was read from */
 int screen; /* The screen number the event came from */
 Time time; /* milliseconds */
 unsigned int state; /* key or button mask */
 unsigned int button; /* detail */
<br>
} XDGAButtonEvent;</pre>
<pre>typedef struct {
 int type; /* KeyPress or KeyRelease + the DGA event base*/
 unsigned long serial; /* # or last request processed by the server */
 Display *display; /* Display the event was read from */
 int screen; /* The screen number the event came from */
 Time time; /* milliseconds */
 unsigned int state; /* key or button mask */
 unsigned int keycode; /* detail */
<br>
} XDGAKeyEvent;</pre>
<pre>typedef struct {
 int type; /* MotionNotify + the DGA event base*/
 unsigned long serial; /* # or last request processed by the server */
 Display *display; /* Display the event was read from */
 int screen; /* The screen number the event came from */
 Time time; /* milliseconds */
 unsigned int state; /* key or button mask */
 int dx; /* relative pointer motion */
 int dy; /* relative pointer motion */
<br>
} XDGAMotionEvent;</pre>
<p><code>XDGAKeyEventToXKeyEvent</code>() is a helper function to translate <i>XDGAKeyEvent</i>s into <i>XKeyEvent</i>s suitable for use with <a href="/docs/linux/man/3-xlookupkeysym/">XLookupKeysym</a>(3). </p>
<p> <code>XDGAFillRectangle</code>(), <code>XDGACopyArea</code>(), and <code>XDGACopyTransparentArea</code>() are included with some reservation since DGA is not intended as a rendering API. These are merely convenience routines and are optionally supported. The associated flags will be set in the <i>XDGAMode</i>&#8216;s <i>flags</i> field if these functions are supported. These functions will be no-ops otherwise. they do not provide direct access to the hardware, but are simply context-less operations performed by the server. </p>
<p> <code>XDGASync</code>() blocks until all server rendering to the framebuffer completes. If Xlib or the 3 rendering functions above are used, <code>XDGASync</code>() must be called before the client directly accesses the framebuffer as the server rendering is asynchronous with the client and may have not completed. This is especially important if the <code>XDGAConcurrentAccess</code> flag is not set in the <i>XDGAMode</i>&#8216;s <i>flags</i> field since concurrent access by the server and client may result in a system lockup.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)</p>
<h2>Authors</h2>
<p><code>XFree86-DGA</code> version 2 was written by Mark Vojkovich. Version 1 was written by Jon Tombs, Harm Hanemaayer, Mark Vojkovich.</p>
