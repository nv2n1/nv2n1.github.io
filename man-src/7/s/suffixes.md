---
title: "suffixes(7)"
name: "suffixes"
section: "7"
letter: "s"
url: "/docs/linux/man/7-suffixes/"
description: "suffixes – list of file suffixes"
---

<p>suffixes &#8211; list of file suffixes</p>
<h2>Description</h2>
<p>It is customary to indicate the contents of a file with the file suffix, which (typically) consists of a period, followed by one or more letters. Many standard utilities, such as compilers, use this to recognize the type of file they are dealing with. The <code><a href="/docs/linux/man/1-make/">make</a></code>(1) utility is driven by rules based on file suffix. </p>
<p> Following is a list of suffixes which are likely to be found on a Linux system. </p>
<table>
<tr VALIGN=top>
<td>Suffix</td>
<td>File type
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;&#8211;</i></td>
<td>backup file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.C</i></td>
<td>C++ source code, equivalent to <i>.cc</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.F</i></td>
<td>Fortran source with <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) directives
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>or file compressed using freeze
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.S</i></td>
<td>assembler source with <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) directives
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.Y</i></td>
<td>file compressed using yabba
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.Z</i></td>
<td>file compressed using <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.[0-9]+gf</i></td>
<td>TeX generic font files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.[0-9]+pk</i></td>
<td>TeX packed font files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.[1-9]</i></td>
<td>manual page for the corresponding section
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.[1-9][a-z]</i></td>
<td>manual page for section plus subsection
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.a</i></td>
<td>static object code library
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ad</i></td>
<td>X application default resource file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ada</i></td>
<td>Ada source (may be body, spec, or combination)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.adb</i></td>
<td>Ada body source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ads</i></td>
<td>Ada spec source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.afm</i></td>
<td>PostScript font metrics
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.al</i></td>
<td>Perl autoload file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.am</i></td>
<td><code><a href="/docs/linux/man/1-automake/">automake</a></code>(1) input file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.arc</i></td>
<td><code><a href="/docs/linux/man/1-arc/">arc</a></code>(1) archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.arj</i></td>
<td><code><a href="/docs/linux/man/1-arj/">arj</a></code>(1) archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.asc</i></td>
<td>PGP ASCII-armored data
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.asm</i></td>
<td>(GNU) assembler source file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.au</i></td>
<td>Audio sound file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.aux</i></td>
<td>LaTeX auxiliary file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.avi</i></td>
<td>(msvideo) movie
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.awk</i></td>
<td>AWK language program
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.b</i></td>
<td>LILO boot loader image
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bak</i></td>
<td>backup file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bash</i></td>
<td><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) shell script
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bb</i></td>
<td>basic block list data produced by
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>gcc -ftest-coverage
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bbg</i></td>
<td>basic block graph data produced by
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>gcc -ftest-coverage
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bbl</i></td>
<td>BibTeX output
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bdf</i></td>
<td>X font file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bib</i></td>
<td>TeX bibliographic database, BibTeX input
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bm</i></td>
<td>bitmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bmp</i></td>
<td>bitmap
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.bz2</i></td>
<td>file compressed using <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.c</i></td>
<td>C source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cat</i></td>
<td>message catalog files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cc</i></td>
<td>C++ source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cf</i></td>
<td>configuration file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cfg</i></td>
<td>configuration file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cgi</i></td>
<td>WWW content generating script or program
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cls</i></td>
<td>LaTeX Class definition
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.class</i></td>
<td>Java compiled byte-code
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.conf</i></td>
<td>configuration file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.config</i></td>
<td>configuration file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cpp</i></td>
<td>equivalent to <i>.cc</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.csh</i></td>
<td><code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) shell script
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.cxx</i></td>
<td>equivalent to <i>.cc</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.dat</i></td>
<td>data file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.deb</i></td>
<td>Debian software package
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.def</i></td>
<td>Modula-2 source for definition modules
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.def</i></td>
<td>other definition files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.desc</i></td>
<td>initial part of mail message unpacked with
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td><code><a href="/docs/linux/man/1-munpack/">munpack</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.diff</i></td>
<td>file differences (<code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) command output)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.dir</i></td>
<td>dbm data base directory file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.doc</i></td>
<td>documentation file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.dsc</i></td>
<td>Debian Source Control (source package)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.dtx</i></td>
<td>LaTeX package source file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.dvi</i></td>
<td>TeX&#8217;s device independent output
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.el</i></td>
<td>Emacs-Lisp source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.elc</i></td>
<td>compiled Emacs-Lisp source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.eps</i></td>
<td>encapsulated PostScript
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.exp</i></td>
<td>Expect source code
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.f</i></td>
<td>Fortran source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.f77</i></td>
<td>Fortran 77 source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.f90</i></td>
<td>Fortran 90 source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.fas</i></td>
<td>precompiled Common-Lisp
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.fi</i></td>
<td>Fortran include files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.fig</i></td>
<td>FIG image file (used by <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1))
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.fmt</i></td>
<td>TeX format file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.gif</i></td>
<td>Compuserve Graphics Image File format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.gmo</i></td>
<td>GNU format message catalog
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.gsf</i></td>
<td>Ghostscript fonts
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.gz</i></td>
<td>file compressed using <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.h</i></td>
<td>C or C++ header files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.help</i></td>
<td>help file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.hf</i></td>
<td>equivalent to <i>.help</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.hlp</i></td>
<td>equivalent to <i>.help</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.htm</i></td>
<td>poor man&#8217;s <i>.html</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.html</i></td>
<td>HTML document used with the World Wide Web
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.hqx</i></td>
<td>7-bit encoded Macintosh file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.i</i></td>
<td>C source after preprocessing
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.icon</i></td>
<td>bitmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.idx</i></td>
<td>reference or datum-index file for hypertext
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>or database system
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.image</i></td>
<td>bitmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.in</i></td>
<td>configuration template, especially for GNU Autoconf
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.info</i></td>
<td>files for the Emacs info browser
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.info-[0-9]+</i></td>
<td>split info files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ins</i></td>
<td>LaTeX package install file for docstrip
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.itcl</i></td>
<td>itcl source code;
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>itcl ([incr Tcl]) is an OO extension of tcl
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.java</i></td>
<td>a Java source file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.jpeg</i></td>
<td>Joint Photographic Experts Group format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.jpg</i></td>
<td>poor man&#8217;s <i>.jpeg</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.kmap</i></td>
<td><code><a href="/docs/linux/man/1-lyx/">lyx</a></code>(1) keymap
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.l</i></td>
<td>equivalent to <i>.lex</i> or <i>.lisp</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lex</i></td>
<td><code><a href="/docs/linux/man/1-lex/">lex</a></code>(1) or <code><a href="/docs/linux/man/1-flex/">flex</a></code>(1) files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lha</i></td>
<td>lharc archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lib</i></td>
<td>Common-Lisp library
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lisp</i></td>
<td>Lisp source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ln</i></td>
<td>files for use with <code><a href="/docs/linux/man/1-lint/">lint</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.log</i></td>
<td>log file, in particular produced by TeX
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lsm</i></td>
<td>Linux Software Map entry
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lsp</i></td>
<td>Common-Lisp source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.lzh</i></td>
<td>lharc archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.m</i></td>
<td>Objective-C source code
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.m4</i></td>
<td><code><a href="/docs/linux/man/1-m4/">m4</a></code>(1) source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mac</i></td>
<td>macro files for various programs
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.man</i></td>
<td>manual page (usually source rather than formatted)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.map</i></td>
<td>map files for various programs
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.me</i></td>
<td>Nroff source using the me macro package
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mf</i></td>
<td>Metafont (font generator for TeX) source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mgp</i></td>
<td>MagicPoint file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mm</i></td>
<td>sources for <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) in mm &#8211; format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mo</i></td>
<td>Message catalog binary file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mod</i></td>
<td>Modula-2 source for implementation modules
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mov</i></td>
<td>(quicktime) movie
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mp</i></td>
<td>Metapost source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mp2</i></td>
<td>MPEG Layer 2 (audio) file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mp3</i></td>
<td>MPEG Layer 3 (audio) file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.mpeg</i></td>
<td>movie file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.o</i></td>
<td>object file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.old</i></td>
<td>old or backup file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.orig</i></td>
<td>backup (original) version of a file, from <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.out</i></td>
<td>output file, often executable program (a.out)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.p</i></td>
<td>Pascal source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pag</i></td>
<td>dbm data base data file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.patch</i></td>
<td>file differences for <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pbm</i></td>
<td>portable bitmap format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pcf</i></td>
<td>X11 font files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pdf</i></td>
<td>Adobe Portable Data Format
</td>
</tr>
<tr VALIGN=top>
<td><i></i></td>
<td>(use Acrobat/<code>acroread</code> or <code>xpdf</code>)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.perl</i></td>
<td>Perl source (see .ph, .pl and .pm)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pfa</i></td>
<td>PostScript font definition files, ASCII format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pfb</i></td>
<td>PostScript font definition files, binary format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pgm</i></td>
<td>portable greymap format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pgp</i></td>
<td>PGP binary data
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ph</i></td>
<td>Perl header file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.php</i></td>
<td>PHP program file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.php3</i></td>
<td>PHP3 program file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pid</i></td>
<td>File to store daemon PID (e.g., crond.pid)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pl</i></td>
<td>TeX property list file or Perl library file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pm</i></td>
<td>Perl module
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.png</i></td>
<td>Portable Network Graphics file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.po</i></td>
<td>Message catalog source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pod</i></td>
<td><code><a href="/docs/linux/man/1-perldoc/">perldoc</a></code>(1) file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ppm</i></td>
<td>portable pixmap format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pr</i></td>
<td>bitmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.ps</i></td>
<td>PostScript file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.py</i></td>
<td>Python source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.pyc</i></td>
<td>compiled python
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.qt</i></td>
<td>quicktime movie
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.r</i></td>
<td>RATFOR source (obsolete)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.rej</i></td>
<td>patches that <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) couldn&#8217;t apply
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.rpm</i></td>
<td>RPM software package
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.rtf</i></td>
<td>Rich Text Format file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.rules</i></td>
<td>rules for something
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.s</i></td>
<td>assembler source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sa</i></td>
<td>stub libraries for a.out shared libraries
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sc</i></td>
<td><code><a href="/docs/linux/man/1-sc/">sc</a></code>(1) spreadsheet commands
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.scm</i></td>
<td>Scheme source code
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sed</i></td>
<td>sed source file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sgml</i></td>
<td>SGML source file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sh</i></td>
<td><code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) scripts
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.shar</i></td>
<td>archive created by the <code><a href="/docs/linux/man/1-shar/">shar</a></code>(1) utility
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.so</i></td>
<td>Shared library or dynamically loadable object
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sql</i></td>
<td>SQL source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sqml</i></td>
<td>SQML schema or query program
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sty</i></td>
<td>LaTeX style files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.sym</i></td>
<td>Modula-2 compiled definition modules
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tar</i></td>
<td>archive created by the <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) utility
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tar.Z</i></td>
<td><a href="/docs/linux/man/1-tar/">tar</a>(1) archive compressed with <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tar.bz2</i></td>
<td><a href="/docs/linux/man/1-tar/">tar</a>(1) archive compressed with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tar.gz</i></td>
<td><a href="/docs/linux/man/1-tar/">tar</a>(1) archive compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.taz</i></td>
<td><a href="/docs/linux/man/1-tar/">tar</a>(1) archive compressed with <code><a href="/docs/linux/man/1-compress/">compress</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tcl</i></td>
<td>tcl source code
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tex</i></td>
<td>TeX or LaTeX source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.texi</i></td>
<td>equivalent to <i>.texinfo</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.texinfo</i></td>
<td>Texinfo documentation source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.text</i></td>
<td>text file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tfm</i></td>
<td>TeX font metric file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tgz</i></td>
<td>tar archive compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tif</i></td>
<td>poor man&#8217;s <i>.tiff</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tiff</i></td>
<td>Tagged Image File Format
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tk</i></td>
<td>tcl/tk script
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tmp</i></td>
<td>temporary file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.tmpl</i></td>
<td>template files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.txt</i></td>
<td>equivalent to <i>.text</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.uu</i></td>
<td>equivalent to <i>.uue</i>
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.uue</i></td>
<td>binary file encoded with <code><a href="/docs/linux/man/1-uuencode/">uuencode</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.vf</i></td>
<td>TeX virtual font file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.vpl</i></td>
<td>TeX virtual property list file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.w</i></td>
<td>Silvio Levi&#8217;s CWEB
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.wav</i></td>
<td>wave sound file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.web</i></td>
<td>Donald Knuth&#8217;s WEB
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.wml</i></td>
<td>Source file for Web Meta Language
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xbm</i></td>
<td>X11 bitmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xcf</i></td>
<td>GIMP graphic
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xml</i></td>
<td>eXtended Markup Language file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xpm</i></td>
<td>X11 pixmap source
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xs</i></td>
<td>Perl xsub file produced by h2xs
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.xsl</i></td>
<td>XSL stylesheet
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.y</i></td>
<td><code><a href="/docs/linux/man/1-yacc/">yacc</a></code>(1) or <code><a href="/docs/linux/man/1-bison/">bison</a></code>(1) (parser generator) files
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.z</i></td>
<td>File compressed using <code><a href="/docs/linux/man/1-pack/">pack</a></code>(1) (or an old <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1))
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.zip</i></td>
<td><code><a href="/docs/linux/man/1-zip/">zip</a></code>(1) archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;.zoo</i></td>
<td><code><a href="/docs/linux/man/1-zoo/">zoo</a></code>(1) archive
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;~</i></td>
<td>Emacs or <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) backup file
</td>
</tr>
<tr VALIGN=top>
<td><i><br />
&nbsp;rc</i></td>
<td>startup (`run control&#8217;) file, e.g., <i>.newsrc</i>
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>General UNIX conventions.</p>
<h2>Bugs</h2>
<p>This list is not exhaustive.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-file/">file</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
