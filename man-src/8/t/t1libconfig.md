---
title: "t1libconfig(8)"
name: "t1libconfig"
section: "8"
letter: "t"
url: "/docs/linux/man/8-t1libconfig/"
description: "t1libconfig – create the t1lib.config and FontDataBase files for t1lib"
---

<p><code>t1libconfig</code> &#8211; create the t1lib.config and FontDataBase files for t1lib</p>
<h2>Synopsis</h2>
<p><code>t1libconfig</code> [ <code>-v</code>,<code>&#8211;version</code> ] [ <code>-h</code>,<code>&#8211;help</code> ] <code>&#8211;force</code> ] [ <code>fontdirectory&#8230;</code> ]</p>
<h2>Description</h2>
<p><code>t1libconfig</code> scans a list of directories for Type 1 fonts and font metric files, and generates a configuration file and font database file for the <code>t1lib</code> rasterizer library accordingly. By default, it looks in all subdirectories of /usr/X11R6/lib/X11/fonts, and in /usr/lib/ghostscript. Extra directories to search may be specified on the command line. The <code>t1libconfig</code> script tries not to scan the same directory twice (this is, however, not foolproof, since /usr/X11R6/lib/X11/fonts and /usr/lib/X11/fonts typically point to the same directory on GNU/Linux systems).</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>,<code>&#8211;version</code></p>
<dd>Print the version of <code>t1libconfig</code> and exit.</p>
<dt><code>-h</code>,<code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>&#8211;force</code></p>
<dd>Force the generation of new configuration files even if these files already exist on the system.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/t1lib/t1lib.config</code></p>
<dd>Contains configuration information for t1lib, including colon-separated lists of paths to Type 1 font files and font metrics files, and the location of the default font database file</p>
<dt><code>/etc/t1lib/FontDataBase</code></p>
<dd>Contains a list of the names of Type 1 font files to be used by t1lib.</dl>
<h2>Author</h2>
<p>David Huggins-Daines &lt;dhd [at] debian.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-fontdatabase/">FontDataBase</a></code>(5) </p>
