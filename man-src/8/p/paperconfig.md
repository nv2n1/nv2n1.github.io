---
title: "paperconfig(8)"
name: "paperconfig"
section: "8"
letter: "p"
url: "/docs/linux/man/8-paperconfig/"
description: "paperconfig – configure the system default paper size"
---

<p><code>paperconfig</code> &#8211; configure the system default paper size</p>
<h2>Synopsis</h2>
<p><code>paperconfig</code> [ <code>-v</code>,<code>&#8211;version</code> ] [ <code>-h</code>,<code>&#8211;help</code> ] [ <code>-p</code>, <code>&#8211;paper</code><i> papername</i> | <code>&#8211;force</code> ]</p>
<h2>Description</h2>
<p><code>paperconfig</code> sets the system (or default) paper to be used by tools using the <code>papersize</code> file. It can either ask interactively for the paper to use or be called non-interactively by scripts. </p>
<p> When the paper size has been changed, <code>paperconfig</code> notifies other packages of the change by running the scripts in the <i>/etc/libpaper.d</i> directory.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>,<code>&#8211;version</code></p>
<dd>Print the version of <code>paperconfig</code> and exit.</p>
<dt><code>-h</code>,<code>&#8211;help</code></p>
<dd>Print help about usage and exit.</p>
<dt><code>-p</code>, <code>&#8211;paper</code><i> papername</i></p>
<dd>Use <i>papername</i> if possible. If <i>papername</i> is not a valid paper, print an error message and exit.</p>
<dt><code>&#8211;force</code></p>
<dd>Force interactive selection of the system paper even if the actual paper is a valid one.</dl>
<h2>Environment</h2>
<p><code>PAPERCONF</code> Full path to a file containing the paper size to use; this file will be rewritten with the system paper size.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/papersize</code></p>
<dd>Contains the name of the system-wide default paper size to be used if the <code>PAPERSIZE</code> variable is not set.</p>
<dt><code>/etc/libpaper.d</code></p>
<dd>Directory of scripts to run after the paper size has been changed. This package puts no scripts here, but other packages may. <code>run-parts</code> is used to run the scripts, therefore their names must comply with <code>run-part&#8217;s</code> naming requirements.</dl>
<h2>Author</h2>
<p>Yves Arrouye &lt;arrouye [at] debian.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-paperconf/">paperconf</a></code>(1)<br />
 <code><a href="/docs/linux/man/5-papersize/">papersize</a></code>(5) </p>
