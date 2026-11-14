---
title: "update-updmap(8)"
name: "update-updmap"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-updmap/"
description: "update-updmap – generate updmap.cfg files for all the system trees"
---

<p><code>update-updmap</code> &#8211; generate updmap.cfg files for all the system trees</p>
<h2>Synopsis</h2>
<p><code>update-updmap</code> [<i>option &#8230;</i> ]</p>
<h2>Description</h2>
<p>This manual page documents <code>update-updmap,</code> a program that was written for the Debian distribution.</p>
<h3>Overview</h3>
<p><code>update-updmap</code> is used to generate <a href="/docs/linux/man/1-updmap/">updmap</a>(1)Ns&#8217;s and updmap-sys8Ns&#8217;s configurations files /var/lib/texmf/updmap.cfg-TEXLIVEDIST which is the link target of /usr/share/texlive/texmf-dist/web2c/updmap.cfg and /var/lib/texmf/updmap.cfg-DEBIAN which is the link target of /usr/share/texmf/web2c/updmap.cfg from the files with names ending in `.cfg&#8217; located in /var/lib/tex-common/fontmap-cfg/texlive/ and /var/lib/tex-common/fontmap-cfg/texmf/ respectively. </p>
<p> Any TeX package shipping map files in one of the trees /usr/share/texlive/texmf-dist or /usr/share/texmf should also provide files in one of the above directories containing the respective lines for updmap.cfg file. </p>
<p> In order to configure (enable additional entries, disable system provided entries, etc), the normal <a href="/docs/linux/man/1-updmap/">updmap</a>(1) mechanism should be used. Please see the man page details.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd>Executes additional checks that all necessary files are present in the kpathsea database. Don&#8217;t use this in maintainer scripts.</p>
<dt><code>&#8211;quiet</code></p>
<dd>don&#8217;t write anything to the standard output during normal operation</p>
<dt><code>&#8211;help</code></p>
<dd>print a summary of the command-line usage of <code>update-updmap</code> and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</dl>
<p> Note that the &#8211;<code>v</code> option, which turns on verbose mode, is deprecated. We are currently in a transition phase where quiet mode is still the default (therefore, &#8211;<code>-quiet</code> has no effect), but <code>update-updmap</code> will be verbose by default as soon as enough packages use &#8211;<code>-quiet</code> in their maintainer scripts.</p>
<h2>Syntax For The .Cfg Files</h2>
<p>The `.cfg&#8217; files under /var/lib/tex-common/fontmap-cfg/ should contain valid configuration lines for <a href="/docs/linux/man/1-updmap/">updmap</a>(1). Usually, they will consist of lines of following one of these forms: </p>
<blockquote>
<pre>Map &lt;foo.map&gt;
MixedMap &lt;bar.map&gt;
KanjiMap &lt;baz.map&gt;</pre>
</blockquote>
<p> The <code>MixedMap</code> form should only be used if the font is available in both bitmap and scalable formats (this way, it won&#8217;t be declared in the default map file for Dvips that is used when <code>dvipsPreferOutline</code> is set to `false&#8217; in updmap.cfg ) </p>
<p> The KanjiMap form should only be used for map files defining Japanese font maps.</p>
<h2>Files</h2>
<pre>/var/lib/tex-common/fontmap-cfg/texlive/*.cfg
/var/lib/tex-common/fontmap-cfg/texmf/*.cfg
/var/lib/texmf/updmap.cfg-TEXLIVEDIST
/var/lib/texmf/updmap.cfg-DEBIAN</pre>
<h2>Diagnostics</h2>
<p><code>update-updmap</code> returns 0 on success, or a strictly positive integer on error.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-updmap/">updmap</a>(1) </p>
<pre>/usr/share/doc/tex-common/README.Debian.{txt,pdf,html}
/usr/share/doc/tex-common/Debian-TeX-Policy.{txt,pdf,html}
/usr/share/doc/tex-common/TeX-on-Debian.{txt,pdf,html}</pre>
<h2>Authors</h2>
<p>This manual page was written by An -nosplit An Atsuhito Kohda Aq kohda [at] debian.org and updated by An Florent Rougon Aq f.rougon [at] free.fr and An Frank Kuester Aq frank [at] debian.org for the Debian distribution (and may be used by others).</p>
