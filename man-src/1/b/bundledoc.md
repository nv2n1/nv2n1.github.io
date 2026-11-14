---
title: "bundledoc(1)"
name: "bundledoc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundledoc/"
description: "bundledoc – bundle all the files needed by a LaTeX document"
---

<h2 class="name">NAME</h2>
<p> bundledoc &#8211; bundle all the files needed by a LaTeX document </p>
<h2>SYNOPSIS</h2>
<p> bundledoc [<code>&#8211;version</code>] [<code>&#8211;help</code>] [<code>&#8212;</code>[<code>no</code>]<code>verbose</code>] [<code>&#8211;texfile</code>=<i>file.tex</i>] [<code>&#8211;directory</code>=<i>directory</i>] [<code>&#8212;</code>[<code>no</code>]<code>localonly</code>] [<code>&#8211;exclude</code>=<i>string</i>] [<code>&#8211;include</code>=<i>filespec</i>] [<code>&#8211;manifest</code>=<i>file</i>] [<code>&#8212;</code><code>listdeps</code>=[yes|no|only|rel]&#8230;] [<code>&#8212;</code>[<code>no</code>]<code>keepdirs</code>] [<code>&#8211;config</code>=<i>file.cfg</i>] <i>file.dep</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bundledoc</code> is a post-processor for the <code>snapshot</code> package that bundles together all the classes, packages, and files needed to build a given LaTeX document. It reads the <i>.dep</i> file that <code>snapshot</code> produces, finds each of the files mentioned therein, and packages them into a single archive file (e.g., a <i>.tar.gz</i> file), suitable for moving across systems, transmitting to a colleague, etc. </p>
<p> As the simplest example possible, consider a LaTeX file called, say, <i>hello.tex</i>: </p>
<pre><code>
\RequirePackage{snapshot} % Needed by bundledoc
    \documentclass[11pt]
{
    article
}
egin{document} Hello, world !
    nd
{
    document
}
</code></pre>
<p> The <tt>&quot;\RequirePackage{snapshot}&quot;</tt> causes a <i>hello.dep</i> file to be produced. When <code>bundledoc</code> is then given <tt>&quot;hello.dep&quot;</tt> as an argument, it locates the dependent files &#8212; <i>snapshot.sty</i>, <i>article.cls</i>, and <i>size11.clo</i> &#8212; and bundles them into a single archive file, along with <i>hello.tex</i> and a <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i> file (described in &#8220;<font SIZE="-1">OPTIONS&#8221;</font>, below).</p>
<h2>OPTIONS</h2>
<p> In the following descriptions, <i>somefile</i> refers to the name of your main LaTeX document (no extension). </p>
<p> <code>bundledoc</code> requires the name of the dependency file produced by <code>snapshot</code>, normally <i>somefile</i><i>.dep</i>). (For convenience, the file can be specified without its <i>.dep</i> extension.) The following options may also be given:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Output the <code>bundledoc</code> script&#8217;s version number. This overrides all of the remaining options.</p>
<dt><code>&#8211;help</code></p>
<dd> Give a brief usage message. This overrides all of the remaining options.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>verbose</code> (default: &quot;noverbose&quot;)</p>
<dd> <code>bundledoc</code> normally does not output anything except error messages. With <tt>&quot;--verbose&quot;</tt>, it outputs copious status messages.</p>
<dt><code>&#8211;texfile</code>=<i>main .tex file</i> (default: <i>somefile</i><i>.tex</i>)</p>
<dd> <code>snapshot</code>&#8216;s dependency file does not list the main LaTeX file (the one that gets passed to <code>latex</code>). In order for <code>bundledoc</code> to find and bundle that file, <code>bundledoc</code> assumes it has the same name as the <code>snapshot</code> dependency file but with a <i>.tex</i> extension. If this is not the case, then use <tt>&quot;--texfile&quot;</tt> to specify the correct filename.</p>
<dt><code>&#8211;directory</code>=<i>archive directory</i> (default: <i>somefile</i>)</p>
<dd> When <code>bundledoc</code> creates an archive (e.g., a <i>.tar</i> or <i>.zip</i> file) containing the document&#8217;s files, it puts all of them in a directory to avoid cluttering the current directory with files. If the given dependency file is called <i>somefile</i><i>.dep</i> then the resulting archive will, by default, store all the dependent files in a <i>somefile</i> directory. To change the directory name use the <tt>&quot;--directory&quot;</tt> option.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>localonly</code> (default: &quot;nolocalonly&quot;)</p>
<dd> Although <code>bundledoc</code> normally archives all of the files named in the <i>.dep</i> file, the <tt>&quot;--localonly&quot;</tt> option tells <code>bundledoc</code> to exclude all files located in a directory other than the <i>.tex</i> file&#8217;s directory or one of its subdirectories.</p>
<dt><code>&#8211;exclude</code>=<i>string</i> (default: <i>none</i>)</p>
<dd> While <tt>&quot;--localonly&quot;</tt> causes files outside of the <i>.tex</i> file&#8217;s directory tree to be omitted from the archive, <tt>&quot;--exclude&quot;</tt> provides finer-grained control over files to omit from the archive. The <tt>&quot;--exclude&quot;</tt> option, which can be specified repeatedly on the command line, causes all files whose name contains <i>string</i> to be omitted from the archive.</p>
<dt><code>&#8211;include</code>=<i>filespec</i> (default: <i>none</i>)</p>
<dd> The <tt>&quot;--include&quot;</tt> option, which can be specified repeatedly on the command line, instructs <code>bundledoc</code> to include in the archive all of the files matching <i>filespec</i>, even if they&#8217;re not referenced in the <i>.dep</i> file.</p>
<dt><code>&#8211;manifest</code>=<i>manifest file</i> (default: <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>)</p>
<dd> In addition to the dependent files, <code>bundledoc</code> includes in the archive file one extra file called, by default, &#8220;<i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>&#8221;. <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i> is a text file that lists the original filenames of all the dependencies. To change the filename from &#8220;<i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>&#8221; to something else, use the <tt>&quot;--manifest&quot;</tt> option. As a special case, <tt>&quot;--manifest=&quot;&quot;&quot;</tt> tells <code>bundledoc</code> not to include a manifest file at all.</p>
<dt><code>&#8211;listdeps</code>=[yes|no|only|rel]&#8230;] (default: &quot;no&quot;)</p>
<dd> <tt>&quot;--listdeps&quot;</tt> accepts one or more of <tt>&quot;yes&quot;</tt>, <tt>&quot;no&quot;</tt>, <tt>&quot;only&quot;</tt>, or <tt>&quot;rel&quot;</tt> as a comma-separated list. As long as <tt>&quot;no&quot;</tt> does not appear in this list, <code>bundledoc</code> outputs all of the main LaTeX file&#8217;s dependencies. If the list contains <tt>&quot;rel&quot;</tt>, then <code>bundledoc</code> outputs the list of dependencies with relative pathnames. If the list contains <tt>&quot;only&quot;</tt>, then <code>bundledoc</code> exits after displaying the list, without producing an archive.</p>
<dt><code>&#8212;</code>[<code>no</code>]<code>keepdirs</code> (default: &quot;nokeepdirs&quot;)</p>
<dd> Normally, the archive file that <code>bundledoc</code> produces contains a single directory &#8212; and subdirectories, if the document refers explicitly to them &#8212; in which all the dependent files lie. If <tt>&quot;--keepdirs&quot;</tt> is specified, all the dependent files are stored with their original pathnames. For example, if <i>somefile.tex</i> depends on <i>figures/somefigure.eps</i>, <i>article.cls</i>, and <i>snapshot.sty</i>, then the <i>somefile</i> archive will normally contain the following files:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <i>somefile/somefile.tex</i></p>
<dt>&bull;</p>
<dd> <i>somefile/figures/somefigure.eps</i></p>
<dt>&bull;</p>
<dd> <i>somefile/article.cls</i></p>
<dt>&bull;</p>
<dd> <i>somefile/snapshot.sty</i></p>
<dt>&bull;</p>
<dd> <i>somefile/MANIFEST</i></dl>
</dl>
<dl>
<dt>
<dd>
<p> However, <tt>&quot;--keepdirs&quot;</tt> will cause the <i>somefile</i> archive to contain the following sorts of filenames instead:</p>
<dl>
<dt>&bull;</p>
<dd> <i>home/me/mydocs/somefile.tex</i></p>
<dt>&bull;</p>
<dd> <i>home/me/mydocs/figures/somefigure.eps</i></p>
<dt>&bull;</p>
<dd> <i>usr/share/texmf/tex/latex/base/article.cls</i></p>
<dt>&bull;</p>
<dd> <i>usr/share/texmf/tex/latex/snapshot/snapshot.sty</i></dl>
</dl>
<dl>
<dt>
<dd>
<p> <tt>&quot;--directory&quot;</tt> is not used when <tt>&quot;--keepdirs&quot;</tt> is in effect. In addition, no manifest file is written to the archive file as it contains redundant information.</dl>
<dt><code>&#8211;config</code>=<i>configuration file</i> (default: &lt;none&gt;)</p>
<dd> The <tt>&quot;--config&quot;</tt> option is used to point <code>bundledoc</code> to the appropriate configuration (<i>.cfg</i>) file for your TeX distribution and operating system. <code>bundledoc</code> comes with a few configuration files and it&#8217;s easy to write more. See &#8220;<font SIZE="-1">CONFIGURATION FILES&#8221;</font> (below) for a description of the configuration file format. For convenience, the file can be specified without its <i>.cfg</i> extension.</dl>
<h2>CONFIGURATION FILES</h2>
<h3>Format</h3>
<p> Configuration files follow a fairly simple format. Lines beginning with <tt>&quot;#&quot;</tt> are comments. Blank lines are ignored. All other lines are of the form: </p>
<pre>
    variable: value
</pre>
<p> The current version of <code>bundledoc</code> recognizes the following variables:</p>
<dl>
<dt><code>bundle</code></p>
<dd> The command to use to bundle a set of files into a single archive file</p>
<dt><code>sink</code></p>
<dd> The affix to a command to discard its output</p>
<dt><code>find</code></p>
<dd> The command to find a file within the TeX tree(s).</dl>
<p> Values that are too long for one line can be split across multiple lines by using <tt>&quot;\&quot;</tt> as the line-continuation symbol. </p>
<p> There are two environment variables that <code>bundledoc</code> makes available for use by configuration-file commands: <tt>&quot;BDBASE&quot;</tt>, which is set to <i>somefile</i> (as in &#8220;<font SIZE="-1">OPTIONS&#8221;</font>), and <tt>&quot;BDINPUTS&quot;</tt>, which is set to a space-separated list of files that a command is to operate upon. That is, when the command associated with <tt>&quot;bundle&quot;</tt> is running, <tt>&quot;BDINPUTS&quot;</tt> contains the list of all the files that are to be archived. In contrast, when the command associated with <tt>&quot;find&quot;</tt> is running, <tt>&quot;BDINPUTS&quot;</tt> contains the name of the file to search for.</p>
<h3>Examples</h3>
<p> The following configuration file parallels <code>bundledoc</code>&#8216;s default values of the various configuration-file variables, which represents a kpathsea-based TeX distribution running on a generic Unix system, which doesn&#8217;t necessarily have any of the <font SIZE="-1">GNU</font> tools, such as <code>gzip</code> or <font SIZE="-1">GNU</font> <code>tar</code>: </p>
<pre>
    # &quot;Default&quot; configuration file
    # By Scott Pakin &lt;scott+bdoc [at] pakin.org&gt;
    bundle: (tar -cvf - $BDINPUTS | compress &gt; $BDBASE.tar.Z)
    sink:   &gt; /dev/null 2&gt;&amp;1
    find:   kpsewhich -progname=latex $BDINPUTS
</pre>
<p> The parentheses in the <tt>&quot;bundle:&quot;</tt> line tell the Unix shell to run the command in a subshell. This is to make the <tt>&quot;sink:&quot;</tt> affix work properly (i.e., so there aren&#8217;t two <tt>&quot;&gt;&quot;</tt>&#8216;s in the same command). </p>
<p> Notice how the commands treat <tt>&quot;BDBASE&quot;</tt> and <tt>&quot;BDINPUTS&quot;</tt> like any other environment variables in a Unix shell, using <tt>&quot;$&quot;</tt> to take their value. Other operating systems use different conventions for referring to environment variables. For instance, a configuration file for a Windows-based TeX distribution would use <tt>&quot;%BDBASE%&quot;</tt> and <tt>&quot;%BDINPUTS%&quot;</tt> instead. </p>
<p> The value for <tt>&quot;sink:&quot;</tt> is specific to an operating system. The value for <tt>&quot;find:&quot;</tt> is specific to a TeX distribution. <tt>&quot;bundle:&quot;</tt> is where the most opportunity for customization lies. You can use <tt>&quot;bundle:&quot;</tt> to specify your favorite archive format. For example, you can produce a shar file on Unix with something like: </p>
<pre>
    bundle: (shar --archive-name=&quot;$BDBASE&quot; $BDINPUTS &gt; $BDBASE.sh)
</pre>
<p> or a <font SIZE="-1">CAB</font> file on Microsoft Windows with something like: </p>
<pre>
    bundle: cabarc -r -p N %BDBASE%.cab %BDINPUTS%
</pre>
<h2>EXAMPLES</h2>
<p> Assume that <i>myfile.dep</i> was produced from <i>myfile.tex</i> by following the instructions in the Description section. The following command produces a <i>.zip</i> file with the MikTeX TeX distribution running on Microsoft Windows: </p>
<pre>
    bundledoc --config=miktex.cfg myfile.dep
</pre>
<p> This can be abbreviated to </p>
<pre>
    bundledoc --config=miktex myfile
</pre>
<p> The following builds a <i>.tar.gz</i> archive with the TeX Live distribution running on a Unix-like operating system. <code>bundledoc</code> will produce verbose output describing its operations. All files not in the same directory tree as <i>myfile.tex</i> and all files containing &#8220;.fd&#8221; or &#8220;.sty&#8221; in their names are omitted. However, all <i>.bib</i> files in the current directory will be included in the archive even though none of them are referenced by <i>myfile.dep</i>. Finally, no <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i> file will be produced. </p>
<pre><code>
bundledoc-- config = texlive - unix.cfg-- verbose-- localonly-- exclude =.fd-- exclude =.cfg-- include = "*.bib" --manifest = "" myfile.dep
</code></pre>
<h2>FILES</h2>
<p> The user must have previously installed <i>snapshot.sty</i> and used it to produce a dependency file for his document. Besides that, the set of external files needed by <code>bundledoc</code> is system-specific and depends on the configuration file used. (See &#8220;<font SIZE="-1">CONFIGURATION FILES&#8221;</font>, above.) </p>
<p> <code>bundledoc</code> currently comes with two configuration files:</p>
<dl>
<dt><i>texlive-unix.cfg</i></p>
<dd> Configuration file for TeX Live installations on Unix or Linux. TeX Live is a kpathsea-based TeX distribution that runs on various flavors of Unix and Microsoft Windows. <i>texlive-unix.cfg</i> assumes you have <code>gzip</code> and uses it to produce a <i>.tar.gz</i> archive file. The configuration file has <code>bundledoc</code> use <code>kpsewhich</code> to find LaTeX files.</p>
<dt><i>miktex.cfg</i></p>
<dd> Configuration file for MikTeX installations. MikTeX is a popular TeX distribution for Microsoft Windows. <i>miktex.cfg</i> assumes you have <code>zip</code> and uses it to produce a <i>.zip</i> archive file. The configuration file now has <code>bundledoc</code> use <code>kpsewhich</code> to find LaTeX files; older version of MikTeX required the rather nonstandard <code>initexmf</code> for this purpose.</p>
<dt><i>texlive-unix-arlatex.cfg</i></p>
<dd> This is a variant of <i>texlive-unix.cfg</i> that uses <code>arlatex</code> instead of <code>gzip</code> to archive files. <code>arlatex</code> is a script included in the <code>bundledoc</code> distribution that generates a self-extracting <i>.tex</i> file based on LaTeX&#8217;s <tt>&quot;filecontents&quot;</tt> environment.</dl>
<h2>NOTES</h2>
<h3>Including and excluding files</h3>
<p> The <tt>&quot;--localonly&quot;</tt>, <tt>&quot;--exclude&quot;</tt>, and <tt>&quot;--include&quot;</tt> options provide control over the archive&#8217;s contents. <tt>&quot;--exclude&quot;</tt> and <tt>&quot;--include&quot;</tt> can be specified repeatedly on the command line. The order in which these options are specified is immaterial; <code>bundledoc</code> processes file inclusions and exclusions in the following order:</p>
<dl>
<dt>1.</p>
<dd> All files referenced by the <i>.dep</i> file are added to the list of files to archive.</p>
<dt>2.</p>
<dd> If <tt>&quot;--localonly&quot;</tt> is specified, all files not found in the <i>.tex</i> file&#8217;s directory are removed from the list.</p>
<dt>3.</p>
<dd> For each <tt>&quot;--exclude&quot;</tt> string specified, all files containing that string are removed from the list.</p>
<dt>4.</p>
<dd> For each <tt>&quot;--include&quot;</tt> file specification, the set of files designated by its expansion are added to the list.</dl>
<h3>Issues When Running Under Microsoft Windows</h3>
<p> First, because <code>bundledoc</code> is a Perl script, you should do one of the following to run it under Windows:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;perl bundledoc&quot;</tt></p>
<dt>&bull;</p>
<dd> Rename <i>bundledoc</i> to <i>bundledoc.pl</i> and run <tt>&quot;bundledoc.pl&quot;</tt>. (This is assuming you have a file association set up for <i>.pl</i>.)</p>
<dt>&bull;</p>
<dd> Run the <code>pl2bat</code> script (if you have it) to convert <i>bundledoc</i> to <i>bundledoc.bat</i>, then run <tt>&quot;bundledoc&quot;</tt>.</dl>
<p> Second, Windows uses a multi-rooted filesystem (i.e., multiple drive letters). I wouldn&#8217;t be surprised if bad things were to happen if the files to be bundled are scattered across drives. In addition, Windows supports &#8220;<font SIZE="-1">UNC</font>&#8221; filenames, which have no drive letter at all, just a machine and share name. <font SIZE="-1">UNC</font> filenames are also untested waters for <code>bundledoc</code>. Be careful!</p>
<h3>Testing Status</h3>
<p> I have tested <code>bundledoc</code> only with Perl v5.6.0 and later and only on the following platforms:</p>
<dl>
<dt>&bull;</p>
<dd> Linux + TeX Live</p>
<dt>&bull;</p>
<dd> Linux + teTeX</p>
<dt>&bull;</p>
<dd> Windows <font SIZE="-1">NT +</font> MiKTeX</p>
<dt>&bull;</p>
<dd> Solaris + ??? (something kpathsea-based)</dl>
<p> It is my hope that <code>bundledoc</code> works on many more platforms than those. I tried to make the program itself fairly independent of the operating system; only the configuration files should have to change to run <code>bundledoc</code> on a different system.</p>
<h3>Future Work</h3>
<p> I&#8217;d like <code>bundledoc</code> to work on as wide a variety of TeX distributions as possible. If your platform is significantly different from the ones listed in &#8220;Testing Status&#8221; (e.g., if you&#8217;re running <font SIZE="-1">OS</font>&nbsp;X) and you need to create a substantially different configuration file from <i>texlive-unix.cfg</i> and <i>miktex.cfg</i>, please send it to me at the address listed in &#8220;<font SIZE="-1">AUTHOR&#8221;</font> so I can include it in a future version of <code>bundledoc</code>. (I make no promises, though). </p>
<p> Once <code>bundledoc</code> works on all the major operating systems and TeX distributions it would be really convenient if I could get <code>bundledoc</code> to detect the platform it&#8217;s running on and automatically select an appropriate configuration file. </p>
<p> Finally, it would be handy for <code>bundledoc</code> to include fonts in the archive file. At a minimum, it should include <i>.tfm</i> files, but it would be even better if it included <i>.mf</i>, <i>.pfb</i>, <i>.ttf</i>, and other common font formats, as well.</p>
<h3>Acknowledgments</h3>
<p> Thanks to Fabien Vignes-Tourneret for suggesting what became the <tt>&quot;--localonly&quot;</tt> option and for a discussion that led to the <tt>&quot;--exclude&quot;</tt> and <tt>&quot;--include&quot;</tt> options; to Marius Kleiner for updating <code>bundledoc</code> to properly handle document subdirectories; and to Frank Mittelbach for suggesting using Kpathsea to help find <i>.cfg</i> files and to automatically append <i>.cfg</i> and <i>.dep</i> extensions if necessary.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arlatex/">arlatex</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-zip/">zip</a></code>(1), the <code>snapshot</code> documentation</p>
<h2>AUTHOR</h2>
<p> Scott Pakin, <i>scott+bdoc [at] pakin.org</i> </p>
<h2>Index</h2>
