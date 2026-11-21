---

title: "lacheck(1)"
name: "lacheck"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lacheck/"
description: "lacheck – A consistency checker for LaTeX documents."
---

<p> <code>lacheck </code> <i>filename</i> [ <i>.tex</i> ]  </p>
<p> LaCheck is a general purpose consistency checker for LaTeX documents. It reads a LaTeX document and displays warning messages, if it finds bad sequences. It should be noted, that the badness is <i>very</i> subjective. LaCheck is designed to help find common mistakes in LaTeX documents, especially those made by beginners. </p>
<p> The things checked are: </p>
<p> Mismatched groups (braces), environments and math mode delimiters. When a mismatch is found, line numbers for <i>both </i> start and end of the mismatch is given. The error messages comes in pairs, one for the end match and one for the beginning, marked with `&lt;-&#8216; and `-&gt;&#8216; respectively. </p>
<p> Bad spacing including missing a `\ &#8216; after an abbreviation, missing an `\@&#8216; before a punctuation mark in a paragraph that is ended by an capital letter, double spaces like ` ~&#8216;, bad usage of ellipsis (like using ... instead of \ldots, or using \ldots where \cdots should be used), missing ~ before a \cite or \ref commands, space before footnotes, italic corrections before comma, point, or italic text, italic correction after normal text, missing italic correction when switching from italic to normal text, and double italic correction. </p>
<p> Badly placed punctuation marks around end of math mode delimiters. This is, punctuation placed right after display math end or punctuation placed right before text math end. Sequences of whitespace followed by punctuation marks are also caught. </p>
<p> Bad use of quotation characters, i.e. constructs like &quot;&#8216;word&quot; or &quot;word`&quot; are warned about, tabs in verbatim environments are caught, certain TeX primitives are frowned upon, attempts to give font specifiers arguments such as \em{text} are noted, and use of @ in LaTeX macros are reported. </p>
<p> LaCheck will read files that are input using \input or \include. Files with suffix `.sty&#8217; are omitted, as they probably will cause LaCheck to crash. </p>
<p> LaCheck may be invoked from within <a href="/docs/linux/man/1-Emacs/">Emacs</a>(1) using compile: </p>
<p> To run: <code>M-x compile RET lacheck RET</code> , and then <code>C-x `</code> to parse the messages </p>
<h2>OUTPUT</h2>
<p> The output is UNIX-error like, and may be parsed using <a href="/docs/linux/man/1-Emacs/">Emacs</a>(1) compile mode. Here is a sample: </p>
<p> lacheck compiler </p>
<dl>
<dt>&quot;/usr/mef/compiler.tex&quot;, line 34: missing `\\\\ &#8216; after &quot;etc.&quot;</dt>
<dd>  </dd>
<dt>&quot;/usr/mef/compiler.tex&quot;, line 179: double space at &quot; ~&quot;</dt>
<dd>  </dd>
<dt>&quot;/usr/mef/compiler.tex&quot;, line 186: &lt;- unmatched &quot;}&quot;</dt>
<dd>  </dd>
<dt>&quot;/usr/mef/compiler.tex&quot;, line 181: -&gt; unmatched &quot;$$&quot;</dt>
<dd>  </dd></dl>
<p> A control space `\ &#8216; should be inserted at line 34, to prevent an end-of-sentence space. Also, at line 179, the first space of the sequence &quot; ~&quot; should probably be deleted. The last two lines is an example, where the user mistyped, and probably inserted an extra &quot;}&quot; somewhere. </p>
<h2>DIAGNOSTICS</h2>
<p> Some special cases should be explained. In cases where a sentence ends with something that LaCheck thinks is an abbreviation an missing `\ &#8216; error may also occur, if the following sentence begins with a lowercase letter. </p>
<p> A mismatch error may cause more to follow, due to the chosen algorithm. In such cases just correct the <i>first</i> error and run LaCheck again </p>
<p> Braces, environments and math mode must be balanced within a file. </p>
<p> LaCheck may be confused by unmatched stuff placed inside verbatim-like environments called something else than exactly `verbatim&#8217;.  </p>
<h2>FILES</h2>
<p> /usr/bin/lacheck  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tex/">tex</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1)  </p>
<h2>BUGS</h2>
<p> LaCheck gets confused by advanced macros, is fooled by simple macros, can&#8217;t figure out if you use a non-standard way to switch italic on or off, does not like TeX at all, does not provide any options to turn off specific warnings, and is at best a crude approximation. </p>
<p> Ideas for improvements and bug reports are very welcome. Such should be directed to the maintainers, their email address is &lt;auc-tex_mgr [at] sunsite.auc.dk&gt;.  </p>
<h2>AUTHOR</h2>
<p> Kresten Krab Thorup with modifications by Per Abrahamsen. </p>
