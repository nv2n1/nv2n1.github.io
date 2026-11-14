---
title: "gpt-virtual-pkg(8)"
name: "gpt-virtual-pkg"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-virtual-pkg/"
description: "gpt-virtual-pkg – Link external software into a GPT managed installation installation."
---

<p><code>gpt-virtual-pkg</code> &#8211; Link external software into a <font SIZE="-1">GPT</font> managed installation installation.</p>
<h2>Synopsis</h2>
<p><code>gpt-virtual-pkg</code> [options]</p>
<h2>Description</h2>
<p><code>gpt-virtual-pkg</code> Link external packages into a globus site installation. The script uses a description file to create the softlinks. The format of this file is defined in the file virtual_package.dtd.</p>
<h2>Options</h2>
<dl>
<dt><code>-installpath</code></p>
<dd>Overrides <tt>$GLOBUS_LOCATION</tt> to point to a globus site installation.</p>
<dt><code>-prefix</code></p>
<dd>Specifies the installation location of the external package</p>
<dt><code>-flavor</code></p>
<dd>Specifies the build flavor of the external package.</p>
<dt><code>-filelist=file</code></p>
<dd>Specifies the file containing the list of installed files..</p>
<dt><code>-gptfile=file</code></p>
<dd>Specifies the file containing the <font SIZE="-1">GPT</font> packaging data.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</dl>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
