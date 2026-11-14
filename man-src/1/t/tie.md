---
title: "tie(1)"
name: "tie"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tie/"
description: "tie – merge or apply WEB change files"
---

<h2 class="name">NAME</h2>
<p> tie &#8211; merge or apply WEB change files </p>
<h2>SYNOPSIS</h2>
<p> <code>tie</code> <code>-c</code>|<code>-m</code> <i>outputfile masterfile</i> <i>changefile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>tie</code> program is used to process multiple change files used with the WEB system for literate programming. The WEB programs allow to apply patches to a source file (the <i>masterfile</i>) by means of a number of change files (often only a single change file is allowed). <code>Tie</code> can be used to either merge up to 32 change files into a single one or to apply the changes to the <i>masterfile</i> in order to create a new one. Output of either the new change file or the patched master file goes into <i>outputfile</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Create a single change file from the given <i>changefile</i>s.</p>
<dt><code>-m</code></p>
<dd> Create a new master file by applying the given <i>changefile</i>s.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable WEBINPUTS is used to search for the input files, or the system default if WEBINPUTS is not set. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching. To avoid conflicts with other programs that also use the WEBINPUTS environment, you can be more specific and use WEBINPUTS_tie for special requirements in TIE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-web/">web</a></code>(1), <code><a href="/docs/linux/man/1-ctie/">ctie</a></code>(1), <code><a href="/docs/linux/man/1-cweb/">cweb</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Klaus Guntermann, TH Darmstadt, Institut f. Theoretische Informatik. Man page by Joachim Schnitter, TH Darmstadt, Phys. Chemie I. </p>
<h2>Index</h2>
