---
title: "xtdisplayinitialize(3)"
name: "xtdisplayinitialize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtdisplayinitialize/"
description: "XtDisplayInitialize, XtOpenDisplay, XtDatabase, XtScreenDatabase, XtCloseDisplay – initialize, open, or close a display"
---

<p>XtDisplayInitialize, XtOpenDisplay, XtDatabase, XtScreenDatabase, XtCloseDisplay &#8211; initialize, open, or close a display </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtDisplayInitialize(XtAppContext <i>app_context</i>, Display *<i>display</i>, const char *<i>application_name</i>, const char *<i>application_class</i>, XrmOptionDescRec *<i>options</i>, Cardinal <i>num_options</i>, int *<i>argc</i>, char **<i>argv</i>);</p>
<dd>Display *XtOpenDisplay(XtAppContext <i>app_context</i>, const char *<i>display_string</i>, const char *<i>application_name</i>, const char *<i>application_class</i>, XrmOptionDescRec *<i>options</i>, Cardinal <i>num_options</i>, int *<i>argc</i>, char **<i>argv</i>);</p>
<dd>void XtCloseDisplay(Display *<i>display</i>);</p>
<dd>XrmDatabase XtDatabase(Display *<i>display</i>);</p>
<dd>XrmDatabase XtScreenDatabase(Screen* <i>screen</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>argc</i></p>
<dd>Specifies a pointer to the number of command line parameters.</p>
<dt><i>argv</i></p>
<dd>Specifies the command line parameters.</p>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>application_class</i></p>
<dd>Specifies the class name of this application, which usually is the generic name for all instances of this application.</p>
<dt><i>application_name</i></p>
<dd>Specifies the name of the application instance.</p>
<dt><i>display</i></p>
<dd>Specifies the display. Note that a display can be in at most one application context.</p>
<dt><i>num_options</i></p>
<dd>Specifies the number of entries in the options list.</p>
<dt><i>options</i></p>
<dd>Specifies how to parse the command line for any application-specific resources. The options argument is passed as a parameter to <code>XrmParseCommand</code>. For further information, see <i>Xlib &#8211; C Language X Interface</i>.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen whose resource database is to be returned.</dl>
<h2>Description</h2>
<p>The <code>XtDisplayInitialize</code> function builds the resource database, calls the Xlib <code>XrmParseCommand</code> function to parse the command line, and performs other per display initialization. After <code>XrmParseCommand</code> has been called, argc and argv contain only those parameters that were not in the standard option table or in the table specified by the options argument. If the modified argc is not zero, most applications simply print out the modified argv along with a message listing the allowable options. On UNIX-based systems, the application name is usually the final component of argv[0]. If the synchronize resource is <code>True</code> for the specified application, <code>XtDisplayInitialize</code> calls the Xlib <code>XSynchronize</code> function to put Xlib into synchronous mode for this display connection. If the reverseVideo resource is <code>True</code>, the Intrinsics exchange <code>XtDefaultForeground</code> and <code>XtDefaultBackground</code> for widgets created on this display. (See Section 9.6.1). </p>
<p> The <code>XtOpenDisplay</code> function calls <code>XOpenDisplay</code> the specified display name. If display_string is NULL, <code>XtOpenDisplay</code> uses the current value of the -display option specified in argv and if no display is specified in argv, uses the user&#8217;s default display (on UNIX-based systems, this is the value of the DISPLAY environment variable). </p>
<p> If this succeeds, it then calls <code>XtDisplayInitialize</code> and pass it the opened display and the value of the -name option specified in argv as the application name. If no name option is specified, it uses the application name passed to <code>XtOpenDisplay</code>. If the application name is NULL, it uses the last component of argv[0]. <code>XtOpenDisplay</code> returns the newly opened display or NULL if it failed. </p>
<p> <code>XtOpenDisplay</code> is provided as a convenience to the application programmer. </p>
<p> The <code>XtCloseDisplay</code> function closes the specified display as soon as it is safe to do so. If called from within an event dispatch (for example, a callback procedure), <code>XtCloseDisplay</code> does not close the display until the dispatch is complete. Note that applications need only call <code>XtCloseDisplay</code> if they are to continue executing after closing the display; otherwise, they should call <code>XtDestroyApplicationContext</code> or just exit. </p>
<p> The <code>XtDatabase</code> function returns the fully merged resource database that was built by <code>XtDisplayInitialize</code> associated with the display that was passed in. If this display has not been initialized by <code>XtDisplayInitialize</code>, the results are not defined. </p>
<p> The <code>XtScreenDatabase</code> function returns the fully merged resource database associated with the specified screen. If the <i>screen</i> does not belong to a <code>Display</code> initialized by <code>XtDisplayInitialize</code>, the results are undefined.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappcreateshell/">XtAppCreateShell</a>(3), <a href="/docs/linux/man/3-xtcreateapplicationcontext/">XtCreateApplicationContext</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
