---
title: "pmxchords(1)"
name: "pmxchords"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmxchords/"
description: "pmxchords – This script processes pmx files with chord symbols, allowing for key transpositions"
---

<h2 class="name">NAME</h2>
<p> pmxchords &#8211; This script processes pmx files with chord symbols, allowing for key transpositions </p>
<h2>SYNOPSIS</h2>
<p> [ texlua ] <code>pmxchords</code> { <i>option</i> | <i>jobname</i> [ .pmx ] } &#8230;</p>
<dl>
<dt>The default effect is to preprocess each pmx file so that chords are transposed as necessary, generating a temporary pmx file which is then processed by pmxab. Finally the resulting tex file is renamed to have the original jobname. The default filename for the temporary file is &lt;jobname&gt;_chtr.pmx.</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v </code></p>
<dd> output program name and version number, and quit</p>
<dt><code>-h</code></p>
<dd> output usage summary and quit</p>
<dt><code>-s </code></p>
<dd> stop after first step (of producing a temporary pmx file with transposed chord symbols). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pmx/">pmx</a>(1), <a href="/docs/linux/man/1-musixtex/">musixtex</a>(1)</p>
<h2>AUTHORS</h2>
<p> pmxchords was written by Ondrej Fafejta &lt;fafejtao [at] gmail.com&gt;. This manual page was written by Bob Tennent &lt;rdt [at] cs.queensu.ca&gt;. </p>
<h2>Index</h2>
