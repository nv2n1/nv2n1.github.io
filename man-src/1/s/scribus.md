---
title: "scribus(1)"
name: "scribus"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scribus/"
description: "scribus – cross platform WYSIWYG desktop publishing app"
---

<h2>NAME</h2>
<p> scribus &#8211; cross platform WYSIWYG desktop publishing app</p>
<h2>SYNOPSIS</h2>
<p> scribus [-h|&#8211;help] [-v|&#8211;version] [-l|&#8211;lang language] [-la|&#8211;langs-available] [-f|&#8211;file|&#8211;] [filename]</p>
<h2>DESCRIPTION</h2>
<p> Scribus is an open source desktop publishing program. It provides true WYSIWYG editing, excellent PDF export facilities, and a wide range of other input and output options. </p>
<p> Please see the scribus documentation at <i><a rel="nofollow" href="http://docs.scribus.net/">http://docs.scribus.net/</a></i> or the program&#8217;s built in help for more comprehensive and up-to-date documentation. </p>
<p> This man page only provides summaries of some aspects of the program&#8217;s use. It&#8217;s main purpose is to make sure you can find the full documentation quickly and easily.</p>
<h2>OPTIONS</h2>
<p> The definitive options are in the program&#8217;s usage statement. Run: <code>scribus &#8211;help</code> to view the usage statement. </p>
<dl>
<dt><code>-l, &#8211;lang xx</code></p>
<dd> Overrides the system locale and runs Scribus in language xx. The language is specified with the same POSIX language codes that are used in the LANG and LC_ALL environment variables. For example, English can be selected with &#8216;en&#8217; (generic English), &#8216;en_GB&#8217; (British English), &#8216;en_US&#8217; (American english), etc. Similarly, Deutsch can be selected with &#8216;de&#8217; or &#8216;de_DE&#8217;.</p>
<dt><code>-la, &#8211;langs-available</code></p>
<dd> Print a list of languages for which user interface translations are available. To use that language run Scribus as &#8216;scribus -l xx&#8217; where xx is the short language code, or set the locale environment variables as described below.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints the Scribus version number and exits.</p>
<dt><code>-f, &#8211;file</code></p>
<dd> Open the specified file. It&#8217;s possible to simply pass the file name as an unqualified argument instead of using this, though if the name begins with a &#8211; you will need to use &#8211;, eg &#8216;scribus &#8212; -myfile.sla&#8217;.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a brief usage summary.</p>
<dt><code>-fi, &#8211;font-info </code></p>
<dd> Shows the font file listing as Scribus starts. This can be used for diagnosing missing glyphs within fonts or possible broken font files.</p>
<dt><code>-pi, &#8211;profile-info </code></p>
<dd> Shows the color profiles listing which Scribus can use. This can be used for diagnosing missing or broken color profiles.</p>
<dt><code>-ns, &#8211;no-splash</code></p>
<dd> Suppresses display of the splash screen during Scribus start-up.</p>
<dt><code>-nns, &#8211;never-splash </code></p>
<dd> Stop the showing of the splashscreen on startup. Writes an empty file called .neversplash in ~/.scribus.</p>
<dt><code>-sb, &#8211;swap-buttons</code></p>
<dd> Use right to left dialog button ordering (eg. Cancel/No/Yes instead of Yes/No/Cancel)</p>
<dt><code>-u, &#8211;upgradecheck</code></p>
<dd> Downloads a file from our scribus server indicating latest available versions. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> Scribus respects the standard locale environment variables. Others may be used through underlying libraries, such as Qt, or by programs used by Scribus. <i><a rel="nofollow" href="http://docs.scribus.net/">http://docs.scribus.net/</a></i> and the in-program documentation may note other environment variables used by Scribus or the programs and libraries it uses.</p>
<dl>
<dt><code>LC_ALL, LC_MESSAGES, LANG</code></p>
<dd> POSIX locale. See <i><a href="/docs/linux/man/1-locale/">locale</a>(1).</i> Scribus uses these three environment variables, in the listed order of precedence, to select the language (including the user interface translation) to use. If none are set, it will fall back on the locale set by the underlying Qt library.</p>
<dt><code>PATH</code></p>
<dd> Scribus may search the PATH for external tools if their paths are not specified absolutely. This is currently most likely to affect you if you have multiple copies of <a href="/docs/linux/man/1-gs/">gs</a>(1) installed. You can set an absolute path to the correct <a href="/docs/linux/man/1-gs/">gs</a>(1) in your Scribus preferences and bypass the <code>PATH</code> search.</dl>
<p> A few important environment variables from other programs are summarised here for convenience, though you should check the original program&#8217;s documentation if you are having trouble.</p>
<dl>
<dt><code>GS_FONTPATH</code></p>
<dd> GhostScript font path. Affects the font search path for GhostScript, a component Scribus uses for some PostScript operations. Add new directories containing fonts to this colon-separated list to help GhostScript find fonts in non-standard locations. See <a href="/docs/linux/man/1-gs/">gs</a>(1) and the GhostScript HTML documentation for more information.</p>
<dt><code>GS_LIB</code></p>
<dd> GhostScript library path. GhostScript searches this path for Fontmap files. Like <code>GS_FONTPATH</code> it&#8217;s a colon separated list of directories. You will usually want to use <code>GS_FONTPATH</code> instead, though building a Fontmap file and using <code>GS_LIB</code> can speed things up if you have a <i>lot</i> of fonts. See <a href="/docs/linux/man/1-gs/">gs</a>(1) and the GhostScript HTML documentation for more information.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.scribus/</code></p>
<dd> User preferences are stored in $HOME/.scribus/ on Unix or Linux . Most other paths are configurable from the Scribus preferences. Scribus 1.3 preferences are separate from Scribus 1.2.x User preferences for Mac OS X, OS/2 and Windows are documented in the help docs (F1) in Scribus. <code>$HOME/.scribus/scribus13.rc</code> Scribus preferences file &#8211; formatted in a custom xml schema. May eventually be retired in favour of new format prefs file. <code>$HOME/.scribus/prefs13.xml</code> Scribus 1.3.8 preferences are separate from Scribus 1.3.3.x</p>
<dt><code>$HOME/.fonts/</code></p>
<dd>
<dt><code>$HOME/.fonts.conf</code></p>
<dd>
<dt><code>/etc/fonts</code></p>
<dd> Fontconfig, the library used by Scribus to locate fonts, is normally configured with files in /etc/fonts, mainly /etc/fonts/fonts.conf and /etc/fonts/local.conf . It may also use a config file $HOME/.fonts.conf and fonts in $HOME/.fonts/ . See <a href="/docs/linux/man/5-fonts-conf/">fonts.conf</a>(5) and the fontconfig documentation for more information. Note that Scribus may also use its internal font path to locate more fonts &#8211; see the Preferences dialog and scribus help.</dl>
<h2>SEE ALSO</h2>
<p> The scribus documentation site <a rel="nofollow" href="http://docs.scribus.net/">http://docs.scribus.net/</a> and home page <a href="http://www.scribus.net/">http://www.scribus.net/</a> </p>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1), the gs html docs, and <a rel="nofollow" href="http://www.ghostscript.com/">http://www.ghostscript.com/</a> </p>
<p> The Qt library &#8211; <a rel="nofollow" href="http://www.trolltech.com/">http://www.trolltech.com/</a> </p>
<p> <a href="/docs/linux/man/5-fonts-conf/">fonts-conf</a>(5) for info on configuring FontConfig</p>
<h2>RELATED SOFTWARE AND AFFILIATES</h2>
<p> <a href="/docs/linux/man/1-inkscape/">inkscape</a>(1) &#8211; <a rel="nofollow" href="http://inkscape.org/">http://inkscape.org/</a> </p>
<p> OpenClipArt &#8211; <a rel="nofollow" href="http://openclipart.org/">http://openclipart.org/</a> </p>
<p> Fontmatrix &#8211; <a rel="nofollow" href="http://fontmatrix.net">http://fontmatrix.net</a> </p>
<p> Other affiliates may be listed in the footer on <a rel="nofollow" href="http://www.scribus.net/">http://www.scribus.net/</a> </p>
<h2>BUGS</h2>
<p> See <i><a rel="nofollow" href="http://bugs.scribus.net/">http://bugs.scribus.net/</a></i> for the Scribus on-line status tracker, which is used to track bug reports and feature requests. <code>If you intend to submit a bug report or feature request, please search the bug database first.</code></p>
<h2>AUTHORS</h2>
<p> Please see the About Scribus option in the Help menu for a list of authors, translators, and contributors. </p>
<h2>Index</h2>
