---
title: "perlsource(1)"
name: "perlsource"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsource/"
---

<h2 class="name">NAME</h2>
 

 perlsource - A guide to the Perl source tree 

<h2>DESCRIPTION</h2>

 This document describes the layout of the Perl source tree. If you're hacking on the Perl core, this will help you find what you're looking for.

<h2>FINDING YOUR WAY AROUND</h2>

 The Perl source tree is big. Here's some of the thing you'll find in it:

<h3>C code</h3>

 The C source code and header files mostly live in the root of the source tree. There are a few platform-specific directories which contain C code. In addition, some of the modules shipped with Perl include C or <font SIZE="-1">XS</font> code. 

 See perlinterp for more details on the files that make up the Perl interpreter, as well as details on how it works.

<h3>Core modules</h3>

 Modules shipped as part of the Perl core live in four subdirectories. Two of these directories contain modules that live in the core, and two contain modules that can also be released separately on <font SIZE="-1">CPAN.</font> Modules which can be released on cpan are known as ``dual-life'' modules.
<dl>
<dt>&bull;
<dd> <i>lib/</i> 

 This directory contains pure-Perl modules which are only released as part of the core. This directory contains <i>all</i> of the modules and their tests, unlike other core modules.
<dt>&bull;
<dd> <i>ext/</i> 

 Like <i>lib/</i>, this directory contains modules which are only released as part of the core. Unlike <i>lib/</i>, however, a module under <i>ext/</i> generally has a CPAN-style directory- and file-layout and its own <i>Makefile.PL</i>. There is no expectation that a module under <i>ext/</i> will work with earlier versions of Perl 5. Hence, such a module may take full advantage of syntactical and other improvements in Perl 5 blead.
<dt>&bull;
<dd> <i>dist/</i> 

 This directory is for dual-life modules where the blead source is canonical. Note that some modules in this directory may not yet have been released separately on <font SIZE="-1">CPAN.</font> Modules under <i>dist/</i> should make an effort to work with earlier versions of Perl 5.
<dt>&bull;
<dd> <i>cpan/</i> 

 This directory contains dual-life modules where the <font SIZE="-1">CPAN</font> module is canonical. Do not patch these modules directly! Changes to these modules should be submitted to the maintainer of the <font SIZE="-1">CPAN</font> module. Once those changes are applied and released, the new version of the module will be incorporated into the core.</dl>
 

 For some dual-life modules, it has not yet been determined if the <font SIZE="-1">CPAN</font> version or the blead source is canonical. Until that is done, those modules should be in <i>cpan/</i>.

<h3>Tests</h3>

 The Perl core has an extensive test suite. If you add new tests (or new modules with tests), you may need to update the <i>t/TEST</i> file so that the tests are run.
<dl>
<dt>&bull;
<dd> Module tests 

 Tests for core modules in the <i>lib/</i> directory are right next to the module itself. For example, we have <i>lib/strict.pm</i> and <i>lib/strict.t</i>. 

 Tests for modules in <i>ext/</i> and the dual-life modules are in <i>t/</i> subdirectories for each module, like a standard <font SIZE="-1">CPAN</font> distribution.
<dt>&bull;
<dd> <i>t/base/</i> 

 Tests for the absolute basic functionality of Perl. This includes <tt>&quot;if&quot;</tt>, basic file reads and writes, simple regexes, etc. These are run first in the test suite and if any of them fail, something is <i>really</i> broken.
<dt>&bull;
<dd> <i>t/cmd/</i> 

 Tests for basic control structures, <tt>&quot;if&quot;</tt>/<tt>&quot;else&quot;</tt>, <tt>&quot;while&quot;</tt>, subroutines, etc.
<dt>&bull;
<dd> <i>t/comp/</i> 

 Tests for basic issues of how Perl parses and compiles itself.
<dt>&bull;
<dd> <i>t/io/</i> 

 Tests for built-in <font SIZE="-1">IO</font> functions, including command line arguments.
<dt>&bull;
<dd> <i>t/mro/</i> 

 Tests for perl's method resolution order implementations (see mro).
<dt>&bull;
<dd> <i>t/op/</i> 

 Tests for perl's built in functions that don't fit into any of the other directories.
<dt>&bull;
<dd> <i>t/opbasic/</i> 

 Tests for perl's built in functions which, like those in <i>t/op/</i>, do not fit into any of the other directories, but which, in addition, cannot use <i>t/test.pl</i>,as that program depends on functionality which the test file itself is testing.
<dt>&bull;
<dd> <i>t/re/</i> 

 Tests for regex related functions or behaviour. (These used to live in t/op).
<dt>&bull;
<dd> <i>t/run/</i> 

 Tests for features of how perl actually runs, including exit codes and handling of PERL* environment variables.
<dt>&bull;
<dd> <i>t/uni/</i> 

 Tests for the core support of Unicode.
<dt>&bull;
<dd> <i>t/win32/</i> 

 Windows-specific tests.
<dt>&bull;
<dd> <i>t/porting/</i> 

 Tests the state of the source tree for various common errors. For example, it tests that everyone who is listed in the git log has a corresponding entry in the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file.
<dt>&bull;
<dd> <i>t/lib/</i> 

 The old home for the module tests, you shouldn't put anything new in here. There are still some bits and pieces hanging around in here that need to be moved. Perhaps you could move them? Thanks!</dl>

<h3>Documentation</h3>

 All of the core documentation intended for end users lives in <i>pod/</i>. Individual modules in <i>lib/</i>, <i>ext/</i>, <i>dist/</i>, and <i>cpan/</i> usually have their own documentation, either in the <i>Module.pm</i> file or an accompanying <i>Module.pod</i> file. 

 Finally, documentation intended for core Perl developers lives in the <i>Porting/</i> directory.

<h3>Hacking tools and documentation</h3>

 The <i>Porting</i> directory contains a grab bag of code and documentation intended to help porters work on Perl. Some of the highlights include:
<dl>
<dt>&bull;
<dd> <i>check*</i> 

 These are scripts which will check the source things like <font SIZE="-1">ANSI C</font> violations, <font SIZE="-1">POD</font> encoding issues, etc.
<dt>&bull;
<dd> <i>Maintainers</i>, <i>Maintainers.pl</i>, and <i>Maintainers.pm</i> 

 These files contain information on who maintains which modules. Run <tt>&quot;perl Porting/Maintainers -M Module::Name&quot;</tt> to find out more information about a dual-life module.
<dt>&bull;
<dd> <i>podtidy</i> 

 Tidies a pod file. It's a good idea to run this on a pod file you've patched.</dl>

<h3>Build system</h3>

 The Perl build system starts with the <i>Configure</i> script in the root directory. 

 Platform-specific pieces of the build system also live in platform-specific directories like <i>win32/</i>, <i>vms/</i>, etc. 

 The <i>Configure</i> script is ultimately responsible for generating a <i>Makefile</i>. 

 The build system that Perl uses is called metaconfig. This system is maintained separately from the Perl core. 

 The metaconfig system has its own git repository. Please see its <font SIZE="-1">README</font> file in &lt;<a rel="nofollow" HREF="http://perl5.git.perl.org/metaconfig.git/">http://perl5.git.perl.org/metaconfig.git/</a>&gt; for more details. 

 The <i>Cross</i> directory contains various files related to cross-compiling Perl. See <i>Cross/README</i> for more details.

<h3><i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i></h3>

 This file lists everyone who's contributed to Perl. If you submit a patch, you should add your name to this file as part of the patch.

<h3><i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i></h3>

 The <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i> file in the root of the source tree contains a list of every file in the Perl core, as well as a brief description of each file. 

 You can get an overview of all the files with this command: 

 <pre><code>
% perl - lne 'print if /^[^\/]+\.[ch]\s+/' MANIFEST
</code></pre> 

<h2>Index</h2>


</dl>
