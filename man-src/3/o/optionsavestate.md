---
title: "optionsavestate(3)"
name: "optionsavestate"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionsavestate/"
---

optionSaveState - saves the option state to memory

<h2>Synopsis</h2>

<pre><code>#include &lt;your-opts.h&gt;

cc[...] - o outfile infile.c - lopts[...] void optionSaveState(tOptions *pOpts);
</code></pre>

<h2>Description</h2>

This routine will allocate enough memory to save the current option processing state. If this routine has been called before, that memory will be reused. You may only save one copy of the option state. This routine may be called before <a HREF="//www.systutorials.com/docs/linux/man/3AO-optionProcess/">optionProcess</a>(3AO). If you do call it before the first call to optionProcess, then you may also change the contents of argc/argv after you call <a HREF="//www.systutorials.com/docs/linux/man/3AO-optionRestore/">optionRestore</a>(3AO) In fact, more strongly put: it is safest to only use this function before having processed any options. In particular, the saving and restoring of stacked string arguments and hierarchical values is disabled. The values are not saved.
<dl><dt><i>pOpts</i>
<dd>program options descriptor 

<h2>Errors</h2>

If it fails to allocate the memory, it will print a message to stderr and exit. Otherwise, it will always succeed.

<h2>See Also</h2>

The <i>info</i> documentation for the -l<i>opts</i> library. 
 <a HREF="/docs/linux/man/3-ao_string_tokenize/">ao_string_tokenize</a>(3), <a HREF="/docs/linux/man/3-configfileload/">configFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfileload/">optionFileLoad</a>(3), <a HREF="/docs/linux/man/3-optionfindnextvalue/">optionFindNextValue</a>(3), <a HREF="/docs/linux/man/3-optionfindvalue/">optionFindValue</a>(3), <a HREF="/docs/linux/man/3-optionfree/">optionFree</a>(3), <a HREF="/docs/linux/man/3-optiongetvalue/">optionGetValue</a>(3), <a HREF="/docs/linux/man/3-optionloadline/">optionLoadLine</a>(3), <a HREF="/docs/linux/man/3-optionmemberlist/">optionMemberList</a>(3), <a HREF="/docs/linux/man/3-optionnextvalue/">optionNextValue</a>(3), <a HREF="/docs/linux/man/3-optiononlyusage/">optionOnlyUsage</a>(3), <a HREF="/docs/linux/man/3-optionprocess/">optionProcess</a>(3), <a HREF="/docs/linux/man/3-optionrestore/">optionRestore</a>(3), <a HREF="/docs/linux/man/3-optionsavefile/">optionSaveFile</a>(3), <a HREF="/docs/linux/man/3-optionunloadnested/">optionUnloadNested</a>(3), <a HREF="/docs/linux/man/3-optionversion/">optionVersion</a>(3), <a HREF="/docs/linux/man/3-strequate/">strequate</a>(3), <a HREF="/docs/linux/man/3-streqvcmp/">streqvcmp</a>(3), <a HREF="/docs/linux/man/3-streqvmap/">streqvmap</a>(3), <a HREF="/docs/linux/man/3-strneqvcmp/">strneqvcmp</a>(3), <a HREF="/docs/linux/man/3-strtransform/">strtransform</a>(3), 
