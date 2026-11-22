---

title: "perlbs2000(1)"
name: "perlbs2000"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlbs2000/"
description: "perlbs2000 – building and installing Perl for BS2000."
---

<p> perlbs2000 &#8211; building and installing Perl for BS2000. </p>
<p> This document needs to be updated, but we don&#8217;t know what it should say. Please email comments to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. </p>
<h2>SYNOPSIS</h2>
<p> This document will help you Configure, build, test and install Perl on BS2000 in the POSIX subsystem.</p>
<h2>DESCRIPTION</h2>
<p> This is a ported perl for the POSIX subsystem in BS2000 VERSION OSD V3.1A or later. It may work on other versions, but we started porting and testing it with 3.1A and are currently using Version V4.0A. </p>
<p> You may need the following GNU programs in order to install perl:</p>
<h3>gzip on BS2000</h3>
<p> We used version 1.2.4, which could be installed out of the box with one failure during &#8216;make check&#8217;.</p>
<h3>bison on BS2000</h3>
<p> The yacc coming with BS2000 POSIX didn&#8217;t work for us. So we had to use bison. We had to make a few changes to perl in order to use the pure (reentrant) parser of bison. We used version 1.25, but we had to add a few changes due to EBCDIC. See below for more details concerning yacc.</p>
<h3>Unpacking Perl Distribution on BS2000</h3>
<p> To extract an ASCII tar archive on BS2000 POSIX you need an ASCII filesystem (we used the mountpoint /usr/local/ascii for this). Now you extract the archive in the ASCII filesystem without I/O-conversion: </p>
<p> cd /usr/local/ascii export IO_CONVERSION=NO gunzip &lt; /usr/local/src/perl.tar.gz | pax -r </p>
<p> You may ignore the error message for the first element of the archive (this doesn&#8217;t look like a tar archive / skipping to next file&#8230;), it&#8217;s only the directory which will be created automatically anyway. </p>
<p> After extracting the archive you copy the whole directory tree to your EBCDIC filesystem. <code>This time you use I/O-conversion</code>: </p>
<p> cd /usr/local/src IO_CONVERSION=YES cp -r /usr/local/ascii/perl5.005_02 ./</p>
<h3>Compiling Perl on BS2000</h3>
<p> There is a &#8220;hints&#8221; file for BS2000 called hints.posix-bc (because posix-bc is the OS name given by `uname`) that specifies the correct values for most things. The major problem is (of course) the EBCDIC character set. We have german EBCDIC version. </p>
<p> Because of our problems with the native yacc we used GNU bison to generate a pure (=reentrant) parser for perly.y. So our yacc is really the following script: </p>
<p> &#8212;&#8211;8&lt;&#8212;&#8211;/usr/local/bin/yacc&#8212;&#8211;8&lt;&#8212;&#8211; #! /usr/bin/sh </p>
<p> # Bison as a reentrant yacc: </p>
<p> # save parameters: params=&quot;&#8220; while [[ $# -gt 1 ]]; do<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;params=&#8221;$params&nbsp;<tt>$1</tt>&quot;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shift done </p>
<p> # add flag <tt>%pure_parser:</tt> </p>
<p> tmpfile=/tmp/bison.$$.y echo <tt>%pure_parser</tt> &gt; <tt>$tmpfile</tt> cat <tt>$1</tt> &gt;&gt; <tt>$tmpfile</tt> </p>
<p> # call bison: </p>
<p> echo &#8220;/usr/local/bin/bison &#8211;yacc <tt>$params</tt> <tt>$1</tt>			(Pure Parser)&#8221; /usr/local/bin/bison &#8211;yacc <tt>$params</tt> <tt>$tmpfile</tt> </p>
<p> # cleanup: </p>
<p> rm -f <tt>$tmpfile</tt> &#8212;&#8211;8&lt;&#8212;&#8212;&#8212;-8&lt;&#8212;&#8211; </p>
<p> We still use the normal yacc for a2p.y though!!! We made a softlink called byacc to distinguish between the two versions: </p>
<p> ln -s /usr/bin/yacc /usr/local/bin/byacc </p>
<p> We build perl using GNU make. We tried the native make once and it worked too.</p>
<h3>Testing Perl on BS2000</h3>
<p> We still got a few errors during <tt>&quot;make test&quot;</tt>. Some of them are the result of using bison. Bison prints <i>parser error</i> instead of <i>syntax error</i>, so we may ignore them. The following list shows our errors, your results may differ: </p>
<p> op/numconvert&#8230;&#8230;.FAILED tests 1409-1440 op/regexp&#8230;&#8230;&#8230;..FAILED tests 483, 496 op/regexp_noamp&#8230;..FAILED tests 483, 496 pragma/overload&#8230;..FAILED tests 152-153, 170-171 pragma/warnings&#8230;..FAILED tests 14, 82, 129, 155, 192, 205, 207 lib/bigfloat&#8230;&#8230;..FAILED tests 351-352, 355 lib/bigfltpm&#8230;&#8230;..FAILED tests 354-355, 358 lib/complex&#8230;&#8230;&#8230;FAILED tests 267, 487 lib/dumper&#8230;&#8230;&#8230;.FAILED tests 43, 45 Failed 11/231 test scripts, 95.24% okay. 57/10595 subtests failed, 99.46% okay.</p>
<h3>Installing Perl on BS2000</h3>
<p> We have no nroff on BS2000 POSIX (yet), so we ignored any errors while installing the documentation.</p>
<h3>Using Perl in the Posix-Shell of BS2000</h3>
<p> BS2000 POSIX doesn&#8217;t support the shebang notation (<tt>&quot;#!/usr/local/bin/perl&quot;</tt>), so you have to use the following lines instead: </p>
<p> : # use perl<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;eval&nbsp;&#8216;exec&nbsp;/usr/local/bin/perl -S&nbsp;<tt>$0</tt>&nbsp;${1+&#8220;$@&#8221;}&#8217;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;<tt>$running_under_some_shell</tt>;</p>
<h3>Using Perl in native BS2000</h3>
<p> We don&#8217;t have much experience with this yet, but try the following: </p>
<p> Copy your Perl executable to a BS2000 LLM using bs2cp: </p>
<p> <tt>&quot;bs2cp /usr/local/bin/perl 'bs2:perl(perl,l)'&quot;</tt> </p>
<p> Now you can start it with the following (SDF) command: </p>
<p> <tt>&quot;/START-PROG FROM-FILE=*MODULE(PERL,PERL),PROG-MODE=*ANY,RUN-MODE=*ADV&quot;</tt> </p>
<p> First you get the BS2000 commandline prompt (&#8216;*&#8217;). Here you may enter your parameters, e.g. <tt>&quot;-e 'print &quot;Hello World!\n&quot;;'&quot;</tt> (note the double backslash!) or <tt>&quot;-w&quot;</tt> and the name of your Perl script. Filenames starting with <tt>&quot;/&quot;</tt> are searched in the Posix filesystem, others are searched in the BS2000 filesystem. You may even use wildcards if you put a <tt>&quot;%&quot;</tt> in front of your filename (e.g. <tt>&quot;-w checkfiles.pl %*.c&quot;</tt>). Read your C/C++ manual for additional possibilities of the commandline prompt (look for PARAMETER-PROMPTING).</p>
<h3>Floating point anomalies on BS2000</h3>
<p> There appears to be a bug in the floating point implementation on BS2000 POSIX systems such that calling <code>int()</code> on the product of a number and a small magnitude number is not the same as calling <code>int()</code> on the quotient of that number and a large magnitude number. For example, in the following Perl code: </p>
<pre><code>
my $x = 100000.0;
my $y = int($x * 1e-5) * 1e5;
#'0' my $z = int($x / 1e+5) * 1e5;
#'100000' print "\$y is $y and \$z is $z
";
#$y is 0 and $z is 100000
</code></pre>
<p> Although one would expect the quantities <tt>$y</tt> and <tt>$z</tt> to be the same and equal to 100000 they will differ and instead will be 0 and 100000 respectively.</p>
<h3>Using PerlIO and different encodings on ASCII and EBCDIC partitions</h3>
<p> Since version 5.8 Perl uses the new PerlIO on BS2000. This enables you using different encodings per IO channel. For example you may use </p>
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
&#8221; in ASCII, EBCDIC, ISO Latin-1 (in this example identical to ASCII) respective UTF-EBCDIC (in this example identical to normal EBCDIC). See the documentation of Encode::PerlIO for details. </p>
<p> As the PerlIO layer uses raw IO internally, all this totally ignores the type of your filesystem (ASCII or EBCDIC) and the IO_CONVERSION environment variable. If you want to get the old behavior, that the BS2000 IO functions determine conversion depending on the filesystem PerlIO still is your friend. You use IO_CONVERSION as usual and tell Perl, that it should use the native IO layer: </p>
<pre>
    export IO_CONVERSION=YES
    export PERLIO=stdio
</pre>
<p> Now your IO would be ASCII on ASCII partitions and EBCDIC on EBCDIC partitions. See the documentation of PerlIO (without <tt>&quot;Encode::&quot;</tt>!) for further possibilities.</p>
<h2>AUTHORS</h2>
<p> Thomas Dorner</p>
<h2>SEE ALSO</h2>
<p> INSTALL, perlport.</p>
<h3>Mailing list</h3>
<p> If you are interested in the z/OS (formerly known as OS/390) and POSIX-BC (BS2000) ports of Perl then see the perl-mvs mailing list. To subscribe, send an empty message to perl-mvs-subscribe [at] perl.org. </p>
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
