---

title: "perlutil(1)"
name: "perlutil"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlutil/"
description: "perlutil – utilities packaged with the Perl distribution"
---

<p> perlutil &#8211; utilities packaged with the Perl distribution </p>
<h2>DESCRIPTION</h2>
<p> Along with the Perl interpreter itself, the Perl distribution installs a range of utilities on your system. There are also several utilities which are used by the Perl distribution itself as part of the install process. This document exists to list all of these utilities, explain what they are for and provide pointers to each module&#8217;s documentation, if appropriate.</p>
<h2>LIST OF UTILITIES</h2>
<h3>Documentation</h3>
<dl>
<dt>perldoc</dt>
<dd> The main interface to Perl&#8217;s documentation is <tt>&quot;perldoc&quot;</tt>, although if you&#8217;re reading this, it&#8217;s more than likely that you&#8217;ve already found it. <i>perldoc</i> will extract and format the documentation from any file in the current directory, any Perl module installed on the system, or any of the standard documentation pages, such as this one. Use <tt>&quot;perldoc &lt;name&gt;&quot;</tt> to get information on any of the utilities described in this document.</dd>
<dt>pod2man and pod2text</dt>
<dd> If it&#8217;s run from a terminal, <i>perldoc</i> will usually call <i>pod2man</i> to translate POD (Plain Old Documentation &#8211; see perlpod for an explanation) into a manpage, and then run <i>man</i> to display it; if <i>man</i> isn&#8217;t available, <i>pod2text</i> will be used instead and the output piped through your favourite pager.</dd>
<dt>pod2html</dt>
<dd> As well as these two, there is another converter: <i>pod2html</i> will produce HTML pages from POD.</dd>
<dt>pod2usage</dt>
<dd> If you just want to know how to use the utilities described here, <i>pod2usage</i> will just extract the &#8220;USAGE&#8221; section; some of the utilities will automatically call <i>pod2usage</i> on themselves when you call them with <tt>&quot;-help&quot;</tt>.</dd>
<dt>podselect</dt>
<dd> <i>pod2usage</i> is a special case of <i>podselect</i>, a utility to extract named sections from documents written in POD. For instance, while utilities have &#8220;USAGE&#8221; sections, Perl modules usually have &#8220;SYNOPSIS&#8221; sections: <tt>&quot;podselect -s &quot;SYNOPSIS&quot; ...&quot;</tt> will extract this section for a given file.</dd>
<dt>podchecker</dt>
<dd> If you&#8217;re writing your own documentation in POD, the <i>podchecker</i> utility will look for errors in your markup.</dd>
<dt>splain</dt>
<dd> <i>splain</i> is an interface to perldiag &#8211; paste in your error message to it, and it&#8217;ll explain it for you.</dd>
<dt>&quot;roffitall&quot;</dt>
<dd> The <tt>&quot;roffitall&quot;</tt> utility is not installed on your system but lives in the <i>pod/</i> directory of your Perl source kit; it converts all the documentation from the distribution to <i>*roff</i> format, and produces a typeset PostScript or text file of the whole lot.</dd></dl>
<h3>Converters</h3>
<p> To help you convert legacy programs to more modern Perl, the pl2pm utility will help you convert old-style Perl 4 libraries to new-style Perl5 modules.</p>
<h3>Administration</h3>
<dl>
<dt>libnetcfg</dt>
<dd> To display and change the libnet configuration run the libnetcfg command.</dd>
<dt>perlivp</dt>
<dd> The <i>perlivp</i> program is set up at Perl source code build time to test the Perl version it was built under. It can be used after running <tt>&quot;make install&quot;</tt> (or your platform&#8217;s equivalent procedure) to verify that perl and its libraries have been installed correctly.</dd></dl>
<h3>Development</h3>
<p> There are a set of utilities which help you in developing Perl programs, and in particular, extending Perl with C.</p>
<dl>
<dt>perlbug</dt>
<dd> <i>perlbug</i> is the recommended way to report bugs in the perl interpreter itself or any of the standard library modules back to the developers; please read through the documentation for <i>perlbug</i> thoroughly before using it to submit a bug report.</dd>
<dt>perlthanks</dt>
<dd> This program provides an easy way to send a thank-you message back to the authors and maintainers of perl. It&#8217;s just <i>perlbug</i> installed under another name.</dd>
<dt>h2ph</dt>
<dd> Back before Perl had the XS system for connecting with C libraries, programmers used to get library constants by reading through the C header files. You may still see <tt>&quot;require 'syscall.ph'&quot;</tt> or similar around &#8211; the <i>.ph</i> file should be created by running <i>h2ph</i> on the corresponding <i>.h</i> file. See the <i>h2ph</i> documentation for more on how to convert a whole bunch of header files at once.</dd>
<dt>h2xs</dt>
<dd> <i>h2xs</i> converts C header files into XS modules, and will try and write as much glue between C libraries and Perl modules as it can. It&#8217;s also very useful for creating skeletons of pure Perl modules.</dd>
<dt>enc2xs</dt>
<dd> <i>enc2xs</i> builds a Perl extension for use by Encode from either Unicode Character Mapping files (.ucm) or Tcl Encoding Files (.enc). Besides being used internally during the build process of the Encode module, you can use <i>enc2xs</i> to add your own encoding to perl. No knowledge of XS is necessary.</dd>
<dt>xsubpp</dt>
<dd> <i>xsubpp</i> is a compiler to convert Perl XS code into C code. It is typically run by the makefiles created by ExtUtils::MakeMaker. </dd>
<p> <i>xsubpp</i> will compile XS code into C code by embedding the constructs necessary to let C functions manipulate Perl values and creates the glue necessary to let Perl access those functions.</p>
<dt>prove</dt>
<dd> <i>prove</i> is a command-line interface to the test-running functionality of <i>Test::Harness</i>. It&#8217;s an alternative to <tt>&quot;make test&quot;</tt>.</dd>
<dt>corelist</dt>
<dd> A command-line front-end to <tt>&quot;Module::CoreList&quot;</tt>, to query what modules were shipped with given versions of perl.</dd></dl>
<h3>General tools</h3>
<p> A few general-purpose tools are shipped with perl, mostly because they came along modules included in the perl distribution.</p>
<dl>
<dt>piconv</dt>
<dd> <code>piconv</code> is a Perl version of <code>iconv</code>, a character encoding converter widely available for various Unixen today. This script was primarily a technology demonstrator for Perl v5.8.0, but you can use piconv in the place of iconv for virtually any case.</dd>
<dt>ptar</dt>
<dd> <i>ptar</i> is a tar-like program, written in pure Perl.</dd>
<dt>ptardiff</dt>
<dd> <i>ptardiff</i> is a small utility that produces a diff between an extracted archive and an unextracted one. (Note that this utility requires the <tt>&quot;Text::Diff&quot;</tt> module to function properly; this module isn&#8217;t distributed with perl, but is available from the CPAN.)</dd>
<dt>ptargrep</dt>
<dd> <i>ptargrep</i> is a utility to apply pattern matching to the contents of files in a tar archive.</dd>
<dt>shasum</dt>
<dd> This utility, that comes with the <tt>&quot;Digest::SHA&quot;</tt> module, is used to print or verify SHA checksums.</dd>
<dt>zipdetails</dt>
<dd> zipdetails displays information about the internal record structure of the zip file. It is not concerned with displaying any details of the compressed data stored in the zip file.</dd></dl>
<h3>Installation</h3>
<p> These utilities help manage extra Perl modules that don&#8217;t come with the perl distribution.</p>
<dl>
<dt>cpan</dt>
<dd> <i>cpan</i> is a command-line interface to CPAN.pm. It allows you to install modules or distributions from CPAN, or just get information about them, and a lot more. It is similar to the command line mode of the CPAN module, </dd>
<pre>
    perl -MCPAN -e shell
</pre>
<dt>instmodsh</dt>
<dd> A little interface to ExtUtils::Installed to examine installed modules, validate your packlists and even create a tarball from an installed module.</dd></dl>
<h2>SEE ALSO</h2>
<p> perldoc, pod2man, perlpod, pod2html, pod2usage, podselect, podchecker, splain, perldiag, <tt>&quot;roffitall|roffitall&quot;</tt>, File::Find, pl2pm, perlbug, h2ph, h2xs, enc2xs, xsubpp, cpan, instmodsh, piconv, prove, corelist, ptar, ptardiff, shasum, zipdetails </p>
