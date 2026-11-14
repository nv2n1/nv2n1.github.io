---
title: "xetex(1)"
name: "xetex"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xetex/"
description: "xetex – extended TeX with native support for Unicode, OpenType, system fonts"
---

<h2 class="name">NAME</h2>
<p> xetex &#8211; extended TeX with native support for Unicode, OpenType, system fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>xetex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> XeTeX (<code>xetex</code>) is a TeX engine with native support for Unicode, OpenType, and system-installed fonts, using third-party libraries (such as ICU, HarfBuzz, and Freetype). It was developed by Jonathan Kew for SIL. </p>
<p> XeTeX includes the e-TeX extensions and many extensions from pdfTeX, sometimes with different primitive names. </p>
<p> XeTeX is now released as part of TeX Live &lt;<a rel="nofollow" href="https://tug.org/texlive">https://tug.org/texlive</a>&gt;.</p>
<h2>OPTIONS</h2>
<p> XeTeX&#8217;s handling of its command-line arguments is similar to that of the other TeX programs in the Web2C implementation. Here we list only additions/deletions of command line options which are specific to XeTeX; see <a href="/docs/linux/man/1-etex/">etex</a>(1) for common options. Additions:</p>
<dl>
<dt><code>-no-pdf</code></p>
<dd> Generate XeTeX&#8217;s extended DVI (.xdv) output instead of pdf.</p>
<dt><code>-output-driver</code><i>&nbsp;cmd</i></p>
<dd> Run <i>cmd</i> instead of xdvipdfmx to translate xdv to pdf.</p>
<dt><code>-papersize</code><i>&nbsp;string</i></p>
<dd> Set pdf media size to <i>string</i>.</dl>
<p> Removals: <code>-draftmode</code>, <code>-enc</code>, <code>-ipc</code>, <code>-ipc-start</code>, <code>-translate-file</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1).<br />
 Home page: &lt;<a rel="nofollow" href="https://tug.org/xetex">https://tug.org/xetex</a>&gt;<br />
 CTAN page: &lt;<a rel="nofollow" href="https://ctan.org/pkg/xetex">https://ctan.org/pkg/xetex</a>&gt;<br />
 Reference manual: &lt;<a rel="nofollow" href="https://ctan.org/pkg/xetexref">https://ctan.org/pkg/xetexref</a>&gt;</p>
<h2>AUTHORS</h2>
<p> XeTeX is maintained by Jonathan Kew and others.<br />
 Public discussion list: &lt;<a rel="nofollow" href="http://lists.tug.org/xetex">http://lists.tug.org/xetex</a>&gt;<br />
 Bug reports: &lt;<a rel="nofollow" href="http://sourceforge.net/p/xetex/bugs/">http://sourceforge.net/p/xetex/bugs/</a>&gt; </p>
<p> This manual page was written by Karl Berry. It is released to the public domain. </p>
<h2>Index</h2>
