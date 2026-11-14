---
title: "h2ph(1)"
name: "h2ph"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h2ph/"
description: "h2ph – convert .h C header files to .ph Perl header files"
---

<h2 class="name">NAME</h2>
<p> h2ph &#8211; convert .h C header files to .ph Perl header files </p>
<h2>SYNOPSIS</h2>
<p> <code>h2ph [-d destination directory] [-r | -a] [-l] [-h] [-e] [-D] [-Q] [headerfiles]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>h2ph</i> converts any C header files specified to the corresponding Perl header file format. It is most easily run while in /usr/include: </p>
<pre>
        cd /usr/include; h2ph * sys/*
</pre>
<p> or </p>
<pre>
        cd /usr/include; h2ph * sys/* arpa/* netinet/*
</pre>
<p> or </p>
<pre>
        cd /usr/include; h2ph -r -l .
</pre>
<p> The output files are placed in the hierarchy rooted at Perl&#8217;s architecture dependent library directory. You can specify a different hierarchy with a <code>-d</code> switch. </p>
<p> If run with no arguments, filters standard input to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d destination_dir</p>
<dd> Put the resulting <code>.ph</code> files beneath <code>destination_dir</code>, instead of beneath the default Perl library location (<tt>$Config{'installsitearch'}</tt>).</p>
<dt>-r</p>
<dd> Run recursively; if any of <code>headerfiles</code> are directories, then run <i>h2ph</i> on all files in those directories (and their subdirectories, etc.). <code>-r</code> and <code>-a</code> are mutually exclusive.</p>
<dt>-a</p>
<dd> Run automagically; convert <code>headerfiles</code>, as well as any <code>.h</code> files which they include. This option will search for <code>.h</code> files in all directories which your C compiler ordinarily uses. <code>-a</code> and <code>-r</code> are mutually exclusive.</p>
<dt>-l</p>
<dd> Symbolic links will be replicated in the destination directory. If <code>-l</code> is not specified, then links are skipped over.</p>
<dt>-h</p>
<dd> Put &#8216;hints&#8217; in the .ph files which will help in locating problems with <i>h2ph</i>. In those cases when you <code>require</code> a <code>.ph</code> file containing syntax errors, instead of the cryptic </p>
<pre>
        [ some error condition ] at (eval mmm) line nnn
</pre>
<p> you will see the slightly more helpful </p>
<pre>
        [ some error condition ] at filename.ph line nnn
</pre>
<p> However, the <code>.ph</code> files almost double in size when built using <code>-h</code>.</p>
<dt>-e</p>
<dd> If an error is encountered during conversion, output file will be removed and a warning emitted instead of terminating the conversion immediately.</p>
<dt>-D</p>
<dd> Include the code from the <code>.h</code> file as a comment in the <code>.ph</code> file. This is primarily used for debugging <i>h2ph</i>.</p>
<dt>-Q</p>
<dd> &#8216;Quiet&#8217; mode; don&#8217;t print out the names of the files being converted.</dl>
<h2>ENVIRONMENT</h2>
<p> No environment variables are used.</p>
<h2>FILES</h2>
<pre>
 /usr/include/*.h
 /usr/include/sys/*.h
</pre>
<p> etc.</p>
<h2>AUTHOR</h2>
<p> Larry Wall</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> The usual warnings if it can&#8217;t read or write the files involved.</p>
<h2>BUGS</h2>
<p> Doesn&#8217;t construct the <tt>%sizeof</tt> array for you. </p>
<p> It doesn&#8217;t handle all C constructs, but it does attempt to isolate definitions inside evals so that you can get at the definitions that it can translate. </p>
<p> It&#8217;s only intended as a rough tool. You may need to dicker with the files produced. </p>
<p> You have to run this program by hand; it&#8217;s not run as part of the Perl installation. </p>
<p> Doesn&#8217;t handle complicated expressions built piecemeal, a la: </p>
<pre><code>
enum {
    FIRST_VALUE,
    SECOND_VALUE,
#ifdef ABC
    THIRD_VALUE
#endif
};
</code></pre>
<p> Doesn&#8217;t necessarily locate all of your C compiler&#8217;s internally-defined symbols. </p>
<h2>Index</h2>
