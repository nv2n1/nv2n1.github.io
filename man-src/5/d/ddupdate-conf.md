---
title: "ddupdate-conf(5)"
name: "ddupdate-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-ddupdate-conf/"
description: "ddupdate.conf – ddupdate configuration file."
---

<p><code>ddupdate.conf</code> &#8211; ddupdate configuration file.</p>
<h2>Synopsis</h2>
<p>The <code>ddupdate.conf</code> file holds default values for all <code><a href="/docs/linux/man/8-ddupdate/">ddupdate</a>(8)</code> options. Since <code>ddupdate</code> normally is invoked without command line parameters, this file then represents the used option values. </p>
<h2>File Format</h2>
<p>The file is formatted according to the rules use by the python3 configparser module. Basically, this is a leading <i>[update]</i> line followed by by <i> key = value</i> lines. The key represents the command line option, and <i>value</i> the value of said option. </p>
<p> The actual options available are documented in <code><a href="/docs/linux/man/8-ddupdate/">ddupdate</a>(8)</code>.</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-ddupdate/">ddupdate</a>(8)</code></p>
<dd>
<dt><code><a rel="nofollow" href="https://github.com/leamas/ddupdate">https://github.com/leamas/ddupdate</a></code></p>
<dd>Project homesite and README</p>
<dt><code><a rel="nofollow" href="https://docs.python.org/3/library/configparser.html">https://docs.python.org/3/library/configparser.html</a></code></p>
<dd>More info on file format. </p>
