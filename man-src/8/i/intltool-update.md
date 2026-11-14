---
title: "intltool-update(8)"
name: "intltool-update"
section: "8"
letter: "i"
url: "/docs/linux/man/8-intltool-update/"
description: "intltool-update – updates PO template file and merge translations with it"
---

<p>intltool-update &#8211; updates PO template file and merge translations with it</p>
<h2>Synopsis</h2>
<p><code>intltool-update</code><i> [option]&#8230;</i><br />
 <code>intltool-update</code><i> LANGCODE</i> </p>
<h2>Description</h2>
<p><code>intltool-update</code> generates new po file templates from source code, and merges existing translations with these new po templates. You must change working directory to the subdirectory containing translations (usually &quot;<i>po/</i>&quot;) before running <code>intltool-update</code>. </p>
<h2>Options</h2>
<p>When executing <code>intltool-update</code> , only one mode of operation is allowed each time.</p>
<h3>Mode of operation</h3>
<dl>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;pot</code></p>
<dd>Generate po template (.pot) only.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;headers</code></p>
<dd>Executes <code><a href="/docs/linux/man/8-intltool-extract/">intltool-extract</a></code>(8) to extract strings inside XML/INI style files listed in <code>POTFILES.in</code>, and writes the extracted strings into header files, so that the strings can be recognised by <code><a href="/docs/linux/man/1-xgettext/">xgettext</a></code>(1).</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;maintain</code></p>
<dd>Search for left out files, which should have been listed in <code>POTFILES.in</code> or <code>POTFILES.skip</code>. A list of all these files are written into another file called &quot;<code>missing</code>&quot;.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;report</code></p>
<dd>Display a status report for all translations in the software.</p>
<dt><code>-d </code><i>LANGCODE</i></p>
<dd>
<dt><code>&#8211;dist </code><i>LANGCODE</i></p>
<dd>Merge <code>LANGCODE</code>.po with existing PO template.</dl>
<h3>Other options</h3>
<dl>
<dt><code>-g </code><i>NAME</i></p>
<dd>
<dt><code>&#8211;gettext-package</code>=<i>NAME</i></p>
<dd>Manually specify PO template file name, instead of determining the name automatically from source. Useful with <code>-p</code>/<code>&#8211;pot</code> option. This option has an additional effect: the name of current working directory is no more limited to &quot;po&quot; or &quot;po-*&quot;.</p>
<dt><code>-o </code><i>FILENAME</i></p>
<dd>
<dt><code>&#8211;output-file</code>=<i>FILENAME</i></p>
<dd>Manually specify output <i>FILENAME</i> after merging old translation with PO template. Useful either with <code>-d</code>/<code>&#8211;dist</code> option or without any option.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Display lots of feedback.</p>
<dt><code>&#8211;version</code></p>
<dd>Show version information.</p>
<dt><code>&#8211;help</code></p>
<dd>Show usage and basic help information. </p>
</dl>
<h2>Examples</h2>
<p>Creates a new PO template from source code, and name it foo.pot:</p>
<dl>
<dd>
<pre>intltool-update --pot --gettext-package=foo</pre>
</dl>
<p> Updates translation file xy.po using existing po template called &quot;bar.pot&quot;, and writes output into &quot;xy1.po&quot;:</p>
<dl>
<dd>
<pre>intltool-update --dist --gettext-package=bar --output-file=xy1.po xy</pre>
</dl>
<p> Creates new PO template and updates translation file xy.po (xy.po is overwritten with new content):</p>
<dl>
<dd>
<pre>intltool-update xy</pre>
<p>(same as <code>intltool-update &#8211;pot &amp;&amp; intltool-update &#8211;dist xy</code>)</dl>
<h2>Files</h2>
<dl>
<dt><code>po/POTFILES.in</code></p>
<dd>Contains list of source files which contain translatable strings, one file per line.</p>
<dt><code>po/POTFILES.skip</code></p>
<dd>
<dt><code>po/POTFILES.ignore</code> (obsolete)</p>
<dd>Contains list of source files which should be ignored when searching for translatable strings. </p>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugs.launchpad.net/intltool">http://bugs.launchpad.net/intltool</a></p>
<h2>Author</h2>
<p>Darin Adler &lt;darin [at] bentspoon.com&gt;<br />
 Kenneth Christiansen &lt;kenneth [at] gnu.org&gt;<br />
 Maciej Stachowiak &lt;mjs [at] eazel.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-intltoolize/">intltoolize</a></code>(8), <code><a href="/docs/linux/man/8-intltool-prepare/">intltool-prepare</a></code>(8), <code><a href="/docs/linux/man/8-intltool-extract/">intltool-extract</a></code>(8), <code><a href="/docs/linux/man/8-intltool-merge/">intltool-merge</a></code>(8), <code><a href="/docs/linux/man/1-xgettext/">xgettext</a></code>(1) </p>
