---
title: "xetex-unsafe(1)"
name: "xetex-unsafe"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xetex-unsafe/"
description: "xetex-unsafe, xelatex-unsafe – run xe(la)latex unsafely"
---

<h2 class="name">NAME</h2>
<p> xetex-unsafe, xelatex-unsafe &#8211; run xe(la)latex unsafely </p>
<h2>SYNOPSIS</h2>
<p> <code>xetex-unsafe</code> [<i>xetex-options</i>] <code>xelatex-unsafe</code> [<i>xetex-options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xetex-unsafe</code> (<code>xelatex-unsafe</code>) runs XeTeX (XeLaTeX) unsafely; specifically, using the <code>dvipdfmx-unsafe.cfg</code> configuration file. </p>
<p> As of TeX Live 2022, doing this is necessary only when running XeTeX on documents using PSTricks features which require transparency. We strongly recommend using Lua(La)TeX with PSTricks instead of XeTeX in this case. </p>
<p> At all costs, avoid using this, or any, unsafe invocation with documents off the net or that are otherwise untrusted in any way.</p>
<h2>WHY?</h2>
<p> You might well ask why using transparency features is unsafe in XeTeX. The answer lies in the implementation history of Ghostscript, starting as a PostScript interpreter before PDF was invented, when it was acceptable to abort on an error, whereas with PDF, it must keep going. The transparency operators, if abused in relation to this error recovery, can cause internal inconsistencies in Ghostscript&#8217;s state. </p>
<p> Thus, to be safe, we must disallow transparency with Ghostscript by default. The <code>xdvipdfmx</code> backend for XeTeX calls Ghostscript under certain circumstances, notably when using PSTricks. <code>(x)dvipdfmx</code> itself is not a PostScript interpreter, which is exactly what PSTricks requires. </p>
<p> Thus, to enable transparency, <code>xe(la)tex-unsafe</code> run XeTeX with arguments to the <code>xdvipdfmx</code> backend (-output-driver=&quot;xdvipdfmx -i dvipdfmx-unsafe.cfg -q -E&quot;) to use <code>dvipdfmx-unsafe.cfg</code>, which in turn tells Ghostscript to enable the transparency operators (-dALLOWPSTRANSPARENCY). They&#8217;re disabled by default. </p>
<p> There have been further complications related to reading from the filesystem, but as of TL22, these have been solved. The transparency issue cannot be solved without a different Ghostscript implementation, and the Ghostscript developers say they have no timeline for this. </p>
<p> To repeat the above: when using PSTricks and transparency, we strongly recommend playing it safe and using Lua(La)TeX instead of Xe(La)TeX.</p>
<h2>OPTIONS</h2>
<p> All command-line arguments except <code>&#8211;help</code> and <code>&#8211;version</code> are passed to Xe(La)TeX.</p>
<h2>BUGS</h2>
<p> For more about XeTeX: <a rel="nofollow" href="https://tug.org/xetex">https://tug.org/xetex</a> </p>
<p> For more about PSTricks: <a rel="nofollow" href="https://tug.org/PSTricks">https://tug.org/PSTricks</a> </p>
<p> Email for xe(la)tex-unsafe specifically: <a rel="nofollow" href="https://lists.tug.org/dvipdfmx">https://lists.tug.org/dvipdfmx</a> </p>
<h2>Index</h2>
