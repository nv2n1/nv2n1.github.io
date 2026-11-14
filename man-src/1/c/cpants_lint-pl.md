---
title: "cpants_lint-pl(1)"
name: "cpants_lint-pl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpants_lint-pl/"
description: "cpants_lint.pl – commandline frontend to Module::CPANTS::Analyse"
---

<p>cpants_lint.pl &#8211; commandline frontend to Module::CPANTS::Analyse </p>
<h2>Synopsis</h2>
<pre> cpants_lint.pl path/to/Foo-Dist-1.42.tgz
 Options:
 --help brief help message
 --man full documentation
 --verbose print more info during run
 --no_capture don't turn on capturing of STDERR and STDOUT
 --dump dump result using Data::Dumper
 --yaml dump result as YAML
 --to_file dump result to a file
 --dir directory to dump files to</pre>
<h2>Description</h2>
<p><tt>&quot;cpants_lint.pl&quot;</tt> checks the <code>Kwalitee</code> of <font SIZE="-1">CPAN</font> distributions. More exact, it checks how a given tarball will be rated on <tt>&quot;<a rel="nofollow" href="http://cpants.perl.org">http://cpants.perl.org</a>&quot;</tt>, without needing to upload it first. </p>
<p> <tt>&quot;cpants_lint.pl&quot;</tt> is also used by <tt>&quot;cpants.perl.org&quot;</tt> itself to check all dists on <font SIZE="-1">CPAN.</font> </p>
<p> For more information on Kwalitee, and the whole of <font SIZE="-1">CPANTS,</font> see <tt>&quot;<a rel="nofollow" href="http://cpants.perl.org">http://cpants.perl.org</a>&quot;</tt> and / or <tt>&quot;Module::CPANTS::Analyse&quot;</tt>.</p>
<h2>Options</h2>
<p>If neither <tt>&quot;--dump&quot;</tt> nor <tt>&quot;--yaml&quot;</tt> are used, a short text describing the Kwalitee of the distribution and hints on how to raise Kwalitee will be displayed. The format of this text can change anytime, so don&#8217;t use it for any automated processing! </p>
<p> <i>&#8211;help</i> </p>
<p> Print a brief help message. </p>
<p> <i>&#8211;man</i> </p>
<p> Print manpage. </p>
<p> <i>&#8211;verbose</i> </p>
<p> Print some informative messages during testing of dists. </p>
<p> <i>&#8211;no_capture</i> </p>
<p> Turn off capturing of <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR.</font> Mostly usefull during debugging / development of new features. </p>
<p> If <tt>&quot;--no_capture&quot;</tt> is used, the value of <tt>&quot;cpants_error&quot;</tt> might be wrong. </p>
<p> <i>&#8211;dump</i> </p>
<p> Dump the result using Data::Dumper </p>
<p> <i>&#8211;yaml</i> </p>
<p> Dump the result as <font SIZE="-1">YAML.</font> </p>
<p> <i>&#8211;to_file</i> </p>
<p> Output the result into a file instead of <font SIZE="-1">STDOUT.</font> </p>
<p> The name of the file will be <i>Foo-Dist.yaml</i> (well, the extension depends on the dump format and can be <tt>&quot;.yaml&quot;</tt>, <tt>&quot;.dump&quot;</tt> or <tt>&quot;.txt&quot;</tt>) </p>
<p> <i>&#8211;dir</i> </p>
<p> Directory to dump files to. Defaults to the current working directory.</p>
<h2>Author</h2>
<p>Thomas Klausner &lt;<a rel="nofollow" href="https://metacpan.org/author/domm">https://metacpan.org/author/domm</a>&gt;</p>
<h2>Copyright And License</h2>
<p>Copyright X 2003X2006, 2009 Thomas Klausner &lt;<a rel="nofollow" href="https://metacpan.org/author/domm">https://metacpan.org/author/domm</a>&gt; </p>
<p> You may use and distribute this module according to the same terms that Perl is distributed under.</p>
