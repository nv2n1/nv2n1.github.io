---
title: "perlhpux(1)"
name: "perlhpux"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhpux/"
---

<h2 class="name">NAME</h2>
 

 perlhpux - Perl version 5 on Hewlett-Packard Unix (HP-UX) systems 

<h2>DESCRIPTION</h2>

 This document describes various features of <font SIZE="-1">HP</font>'s Unix operating system (HP-UX) that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.

<h3>Using perl as shipped with HP-UX</h3>

 Application release September 2001, HP-UX 11.00 is the first to ship with Perl. By the time it was perl-5.6.1 in /opt/perl. The first occurrence is on <font SIZE="-1">CD 5012-7954</font> and can be installed using 

 <pre>
  swinstall -s /cdrom perl
</pre> 

 assuming you have mounted that <font SIZE="-1">CD</font> on /cdrom. 

 That build was a portable hppa-1.1 multithread build that supports large files compiled with gcc-2.9-hppa-991112. 

 If you perform a new installation, then (a newer) Perl will be installed automatically. Pre-installed HP-UX systems now have more recent versions of Perl and the updated modules. 

 The official (threaded) builds from <font SIZE="-1">HP,</font> as they are shipped on the Application <font SIZE="-1">DVD/CD</font>'s are available on &lt;<a rel="nofollow" HREF="http://www.software.hp.com/portal/swdepot/displayProductInfo.do?productNumber=PERL">http://www.software.hp.com/portal/swdepot/displayProductInfo.do?productNumber=PERL</a>&gt; for both PA-RISC and <font SIZE="-1">IPF</font> (Itanium Processor Family). They are built with the <font SIZE="-1">HP</font> ANSI-C compiler. Up till 5.8.8 that was done by ActiveState. 

 To see what version is included on the <font SIZE="-1">DVD</font> (assumed here to be mounted on /cdrom), issue this command: 

 <pre>
  # swlist -s /cdrom perl
  # perl           D.5.8.8.B  5.8.8 Perl Programming Language
    perl.Perl5-32  D.5.8.8.B  32-bit 5.8.8 Perl Programming Language
                                           with Extensions
    perl.Perl5-64  D.5.8.8.B  64-bit 5.8.8 Perl Programming Language
                                           with Extensions
</pre> 

 To see what is installed on your system: 

 <pre><code>
#swlist - R perl
#perl E .5.8.8.J Perl Programming Language
#perl.Perl5 - 32 E .5.8.8.J 32 - bit Perl Programming Language
                                       with Extensions
    perl.Perl5-32.PERL-MAN  E.5.8.8.J  32-bit Perl Man Pages for IA
    perl.Perl5-32.PERL-RUN  E.5.8.8.J  32-bit Perl Binaries for IA
#perl.Perl5 - 64 E .5.8.8.J 64 - bit Perl Programming Language
                                       with Extensions
    perl.Perl5-64.PERL-MAN  E.5.8.8.J  64-bit Perl Man Pages for IA
    perl.Perl5-64.PERL-RUN  E.5.8.8.J  64-bit Perl Binaries for IA
</code></pre>

<h3>Using perl from <font SIZE="-1">HP</font>'s porting centre</h3>

 <font SIZE="-1">HP</font> porting centre tries to keep up with customer demand and release updates from the Open Source community. Having precompiled Perl binaries available is obvious, though ``up-to-date'' is something relative. At the moment of writing perl-5.10.1 and 5.28.0 were available. 

 The <font SIZE="-1">HP</font> porting centres are limited in what systems they are allowed to port to and they usually choose the two most recent <font SIZE="-1">OS</font> versions available. 

 <font SIZE="-1">HP</font> has asked the porting centre to move Open Source binaries from /opt to /usr/local, so binaries produced since the start of July 2002 are located in /usr/local. 

 One of <font SIZE="-1">HP</font> porting centres <font SIZE="-1">URL</font>'s is &lt;<a rel="nofollow" HREF="http://hpux.connect.org.uk/">http://hpux.connect.org.uk/</a>&gt; The port currently available is built with <font SIZE="-1">GNU</font> gcc. As porting modern <font SIZE="-1">GNU</font> gcc is extremely hard on HP-UX, they are stuck at version gcc-4.2.3.

<h3>Other prebuilt perl binaries</h3>

 To get more perl depots for the whole range of HP-UX, visit H.Merijn Brand's site at &lt;<a rel="nofollow" HREF="http://mirrors.develooper.com/hpux/#Perl">http://mirrors.develooper.com/hpux/#Perl</a>&gt;. Carefully read the notes to see if the available versions suit your needs.

<h3>Compiling Perl 5 on HP-UX</h3>

 When compiling Perl, you must use an <font SIZE="-1">ANSI C</font> compiler. The C compiler that ships with all HP-UX systems is a K&amp;R compiler that should only be used to build new kernels. 

 Perl can be compiled with either <font SIZE="-1">HP</font>'s <font SIZE="-1">ANSI C</font> compiler or with gcc. The former is recommended, as not only can it compile Perl with no difficulty, but also can take advantage of features listed later that require the use of <font SIZE="-1">HP</font> compiler-specific command-line flags. 

 If you decide to use gcc, make sure your installation is recent and complete, and be sure to read the Perl <font SIZE="-1">INSTALL</font> file for more gcc-specific details.

<h3>PA-RISC</h3>

 The last and final version of PA-RISC is 2.0, <font SIZE="-1">HP</font> no longer sells any system with these <font SIZE="-1">CPU</font>'s. 

 <font SIZE="-1">HP</font>'s <font SIZE="-1">HP9000</font> Unix systems run on <font SIZE="-1">HP</font>'s own Precision Architecture (PA-RISC) chip. HP-UX used to run on the Motorola <font SIZE="-1">MC68000</font> family of chips, but any machine with this chip in it is quite obsolete and this document will not attempt to address issues for compiling Perl on the Motorola chipset. Even though PA-RISC hardware is not sold anymore, a lot of machines still running on these <font SIZE="-1">CPU</font>'s can be found in the wild. 

 The last order date for <font SIZE="-1">HP 9000</font> systems was December 31, 2008. 

 <font SIZE="-1">HP</font> PA-RISC systems are usually referred to with model description ``<font SIZE="-1">HP 9000''.</font> The last <font SIZE="-1">CPU</font> in this series is the <font SIZE="-1">PA-8900.</font> Support for PA-RISC architectured machines officially ended as shown in the following table: 

 
PA - RISC End - of - Life Roadmap + -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -+ | HP9000 | Superdome | PA - 8700 | Spring 2011 |
    | 4 - 128 | | PA - 8800 / sx1000 | Summer 2012 |
    | cores | | PA - 8900 / sx1000 | 2014 |
    | | | PA - 8900 / sx2000 | 2015 |
    +-- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -+ | HP9000 | rp7410,
    rp8400 | PA - 8700 | Spring 2011 |
        | 2 - 32 | rp7420,
    rp8420 | PA - 8800 / sx1000 | 2012 |
        | cores | rp7440,
    rp8440 | PA - 8900 / sx1000 | Autumn 2013 |
        | | | PA - 8900 / sx2000 | 2015 |
        +-- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -+ | HP9000 | rp44x0 | PA - 8700 | Spring 2011 |
        | 1 - 8 | | PA - 8800 / rp44x0 | 2012 |
        | cores | | PA - 8900 / rp44x0 | 2014 |
        +-- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -+ | HP9000 | rp34x0 | PA - 8700 | Spring 2011 |
        | 1 - 4 | | PA - 8800 / rp34x0 | 2012 |
        | cores | | PA - 8900 / rp34x0 | 2014 |
        +-- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -+
 

 A complete list of models at the time the <font SIZE="-1">OS</font> was built is in the file /usr/sam/lib/mo/sched.models. The first column corresponds to the last part of the output of the ``model'' command. The second column is the PA-RISC version and the third column is the exact chip type used. (Start browsing at the bottom to prevent confusion ;-) 

 <pre>
  # model
  9000/800/L1000-44
  # grep L1000-44 /usr/sam/lib/mo/sched.models
  L1000-44        2.0     PA8500
</pre>

<h3>PA-RISC 1.0</h3>

 The original version of PA-RISC, <font SIZE="-1">HP</font> no longer sells any system with this chip. 

 The following systems contained PA-RISC 1.0 chips: 

 <pre>
  600, 635, 645, 808, 815, 822, 825, 832, 834, 835, 840, 842, 845, 850,
  852, 855, 860, 865, 870, 890
</pre>

<h3>PA-RISC 1.1</h3>

 An upgrade to the PA-RISC design, it shipped for many years in many different system. 

 The following systems contain with PA-RISC 1.1 chips: 

 <pre>
  705, 710, 712, 715, 720, 722, 725, 728, 730, 735, 742, 743, 744, 745,
  747, 750, 755, 770, 777, 778, 779, 800, 801, 803, 806, 807, 809, 811,
  813, 816, 817, 819, 821, 826, 827, 829, 831, 837, 839, 841, 847, 849,
  851, 856, 857, 859, 867, 869, 877, 887, 891, 892, 897, A180, A180C,
  B115, B120, B132L, B132L+, B160L, B180L, C100, C110, C115, C120,
  C160L, D200, D210, D220, D230, D250, D260, D310, D320, D330, D350,
  D360, D410, DX0, DX5, DXO, E25, E35, E45, E55, F10, F20, F30, G30,
  G40, G50, G60, G70, H20, H30, H40, H50, H60, H70, I30, I40, I50, I60,
  I70, J200, J210, J210XC, K100, K200, K210, K220, K230, K400, K410,
  K420, S700i, S715, S744, S760, T500, T520
</pre>

<h3>PA-RISC 2.0</h3>

 The most recent upgrade to the PA-RISC design, it added support for 64-bit integer data. 

 As of the date of this document's last update, the following systems contain PA-RISC 2.0 chips: 

 <pre>
  700, 780, 781, 782, 783, 785, 802, 804, 810, 820, 861, 871, 879, 889,
  893, 895, 896, 898, 899, A400, A500, B1000, B2000, C130, C140, C160,
  C180, C180+, C180-XP, C200+, C400+, C3000, C360, C3600, CB260, D270,
  D280, D370, D380, D390, D650, J220, J2240, J280, J282, J400, J410,
  J5000, J5500XM, J5600, J7000, J7600, K250, K260, K260-EG, K270, K360,
  K370, K380, K450, K460, K460-EG, K460-XP, K470, K570, K580, L1000,
  L2000, L3000, N4000, R380, R390, SD16000, SD32000, SD64000, T540,
  T600, V2000, V2200, V2250, V2500, V2600
</pre> 

 Just before <font SIZE="-1">HP</font> took over Compaq, some systems were renamed. the link that contained the explanation is dead, so here's a short summary: 

 <pre>
  HP 9000 A-Class servers, now renamed HP Server rp2400 series.
  HP 9000 L-Class servers, now renamed HP Server rp5400 series.
  HP 9000 N-Class servers, now renamed HP Server rp7400.
  rp2400, rp2405, rp2430, rp2450, rp2470, rp3410, rp3440, rp4410,
  rp4440, rp5400, rp5405, rp5430, rp5450, rp5470, rp7400, rp7405,
  rp7410, rp7420, rp7440, rp8400, rp8420, rp8440, Superdome
</pre> 

 The current naming convention is: 

 
  aadddd
  ||||`+- 00 - 99 relative capacity &amp; newness (upgrades, etc.)
  |||`--- unique number for each architecture to ensure different
  |||     systems do not have the same numbering across
  |||     architectures
  ||`---- 1 - 9 identifies family and/or relative positioning
  ||
  |`----- c = ia32 (cisc)
  |       p = pa-risc
  |       x = ia-64 (Itanium &amp; Itanium 2)
  |       h = housing
  `------ t = tower
          r = rack optimized
          s = super scalable
          b = blade
          sa = appliance


<h3>Portability Between PA-RISC Versions</h3>

 An executable compiled on a PA-RISC 2.0 platform will not execute on a PA-RISC 1.1 platform, even if they are running the same version of HP-UX. If you are building Perl on a PA-RISC 2.0 platform and want that Perl to also run on a PA-RISC 1.1, the compiler flags +DAportable and +DS32 should be used. 

 It is no longer possible to compile PA-RISC 1.0 executables on either the PA-RISC 1.1 or 2.0 platforms. The command-line flags are accepted, but the resulting executable will not run when transferred to a PA-RISC 1.0 system.

<h3>Itanium Processor Family (<font SIZE="-1">IPF</font>) and HP-UX</h3>

 HP-UX also runs on the newer Itanium processor. This requires the use of HP-UX version 11.23 (11i v2) or 11.31 (11i v3), and with the exception of a few differences detailed below and in later sections, Perl should compile with no problems. 

 Although PA-RISC binaries can run on Itanium systems, you should not attempt to use a PA-RISC version of Perl on an Itanium system. This is because shared libraries created on an Itanium system cannot be loaded while running a PA-RISC executable. 

 <font SIZE="-1">HP</font> Itanium 2 systems are usually referred to with model description ``<font SIZE="-1">HP</font> Integrity''.

<h3>Itanium, Itanium 2 &amp; Madison 6</h3>

 <font SIZE="-1">HP</font> also ships servers with the 128-bit Itanium processor(s). The cx26x0 is told to have Madison 6. As of the date of this document's last update, the following systems contain Itanium or Itanium 2 chips (this is likely to be out of date): 

 <pre>
  BL60p, BL860c, BL870c, BL890c, cx2600, cx2620, rx1600, rx1620, rx2600,
  rx2600hptc, rx2620, rx2660, rx2800, rx3600, rx4610, rx4640, rx5670,
  rx6600, rx7420, rx7620, rx7640, rx8420, rx8620, rx8640, rx9610,
  sx1000, sx2000
</pre> 

 To see all about your machine, type 

 <pre>
  # model
  ia64 hp server rx2600
  # /usr/contrib/bin/machinfo
</pre>

<h3>HP-UX versions</h3>

 Not all architectures (<font SIZE="-1">PA</font> = PA-RISC, <font SIZE="-1">IPF</font> = Itanium Processor Family) support all versions of HP-UX, here is a short list 

 
HP - UX version Kernel Architecture End - of - factory support-- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --10.20 32 bit PA 30 - Jun - 2003 11.00 32 / 64 PA 31 - Dec - 2006 11.11 11i v1 32 / 64 PA 31 - Dec - 2015 11.22 11i v2 64 IPF 30 - Apr - 2004 11.23 11i v2 64 PA &amp;IPF 31 - Dec - 2015 11.31 11i v3 64 PA &amp;IPF 31 - Dec - 2020(PA)31 - Dec - 2025(IPF)
 

 See for the full list of hardware/OS support and expected end-of-life &lt;<a rel="nofollow" HREF="https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf">https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf</a>&gt;

<h3>Building Dynamic Extensions on HP-UX</h3>

 HP-UX supports dynamically loadable libraries (shared libraries). Shared libraries end with the suffix .sl. On Itanium systems, they end with the suffix .so. 

 Shared libraries created on a platform using a particular PA-RISC version are not usable on platforms using an earlier PA-RISC version by default. However, this backwards compatibility may be enabled using the same +DAportable compiler flag (with the same PA-RISC 1.0 caveat mentioned above). 

 Shared libraries created on an Itanium platform cannot be loaded on a PA-RISC platform. Shared libraries created on a PA-RISC platform can only be loaded on an Itanium platform if it is a PA-RISC executable that is attempting to load the PA-RISC library. A PA-RISC shared library cannot be loaded into an Itanium executable nor vice-versa. 

 To create a shared library, the following steps must be performed: 

 <pre>
  1. Compile source modules with +z or +Z flag to create a .o module
     which contains Position-Independent Code (PIC).  The linker will
     tell you in the next step if +Z was needed.
     (For gcc, the appropriate flag is -fpic or -fPIC.)
  2. Link the shared library using the -b flag.  If the code calls
     any functions in other system libraries (e.g., libm), it must
     be included on this line.
</pre> 

 (Note that these steps are usually handled automatically by the extension's Makefile). 

 If these dependent libraries are not listed at shared library creation time, you will get fatal ``Unresolved symbol'' errors at run time when the library is loaded. 

 You may create a shared library that refers to another library, which may be either an archive library or a shared library. If this second library is a shared library, this is called a ``dependent library''. The dependent library's name is recorded in the main shared library, but it is not linked into the shared library. Instead, it is loaded when the main shared library is loaded. This can cause problems if you build an extension on one system and move it to another system where the libraries may not be located in the same place as on the first system. 

 If the referred library is an archive library, then it is treated as a simple collection of .o modules (all of which must contain <font SIZE="-1">PIC</font>). These modules are then linked into the shared library. 

 Note that it is okay to create a library which contains a dependent library that is already linked into perl. 

 Some extensions, like DB_File and Compress::Zlib use/require prebuilt libraries for the perl extensions/modules to work. If these libraries are built using the default configuration, it might happen that you run into an error like ``invalid loader fixup'' during load phase. <font SIZE="-1">HP</font> is aware of this problem. Search the HP-UX cxx-dev forums for discussions about the subject. The short answer is that <b>everything</b> (all libraries, everything) must be compiled with <tt>&quot;+z&quot;</tt> or <tt>&quot;+Z&quot;</tt> to be <font SIZE="-1">PIC</font> (position independent code). (For gcc, that would be <tt>&quot;-fpic&quot;</tt> or <tt>&quot;-fPIC&quot;</tt>). In HP-UX 11.00 or newer the linker error message should tell the name of the offending object file. 

 A more general approach is to intervene manually, as with an example for the DB_File module, which requires SleepyCat's libdb.sl: 

 
#cd... / db - 3.2.9 / build_unix
#vi Makefile
... add + Z to all cflags to create shared objects
              CFLAGS = -c $(CPPFLAGS) + Z - Ae + O2 + Onolimit - I / usr / local / include - I / usr / include / X11R6 CXXFLAGS = -c $(CPPFLAGS) + Z - Ae + O2 + Onolimit - I / usr / local / include - I / usr / include / X11R6
#make clean
#make
#mkdir tmp
#cd tmp
#ar x../ libdb.a
#ld - b - o libdb - 3.2.sl *.o
#mv libdb - 3.2.sl / usr / local / lib
#rm *.o
#cd / usr / local / lib
#rm - f libdb.sl
#ln - s libdb - 3.2.sl libdb.sl
#cd... / DB_File - 1.76
#make distclean
#perl Makefile.PL
#make
#make test
#make install
 

 As of db-4.2.x it is no longer needed to do this by hand. Sleepycat has changed the configuration process to add +z on HP-UX automatically. 

 <pre>
  # cd .../db-4.2.25/build_unix
  # env CFLAGS=+DD64 LDFLAGS=+DD64 ../dist/configure
</pre> 

 should work to generate 64bit shared libraries for HP-UX 11.00 and 11i. 

 It is no longer possible to link PA-RISC 1.0 shared libraries (even though the command-line flags are still present). 

 PA-RISC and Itanium object files are not interchangeable. Although you may be able to use ar to create an archive library of PA-RISC object files on an Itanium system, you cannot link against it using an Itanium link editor.

<h3>The <font SIZE="-1">HP ANSI C</font> Compiler</h3>

 When using this compiler to build Perl, you should make sure that the flag -Aa is added to the cpprun and cppstdin variables in the config.sh file (though see the section on 64-bit perl below). If you are using a recent version of the Perl distribution, these flags are set automatically. 

 Even though HP-UX 10.20 and 11.00 are not actively maintained by <font SIZE="-1">HP</font> anymore, updates for the <font SIZE="-1">HP ANSI C</font> compiler are still available from time to time, and it might be advisable to see if updates are applicable. At the moment of writing, the latests available patches for 11.00 that should be applied are <font SIZE="-1">PHSS_35098, PHSS_35175, PHSS_35100, PHSS_33036,</font> and <font SIZE="-1">PHSS_33902</font>). If you have a <font SIZE="-1">SUM</font> account, you can use it to search for updates/patches. Enter ``<font SIZE="-1">ANSI''</font> as keyword.

<h3>The <font SIZE="-1">GNU C</font> Compiler</h3>

 When you are going to use the <font SIZE="-1">GNU C</font> compiler (gcc), and you don't have gcc yet, you can either build it yourself (if you feel masochistic enough) from the sources (available from e.g. &lt;<a rel="nofollow" HREF="http://gcc.gnu.org/mirrors.html">http://gcc.gnu.org/mirrors.html</a>&gt;) or fetch a prebuilt binary from the <font SIZE="-1">HP</font> porting center at &lt;<a rel="nofollow" HREF="http://hpux.connect.org.uk/hppd/cgi-bin/search?term=gcc">http://hpux.connect.org.uk/hppd/cgi-bin/search?term=gcc</a>&amp;Search=Search&gt; or from the <font SIZE="-1">DSPP</font> (you need to be a member) at &lt;<a rel="nofollow" HREF="http://h21007.www2.hp.com/portal/site/dspp/menuitem.863c3e4cbcdc3f3515b49c108973a801?ciid=2a08725cc2f02110725cc2f02110275d6e10RCRD">http://h21007.www2.hp.com/portal/site/dspp/menuitem.863c3e4cbcdc3f3515b49c108973a801?ciid=2a08725cc2f02110725cc2f02110275d6e10RCRD</a>&amp;jumpid=reg_r1002_usen_c-001_title_r0001&gt; (Browse through the list, because there are often multiple versions of the same package available). 

 Most mentioned distributions are depots. H.Merijn Brand has made prebuilt gcc binaries available on &lt;<a rel="nofollow" HREF="http://mirrors.develooper.com/hpux/">http://mirrors.develooper.com/hpux/</a>&gt; and/or &lt;<a rel="nofollow" HREF="http://www.cmve.net/~merijn/">http://www.cmve.net/~merijn/</a>&gt; for HP-UX 10.20 (only 32bit), HP-UX 11.00, HP-UX 11.11 (HP-UX 11i v1), and HP-UX 11.23 (HP-UX 11i v2 PA-RISC) in both 32- and 64-bit versions. For HP-UX 11.23 <font SIZE="-1">IPF</font> and HP-UX 11.31 <font SIZE="-1">IPF</font> depots are available too. The <font SIZE="-1">IPF</font> versions do not need two versions of <font SIZE="-1">GNU</font> gcc. 

 On PA-RISC you need a different compiler for 32-bit applications and for 64-bit applications. On PA-RISC, 32-bit objects and 64-bit objects do not mix. Period. There is no different behaviour for <font SIZE="-1">HP</font> C-ANSI-C or <font SIZE="-1">GNU</font> gcc. So if you require your perl binary to use 64-bit libraries, like Oracle-64bit, you <font SIZE="-1">MUST</font> build a 64-bit perl. 

 Building a 64-bit capable gcc on PA-RISC from source is possible only when you have the <font SIZE="-1">HP C-ANSI C</font> compiler or an already working 64-bit binary of gcc available. Best performance for perl is achieved with <font SIZE="-1">HP</font>'s native compiler.

<h3>Using Large Files with Perl on HP-UX</h3>

 Beginning with HP-UX version 10.20, files larger than 2GB (2^31 bytes) may be created and manipulated. Three separate methods of doing this are available. Of these methods, the best method for Perl is to compile using the -Duselargefiles flag to Configure. This causes Perl to be compiled using structures and functions in which these are 64 bits wide, rather than 32 bits wide. (Note that this will only work with <font SIZE="-1">HP</font>'s <font SIZE="-1">ANSI C</font> compiler. If you want to compile Perl using gcc, you will have to get a version of the compiler that supports 64-bit operations. See above for where to find it.) 

 There are some drawbacks to this approach. One is that any extension which calls any file-manipulating C function will need to be recompiled (just follow the usual ``perl Makefile.PL; make; make test; make install'' procedure). 

 The list of functions that will need to recompiled is: 
&nbsp;<wbr>&nbsp;creat,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fgetpos,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fopen, 
&nbsp;<wbr>&nbsp;freopen,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsetpos,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fstat, 
&nbsp;<wbr>&nbsp;fstatvfs,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fstatvfsdev,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ftruncate, 
&nbsp;<wbr>&nbsp;ftw,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lockf,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lseek, 
&nbsp;<wbr>&nbsp;lstat,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mmap,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nftw, 
&nbsp;<wbr>&nbsp;open,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prealloc,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stat, 
&nbsp;<wbr>&nbsp;statvfs,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;statvfsdev,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tmpfile, 
&nbsp;<wbr>&nbsp;truncate,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getrlimit,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setrlimit 

 Another drawback is only valid for Perl versions before 5.6.0. This drawback is that the seek and tell functions (both the builtin version and <font SIZE="-1">POSIX</font> module version) will not perform correctly. 

 It is strongly recommended that you use this flag when you run Configure. If you do not do this, but later answer the question about large files when Configure asks you, you may get a configuration that cannot be compiled, or that does not function as expected.

<h3>Threaded Perl on HP-UX</h3>

 It is possible to compile a version of threaded Perl on any version of HP-UX before 10.30, but it is strongly suggested that you be running on HP-UX 11.00 at least. 

 To compile Perl with threads, add -Dusethreads to the arguments of Configure. Verify that the -D_POSIX_C_SOURCE=199506L compiler flag is automatically added to the list of flags. Also make sure that -lpthread is listed before -lc in the list of libraries to link Perl with. The hints provided for HP-UX during Configure will try very hard to get this right for you. 

 HP-UX versions before 10.30 require a separate installation of a <font SIZE="-1">POSIX</font> threads library package. Two examples are the <font SIZE="-1">HP DCE</font> package, available on ``HP-UX Hardware Extensions 3.0, Install and Core <font SIZE="-1">OS,</font> Release 10.20, April 1999 (B3920-13941)'' or the Freely available <font SIZE="-1">PTH</font> package, available on H.Merijn's site (&lt;<a rel="nofollow" HREF="http://mirrors.develooper.com/hpux/">http://mirrors.develooper.com/hpux/</a>&gt;). The use of <font SIZE="-1">PTH</font> will be unsupported in perl-5.12 and up and is rather buggy in 5.11.x. 

 If you are going to use the <font SIZE="-1">HP DCE</font> package, the library used for threading is /usr/lib/libcma.sl, but there have been multiple updates of that library over time. Perl will build with the first version, but it will not pass the test suite. Older Oracle versions might be a compelling reason not to update that library, otherwise please find a newer version in one of the following patches: <font SIZE="-1">PHSS_19739, PHSS_20608,</font> or <font SIZE="-1">PHSS_23672</font> 

 reformatted output: 

 <pre>
  d3:/usr/lib 106 &gt; what libcma-*.1
  libcma-00000.1:
     HP DCE/9000 1.5               Module: libcma.sl (Export)
                                   Date: Apr 29 1996 22:11:24
  libcma-19739.1:
     HP DCE/9000 1.5 PHSS_19739-40 Module: libcma.sl (Export)
                                   Date: Sep  4 1999 01:59:07
  libcma-20608.1:
     HP DCE/9000 1.5 PHSS_20608    Module: libcma.1 (Export)
                                   Date: Dec  8 1999 18:41:23
  libcma-23672.1:
     HP DCE/9000 1.5 PHSS_23672    Module: libcma.1 (Export)
                                   Date: Apr  9 2001 10:01:06
  d3:/usr/lib 107 &gt;
</pre> 

 If you choose for the <font SIZE="-1">PTH</font> package, use swinstall to install pth in the default location (/opt/pth), and then make symbolic links to the libraries from /usr/lib 

 <pre>
  # cd /usr/lib
  # ln -s /opt/pth/lib/libpth* .
</pre> 

 For building perl to support Oracle, it needs to be linked with libcl and libpthread. So even if your perl is an unthreaded build, these libraries might be required. See ``Oracle on HP-UX'' below.

<h3>64-bit Perl on HP-UX</h3>

 Beginning with HP-UX 11.00, programs compiled under HP-UX can take advantage of the <font SIZE="-1">LP64</font> programming environment (<font SIZE="-1">LP64</font> means Longs and Pointers are 64 bits wide), in which scalar variables will be able to hold numbers larger than 2^32 with complete precision. Perl has proven to be consistent and reliable in 64bit mode since 5.8.1 on all HP-UX 11.xx. 

 As of the date of this document, Perl is fully 64-bit compliant on HP-UX 11.00 and up for both cc- and gcc builds. If you are about to build a 64-bit perl with <font SIZE="-1">GNU</font> gcc, please read the gcc section carefully. 

 Should a user have the need for compiling Perl in the <font SIZE="-1">LP64</font> environment, use the -Duse64bitall flag to Configure. This will force Perl to be compiled in a pure <font SIZE="-1">LP64</font> environment (with the +DD64 flag for <font SIZE="-1">HP</font> C-ANSI-C, with no additional options for <font SIZE="-1">GNU</font> gcc 64-bit on PA-RISC, and with -mlp64 for <font SIZE="-1">GNU</font> gcc on Itanium). If you want to compile Perl using gcc, you will have to get a version of the compiler that supports 64-bit operations.) 

 You can also use the -Duse64bitint flag to Configure. Although there are some minor differences between compiling Perl with this flag versus the -Duse64bitall flag, they should not be noticeable from a Perl user's perspective. When configuring -Duse64bitint using a 64bit gcc on a pa-risc architecture, -Duse64bitint is silently promoted to -Duse64bitall. 

 In both cases, it is strongly recommended that you use these flags when you run Configure. If you do not use do this, but later answer the questions about 64-bit numbers when Configure asks you, you may get a configuration that cannot be compiled, or that does not function as expected.

<h3>Oracle on HP-UX</h3>

 Using perl to connect to Oracle databases through <font SIZE="-1">DBI</font> and DBD::Oracle has caused a lot of people many headaches. Read <font SIZE="-1">README</font>.hpux in the DBD::Oracle for much more information. The reason to mention it here is that Oracle requires a perl built with libcl and libpthread, the latter even when perl is build without threads. Building perl using all defaults, but still enabling to build DBD::Oracle later on can be achieved using 

 <pre>
  Configure -A prepend:libswanted='cl pthread ' ...
</pre> 

 Do not forget the space before the trailing quote. 

 Also note that this does not (yet) work with all configurations, it is known to fail with 64-bit versions of <font SIZE="-1">GCC.</font>

<h3><font SIZE="-1">GDBM</font> and Threads on HP-UX</h3>

 If you attempt to compile Perl with (<font SIZE="-1">POSIX</font>) threads on an 11.X system and also link in the <font SIZE="-1">GDBM</font> library, then Perl will immediately core dump when it starts up. The only workaround at this point is to relink the <font SIZE="-1">GDBM</font> library under 11.X, then relink it into Perl. 

 the error might show something like: 

 Pthread internal error: message: _<b>_libc_reinit()</b> failed, file: ../pthreads/pthread.c, line: 1096 Return Pointer is 0xc082bf33 sh: 5345 Quit(coredump) 

 and Configure will give up.

<h3><font SIZE="-1">NFS</font> filesystems and <b><a HREF="/docs/linux/man/2-utime/">utime</a></b>(2) on HP-UX</h3>

 If you are compiling Perl on a remotely-mounted <font SIZE="-1">NFS</font> filesystem, the test io/fs.t may fail on test #18. This appears to be a bug in HP-UX and no fix is currently available.

<h3>HP-UX Kernel Parameters (maxdsiz) for Compiling Perl</h3>

 By default, HP-UX comes configured with a maximum data segment size of 64MB. This is too small to correctly compile Perl with the maximum optimization levels. You can increase the size of the maxdsiz kernel parameter through the use of <font SIZE="-1">SAM.</font> 

 When using the <font SIZE="-1">GUI</font> version of <font SIZE="-1">SAM,</font> click on the Kernel Configuration icon, then the Configurable Parameters icon. Scroll down and select the maxdsiz line. From the Actions menu, select the Modify Configurable Parameter item. Insert the new formula into the Formula/Value box. Then follow the instructions to rebuild your kernel and reboot your system. 

 In general, a value of 256MB (or ``256*1024*1024'') is sufficient for Perl to compile at maximum optimization.

<h2>nss_delete core dump from op/pwent or op/grent</h2>

 You may get a bus error core dump from the op/pwent or op/grent tests. If compiled with -g you will see a stack trace much like the following: 

 <pre>
  #0  0xc004216c in  () from /usr/lib/libc.2
  #1  0xc00d7550 in __nss_src_state_destr () from /usr/lib/libc.2
  #2  0xc00d7768 in __nss_src_state_destr () from /usr/lib/libc.2
  #3  0xc00d78a8 in nss_delete () from /usr/lib/libc.2
  #4  0xc01126d8 in endpwent () from /usr/lib/libc.2
  #5  0xd1950 in Perl_pp_epwent () from ./perl
  #6  0x94d3c in Perl_runops_standard () from ./perl
  #7  0x23728 in S_run_body () from ./perl
  #8  0x23428 in perl_run () from ./perl
  #9  0x2005c in main () from ./perl
</pre> 

 The key here is the <tt>&quot;nss_delete&quot;</tt> call. One workaround for this bug seems to be to create add to the file <i>/etc/nsswitch.conf</i> (at least) the following lines 

 <pre>
  group: files
  passwd: files
</pre> 

 Whether you are using <font SIZE="-1">NIS</font> does not matter. Amazingly enough, the same bug also affects Solaris.

<h2>error: pasting ) and l does not give a valid preprocessing token</h2>

 There seems to be a broken system header file in HP-UX 11.00 that breaks perl building in 32bit mode with <font SIZE="-1">GNU</font> gcc-4.x causing this error. The same file for HP-UX 11.11 (even though the file is older) does not show this failure, and has the correct definition, so the best fix is to patch the header to match: 

 <pre><code>
-- - / usr / include / inttypes.h 2001 - 04 - 20 18 : 42 : 14 + 0200 ++ + / usr / include / inttypes.h 2000 - 11 - 14 09 : 00 : 00 + 0200 @ @-72, 7 + 72, 7 @ @
#define UINT32_C(__c) __CONCAT_U__(__c)
#else /* __LP64 */
#define INT32_C(__c) __CONCAT__(__c, l)
                                                                                                                                                              -#define UINT32_C(__c) __CONCAT__(__CONCAT_U__(__c), l) +
                                                                                                                                                              #define UINT32_C(__c) __CONCAT__(__c, ul)
#endif /* __LP64 */
#define INT64_C(__c) __CONCAT_L__(__c, l)
</code></pre>

<h2>Redeclaration of sendpath with a different storage class specifier</h2>

 The following compilation warnings may happen in HP-UX releases earlier than 11.31 but are harmless: 

 <pre>
 cc: &quot;/usr/include/sys/socket.h&quot;, line 535: warning 562:
    Redeclaration of &quot;sendfile&quot; with a different storage class
    specifier: &quot;sendfile&quot; will have internal linkage.
 cc: &quot;/usr/include/sys/socket.h&quot;, line 536: warning 562:
    Redeclaration of &quot;sendpath&quot; with a different storage class
    specifier: &quot;sendpath&quot; will have internal linkage.
</pre> 

 They seem to be caused by broken system header files, and also other open source projects are seeing them. The following HP-UX patches should make the warnings go away: 

 <pre>
  CR JAGae12001: PHNE_27063
  Warning 562 on sys/socket.h due to redeclaration of prototypes
  CR JAGae16787:
  Warning 562 from socket.h sendpath/sendfile -D_FILEFFSET_BITS=64
  CR JAGae73470 (11.23)
  ER: Compiling socket.h with cc -D_FILEFFSET_BITS=64 warning 267/562
</pre>

<h2>Miscellaneous</h2>

 HP-UX 11 Y2K patch ``Y2K-1100 B.11.00.B0125 HP-UX Core <font SIZE="-1">OS</font> Year 2000 Patch Bundle'' has been reported to break the io/fs test #18 which tests whether <b>utime()</b> can change timestamps. The Y2K patch seems to break <b>utime()</b> so that over <font SIZE="-1">NFS</font> the timestamps do not get changed (on local filesystems <b>utime()</b> still works). This has probably been fixed on your system by now.

<h2>AUTHOR</h2>

 H.Merijn Brand &lt;h.m.brand [at] xs4all.nl&gt; Jeff Okamoto &lt;okamoto [at] corp.hp.com&gt; 

 With much assistance regarding shared libraries from Marc Sabatella. 

<h2>Index</h2>



<dt><a HREF="#lbAZ">nss_delete core dump from op/pwent or op/grent</a>
<dd>
<dt><a HREF="#lbBA">error: pasting ) and l does not give a valid preprocessing token</a>
<dd>
<dt><a HREF="#lbBB">Redeclaration of sendpath with a different storage class specifier</a>
<dd>
<dt><a HREF="#lbBC">Miscellaneous</a>
<dd>
<dt><a HREF="#lbBD">AUTHOR</a>
<dd></dl>
