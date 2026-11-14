---
title: "xf86miscsetsaver(3)"
name: "xf86miscsetsaver"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xf86miscsetsaver/"
description: "XF86MiscQueryExtension, XF86MiscQueryVersion, XF86MiscGetMouseSettings, XF86MiscSetMouseSettings, XF86MiscGetKbdSettings, XF86MiscSetKbdSettings – Extension library for the XFree86-Misc X extension."
---

<p>XF86MiscQueryExtension, XF86MiscQueryVersion, XF86MiscGetMouseSettings, XF86MiscSetMouseSettings, XF86MiscGetKbdSettings, XF86MiscSetKbdSettings &#8211; Extension library for the XFree86-Misc X extension.</p>
<h2>Syntax</h2>
<pre>#include &lt;X11/extensions/xf86misc.h&gt;
Bool XF86MiscQueryExtension(
 Display *<i>display</i>,
 int *<i>event_base_return</i>,
 int *<i>error_base_return</i>);
Bool XF86MiscQueryVersion(
 Display *<i>display</i>,
 int *<i>major_version_return</i>,
 int *<i>minor_version_return</i>);
Status XF86MiscGetMouseSettings(
 Display *<i>display</i>,
 XF86MiscMouseSettings *<i>mseinfo</i>);
Status XF86MiscSetMouseSettings(
 Display *<i>display</i>,
 XF86MiscMouseSettings *<i>mseinfo</i>);
Status XF86MiscGetKbdSettings(
 Display *<i>display</i>,
 XF86MiscKbdSettings *<i>kbdinfo</i>);
Status XF86MiscSetKbdSettings(
 Display *<i>display</i>,
 XF86MiscKbdSettings *<i>kbdinfo</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen</i></p>
<dd>Specifies which screen number the setting apply to.</p>
<dt><i>event_base_return</i></p>
<dd>Returns the base event number for the extension.</p>
<dt><i>error_base_return</i></p>
<dd>Returns the base error number for the extension.</p>
<dt><i>major_version_return</i></p>
<dd>Returns the major version number of the extension.</p>
<dt><i>minor_version_return</i></p>
<dd>Returns the minor version number of the extension.</p>
<dt><i>mseinfo</i></p>
<dd>Specifies a structure which contains the mouse parameters.</p>
<dt><i>kbdinfo</i></p>
<dd>Specifies a structure which contains the keyboard parameters.</dl>
<h2>Structures</h2>
<pre><i>Mouse:</i>
typedef struct {
 char *device; /* returned path to device */
 int type; /* mouse protocol */
 int baudrate; /* 1200, 2400, 4800, or 9600 */
 int samplerate; /* samples per second */
 int resolution; /* resolution, count per inch */
 int buttons; /* number of buttons */
 Bool emulate3buttons; /* Button1+Button3 -&gt; Button2 ? */
 int emulate3timeout; /* in milliseconds */
 Bool chordmiddle; /* Button1+Button3 == Button2 ? */
 int flags; /* Device open flags */
} XF86MiscMouseSettings;
<i>Keyboard:</i>
typedef struct {
 int type; /* of keyboard: 84-key, 101-key, Xqueue */
 int rate; /* repeat rate */
 int delay; /* delay until repeat starts */
 Bool servnumlock; /* Server handles NumLock ? */
} XF86MiscKbdSettings;</pre>
<h2>Description</h2>
<p>These functions provide an interface to the <i>XFree86-Misc</i> extension which allows various server settings to be queried and changed dynamically. Applications that use these functions must be linked with <i>-lXxf86misc</i></p>
<h3>Power-Saver Functions</h3>
<p>The <i>XF86MiscGetSaver</i> and <i>XF86MiscSetSaver</i> functions have been removed. This functionality is now provided by the DPMS extension.</p>
<h3>Mouse Functions</h3>
<p>Mouse parameters can be queried using the function <i>XF86MiscGetMouseSettings</i>. The structure pointed to by its second argument is filled in with the current mouse settings. </p>
<p> Not all fields are valid in all cases. For example, when the protocol indicates a bus mouse (i.e. the type field has value <i>MTYPE_BUSMOUSE</i> as defined in <i>xf86misc.h</i>), then the value in the <i>baudrate</i> field should be ignored as it does not apply to bus mice. </p>
<p> The <i>samplerate</i> field contains the resolution in lines per inch when using the Hitachi tablet protocol. </p>
<p> The device field of the structure points to dynamically allocated storage which should be freed by the caller. </p>
<p> Any of the fields of the structure can be altered and then passed to the <i>XF86MiscSetMouseSettings</i> function to change their value in the server, with the following restrictions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>1)</p>
<dd>The device can not be changed</p>
<dt>2)</p>
<dd>The protocol can not be changed to or from Xqueue or OsMouse</p>
<dt>3)</p>
<dd>The buttons field can not be changed</p>
<dt>4)</p>
<dd>Invalid combinations of parameters are not allowed</dl>
</dl>
<p> The server will generate an error if any of the above is attempted, except the first &#8211; the contents of the device field are simply ignored. </p>
<p> A change of the protocol causes the device to be closed and reopened. Changes to the baud rate, sample rate, resolution or flags, when applicable to the selected protocol, also cause a reopen of the device. A reopen can be forced by using the MF_REOPEN flag, except in the case of the OsMouse and Xqueue protocols which ignore all attempts to reopen the device.</p>
<h3>Keyboard Functions</h3>
<p>The <i>XF86MiscGetKbdSettings</i> function allows you to retrieve the current keyboard-related settings from the server. </p>
<p> Using the <i>XF86MiscSetKbdSettings</i> function, the keyboard autorepeat delay and rate can be set. Requests to change the <i>type</i> and <i>servnumlock</i> fields are ignored (except for checking for an invalid keyboard type). This is expected to change in a future release.</p>
<h3>Other Functions</h3>
<p>Two functions, <i>XF86MiscQueryExtension</i> and <i>XF86MiscQueryVersion</i>, are provided which allow the client to query some information regarding the extension itself.</p>
<h2>Predefined Values</h2>
<p>The header file <i>X11/extensions/xf86misc.h</i> contains definitions for</p>
<dl COMPACT>
<dt><code>MTYPE_</code>*</p>
<dd>Mouse protocols</p>
<dt><code>KTYPE_</code>*</p>
<dd>Keyboard types</p>
<dt><code>MF_</code>*</p>
<dd>Mouse flags</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xset/">xset</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5)</p>
<h2>Authors</h2>
<p>Joe Moss and David Dawes, The XFree86 Project, Inc.</p>
