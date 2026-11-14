---
title: "bg5latex(1)"
name: "bg5latex"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bg5latex/"
description: "bg5latex – Use LaTeX directly on a Big5 encoded .tex file bg5pdflatex – Use pdfLaTeX directly on a Big5 encoded .tex file bg5+latex – Use LaTeX directly on a Big5+ encoded .tex file bg5+pdflatex – ..."
---

<h2 class="name">NAME</h2>
<p> bg5latex &#8211; Use LaTeX directly on a Big5 encoded .tex file<br />
 bg5pdflatex &#8211; Use pdfLaTeX directly on a Big5 encoded .tex file<br />
 bg5+latex &#8211; Use LaTeX directly on a Big5+ encoded .tex file<br />
 bg5+pdflatex &#8211; Use pdfLaTeX directly on a Big5+ encoded .tex file<br />
 cef5latex &#8211; Use LaTeX directly on a Big5 encoded .tex file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containing CEF macros<br />
 cef5pdflatex &#8211; Use pdfLaTeX directly on a Big5 encoded .tex file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containing CEF macros<br />
 ceflatex &#8211; Use LaTeX directly on a .tex file containing CEF </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;macros<br />
 cefpdflatex &#8211; Use pdfLaTeX directly on a .tex file containing CEF </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;macros<br />
 cefslatex &#8211; Use LaTeX directly on an SJIS encoded .tex file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containing CEF macros<br />
 cefspdflatex &#8211; Use pdfLaTeX directly on an SJIS encoded .tex file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;containing CEF macros<br />
 gbklatex &#8211; Use LaTeX directly on a GBK encoded .tex file<br />
 gbkpdflatex &#8211; Use pdfLaTeX directly on a GBK encoded .tex file<br />
 sjislatex &#8211; Use LaTeX directly on an SJIS encoded .tex file<br />
 sjispdflatex &#8211; Use pdfLaTeX directly on an SJIS encoded .tex file </p>
<h2>SYNOPSIS</h2>
<p> <code>bg5latex</code> file.tex<br />
 <code>bg5pdflatex</code> file.tex<br />
 etc.</p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the different <code>*latex</code> batch files that come with the CJK LaTeX macro. </p>
<p> The <code>*latex</code> commands are shell scripts that will convert a (Big5(+), GBK or SJIS encoded) .tex file in a .cjk file using the respective <code>*conv</code> command resulting in a .cjk file, and will then run (<code>pdf</code>)<code>latex</code> on the .cjk file. </p>
<p> If you use Big5+ encoding, then use <code>bg5+latex</code> or <code>bg5+pdflatex</code>. </p>
<p> If you use CEF macro&#8217;s in your Big5 or SJIS encoded file, use <code>cef5latex</code> or <code>cefslatex</code> resp. instead. If it&#8217;s in plain ASCII, use <code>ceflatex</code>. </p>
<p> If you use GNU/Emacs (&gt;=20), you don&#8217;t have to use any of these commands: just put the Lisp file &quot;cjk-enc.el&quot; in Emacs&#8217; load-path, load the library &quot;cjk-enc&quot; and run &quot;M-x cjk-write-file&quot; to create a .cjk file. Then process the .cjk file with <code>latex</code> or <code>pdflatex</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bg5conv/">bg5conv</a></code>(1), <code>bg5+<a href="/docs/linux/man/1-conv/">conv</a></code>(1), <code><a href="/docs/linux/man/1-cef5conv/">cef5conv</a></code>(1), <code><a href="/docs/linux/man/1-cefconv/">cefconv</a></code>(1), <code><a href="/docs/linux/man/1-cefsconv/">cefsconv</a></code>(1), <code><a href="/docs/linux/man/1-extconv/">extconv</a></code>(1), <code><a href="/docs/linux/man/1-sjisconv/">sjisconv</a></code>(1), the <code>CJK</code> documentation files in /usr/share/doc/latex-cjk-common/.</p>
<h2>AVAILABILITY</h2>
<p> The <code>*latex</code> scripts are part of the CJK macro package for LaTeX 2e available at the CTAN hosts and its mirrors, and available for Debian under latex-cjk-chinese and latex-cjk-japanese.</p>
<h2>AUTHOR</h2>
<p> The programs mentioned under <code>NAME</code> were written by Werner Lemberg &lt;wl [at] gnu.org&gt;. </p>
<p> This manual page was written by Danai SAE-HAN &lt;danai.sae-han [at] edpnet.be&gt; for the Debian project. It is licensed under the GNU General Public License version 2 or higher, of which you can find a copy online at <a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a> or on Debian systems under /usr/share/common-licenses/GPL-2 (part of the &quot;base-files&quot; package). </p>
<h2>Index</h2>
