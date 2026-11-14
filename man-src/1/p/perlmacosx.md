---
title: "perlmacosx(1)"
name: "perlmacosx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlmacosx/"
---

<h2 class="name">NAME</h2>
 

 perlmacosx - Perl under Mac OS X 

<h2>SYNOPSIS</h2>

 This document briefly describes Perl under Mac <font SIZE="-1">OS X.</font> 

 <pre>
  curl -O <a rel="nofollow" HREF="http://www.cpan.org/src/perl-5.30.0.tar.gz">http://www.cpan.org/src/perl-5.30.0.tar.gz</a>
  tar -xzf perl-5.30.0.tar.gz
  cd perl-5.30.0
  ./Configure -des -Dprefix=/usr/local/
  make
  make test
  sudo make install
</pre>

<h2>DESCRIPTION</h2>

 The latest Perl release (5.30.0 as of this writing) builds without changes under all versions of Mac <font SIZE="-1">OS X</font> from 10.3 ``Panther'' onwards. 

 In order to build your own version of Perl you will need 'make', which is part of Apple's developer tools - also known as Xcode. From Mac <font SIZE="-1">OS X 10.7</font> ``Lion'' onwards, it can be downloaded separately as the 'Command Line Tools' bundle directly from &lt;<a rel="nofollow" HREF="https://developer.apple.com/downloads/">https://developer.apple.com/downloads/</a>&gt; (you will need a free account to log in), or as a part of the Xcode suite, freely available at the App Store. Xcode is a pretty big app, so unless you already have it or really want it, you are advised to get the 'Command Line Tools' bundle separately from the link above. If you want to do it from within Xcode, go to Xcode -&gt; Preferences -&gt; Downloads and select the 'Command Line Tools' option. 

 Between Mac <font SIZE="-1">OS X 10.3</font> ``Panther'' and 10.6 ``Snow Leopard'', the 'Command Line Tools' bundle was called 'unix tools', and was usually supplied with Mac <font SIZE="-1">OS</font> install DVDs. 

 Earlier Mac <font SIZE="-1">OS X</font> releases (10.2 ``Jaguar'' and older) did not include a completely thread-safe libc, so threading is not fully supported. Also, earlier releases included a buggy libdb, so some of the DB_File tests are known to fail on those releases.

<h3>Installation Prefix</h3>

 The default installation location for this release uses the traditional <font SIZE="-1">UNIX</font> directory layout under /usr/local. This is the recommended location for most users, and will leave the Apple-supplied Perl and its modules undisturbed. 

 Using an installation prefix of '/usr' will result in a directory layout that mirrors that of Apple's default Perl, with core modules stored in '/System/Library/Perl/${version}', <font SIZE="-1">CPAN</font> modules stored in '/Library/Perl/${version}', and the addition of '/Network/Library/Perl/${version}' to <tt>@INC</tt> for modules that are stored on a file server and used by many Macs.

<h3><font SIZE="-1">SDK</font> support</h3>

 First, export the path to the <font SIZE="-1">SDK</font> into the build environment: 

 <pre>
 export SDK=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.8.sdk
</pre> 

 Please make sure the <font SIZE="-1">SDK</font> version (i.e. the numbers right before '.sdk') matches your system's (in this case, Mac <font SIZE="-1">OS X 10.8</font> ``Mountain Lion''), as it is possible to have more than one <font SIZE="-1">SDK</font> installed. Also make sure the path exists in your system, and if it doesn't please make sure the <font SIZE="-1">SDK</font> is properly installed, as it should come with the 'Command Line Tools' bundle mentioned above. Finally, if you have an older Mac <font SIZE="-1">OS X</font> (10.6 ``Snow Leopard'' and below) running Xcode 4.2 or lower, the <font SIZE="-1">SDK</font> path might be something like <tt>'/Developer/SDKs/MacOSX10.3.9.sdk'</tt>. 

 You can use the <font SIZE="-1">SDK</font> by exporting some additions to Perl's 'ccflags' and '..flags' config variables: 

 <pre>
    ./Configure -Accflags=&quot;-nostdinc -B$SDK/usr/include/gcc \
                           -B$SDK/usr/lib/gcc -isystem$SDK/usr/include \
                           -F$SDK/System/Library/Frameworks&quot; \
                -Aldflags=&quot;-Wl,-syslibroot,$SDK&quot; \
                -de
</pre>

<h3>Universal Binary support</h3>

 Note: From Mac <font SIZE="-1">OS X 10.6</font> ``Snow Leopard'' onwards, Apple only supports Intel-based hardware. This means you can safely skip this section unless you have an older Apple computer running on ppc or wish to create a perl binary with backwards compatibility. 

 You can compile perl as a universal binary (built for both ppc and intel). In Mac <font SIZE="-1">OS X 10.4</font> ``Tiger'', you must export the 'u' variant of the <font SIZE="-1">SDK:</font> 

 <pre>
    export SDK=/Developer/SDKs/MacOSX10.4u.sdk
</pre> 

 Mac <font SIZE="-1">OS X 10.5</font> ``Leopard'' and above do not require the 'u' variant. 

 In addition to the compiler flags used to select the <font SIZE="-1">SDK,</font> also add the flags for creating a universal binary: 

 <pre>
 ./Configure -Accflags=&quot;-arch i686 -arch ppc -nostdinc               \
                         -B$SDK/usr/include/gcc                      \
                        -B$SDK/usr/lib/gcc -isystem$SDK/usr/include  \
                        -F$SDK/System/Library/Frameworks&quot;            \
             -Aldflags=&quot;-arch i686 -arch ppc -Wl,-syslibroot,$SDK&quot;   \
             -de
</pre> 

 Keep in mind that these compiler and linker settings will also be used when building <font SIZE="-1">CPAN</font> modules. For <font SIZE="-1">XS</font> modules to be compiled as a universal binary, any libraries it links to must also be universal binaries. The system libraries that Apple includes with the 10.4u <font SIZE="-1">SDK</font> are all universal, but user-installed libraries may need to be re-installed as universal binaries.

<h3>64-bit <font SIZE="-1">PPC</font> support</h3>

 Follow the instructions in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> to build perl with support for 64-bit integers (<tt>&quot;use64bitint&quot;</tt>) or both 64-bit integers and 64-bit addressing (<tt>&quot;use64bitall&quot;</tt>). In the latter case, the resulting binary will run only on G5-based hosts. 

 Support for 64-bit addressing is experimental: some aspects of Perl may be omitted or buggy. Note the messages output by <i>Configure</i> for further information. Please use <tt>&quot;perlbug&quot;</tt> to submit a problem report in the event that you encounter difficulties. 

 When building 64-bit modules, it is your responsibility to ensure that linked external libraries and frameworks provide 64-bit support: if they do not, module building may appear to succeed, but attempts to use the module will result in run-time dynamic linking errors, and subsequent test failures. You can use <tt>&quot;file&quot;</tt> to discover the architectures supported by a library: 

 <pre>
    $ file libgdbm.3.0.0.dylib 
    libgdbm.3.0.0.dylib: Mach-O fat file with 2 architectures
    libgdbm.3.0.0.dylib (for architecture ppc):      Mach-O dynamically linked shared library ppc
    libgdbm.3.0.0.dylib (for architecture ppc64):    Mach-O 64-bit dynamically linked shared library ppc64
</pre> 

 Note that this issue precludes the building of many Macintosh-specific <font SIZE="-1">CPAN</font> modules (<tt>&quot;Mac::*&quot;</tt>), as the required Apple frameworks do not provide <font SIZE="-1">PPC64</font> support. Similarly, downloads from Fink or Darwinports are unlikely to provide 64-bit support; the libraries must be rebuilt from source with the appropriate compiler and linker flags. For further information, see Apple's <i>64-Bit Transition Guide</i> at &lt;<a rel="nofollow" HREF="http://developer.apple.com/documentation/Darwin/Conceptual/64bitPorting/index.html">http://developer.apple.com/documentation/Darwin/Conceptual/64bitPorting/index.html</a>&gt;.

<h3>libperl and Prebinding</h3>

 Mac <font SIZE="-1">OS X</font> ships with a dynamically-loaded libperl, but the default for this release is to compile a static libperl. The reason for this is pre-binding. Dynamic libraries can be pre-bound to a specific address in memory in order to decrease load time. To do this, one needs to be aware of the location and size of all previously-loaded libraries. Apple collects this information as part of their overall <font SIZE="-1">OS</font> build process, and thus has easy access to it when building Perl, but ordinary users would need to go to a great deal of effort to obtain the information needed for pre-binding. 

 You can override the default and build a shared libperl if you wish (Configure ... -Duseshrplib). 

 With Mac <font SIZE="-1">OS X 10.4</font> ``Tiger'' and newer, there is almost no performance penalty for non-prebound libraries. Earlier releases will suffer a greater load time than either the static library, or Apple's pre-bound dynamic library.

<h3>Updating Apple's Perl</h3>

 In a word - don't, at least not without a *very* good reason. Your scripts can just as easily begin with ``#!/usr/local/bin/perl'' as with ``#!/usr/bin/perl''. Scripts supplied by Apple and other third parties as part of installation packages and such have generally only been tested with the /usr/bin/perl that's installed by Apple. 

 If you find that you do need to update the system Perl, one issue worth keeping in mind is the question of static vs. dynamic libraries. If you upgrade using the default static libperl, you will find that the dynamic libperl supplied by Apple will not be deleted. If both libraries are present when an application that links against libperl is built, ld will link against the dynamic library by default. So, if you need to replace Apple's dynamic libperl with a static libperl, you need to be sure to delete the older dynamic library after you've installed the update.

<h3>Known problems</h3>

 If you have installed extra libraries such as <font SIZE="-1">GDBM</font> through Fink (in other words, you have libraries under <i>/sw/lib</i>), or libdlcompat to <i>/usr/local/lib</i>, you may need to be extra careful when running Configure to not to confuse Configure and Perl about which libraries to use. Being confused will show up for example as ``dyld'' errors about symbol problems, for example during ``make test''. The safest bet is to run Configure as 

 <pre>
    Configure ... -Uloclibpth -Dlibpth=/usr/lib
</pre> 

 to make Configure look only into the system libraries. If you have some extra library directories that you really want to use (such as newer Berkeley <font SIZE="-1">DB</font> libraries in pre-Panther systems), add those to the libpth: 

 <pre>
    Configure ... -Uloclibpth -Dlibpth='/usr/lib /opt/lib'
</pre> 

 The default of building Perl statically may cause problems with complex applications like Tk: in that case consider building shared Perl 

 <pre>
    Configure ... -Duseshrplib
</pre> 

 but remember that there's a startup cost to pay in that case (see above ``libperl and Prebinding''). 

 Starting with Tiger (Mac <font SIZE="-1">OS X 10.4</font>), Apple shipped broken locale files for the eu_ES locale (Basque-Spain). In previous releases of Perl, this resulted in failures in the <i>lib/locale</i> test. These failures have been suppressed in the current release of Perl by making the test ignore the broken locale. If you need to use the eu_ES locale, you should contact Apple support.

<h3>Cocoa</h3>

 There are two ways to use Cocoa from Perl. Apple's PerlObjCBridge module, included with Mac <font SIZE="-1">OS X,</font> can be used by standalone scripts to access Foundation (i.e. non-GUI) classes and objects. 

 An alternative is CamelBones, a framework that allows access to both Foundation and AppKit classes and objects, so that full <font SIZE="-1">GUI</font> applications can be built in Perl. CamelBones can be found on SourceForge, at &lt;<a rel="nofollow" HREF="http://www.sourceforge.net/projects/camelbones/">http://www.sourceforge.net/projects/camelbones/</a>&gt;.

<h2>Starting From Scratch</h2>

 Unfortunately it is not that difficult somehow manage to break one's Mac <font SIZE="-1">OS X</font> Perl rather severely. If all else fails and you want to really, <font SIZE="-1"><b>REALLY</b></font>, start from scratch and remove even your Apple Perl installation (which has become corrupted somehow), the following instructions should do it. <b>Please think twice before following these instructions: they are much like conducting brain surgery to yourself. Without anesthesia.</b> We will <b>not</b> come to fix your system if you do this. 

 First, get rid of the libperl.dylib: 

 <pre>
    # cd /System/Library/Perl/darwin/CORE
    # rm libperl.dylib
</pre> 

 Then delete every .bundle file found anywhere in the folders: 

 <pre>
    /System/Library/Perl
    /Library/Perl
</pre> 

 You can find them for example by 

 <pre>
    # find /System/Library/Perl /Library/Perl -name '*.bundle' -print
</pre> 

 After this you can either copy Perl from your operating system media (you will need at least the /System/Library/Perl and /usr/bin/perl), or rebuild Perl from the source code with <tt>&quot;Configure -Dprefix=/usr -Duseshrplib&quot;</tt> <font SIZE="-1">NOTE:</font> the <tt>&quot;-Dprefix=/usr&quot;</tt> to replace the system Perl works much better with Perl 5.8.1 and later, in Perl 5.8.0 the settings were not quite right. 

 ``Pacifist'' from CharlesSoft (&lt;<a rel="nofollow" HREF="http://www.charlessoft.com/">http://www.charlessoft.com/</a>&gt;) is a nice way to extract the Perl binaries from the <font SIZE="-1">OS</font> media, without having to reinstall the entire <font SIZE="-1">OS.</font>

<h2>AUTHOR</h2>

 This <font SIZE="-1">README</font> was written by Sherm Pendley &lt;sherm [at] dot-app.org&gt;, and subsequently updated by Dominic Dunlop &lt;domo [at] computer.org&gt; and Breno G. de Oliveira &lt;garu [at] cpan.org&gt;. The ``Starting From Scratch'' recipe was contributed by John Montbriand &lt;montbriand [at] apple.com&gt;.

<h2>DATE</h2>

 Last modified 2013-04-29. 

<h2>Index</h2>



<dt><a HREF="#lbAM">Starting From Scratch</a>
<dd>
<dt><a HREF="#lbAN">AUTHOR</a>
<dd>
<dt><a HREF="#lbAO">DATE</a>
<dd></dl>
