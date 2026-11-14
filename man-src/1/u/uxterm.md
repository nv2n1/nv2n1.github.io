---
title: "uxterm(1)"
name: "uxterm"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uxterm/"
description: "uxterm – X terminal emulator for Unicode (UTF-8) environments"
---

<h2 class="name">NAME</h2>
<p> uxterm &#8211; X terminal emulator for Unicode (UTF-8) environments </p>
<h2>SYNOPSIS</h2>
<p> <code>uxterm</code> [ <i>xterm-options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>uxterm</code> is a wrapper around the <code><a href="/docs/linux/man/1-xterm/">xterm</a>(1)</code> program that invokes the latter program with the &#8220;UXTerm&#8221; X resource class set. All arguments to <code>uxterm</code> are passed to <code>xterm</code> without processing; the <code>-class</code> and <code>-u8</code> options should not be specified because they are used by the wrapper. See the <code>xterm</code> manual page for more information on <i>xterm-options</i>. </p>
<p> The environment&#8217;s locale settings (see &#8220;ENVIRONMENT&#8221; below) are used to discern the locale&#8217;s character set. If no current locale can be determined, the locale &#8220;en_US&#8221; (the English language as used in the territory of the United States) is assumed. The <code><a href="/docs/linux/man/1-locale/">locale</a>(1)</code> utility is used to determine whether the system supports the selected locale. If it does not, <code>uxterm</code> will exit with an error and report the output of <code>locale</code>. </p>
<p> <code>Note: uxterm</code> may produce unexpected results if the current locale is set to one in which the UTF-8 character encoding is not supported, or if fonts using the ISO 10646-1 character set are not available. In the Debian system, the &#8220;xfonts-base&#8221; package provides the fonts that <code>uxterm</code> uses by default. To change the fonts <code>uxterm</code> uses, edit the <i>/etc/X11/app-defaults/UXTerm</i> file. </p>
<p> A similar wrapper, <code><a href="/docs/linux/man/1-koi8rxterm/">koi8rxterm</a>(1),</code> is available for KOI8-R environments.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code></p>
<dd> The values of these variables are checked, in order, to determine the character set used by the current locale.</dl>
<h2>AUTHOR</h2>
<p> Thomas Dickey</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a>(1),</code> <code><a href="/docs/linux/man/7-locale/">locale</a>(7),</code> <code><a href="/docs/linux/man/1-koi8rxterm/">koi8rxterm</a>(1),</code> <code><a href="/docs/linux/man/1-xterm/">xterm</a>(1)</code> </p>
<h2>Index</h2>
