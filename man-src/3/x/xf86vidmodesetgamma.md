---
title: "xf86vidmodesetgamma(3)"
name: "xf86vidmodesetgamma"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xf86vidmodesetgamma/"
---

XF86VidModeQueryExtension, XF86VidModeQueryVersion, XF86VidModeSetClientVersion, XF86VidModeGetModeLine, XF86VidModeGetAllModeLines, XF86VidModeAddModeLine, XF86VidModeDeleteModeLine, XF86VidModeModModeLine, XF86VidModeValidateModeLine, XF86VidModeSwitchMode, XF86VidModeSwitchToMode, XF86VidModeLockModeSwitch, XF86VidModeGetMonitor, XF86VidModeGetViewPort, XF86VidModeSetViewPort, XF86VidModeGetDotClocks, XF86VidModeGetGamma, XF86VidModeSetGamma, XF86VidModeGetGammaRamp, XF86VidModeSetGammaRamp, XF86VidModeGetGammaRampSize, XF86VidModeGetPermissions - Extension library for the XFree86-VidMode X extension
<h2>Synopsis</h2><pre>#include &lt;X11/extensions/xf86vmode.h&gt;
Bool XF86VidModeQueryExtension(
 Display *<i>display</i>,
 int *<i>event_base_return</i>,
 int *<i>error_base_return</i>);
Bool XF86VidModeQueryVersion(
 Display *<i>display</i>,
 int *<i>major_version_return</i>,
 int *<i>minor_version_return</i>);
Bool XF86VidModeSetClientVersion(
 Display *<i>display</i>);
Bool XF86VidModeGetModeLine(
 Display *<i>display</i>,
 int <i>screen</i>,
 int *<i>dotclock_return</i>,
 XF86VidModeModeLine *<i>modeline</i>);
Bool XF86VidModeGetAllModeLines(
 Display *<i>display</i>,
 int <i>screen</i>,
 int *<i>modecount_return</i>,
 XF86VidModeModeInfo ***<i>modesinfo</i>);
Bool XF86VidModeAddModeLine(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeModeInfo *<i>modeline</i>,
 XF86VidModeModeInfo *<i>aftermode</i>);
Bool XF86VidModeDeleteModeLine(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeModeInfo *<i>modeline</i>);
Bool XF86VidModeModModeLine(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeModeLine *<i>modeline</i>);
Status XF86VidModeValidateModeLine(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeModeLine *<i>modeline</i>);
Bool XF86VidModeSwitchMode(
 Display *<i>display</i>,
 int <i>screen</i>,
 int <i>zoom</i>);
Bool XF86VidModeSwitchToMode(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeModeInfo *<i>modeline</i>);
Bool XF86VidModeLockModeSwitch(
 Display *<i>display</i>,
 int <i>screen</i>,
 int <i>lock</i>);
Bool XF86VidModeGetMonitor(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeMonitor *<i>monitor</i>);
Bool XF86VidModeGetViewPort(
 Display *<i>display</i>,
 int <i>screen</i>,
 int *<i>x_return</i>,
 int *<i>y_return</i>);
Bool XF86VidModeSetViewPort(
 Display *<i>display</i>,
 int <i>screen</i>,
 int <i>x</i>,
 int <i>y</i>);
XF86VidModeGetDotClocks(
 Display *<i>display</i>,
 int <i>screen</i>,
 int *<i>flags return</i>,
 int *<i>number of clocks return</i>,
 int *<i>max dot clock return</i>,
 int **<i>clocks return</i>);
XF86VidModeGetGamma(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeGamma *<i>Gamma</i>);
XF86VidModeSetGamma(
 Display *<i>display</i>,
 int <i>screen</i>,
 XF86VidModeGamma *<i>Gamma</i>);
XF86VidModeGetGammaRamp(
 Display *<i>display</i>,
 int <i>screen</i>,
 int <i>size</i>,
 unsigned short *<i>red array</i>,
 unsigned short *<i>green array</i>,
 unsigned short *<i>blue array</i>);
XF86VidModeSetGammaRamp(
 Display *<i>display</i>,
 int <i>screen</i>,
 int <i>size</i>,
 unsigned short *<i>red array</i>,
 unsigned short *<i>green array</i>,
 unsigned short *<i>blue array</i>);
XF86VidModeGetGammaRampSize(
 Display *<i>display</i>,
 int <i>screen</i>,
 int *<i>size</i>);</pre><h2>Arguments</h2><dl COMPACT><dt><i>display</i>
<dd>Specifies the connection to the X server.
<dt><i>screen</i>
<dd>Specifies which screen number the setting apply to.
<dt><i>event_base_return</i>
<dd>Returns the base event number for the extension.
<dt><i>error_base_return</i>
<dd>Returns the base error number for the extension.
<dt><i>major_version_return</i>
<dd>Returns the major version number of the extension.
<dt><i>minor_version_return</i>
<dd>Returns the minor version number of the extension.
<dt><i>dotclock_return</i>
<dd>Returns the clock for the mode line.
<dt><i>modecount_return</i>
<dd>Returns the number of video modes available in the server.
<dt><i>zoom</i>
<dd>If greater than zero, indicates that the server should switch to the next mode, otherwise switch to the previous mode.
<dt><i>lock</i>
<dd>Indicates that mode switching should be locked, if non-zero.
<dt><i>modeline</i>
<dd>Specifies or returns the timing values for a video mode.
<dt><i>aftermode</i>
<dd>Specifies the timing values for the video mode after which the new mode will added.
<dt><i>modesinfo</i>
<dd>Returns the timing values and dotclocks for all of the available video modes.
<dt><i>monitor</i>
<dd>Returns information about the monitor.
<dt><i>x</i>
<dd>Specifies the desired X location for the viewport.
<dt><i>x_return</i>
<dd>Returns the current X location of the viewport.
<dt><i>y</i>
<dd>Specifies the desired Y location for the viewport.
<dt><i>y_return</i>
<dd>Returns the current Y location of the viewport.</dl><h2>Structures</h2><i>Video Mode Settings:</i>
<dl COMPACT><dd><pre>typedef struct {
 unsigned short hdisplay; /* Number of display pixels horizontally */
 unsigned short hsyncstart; /* Horizontal sync start */
 unsigned short hsyncend; /* Horizontal sync end */
 unsigned short htotal; /* Total horizontal pixels */
 unsigned short vdisplay; /* Number of display pixels vertically */
 unsigned short vsyncstart; /* Vertical sync start */
 unsigned short vsyncend; /* Vertical sync start */
 unsigned short vtotal; /* Total vertical pixels */
 unsigned int flags; /* Mode flags */
 int privsize; /* Size of private */
 INT32 *private; /* Server privates */
} XF86VidModeModeLine;
typedef struct {
 unsigned int dotclock; /* Pixel clock */
 unsigned short hdisplay; /* Number of display pixels horizontally */
 unsigned short hsyncstart; /* Horizontal sync start */
 unsigned short hsyncend; /* Horizontal sync end */
 unsigned short htotal; /* Total horizontal pixels */
 unsigned short vdisplay; /* Number of display pixels vertically */
 unsigned short vsyncstart; /* Vertical sync start */
 unsigned short vsyncend; /* Vertical sync start */
 unsigned short vtotal; /* Total vertical pixels */
 unsigned int flags; /* Mode flags */
 int privsize; /* Size of private */
 INT32 *private; /* Server privates */
} XF86VidModeModeInfo;</pre></dl>
 

 <i>Monitor information:</i>
<dl COMPACT><dd><pre>typedef struct {
 char* vendor; /* Name of manufacturer */
 char* model; /* Model name */
 float EMPTY; /* unused, for backward compatibility */
 unsigned char nhsync; /* Number of horiz sync ranges */
 XF86VidModeSyncRange* hsync; /* Horizontal sync ranges */
 unsigned char nvsync; /* Number of vert sync ranges */
 XF86VidModeSyncRange* vsync; /* Vertical sync ranges */
} XF86VidModeMonitor;
typedef struct {
 float hi; /* Top of range */
 float lo; /* Bottom of range */
} XF86VidModeSyncRange;
typedef struct {
 int type; /* of event */
 unsigned long serial; /* # of last request processed by server */
 Bool send_event; /* true if this came from a SendEvent req */
 Display *display; /* Display the event was read from */
 Window root; /* root window of event screen */
 int state; /* What happened */
 int kind; /* What happened */
 Bool forced; /* extents of new region */
 Time time; /* event timestamp */
} XF86VidModeNotifyEvent;
typedef struct {
 float red; /* Red Gamma value */
 float green; /* Green Gamma value */
 float blue; /* Blue Gamma value */
} XF86VidModeGamma;</pre></dl><h2>Description</h2>These functions provide an interface to the server extension <i>XFree86-VidModeExtension</i> which allows the video modes to be queried and adjusted dynamically and mode switching to be controlled. Applications that use these functions must be linked with <i>-lXxf86vm</i>
<h3>Modeline Functions</h3>The <i>XF86VidModeGetModeLine</i> function is used to query the settings for the currently selected video mode. The calling program should pass a pointer to a <i>XF86VidModeModeLine</i> structure that it has already allocated. The function fills in the fields of the structure. 

 If there are any server private values (currently only applicable to the S3 server) the function will allocate storage for them. Therefore, if the <i>privsize</i> field is non-zero, the calling program should call <i>Xfree(private)</i> to free the storage. 

 <i>XF86VidModeGetAllModeLines</i> returns the settings for all video modes. The calling program supplies the address of a pointer which will be set by the function to point to an array of <i>XF86VidModeModeInfo</i> structures. The memory occupied by the array is dynamically allocated by the <i>XF86VidModeGetAllModeLines</i> function and should be freed by the caller. The first element of the array corresponds to the current video mode. 

 The <i>XF86VidModeModModeLine</i> function can be used to change the settings of the current video mode provided the requested settings are valid (e.g. they don't exceed the capabilities of the monitor). 

 To add a mode to the list of available modes, the <i>XF86VidModeAddModeLine</i> function can be used. Assuming the settings are valid, the video mode will be added after the existing mode which matches the timings specified by the <i>aftermode</i> parameter. To be considered a match, all of the fields of the given <i>XF86VidModeModeInfo</i> structure must match, except the <i>privsize</i> and <i>private</i> fields. If the <i>aftermode</i> parameter is zero, the mode will be added after the current mode. 

 Modes can be deleted with the <i>XF86VidModeDeleteModeLine</i> function. The specified mode must match an existing mode. To be considered a match, all of the fields of the given <i>XF86VidModeModeInfo</i> structure must match, except the <i>privsize</i> and <i>private</i> fields. If the mode to be deleted is the current mode, a mode switch to the next mode will occur first. The last remaining mode can not be deleted. 

 The validity of a mode can be checked with the <i>XF86VidModeValidateModeLine</i> function. If the specified mode can be used by the server (i.e. meets all the constraints placed upon a mode by the combination of the server, card, and monitor) the function returns <i>MODE_OK</i>, otherwise it returns a value indicating the reason why the mode is invalid (as defined in <i>xf86.h</i>)
<h3>Mode Switch Functions</h3>When the function <i>XF86VidModeSwitchMode</i> is called, the server will change the video mode to next (or previous) video mode. The <i>XF86VidModeSwitchToMode</i> function can be used to switch directly to the specified mode. Matching is as specified in the description of the <i>XF86VidModeAddModeLine</i> function above. The <i>XF86VidModeLockModeSwitch</i> function can be used to allow or disallow mode switching whether the request to switch modes comes from a call to the <i>XF86VidModeSwitchMode</i> or <i>XF86VidModeSwitchToMode</i> functions or from one of the mode switch key sequences. 

 Note: Because of the asynchronous nature of the X protocol, a call to <i>XFlush</i> is needed if the application wants to see the mode change immediately. To be informed of the execution status of the request, a custom error handler should be installed using <i>XSetErrorHandler</i> before calling the mode switching function.
<h3>Monitor Functions</h3>Information known to the server about the monitor is returned by the <i>XF86VidModeGetMonitor</i> function. The <i>hsync</i> and <i>vsync</i> fields each point to an array of <i>XF86VidModeSyncRange</i> structures. The arrays contain <i>nhsync</i> and <i>nvsync</i> elements, respectively. The <i>hi</i> and <i>low</i> values will be equal if a discreate value was given in the <i>XF86Config</i> file. 

 The <i>vendor</i>, <i>model</i>, <i>hsync</i>, and <i>vsync</i> fields point to dynamically allocated storage that should be freed by the caller.
<h3>Viewport Functions</h3>The <i>XF86VidModeGetViewPort</i> and <i>XF86VidModeSetViewPort</i> functions can be used to, respectively, query and change the location of the upper left corner of the viewport into the virtual screen.
<h3>Other Functions</h3>The <i>XF86VidModeQueryVersion</i> function can be used to determine the version of the extension built into the server. 

 The function <i>XF86VidModeQueryExtension</i> returns the lowest numbered error and event values assigned to the extension.
<h2>Bugs</h2>The XF86VidModeSetClientVersion, XF86VidModeGetDotClocks, XF86VidModeGetGamma, XF86VidModeSetGamma, XF86VidModeSetGammaRamp, XF86VidModeGetGammaRamp, XF86VidModeGetGammaRampSize, and XF86VidModeGetPermissions functions need to be documented. In the meantime, check the source code for information about how to use them.
<h2>See Also</h2><a HREF="/docs/linux/man/1-xorg/">Xorg</a>(1), <a HREF="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a HREF="/docs/linux/man/3-xflush/">XFlush</a>(3), <a HREF="/docs/linux/man/3-xseterrorhandler/">XSetErrorHandler</a>(3), <a HREF="/docs/linux/man/1-xvidtune/">xvidtune</a>(1)
<h2>Authors</h2>Kaleb Keithley, Jon Tombs, David Dawes, and Joe Moss
