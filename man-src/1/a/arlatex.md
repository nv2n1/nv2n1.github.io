---

title: "arlatex(1)"
name: "arlatex"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arlatex/"
description: "arlatex – archive a number of ancillary LaTeX files into a master .tex file"
---

<p> arlatex [<code>&#8211;outfile</code>=<i>filename</i><i>.tex</i>] <code>&#8211;document</code>=<i>filename</i><i>.tex</i> <i>filename</i> &#8230; </p>
<p> arlatex <code>&#8211;version</code> </p>
<p> arlatex <code>&#8211;help</code></p>
<p> <code>arlatex</code> is an archiving program like <code>shar</code>, <code>tar</code>, <code>zip</code>, etc. Unlike those other archivers, however, <code>arlatex</code> is designed specifically for use with LaTeX. <code>arlatex</code> takes the name of a master <i>.tex</i> file and a number of ancillary files used by that master file (e.g., <i>.tex</i>, <i>.sty</i>, <i>.cls</i>, and <i>.eps</i> files). From these, <code>arlatex</code> outputs a single file that, when it&#8217;s run through <code>latex</code>, both regenerates the ancillary files and compiles the document into a <i>.dvi</i> file. </p>
<p> <code>arlatex</code> has a few advantages over other archiving programs:</p>
<dl>
<dt>&bull;</dt>
<dd> The <i>.tex</i> files produced by <code>arlatex</code> are in a plain-text format. They are therefore perfectly portable and trivial to e-mail to colleagues.</dd>
<dt>&bull;</dt>
<dd> <code>arlatex</code> needs only LaTeX to run. There is no dependence on any external tools.</dd>
<dt>&bull;</dt>
<dd> There is no explicit extraction step. As the generated document is run through <code>latex</code>, it extracts the ancillary files and builds the document in the same step. The user running <code>latex</code> may not even notice that additional files are being produced.</dd></dl>
<p> <code>arlatex</code> works by writing a number of <tt>&quot;egin{filecontents*}&quot;</tt>&nbsp;&#8230; <tt>&quot;nd{filecontents*}&quot;</tt> blocks to the output file, followed by the contents of the master file. (In fact, any LaTeX comments at the beginning of the master file are hoisted to the top of the generated file. This enables the author to draw attention, if so desired, to the fact that ancillary files will be generated.) The <tt>&quot;filecontents*&quot;</tt> environment, part of standard LaTeX2e, writes its contents verbatim to a specified file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Output the <code>arlatex</code> script&#8217;s version number.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Output brief <code>arlatex</code> usage information.</dd>
<dt><code>&#8211;document</code>=<i>.tex file</i></dt>
<dd> Specify the master document. The output from <code>arlatex</code> is this file with all of the other files named on the command line prepended to it. Note that <tt>&quot;--document&quot;</tt> is a <i>mandatory</i> parameter; <code>arlatex</code> will abort with an error message if <tt>&quot;--document&quot;</tt> is not specified.</dd>
<dt><code>&#8211;outfile</code>=<i>.tex file</i></dt>
<dd> Specify the output file. The output file looks just like the master document, but with a number of <tt>&quot;filecontents*&quot;</tt> environments preceding the <tt>&quot;\documentclass&quot;</tt> line. If <tt>&quot;--outfile&quot;</tt> is not specified, output will be written to the standard output device.</dd></dl>
<h2>EXAMPLES</h2>
<p> Suppose you have a paper called <i>paper.tex</i> that loads a custom package with <tt>&quot;</tt>\usepackage{mypackage}&quot;</code>. You want to submit the paper to a conference, but you want to be absolutely certain that <i>mypackage.sty</i> doesn&#8217;t get lost as your paper is shuttled from person to person. Here&#8217;s how <code>arlatex</code> can be of use: </p>
<pre><code>    arlatex --document=paper.tex mypackage.sty --outfile=paper-submit.tex
</code></pre>
<p> When <i>paper-submit.tex</i> is processed with <code>latex</code>, it builds just like the original <i>paper.tex</i>, except that it additionally creates a <i>mypackage.sty</i> in the current directory: </p>
<pre><code>    This is TeX, Version 3.14159 (Web2C 7.3.1)
    (paper-submit.tex
    LaTeX2e &lt;1999/12/01&gt; patch level 1
    Babel &lt;v3.6Z&gt; and hyphenation patterns for american, french, german,
    ngerman, italian, nohyphenation, loaded.
    LaTeX Warning: Writing file `./mypackage.sty'.
    (/usr/share/texmf/tex/latex/base/article.cls
    Document Class: article 1999/09/10 v1.4a Standard LaTeX document class
    (/usr/share/texmf/tex/latex/base/size12.clo)) (mypackage.sty)
                                  .
                                  .
                                  .
</code></pre>
<p> As another example, here&#8217;s how you could bundle together all of the files needed to build a large document for longevity: </p>
<pre><code>    arlatex --document=thesis.tex abstract.tex introduction.tex
      background.tex approach.tex experiments.tex relatedwork.tex
      conclusions.tex before.eps after.eps fast.eps slow.eps
      podunkUthesis.cls --outfile=thesis-all.tex
</code></pre>
<p> As the number of files to archive together increases it becomes more cumbersome to run <code>arlatex</code> manually. Fortunately, using <code>arlatex</code> with <code>bundledoc</code> is straightforward. <code>bundledoc</code> finds all of the files needed to build the document, and <code>arlatex</code> combines them into a single file. The following are examples of the <code>&quot;bundle:&quot;</code> line you might use in a <code>bundledoc</code> configuration file: </p>
<dl>
<dt>Unix:</dt>
<dd> <pre><code>   bundle: (arlatex --document=$BDBASE.tex $BDINPUTS \
     --outfile=$BDBASE-all.tex)
</code></pre>
 </dd>
<dt>Windows:</dt>
<dd> <pre><code>   bundle: arlatex --document=%BDBASE%.tex %BDINPUTS% \
     --outfile=%BDBASE%-all.tex
</code></pre>
 </dd></dl>
<p> See the <code>bundledoc</code> documentation for more information.  </p>
<h2>CAVEATS</h2>
<p> <code>arlatex</code> makes use of LaTeX2e&#8217;s <code>&quot;filecontents*&quot;</code> environment. <code>&quot;filecontents*&quot;</code> refuses to overwrite an existing file. However, it also refuses to create a file that exists <i>anywhere</i> that LaTeX can find it. That is, if the user running <code>latex</code> on an <code>arlatex</code>-generated <i>.tex</i> file already has a <i>/usr/share/texmf/tex/latex/whatever/whatever.sty</i> file then <code>&quot;filecontents*&quot;</code> will refuse to create a <i>whatever.sty</i> file, even in a different directory.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bundledoc/">bundledoc</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-shar/">shar</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-zip/">zip</a></code>(1)  </p>
<h2>AUTHOR</h2>
<p> Scott Pakin, <i>scott+bdoc [at] pakin.org</i> </p>
