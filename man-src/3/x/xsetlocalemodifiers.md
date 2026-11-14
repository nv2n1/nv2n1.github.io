---
title: "xsetlocalemodifiers(3)"
name: "xsetlocalemodifiers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetlocalemodifiers/"
description: "XSupportsLocale, XSetLocaleModifiers – determine locale support and configure locale modifiers"
---

<p>XSupportsLocale, XSetLocaleModifiers &#8211; determine locale support and configure locale modifiers </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Bool XSupportsLocale(void);</p>
<dd>char *XSetLocaleModifiers(char *<i>modifier_list</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>modifier_list</i></p>
<dd>Specifies the modifiers.</dl>
<h2>Description</h2>
<p>The <code>XSupportsLocale</code> function returns <code>True</code> if Xlib functions are capable of operating under the current locale. If it returns <code>False</code>, Xlib locale-dependent functions for which the <code>XLocaleNotSupported</code> return status is defined will return <code>XLocaleNotSupported</code>. Other Xlib locale-dependent routines will operate in the &#8220;C&#8221; locale. </p>
<p> The <code>XSetLocaleModifiers</code> function sets the X modifiers for the current locale setting. The modifier_list argument is a null-terminated string of the form &#8220;{@<i>category</i>=<i>value</i>}&#8221;, that is, having zero or more concatenated &#8220;@<i>category</i>=<i>value</i>&#8221; entries, where <i>category</i> is a category name and <i>value</i> is the (possibly empty) setting for that category. The values are encoded in the current locale. Category names are restricted to the POSIX Portable Filename Character Set. </p>
<p> The local host X locale modifiers announcer (on POSIX-compliant systems, the XMODIFIERS environment variable) is appended to the modifier_list to provide default values on the local host. If a given category appears more than once in the list, the first setting in the list is used. If a given category is not included in the full modifier list, the category is set to an implementation-dependent default for the current locale. An empty value for a category explicitly specifies the implementation-dependent default. </p>
<p> If the function is successful, it returns a pointer to a string. The contents of the string are such that a subsequent call with that string (in the same locale) will restore the modifiers to the same settings. If modifier_list is a NULL pointer, <code>XSetLocaleModifiers</code> also returns a pointer to such a string, and the current locale modifiers are not changed. </p>
<p> If invalid values are given for one or more modifier categories supported by the locale, a NULL pointer is returned, and none of the current modifiers are changed. </p>
<p> At program startup, the modifiers that are in effect are unspecified until the first successful call to set them. Whenever the locale is changed, the modifiers that are in effect become unspecified until the next successful call to set them. Clients should always call <code>XSetLocaleModifiers</code> with a non-NULL modifier_list after setting the locale before they call any locale-dependent Xlib routine. </p>
<p> The only standard modifier category currently defined is &#8220;im&#8221;, which identifies the desired input method. The values for input method are not standardized. A single locale may use multiple input methods, switching input method under user control. The modifier may specify the initial input method in effect or an ordered list of input methods. Multiple input methods may be specified in a single im value string in an implementation-dependent manner. </p>
<p> The returned modifiers string is owned by Xlib and should not be modified or freed by the client. It may be freed by Xlib after the current locale or modifiers are changed. Until freed, it will not be modified by Xlib.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
