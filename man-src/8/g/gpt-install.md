---
title: "gpt-install(8)"
name: "gpt-install"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-install/"
description: "gpt-install – Installs GPT packages."
---

<p><code>gpt-install</code> &#8211; Installs GPT packages.</p>
<h2>Synopsis</h2>
<p><code>gpt-install</code> [options] [packages or bundles] </p>
<pre> Options:
 -verbose Print copious output
 -help Print usage
 -man Print man page.
 -version Print GPT version.
 -force Replace package no matter what.
 -loose Replace a broader range of packages.
 -installdir=PATH Override $GLOBUS_LOCATION.
 -tmpdir=PATH Path to tmp disk space
 [packages or bundles] List of binary packages and bundles to install.</pre>
<h2>Description</h2>
<p><code>gpt-install</code> takes a GPT described package or bundle and installs it. The program can install either RPM&#8216;s or GPT packages.</p>
<h2>Options</h2>
<dl>
<dt><code>-force</code></dt>
<dd>forces all action to be taken, regardless of state.</dd>
<dt><code>-tmpdir</code></dt>
<dd>Place to unpack bundles.</dd>
<dt><code>-installdir</code></dt>
<dd>Directory to which files shall be written. Default is <tt>$GLOBUS_LOCATION</tt></dd>
<dt><code>-loose</code></dt>
<dd>pgm packages can replace a pgm_static package (and vice versa) or a pgm package with a different flavor.</dd>
<dt><code>-help</code></dt>
<dd>Print a brief help message and exits.</dd>
<dt><code>-man</code></dt>
<dd>Prints the manual page and exits.</dd>
<dt><code>-version</code></dt>
<dd>Prints the version of GPT and exits.</dd></dl>
<h2>Examples</h2>
<p>For the command: </p>
<pre> gpt-install foo-2.1-gcc32-pgm.tar.gz
 foo-1.1-gcc32-pgm will be replaced.
 foo-2.2-gcc32-pgm will B&lt;not&gt; be replaced. It is newer.
 foo-1.1-vendorcc32-pgm will B&lt;not&gt; be replaced. Wrong flavor.
 foo-1.1-gcc32-pgm_static will B&lt;not&gt; be replaced. Wrong package type
 foo-2.2-gcc32-pgm_static will B&lt;not&gt; be replaced. Wrong package type</pre>
<p>For the command: </p>
<pre> gpt-install -force foo-2.1-gcc32-pgm.tar.gz
 foo-1.1-gcc32-pgm will be replaced.
 foo-2.2-gcc32-pgm will be replaced.
 foo-1.1-vendorcc32-pgm will B&lt;not&gt; be replaced. Wrong flavor
 foo-1.1-gcc32-pgm_static will B&lt;not&gt; be replaced. Wrong package type
 foo-2.2-gcc32-pgm_static will B&lt;not&gt; be replaced. Wrong package type</pre>
<p>For the command: </p>
<pre> gpt-install -loose foo-2.1-gcc32-pgm.tar.gz
 foo-1.1-gcc32-pgm will be replaced.
 foo-2.2-gcc32-pgm will B&lt;not&gt; be replaced. It is newer.
 foo-1.1-vendorcc32-pgm will be replaced.
 foo-1.1-gcc32-pgm_static will be replaced.
 foo-2.2-gcc32-pgm_static will B&lt;not&gt; be replaced. It is newer.</pre>
<p>For the command: </p>
<pre> gpt-install -force -loose foo-2.1-gcc32-pgm.tar.gz
 foo-1.1-gcc32-pgm will be replaced.
 foo-2.2-gcc32-pgm will be replaced.
 foo-1.1-vendorcc32-pgm will be replaced.
 foo-1.1-gcc32-pgm_static will be replaced.
 foo-2.2-gcc32-pgm_static will be replaced.</pre>
<h2>Bugs</h2>
<p><code>gpt-install</code> currently does not honor static build numbers. Instead it will replace any pgm_static package that is the same version or older. For example: </p>
<pre> gpt-install -force foo-2.1-2-gcc32-pgm_static.tar.gz
 foo-1.1-5-gcc32-pgm_static will be replaced.
 foo-2.1-1-gcc32-pgm_static will be replaced.
 foo-2.1-5-gcc32-pgm_static will be replaced.
 foo-2.2-1-gcc32-pgm_static will not be replaced.
 foo-2.1-gcc32-pgm will not be replaced.</pre>
<h2>See Also</h2>
<p><i>gpt-uninstall</i>(1) <i>gpt-query</i>(1) <i>gpt-verify</i>(1)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
