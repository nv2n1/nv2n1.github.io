---
title: "latexrevise(1)"
name: "latexrevise"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latexrevise/"
description: "latexrevise – selectively remove markup and text from latexdiff output"
---
<h2 class="name">NAME</h2>
<p> latexrevise - selectively remove markup and text from latexdiff output </p>
<h2>SYNOPSIS</h2>
<p> <code>latexrevise</code> [ <font SIZE="-1"><code>OPTIONS</code></font> ] [ <i>diff.tex</i> ] &gt; <i>revised.tex</i>  </p>
<h2>DESCRIPTION</h2>
<p> <i>latexrevise</i> reads a file <code>&quot;diff.tex&quot;</code> (output of <i>latexdiff</i>), and remove the markup commands. If no filename is given the input is read from standard input. The command can be used in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i>, <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i>, or <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode, or can be used to remove user-defined latex commands from the input (see <code>-c</code>, <code>-e</code>, <code>-m</code>, and <code>-n</code> below). In <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> mode, all appended text fragments (or preamble lines) are kept, and all discarded text fragments (or preamble lines) are deleted. In <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode, all discarded text fragments are kept, and all appended text fragments are deleted. If you wish to keep some changes, edit the diff.tex file in advance, and manually remove those tokens which would otherwise be deleted. Note that <i>latexrevise</i> only pays attention to the <code>&quot;\DIFaddbegin&quot;</code>, <code>&quot;\DIFaddend&quot;</code>, <code>&quot;\DIFdelbegin&quot;</code>, and <code>&quot;\DIFdelend&quot;</code> tokens and corresponding <font SIZE="-1">FL</font> varieties. All <code>&quot;\DIFadd&quot;</code> and <code>&quot;\DIFdel&quot;</code> commands (but not their contents) are simply deleted. The commands added by latexdiff to the preamble are also removed. In <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode, <code>&quot;\DIFaddbegin, \DIFaddend, \DIFdelbegin, \DIFdelend&quot;</code> tokens and their corresponding <code>&quot;FL&quot;</code> varieties are kept but all other markup (e.g. <code>&quot;DIFadd&quot;</code> and &lt;\DIFdel&gt;) is removed. The result will not in general be valid latex-code but it will be easier to read and edit in preparation for a subsequent run in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> or <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode. In <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode the preamble is left unmodified.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> or <code>--accept</code></dt>
<dd> <p> Run in <i></i><font SIZE="-1"><i>ACCEPT</i></font><i></i> mode (delete all blocks marked by <code>&quot;\DIFdelbegin&quot;</code> and <code>&quot;\DIFdelend&quot;</code>). </p>
 </dd>
<dt><code>-d</code> or <code>--decline</code></dt>
<dd> <p> Run in <i></i><font SIZE="-1"><i>DECLINE</i></font><i></i> mode (delete all blocks marked by <code>&quot;\DIFaddbegin&quot;</code> and <code>&quot;\DIFaddend&quot;</code>). </p>
 </dd>
<dt><code>-s</code> or <code>--simplify</code></dt>
<dd> <p> Run in <i></i><font SIZE="-1"><i>SIMPLIFY</i></font><i></i> mode (Keep all <code>&quot;\DIFaddbegin&quot;</code>, <code>&quot;\DIFaddend&quot;</code>, <code>&quot;\DIFdelbegin&quot;</code>, <code>&quot;\DIFdelend&quot;</code> tokens, but remove all other latexdiff markup from body). </p>
 </dd></dl>
<p> Note that the three mode options are mutually exclusive. If no mode option is given, <i>latexrevise</i> simply removes user annotations and markup according to the following four options. </p>
<dl>
<dt><code>-c cmd</code> or <code>--comment=cmd</code></dt>
<dd> <p> Remove <code>&quot;\cmd{...}&quot;</code> sequences. <code>&quot;cmd&quot;</code> is supposed to mark some explicit annotations which should be removed from the file before release. </p>
 </dd>
<dt><code>-e envir</code> or <code>--comment-environment=envir</code></dt>
<dd> <p> Remove explicit annotation environments from the text, i.e. remove </p>
<pre><code>            \begin{envir}
            ...
            \end{envir}
</code></pre>
<p> blocks. </p>
 </dd>
<dt><code>-m cmd</code> or <code>--markup=cmd</code></dt>
<dd> <p> Remove the markup command <code>&quot;\cmd&quot;</code> but leave its argument, i.e. turn <code>&quot;\cmd{abc}&quot;</code> into <code>&quot;abc&quot;</code>. </p>
 </dd>
<dt><code>-n envir</code> or <code>--markup-environment=envir</code></dt>
<dd> <p> Similarly, remove <code>&quot;\begin{envir}&quot;</code> and <code>&quot;\end{envir}&quot;</code> commands but leave content of the environment in the text. </p>
 </dd>
<dt><code>-V</code> or <code>--verbose</code></dt>
<dd> <p> Verbose output </p>
 </dd>
<dt><code>-q</code> or <code>--no-warnings</code></dt>
<dd> <p> Do not warn users about <code>&quot;\DIDadd{..}&quot;</code> or <code>&quot;\DIFdel{..}&quot;</code> statements which should have been removed already. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> The current version is a beta version which has not yet been extensively tested. It has not been actively maintained so might not process output of newer versions of latexdiff entirely correctly. Please submit bug reports using the issue tracker of the github repository page <i><a rel="nofollow" href="https://github.com/ftilmann/latexdiff.git">https://github.com/ftilmann/latexdiff.git</a></i>, or send them to <i>tilmann --- </i><font SIZE="-1"><i>AT</i></font><i> --- gfz-potsdam.de</i>. Include the serial number of <i>latexrevise</i> (Option --version). If you come across latexdiff output which is not processed correctly by <i>latexrevise</i> please include the problem file as well as the old and new files on which it is based, ideally edited to only contain the offending passage as long as that still reproduces the problem. </p>
<p> Note that <i>latexrevise</i> gets confused by commented <code>&quot;\begin{document}&quot;</code> or <code>&quot;\end{document}&quot;</code> statements  </p>
<h2>SEE ALSO</h2>
<p> latexdiff  </p>
<h2>PORTABILITY</h2>
<p> <i>latexrevise</i> does not make use of external commands and thus should run on any platform supporting <font SIZE="-1">PERL</font> v5 or higher.  </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2004 Frederik Tilmann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License Version 3 </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">PORTABILITY</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">AUTHOR</a></dt>
<dd>  </dd></dl>
