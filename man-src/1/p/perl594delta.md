---
title: "perl594delta(1)"
name: "perl594delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl594delta/"
description: "perl594delta – what is new for perl v5.9.4"
---

<h2 class="name">NAME</h2>
<p> perl594delta &#8211; what is new for perl v5.9.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.3 and the 5.9.4 development releases. See perl590delta, perl591delta, perl592delta and perl593delta for the differences between 5.8.0 and 5.9.3.</p>
<h2>Incompatible Changes</h2>
<h3>chdir <font SIZE="-1">FOO</font></h3>
<p> A bareword argument to <i>chdir()</i> is now recognized as a file handle. Earlier releases interpreted the bareword as a directory name. (Gisle Aas)</p>
<h3>Handling of pmc files</h3>
<p> An old feature of perl was that before <tt>&quot;require&quot;</tt> or <tt>&quot;use&quot;</tt> look for a file with a <i>.pm</i> extension, they will first look for a similar filename with a <i>.pmc</i> extension. If this file is found, it will be loaded in place of any potentially existing file ending in a <i>.pm</i> extension. </p>
<p> Previously, <i>.pmc</i> files were loaded only if more recent than the matching <i>.pm</i> file. Starting with 5.9.4, they&#8217;ll be always loaded if they exist. (This trick is used by Pugs.)</p>
<h3>@- and @+ in patterns</h3>
<p> The special arrays <tt>&quot;@-&quot;</tt> and <tt>&quot;@+&quot;</tt> are no longer interpolated in regular expressions. (Sadahiro Tomoyuki)</p>
<h3>$AUTOLOAD can now be tainted</h3>
<p> If you call a subroutine by a tainted name, and if it defers to an <font SIZE="-1">AUTOLOAD</font> function, then <tt>$AUTOLOAD</tt> will be (correctly) tainted. (Rick Delaney)</p>
<h2>Core Enhancements</h2>
<h3><i>state()</i> variables</h3>
<p> A new class of variables has been introduced. State variables are similar to <tt>&quot;my&quot;</tt> variables, but are declared with the <tt>&quot;state&quot;</tt> keyword in place of <tt>&quot;my&quot;</tt>. They&#8217;re visible only in their lexical scope, but their value is persistent: unlike <tt>&quot;my&quot;</tt> variables, they&#8217;re not undefined at scope entry, but retain their previous value. (Rafael Garcia-Suarez) </p>
<p> To use state variables, one needs to enable them by using </p>
<pre>
    use feature &quot;state&quot;;
</pre>
<p> or by using the <tt>&quot;-E&quot;</tt> command-line switch in one-liners. </p>
<p> See &#8220;Persistent variables via <i>state()</i>&#8221; in perlsub.</p>
<h3><font SIZE="-1"><i>UNIVERSAL::DOES</i></font><i>()</i></h3>
<p> The <tt>&quot;UNIVERSAL&quot;</tt> class has a new method, <tt>&quot;DOES()&quot;</tt>. It has been added to solve semantic problems with the <tt>&quot;isa()&quot;</tt> method. <tt>&quot;isa()&quot;</tt> checks for inheritance, while <tt>&quot;DOES()&quot;</tt> has been designed to be overridden when module authors use other types of relations between classes (in addition to inheritance). (chromatic) </p>
<p> See &#8220;$obj-&gt;<font SIZE="-1">DOES</font>( <font SIZE="-1">ROLE</font> )&#8221; in <font SIZE="-1">UNIVERSAL</font>.</p>
<h3>Exceptions in constant folding</h3>
<p> The constant folding routine is now wrapped in an exception handler, and if folding throws an exception (such as attempting to evaluate 0/0), perl now retains the current optree, rather than aborting the whole program. (Nicholas Clark, Dave Mitchell)</p>
<h3>Source filters in @INC</h3>
<p> It&#8217;s possible to enhance the mechanism of subroutine hooks in <tt>@INC</tt> by adding a source filter on top of the filehandle opened and returned by the hook. This feature was planned a long time ago, but wasn&#8217;t quite working until now. See &#8220;require&#8221; in perlfunc for details. (Nicholas Clark)</p>
<h3><font SIZE="-1">MAD</font></h3>
<p> <font SIZE="-1">MAD</font>, which stands for <i>Misc Attribute Decoration</i>, is a still-in-development work leading to a Perl 5 to Perl 6 converter. To enable it, it&#8217;s necessary to pass the argument <tt>&quot;-Dmad&quot;</tt> to Configure. The obtained perl isn&#8217;t binary compatible with a regular perl 5.9.4, and has space and speed penalties; moreover not all regression tests still pass with it. (Larry Wall, Nicholas Clark)</p>
<h2>Modules and Pragmas</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;encoding::warnings&quot;</tt> is now a lexical pragma. (Although on older perls, which don&#8217;t have support for lexical pragmas, it keeps its global behaviour.) (Audrey Tang)</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> is now a dual-life module, also available on <font SIZE="-1">CPAN</font>. It has been expanded in many ways. A <i>kill()</i> method is available for thread signalling. One can get thread status, or the list of running or joinable threads. </p>
<p> A new <tt>&quot;threads-&gt;exit()&quot;</tt> method is used to exit from the application (this is the default for the main thread) or from the current thread only (this is the default for all other threads). On the other hand, the <i>exit()</i> built-in now always causes the whole application to terminate. (Jerry D. Hedden)</dl>
<h3>New Core Modules</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util::FieldHash&quot;</tt>, by Anno Siegel, has been added. This module provides support for <i>field hashes</i>: hashes that maintain an association of a reference with a value, in a thread-safe garbage-collected way. Such hashes are useful to implement inside-out objects.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Build&quot;</tt>, by Ken Williams, has been added. It&#8217;s an alternative to <tt>&quot;ExtUtils::MakeMaker&quot;</tt> to build and install perl modules.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Load&quot;</tt>, by Jos Boumans, has been added. It provides a single interface to load Perl modules and <i>.pl</i> files.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Loaded&quot;</tt>, by Jos Boumans, has been added. It&#8217;s used to mark modules as loaded or unloaded.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Package::Constants&quot;</tt>, by Jos Boumans, has been added. It&#8217;s a simple helper to list all constants declared in a given package.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Win32API::File&quot;</tt>, by Tye McQueen, has been added (for Windows builds). This module provides low-level access to Win32 system <font SIZE="-1">API</font> calls for files/dirs.</dl>
<h2>Utility Changes</h2>
<h3>config_data</h3>
<p> <tt>&quot;config_data&quot;</tt> is a new utility that comes with <tt>&quot;Module::Build&quot;</tt>. It provides a command-line interface to the configuration of Perl modules that use Module::Build&#8217;s framework of configurability (that is, <tt>*::ConfigData</tt> modules that contain local configuration information for their parent modules.)</p>
<h2>Documentation</h2>
<h3>New manpage, perlpragma</h3>
<p> The perlpragma manpage documents how to write one&#8217;s own lexical pragmas in pure Perl (something that is possible starting with 5.9.4).</p>
<h3>New manpage, perlreguts</h3>
<p> The perlreguts manpage, courtesy of Yves Orton, describes internals of the Perl regular expression engine.</p>
<h3>New manpage, perlunitut</h3>
<p> The perlunitut manpage is an tutorial for programming with Unicode and string encodings in Perl, courtesy of Juerd Waalboer.</p>
<h2>Performance Enhancements</h2>
<h3>Memory optimisations</h3>
<p> Several internal data structures (typeglobs, GVs, CVs, formats) have been restructured to use less memory. (Nicholas Clark)</p>
<h3><font SIZE="-1">UTF-8</font> cache optimisation</h3>
<p> The <font SIZE="-1">UTF-8</font> caching code is now more efficient, and used more often. (Nicholas Clark)</p>
<h3>Regular expressions</h3>
<dl>
<dt>Engine de-recursivised</p>
<dd> The regular expression engine is no longer recursive, meaning that patterns that used to overflow the stack will either die with useful explanations, or run to completion, which, since they were able to blow the stack before, will likely take a very long time to happen. If you were experiencing the occasional stack overflow (or segfault) and upgrade to discover that now perl apparently hangs instead, look for a degenerate regex. (Dave Mitchell)</p>
<dt>Single char char-classes treated as literals</p>
<dd> Classes of a single character are now treated the same as if the character had been used as a literal, meaning that code that uses char-classes as an escaping mechanism will see a speedup. (Yves Orton)</p>
<dt>Trie optimisation of literal string alternations</p>
<dd> Alternations, where possible, are optimised into more efficient matching structures. String literal alternations are merged into a trie and are matched simultaneously. This means that instead of O(N) time for matching N alternations at a given point the new code performs in <a href="/docs/linux/man/1-o/">O</a>(1) time. (Yves Orton) </p>
<p> <code>Note:</code> Much code exists that works around perl&#8217;s historic poor performance on alternations. Often the tricks used to do so will disable the new optimisations. Hopefully the utility modules used for this purpose will be educated about these new optimisations by the time 5.10 is released.</p>
<dt>Aho-Corasick start-point optimisation</p>
<dd> When a pattern starts with a trie-able alternation and there aren&#8217;t better optimisations available the regex engine will use Aho-Corasick matching to find the start point. (Yves Orton)</dl>
<h3>Sloppy stat on Windows</h3>
<p> On Windows, perl&#8217;s <i>stat()</i> function normally opens the file to determine the link count and update attributes that may have been changed through hard links. Setting ${^WIN32_SLOPPY_STAT} to a true value speeds up <i>stat()</i> by not performing this operation. (Jan Dubois)</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Relocatable installations</h3>
<p> There is now Configure support for creating a relocatable perl tree. If you Configure with <tt>&quot;-Duserelocatableinc&quot;</tt>, then the paths in <tt>@INC</tt> (and everything else in <tt>%Config</tt>) can be optionally located via the path of the perl executable. </p>
<p> That means that, if the string <tt>&quot;.../&quot;</tt> is found at the start of any path, it&#8217;s substituted with the directory of $^X. So, the relocation can be configured on a per-directory basis, although the default with <tt>&quot;-Duserelocatableinc&quot;</tt> is that everything is relocated. The initial install is done to the original configured prefix.</p>
<h3>Ports</h3>
<p> Many improvements have been made towards making Perl work correctly on z/OS. </p>
<p> Perl has been reported to work on DragonFlyBSD.</p>
<h3>Compilation improvements</h3>
<p> All <i>ppport.h</i> files in the <font SIZE="-1">XS</font> modules bundled with perl are now autogenerated at build time. (Marcus Holland-Moritz)</p>
<h3>New probes</h3>
<p> The configuration process now detects whether <i>strlcat()</i> and <i>strlcpy()</i> are available. When they are not available, perl&#8217;s own version is used (from Russ Allbery&#8217;s public domain implementation). Various places in the perl interpreter now use them. (Steve Peters)</p>
<h3>Windows build improvements</h3>
<dl>
<dt>Building <font SIZE="-1">XS</font> extensions</p>
<dd> Support for building <font SIZE="-1">XS</font> extension modules with the free MinGW compiler has been improved in the case where perl itself was built with the Microsoft <font SIZE="-1">VC++</font> compiler. (ActiveState)</p>
<dt>Support for 64-bit compiler</p>
<dd> Support for building perl with Microsoft&#8217;s 64-bit compiler has been improved. (ActiveState)</dl>
<h2>Selected Bug Fixes</h2>
<h3><font SIZE="-1">PERL5SHELL</font> and tainting</h3>
<p> On Windows, the <font SIZE="-1">PERL5SHELL</font> environment variable is now checked for taintedness. (Rafael Garcia-Suarez)</p>
<h3>Using *FILE{<font SIZE="-1">IO</font>}</h3>
<p> <tt>&quot;stat()&quot;</tt> and <tt>&quot;-X&quot;</tt> filetests now treat *FILE{<font SIZE="-1">IO</font>} filehandles like *FILE filehandles. (Steve Peters)</p>
<h3>Overloading and reblessing</h3>
<p> Overloading now works when references are reblessed into another class. Internally, this has been implemented by moving the flag for &#8220;overloading&#8221; from the reference to the referent, which logically is where it should always have been. (Nicholas Clark)</p>
<h3>Overloading and <font SIZE="-1">UTF-8</font></h3>
<p> A few bugs related to <font SIZE="-1">UTF-8</font> handling with objects that have stringification overloaded have been fixed. (Nicholas Clark)</p>
<h3>eval memory leaks fixed</h3>
<p> Traditionally, <tt>&quot;eval 'syntax error'&quot;</tt> has leaked badly. Many (but not all) of these leaks have now been eliminated or reduced. (Dave Mitchell)</p>
<h3>Random device on Windows</h3>
<p> In previous versions, perl would read the file <i>/dev/urandom</i> if it existed when seeding its random number generator. That file is unlikely to exist on Windows, and if it did would probably not contain appropriate data, so perl no longer tries to read it on Windows. (Alex Davies)</p>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>State variable %s will be reinitialized</p>
<dd> One can assign initial values to state variables, but not when they&#8217;re declared as a sub-part of a list assignment. See perldiag.</dl>
<h2>Changed Internals</h2>
<p> A new file, <i>mathoms.c</i>, contains functions that aren&#8217;t used anymore in the perl core, but remain around because modules out there might still use them. They come from a factorization effort: for example, many <font SIZE="-1">PP</font> functions are now shared for several ops. </p>
<p> The implementation of the special variables $^H and %^H has changed, to allow implementing lexical pragmas in pure perl.</p>
<h2>Known Problems</h2>
<p> One warning test (number 263 in <i>lib/warnings.t</i>) fails under <font SIZE="-1">UTF-8</font> locales. </p>
<p> Bytecode tests fail under several platforms. We are considering removing support for byteloader and compiler before the 5.10.0 release.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/rt3/">http://rt.perl.org/rt3/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Core Enhancements</a></p>
<dd>
<dt><a href="#lbAO">Modules and Pragmas</a></p>
<dd>
<dt><a href="#lbAQ">Utility Changes</a></p>
<dd>
<dt><a href="#lbAS">Documentation</a></p>
<dd>
<dt><a href="#lbAW">Performance Enhancements</a></p>
<dd>
<dt><a href="#lbBB">Installation and Configuration Improvements</a></p>
<dd>
<dt><a href="#lbBH">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbBO">New or Changed Diagnostics</a></p>
<dd>
<dt><a href="#lbBP">Changed Internals</a></p>
<dd>
<dt><a href="#lbBQ">Known Problems</a></p>
<dd>
<dt><a href="#lbBR">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbBS">SEE ALSO</a></p>
<dd></dl>
