---
title: "streqvcmp(3)"
name: "streqvcmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-streqvcmp/"
---

streqvcmp - compare two strings with an equivalence mapping

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] int streqvcmp(char const *str1, char const *str2);
</code></pre>

<h2>Description</h2>

Using a character mapping, two strings are compared for &quot;equivalence&quot;. Each input character is mapped to a comparison character and the mapped-to characters are compared for the two NUL terminated input strings. This function name is mapped to option_streqvcmp so as to not conflict with the POSIX name space.
<dl><dt><i>str1</i>
<dd>first string
<dt><i>str2</i>
<dd>second string 

<h2>Return Value</h2>

the difference between two differing characters 

<h2>Errors</h2>

none checked. Caller responsible for seg faults.

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a HREF="/docs/linux/man/3-strtransform/">strtransform</a>(3), 
