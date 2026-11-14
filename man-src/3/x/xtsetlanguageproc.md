---
title: "xtsetlanguageproc(3)"
name: "xtsetlanguageproc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetlanguageproc/"
description: "XtSetLanguageProc – set the language procedure"
---

<p>XtSetLanguageProc &#8211; set the language procedure </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtLanguageProc XtSetLanguageProc(XtAppContext <i>app_context</i>, XtLanguageProc <i>proc</i>, XtPointer <i>client_data</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context in which the language procedure is to be used, or NULL.</dl>
<dl COMPACT>
<dt><i>proc</i></p>
<dd>Specifies the language procedure, or NULL.</dl>
<dl COMPACT>
<dt><i>client_data</i></p>
<dd>Specifies additional client data to be passed to the language procedure when it is called.</dl>
<h2>Description</h2>
<p><code>XtSetLanguageProc</code> sets the language procedure that will be called from <code>XtDisplayInitialize</code> for all subsequent Displays initialized in the specified application context. If <i>app_context</i> is NULL, the specified language procedure is registered in all application contexts created by the calling process, including any future application contexts that may be created. If <i>proc</i> is NULL a default language procedure is registered. <code>XtSetLanguageProc</code> returns the previously registered language procedure. If a language procedure has not yet been registered, the return value is unspecified but if this return value is used in a subsequent call to <code>XtSetLanguageProc</code>, it will cause the default language procedure to be registered. </p>
<p> The default language procedure does the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Sets the locale according to the environment. On ANSI C-based systems this is done by calling <code>setlocale</code>( <code>LC_ALL</code>, language ). If an error is encountered a warning message is issued with <code>XtWarning</code>.</p>
<dt>&bull;</p>
<dd>Calls <code>XSupportsLocale</code> to verify that the current locale is supported. If the locale is not supported, a warning message is issued with <code>XtWarning</code> and the locale is set to &#8220;C&#8221;.</p>
<dt>&bull;</p>
<dd>Calls <code>XSetLocaleModifiers</code> specifying the empty string.</p>
<dt>&bull;</p>
<dd>Returns the value of the current locale. On ANSI C-based systems this is the return value from a final call to <code>setlocale</code>( <code>LC_ALL</code>, NULL ).</dl>
<p> A client wishing to use this mechanism to establish locale can do so by calling <code>XtSetLanguageProc</code> prior to <code>XtDisplayInitialize.</code></p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
