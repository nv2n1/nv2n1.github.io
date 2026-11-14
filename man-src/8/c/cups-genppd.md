---
title: "cups-genppd(8)"
name: "cups-genppd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-genppd/"
description: "cups-genppd – generate Gutenprint PPD files for use with CUPS"
---

<p>cups-genppd &#8211; generate Gutenprint PPD files for use with CUPS</p>
<h2>Synopsis</h2>
<p><code>cups-genppd</code> [<i>-c localedir</i>] [<i>-l locale</i>] [<i>-p prefix</i>] [<i>-q</i>] [<i>-v</i>] <i>model1</i> <i>[model2, &#8230;modeln]</i><br />
 <code>cups-genppd</code> <i>-L </i>[<i>-c localedir</i>]<br />
 <code>cups-genppd</code> <i>-M </i>[<i>-v</i>]<br />
 <code>cups-genppd</code> <i>-h</i><br />
 <code>cups-genppd</code> <i>-V</i></p>
<h2>Description</h2>
<p><code>cups-genppd</code> generates <i>Gutenprint</i> PPD files for use with CUPS. The default behavior is to output PPD files for all models of printer that the <i>Gutenprint</i> printer driver library supports. You may restrict the models by listing either the driver names or the full names of the printers you wish to generate PPD files for after any options. Additionally, the PPD files may be <i>localised</i>, that is, translated, to use your native language rather than US English. There are commands to find out what printer models and languages are supported.</p>
<h2>Examples</h2>
<dl>
<dt><code>cups-genppd -v bjc-6200 &#8216;Epson Stylus Photo 1280&#8217; &#8216;HP DeskJet 850C&#8217;</code></p>
<dd>verbosely generate three PPD files, listing the driver name in the first case, and the full name in the second.</p>
<dt><code>LANG=de_DE genppd -p ppd -c /usr/share/locale</code></p>
<dd>generate PPDs for all available models, in directory <i>ppd</i> using the locale data found under <i>/usr/share/locale</i>. The language to use is taken from the environment (de_DE).</p>
<dt><code>cups-genppd -L -c /usr/local/share/locale</code></p>
<dd>list available languages using the locale data found under <i>/usr/local/share/locale</i>.</p>
<dt><code>cups-genppd -M -v</code></p>
<dd>list available drivers, with long model descriptions</dl>
<h2>Commands</h2>
<dl>
<dt><code>-h</code></p>
<dd>show a help message</p>
<dt><code>-L</code></p>
<dd>list available translations (message catalogs). If a locale is used for which there is not a corresponding translation, then then US English will be used.</p>
<dt><code>-M</code></p>
<dd>list available printer models. By default, only driver names are listed; if verbose mode is used, the full model name will also be printed</p>
<dt><code>-V</code></p>
<dd>show version information and defaults</p>
<dd>The default behavior is to output PPDs if no command is given.</dl>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>localedir</i></p>
<dd>use <i>localedir</i> as the base directory for locale data</p>
<dt><code>-l</code> <i>locale</i></p>
<dd>output PPDs translated with messages for <i>locale</i>. Note that <i>locale</i> <code>must</code> be a locale as shown by <i>locale -a</i>. For example, the <i>de</i> translation is used by the <i>de_DE</i> locale; <i>de</i> alone will not work.</p>
<dt><code>-p</code> <i>prefix</i></p>
<dd>output PPDs in directory <i>prefix</i>. Directories are <code>not</code> recursively created.</p>
<dt><code>-q</code></p>
<dd>Quiet mode.</p>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>models</code></p>
<dd>a list of printer models, either the driver or quoted full name.</dl>
<h2>See Also</h2>
<p>CUPS Software Administrators Manual, <a rel="nofollow" href="http://localhost:631/documentation.html">http://localhost:631/documentation.html</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 1992-2002 Michael Sweet (mike [at] easysw.com) </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<p> This manual page was written by Roger Leigh (rleigh [at] debian.org).</p>
