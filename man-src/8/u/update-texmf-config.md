---
title: "update-texmf-config(8)"
name: "update-texmf-config"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-texmf-config/"
description: "update-texmf-config – script used in maintainer scripts to trigger tex-common actions"
---

<p>update-texmf-config &#8211; script used in maintainer scripts to trigger tex-common actions</p>
<h2>Synopsis</h2>
<p><code>update-texmf-config</code> <i>[options]</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>update-texmf-config</code> command. This manual page was written for the Debian GNU/Linux distribution because the original script was designed for Debian packaging system. </p>
<p> <code>update-texmf-config</code> is a shell script that is called from maintainer scripts shipping new map files, hyphenation patterns, or any other TeX input file. </p>
<p> The script simply activates the respective trigger, namely texmf-map for font map files, texmf-hyphen for hyphenation patterns, and texmf-format for format updates. All the necessary action will then be carried out by the tex-common package.</p>
<h2>Options</h2>
<dl>
<dt><code>map</code></p>
<dd>Activate the texmf-map trigger.</p>
<dt><code>hyphen</code></p>
<dd>Activate the texmf-hyphen trigger.</p>
<dt><code>format</code></p>
<dd>Activate the texmf-format trigger. </p>
</dl>
<h2>See Also</h2>
<p>Further information can be found in /usr/share/doc/tex-common/README.Debian.{txt,pdf.html} </p>
<h2>Author</h2>
<p>This manual page was written by Norbert Preining &lt;preining [at] logic.at&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
