---
title: "optionfindvalue(3)"
name: "optionfindvalue"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionfindvalue/"
description: "optionFindValue – find a hierarcicaly valued option instance"
---

<p>optionFindValue &#8211; find a hierarcicaly valued option instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] const tOptionValue *optionFindValue(const tOptDesc *odesc, char const *name, char const *val);
</code></pre>
<h2>Description</h2>
<p>This routine will find an entry in a nested value option or configurable. It will search through the list and return a matching entry.</p>
<dl>
<dt><i>odesc</i></p>
<dd>an option with a nested arg type</p>
<dt><i>name</i></p>
<dd>name of value to find</p>
<dt><i>val</i></p>
<dd>the matching value </p>
<h2>Return Value</h2>
<p>a compound value structure </p>
<h2>Errors</h2>
<p>The returned result is NULL and errno is set: </p>
<p> <code>EINVAL</code> &#8211; the <code>pOptValue</code> does not point to a valid hierarchical option value. </p>
<p> <code>ENOENT</code> &#8211; no entry matched the given name. @end itemize</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
