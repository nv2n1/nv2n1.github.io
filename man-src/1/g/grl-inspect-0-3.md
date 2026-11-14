---
title: "grl-inspect-0-3(1)"
name: "grl-inspect-0-3"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grl-inspect-0-3/"
description: "grl-inspect – show information about Grilo sources and keys"
---

<p>grl-inspect &#8211; show information about Grilo sources and keys </p>
<h2>Synopsis</h2>
<p><code>grl-inspect</code> [<i>options</i>] [<i>source</i>|<i>key</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>grl-inspect</code> command. </p>
<p> <code>grl-inspect</code> is a tool that prints out information on available Grilo sources and metadata keys. When executed with no SOURCE argument, grl-inspect will print the list of all plugins and sources. When executed with a SOURCE, grl-inspect will print information about that source. </p>
<p> Alternatively, using <code>-k</code> prints out information about the available metadata keys.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of grl-inspect options.</p>
<dt><code>&#8211;help-grl</code></p>
<dd>Show summary of Grilo options.</p>
<dt><code>&#8211;help-all</code></p>
<dd>Show summary of all options.</p>
<dt><code>-k</code></p>
<dd>Show information about metadata keys</p>
<dt><code>-d, &#8211;delay</code><i> seconds</i></p>
<dd>Wait for some seconds before showing results. Useful when plugins may need some time for the source discovery process (example: UPnP). If not specified, by default it waits 1 second.</p>
<dt><code>-c, &#8211;config</code><i> config-file</i></p>
<dd>Configuration file to use with the plugins.</dl>
<h2>Author</h2>
<p>This manual page was written by Alberto Garcia &lt;berto [at] igalia.com&gt;.</p>
