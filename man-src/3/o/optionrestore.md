---
title: "optionrestore(3)"
name: "optionrestore"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionrestore/"
description: "optionRestore – restore option state from memory copy"
---

<p>optionRestore &#8211; restore option state from memory copy</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionRestore(tOptions *pOpts);
</code></pre>
<h2>Description</h2>
<p>Copy back the option state from saved memory. The allocated memory is left intact, so this routine can be called repeatedly without having to call optionSaveState again. If you are restoring a state that was saved before the first call to <a href="//www.systutorials.com/docs/linux/man/3AO-optionProcess/">optionProcess</a>(3AO), then you may change the contents of the argc/argv parameters to optionProcess.</p>
<dl>
<dt><i>pOpts</i></p>
<dd>program options descriptor </p>
<h2>Errors</h2>
<p>If you have not called <code>optionSaveState</code> before, a diagnostic is printed to <code>stderr</code> and exit is called.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
