---
title: "xtopenapplication(3)"
name: "xtopenapplication"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtopenapplication/"
---

XtOpenApplication, XtVaOpenApplication - initialize, open, or close a display 

<h2>Syntax</h2>#include &lt;X11/Intrinsic.h&gt;
<dl COMPACT><dd>Widget XtOpenApplication(XtAppContext *<i>app_context_return</i>, const char *<i>application_class</i>, XrmOptionDescRec *<i>options</i>, Cardinal <i>num_options</i>, int *<i>argc_in_out</i>, char **<i>argv_in_out</i>, String *<i>fallback_resources</i>, WidgetClass <i>widget_class</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);
<dd>Widget XtVaOpenApplication(XtAppContext *<i>app_context_return</i>, const char *<i>application_class</i>, XrmOptionDescRec *<i>options</i>, Cardinal <i>num_options</i>, int *<i>argc_in_out</i>, char **<i>argv_in_out</i>, String *<i>fallback_resources</i>, WidgetClass <i>widget_class</i>, ...);</dl><h2>Arguments</h2><dl COMPACT><dt><i>app_context_return</i>
<dd>Specifies the application context.
<dt><i>application_class</i>
<dd>Specifies the class name of this application, which usually is the generic name for all instances of this application.
<dt><i>options</i>
<dd>Specifies how to parse the command line for any application-specific resources. The options argument is passed as a parameter to <b>XrmParseCommand</b>. For further information, see <i>Xlib - C Language X Interface</i>.
<dt><i>num_options</i>
<dd>Specifies the number of entries in the options list.
<dt><i>argc_in_out</i>
<dd>Specifies a pointer to the number of command line parameters.
<dt><i>argv_in_out</i>
<dd>Specifies the command line parameters.
<dt><i>fallback_resources</i>
<dd>Specifies resource values to be used if the application class resource file cannot be opened or read, or NULL.
<dt><i>widget_class</i>
<dd>Specifies the widget class of the shell to be created.
<dt><i>args</i>
<dd>Specifies the argument list to override any other resource specification for the created shell widget.
<dt><i>num_args</i>
<dd>Specifies the number of entries in the argument list.
<dt><i>...</i>
<dd>Specifies the variable argument list to override any other resource specification for the created shell widget.</dl><h2>Description</h2>The <b>XtOpenApplication</b> function calls <b>XtToolkitInitialize</b> followed by <b>XtCreateApplicationContext</b>, then calls <b>XtOpenDisplay</b> with <i>display_string</i> NULL and <i>application_name</i> NULL, and finally calls <b>XtAppCreateShell</b> with <i>application_name</i> NULL, the specified <i>widget_class</i>, and the specified <i>args</i> and <i>num_args</i> and returns the created shell. The modified <i>argc</i> and <i>argv</i> returned by <b>XtDisplayInitialize</b> are returned in <i>argc_in_out</i> and <i>argv_in_out</i>. If <i>app_context_return</i> is not NULL, the created application context is also returned. If the display specified by the command line cannot be opened, an error message is issued and <b>XtOpenApplication</b> terminates the application. If <i>fallback_resources</i> is non-NULL, <b>XtAppSetFallbackResources</b> is called with the value prior to calling <b>XtOpenDisplay</b>. 

 XtAppInitialize and XtVaAppInitialize have been superceded by <b>XtOpenApplication</b> and <b>XtVaOpenApplication</b> respectively.
<h2>See Also</h2><a HREF="/docs/linux/man/3-xtappinitialize/">XtAppInitialize</a>(3), <a HREF="/docs/linux/man/3-xtvaappinitialize/">XtVaAppInitialize</a>(3) 
 <i>X Toolkit Intrinsics - C Language Interface</i> 
 <i>Xlib - C Language X Interface</i>
