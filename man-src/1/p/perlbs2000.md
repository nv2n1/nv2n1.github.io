---
title: "perlbs2000(1)"
name: "perlbs2000"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlbs2000/"
description: "perlbs2000 – building and installing Perl for BS2000."
---

<h2 class="name">NAME</h2>
<p> perlbs2000 &#8211; building and installing Perl for BS2000. </p>
<p> This document needs to be updated, but we don&#8217;t know what it should say. Please email comments to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. </p>
<h2>SYNOPSIS</h2>
<p> This document will help you Configure, build, test and install Perl on <font SIZE="-1">BS2000</font> in the <font SIZE="-1">POSIX</font> subsystem.</p>
<h2>DESCRIPTION</h2>
<p> This is a ported perl for the <font SIZE="-1">POSIX</font> subsystem in <font SIZE="-1">BS2000 VERSION OSD V3.1A</font> or later. It may work on other versions, but we started porting and testing it with 3.1A and are currently using Version V4.0A. </p>
<p> You may need the following <font SIZE="-1">GNU</font> programs in order to install perl:</p>
<h3>gzip on <font SIZE="-1">BS2000</font></h3>
<p> We used version 1.2.4, which could be installed out of the box with one failure during &#8216;make check&#8217;.</p>
<h3>bison on <font SIZE="-1">BS2000</font></h3>
<p> The yacc coming with <font SIZE="-1">BS2000 POSIX</font> didn&#8217;t work for us. So we had to use bison. We had to make a few changes to perl in order to use the pure (reentrant) parser of bison. We used version 1.25, but we had to add a few changes due to <font SIZE="-1">EBCDIC.</font> See below for more details concerning yacc.</p>
<h3>Unpacking Perl Distribution on <font SIZE="-1">BS2000</font></h3>
<p> To extract an <font SIZE="-1">ASCII</font> tar archive on <font SIZE="-1">BS2000 POSIX</font> you need an <font SIZE="-1">ASCII</font> filesystem (we used the mountpoint /usr/local/ascii for this). Now you extract the archive in the <font SIZE="-1">ASCII</font> filesystem without I/O-conversion: </p>
<p> cd /usr/local/ascii export IO_CONVERSION=NO gunzip &lt; /usr/local/src/perl.tar.gz | pax -r </p>
<p> You may ignore the error message for the first element of the archive (this doesn&#8217;t look like a tar archive / skipping to next file&#8230;), it&#8217;s only the directory which will be created automatically anyway. </p>
<p> After extracting the archive you copy the whole directory tree to your <font SIZE="-1">EBCDIC</font> filesystem. <code>This time you use I/O-conversion</code>: </p>
<p> cd /usr/local/src IO_CONVERSION=YES cp -r /usr/local/ascii/perl5.005_02 ./</p>
<h3>Compiling Perl on <font SIZE="-1">BS2000</font></h3>
<p> There is a &#8220;hints&#8221; file for <font SIZE="-1">BS2000</font> called hints.posix-bc (because posix-bc is the <font SIZE="-1">OS</font> name given by `uname`) that specifies the correct values for most things. The major problem is (of course) the <font SIZE="-1">EBCDIC</font> character set. We have german <font SIZE="-1">EBCDIC</font> version. </p>
<p> Because of our problems with the native yacc we used <font SIZE="-1">GNU</font> bison to generate a pure (=reentrant) parser for perly.y. So our yacc is really the following script: </p>
<p> &#8212;&#8211;8&lt;&#8212;&#8211;/usr/local/bin/yacc&#8212;&#8211;8&lt;&#8212;&#8211; #! /usr/bin/sh </p>
<p> # Bison as a reentrant yacc: </p>
<p> # save parameters: params=&quot;&#8220; while [[ $# -gt 1 ]]; do<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;params=&#8221;$params&nbsp;<tt>$1</tt>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shift done </p>
<p> # add flag <tt>%pure_parser:</tt> </p>
<p> tmpfile=/tmp/bison.$$.y echo <tt>%pure_parser</tt> &gt; <tt>$tmpfile</tt> cat <tt>$1</tt> &gt;&gt; <tt>$tmpfile</tt> </p>
<p> # call bison: </p>
<p> echo &#8220;/usr/local/bin/bison &#8211;yacc <tt>$params</tt> <tt>$1</tt>			(Pure Parser)&#8221; /usr/local/bin/bison &#8211;yacc <tt>$params</tt> <tt>$tmpfile</tt> </p>
<p> # cleanup: </p>
<p> rm -f <tt>$tmpfile</tt> &#8212;&#8211;8&lt;&#8212;&#8212;&#8212;-8&lt;&#8212;&#8211; </p>
<p> We still use the normal yacc for a2p.y though!!! We made a softlink called byacc to distinguish between the two versions: </p>
<p> ln -s /usr/bin/yacc /usr/local/bin/byacc </p>
<p> We build perl using <font SIZE="-1">GNU</font> make. We tried the native make once and it worked too.</p>
<h3>Testing Perl on <font SIZE="-1">BS2000</font></h3>
<p> We still got a few errors during <tt>&quot;make test&quot;</tt>. Some of them are the result of using bison. Bison prints <i>parser error</i> instead of <i>syntax error</i>, so we may ignore them. The following list shows our errors, your results may differ: </p>
<p> op/numconvert&#8230;&#8230;.FAILED tests 1409-1440 op/regexp&#8230;&#8230;&#8230;..FAILED tests 483, 496 op/regexp_noamp&#8230;..FAILED tests 483, 496 pragma/overload&#8230;..FAILED tests 152-153, 170-171 pragma/warnings&#8230;..FAILED tests 14, 82, 129, 155, 192, 205, 207 lib/bigfloat&#8230;&#8230;..FAILED tests 351-352, 355 lib/bigfltpm&#8230;&#8230;..FAILED tests 354-355, 358 lib/complex&#8230;&#8230;&#8230;FAILED tests 267, 487 lib/dumper&#8230;&#8230;&#8230;.FAILED tests 43, 45 Failed 11/231 test scripts, 95.24% okay. 57/10595 subtests failed, 99.46% okay.</p>
<h3>Installing Perl on <font SIZE="-1">BS2000</font></h3>
<p> We have no nroff on <font SIZE="-1">BS2000 POSIX</font> (yet), so we ignored any errors while installing the documentation.</p>
<h3>Using Perl in the Posix-Shell of <font SIZE="-1">BS2000</font></h3>
<p> <font SIZE="-1">BS2000 POSIX</font> doesn&#8217;t support the shebang notation (<tt>&quot;#!/usr/local/bin/perl&quot;</tt>), so you have to use the following lines instead: </p>
<p> : # use perl<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;eval&nbsp;&#8216;exec&nbsp;/usr/local/bin/perl -S&nbsp;<tt>$0</tt>&nbsp;${1+&#8220;$@&#8221;}&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;<tt>$running_under_some_shell</tt>;</p>
<h3>Using Perl in native <font SIZE="-1">BS2000</font></h3>
<p> We don&#8217;t have much experience with this yet, but try the following: </p>
<p> Copy your Perl executable to a <font SIZE="-1">BS2000 LLM</font> using bs2cp: </p>
<p> <tt>&quot;bs2cp /usr/local/bin/perl 'bs2:perl(perl,l)'&quot;</tt> </p>
<p> Now you can start it with the following (<font SIZE="-1">SDF</font>) command: </p>
<p> <tt>&quot;/START-PROG FROM-FILE=*MODULE(PERL,PERL),PROG-MODE=*ANY,RUN-MODE=*ADV&quot;</tt> </p>
<p> First you get the <font SIZE="-1">BS2000</font> commandline prompt (&#8216;*&#8217;). Here you may enter your parameters, e.g. <tt>&quot;-e 'print &quot;Hello World!\n&quot;;'&quot;</tt> (note the double backslash!) or <tt>&quot;-w&quot;</tt> and the name of your Perl script. Filenames starting with <tt>&quot;/&quot;</tt> are searched in the Posix filesystem, others are searched in the <font SIZE="-1">BS2000</font> filesystem. You may even use wildcards if you put a <tt>&quot;%&quot;</tt> in front of your filename (e.g. <tt>&quot;-w checkfiles.pl %*.c&quot;</tt>). Read your C/C<font SIZE="-2">++</font> manual for additional possibilities of the commandline prompt (look for PARAMETER-PROMPTING).</p>
<h3>Floating point anomalies on <font SIZE="-1">BS2000</font></h3>
<p> There appears to be a bug in the floating point implementation on <font SIZE="-1">BS2000 POSIX</font> systems such that calling <code>int()</code> on the product of a number and a small magnitude number is not the same as calling <code>int()</code> on the quotient of that number and a large magnitude number. For example, in the following Perl code: </p>
<pre><code>
my $x = 100000.0;
my $y = int($x * 1e-5) * 1e5;
#'0' my $z = int($x / 1e+5) * 1e5;
#'100000' print "\$y is $y and \$z is $z
";
#$y is 0 and $z is 100000
</code></pre>
<p> Although one would expect the quantities <tt>$y</tt> and <tt>$z</tt> to be the same and equal to 100000 they will differ and instead will be 0 and 100000 respectively.</p>
<h3>Using PerlIO and different encodings on <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> partitions</h3>
<p> Since version 5.8 Perl uses the new PerlIO on <font SIZE="-1">BS2000.</font> This enables you using different encodings per <font SIZE="-1">IO</font> channel. For example you may use </p>
<pre><code>
use Encode;
open($f, "&gt;:encoding(ascii)", "test.ascii");
print $f "Hello World!
";
open($f, "&gt;:encoding(posix-bc)", "test.ebcdic");
print $f "Hello World!
";
open($f, "&gt;:encoding(latin1)", "test.latin1");
print $f "Hello World!
";
open($f, "&gt;:encoding(utf8)", "test.utf8");
print $f "Hello World!
";
</code></pre>
<p> to get two files containing &#8220;Hello World!
&#8221; in <font SIZE="-1">ASCII, EBCDIC, ISO</font> Latin-1 (in this example identical to <font SIZE="-1">ASCII</font>) respective UTF-EBCDIC (in this example identical to normal <font SIZE="-1">EBCDIC</font>). See the documentation of Encode::PerlIO for details. </p>
<p> As the PerlIO layer uses raw <font SIZE="-1">IO</font> internally, all this totally ignores the type of your filesystem (<font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC</font>) and the <font SIZE="-1">IO_CONVERSION</font> environment variable. If you want to get the old behavior, that the <font SIZE="-1">BS2000 IO</font> functions determine conversion depending on the filesystem PerlIO still is your friend. You use <font SIZE="-1">IO_CONVERSION</font> as usual and tell Perl, that it should use the native <font SIZE="-1">IO</font> layer: </p>
<pre>
    export IO_CONVERSION=YES
    export PERLIO=stdio
</pre>
<p> Now your <font SIZE="-1">IO</font> would be <font SIZE="-1">ASCII</font> on <font SIZE="-1">ASCII</font> partitions and <font SIZE="-1">EBCDIC</font> on <font SIZE="-1">EBCDIC</font> partitions. See the documentation of PerlIO (without <tt>&quot;Encode::&quot;</tt>!) for further possibilities.</p>
<h2>AUTHORS</h2>
<p> Thomas Dorner</p>
<h2>SEE ALSO</h2>
<p> <font SIZE="-1">INSTALL</font>, perlport.</p>
<h3>Mailing list</h3>
<p> If you are interested in the z/OS (formerly known as <font SIZE="-1">OS/390</font>) and POSIX-BC (<font SIZE="-1">BS2000</font>) ports of Perl then see the perl-mvs mailing list. To subscribe, send an empty message to perl-mvs-subscribe [at] perl.org. </p>
<p> See also: </p>
<pre>
    <a rel="nofollow" href="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a>
</pre>
<p> There are web archives of the mailing list at: </p>
<pre>
    <a rel="nofollow" href="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a>
    <a rel="nofollow" href="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a>
</pre>
<h2>HISTORY</h2>
<p> This document was originally written by Thomas Dorner for the 5.005 release of Perl. </p>
<p> This document was podified for the 5.6 release of perl 11 July 2000. </p>
<h2>Index</h2>
<dt><a href="#lbAO">AUTHORS</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAR">HISTORY</a></p>
<dd></dl>
