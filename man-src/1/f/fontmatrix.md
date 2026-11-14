---
title: "fontmatrix(1)"
name: "fontmatrix"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontmatrix/"
description: "fontmatrix – a powerful open source font manager"
---

<h2>NAME</h2>
<p> fontmatrix &#8211; a powerful open source font manager </p>
<h2>SYNOPSIS</h2>
<p> fontmatrix [-h|&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Fontmatrix is an open source font manager originally developed on Linux, but now runs on OSX as well. </p>
<p> This man page only provides summaries of some aspects of the program&#8217;s use. It&#8217;s main purpose is to make sure you can find the full documentation quickly and easily.</p>
<h2>OPTIONS</h2>
<p> The definitive options are in the program&#8217;s usage statement. Run: <code>fontmatrix &#8211;help</code> to view the usage statement. </p>
<dl>
<dt><code>-l, &#8211;lang xx</code></p>
<dd> Overrides the system locale and runs Fontmatrix in language xx. The language is specified with the same POSIX language codes that are used in the LANG and LC_ALL environment variables. For example, English can be selected with &#8216;en&#8217; (generic English), &#8216;en_GB&#8217; (British English), &#8216;en_US&#8217; (American english), etc. Similarly, Deutsch can be selected with &#8216;de&#8217; or &#8216;de_DE&#8217;.</p>
<dt>
<dd> <code>-la, &#8211;langs-available</code> Print a list of languages for which user interface translations are available. To use that language run Fontmatrix as &#8216;fontmatrix -l xx&#8217; where xx is the short language code, or set the locale environment variables as described below.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints the Fontmatrix version number and exits.</p>
<dt><code>-f, &#8211;file</code></p>
<dd> Open the specified file. It&#8217;s possible to simply pass the file name as an unqualified argument instead of using this, though if the name begins with a &#8211; you will need to use &#8211;, eg &#8216;fontmatrix &#8212; -myfile.sla&#8217;.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a brief usage summary.</p>
<dt><code>-ns, &#8211;no-splash</code></p>
<dd> Suppresses display of the splash screen during SCribus start-up.</dl>
<h2>ENVIRONMENT</h2>
<p> Fontmatrix respects the standard locale environment variables. Others may be used through underlying libraries, such as Qt, or by programs used by Fontmatrix. <code>LC_ALL, LC_MESSAGES, LANG</code> POSIX locale. See <i><a href="/docs/linux/man/1-locale/">locale</a>(1).</i> Fontmatrix uses these three environment variables, in the listed order of precedence, to select the language (including the user interface translation) to use. If none are set, it will fall back on the locale set by the underlying Qt library.</p>
<dl>
<dt><code>PATH</code></p>
<dd> Fontmatrix may search the PATH for external tools if their paths are not specified absolutely. This is currently most likely to affect you if you have multiple copies of <a href="/docs/linux/man/1-fontforge/">fontforge</a>(1) installed. You can set an absolute path to the correct <a href="/docs/linux/man/1-fontforge/">fontforge</a>(1) in your Fontmatrix preferences and bypass the <code>PATH</code> search.</dl>
<p> A few important environment variables from other programs are summarised here for convenience, though you should check the original program&#8217;s documentation if you are having trouble.</p>
<dl>
<dt></dl>
<h2>FILES</h2>
<dd>
<dl>
<dt><code>$HOME/.fontmatrix/</code></p>
<dd> User preferences are stored in $HOME/.fontmatrix/ on Unix or Linux. Most other paths are configurable from the Fontmatrix preferences. <code>$HOME/.fonts/</code></p>
<dt><code>$HOME/.fonts.conf</code></p>
<dd>
<dt><code>/etc/fonts</code></p>
<dd> Fontconfig, the library used by Fontmatrix to locate fonts, is normally configured with files in /etc/fonts, mainly /etc/fonts/fonts.conf and /etc/fonts/local.conf . It may also use a config file $HOME/.fonts.conf and fonts in $HOME/.fonts/ . See <a href="/docs/linux/man/5-fonts-conf/">fonts.conf</a>(5) and the fontconfig documentation for more information. Note that Fontmatrix may also use its internal font path to locate more fonts &#8211; see the Preferences dialog and fontmatrix help.</dl>
<h2>RELATED SOFTWARE AND AFFILIATES</h2>
<p> Scribus &#8211; <a rel="nofollow" href="http://www.scribus.net">http://www.scribus.net</a> </p>
<p> Other affiliates may be listed in the footer on <a rel="nofollow" href="http://www.fontmatrix.net/">http://www.fontmatrix.net/</a> </p>
<h2>BUGS</h2>
<p> See <i><a rel="nofollow" href="https://gna.org/bugs/?group=undertype">https://gna.org/bugs/?group=undertype</a></i> for the Fontmatrix on-line status tracker, which is used to track bug reports and feature requests. <code>If you intend to submit a bug report or feature request, please search the bug database first.</code></p>
<h2>AUTHORS</h2>
<p> Please see the About Fontmatrix option in the Help menu for a list of authors, translators, and contributors. </p>
<h2>Index</h2>
