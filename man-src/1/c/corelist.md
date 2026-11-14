---
title: "corelist(1)"
name: "corelist"
section: "1"
letter: "c"
url: "/docs/linux/man/1-corelist/"
---

<h2 class="name">NAME</h2>
 

 corelist - a commandline frontend to Module::CoreList 

<h2>DESCRIPTION</h2>

 See Module::CoreList for one.

<h2>SYNOPSIS</h2>

 <pre><code>
corelist - v
               corelist[-a | -d]&lt;ModuleName&gt; |
    / &lt;ModuleRegex&gt; / [&lt;ModuleVersion&gt;]... corelist[-v&lt;PerlVersion&gt;][&lt;ModuleName&gt; | / &lt;ModuleRegex&gt; / ]... corelist[-r&lt;PerlVersion&gt;]... corelist-- utils[-d]&lt;UtilityName&gt;[&lt;UtilityName&gt;]... corelist-- utils - v&lt;PerlVersion&gt;
                                                                                                                                                                                                                   corelist-- feature&lt;FeatureName&gt;[&lt;FeatureName&gt;]... corelist-- diff PerlVersion PerlVersion
                                                                                                                                                                                                                       corelist-- upstream&lt;ModuleName&gt;
</code></pre>

<h2>OPTIONS</h2>

<dl>
<dt>-a
<dd> lists all versions of the given module (or the matching modules, in case you used a module regexp) in the perls Module::CoreList knows about. 

 <pre>
    corelist -a Unicode
    Unicode was first released with perl v5.6.2
      v5.6.2     3.0.1
      v5.8.0     3.2.0
      v5.8.1     4.0.0
      v5.8.2     4.0.0
      v5.8.3     4.0.0
      v5.8.4     4.0.1
      v5.8.5     4.0.1
      v5.8.6     4.0.1
      v5.8.7     4.1.0
      v5.8.8     4.1.0
      v5.8.9     5.1.0
      v5.9.0     4.0.0
      v5.9.1     4.0.0
      v5.9.2     4.0.1
      v5.9.3     4.1.0
      v5.9.4     4.1.0
      v5.9.5     5.0.0
      v5.10.0    5.0.0
      v5.10.1    5.1.0
      v5.11.0    5.1.0
      v5.11.1    5.1.0
      v5.11.2    5.1.0
      v5.11.3    5.2.0
      v5.11.4    5.2.0
      v5.11.5    5.2.0
      v5.12.0    5.2.0
      v5.12.1    5.2.0
      v5.12.2    5.2.0
      v5.12.3    5.2.0
      v5.12.4    5.2.0
      v5.13.0    5.2.0
      v5.13.1    5.2.0
      v5.13.2    5.2.0
      v5.13.3    5.2.0
      v5.13.4    5.2.0
      v5.13.5    5.2.0
      v5.13.6    5.2.0
      v5.13.7    6.0.0
      v5.13.8    6.0.0
      v5.13.9    6.0.0
      v5.13.10   6.0.0
      v5.13.11   6.0.0
      v5.14.0    6.0.0
      v5.14.1    6.0.0
      v5.15.0    6.0.0
</pre>
<dt>-d
<dd> finds the first perl version where a module has been released by date, and not by version number (as is the default).
<dt>--diff
<dd> Given two versions of perl, this prints a human-readable table of all module changes between the two. The output format may change in the future, and is meant for <i>humans</i>, not programs. For programs, use the Module::CoreList <font SIZE="-1">API.</font>
<dt>-? or -help
<dd> help! help! help! to see more help, try --man.
<dt>-man
<dd> all of the help
<dt>-v
<dd> lists all of the perl release versions we got the CoreList for. 

 If you pass a version argument (value of <tt>$]</tt>, like <tt>5.00503</tt> or <tt>5.008008</tt>), you get a list of all the modules and their respective versions. (If you have the <tt>&quot;version&quot;</tt> module, you can also use new-style version numbers, like <tt>5.8.8</tt>.) 

 In module filtering context, it can be used as Perl version filter.
<dt>-r
<dd> lists all of the perl releases and when they were released 

 If you pass a perl version you get the release date for that version only.
<dt>--utils
<dd> lists the first version of perl each named utility program was released with 

 May be used with -d to modify the first release criteria. 

 If used with -v &lt;version&gt; then all utilities released with that version of perl are listed, and any utility programs named on the command line are ignored.
<dt>--feature, -f
<dd> lists the first version bundle of each named feature given
<dt>--upstream, -u
<dd> Shows if the given module is primarily maintained in perl core or on <font SIZE="-1">CPAN</font> and bug tracker <font SIZE="-1">URL.</font></dl>
 

 As a special case, if you specify the module name <tt>&quot;Unicode&quot;</tt>, you'll get the version number of the Unicode Character Database bundled with the requested perl versions.

<h2>EXAMPLES</h2>

 <pre>
    $ corelist File::Spec
    File::Spec was first released with perl 5.005
    $ corelist File::Spec 0.83
    File::Spec 0.83 was released with perl 5.007003
    $ corelist File::Spec 0.89
    File::Spec 0.89 was not in CORE (or so I think)
    $ corelist File::Spec::Aliens
    File::Spec::Aliens  was not in CORE (or so I think)
    $ corelist /IPC::Open/
    IPC::Open2 was first released with perl 5
    IPC::Open3 was first released with perl 5
    $ corelist /MANIFEST/i
    ExtUtils::Manifest was first released with perl 5.001
    $ corelist /Template/
    /Template/  has no match in CORE (or so I think)
    $ corelist -v 5.8.8 B
    B                        1.09_01
    $ corelist -v 5.8.8 /^B::/
    B::Asmdata               1.01
    B::Assembler             0.07
    B::Bblock                1.02_01
    B::Bytecode              1.01_01
    B::C                     1.04_01
    B::CC                    1.00_01
    B::Concise               0.66
    B::Debug                 1.02_01
    B::Deparse               0.71
    B::Disassembler          1.05
    B::Lint                  1.03
    B::O                     1.00
    B::Showlex               1.02
    B::Stackobj              1.00
    B::Stash                 1.00
    B::Terse                 1.03_01
    B::Xref                  1.01
</pre>

<h2>COPYRIGHT</h2>

 Copyright (c) 2002-2007 by D.H. aka PodMaster 

 Currently maintained by the perl 5 porters &lt;perl5-porters [at] perl.org&gt;. 

 This program is distributed under the same terms as perl itself. See <a rel="nofollow" HREF="http://perl.org/">http://perl.org/</a> or <a rel="nofollow" HREF="http://cpan.org/">http://cpan.org/</a> for more info on that. 

<h2>Index</h2>


