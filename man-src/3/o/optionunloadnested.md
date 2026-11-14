---
title: "optionunloadnested(3)"
name: "optionunloadnested"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionunloadnested/"
description: "optionUnloadNested – Deallocate the memory for a nested value"
---

<p>optionUnloadNested &#8211; Deallocate the memory for a nested value</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionUnloadNested(tOptionValue const *pOptVal);
</code></pre>
<h2>Description</h2>
<p>A nested value needs to be deallocated. The pointer passed in should have been gotten from a call to <code>configFileLoad()</code> (See @pxref{libopts-configFileLoad}).</p>
<dl>
<dt><i>pOptVal</i></p>
<dd>the hierarchical value</dl>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
