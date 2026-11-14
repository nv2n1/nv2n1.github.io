---
title: "strtransform(3)"
name: "strtransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtransform/"
---

strtransform - convert a string into its mapped-to value

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void strtransform(char *dest, char const *src);
</code></pre>

<h2>Description</h2>

Each character in the input string is mapped and the mapped-to character is put into the output. This function name is mapped to option_strtransform so as to not conflict with the POSIX name space. The source and destination may be the same.
<dl><dt><i>dest</i>
<dd>output string
<dt><i>src</i>
<dd>input string 

<h2>Errors</h2>

none.

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), 
