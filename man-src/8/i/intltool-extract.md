---
title: "intltool-extract(8)"
name: "intltool-extract"
section: "8"
letter: "i"
url: "/docs/linux/man/8-intltool-extract/"
description: "intltool-extract – generate header files which can be read by gettext"
---

<p>intltool-extract &#8211; generate header files which can be read by gettext</p>
<h2>Synopsis</h2>
<p><code>intltool-extract</code> <i>[options]&#8230; SOURCE_FILE</i> </p>
<h2>Description</h2>
<p><code>intltool-extract</code> extracts strings in the specified XML/INI type <i>SOURCE_FILE</i> and writes them into a C header file. Then <code><a href="/docs/linux/man/1-xgettext/">xgettext</a></code>(1) can merge these strings inside header file into po template. <code>intltool-extract</code> is usually not executed manually, but called from <code><a href="/docs/linux/man/8-intltool-update/">intltool-update</a></code>(8) instead. </p>
<h2>Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;local</code></p>
<dd>Creates a subdirectory under current working directory (named &quot;<code>tmp/</code>&quot;) and writes files there. This option can&#8217;t be used with <code>&#8211;update</code> option.</p>
<dt><code>&#8211;update</code></p>
<dd>Writes header file into the same directory the source file is in. New file name is the source file name appending &quot;.h&quot; extension. This option can&#8217;t be used with <code>-l</code>/<code>&#8211;local</code> option. Besides, this option is the default option if neither <code>&#8211;local</code> nor <code>&#8211;update</code> is specified.</p>
<dt><code>&#8211;type</code>=<i>TYPE</i></p>
<dd>Specify the type of source file. Currently supported types are:<br />
 &quot;gettext/glade&quot; (.glade, .glade2)<br />
 &quot;gettext/gsettings&quot; (.gschema.xml)<br />
 &quot;gettext/ini&quot; (Generic INI file)<br />
 &quot;gettext/keys&quot; (.keys)<br />
 &quot;gettext/rfc822deb&quot; (RFC 822 format file)<br />
 &quot;gettext/quoted&quot; (all strings within &quot;&quot;)<br />
 &quot;gettext/schemas&quot; (.schemas)<br />
 &quot;gettext/scheme&quot; (.scm)<br />
 &quot;gettext/xml&quot; (Generic XML file)<br />
 &quot;gettext/qtdesigner&quot; (Qt Designer .ui files)</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Show version information.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Show usage and basic help information.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd>Be quiet while running. </p>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugs.launchpad.net/intltool">http://bugs.launchpad.net/intltool</a></p>
<h2>Author</h2>
<p>Darin Adler &lt;darin [at] bentspoon.com&gt;<br />
 Kenneth Christiansen &lt;kenneth [at] gnu.org&gt;<br />
 Maciej Stachowiak &lt;mjs [at] eazel.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-intltoolize/">intltoolize</a></code>(8), <code><a href="/docs/linux/man/8-intltool-prepare/">intltool-prepare</a></code>(8), <code><a href="/docs/linux/man/8-intltool-merge/">intltool-merge</a></code>(8), <code><a href="/docs/linux/man/8-intltool-update/">intltool-update</a></code>(8), <code><a href="/docs/linux/man/1-xgettext/">xgettext</a></code>(1) </p>
