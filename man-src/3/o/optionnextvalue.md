---
title: "optionnextvalue(3)"
name: "optionnextvalue"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionnextvalue/"
description: "optionNextValue – get the next value from a hierarchical list"
---

<p>optionNextValue &#8211; get the next value from a hierarchical list</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] const tOptionValue *optionNextValue(const tOptionValue *pOptValue, const tOptionValue *pOldValue);
</code></pre>
<h2>Description</h2>
<p>This routine will return the next entry after the entry passed in. At the end of the list, NULL will be returned. If the entry is not found on the list, NULL will be returned and &quot;<code>errno</code>&quot; will be set to EINVAL. The &quot;<code>pOldValue</code>&quot; must have been gotten from a prior call to this routine or to &quot;<code>opitonGetValue()</code>&quot;.</p>
<dl>
<dt><i>pOptValue</i></p>
<dd>a hierarchcal list value</p>
<dt><i>pOldValue</i></p>
<dd>a value from this list </p>
<h2>Return Value</h2>
<p>a compound value structure </p>
<h2>Errors</h2>
<p>The returned result is NULL and errno is set: </p>
<p> <code>EINVAL</code> &#8211; the <code>pOptValue</code> does not point to a valid hierarchical option value or <code>pOldValue</code> does not point to a member of that option value. </p>
<p> <code>ENOENT</code> &#8211; the supplied <code>pOldValue</code> pointed to the last entry. @end itemize</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
