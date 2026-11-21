---
title: "grl-inspect(1)"
name: "grl-inspect"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grl-inspect/"
description: "grl-inspect – show information about Grilo sources and keys"
---

<h2>SYNOPSIS</h2>
<p> <code>grl-inspect</code> [<i>options</i>] [<i>source</i>|<i>key</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>grl-inspect</code> command. </p>
<p> <code>grl-inspect</code> is a tool that prints out information on available Grilo sources and metadata keys. When executed with no SOURCE argument, grl-inspect will print the list of all plugins and sources. When executed with a SOURCE, grl-inspect will print information about that source. </p>
<p> Alternatively, using <code>-k</code> prints out information about the available metadata keys.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of grl-inspect options.</dd>
<dt><code>&#8211;help-grl</code></dt>
<dd> Show summary of Grilo options.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show summary of all options.</dd>
<dt><code>-k</code></dt>
<dd> Show information about metadata keys</dd>
<dt><code>-d, &#8211;delay</code><i> seconds</i></dt>
<dd> Wait for some seconds before showing results. Useful when plugins may need some time for the source discovery process (example: UPnP). If not specified, by default it waits 1 second.</dd>
<dt><code>-c, &#8211;config</code><i> config-file</i></dt>
<dd> Configuration file to use with the plugins.</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Alberto Garcia &lt;agarcia [at] igalia.com&gt;. </p>
