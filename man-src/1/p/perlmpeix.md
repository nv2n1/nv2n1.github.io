---

title: "perlmpeix(1)"
name: "perlmpeix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmpeix/"
---

perlmpeix - Perl/iX for HP e3000 MPE 

<h2>SYNOPSIS</h2>

 <pre>
   <a rel="nofollow" HREF="http://www.bixby.org/mark/perlix.html">http://www.bixby.org/mark/perlix.html</a>
   Perl language for MPE
   Last updated January 12, 2006 @ 2100 UTC
</pre>

<h2>NOTE</h2>

 This is a podified version of what used to be on the above-mentioned web page, podified by Jarkko Hietaniemi 2001-Jan-01.

<h2>What's New in Perl for MPE/iX</h2>

 January 12, 2006
<dl>
<dt>&bull;
</dt><dd> Updated for perl-5.8.8 and perl-5.9.3 by Ken Hirsch. 
 Simplified the build process by using the MPEAUTOCONF functionality in Mark Klein's ld. 
 If you build this from scratch, make sure you have a version of ld which supports it. In the shell, type 
 <pre>
  ld --help
    and look for AUTOCONF or MPEAUTOCONF near the bottom
  or do this:
  ld --help 2&gt;&amp;1 | grep AUTOCONF
</pre> 
 If you see don't see AUTOCONF or MPEAUTOCONF, make sure you get a new version. 
 You also do not have to use mpeix/relink after building, so the recommend sequence is: 
 <pre><code>
./ Configure - de
# or./ Configure - de - Dusedevel
#if you're building a development version
                   make
                       make test
#if you run this in a job, do "make test_notty"
                           make install
</code></pre> 
 Be prepared for a wait. These take much longer on MPE/iX than on a Unix system, because of a slow forking, mostly. On a lightly-loaded HP3000 Series 979 running MPE/iX 7.5: 
 <pre>
    Configure: 1 hour
    make:      1 hour 15 minutes
    make test  1 hour 45 minutes
</pre> 
 Various socket problems were fixed in mpeix.c. 
 Mark Klein provided a fixed sigsetjmp (that works with dynamic libraries) in mpeix_setjmp.c</dd></dl>
 

 June 1, 2000
<dl>
<dt>&bull;
</dt><dd> Rebuilt to be compatible with mod_perl. If you plan on using mod_perl, you MUST download and install this version of Perl/iX!
</dd><dt>&bull;
</dt><dd> uselargefiles=``undef'': not available in MPE for POSIX files yet.
</dd><dt>&bull;
</dt><dd> Now bundled with various add-on packages:
</dd><dl>
<dl>
<dt>&bull;
</dt><dd> libnet (as seen on CPAN)
</dd><dt>&bull;
</dt><dd> libwww-perl (LWP) which lets Perl programs behave like web browsers:
</dd><dt>&bull;
</dt><dd> mod_perl (just the perl portion; the actual DSO will be released soon with Apache/iX 1.3.12 from bixby.org). This module allows you to write high performance persistent Perl CGI scripts and all sorts of cool things. (&lt;<a rel="nofollow" HREF="http://perl.apache.org/">http://perl.apache.org/</a>&gt;) 
 and much much more hiding under /PERL/PUB/.cpan/
</dd><dt>&bull;
</dt><dd> The CPAN module now works for automatic downloading and installing of add-on packages: 
 <pre>
    1. export FTP_PASSIVE=1
    2. perl -MCPAN -e shell
    3. Ignore any terminal I/O related complaints!
</pre> 
 (&lt;<a rel="nofollow" HREF="http://search.cpan.org/dist/CPAN/">http://search.cpan.org/dist/CPAN/</a>&gt;)</dd></dl>
</dl>

<dl>
</dl>
</dl>
 

 May 20, 2000
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.6.0. Builds straight out of the box on MPE/iX.
</dd><dt>&bull;
</dt><dd> Perl's <i>getpwnam()</i> function which had regressed to being unimplemented on MPE is now implemented once again.</dd></dl>
 

 September 17, 1999
<dl>
<dt>&bull;
</dt><dd> Migrated from cccd.edu to bixby.org.</dd></dl>

<h2>Welcome to Perl/iX</h2>

 This is the official home page for the HP e3000 MPE/iX ( &lt;<a rel="nofollow" HREF="http://www.hp.com/go/e3000">http://www.hp.com/go/e3000</a>&gt; ) port of the Perl scripting language ( &lt;<a rel="nofollow" HREF="http://www.perl.com/">http://www.perl.com/</a>&gt; ) which gives you all of the power of C, awk, sed, and sh in a single language. Check here for the latest news, implemented functionality, known bugs, to-do list, etc. Status reports about major milestones will also be posted to the HP3000-L mailing list ( <a rel="nofollow" HREF="http://www.lsoft.com/scripts/wl.exe?SL1=HP3000-L">http://www.lsoft.com/scripts/wl.exe?SL1=HP3000-L</a>&amp;H=RAVEN.UTC.EDU &lt;<a HREF="http://www.lsoft.com/scripts/wl.exe?SL1=HP3000-L">http://www.lsoft.com/scripts/wl.exe?SL1=HP3000-L</a>&amp;H=RAVEN.UTC.EDU&gt; ) and its associated gatewayed newsgroup comp.sys.hp.mpe. 

 I'm doing this port because I can't live without Perl on the Unix machines that I administer, and I want to have the same power available to me on MPE. 

 Please send your comments, questions, and bug reports directly to me, Mark Bixby ( &lt;<a rel="nofollow" HREF="http://www.bixby.org/mark/">http://www.bixby.org/mark/</a>&gt; ). Or just post them to HP3000-L. 

 The platform I'm using to do this port is an HP 3000 957RX running MPE/iX 6.0 and using the GNU gcc C compiler ( &lt;<a rel="nofollow" HREF="http://jazz.external.hp.com/src/gnu/gnuframe.html">http://jazz.external.hp.com/src/gnu/gnuframe.html</a>&gt; ). 

 The combined porting wisdom from all of my ports can be found in my MPE/iX Porting Guide (&lt;<a rel="nofollow" HREF="http://www.bixby.org/mark/porting.html">http://www.bixby.org/mark/porting.html</a>&gt;). 

 IMPORTANT NOTICE: Yes, I do work for the HP CSY R&amp;D lab, but ALL of the software you download from bixby.org is my personal freeware that is NOT supported by HP.

<h2>System Requirements for Perl/iX</h2>

<dl>
<dt>&bull;
</dt><dd> MPE/iX 5.5 or later. This version of Perl/iX does NOT run on MPE/iX 5.0 or earlier, nor does it run on ``classic'' MPE/V machines.
</dd><dt>&bull;
</dt><dd> If you wish to recompile Perl, you must install both GNUCORE and GNUGCC from jazz (&lt;<a rel="nofollow" HREF="http://jazz.external.hp.com/src/gnu/gnuframe.html">http://jazz.external.hp.com/src/gnu/gnuframe.html</a>&gt;).
</dd><dt>&bull;
</dt><dd> Perl/iX will be happier on MPE/iX 5.5 if you install the MPEKX40B extended POSIX filename characters patch, but this is optional.
</dd><dt>&bull;
</dt><dd> Patch LBCJXT6A is required on MPE/iX 5.5 machines in order to prevent Perl/iX from dying with an unresolved external reference to _getenv_libc.
</dd><dt>&bull;
</dt><dd> If you will be compiling Perl/iX yourself, you will also need Syslog/iX ( &lt;<a rel="nofollow" HREF="http://www.bixby.org/mark/syslogix.html">http://www.bixby.org/mark/syslogix.html</a>&gt; ) and the /BIND/PUB/include and /BIND/PUB/lib portions of BIND/iX ( &lt;<a rel="nofollow" HREF="http://www.bixby.org/mark/bindix.html">http://www.bixby.org/mark/bindix.html</a>&gt; ).</dd></dl>

<h2>How to Obtain Perl/iX</h2>

<dl>
<dt>1.
</dt><dd> Download Perl using either FTP.ARPA.SYS or some other client
</dd><dt>2.
</dt><dd> Extract the installation script
</dd><dt>3.
</dt><dd> Edit the installation script
</dd><dt>4.
</dt><dd> Run the installation script
</dd><dt>5.
</dt><dd> Convert your *.a system archive libraries to *.sl shared libraries</dd></dl>
 

 Download Perl using FTP.ARPA.SYS from your HP 3000 (the preferred method)..... 

 <pre>
    :HELLO MANAGER.SYS
    :XEQ FTP.ARPA.SYS
    open <a HREF="ftp://ftp.bixby.org">ftp.bixby.org</a>
    anonymous
    your [at] email.address
    bytestream
    cd /pub/mpe
    get perl-5.6.0-mpe.tar.Z /tmp/perl.tar.Z;disc=2147483647
    exit
</pre> 

 .....Or download using some other generic web or ftp client (the alternate method) 

 Download the following files (make sure that you use ``binary mode'' or whatever client feature that is 8-bit clean):
<dl>
<dt>&bull;
</dt><dd> Perl from 
 <pre>
    <a rel="nofollow" HREF="http://www.bixby.org/ftp/pub/mpe/perl-5.6.0-mpe.tar.Z">http://www.bixby.org/ftp/pub/mpe/perl-5.6.0-mpe.tar.Z</a>
</pre> 
 or 
 <pre>
    <a HREF="ftp://ftp.bixby.org/pub/mpe/perl-5.6.0-mpe.tar.Z">ftp://ftp.bixby.org/pub/mpe/perl-5.6.0-mpe.tar.Z</a>
</pre>
</dd><dt>&bull;
</dt><dd> Upload those files to your HP 3000 in an 8-bit clean bytestream manner to: 
 <pre>
    /tmp/perl.tar.Z
</pre>
</dd><dt>&bull;
</dt><dd> Then extract the installation script (after both download methods) 
 <pre>
    :CHDIR /tmp
    :XEQ TAR.HPBIN.SYS 'xvfopz /tmp/perl.tar.Z INSTALL'
</pre>
</dd><dt>&bull;
</dt><dd> Edit the installation script 
 Examine the accounting structure creation commands and modify if necessary (adding additional capabilities, choosing a non-system volume set, etc). 
 <pre>
    :XEQ VI.HPBIN.SYS /tmp/INSTALL
</pre>
</dd><dt>&bull;
</dt><dd> Run the installation script. 
 The accounting structure will be created and then all files will be extracted from the archive. 
 <pre>
    :XEQ SH.HPBIN.SYS /tmp/INSTALL
</pre>
</dd><dt>&bull;
</dt><dd> Convert your *.a system archive libraries to *.sl shared libraries 
 You only have to do this ONCE on your MPE/iX 5.5 machine in order to convert /lib/lib*.a and /usr/lib/lib*.a libraries to their *.sl equivalents. This step should not be necessary on MPE/iX 6.0 or later machines because the 6.0 or later update process does it for you. 
 <pre>
    :XEQ SH.HPBIN.SYS /PERL/PUB/LIBSHP3K
</pre></dd></dl>

<h2>Perl/iX Distribution Contents Highlights</h2>

<dl>
<dt>README
</dt><dd> The file you're reading now.
</dd><dt>INSTALL
</dt><dd> Perl/iX Installation script.
</dd><dt>LIBSHP3K
</dt><dd> Script to convert *.a system archive libraries to *.sl shared libraries.
</dd><dt>PERL
</dt><dd> Perl NMPRG executable. A version-numbered backup copy also exists. You might wish to ``ln -s /PERL/PUB/PERL /usr/local/bin/perl''.
</dd><dt>.cpan/
</dt><dd> Much add-on source code downloaded with the CPAN module.
</dd><dt>lib/
</dt><dd> Perl libraries, both core and add-on.
</dd><dt>man/
</dt><dd> Perl man page documentation.
</dd><dt>public_html/feedback.cgi
</dt><dd> Sample feedback CGI form written in Perl.
</dd><dt>src/perl-5.6.0-mpe
</dt><dd> Source code.</dd></dl>

<h2>How to Compile Perl/iX</h2>

<dl>
<dt>1.
</dt><dd> cd src/perl-5.6.0-mpe
</dd><dt>2.
</dt><dd> Read the INSTALL file for the official instructions
</dd><dt>3.
</dt><dd> ./Configure -d
</dd><dt>4.
</dt><dd> make
</dd><dt>5.
</dt><dd> ./mpeix/relink
</dd><dt>6.
</dt><dd> make test (expect approximately 15 out of 11306 subtests to fail, mostly due to MPE not supporting hard links, UDP socket problems, and handling <i>exit()</i> return codes improperly)
</dd><dt>7.
</dt><dd> make install
</dd><dt>8.
</dt><dd> Optionally create symbolic links that point to the Perl executable, i.e. ln -s /PERL/PUB/PERL /usr/local/bin/perl</dd></dl>
 

 The summary test results from ``cd t; ./perl -I../lib harness'': 

 <pre><code>
Failed Test Status Wstat Total Fail Failed List of failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -io / fs.t 29 8 27.59 % 2 - 5, 7 - 9, 11 io / openpid.t 10 1 10.00 % 7 lib / io_sock.t 14 1 7.14 % 13 lib / io_udp.t 7 2 28.57 % 3, 5 lib / posix.t 27 1 3.70 % 12 op / lex_assign.t 187 1 0.53 % 13 op / stat.t 58 1 1.72 % 3 15 tests and 94 subtests skipped.Failed 7 / 236 test scripts, 97.03 % okay.15 / 11306 subtests failed, 99.87 % okay.
</code></pre>

<h2>Getting Started with Perl/iX</h2>

 Create your Perl script files with ``#!/PERL/PUB/perl'' (or an equivalent symbolic link) as the first line. Use the chmod command to make sure that your script has execute permission. Run your script! 

 Be sure to take a look at the CPAN module list ( &lt;<a rel="nofollow" HREF="http://www.cpan.org/CPAN.html">http://www.cpan.org/CPAN.html</a>&gt; ). A wide variety of free Perl software is available. You can automatically download these packages by using the CPAN module ( &lt;<a rel="nofollow" HREF="http://search.cpan.org/dist/CPAN/">http://search.cpan.org/dist/CPAN/</a>&gt; ).

<h2>MPE/iX Implementation Considerations</h2>

 There some minor functionality issues to be aware of when comparing Perl for Unix (Perl/UX) to Perl/iX:
<dl>
<dt>&bull;
</dt><dd> MPE gcc/ld doesn't properly support linking NMPRG executables against NMXL dynamic libraries, so you must manually run mpeix/relink after each re-build of Perl.
</dd><dt>&bull;
</dt><dd> Perl/iX File::Copy will use MPE's /bin/cp command to copy files by name in order to preserve file attributes like file code.
</dd><dt>&bull;
</dt><dd> MPE (and thus Perl/iX) lacks support for <i>setgrent()</i>, <i>endgrent()</i>, <i>setpwent()</i>, <i>endpwent()</i>.
</dd><dt>&bull;
</dt><dd> MPE (and thus Perl/iX) lacks support for hard links.
</dd><dt>&bull;
</dt><dd> MPE requires <i>GETPRIVMODE</i><i>()</i> in order to <i>bind()</i> to ports less than 1024. Perl/iX will call <i>GETPRIVMODE</i><i>()</i> automatically on your behalf if you attempt to <i>bind()</i> to these low-numbered ports. Note that the Perl/iX executable and the PERL account do not normally have CAP=PM, so if you will be <i>bind()</i>-ing to these privileged ports, you will manually need to add PM capability as appropriate.
</dd><dt>&bull;
</dt><dd> MPE requires that you <i>bind()</i> to an IP address of zero. Perl/iX automatically replaces the IP address that you pass to <i>bind()</i> with a zero.
</dd><dt>&bull;
</dt><dd> MPE requires <i>GETPRIVMODE</i><i>()</i> in order to <i>setuid()</i>. There are too many calls to <i>setuid()</i> within Perl/iX, so I have not attempted an automatic <i>GETPRIVMODE</i><i>()</i> solution similar to <i>bind()</i>.</dd></dl>

<h2>Known Perl/iX Bugs Under Investigation</h2>

 None.

<h2>Perl/iX To-Do List</h2>

<dl>
<dt>&bull;
</dt><dd> Make <i>setuid()</i>/<i>setgid()</i> support work.
</dd><dt>&bull;
</dt><dd> Make sure that <i>fcntl()</i> against a socket descriptor is redirected to <i>sfcntl()</i>.
</dd><dt>&bull;
</dt><dd> Add support for Berkeley DB once I've finished porting Berkeley DB.
</dd><dt>&bull;
</dt><dd> Write an MPE XS extension library containing miscellaneous important MPE functions like <i>GETPRIVMODE</i><i>()</i>, <i>GETUSERMODE</i><i>()</i>, and <i>sfcntl()</i>.</dd></dl>

<h2>Perl/iX Change History</h2>

 May 6, 1999
<dl>
<dt>&bull;
</dt><dd> Patch LBCJXT6A is required on MPE/iX 5.5 machines in order to prevent Perl/iX from dying with an unresolved external reference to _getenv_libc.</dd></dl>
 

 April 7, 1999
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.005_03.
</dd><dt>&bull;
</dt><dd> The official source distribution once again compiles ``straight out of the box'' for MPE.
</dd><dt>&bull;
</dt><dd> The current incarnation of the 5.5 POSIX filename extended characters patch is now MPEKX40B.
</dd><dt>&bull;
</dt><dd> The LIBSHP3K *.a -&gt; *.sl library conversion script is now included as /PERL/PUB/LIBSHP3K.</dd></dl>
 

 November 20, 1998
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.005_02.
</dd><dt>&bull;
</dt><dd> Fixed a DynaLoader bug that was unable to load symbols from relative path name libraries.
</dd><dt>&bull;
</dt><dd> Fixed a .xs compilation bug where the mpeixish.sh include file wasn't being installed into the proper directory.
</dd><dt>&bull;
</dt><dd> All bugfixes will be submitted back to the official Perl developers.
</dd><dt>&bull;
</dt><dd> The current incarnation of the POSIX filename extended characters patch is now MPEKXJ3A.</dd></dl>
 

 August 14, 1998
<dl>
<dt>&bull;
</dt><dd> The previous POSIX filename extended characters patch MPEKX44C has been superseded by MPEKXB5A.</dd></dl>
 

 August 7, 1998
<dl>
<dt>&bull;
</dt><dd> The previous POSIX filename extended characters patch MPEKX76A has been superseded by MPEKX44C.</dd></dl>
 

 July 28, 1998
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.005_01.</dd></dl>
 

 July 23, 1998
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.005 (production release). The public freeware sources are now 100% MPE-ready ``straight out of the box''.</dd></dl>
 

 July 17, 1998
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.005b1 (public beta release). The public freeware sources are now 99.9% MPE-ready. By installing and testing this beta on your own HP3000, you will be helping to insure that the final release of 5.005 will be 100% MPE-ready and 100% bug free.
</dd><dt>&bull;
</dt><dd> My MPE binary release is now extracted using my standard INSTALL script.</dd></dl>
 

 July 15, 1998
<dl>
<dt>&bull;
</dt><dd> Changed startperl to #!/PERL/PUB/perl so that Perl will recognize scripts more easily and efficiently.</dd></dl>
 

 July 8, 1998
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.004_70 (internal developer release) which is now MPE-ready. The next public freeware release of Perl should compile ``straight out of the box'' on MPE. Note that this version of Perl/iX was strictly internal to me and never publicly released. Note that [21]BIND/iX is now required (well, the include files and libbind.a) if you wish to compile Perl/iX.</dd></dl>
 

 November 6, 1997
<dl>
<dt>&bull;
</dt><dd> Updated to version 5.004_04. No changes in MPE-specific functionality.</dd></dl>
 

 October 16, 1997
<dl>
<dt>&bull;
</dt><dd> Added Demos section to the Perl/iX home page so you can see some sample Perl applications running on my 3000.</dd></dl>
 

 October 3, 1997
<dl>
<dt>&bull;
</dt><dd> Added System Requirements section to the Perl/iX home page just so the prerequisites stand out more. Various other home page tweaks.</dd></dl>
 

 October 2, 1997
<dl>
<dt>&bull;
</dt><dd> Initial public release.</dd></dl>
 

 September 1997
<dl>
<dt>&bull;
</dt><dd> Porting begins.</dd></dl>

<h2>AUTHOR</h2>

 Mark Bixby, &lt;<a rel="nofollow" HREF="http://www.bixby.org/mark/">http://www.bixby.org/mark/</a>&gt;
