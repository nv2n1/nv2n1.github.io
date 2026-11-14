---
title: "optionfileload(3)"
name: "optionfileload"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionfileload/"
description: "optionFileLoad – Load the locatable config files, in order"
---

<p>optionFileLoad &#8211; Load the locatable config files, in order</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] int optionFileLoad(tOptions *opts, char const *prog);
</code></pre>
<h2>Description</h2>
<p>This function looks in all the specified directories for a configuration file (&quot;rc&quot; file or &quot;ini&quot; file) and processes any found twice. The first time through, they are processed in reverse order (last file first). At that time, only &quot;immediate action&quot; configurables are processed. For example, if the last named file specifies not processing any more configuration files, then no more configuration files will be processed. Such an option in the <code>first</code> named directory will have no effect. Once the immediate action configurables have been handled, then the directories are handled in normal, forward order. In that way, later config files can override the settings of earlier config files. See the AutoOpts documentation for a thorough discussion of the config file format. Configuration files not found or not decipherable are simply ignored.</p>
<dl>
<dt><i>opts</i></p>
<dd>program options descriptor</p>
<dt><i>prog</i></p>
<dd>program name </p>
<h2>Return Value</h2>
<p>0 -&gt; SUCCESS, -1 -&gt; FAILURE </p>
<h2>Errors</h2>
<p>Returns the value, &quot;-1&quot; if the program options descriptor is out of date or indecipherable. Otherwise, the value &quot;0&quot; will always be returned.</p>
<h2>See Also</h2>
<p>The <i>info</i> documentation for the -l<i>opts</i> library.<br />
 <a href="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a href="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a href="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a href="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a href="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a href="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a href="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a href="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a href="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a href="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a href="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a href="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a href="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a href="/docs/linux/man/3-optionsavestate/">optionSaveState</a>(3), <a href="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a href="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a href="/docs/linux/man/3-strequate/">strequate</a>(3), <a href="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a href="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a href="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a href="/docs/linux/man/3-strtransform/">strtransform</a>(3), </p>
