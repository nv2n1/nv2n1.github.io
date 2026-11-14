---
title: "xgeterrordatabasetext(3)"
name: "xgeterrordatabasetext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgeterrordatabasetext/"
description: "XSetErrorHandler, XGetErrorText, XDisplayName, XSetIOErrorHandler, XGetErrorDatabaseText – default error handlers"
---

<p>XSetErrorHandler, XGetErrorText, XDisplayName, XSetIOErrorHandler, XGetErrorDatabaseText &#8211; default error handlers </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int (*XSetErrorHandler(int (*<i>handler</i>)(Display *, XErrorEvent *)))();</p>
<dd>int XGetErrorText(Display *<i>display</i>, int <i>code</i>, char *<i>buffer_return</i>, int <i>length</i>);</p>
<dd>char *XDisplayName(char *<i>string</i>);</p>
<dd>int (*XSetIOErrorHandler(int (*<i>handler</i>)(Display *)))();</p>
<dd>int XGetErrorDatabaseText(Display *<i>display</i>, char *<i>name</i>, char *<i>message</i>, char *<i>default_string</i>, char *<i>buffer_return</i>, int <i>length</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>buffer_return</i></p>
<dd>Returns the error description.</p>
<dt><i>code</i></p>
<dd>Specifies the error code for which you want to obtain a description.</p>
<dt><i>default_string</i></p>
<dd>Specifies the default error message if none is found in the database.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>handler</i></p>
<dd>Specifies the program&#8217;s supplied error handler.</p>
<dt><i>length</i></p>
<dd>Specifies the size of the buffer.</p>
<dt><i>message</i></p>
<dd>Specifies the type of the error message.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the application.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</dl>
<h2>Description</h2>
<p>Xlib generally calls the program&#8217;s supplied error handler whenever an error is received. It is not called on <code>BadName</code> errors from <code>OpenFont</code>, <code>LookupColor</code>, or <code>AllocNamedColor</code> protocol requests or on <code>BadFont</code> errors from a <code>QueryFont</code> protocol request. These errors generally are reflected back to the program through the procedural interface. Because this condition is not assumed to be fatal, it is acceptable for your error handler to return; the returned value is ignored. However, the error handler should not call any functions (directly or indirectly) on the display that will generate protocol requests or that will look for input events. The previous error handler is returned. </p>
<p> The <code>XGetErrorText</code> function copies a null-terminated string describing the specified error code into the specified buffer. The returned text is in the encoding of the current locale. It is recommended that you use this function to obtain an error description because extensions to Xlib may define their own error codes and error strings. </p>
<p> The <code>XDisplayName</code> function returns the name of the display that <code>XOpenDisplay</code> would attempt to use. If a NULL string is specified, <code>XDisplayName</code> looks in the environment for the display and returns the display name that <code>XOpenDisplay</code> would attempt to use. This makes it easier to report to the user precisely which display the program attempted to open when the initial connection attempt failed. </p>
<p> The <code>XSetIOErrorHandler</code> sets the fatal I/O error handler. Xlib calls the program&#8217;s supplied error handler if any sort of system call error occurs (for example, the connection to the server was lost). This is assumed to be a fatal condition, and the called routine should not return. If the I/O error handler does return, the client process exits. </p>
<p> Note that the previous error handler is returned. </p>
<p> The <code>XGetErrorDatabaseText</code> function returns a null-terminated message (or the default message) from the error message database. Xlib uses this function internally to look up its error messages. The text in the default_string argument is assumed to be in the encoding of the current locale, and the text stored in the buffer_return argument is in the encoding of the current locale. </p>
<p> The name argument should generally be the name of your application. The message argument should indicate which type of error message you want. If the name and message are not in the Host Portable Character Encoding, the result is implementation-dependent. Xlib uses three predefined &#8220;application names&#8221; to report errors. In these names, uppercase and lowercase matter.</p>
<dl COMPACT>
<dt>XProtoError</p>
<dd>The protocol error number is used as a string for the message argument.</p>
<dt>XlibMessage</p>
<dd>These are the message strings that are used internally by the library.</p>
<dt>XRequest</p>
<dd>For a core protocol request, the major request protocol number is used for the message argument. For an extension request, the extension name (as given by <code>InitExtension</code>) followed by a period (.) and the minor request protocol number is used for the message argument. If no string is found in the error database, the default_string is returned to the buffer argument.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a>(3), <a href="/docs/linux/man/3-xsynchronize/">XSynchronize</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
