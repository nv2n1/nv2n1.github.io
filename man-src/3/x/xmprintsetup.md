---
title: "xmprintsetup(3)"
name: "xmprintsetup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprintsetup/"
description: "XmPrintSetup — setup and create a Print Shell widget"
---

<p><code>XmPrintSetup</code> &#8212; setup and create a Print Shell widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Print.h&gt;
<code>Widget XmPrintSetup</code>(
<code>Widget video_widget</code>,
<code>Screen *print_screen</code>,
<code>String print_shell_name</code>,
<code>ArgList args</code>,
<code>Cardinal num_args</code>);</pre>
<h2>Description</h2>
<p>A function that does the appropriate setting and creates a realized <code>XmPrintShell</code> that it returns to the caller. This function hides the details of the <code>Xt</code> to set up a valid print shell heirarchy for the application. It is also meant to encourage consistency in the way applications root their print widget hierarchy. </p>
<p> <code>print_screen</code> must belong to a Display connection that has already been initialized with <code>Xt</code>. </p>
<p> The <code>video_widget</code> is used to get at the application context, application name and class, and <code>argc/argv</code> stored on the <code>applicationShell</code> that roots this widget. If no <code>applicationShell</code> is found, <code>NULL argv/argc</code> are used. </p>
<p> <code>XmPrintSetup</code> then creates an unrealized <code>ApplicationShell</code> with the same name and class as the one given by the video display, on the print display and on the print screen specified. </p>
<p> An <code>XmPrintShell</code> is then created as a child of this toplevel shell, using <code>XtCreatePopupShell</code>, with the name <code>print_shell_name</code>, and using the <code>args</code> provided. It then realizes and maps the print shell, using <code>XtPopup</code> with <code>XtGrabNone</code>. </p>
<p> This way, application resource files and users can specify print specific attributes using the following syntax (if <code>print_shell_name</code> is &quot;Print&quot;): </p>
<pre><tt>Dtpad.Print*textFontList: somefont
*Print*background:white
*Print*highlightThickness:0</tt></pre>
<dl COMPACT>
<dt><i>video_widget</i></p>
<dd>A video widget to fetch app video data from.</p>
<dt><i>print_screen</i></p>
<dd>A print screen on the print display &#8211; specifies the screen onto which the new shell is created.</p>
<dt><i>print_shell_name</i></p>
<dd>Specifies the name of the XmPrintShell created on the X Print server.</p>
<dt><i>args</i></p>
<dd>Specifies the argument list from which to get the resources for the XmPrintShell.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</dl>
<h2>Return Value</h2>
<p>The id the <code>XmPrintShell</code> widget created on the X Print Server connection, or NULL if an error has occured.</p>
<h2>Errors/Warnings</h2>
<p>None.</p>
<h2>Examples</h2>
<p>From the <code>OK</code> callback and the <code>SetUp</code> callback of the primary print dialog widget: </p>
<pre><tt>static void
printOKCB(Widget, XtPointer call_data, XtPointer client_data)
{
 AppPrint *p = (AppPrint *) client_data;
 DtPrintSetupCallbackStruct *pbs =
 (XmPrintCallbackStruct *) call_data;
 /* connect if not already done.
 the print dialog callback always provides valid
 printer name, print display and screen
 already initialized: XpInitContext called */
 */
 p-&gt;print_shell = XmPrintSetup (widget, pbs-&gt;print_screen,
 &quot;Print&quot;, NULL, 0);
 ...
}</tt></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintshell/">XmPrintShell</a></code>(3), <code><a href="/docs/linux/man/3-xmredisplaywidget/">XmRedisplayWidget</a></code>(3), <code><a href="/docs/linux/man/3-xmprinttofile/">XmPrintToFile</a></code>(3), <code><a href="/docs/linux/man/3-xmprintpopuppdm/">XmPrintPopupPDM</a></code>(3)</p>
