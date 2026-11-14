---
title: "perlos390(1)"
name: "perlos390"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlos390/"
---

<h2 class="name">NAME</h2>
 

 perlos390 - building and installing Perl for OS/390 and z/OS 

<h2>SYNOPSIS</h2>

 This document will help you Configure, build, test and install Perl on <font SIZE="-1">OS/390</font> (aka z/OS) Unix System Services. 

 <b>This document needs to be updated, but we don't know what it should say. Please email comments to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;.</b>

<h2>DESCRIPTION</h2>

 This is a fully ported Perl for <font SIZE="-1">OS/390</font> Version 2 Release 3, 5, 6, 7, 8, and 9. It may work on other versions or releases, but those are the ones we've tested it on. 

 You may need to carry out some system configuration tasks before running the Configure script for Perl.

<h3>Tools</h3>

 The z/OS Unix Tools and Toys list may prove helpful and contains links to ports of much of the software helpful for building Perl. &lt;<a rel="nofollow" HREF="http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1toy.html">http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1toy.html</a>&gt;

<h3>Unpacking Perl distribution on <font SIZE="-1">OS/390</font></h3>

 If using ftp remember to transfer the distribution in binary format. 

 Gunzip/gzip for <font SIZE="-1">OS/390</font> is discussed at: 

 <pre>
  <a rel="nofollow" HREF="http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1ty1.html">http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1ty1.html</a>
</pre> 

 to extract an <font SIZE="-1">ASCII</font> tar archive on <font SIZE="-1">OS/390,</font> try this: 

 <pre>
   pax -o to=IBM-1047,from=ISO8859-1 -r &lt; latest.tar
</pre> 

 or 

 <pre>
   zcat latest.tar.Z | pax -o to=IBM-1047,from=ISO8859-1 -r
</pre> 

 If you get lots of errors of the form 

 <pre>
 tar: FSUM7171 ...: cannot set uid/gid: EDC5139I Operation not permitted
</pre> 

 you didn't read the above and tried to use tar instead of pax, you'll first have to remove the (now corrupt) perl directory 

 <pre>
   rm -rf perl-...
</pre> 

 and then use pax.

<h3>Setup and utilities for Perl on <font SIZE="-1">OS/390</font></h3>

 Be sure that your yacc installation is in place including any necessary parser template files. If you have not already done so then be sure to: 

 <pre>
  cp /samples/yyparse.c /etc
</pre> 

 This may also be a good time to ensure that your /etc/protocol file and either your /etc/resolv.conf or /etc/hosts files are in place. The <font SIZE="-1">IBM</font> document that described such <font SIZE="-1">USS</font> system setup issues was <font SIZE="-1">SC28-1890-07 ``OS/390 UNIX</font> System Services Planning'', in particular Chapter 6 on customizing the <font SIZE="-1">OE</font> shell. 

 <font SIZE="-1">GNU</font> make for <font SIZE="-1">OS/390,</font> which is recommended for the build of perl (as well as building <font SIZE="-1">CPAN</font> modules and extensions), is available from the ``Tools''. 

 Some people have reported encountering ``Out of memory!'' errors while trying to build Perl using <font SIZE="-1">GNU</font> make binaries. If you encounter such trouble then try to download the source code kit and build <font SIZE="-1">GNU</font> make from source to eliminate any such trouble. You might also find <font SIZE="-1">GNU</font> make (as well as Perl and Apache) in the red-piece/book ``Open Source Software for <font SIZE="-1">OS/390 UNIX'', SG24-5944-00</font> from <font SIZE="-1">IBM.</font> 

 If instead of the recommended <font SIZE="-1">GNU</font> make you would like to use the system supplied make program then be sure to install the default rules file properly via the shell command: 

 <pre>
    cp /samples/startup.mk /etc
</pre> 

 and be sure to also set the environment variable _C89_CCMODE=1 (exporting _C89_CCMODE=1 is also a good idea for users of <font SIZE="-1">GNU</font> make). 

 You might also want to have <font SIZE="-1">GNU</font> groff for <font SIZE="-1">OS/390</font> installed before running the ``make install'' step for Perl. 

 There is a syntax error in the /usr/include/sys/socket.h header file that <font SIZE="-1">IBM</font> supplies with <font SIZE="-1">USS V2R7, V2R8,</font> and possibly V2R9. The problem with the header file is that near the definition of the <font SIZE="-1">SO_REUSEPORT</font> constant there is a spurious extra '/' character outside of a comment like so: 

 <pre><code>
#define SO_REUSEPORT 0x0200 /* allow local address &amp; port \
                               reuse */                   \
                         /
</code></pre> 

 You could edit that header yourself to remove that last '/', or you might note that Language Environment (<font SIZE="-1">LE</font>) <font SIZE="-1">APAR PQ39997</font> describes the problem and <font SIZE="-1">PTF</font>'s <font SIZE="-1">UQ46272</font> and <font SIZE="-1">UQ46271</font> are the (R8 at least) fixes and apply them. If left unattended that syntax error will turn up as an inability for Perl to build its ``Socket'' extension. 

 For successful testing you may need to turn on the sticky bit for your world readable /tmp directory if you have not already done so (see man chmod).

<h3>Configure Perl on <font SIZE="-1">OS/390</font></h3>

 Once you've unpacked the distribution, run ``sh Configure'' (see <font SIZE="-1">INSTALL</font> for a full discussion of the Configure options). There is a ``hints'' file for os390 that specifies the correct values for most things. Some things to watch out for include:
<dl>
<dt>&bull;
<dd> A message of the form: 

 <pre>
 (I see you are using the Korn shell.  Some ksh's blow up on
 Configure, mainly on older exotic systems.  If yours does, try the
 Bourne shell instead.)
</pre> 

 is nothing to worry about at all.
<dt>&bull;
<dd> Some of the parser default template files in /samples are needed in /etc. In particular be sure that you at least copy /samples/yyparse.c to /etc before running Perl's Configure. This step ensures successful extraction of <font SIZE="-1">EBCDIC</font> versions of parser files such as perly.c and perly.h. This has to be done before running Configure the first time. If you failed to do so then the easiest way to re-Configure Perl is to delete your misconfigured build root and re-extract the source from the tar ball. Then you must ensure that /etc/yyparse.c is properly in place before attempting to re-run Configure.
<dt>&bull;
<dd> This port will support dynamic loading, but it is not selected by default. If you would like to experiment with dynamic loading then be sure to specify -Dusedl in the arguments to the Configure script. See the comments in hints/os390.sh for more information on dynamic loading. If you build with dynamic loading then you will need to add the <tt>$archlibexp</tt>/CORE directory to your <font SIZE="-1">LIBPATH</font> environment variable in order for perl to work. See the config.sh file for the value of <tt>$archlibexp</tt>. If in trying to use Perl you see an error message similar to: 

 <pre>
 CEE3501S The module libperl.dll was not found.
   From entry point __dllstaticinit at compile unit offset +00000194
   at
</pre> 

 then your <font SIZE="-1">LIBPATH</font> does not have the location of libperl.x and either libperl.dll or libperl.so in it. Add that directory to your <font SIZE="-1">LIBPATH</font> and proceed.
<dt>&bull;
<dd> Do not turn on the compiler optimization flag ``-O''. There is a bug in either the optimizer or perl that causes perl to not work correctly when the optimizer is on.
<dt>&bull;
<dd> Some of the configuration files in /etc used by the networking APIs are either missing or have the wrong names. In particular, make sure that there's either an /etc/resolv.conf or an /etc/hosts, so that <b>gethostbyname()</b> works, and make sure that the file /etc/proto has been renamed to /etc/protocol (<font SIZE="-1">NOT</font> /etc/protocols, as used by other Unix systems). You may have to look for things like <font SIZE="-1">HOSTNAME</font> and <font SIZE="-1">DOMAINORIGIN</font> in the ``//'<font SIZE="-1">SYS1.TCPPARMS</font>(<font SIZE="-1">TCPDATA</font>)''' <font SIZE="-1">PDS</font> member in order to properly set up your /etc networking files.</dl>

<h3>Build, Test, Install Perl on <font SIZE="-1">OS/390</font></h3>

 Simply put: 

 <pre>
    sh Configure
    make
    make test
</pre> 

 if everything looks ok (see the next section for test/IVP diagnosis) then: 

 <pre>
    make install
</pre> 

 this last step may or may not require UID=0 privileges depending on how you answered the questions that Configure asked and whether or not you have write access to the directories you specified.

<h3>Build Anomalies with Perl on <font SIZE="-1">OS/390</font></h3>

 ``Out of memory!'' messages during the build of Perl are most often fixed by re building the <font SIZE="-1">GNU</font> make utility for <font SIZE="-1">OS/390</font> from a source code kit. 

 Another memory limiting item to check is your <font SIZE="-1">MAXASSIZE</font> parameter in your '<font SIZE="-1">SYS1.PARMLIB</font>(BPXPRMxx)' data set (note too that as of V2R8 address space limits can be set on a per user <font SIZE="-1">ID</font> basis in the <font SIZE="-1">USS</font> segment of a <font SIZE="-1">RACF</font> profile). People have reported successful builds of Perl with <font SIZE="-1">MAXASSIZE</font> parameters as small as 503316480 (and it may be possible to build Perl with a <font SIZE="-1">MAXASSIZE</font> smaller than that). 

 Within <font SIZE="-1">USS</font> your /etc/profile or <tt>$HOME</tt>/.profile may limit your ulimit settings. Check that the following command returns reasonable values: 

 <pre>
    ulimit -a
</pre> 

 To conserve memory you should have your compiler modules loaded into the Link Pack Area (<font SIZE="-1">LPA/ELPA</font>) rather than in a link list or step lib. 

 If the c89 compiler complains of syntax errors during the build of the Socket extension then be sure to fix the syntax error in the system header /usr/include/sys/socket.h.

<h3>Testing Anomalies with Perl on <font SIZE="-1">OS/390</font></h3>

 The ``make test'' step runs a Perl Verification Procedure, usually before installation. You might encounter <font SIZE="-1">STDERR</font> messages even during a successful run of ``make test''. Here is a guide to some of the more commonly seen anomalies:
<dl>
<dt>&bull;
<dd> A message of the form: 

 <pre>
 io/openpid...........CEE5210S The signal SIGHUP was received.
 CEE5210S The signal SIGHUP was received.
 CEE5210S The signal SIGHUP was received.
 ok
</pre> 

 indicates that the t/io/openpid.t test of Perl has passed but done so with extraneous messages on stderr from <font SIZE="-1">CEE.</font>
<dt>&bull;
<dd> A message of the form: 

 <pre>
 lib/ftmp-security....File::Temp::_gettemp: Parent directory (/tmp/)
 is not safe (sticky bit not set when world writable?) at
 lib/ftmp-security.t line 100
 File::Temp::_gettemp: Parent directory (/tmp/) is not safe (sticky
 bit not set when world writable?) at lib/ftmp-security.t line 100
 ok
</pre> 

 indicates a problem with the permissions on your /tmp directory within the <font SIZE="-1">HFS.</font> To correct that problem issue the command: 

 <pre>
     chmod a+t /tmp
</pre> 

 from an account with write access to the directory entry for /tmp.
<dt>&bull;
<dd> Out of Memory! 

 Recent perl test suite is quite memory hungry. In addition to the comments above on memory limitations it is also worth checking for _CEE_RUNOPTS in your environment. Perl now has (in miniperlmain.c) a C #pragma to set <font SIZE="-1">CEE</font> run options, but the environment variable wins. 

 The C code asks for: 

 <pre>
 #pragma runopts(HEAP(2M,500K,ANYWHERE,KEEP,8K,4K) STACK(,,ANY,) ALL31(ON))
</pre> 

 The important parts of that are the second argument (the increment) to <font SIZE="-1">HEAP,</font> and allowing the stack to be ``Above the (16M) line''. If the heap increment is too small then when perl (for example loading unicode/Name.pl) tries to create a ``big'' (400K+) string it cannot fit in a single segment and you get ``Out of Memory!'' - even if there is still plenty of memory available. 

 A related issue is use with perl's malloc. Perl's malloc uses <tt>&quot;sbrk()&quot;</tt> to get memory, and <tt>&quot;sbrk()&quot;</tt> is limited to the first allocation so in this case something like: 

 <pre>
  HEAP(8M,500K,ANYWHERE,KEEP,8K,4K)
</pre> 

 is needed to get through the test suite.</dl>

<h3>Installation Anomalies with Perl on <font SIZE="-1">OS/390</font></h3>

 The installman script will try to run on <font SIZE="-1">OS/390.</font> There will be fewer errors if you have a roff utility installed. You can obtain <font SIZE="-1">GNU</font> groff from the Redbook <font SIZE="-1">SG24-5944-00</font> ftp site.

<h3>Usage Hints for Perl on <font SIZE="-1">OS/390</font></h3>

 When using perl on <font SIZE="-1">OS/390</font> please keep in mind that the <font SIZE="-1">EBCDIC</font> and <font SIZE="-1">ASCII</font> character sets are different. See perlebcdic.pod for more on such character set issues. Perl builtin functions that may behave differently under <font SIZE="-1">EBCDIC</font> are also mentioned in the perlport.pod document. 

 Open Edition (<font SIZE="-1">UNIX</font> System Services) from V2R8 onward does support #!/path/to/perl script invocation. There is a <font SIZE="-1">PTF</font> available from <font SIZE="-1">IBM</font> for V2R7 that will allow shell/kernel support for #!. <font SIZE="-1">USS</font> releases prior to V2R7 did not support the #! means of script invocation. If you are running V2R6 or earlier then see: 

 <pre>
    head `whence perldoc`
</pre> 

 for an example of how to use the ``eval exec'' trick to ask the shell to have Perl run your scripts on those older releases of Unix System Services. 

 If you are having trouble with square brackets then consider switching your rlogin or telnet client. Try to avoid older 3270 emulators and <font SIZE="-1">ISHELL</font> for working with Perl on <font SIZE="-1">USS.</font>

<h3>Floating Point Anomalies with Perl on <font SIZE="-1">OS/390</font></h3>

 There appears to be a bug in the floating point implementation on S/390 systems such that calling <b>int()</b> on the product of a number and a small magnitude number is not the same as calling <b>int()</b> on the quotient of that number and a large magnitude number. For example, in the following Perl code: 

 
my $x = 100000.0;
my $y = int($x * 1e-5) * 1e5;
#'0' my $z = int($x / 1e+5) * 1e5;
#'100000' print "\$y is $y and \$z is $z\n";
#$y is 0 and $z is 100000
 

 Although one would expect the quantities <tt>$y</tt> and <tt>$z</tt> to be the same and equal to 100000 they will differ and instead will be 0 and 100000 respectively. 

 The problem can be further examined in a roughly equivalent C program: 

 <pre><code>
#include &lt;math.h&gt;
#include &lt;stdio.h&gt;
main()
{
    double r1, r2;
    double x = 100000.0;
    double y = 0.0;
    double z = 0.0;
    x = 100000.0 * 1e-5;
    r1 = modf(x, &amp;y);
    x = 100000.0 / 1e+5;
    r2 = modf(x, &amp;z);
    printf("y is %e and z is %e\n", y * 1e5, z * 1e5);
    /* y is 0.000000e+00 and z is 1.000000e+05 (with c89) */
}
</code></pre>

<h3>Modules and Extensions for Perl on <font SIZE="-1">OS/390</font></h3>

 Pure pure (that is non xs) modules may be installed via the usual: 

 <pre>
    perl Makefile.PL
    make
    make test
    make install
</pre> 

 If you built perl with dynamic loading capability then that would also be the way to build xs based extensions. However, if you built perl with the default static linking you can still build xs based extensions for <font SIZE="-1">OS/390</font> but you will need to follow the instructions in ExtUtils::MakeMaker for building statically linked perl binaries. In the simplest configurations building a static perl + xs extension boils down to: 

 <pre>
    perl Makefile.PL
    make
    make perl
    make test
    make install
    make -f Makefile.aperl inst_perl MAP_TARGET=perl
</pre> 

 In most cases people have reported better results with <font SIZE="-1">GNU</font> make rather than the system's /bin/make program, whether for plain modules or for xs based extensions. 

 If the make process encounters trouble with either compilation or linking then try setting the _C89_CCMODE to 1. Assuming sh is your login shell then run: 

 <pre>
    export _C89_CCMODE=1
</pre> 

 If tcsh is your login shell then use the setenv command.

<h2>AUTHORS</h2>

 David Fiander and Peter Prymmer with thanks to Dennis Longnecker and William Raffloer for valuable reports, <font SIZE="-1">LPAR</font> and <font SIZE="-1">PTF</font> feedback. Thanks to Mike MacIsaac and Egon Terwedow for <font SIZE="-1">SG24-5944-00.</font> Thanks to Ignasi Roca for pointing out the floating point problems. Thanks to John Goodyear for dynamic loading help.

<h2>SEE ALSO</h2>

 <font SIZE="-1">INSTALL</font>, perlport, perlebcdic, ExtUtils::MakeMaker. 

 <pre>
 <a rel="nofollow" HREF="http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1toy.html">http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1toy.html</a>
 <a rel="nofollow" HREF="http://www.redbooks.ibm.com/redbooks/SG245944.html">http://www.redbooks.ibm.com/redbooks/SG245944.html</a>
 <a rel="nofollow" HREF="http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1ty1.html#opensrc">http://www.ibm.com/servers/eserver/zseries/zos/unix/bpxa1ty1.html#opensrc</a>
 <a rel="nofollow" HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a>
 <a rel="nofollow" HREF="http://publibz.boulder.ibm.com:80/cgi-bin/bookmgr_OS390/BOOKS/ceea3030/">http://publibz.boulder.ibm.com:80/cgi-bin/bookmgr_OS390/BOOKS/ceea3030/</a>
 <a rel="nofollow" HREF="http://publibz.boulder.ibm.com:80/cgi-bin/bookmgr_OS390/BOOKS/CBCUG030/">http://publibz.boulder.ibm.com:80/cgi-bin/bookmgr_OS390/BOOKS/CBCUG030/</a>
</pre>

<h3>Mailing list for Perl on <font SIZE="-1">OS/390</font></h3>

 If you are interested in the z/OS (formerly known as <font SIZE="-1">OS/390</font>) and POSIX-BC (<font SIZE="-1">BS2000</font>) ports of Perl then see the perl-mvs mailing list. To subscribe, send an empty message to perl-mvs-subscribe [at] perl.org. 

 See also: 

 <pre>
    <a rel="nofollow" HREF="http://lists.perl.org/list/perl-mvs.html">http://lists.perl.org/list/perl-mvs.html</a>
</pre> 

 There are web archives of the mailing list at: 

 <pre>
    <a rel="nofollow" HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/">http://www.xray.mpe.mpg.de/mailing-lists/perl-mvs/</a>
    <a rel="nofollow" HREF="http://archive.develooper.com/perl-mvs@perl.org/">http://archive.develooper.com/perl-mvs@perl.org/</a>
</pre>

<h2>HISTORY</h2>

 This document was originally written by David Fiander for the 5.005 release of Perl. 

 This document was podified for the 5.005_03 release of Perl 11 March 1999. 

 Updated 28 November 2001 for broken URLs. 

 Updated 12 November 2000 for the 5.7.1 release of Perl. 

 Updated 15 January 2001 for the 5.7.1 release of Perl. 

 Updated 24 January 2001 to mention dynamic loading. 

 Updated 12 March 2001 to mention //'<font SIZE="-1">SYS1.TCPPARMS</font>(<font SIZE="-1">TCPDATA</font>)'. 

<h2>Index</h2>



<dt><a HREF="#lbAP">AUTHORS</a>
<dd>
<dt><a HREF="#lbAQ">SEE ALSO</a>
<dd>


<dt><a HREF="#lbAS">HISTORY</a>
<dd></dl>
