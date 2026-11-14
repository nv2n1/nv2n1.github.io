---
title: "iconvconfig(8)"
name: "iconvconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iconvconfig/"
description: "iconvconfig – create iconv module configuration cache"
---

<p>iconvconfig &#8211; create iconv module configuration cache</p>
<h2>Synopsis</h2>
<p><code>iconvconfig</code> [<i>options</i>] [<i>directory</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) function internally uses <i>gconv</i> modules to convert to and from a character set. A configuration file is used to determine the needed modules for a conversion. Loading and parsing such a configuration file would slow down programs that use <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), so a caching mechanism is employed. </p>
<p> The <code>iconvconfig</code> program reads iconv module configuration files and writes a fast-loading gconv module configuration cache file. </p>
<p> In addition to the system provided gconv modules, the user can specify custom gconv module directories with the environment variable <code>GCONV_PATH</code>. However, iconv module configuration caching is used only when the environment variable <code>GCONV_PATH</code> is not set.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;nostdlib</code></p>
<dd>Do not search the system default gconv directory, only the directories provided on the command line.</p>
<dt><code>-o</code><i> outputfile</i><code>, &#8211;output=</code><i>outputfile</i></p>
<dd>Use <i>outputfile</i> for output instead of the system default cache location.</p>
<dt><code>&#8211;prefix=</code><i>pathname</i></p>
<dd>Set the prefix to be prepended to the system pathnames. See FILES, below. By default, the prefix is empty. Setting the prefix to <i>foo</i>, the gconv module configuration would be read from <i>foo/usr/lib/gconv/gconv-modules</i> and the cache would be written to <i>foo/usr/lib/gconv/gconv-modules.cache</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Print a usage summary and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Print a short usage summary and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version number, license, and disclaimer of warranty for <code>iconv</code>.</dl>
<h2>Exit Status</h2>
<p>Zero on success, nonzero on errors.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/gconv</i></p>
<dd>Usual default gconv module path.</p>
<dt><i>/usr/lib/gconv/gconv-modules</i></p>
<dd>Usual system default gconv module configuration file.</p>
<dt><i>/usr/lib/gconv/gconv-modules.cache</i></p>
<dd>Usual system gconv module configuration cache.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
