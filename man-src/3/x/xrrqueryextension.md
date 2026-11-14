---
title: "xrrqueryextension(3)"
name: "xrrqueryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrrqueryextension/"
description: "Xrandr – X Resize, Rotate and Reflection extension."
---

<p>&nbsp;Xrandr &#8211; X Resize, Rotate and Reflection extension. </p>
<h2>Syntax</h2>
<p>#include &lt;X11/extensions/Xrandr.h&gt; </p>
<pre>Bool XRRQueryExtension (Display *<i>dpy</i>,
 int *<i>event_base_return</i>, int *<i>error_base_return</i>);
Status XRRQueryVersion (Display *<i>dpy</i>,
 int *<i>major_version_return</i>,
 int *<i>minor_version_return</i>);
XRRScreenConfiguration *XRRGetScreenInfo (Display *dpy,
 Drawable <i>draw</i>);
void XRRFreeScreenConfigInfo (
 <i>XRRScreenConfiguration *config</i>);
Status XRRSetScreenConfig (Display *<i>dpy</i>,
 XRRScreenConfiguration *<i>config</i>,
 Drawable <i>draw</i>,
 int <i>size_index</i>,
 Rotation <i>rotation</i>,
 Time <i>timestamp</i>);
Status XRRSetScreenConfigAndRate (Display *<i>dpy</i>,
 XRRScreenConfiguration *<i>config</i>,
 Drawable <i>draw</i>,
 int <i>size_index</i>,
 Rotation <i>rotation</i>,
 short <i>rate</i>,
 Time <i>timestamp</i>);
Rotation XRRConfigRotations(
 XRRScreenConfiguration *<i>config</i>,
 Rotation *<i>current_rotation</i>);
Time XRRConfigTimes (
 XRRScreenConfiguration *<i>config</i>,
 Time *<i>config_timestamp</i>);
XRRScreenSize *XRRConfigSizes(
 XRRScreenConfiguration *<i>config</i>,
 int *<i>nsizes</i>);
short *XRRConfigRates (
 XRRScreenConfiguration *<i>config</i>,
 int <i>size_index</i>,
 int *<i>nrates</i>);
SizeID XRRConfigCurrentConfiguration (
 XRRScreenConfiguration *<i>config</i>,
 Rotation *<i>rotation</i>);
short XRRConfigCurrentRate (
 XRRScreenConfiguration *<i>config</i>);
int XRRRootToScreen(
 Display *<i>dpy</i>,
 Window <i>root</i>);
void XRRSelectInput(Display *<i>dpy</i>, Window <i>window</i>, int <i>mask</i>);
/*
 * intended to take RRScreenChangeNotify, or
 * ConfigureNotify (<i>on the root window</i>)
 * returns 1 if it is an event type it understands, 0 if not
 */
int XRRUpdateConfiguration(XEvent *<i>event</i>);
/*
 * the following are always safe to call, even if RandR is
 * not implemented on a screen
 */
<br>
Rotation XRRRotations(
 Display *<i>dpy</i>, int <i>screen</i>,
 Rotation *<i>current_rotation</i>);
XRRScreenSize *XRRSizes(Display *<i>dpy</i>,
 int <i>screen</i>, int *<i>nsizes</i>);
short *XRRRates (Display *<i>dpy</i>, int <i>screen</i>,
 int <i>size_index</i>, int *<i>nrates</i>);
Time XRRTimes (Display *<i>dpy</i>, int <i>screen</i>, Time *<i>config_timestamp</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen</i></p>
<dd>Specifies which screen.</p>
<dt><i>draw</i></p>
<dd>Specifies the screen.</p>
<dt><i>rotation</i></p>
<dd>Specifies the possible rotations or reflections of the screen.</p>
<dt><i>current_rotation</i></p>
<dd>Specifies the current rotations and reflection of the screen.</p>
<dt><i>timestamp</i></p>
<dd>Specifies the server timestamp.</p>
<dt><i>config_timestamp</i></p>
<dd>Specifies the timestamp when the screen was last (re)configured.</p>
<dt><i>config</i></p>
<dd>Specifies the screen configuration being used.</p>
<dt><i>sizes</i></p>
<dd>Specifies the array of supported sizes.</p>
<dt><i>rate</i></p>
<dd>Specifies the refresh rate in Hz. </p>
</dl>
<h2>Datatypes</h2>
<p><code>Rotations/Reflections</code> </p>
<p> Can be any of: </p>
<pre>#define RR_Rotate_0 1
#define RR_Rotate_90 2
#define RR_Rotate_180 4
#define RR_Rotate_270 8
/* new in 1.0 protocol, to allow reflection of screen */
/* reflection is applied after rotation */
#define RR_Reflect_X 16
#define RR_Reflect_Y 32
typedef struct {
 int width, height;
 int mwidth, mheight;
} XRRScreenSize;
typedef struct {
 int type; /* event base */
 unsigned long serial; /* # of last request processed by server */
 Bool send_event; /* true if this came from a SendEvent request */
 Display *display; /* Display the event was read from */
 Window window; /* window which selected for this event */
 Window root; /* Root window for changed screen */
 Time timestamp; /* when the screen change occurred */
 Time config_timestamp; /* when the last configuration change */
 SizeID size_index;
 SubpixelOrder subpixel_order;
 Rotation rotation;
 int width;
 int height;
 int mwidth;
 int mheight;
} XRRScreenChangeNotifyEvent;</pre>
<p>The <code>XRRScreenSize</code> structure contains a possible root size in pixels and in millimeters. </p>
<p> A <code>XRRScreenChangeNotifyEvent</code> is sent to a client that has requested notification whenever the screen configuration is changed. A client can perform this request by calling <code>XRRSelectInput</code>, passing the display, the root window, and the <code>RRScreenChangeNotifyMask</code> mask. </p>
<p> <code>XRRScreenConfiguration</code> is an opaque data type containing the configuration information for a screen. </p>
<p> <code>Timestamps</code> </p>
<p> Time stamps are included and must be used to ensure the client is playing with a full deck: the screen may change properties on the fly and this ensures its knowledge of the configuration is up to date. This is to help issues when screens may become hot-pluggable in the future. </p>
<h2>Description</h2>
<p><code>Xrandr</code> is a simple library designed to interface the X Resize and Rotate Extension. This allows clients to change the size and rotation of the root window of a screen, along with the ability to reflect the screen about either axis (if supported by the implementation). Rotation and reflection may be implemented by software and may result in slower performance if rotation and reflection are implemented in this fashion (as are all implementations as of October 2002). </p>
<p> The Xrandr library does some minimal caching to avoid roundtrips to provide clients frequently used information. See &quot;The X Resize and Rotate Extension&quot; for a detailed description; also note that depth switching, as described in the document is not implemented, and may (or may not) ever be implemented, as display memory is growing rapidly, and toolkits are already beginning to support migration, mitigating the need for depth switching. If it is implemented in the future, we expect to do so via an upward compatible extension to the current library/protocol; functionality described here should continue to work. </p>
<p> Rotation and reflection and how they interact can be confusing. In Randr, the coordinate system is rotated in a counter-clockwise direction relative to the normal orientation. Reflection is along the window system coordinate system, not the physical screen X and Y axis, so that rotation and reflection do not interact. The other way to consider reflection is to treat it as specified in the &quot;normal&quot; orientation, before rotation. </p>
<p> The <code>XRRScreenChangeNotify</code> event is sent to clients that ask to be informed whenever the root window configuration changes. Configuration changes may include resolution, physical size, subpixel order (see <a href="/docs/linux/man/3-xrender/">XRender</a>(3)), and rotation. Note that changes to any or all of these could occur due to external events (user control in the X server, a different monitor/flat panel display being hot-plugged) and is not only the result of a protocol/library request to the X server. </p>
<p> Additionally, to eliminate a potential race condition, this event may be generated immediately upon selecting for notification if the screen has changed since the client of Xrandr connected to the X server, to enable reliable screen resolution changing when a user may log in and change the configuration while one or many clients are starting up. </p>
<p> <code>Xlib notification</code> </p>
<p> Clients must call back into Xlib using <code>XRRUpdateConfiguration</code> when screen configuration change notify events are generated (or root window configuration changes occur, to update Xlib&#8217;s view of the resolution, size, rotation, reflection or subpixel order. Generally, toolkits will perform this operation on behalf of applications; we did not want to change display structure data behind the back of toolkits, as in multithreaded clients, various race conditions might occur. Toolkits should provide clients some mechanism for notification of screen change, of course. </p>
<h2>Functions</h2>
<p>There are two classes of interfaces: those which can be safely called even if RandR is not implemented on a screen (to make common idioms not dependent on the server having support), and those which will return errors if the extension is not present. </p>
<p> <code>XRRRotations</code> returns both the possible set of rotations/reflections supported (as a bitmask) as the value of the function, along with the current rotation/reflection of the screen. </p>
<p> <code>XRRSizes</code> returns the size and a pointer to the current sizes supported by the specified screen. The first size specified is the default size of the server. If RandR is not supported, it returns 0 for the number of sizes. </p>
<p> <code>XRRRates</code> returns a pointer to the rates supported by the specified size. If RandR is not supported, it returns 0 for the number of rates. </p>
<p> <code>XRRTimes</code> returns the time last reported by the server along with the timestamp the last configuration changed. If the configuration has changed since the client last updated its view of the server time, requests to change the configuration will fail until the client has an up to date timestamp. </p>
<p> <code>XRRRootToScreen</code> returns the screen number given a root window (for example, from an <code>XRRScreenChangeNotifyEvent</code>). </p>
<p> The rest of the functions will fail if applied to screens not implementing the RandR extension. <code>XRRSetScreenConfig</code> sets the screen size and rotation and reflection to the desired values on the screen specified by <i>draw</i>, or returns a <code>BadValue</code> error. <i>size_index</i> specifies which size configuration is to be used, <i>rotation</i> specifies which rotation or reflection is to be used (or a <code>BadValue</code> error is returned). The <i>timestamp</i> is used by the server to make sure the client has up to date configuration information. Status is returned to indicate success or failure; a client must refresh its configuration information if it fails and try the call again (by calling <code>XRRGetScreenInfo</code>). </p>
<p> <code>XRRSetScreenConfigAndRate</code> is like <code>XRRSetScreenConfig</code> but also sets the refresh rate. If specified rate is not supported a <code>BadValue</code> error is returned. </p>
<p> <code>XRRConfigRotations,</code> <code>XRRConfigSizes,</code> <code>XRRConfigCurrentConfiguration,</code> <code>XRRConfigTimes,</code> <code>XRRConfigRates,</code> and <code>XRRConfigCurrentRate</code> are used to get specific configuration information out of a screen configuration. </p>
<p> <code>XRRGetScreenInfo</code> returns a screen configuration for later use; the information is private to the library. Call <code>XRRFreeScreenConfigInfo</code> to free this information when you are finished with it. It forces a round trip to the server. </p>
<p> Other functions include: <code>XRRQueryExtension</code> which returns the event and error base codes, <code>XRRQueryVersion</code> , which returns the current version of the extension (this information is cached by the library).</p>
<h2>Restrictions</h2>
<p><code>Xrandr</code> will remain upward compatible after the current 1.0 release.</p>
<h2>Author</h2>
<p>Jim Gettys, and Keith Packard, HP.</p>
