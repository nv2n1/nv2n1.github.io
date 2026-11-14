---
title: "optiononlyusage(3)"
name: "optiononlyusage"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optiononlyusage/"
---

optionOnlyUsage - Print usage text for just the options

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionOnlyUsage(tOptions *pOpts, int ex_code);
</code></pre>

<h2>Description</h2>

This routine will print only the usage for each option. This function may be used when the emitted usage must incorporate information not available to AutoOpts.
<dl><dt><i>pOpts</i>
<dd>program options descriptor
<dt><i>ex_code</i>
<dd>exit code for calling <a HREF="/docs/linux/man/3-exit/">exit</a>(3)</dl>

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a HREF="/docs/linux/man/3-strtransform/">strtransform</a>(3), 
