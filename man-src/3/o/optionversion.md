---
title: "optionversion(3)"
name: "optionversion"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionversion/"
---

optionVersion - return the compiled AutoOpts version number

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] char const *optionVersion(void);
</code></pre>

<h2>Description</h2>

Returns the full version string compiled into the library. The returned string cannot be modified. 

<h2>Return Value</h2>

the version string in constant memory

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a HREF="/docs/linux/man/3-strtransform/">strtransform</a>(3), 
