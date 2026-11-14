---
title: "xclosedisplay(3)"
name: "xclosedisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xclosedisplay/"
description: "XOpenDisplay, XCloseDisplay – connect or disconnect to X server"
---

<p>XOpenDisplay, XCloseDisplay &#8211; connect or disconnect to X server </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Display *XOpenDisplay(char *<i>display_name</i>);</p>
<dd>int XCloseDisplay(Display *<i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>display_name</i></p>
<dd>Specifies the hardware display name, which determines the display and communications domain to be used. On a POSIX-conformant system, if the display_name is NULL, it defaults to the value of the DISPLAY environment variable.</dl>
<h2>Description</h2>
<p>The <code>XOpenDisplay</code> function returns a <code>Display</code> structure that serves as the connection to the X server and that contains all the information about that X server. <code>XOpenDisplay</code> connects your application to the X server through TCP or DECnet communications protocols, or through some local inter-process communication protocol. If the hostname is a host machine name and a single colon (:) separates the hostname and display number, <code>XOpenDisplay</code> connects using TCP streams. If the hostname is not specified, Xlib uses whatever it believes is the fastest transport. If the hostname is a host machine name and a double colon (::) separates the hostname and display number, <code>XOpenDisplay</code> connects using DECnet. A single X server can support any or all of these transport mechanisms simultaneously. A particular Xlib implementation can support many more of these transport mechanisms. </p>
<p> If successful, <code>XOpenDisplay</code> returns a pointer to a <code>Display</code> structure, which is defined in If <code>XOpenDisplay</code> does not succeed, it returns NULL. After a successful call to <code>XOpenDisplay</code>, all of the screens in the display can be used by the client. The screen number specified in the display_name argument is returned by the <code>DefaultScreen</code> macro (or the <code>XDefaultScreen</code> function). You can access elements of the <code>Display</code> and <code>Screen</code> structures only by using the information macros or functions. For information about using macros and functions to obtain information from the <code>Display</code> structure, see section 2.2.1. </p>
<p> The <code>XCloseDisplay</code> function closes the connection to the X server for the display specified in the <code>Display</code> structure and destroys all windows, resource IDs <code>Font</code>, <code>Pixmap</code>, <code>Colormap</code>, <code>Cursor</code>, and <code>GContext</code>), or other resources that the client has created on this display, unless the close-down mode of the resource has been changed (see <code>XSetCloseDownMode</code>). Therefore, these windows, resource IDs, and other resources should never be referenced again or an error will be generated. Before exiting, you should call <code>XCloseDisplay</code> explicitly so that any pending errors are reported as <code>XCloseDisplay</code> performs a final <code>XSync</code> operation. </p>
<p> <code>XCloseDisplay</code> can generate a <code>BadGC</code> error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-xflush/">XFlush</a>(3), <a href="/docs/linux/man/3-xsetclosedownmode/">XSetCloseDownMode</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
