---
title: "perl5120delta(1)"
name: "perl5120delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5120delta/"
description: "perl5120delta – what is new for perl v5.12.0"
---

<h2 class="name">NAME</h2>
<p> perl5120delta &#8211; what is new for perl v5.12.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.12.0 release. </p>
<p> Many of the bug fixes in 5.12.0 are already included in the 5.10.1 maintenance release. </p>
<p> You can see the list of those changes in the 5.10.1 release notes (perl5101delta).</p>
<h2>Core Enhancements</h2>
<h3>New package NAME VERSION syntax</h3>
<p> This new syntax allows a module author to set the <tt>$VERSION</tt> of a namespace when the namespace is declared with &#8216;package&#8217;. It eliminates the need for <tt>&quot;our $VERSION = ...&quot;</tt> and similar constructs. E.g. </p>
<pre>
      package Foo::Bar 1.23;
      # $Foo::Bar::VERSION == 1.23
</pre>
<p> There are several advantages to this:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>$VERSION</tt> is parsed in exactly the same way as <tt>&quot;use NAME VERSION&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>$VERSION</tt> is set at compile time</dd>
<dt>&bull;</dt>
<dd> <tt>$VERSION</tt> is a version object that provides proper overloading of comparison operators so comparing <tt>$VERSION</tt> to decimal (1.23) or dotted-decimal (v1.2.3) version numbers works correctly.</dd>
<dt>&bull;</dt>
<dd> Eliminates <tt>&quot;$VERSION = ...&quot;</tt> and <tt>&quot;eval $VERSION&quot;</tt> clutter</dd>
<dt>&bull;</dt>
<dd> As it requires <font SIZE="-1">VERSION</font> to be a numeric literal or v-string literal, it can be statically parsed by toolchain modules without <tt>&quot;eval&quot;</tt> the way <font SIZE="-1">MM-</font>&gt;parse_version does for <tt>&quot;$VERSION = ...&quot;</tt></dd></dl>
<p> It does not break old code with only <tt>&quot;package NAME&quot;</tt>, but code that uses <tt>&quot;package NAME VERSION&quot;</tt> will need to be restricted to perl 5.12.0 or newer This is analogous to the change to <tt>&quot;open&quot;</tt> from two-args to three-args. Users requiring the latest Perl will benefit, and perhaps after several years, it will become a standard practice. </p>
<p> However, <tt>&quot;package NAME VERSION&quot;</tt> requires a new, &#8216;strict&#8217; version number format. See &#8220;Version number formats&#8221; for details.</p>
<h3>The &#8230; operator</h3>
<p> A new operator, <tt>&quot;...&quot;</tt>, nicknamed the Yada Yada operator, has been added. It is intended to mark placeholder code that is not yet implemented. See &#8220;Yada Yada Operator&#8221; in perlop.</p>
<h3>Implicit strictures</h3>
<p> Using the <tt>&quot;use VERSION&quot;</tt> syntax with a version number greater or equal to 5.11.0 will lexically enable strictures just like <tt>&quot;use strict&quot;</tt> would do (in addition to enabling features.) The following: </p>
<pre>
    use 5.12.0;
</pre>
<p> means: </p>
<pre>
    use strict;
    use feature ':5.12';
</pre>
<h3>Unicode improvements</h3>
<p> Perl 5.12 comes with Unicode 5.2, the latest version available to us at the time of release. This version of Unicode was released in October 2009. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.2.0">http://www.unicode.org/versions/Unicode5.2.0</a>&gt; for further details about what&#8217;s changed in this version of the standard. See perlunicode for instructions on installing and using other versions of Unicode. </p>
<p> Additionally, Perl&#8217;s developers have significantly improved Perl&#8217;s Unicode implementation. For full details, see &#8220;Unicode overhaul&#8221; below.</p>
<h3>Y2038 compliance</h3>
<p> Perl&#8217;s core time-related functions are now Y2038 compliant. (It may not mean much to you, but your kids will love it!)</p>
<h3>qr overloading</h3>
<p> It is now possible to overload the <tt>&quot;qr//&quot;</tt> operator, that is, conversion to regexp, like it was already possible to overload conversion to boolean, string or number of objects. It is invoked when an object appears on the right hand side of the <tt>&quot;=~&quot;</tt> operator or when it is interpolated into a regexp. See overload.</p>
<h3>Pluggable keywords</h3>
<p> Extension modules can now cleanly hook into the Perl parser to define new kinds of keyword-headed expression and compound statement. The syntax following the keyword is defined entirely by the extension. This allows a completely non-Perl sublanguage to be parsed inline, with the correct ops cleanly generated. </p>
<p> See &#8220;PL_keyword_plugin&#8221; in perlapi for the mechanism. The Perl core source distribution also includes a new module XS::APItest::KeywordRPN, which implements reverse Polish notation arithmetic via pluggable keywords. This module is mainly used for test purposes, and is not normally installed, but also serves as an example of how to use the new mechanism. </p>
<p> Perl&#8217;s developers consider this feature to be experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.</p>
<h3>APIs for more internals</h3>
<p> The lowest layers of the lexer and parts of the pad system now have C APIs available to <font SIZE="-1">XS</font> extensions. These are necessary to support proper use of pluggable keywords, but have other uses too. The new APIs are experimental, and only cover a small proportion of what would be necessary to take full advantage of the core&#8217;s facilities in these areas. It is intended that the Perl 5.13 development cycle will see the addition of a full range of clean, supported interfaces. </p>
<p> Perl&#8217;s developers consider this feature to be experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.</p>
<h3>Overridable function lookup</h3>
<p> Where an extension module hooks the creation of rv2cv ops to modify the subroutine lookup process, this now works correctly for bareword subroutine calls. This means that prototypes on subroutines referenced this way will be processed correctly. (Previously bareword subroutine names were initially looked up, for parsing purposes, by an unhookable mechanism, so extensions could only properly influence subroutine names that appeared with an <tt>&quot;&amp;&quot;</tt> sigil.)</p>
<h3>A proper interface for pluggable Method Resolution Orders</h3>
<p> As of Perl 5.12.0 there is a new interface for plugging and using method resolution orders other than the default linear depth first search. The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. See perlmroapi for more information.</p>
<h3>\N experimental regex escape</h3>
<p> Perl now supports <tt>&quot;\N&quot;</tt>, a new regex escape which you can think of as the inverse of <tt>&quot;
&quot;</tt>. It will match any character that is not a newline, independently from the presence or absence of the single line match modifier <tt>&quot;/s&quot;</tt>. It is not usable within a character class. <tt>&quot;\N{3}&quot;</tt> means to match 3 non-newlines; <tt>&quot;\N{5,}&quot;</tt> means to match at least 5. <tt>&quot;\N{NAME}&quot;</tt> still means the character or sequence named <tt>&quot;NAME&quot;</tt>, but <tt>&quot;NAME&quot;</tt> no longer can be things like <tt>3</tt>, or <tt>&quot;5,&quot;</tt>. </p>
<p> This will break a custom charnames translator which allows numbers for character names, as <tt>&quot;\N{3}&quot;</tt> will now mean to match 3 non-newline characters, and not the character whose name is <tt>3</tt>. (No name defined by the Unicode standard is a number, so only custom translators might be affected.) </p>
<p> Perl&#8217;s developers are somewhat concerned about possible user confusion with the existing <tt>&quot;\N{...}&quot;</tt> construct which matches characters by their Unicode name. Consequently, this feature is experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.</p>
<h3>DTrace support</h3>
<p> Perl now has some support for DTrace. See &#8220;DTrace support&#8221; in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.</p>
<h3>Support for configure_requires in <font SIZE="-1">CPAN</font> module metadata</h3>
<p> Both <tt>&quot;CPAN&quot;</tt> and <tt>&quot;CPANPLUS&quot;</tt> now support the <tt>&quot;configure_requires&quot;</tt> keyword in the <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> metadata file included in most recent <font SIZE="-1">CPAN</font> distributions. This allows distribution authors to specify configuration prerequisites that must be installed before running <i>Makefile.PL</i> or <i>Build.PL</i>. </p>
<p> See the documentation for <tt>&quot;ExtUtils::MakeMaker&quot;</tt> or <tt>&quot;Module::Build&quot;</tt> for more on how to specify <tt>&quot;configure_requires&quot;</tt> when creating a distribution for <font SIZE="-1">CPAN.</font></p>
<h3>each, keys, values are now more flexible</h3>
<p> The <tt>&quot;each&quot;</tt>, <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt> function can now operate on arrays.</p>
<h3>when as a statement modifier</h3>
<p> <tt>&quot;when&quot;</tt> is now allowed to be used as a statement modifier.</p>
<h3>$, flexibility</h3>
<p> The variable <tt>$,</tt> may now be tied.</p>
<h3>// in when clauses</h3>
<p> // now behaves like || in when clauses</p>
<h3>Enabling warnings from your shell environment</h3>
<p> You can now set <tt>&quot;-W&quot;</tt> from the <tt>&quot;PERL5OPT&quot;</tt> environment variable</p>
<h3>delete local</h3>
<p> <tt>&quot;delete local&quot;</tt> now allows you to locally delete a hash entry.</p>
<h3>New support for Abstract namespace sockets</h3>
<p> Abstract namespace sockets are Linux-specific socket type that live in <font SIZE="-1">AF_UNIX</font> family, slightly abusing it to be able to use arbitrary character arrays as addresses: They start with nul byte and are not terminated by nul byte, but with the length passed to the <code>socket()</code> system call.</p>
<h3>32-bit limit on substr arguments removed</h3>
<p> The 32-bit limit on <tt>&quot;substr&quot;</tt> arguments has now been removed. The full range of the system&#8217;s signed and unsigned integers is now available for the <tt>&quot;pos&quot;</tt> and <tt>&quot;len&quot;</tt> arguments.</p>
<h2>Potentially Incompatible Changes</h2>
<h3>Deprecations warn by default</h3>
<p> Over the years, Perl&#8217;s developers have deprecated a number of language features for a variety of reasons. Perl now defaults to issuing a warning if a deprecated language feature is used. Many of the deprecations Perl now warns you about have been deprecated for many years. You can find a list of what was deprecated in a given release of Perl in the <tt>&quot;perl5xxdelta.pod&quot;</tt> file for that release. </p>
<p> To disable this feature in a given lexical scope, you should use <tt>&quot;no warnings 'deprecated';&quot;</tt> For information about which language features are deprecated and explanations of various deprecation warnings, please see perldiag. See &#8220;Deprecations&#8221; below for the list of features and modules Perl&#8217;s developers have deprecated as part of this release.</p>
<h3>Version number formats</h3>
<p> Acceptable version number formats have been formalized into &#8220;strict&#8221; and &#8220;lax&#8221; rules. <tt>&quot;package NAME VERSION&quot;</tt> takes a strict version number. <tt>&quot;UNIVERSAL::VERSION&quot;</tt> and the version object constructors take lax version numbers. Providing an invalid version will result in a fatal error. The version argument in <tt>&quot;use NAME VERSION&quot;</tt> is first parsed as a numeric literal or v-string and then passed to <tt>&quot;UNIVERSAL::VERSION&quot;</tt> (and must then pass the &#8220;lax&#8221; format test). </p>
<p> These formats are documented fully in the version module. To a first approximation, a &#8220;strict&#8221; version number is a positive decimal number (integer or decimal-fraction) without exponentiation or else a dotted-decimal v-string with a leading &#8216;v&#8217; character and at least three components. A &#8220;lax&#8221; version number allows v-strings with fewer than three components or without a leading &#8216;v&#8217;. Under &#8220;lax&#8221; rules, both decimal and dotted-decimal versions may have a trailing &#8220;alpha&#8221; component separated by an underscore character after a fractional or dotted-decimal component. </p>
<p> The version module adds <tt>&quot;version::is_strict&quot;</tt> and <tt>&quot;version::is_lax&quot;</tt> functions to check a scalar against these rules.</p>
<h3>@INC reorganization</h3>
<p> In <tt>@INC</tt>, <tt>&quot;ARCHLIB&quot;</tt> and <tt>&quot;PRIVLIB&quot;</tt> now occur after the current version&#8217;s <tt>&quot;site_perl&quot;</tt> and <tt>&quot;vendor_perl&quot;</tt>. Modules installed into <tt>&quot;site_perl&quot;</tt> and <tt>&quot;vendor_perl&quot;</tt> will now be loaded in preference to those installed in <tt>&quot;ARCHLIB&quot;</tt> and <tt>&quot;PRIVLIB&quot;</tt>.</p>
<h3>REGEXPs are now first class</h3>
<p> Internally, Perl now treats compiled regular expressions (such as those created with <tt>&quot;qr//&quot;</tt>) as first class entities. Perl modules which serialize, deserialize or otherwise have deep interaction with Perl&#8217;s internal data structures need to be updated for this change. Most affected <font SIZE="-1">CPAN</font> modules have already been updated as of this writing.</p>
<h3>Switch statement changes</h3>
<p> The <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt> switch statement handles complex statements better than Perl 5.10.0 did (These enhancements are also available in 5.10.1 and subsequent 5.10 releases.) There are two new cases where <tt>&quot;when&quot;</tt> now interprets its argument as a boolean, instead of an expression to be used in a smart match:</p>
<dl>
<dt>flip-flop operators</dt>
<dd> The <tt>&quot;..&quot;</tt> and <tt>&quot;...&quot;</tt> flip-flop operators are now evaluated in boolean context, following their usual semantics; see &#8220;Range Operators&#8221; in perlop. </dd>
<p> Note that, as in perl 5.10.0, <tt>&quot;when (1..10)&quot;</tt> will not work to test whether a given value is an integer between 1 and 10; you should use <tt>&quot;when ([1..10])&quot;</tt> instead (note the array reference). </p>
<p> However, contrary to 5.10.0, evaluating the flip-flop operators in boolean context ensures it can now be useful in a <tt>&quot;when()&quot;</tt>, notably for implementing bistable conditions, like in: </p>
<pre>
    when (/^=begin/ .. /^=end/) {
      # do something
    }
</pre>
<dt>defined-or operator</dt>
<dd> A compound expression involving the defined-or operator, as in <tt>&quot;when (expr1 // expr2)&quot;</tt>, will be treated as boolean if the first expression is boolean. (This just extends the existing rule that applies to the regular or operator, as in <tt>&quot;when (expr1 || expr2)&quot;</tt>.)</dd></dl>
<h3>Smart match changes</h3>
<p> Since Perl 5.10.0, Perl&#8217;s developers have made a number of changes to the smart match operator. These, of course, also alter the behaviour of the switch statements where smart matching is implicitly used. These changes were also made for the 5.10.1 release, and will remain in subsequent 5.10 releases. </p>
<p> <i>Changes to type-based dispatch</i> </p>
<p> The smart match operator <tt>&quot;~~&quot;</tt> is no longer commutative. The behaviour of a smart match now depends primarily on the type of its right hand argument. Moreover, its semantics have been adjusted for greater consistency or usefulness in several cases. While the general backwards compatibility is maintained, several changes must be noted:</p>
<dl>
<dt>&bull;</dt>
<dd> Code references with an empty prototype are no longer treated specially. They are passed an argument like the other code references (even if they choose to ignore it).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;%hash ~~ sub {}&quot;</tt> and <tt>&quot;@array ~~ sub {}&quot;</tt> now test that the subroutine returns a true value for each key of the hash (or element of the array), instead of passing the whole hash or array as a reference to the subroutine.</dd>
<dt>&bull;</dt>
<dd> Due to the commutativity breakage, code references are no longer treated specially when appearing on the left of the <tt>&quot;~~&quot;</tt> operator, but like any vulgar scalar.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;undef ~~ %hash&quot;</tt> is always false (since <tt>&quot;undef&quot;</tt> can&#8217;t be a key in a hash). No implicit conversion to <tt>&quot;&quot;</tt> is done (as was the case in perl 5.10.0).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;$scalar ~~ @array&quot;</tt> now always distributes the smart match across the elements of the array. It&#8217;s true if one element in <tt>@array</tt> verifies <tt>&quot;$scalar ~~ $element&quot;</tt>. This is a generalization of the old behaviour that tested whether the array contained the scalar.</dd></dl>
<p> The full dispatch table for the smart match operator is given in &#8220;Smart matching in detail&#8221; in perlsyn. </p>
<p> <i>Smart match and overloading</i> </p>
<p> According to the rule of dispatch based on the rightmost argument type, when an object overloading <tt>&quot;~~&quot;</tt> appears on the right side of the operator, the overload routine will always be called (with a 3rd argument set to a true value, see overload.) However, when the object will appear on the left, the overload routine will be called only when the rightmost argument is a simple scalar. This way, distributivity of smart match across arrays is not broken, as well as the other behaviours with complex types (coderefs, hashes, regexes). Thus, writers of overloading routines for smart match mostly need to worry only with comparing against a scalar, and possibly with stringification overloading; the other common cases will be automatically handled consistently. </p>
<p> <tt>&quot;~~&quot;</tt> will now refuse to work on objects that do not overload it (in order to avoid relying on the object&#8217;s underlying structure). (However, if the object overloads the stringification or the numification operators, and if overload fallback is active, it will be used instead, as usual.)</p>
<h3>Other potentially incompatible changes</h3>
<dl>
<dt>&bull;</dt>
<dd> The definitions of a number of Unicode properties have changed to match those of the current Unicode standard. These are listed above under &#8220;Unicode overhaul&#8221;. This change may break code that expects the old definitions.</dd>
<dt>&bull;</dt>
<dd> The boolkeys op has moved to the group of hash ops. This breaks binary compatibility.</dd>
<dt>&bull;</dt>
<dd> Filehandles are now always blessed into <tt>&quot;IO::File&quot;</tt>. </dd>
<p> The previous behaviour was to bless Filehandles into FileHandle (an empty proxy class) if it was loaded into memory and otherwise to bless them into <tt>&quot;IO::Handle&quot;</tt>.</p>
<dt>&bull;</dt>
<dd> The semantics of <tt>&quot;use feature :5.10*&quot;</tt> have changed slightly. See &#8220;Modules and Pragmata&#8221; for more information.</dd>
<dt>&bull;</dt>
<dd> Perl&#8217;s developers now use git, rather than Perforce. This should be a purely internal change only relevant to people actively working on the core. However, you may see minor difference in perl as a consequence of the change. For example in some of details of the output of <tt>&quot;perl -V&quot;</tt>. See perlrepository for more information.</dd>
<dt>&bull;</dt>
<dd> As part of the <tt>&quot;Test::Harness&quot;</tt> 2.x to 3.x upgrade, the experimental <tt>&quot;Test::Harness::Straps&quot;</tt> module has been removed. See &#8220;Modules and Pragmata&#8221; for more details.</dd>
<dt>&bull;</dt>
<dd> As part of the <tt>&quot;ExtUtils::MakeMaker&quot;</tt> upgrade, the <tt>&quot;ExtUtils::MakeMaker::bytes&quot;</tt> and <tt>&quot;ExtUtils::MakeMaker::vmsish&quot;</tt> modules have been removed from this distribution.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Module::CoreList&quot;</tt> no longer contains the <tt>%:patchlevel</tt> hash.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;length undef&quot;</tt> now returns undef.</dd>
<dt>&bull;</dt>
<dd> Unsupported private C <font SIZE="-1">API</font> functions are now declared &#8220;static&#8221; to prevent leakage to Perl&#8217;s public <font SIZE="-1">API.</font></dd>
<dt>&bull;</dt>
<dd> To support the bootstrapping process, <i>miniperl</i> no longer builds with <font SIZE="-1">UTF-8</font> support in the regexp engine. </dd>
<p> This allows a build to complete with <font SIZE="-1">PERL_UNICODE</font> set and a <font SIZE="-1">UTF-8</font> locale. Without this there&#8217;s a bootstrapping problem, as miniperl can&#8217;t load the <font SIZE="-1">UTF-8</font> components of the regexp engine, because they&#8217;re not yet built.</p>
<dt>&bull;</dt>
<dd> <i>miniperl</i>&#8216;s <tt>@INC</tt> is now restricted to just <tt>&quot;-I...&quot;</tt>, the split of <tt>$ENV{PERL5LIB}</tt>, and &quot;<tt>&quot;.&quot;</tt>&quot;</dd>
<dt>&bull;</dt>
<dd> A space or a newline is now required after a <tt>&quot;#line XXX&quot;</tt> directive.</dd>
<dt>&bull;</dt>
<dd> Tied filehandles now have an additional method <font SIZE="-1">EOF</font> which provides the <font SIZE="-1">EOF</font> type.</dd>
<dt>&bull;</dt>
<dd> To better match all other flow control statements, <tt>&quot;foreach&quot;</tt> may no longer be used as an attribute.</dd>
<dt>&bull;</dt>
<dd> Perl&#8217;s command-line switch &#8220;-P&#8221;, which was deprecated in version 5.10.0, has now been removed. The <font SIZE="-1">CPAN</font> module <tt>&quot;Filter::cpp&quot;</tt> can be used as an alternative.</dd></dl>
<h2>Deprecations</h2>
<p> From time to time, Perl&#8217;s developers find it necessary to deprecate features or modules we&#8217;ve previously shipped as part of the core distribution. We are well aware of the pain and frustration that a backwards-incompatible change to Perl can cause for developers building or maintaining software in Perl. You can be sure that when we deprecate a functionality or syntax, it isn&#8217;t a choice we make lightly. Sometimes, we choose to deprecate functionality or syntax because it was found to be poorly designed or implemented. Sometimes, this is because they&#8217;re holding back other features or causing performance problems. Sometimes, the reasons are more complex. Wherever possible, we try to keep deprecated functionality available to developers in its previous form for at least one major release. So long as a deprecated feature isn&#8217;t actively disrupting our ability to maintain and extend Perl, we&#8217;ll try to leave it in place as long as possible. </p>
<p> The following items are now deprecated:</p>
<dl>
<dt>suidperl</dt>
<dd> <tt>&quot;suidperl&quot;</tt> is no longer part of Perl. It used to provide a mechanism to emulate setuid permission bits on systems that don&#8217;t support it properly.</dd>
<dt>Use of &quot;:=&quot; to mean an empty attribute list</dt>
<dd> An accident of Perl&#8217;s parser meant that these constructions were all equivalent: </dd>
<pre>
    my $pi := 4;
    my $pi : = 4;
    my $pi :  = 4;
</pre>
<p> with the <tt>&quot;:&quot;</tt> being treated as the start of an attribute list, which ends before the <tt>&quot;=&quot;</tt>. As whitespace is not significant here, all are parsed as an empty attribute list, hence all the above are equivalent to, and better written as </p>
<pre>
    my $pi = 4;
</pre>
<p> because no attribute processing is done for an empty list. </p>
<p> As is, this meant that <tt>&quot;:=&quot;</tt> cannot be used as a new token, without silently changing the meaning of existing code. Hence that particular form is now deprecated, and will become a syntax error. If it is absolutely necessary to have empty attribute lists (for example, because of a code generator) then avoid the warning by adding a space before the <tt>&quot;=&quot;</tt>.</p>
<dt>&quot;UNIVERSAL-&gt;import()&quot;</dt>
<dd> The method <tt>&quot;UNIVERSAL-&gt;import()&quot;</tt> is now deprecated. Attempting to pass import arguments to a <tt>&quot;use UNIVERSAL&quot;</tt> statement will result in a deprecation warning.</dd>
<dt>Use of &quot;goto&quot; to jump into a construct</dt>
<dd> Using <tt>&quot;goto&quot;</tt> to jump from an outer scope into an inner scope is now deprecated. This rare use case was causing problems in the implementation of scopes.</dd>
<dt>Custom character names in \N{name} that don&#8217;t look like names</dt>
<dd> In <tt>&quot;\N{</tt>name<tt>}&quot;</tt>, <i>name</i> can be just about anything. The standard Unicode names have a very limited domain, but a custom name translator could create names that are, for example, made up entirely of punctuation symbols. It is now deprecated to make names that don&#8217;t begin with an alphabetic character, and aren&#8217;t alphanumeric or contain other than a very few other characters, namely spaces, dashes, parentheses and colons. Because of the added meaning of <tt>&quot;\N&quot;</tt> (See &quot;<tt>&quot;\N&quot;</tt> experimental regex escape&quot;), names that look like curly brace -enclosed quantifiers won&#8217;t work. For example, <tt>&quot;\N{3,4}&quot;</tt> now means to match 3 to 4 non-newlines; before a custom name <tt>&quot;3,4&quot;</tt> could have been created.</dd>
<dt>Deprecated Modules</dt>
<dd> The following modules will be removed from the core distribution in a future release, and should be installed from <font SIZE="-1">CPAN</font> instead. Distributions on <font SIZE="-1">CPAN</font> which require these should add them to their prerequisites. The core versions of these modules warnings will issue a deprecation warning. </dd>
<p> If you ship a packaged version of Perl, either alone or as part of a larger system, then you should carefully consider the repercussions of core module deprecations. You may want to consider shipping your default build of Perl with packages for some or all deprecated modules which install into <tt>&quot;vendor&quot;</tt> or <tt>&quot;site&quot;</tt> perl library directories. This will inhibit the deprecation warnings. </p>
<p> Alternatively, you may want to consider patching <i>lib/deprecate.pm</i> to provide deprecation warnings specific to your packaging system or distribution of Perl, consistent with how your packaging system or distribution manages a staged transition from a release where the installation of a single package provides the given functionality, to a later release where the system administrator needs to know to install multiple packages to get that same functionality. </p>
<p> You can silence these deprecation warnings by installing the modules in question from <font SIZE="-1">CPAN.</font> To install the latest version of all of them, just install <tt>&quot;Task::Deprecations::5_12&quot;</tt>.</p>
<dl>
<dl>
<dt>Class::ISA</dt>
<dd>
</dd><dt>Pod::Plainer</dt>
<dd>
</dd><dt>Shell</dt>
<dd>
</dd><dt>Switch</dt>
<dd> Switch is buggy and should be avoided. You may find Perl&#8217;s new <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt> feature a suitable replacement. See &#8220;Switch statements&#8221; in perlsyn for more information.</dd></dl>
</dl>
<dl>
</dl>
<dt>Assignment to $[</dt>
<dd>
</dd><dt>Use of the attribute :locked on subroutines</dt>
<dd>
</dd><dt>Use of &quot;locked&quot; with the attributes pragma</dt>
<dd>
</dd><dt>Use of &quot;unique&quot; with the attributes pragma</dt>
<dd>
</dd><dt>Perl_pmflag</dt>
<dd> <tt>&quot;Perl_pmflag&quot;</tt> is no longer part of Perl&#8217;s public <font SIZE="-1">API.</font> Calling it now generates a deprecation warning, and it will be removed in a future release. Although listed as part of the <font SIZE="-1">API,</font> it was never documented, and only ever used in <i>toke.c</i>, and prior to 5.10, <i>regcomp.c</i>. In core, it has been replaced by a static function.</dd>
<dt>Numerous Perl 4-era libraries</dt>
<dd> <i>termcap.pl</i>, <i>tainted.pl</i>, <i>stat.pl</i>, <i>shellwords.pl</i>, <i>pwd.pl</i>, <i>open3.pl</i>, <i>open2.pl</i>, <i>newgetopt.pl</i>, <i>look.pl</i>, <i>find.pl</i>, <i>finddepth.pl</i>, <i>importenv.pl</i>, <i>hostname.pl</i>, <i>getopts.pl</i>, <i>getopt.pl</i>, <i>getcwd.pl</i>, <i>flush.pl</i>, <i>fastcwd.pl</i>, <i>exceptions.pl</i>, <i>ctime.pl</i>, <i>complete.pl</i>, <i>cacheout.pl</i>, <i>bigrat.pl</i>, <i>bigint.pl</i>, <i>bigfloat.pl</i>, <i>assert.pl</i>, <i>abbrev.pl</i>, <i>dotsh.pl</i>, and <i>timelocal.pl</i> are all now deprecated. Earlier, Perl&#8217;s developers intended to remove these libraries from Perl&#8217;s core for the 5.14.0 release. </dd>
<p> During final testing before the release of 5.12.0, several developers discovered current production code using these ancient libraries, some inside the Perl core itself. Accordingly, the pumpking granted them a stay of execution. They will begin to warn about their deprecation in the 5.14.0 release and will be removed in the 5.16.0 release.</dl>
<h2>Unicode overhaul</h2>
<p> Perl&#8217;s developers have made a concerted effort to update Perl to be in sync with the latest Unicode standard. Changes for this include: </p>
<p> Perl can now handle every Unicode character property. New documentation, perluniprops, lists all available non-Unihan character properties. By default, perl does not expose Unihan, deprecated or Unicode-internal properties. See below for more details on these; there is also a section in the pod listing them, and explaining why they are not exposed. </p>
<p> Perl now fully supports the Unicode compound-style of using <tt>&quot;=&quot;</tt> and <tt>&quot;:&quot;</tt> in writing regular expressions: <tt>&quot;\p{property=value}&quot;</tt> and <tt>&quot;\p{property:value}&quot;</tt> (both of which mean the same thing). </p>
<p> Perl now fully supports the Unicode loose matching rules for text between the braces in <tt>&quot;\p{...}&quot;</tt> constructs. In addition, Perl allows underscores between digits of numbers. </p>
<p> Perl now accepts all the Unicode-defined synonyms for properties and property values. </p>
<p> <tt>&quot;qr/\X/&quot;</tt>, which matches a Unicode logical character, has been expanded to work better with various Asian languages. It now is defined as an <i>extended grapheme cluster</i>. (See &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;). Anything matched previously and that made sense will continue to be accepted. Additionally:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;\X&quot;</tt> will not break apart a <tt>&quot;CR LF&quot;</tt> sequence.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;\X&quot;</tt> will now match a sequence which includes the <tt>&quot;ZWJ&quot;</tt> and <tt>&quot;ZWNJ&quot;</tt> characters.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;\X&quot;</tt> will now always match at least one character, including an initial mark. Marks generally come after a base character, but it is possible in Unicode to have them in isolation, and <tt>&quot;\X&quot;</tt> will now handle that case, for example at the beginning of a line, or after a <tt>&quot;ZWSP&quot;</tt>. And this is the part where <tt>&quot;\X&quot;</tt> doesn&#8217;t match the things that it used to that don&#8217;t make sense. Formerly, for example, you could have the nonsensical case of an accented <font SIZE="-1">LF.</font></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;\X&quot;</tt> will now match a (Korean) Hangul syllable sequence, and the Thai and Lao exception cases.</dd></dl>
<p> Otherwise, this change should be transparent for the non-affected languages. </p>
<p> <tt>&quot;\p{...}&quot;</tt> matches using the Canonical_Combining_Class property were completely broken in previous releases of Perl. They should now work correctly. </p>
<p> Before Perl 5.12, the Unicode <tt>&quot;Decomposition_Type=Compat&quot;</tt> property and a Perl extension had the same name, which led to neither matching all the correct values (with more than 100 mistakes in one, and several thousand in the other). The Perl extension has now been renamed to be <tt>&quot;Decomposition_Type=Noncanonical&quot;</tt> (short: <tt>&quot;dt=noncanon&quot;</tt>). It has the same meaning as was previously intended, namely the union of all the non-canonical Decomposition types, with Unicode <tt>&quot;Compat&quot;</tt> being just one of those. </p>
<p> <tt>&quot;\p{Decomposition_Type=Canonical}&quot;</tt> now includes the Hangul syllables. </p>
<p> <tt>&quot;\p{Uppercase}&quot;</tt> and <tt>&quot;\p{Lowercase}&quot;</tt> now work as the Unicode standard says they should. This means they each match a few more characters than they used to. </p>
<p> <tt>&quot;\p{Cntrl}&quot;</tt> now matches the same characters as <tt>&quot;\p{Control}&quot;</tt>. This means it no longer will match Private Use (gc=co), Surrogates (gc=cs), nor Format (gc=cf) code points. The Format code points represent the biggest possible problem. All but 36 of them are either officially deprecated or strongly discouraged from being used. Of those 36, likely the most widely used are the soft hyphen (U+00AD), and <font SIZE="-1">BOM, ZWSP, ZWNJ, WJ,</font> and similar characters, plus bidirectional controls. </p>
<p> <tt>&quot;\p{Alpha}&quot;</tt> now matches the same characters as <tt>&quot;\p{Alphabetic}&quot;</tt>. Before 5.12, Perl&#8217;s definition included a number of things that aren&#8217;t really alpha (all marks) while omitting many that were. The definitions of <tt>&quot;\p{Alnum}&quot;</tt> and <tt>&quot;\p{Word}&quot;</tt> depend on Alpha&#8217;s definition and have changed accordingly. </p>
<p> <tt>&quot;\p{Word}&quot;</tt> no longer incorrectly matches non-word characters such as fractions. </p>
<p> <tt>&quot;\p{Print}&quot;</tt> no longer matches the line control characters: Tab, <font SIZE="-1">LF, CR, FF, VT,</font> and <font SIZE="-1">NEL.</font> This brings it in line with standards and the documentation. </p>
<p> <tt>&quot;\p{XDigit}&quot;</tt> now matches the same characters as <tt>&quot;\p{Hex_Digit}&quot;</tt>. This means that in addition to the characters it currently matches, <tt>&quot;[A-Fa-f0-9]&quot;</tt>, it will also match the 22 fullwidth equivalents, for example U+FF10: <font SIZE="-1">FULLWIDTH DIGIT ZERO.</font> </p>
<p> The Numeric type property has been extended to include the Unihan characters. </p>
<p> There is a new Perl extension, the &#8216;Present_In&#8217;, or simply &#8216;In&#8217;, property. This is an extension of the Unicode Age property, but <tt>&quot;\p{In=5.0}&quot;</tt> matches any code point whose usage has been determined <i>as of</i> Unicode version 5.0. The <tt>&quot;\p{Age=5.0}&quot;</tt> only matches code points added in <i>precisely</i> version 5.0. </p>
<p> A number of properties now have the correct values for unassigned code points. The affected properties are Bidi_Class, East_Asian_Width, Joining_Type, Decomposition_Type, Hangul_Syllable_Type, Numeric_Type, and Line_Break. </p>
<p> The Default_Ignorable_Code_Point, ID_Continue, and ID_Start properties are now up to date with current Unicode definitions. </p>
<p> Earlier versions of Perl erroneously exposed certain properties that are supposed to be Unicode internal-only. Use of these in regular expressions will now generate, if enabled, a deprecation warning message. The properties are: Other_Alphabetic, Other_Default_Ignorable_Code_Point, Other_Grapheme_Extend, Other_ID_Continue, Other_ID_Start, Other_Lowercase, Other_Math, and Other_Uppercase. </p>
<p> It is now possible to change which Unicode properties Perl understands on a per-installation basis. As mentioned above, certain properties are turned off by default. These include all the Unihan properties (which should be accessible via the <font SIZE="-1">CPAN</font> module Unicode::Unihan) and any deprecated or Unicode internal-only property that Perl has never exposed. </p>
<p> The generated files in the <tt>&quot;lib/unicore/To&quot;</tt> directory are now more clearly marked as being stable, directly usable by applications. New hash entries in them give the format of the normal entries, which allows for easier machine parsing. Perl can generate files in this directory for any property, though most are suppressed. You can find instructions for changing which are written in perluniprops.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> <tt>&quot;autodie&quot;</tt> is a new lexically-scoped alternative for the <tt>&quot;Fatal&quot;</tt> module. The bundled version is 2.06_01. Note that in this release, using a string eval when <tt>&quot;autodie&quot;</tt> is in effect can cause the autodie behaviour to leak into the surrounding scope. See &#8220;<font SIZE="-1">BUGS&#8221;</font> in autodie for more details. </dd>
<p> Version 2.06_01 has been added to the Perl core.</p>
<dt>&quot;Compress::Raw::Bzip2&quot;</dt>
<dd> Version 2.024 has been added to the Perl core.</dd>
<dt>&quot;overloading&quot;</dt>
<dd> <tt>&quot;overloading&quot;</tt> allows you to lexically disable or enable overloading for some or all operations. </dd>
<p> Version 0.001 has been added to the Perl core.</p>
<dt>&quot;parent&quot;</dt>
<dd> <tt>&quot;parent&quot;</tt> establishes an <font SIZE="-1">ISA</font> relationship with base classes at compile time. It provides the key feature of <tt>&quot;base&quot;</tt> without further unwanted behaviors. </dd>
<p> Version 0.223 has been added to the Perl core.</p>
<dt>&quot;Parse::CPAN::Meta&quot;</dt>
<dd> Version 1.40 has been added to the Perl core.</dd>
<dt>&quot;VMS::DCLsym&quot;</dt>
<dd> Version 1.03 has been added to the Perl core.</dd>
<dt>&quot;VMS::Stdio&quot;</dt>
<dd> Version 2.4 has been added to the Perl core.</dd>
<dt>&quot;XS::APItest::KeywordRPN&quot;</dt>
<dd> Version 0.003 has been added to the Perl core.</dd></dl>
<h3>Updated Pragmata</h3>
<dl>
<dt>&quot;base&quot;</dt>
<dd> Upgraded from version 2.13 to 2.15.</dd>
<dt>&quot;bignum&quot;</dt>
<dd> Upgraded from version 0.22 to 0.23.</dd>
<dt>&quot;charnames&quot;</dt>
<dd> <tt>&quot;charnames&quot;</tt> now contains the Unicode <i>NameAliases.txt</i> database file. This has the effect of adding some extra <tt>&quot;\N&quot;</tt> character names that formerly wouldn&#8217;t have been recognised; for example, <tt>&quot;\N{LATIN CAPITAL LETTER GHA}&quot;</tt>. </dd>
<p> Upgraded from version 1.06 to 1.07.</p>
<dt>&quot;constant&quot;</dt>
<dd> Upgraded from version 1.13 to 1.20.</dd>
<dt>&quot;diagnostics&quot;</dt>
<dd> <tt>&quot;diagnostics&quot;</tt> now supports %.0f formatting internally. </dd>
<p> <tt>&quot;diagnostics&quot;</tt> no longer suppresses <tt>&quot;Use of uninitialized value in range (or flip)&quot;</tt> warnings. [perl #71204] </p>
<p> Upgraded from version 1.17 to 1.19.</p>
<dt>&quot;feature&quot;</dt>
<dd> In <tt>&quot;feature&quot;</tt>, the meaning of the <tt>&quot;:5.10&quot;</tt> and <tt>&quot;:5.10.X&quot;</tt> feature bundles has changed slightly. The last component, if any (i.e. <tt>&quot;X&quot;</tt>) is simply ignored. This is predicated on the assumption that new features will not, in general, be added to maintenance releases. So <tt>&quot;:5.10&quot;</tt> and <tt>&quot;:5.10.X&quot;</tt> have identical effect. This is a change to the behaviour documented for 5.10.0. </dd>
<p> <tt>&quot;feature&quot;</tt> now includes the <tt>&quot;unicode_strings&quot;</tt> feature: </p>
<pre>
    use feature &quot;unicode_strings&quot;;
</pre>
<p> This pragma turns on Unicode semantics for the case-changing operations (<tt>&quot;uc&quot;</tt>, <tt>&quot;lc&quot;</tt>, <tt>&quot;ucfirst&quot;</tt>, <tt>&quot;lcfirst&quot;</tt>) on strings that don&#8217;t have the internal <font SIZE="-1">UTF-8</font> flag set, but that contain single-byte characters between 128 and 255. </p>
<p> Upgraded from version 1.11 to 1.16.</p>
<dt>&quot;less&quot;</dt>
<dd> <tt>&quot;less&quot;</tt> now includes the <tt>&quot;stash_name&quot;</tt> method to allow subclasses of <tt>&quot;less&quot;</tt> to pick where in %^H to store their stash. </dd>
<p> Upgraded from version 0.02 to 0.03.</p>
<dt>&quot;lib&quot;</dt>
<dd> Upgraded from version 0.5565 to 0.62.</dd>
<dt>&quot;mro&quot;</dt>
<dd> <tt>&quot;mro&quot;</tt> is now implemented as an <font SIZE="-1">XS</font> extension. The documented interface has not changed. Code relying on the implementation detail that some <tt>&quot;mro::&quot;</tt> methods happened to be available at all times gets to &#8220;keep both pieces&#8221;. </dd>
<p> Upgraded from version 1.00 to 1.02.</p>
<dt>&quot;overload&quot;</dt>
<dd> <tt>&quot;overload&quot;</tt> now allow overloading of &#8216;qr&#8217;. </dd>
<p> Upgraded from version 1.06 to 1.10.</p>
<dt>&quot;threads&quot;</dt>
<dd> Upgraded from version 1.67 to 1.75.</dd>
<dt>&quot;threads::shared&quot;</dt>
<dd> Upgraded from version 1.14 to 1.32.</dd>
<dt>&quot;version&quot;</dt>
<dd> <tt>&quot;version&quot;</tt> now has support for &#8220;Version number formats&#8221; as described earlier in this document and in its own documentation. </dd>
<p> Upgraded from version 0.74 to 0.82.</p>
<dt>&quot;warnings&quot;</dt>
<dd> <tt>&quot;warnings&quot;</tt> has a new <tt>&quot;warnings::fatal_enabled()&quot;</tt> function. It also includes a new <tt>&quot;illegalproto&quot;</tt> warning category. See also &#8220;New or Changed Diagnostics&#8221; for this change. </dd>
<p> Upgraded from version 1.06 to 1.09.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</dt>
<dd> Upgraded from version 0.24 to 0.38.</dd>
<dt>&quot;Archive::Tar&quot;</dt>
<dd> Upgraded from version 1.38 to 1.54.</dd>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> Upgraded from version 0.79 to 0.87.</dd>
<dt>&quot;AutoLoader&quot;</dt>
<dd> Upgraded from version 5.63 to 5.70.</dd>
<dt>&quot;B::Concise&quot;</dt>
<dd> Upgraded from version 0.74 to 0.78.</dd>
<dt>&quot;B::Debug&quot;</dt>
<dd> Upgraded from version 1.05 to 1.12.</dd>
<dt>&quot;B::Deparse&quot;</dt>
<dd> Upgraded from version 0.83 to 0.96.</dd>
<dt>&quot;B::Lint&quot;</dt>
<dd> Upgraded from version 1.09 to 1.11_01.</dd>
<dt>&quot;CGI&quot;</dt>
<dd> Upgraded from version 3.29 to 3.48.</dd>
<dt>&quot;Class::ISA&quot;</dt>
<dd> Upgraded from version 0.33 to 0.36. </dd>
<p> <font SIZE="-1">NOTE:</font> <tt>&quot;Class::ISA&quot;</tt> is deprecated and may be removed from a future version of Perl.</p>
<dt>&quot;Compress::Raw::Zlib&quot;</dt>
<dd> Upgraded from version 2.008 to 2.024.</dd>
<dt>&quot;CPAN&quot;</dt>
<dd> Upgraded from version 1.9205 to 1.94_56.</dd>
<dt>&quot;CPANPLUS&quot;</dt>
<dd> Upgraded from version 0.84 to 0.90.</dd>
<dt>&quot;CPANPLUS::Dist::Build&quot;</dt>
<dd> Upgraded from version 0.06_02 to 0.46.</dd>
<dt>&quot;Data::Dumper&quot;</dt>
<dd> Upgraded from version 2.121_14 to 2.125.</dd>
<dt>&quot;DB_File&quot;</dt>
<dd> Upgraded from version 1.816_1 to 1.820.</dd>
<dt>&quot;Devel::PPPort&quot;</dt>
<dd> Upgraded from version 3.13 to 3.19.</dd>
<dt>&quot;Digest&quot;</dt>
<dd> Upgraded from version 1.15 to 1.16.</dd>
<dt>&quot;Digest::MD5&quot;</dt>
<dd> Upgraded from version 2.36_01 to 2.39.</dd>
<dt>&quot;Digest::SHA&quot;</dt>
<dd> Upgraded from version 5.45 to 5.47.</dd>
<dt>&quot;Encode&quot;</dt>
<dd> Upgraded from version 2.23 to 2.39.</dd>
<dt>&quot;Exporter&quot;</dt>
<dd> Upgraded from version 5.62 to 5.64_01.</dd>
<dt>&quot;ExtUtils::CBuilder&quot;</dt>
<dd> Upgraded from version 0.21 to 0.27.</dd>
<dt>&quot;ExtUtils::Command&quot;</dt>
<dd> Upgraded from version 1.13 to 1.16.</dd>
<dt>&quot;ExtUtils::Constant&quot;</dt>
<dd> Upgraded from version 0.2 to 0.22.</dd>
<dt>&quot;ExtUtils::Install&quot;</dt>
<dd> Upgraded from version 1.44 to 1.55.</dd>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> Upgraded from version 6.42 to 6.56.</dd>
<dt>&quot;ExtUtils::Manifest&quot;</dt>
<dd> Upgraded from version 1.51_01 to 1.57.</dd>
<dt>&quot;ExtUtils::ParseXS&quot;</dt>
<dd> Upgraded from version 2.18_02 to 2.21.</dd>
<dt>&quot;File::Fetch&quot;</dt>
<dd> Upgraded from version 0.14 to 0.24.</dd>
<dt>&quot;File::Path&quot;</dt>
<dd> Upgraded from version 2.04 to 2.08_01.</dd>
<dt>&quot;File::Temp&quot;</dt>
<dd> Upgraded from version 0.18 to 0.22.</dd>
<dt>&quot;Filter::Simple&quot;</dt>
<dd> Upgraded from version 0.82 to 0.84.</dd>
<dt>&quot;Filter::Util::Call&quot;</dt>
<dd> Upgraded from version 1.07 to 1.08.</dd>
<dt>&quot;Getopt::Long&quot;</dt>
<dd> Upgraded from version 2.37 to 2.38.</dd>
<dt>&quot;IO&quot;</dt>
<dd> Upgraded from version 1.23_01 to 1.25_02.</dd>
<dt>&quot;IO::Zlib&quot;</dt>
<dd> Upgraded from version 1.07 to 1.10.</dd>
<dt>&quot;IPC::Cmd&quot;</dt>
<dd> Upgraded from version 0.40_1 to 0.54.</dd>
<dt>&quot;IPC::SysV&quot;</dt>
<dd> Upgraded from version 1.05 to 2.01.</dd>
<dt>&quot;Locale::Maketext&quot;</dt>
<dd> Upgraded from version 1.12 to 1.14.</dd>
<dt>&quot;Locale::Maketext::Simple&quot;</dt>
<dd> Upgraded from version 0.18 to 0.21.</dd>
<dt>&quot;Log::Message&quot;</dt>
<dd> Upgraded from version 0.01 to 0.02.</dd>
<dt>&quot;Log::Message::Simple&quot;</dt>
<dd> Upgraded from version 0.04 to 0.06.</dd>
<dt>&quot;Math::BigInt&quot;</dt>
<dd> Upgraded from version 1.88 to 1.89_01.</dd>
<dt>&quot;Math::BigInt::FastCalc&quot;</dt>
<dd> Upgraded from version 0.16 to 0.19.</dd>
<dt>&quot;Math::BigRat&quot;</dt>
<dd> Upgraded from version 0.21 to 0.24.</dd>
<dt>&quot;Math::Complex&quot;</dt>
<dd> Upgraded from version 1.37 to 1.56.</dd>
<dt>&quot;Memoize&quot;</dt>
<dd> Upgraded from version 1.01_02 to 1.01_03.</dd>
<dt>&quot;MIME::Base64&quot;</dt>
<dd> Upgraded from version 3.07_01 to 3.08.</dd>
<dt>&quot;Module::Build&quot;</dt>
<dd> Upgraded from version 0.2808_01 to 0.3603.</dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> Upgraded from version 2.12 to 2.29.</dd>
<dt>&quot;Module::Load&quot;</dt>
<dd> Upgraded from version 0.12 to 0.16.</dd>
<dt>&quot;Module::Load::Conditional&quot;</dt>
<dd> Upgraded from version 0.22 to 0.34.</dd>
<dt>&quot;Module::Loaded&quot;</dt>
<dd> Upgraded from version 0.01 to 0.06.</dd>
<dt>&quot;Module::Pluggable&quot;</dt>
<dd> Upgraded from version 3.6 to 3.9.</dd>
<dt>&quot;Net::Ping&quot;</dt>
<dd> Upgraded from version 2.33 to 2.36.</dd>
<dt>&quot;NEXT&quot;</dt>
<dd> Upgraded from version 0.60_01 to 0.64.</dd>
<dt>&quot;Object::Accessor&quot;</dt>
<dd> Upgraded from version 0.32 to 0.36.</dd>
<dt>&quot;Package::Constants&quot;</dt>
<dd> Upgraded from version 0.01 to 0.02.</dd>
<dt>&quot;PerlIO&quot;</dt>
<dd> Upgraded from version 1.04 to 1.06.</dd>
<dt>&quot;Pod::Parser&quot;</dt>
<dd> Upgraded from version 1.35 to 1.37.</dd>
<dt>&quot;Pod::Perldoc&quot;</dt>
<dd> Upgraded from version 3.14_02 to 3.15_02.</dd>
<dt>&quot;Pod::Plainer&quot;</dt>
<dd> Upgraded from version 0.01 to 1.02. </dd>
<p> <font SIZE="-1">NOTE:</font> <tt>&quot;Pod::Plainer&quot;</tt> is deprecated and may be removed from a future version of Perl.</p>
<dt>&quot;Pod::Simple&quot;</dt>
<dd> Upgraded from version 3.05 to 3.13.</dd>
<dt>&quot;Safe&quot;</dt>
<dd> Upgraded from version 2.12 to 2.22.</dd>
<dt>&quot;SelfLoader&quot;</dt>
<dd> Upgraded from version 1.11 to 1.17.</dd>
<dt>&quot;Storable&quot;</dt>
<dd> Upgraded from version 2.18 to 2.22.</dd>
<dt>&quot;Switch&quot;</dt>
<dd> Upgraded from version 2.13 to 2.16. </dd>
<p> <font SIZE="-1">NOTE:</font> <tt>&quot;Switch&quot;</tt> is deprecated and may be removed from a future version of Perl.</p>
<dt>&quot;Sys::Syslog&quot;</dt>
<dd> Upgraded from version 0.22 to 0.27.</dd>
<dt>&quot;Term::ANSIColor&quot;</dt>
<dd> Upgraded from version 1.12 to 2.02.</dd>
<dt>&quot;Term::UI&quot;</dt>
<dd> Upgraded from version 0.18 to 0.20.</dd>
<dt>&quot;Test&quot;</dt>
<dd> Upgraded from version 1.25 to 1.25_02.</dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> Upgraded from version 2.64 to 3.17.</dd>
<dt>&quot;Test::Simple&quot;</dt>
<dd> Upgraded from version 0.72 to 0.94.</dd>
<dt>&quot;Text::Balanced&quot;</dt>
<dd> Upgraded from version 2.0.0 to 2.02.</dd>
<dt>&quot;Text::ParseWords&quot;</dt>
<dd> Upgraded from version 3.26 to 3.27.</dd>
<dt>&quot;Text::Soundex&quot;</dt>
<dd> Upgraded from version 3.03 to 3.03_01.</dd>
<dt>&quot;Thread::Queue&quot;</dt>
<dd> Upgraded from version 2.00 to 2.11.</dd>
<dt>&quot;Thread::Semaphore&quot;</dt>
<dd> Upgraded from version 2.01 to 2.09.</dd>
<dt>&quot;Tie::RefHash&quot;</dt>
<dd> Upgraded from version 1.37 to 1.38.</dd>
<dt>&quot;Time::HiRes&quot;</dt>
<dd> Upgraded from version 1.9711 to 1.9719.</dd>
<dt>&quot;Time::Local&quot;</dt>
<dd> Upgraded from version 1.18 to 1.1901_01.</dd>
<dt>&quot;Time::Piece&quot;</dt>
<dd> Upgraded from version 1.12 to 1.15.</dd>
<dt>&quot;Unicode::Collate&quot;</dt>
<dd> Upgraded from version 0.52 to 0.52_01.</dd>
<dt>&quot;Unicode::Normalize&quot;</dt>
<dd> Upgraded from version 1.02 to 1.03.</dd>
<dt>&quot;Win32&quot;</dt>
<dd> Upgraded from version 0.34 to 0.39.</dd>
<dt>&quot;Win32API::File&quot;</dt>
<dd> Upgraded from version 0.1001_01 to 0.1101.</dd>
<dt>&quot;XSLoader&quot;</dt>
<dd> Upgraded from version 0.08 to 0.10.</dd></dl>
<h3>Removed Modules and Pragmata</h3>
<dl>
<dt>&quot;attrs&quot;</dt>
<dd> Removed from the Perl core. Prior version was 1.02.</dd>
<dt>&quot;CPAN::API::HOWTO&quot;</dt>
<dd> Removed from the Perl core. Prior version was &#8216;undef&#8217;.</dd>
<dt>&quot;CPAN::DeferedCode&quot;</dt>
<dd> Removed from the Perl core. Prior version was 5.50.</dd>
<dt>&quot;CPANPLUS::inc&quot;</dt>
<dd> Removed from the Perl core. Prior version was &#8216;undef&#8217;.</dd>
<dt>&quot;DCLsym&quot;</dt>
<dd> Removed from the Perl core. Prior version was 1.03.</dd>
<dt>&quot;ExtUtils::MakeMaker::bytes&quot;</dt>
<dd> Removed from the Perl core. Prior version was 6.42.</dd>
<dt>&quot;ExtUtils::MakeMaker::vmsish&quot;</dt>
<dd> Removed from the Perl core. Prior version was 6.42.</dd>
<dt>&quot;Stdio&quot;</dt>
<dd> Removed from the Perl core. Prior version was 2.3.</dd>
<dt>&quot;Test::Harness::Assert&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.02.</dd>
<dt>&quot;Test::Harness::Iterator&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.02.</dd>
<dt>&quot;Test::Harness::Point&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.01.</dd>
<dt>&quot;Test::Harness::Results&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.01.</dd>
<dt>&quot;Test::Harness::Straps&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.26_01.</dd>
<dt>&quot;Test::Harness::Util&quot;</dt>
<dd> Removed from the Perl core. Prior version was 0.01.</dd>
<dt>&quot;XSSymSet&quot;</dt>
<dd> Removed from the Perl core. Prior version was 1.1.</dd></dl>
<h3>Deprecated Modules and Pragmata</h3>
<p> See &#8220;Deprecated Modules&#8221; above.</p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<dl>
<dt>&bull;</dt>
<dd> perlhaiku contains instructions on how to build perl for the Haiku platform.</dd>
<dt>&bull;</dt>
<dd> perlmroapi describes the new interface for pluggable Method Resolution Orders.</dd>
<dt>&bull;</dt>
<dd> perlperf, by Richard Foley, provides an introduction to the use of performance and optimization techniques which can be used with particular reference to perl programs.</dd>
<dt>&bull;</dt>
<dd> perlrepository describes how to access the perl source using the <i>git</i> version control system.</dd>
<dt>&bull;</dt>
<dd> perlpolicy extends the &#8220;Social contract about contributed modules&#8221; into the beginnings of a document on Perl porting policies.</dd></dl>
<h3>Changes to Existing Documentation</h3>
<dl>
<dt>&bull;</dt>
<dd> The various large <i>Changes*</i> files (which listed every change made to perl over the last 18 years) have been removed, and replaced by a small file, also called <i>Changes</i>, which just explains how that same information may be extracted from the git version control system.</dd>
<dt>&bull;</dt>
<dd> <i>Porting/patching.pod</i> has been deleted, as it mainly described interacting with the old Perforce-based repository, which is now obsolete. Information still relevant has been moved to perlrepository.</dd>
<dt>&bull;</dt>
<dd> The syntax <tt>&quot;unless (EXPR) BLOCK else BLOCK&quot;</tt> is now documented as valid, as is the syntax <tt>&quot;unless (EXPR) BLOCK elsif (EXPR) BLOCK ... else BLOCK&quot;</tt>, although actually using the latter may not be the best idea for the readability of your source code.</dd>
<dt>&bull;</dt>
<dd> Documented -X overloading.</dd>
<dt>&bull;</dt>
<dd> Documented that <tt>&quot;when()&quot;</tt> treats specially most of the filetest operators</dd>
<dt>&bull;</dt>
<dd> Documented <tt>&quot;when&quot;</tt> as a syntax modifier.</dd>
<dt>&bull;</dt>
<dd> Eliminated &#8220;Old Perl threads tutorial&#8221;, which described 5005 threads. </dd>
<p> <i>pod/perlthrtut.pod</i> is the same material reworked for ithreads.</p>
<dt>&bull;</dt>
<dd> Correct previous documentation: v-strings are not deprecated </dd>
<p> With version objects, we need them to use <font SIZE="-1">MODULE VERSION</font> syntax. This patch removes the deprecation notice.</p>
<dt>&bull;</dt>
<dd> Security contact information is now part of perlsec.</dd>
<dt>&bull;</dt>
<dd> A significant fraction of the core documentation has been updated to clarify the behavior of Perl&#8217;s Unicode handling. </dd>
<p> Much of the remaining core documentation has been reviewed and edited for clarity, consistent use of language, and to fix the spelling of Tom Christiansen&#8217;s name.</p>
<dt>&bull;</dt>
<dd> The Pod specification (perlpodspec) has been updated to bring the specification in line with modern usage already supported by most Pod systems. A parameter string may now follow the format name in a &#8220;begin/end&#8221; region. Links to URIs with a text description are now allowed. The usage of <tt>&quot;L&lt;&quot;section&quot;&gt;&quot;</tt> has been marked as deprecated.</dd>
<dt>&bull;</dt>
<dd> if.pm has been documented in &#8220;use&#8221; in perlfunc as a means to get conditional loading of modules despite the implicit <font SIZE="-1">BEGIN</font> block around <tt>&quot;use&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> The documentation for <tt>$1</tt> in perlvar.pod has been clarified.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;\N{U+</tt>code point<tt>}&quot;</tt> is now documented.</dd></dl>
<h2>Selected Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> A new internal cache means that <tt>&quot;isa()&quot;</tt> will often be faster.</dd>
<dt>&bull;</dt>
<dd> The implementation of <tt>&quot;C3&quot;</tt> Method Resolution Order has been optimised &#8211; linearisation for classes with single inheritance is 40% faster. Performance for multiple inheritance is unchanged.</dd>
<dt>&bull;</dt>
<dd> Under <tt>&quot;use locale&quot;</tt>, the locale-relevant information is now cached on read-only values, such as the list returned by <tt>&quot;keys %hash&quot;</tt>. This makes operations such as <tt>&quot;sort keys %hash&quot;</tt> in the scope of <tt>&quot;use locale&quot;</tt> much faster.</dd>
<dt>&bull;</dt>
<dd> Empty <tt>&quot;DESTROY&quot;</tt> methods are no longer called.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Perl_sv_utf8_upgrade()&quot;</tt> is now faster.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;keys&quot;</tt> on empty hash is now faster.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;if (%foo)&quot;</tt> has been optimized to be faster than <tt>&quot;if (keys %foo)&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> The string repetition operator (<tt>&quot;$str x $num&quot;</tt>) is now several times faster when <tt>$str</tt> has length one or <tt>$num</tt> is large.</dd>
<dt>&bull;</dt>
<dd> Reversing an array to itself (as in <tt>&quot;@a = reverse @a&quot;</tt>) in void context now happens in-place and is several orders of magnitude faster than it used to be. It will also preserve non-existent elements whenever possible, i.e. for non magical arrays or tied arrays with <tt>&quot;EXISTS&quot;</tt> and <tt>&quot;DELETE&quot;</tt> methods.</dd></dl>
<h2>Installation and Configuration Improvements</h2>
<dl>
<dt>&bull;</dt>
<dd> perlapi, perlintern, perlmodlib and perltoc are now all generated at build time, rather than being shipped as part of the release.</dd>
<dt>&bull;</dt>
<dd> If <tt>&quot;vendorlib&quot;</tt> and <tt>&quot;vendorarch&quot;</tt> are the same, then they are only added to <tt>@INC</tt> once.</dd>
<dt>&bull;</dt>
<dd> <tt>$Config{usedevel}</tt> and the C-level <tt>&quot;PERL_USE_DEVEL&quot;</tt> are now defined if perl is built with <tt>&quot;-Dusedevel&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>Configure</i> will enable use of <tt>&quot;-fstack-protector&quot;</tt>, to provide protection against stack-smashing attacks, if the compiler supports it.</dd>
<dt>&bull;</dt>
<dd> <i>Configure</i> will now determine the correct prototypes for re-entrant functions and for <tt>&quot;gconvert&quot;</tt> if you are using a C<font SIZE="-2">++</font> compiler rather than a C compiler.</dd>
<dt>&bull;</dt>
<dd> On Unix, if you build from a tree containing a git repository, the configuration process will note the commit hash you have checked out, for display in the output of <tt>&quot;perl -v&quot;</tt> and <tt>&quot;perl -V&quot;</tt>. Unpushed local commits are automatically added to the list of local patches displayed by <tt>&quot;perl -V&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Perl now supports SystemTap&#8217;s <tt>&quot;dtrace&quot;</tt> compatibility layer and an issue with linking <tt>&quot;miniperl&quot;</tt> has been fixed in the process.</dd>
<dt>&bull;</dt>
<dd> perldoc now uses <tt>&quot;less -R&quot;</tt> instead of <tt>&quot;less&quot;</tt> for improved behaviour in the face of <tt>&quot;groff&quot;</tt>&#8216;s new usage of <font SIZE="-1">ANSI</font> escape codes.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;perl -V&quot;</tt> now reports use of the compile-time options <tt>&quot;USE_PERL_ATOF&quot;</tt> and <tt>&quot;USE_ATTRIBUTES_FOR_PERLIO&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> As part of the flattening of <i>ext</i>, all extensions on all platforms are built by <i>make_ext.pl</i>. This replaces the Unix-specific <i>ext/util/make_ext</i>, VMS-specific <i>make_ext.com</i> and Win32-specific <i>win32/buildext.pl</i>.</dd></dl>
<h2>Internal Changes</h2>
<p> Each release of Perl sees numerous internal changes which shouldn&#8217;t affect day to day usage but may still be notable for developers working with Perl&#8217;s source code.</p>
<dl>
<dt>&bull;</dt>
<dd> The J.R.R. Tolkien quotes at the head of C source file have been checked and proper citations added, thanks to a patch from Tom Christiansen.</dd>
<dt>&bull;</dt>
<dd> The internal structure of the dual-life modules traditionally found in the <i>lib/</i> and <i>ext/</i> directories in the perl source has changed significantly. Where possible, dual-lifed modules have been extracted from <i>lib/</i> and <i>ext/</i>. </dd>
<p> Dual-lifed modules maintained by Perl&#8217;s developers as part of the Perl core now live in <i>dist/</i>. Dual-lifed modules maintained primarily on <font SIZE="-1">CPAN</font> now live in <i>cpan/</i>. When reporting a bug in a module located under <i>cpan/</i>, please send your bug report directly to the module&#8217;s bug tracker or author, rather than Perl&#8217;s bug tracker.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;\N{...}&quot;</tt> now compiles better, always forces <font SIZE="-1">UTF-8</font> internal representation </dd>
<p> Perl&#8217;s developers have fixed several problems with the recognition of <tt>&quot;\N{...}&quot;</tt> constructs. As part of this, perl will store any scalar or regex containing <tt>&quot;\N{</tt>name<tt>}&quot;</tt> or <tt>&quot;\N{U+</tt>code point<tt>}&quot;</tt> in its definition in <font SIZE="-1">UTF-8</font> format. (This was true previously for all occurrences of <tt>&quot;\N{</tt>name<tt>}&quot;</tt> that did not use a custom translator, but now it&#8217;s always true.)</p>
<dt>&bull;</dt>
<dd> Perl_magic_setmglob now knows about globs, fixing <font SIZE="-1">RT</font> #71254.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;SVt_RV&quot;</tt> no longer exists. RVs are now stored in IVs.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Perl_vcroak()&quot;</tt> now accepts a null first argument. In addition, a full audit was made of the &#8220;not <font SIZE="-1">NULL&#8221;</font> compiler annotations, and those for several other internal functions were corrected.</dd>
<dt>&bull;</dt>
<dd> New macros <tt>&quot;dSAVEDERRNO&quot;</tt>, <tt>&quot;dSAVE_ERRNO&quot;</tt>, <tt>&quot;SAVE_ERRNO&quot;</tt>, <tt>&quot;RESTORE_ERRNO&quot;</tt> have been added to formalise the temporary saving of the <tt>&quot;errno&quot;</tt> variable.</dd>
<dt>&bull;</dt>
<dd> The function <tt>&quot;Perl_sv_insert_flags&quot;</tt> has been added to augment <tt>&quot;Perl_sv_insert&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> The function <tt>&quot;Perl_newSV_type(type)&quot;</tt> has been added, equivalent to <tt>&quot;Perl_newSV()&quot;</tt> followed by <tt>&quot;Perl_sv_upgrade(type)&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> The function <tt>&quot;Perl_newSVpvn_flags()&quot;</tt> has been added, equivalent to <tt>&quot;Perl_newSVpvn()&quot;</tt> and then performing the action relevant to the flag. </dd>
<p> Two flag bits are currently supported.</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;SVf_UTF8&quot;</tt> will call <tt>&quot;SvUTF8_on()&quot;</tt> for you. (Note that this does not convert a sequence of <font SIZE="-1">ISO 8859-1</font> characters to <font SIZE="-1">UTF-8</font>). A wrapper, <tt>&quot;newSVpvn_utf8()&quot;</tt> is available for this.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;SVs_TEMP&quot;</tt> now calls <tt>&quot;Perl_sv_2mortal()&quot;</tt> on the new <font SIZE="-1">SV.</font></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> There is also a wrapper that takes constant strings, <tt>&quot;newSVpvs_flags()&quot;</tt>.</dd></dl>
<dt>&bull;</dt>
<dd> The function <tt>&quot;Perl_croak_xs_usage&quot;</tt> has been added as a wrapper to <tt>&quot;Perl_croak&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Perl now exports the functions <tt>&quot;PerlIO_find_layer&quot;</tt> and <tt>&quot;PerlIO_list_alloc&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;PL_na&quot;</tt> has been exterminated from the core code, replaced by local <font SIZE="-1">STRLEN</font> temporaries, or <tt>&quot;*_nolen()&quot;</tt> calls. Either approach is faster than <tt>&quot;PL_na&quot;</tt>, which is a pointer dereference into the interpreter structure under ithreads, and a global variable otherwise.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Perl_mg_free()&quot;</tt> used to leave freed memory accessible via <tt>&quot;SvMAGIC()&quot;</tt> on the scalar. It now updates the linked list to remove each piece of magic as it is freed.</dd>
<dt>&bull;</dt>
<dd> Under ithreads, the regex in <tt>&quot;PL_reg_curpm&quot;</tt> is now reference counted. This eliminates a lot of hackish workarounds to cope with it not being reference counted.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Perl_mg_magical()&quot;</tt> would sometimes incorrectly turn on <tt>&quot;SvRMAGICAL()&quot;</tt>. This has been fixed.</dd>
<dt>&bull;</dt>
<dd> The <i>public</i> <font SIZE="-1">IV</font> and <font SIZE="-1">NV</font> flags are now not set if the string value has trailing &#8220;garbage&#8221;. This behaviour is consistent with not setting the public <font SIZE="-1">IV</font> or <font SIZE="-1">NV</font> flags if the value is out of range for the type.</dd>
<dt>&bull;</dt>
<dd> Uses of <tt>&quot;Nullav&quot;</tt>, <tt>&quot;Nullcv&quot;</tt>, <tt>&quot;Nullhv&quot;</tt>, <tt>&quot;Nullop&quot;</tt>, <tt>&quot;Nullsv&quot;</tt> etc have been replaced by <tt>&quot;NULL&quot;</tt> in the core code, and non-dual-life modules, as <tt>&quot;NULL&quot;</tt> is clearer to those unfamiliar with the core code.</dd>
<dt>&bull;</dt>
<dd> A macro <tt>MUTABLE_PTR(p)</tt> has been added, which on (non-pedantic) gcc will not cast away <tt>&quot;const&quot;</tt>, returning a <tt>&quot;void *&quot;</tt>. Macros <tt>&quot;MUTABLE_SV(av)&quot;</tt>, <tt>&quot;MUTABLE_SV(cv)&quot;</tt> etc build on this, casting to <tt>&quot;AV *&quot;</tt> etc without casting away <tt>&quot;const&quot;</tt>. This allows proper compile-time auditing of <tt>&quot;const&quot;</tt> correctness in the core, and helped picked up some errors (now fixed).</dd>
<dt>&bull;</dt>
<dd> Macros <tt>&quot;mPUSHs()&quot;</tt> and <tt>&quot;mXPUSHs()&quot;</tt> have been added, for pushing SVs on the stack and mortalizing them.</dd>
<dt>&bull;</dt>
<dd> Use of the private structure <tt>&quot;mro_meta&quot;</tt> has changed slightly. Nothing outside the core should be accessing this directly anyway.</dd>
<dt>&bull;</dt>
<dd> A new tool, <i>Porting/expand-macro.pl</i> has been added, that allows you to view how a C preprocessor macro would be expanded when compiled. This is handy when trying to decode the macro hell that is the perl guts.</dd></dl>
<h2>Testing</h2>
<h3>Testing improvements</h3>
<dl>
<dt>Parallel tests</dt>
<dd> The core distribution can now run its regression tests in parallel on Unix-like platforms. Instead of running <tt>&quot;make test&quot;</tt>, set <tt>&quot;TEST_JOBS&quot;</tt> in your environment to the number of tests to run in parallel, and run <tt>&quot;make test_harness&quot;</tt>. On a Bourne-like shell, this can be done as </dd>
<pre>
    TEST_JOBS=3 make test_harness  # Run 3 tests in parallel
</pre>
<p> An environment variable is used, rather than parallel make itself, because TAP::Harness needs to be able to schedule individual non-conflicting test scripts itself, and there is no standard interface to <tt>&quot;make&quot;</tt> utilities to interact with their job schedulers. </p>
<p> Note that currently some test scripts may fail when run in parallel (most notably <tt>&quot;ext/IO/t/io_dir.t&quot;</tt>). If necessary run just the failing scripts again sequentially and see if the failures go away.</p>
<dt>Test harness flexibility</dt>
<dd> It&#8217;s now possible to override <tt>&quot;PERL5OPT&quot;</tt> and friends in <i>t/TEST</i></dd>
<dt>Test watchdog</dt>
<dd> Several tests that have the potential to hang forever if they fail now incorporate a &#8220;watchdog&#8221; functionality that will kill them after a timeout, which helps ensure that <tt>&quot;make test&quot;</tt> and <tt>&quot;make test_harness&quot;</tt> run to completion automatically.</dd></dl>
<h3>New Tests</h3>
<p> Perl&#8217;s developers have added a number of new tests to the core. In addition to the items listed below, many modules updated from <font SIZE="-1">CPAN</font> incorporate new tests.</p>
<dl>
<dt>&bull;</dt>
<dd> Significant cleanups to core tests to ensure that language and interpreter features are not used before they&#8217;re tested.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;make test_porting&quot;</tt> now runs a number of important pre-commit checks which might be of use to anyone working on the Perl core.</dd>
<dt>&bull;</dt>
<dd> <i>t/porting/podcheck.t</i> automatically checks the well-formedness of <font SIZE="-1">POD</font> found in all .pl, .pm and .pod files in the <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>, other than in dual-lifed modules which are primarily maintained outside the Perl core.</dd>
<dt>&bull;</dt>
<dd> <i>t/porting/manifest.t</i> now tests that all files listed in <font SIZE="-1">MANIFEST</font> are present.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/while_readdir.t</i> tests that a bare readdir in while loop sets <tt>$_</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/comp/retainedlines.t</i> checks that the debugger can retain source lines from <tt>&quot;eval&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/io/perlio_fail.t</i> checks that bad layers fail.</dd>
<dt>&bull;</dt>
<dd> <i>t/io/perlio_leaks.t</i> checks that PerlIO layers are not leaking.</dd>
<dt>&bull;</dt>
<dd> <i>t/io/perlio_open.t</i> checks that certain special forms of open work.</dd>
<dt>&bull;</dt>
<dd> <i>t/io/perlio.t</i> includes general PerlIO tests.</dd>
<dt>&bull;</dt>
<dd> <i>t/io/pvbm.t</i> checks that there is no unexpected interaction between the internal types <tt>&quot;PVBM&quot;</tt> and <tt>&quot;PVGV&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/mro/package_aliases.t</i> checks that mro works properly in the presence of aliased packages.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/dbm.t</i> tests <tt>&quot;dbmopen&quot;</tt> and <tt>&quot;dbmclose&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/index_thr.t</i> tests the interaction of <tt>&quot;index&quot;</tt> and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/pat_thr.t</i> tests the interaction of esoteric patterns and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/qr_gc.t</i> tests that <tt>&quot;qr&quot;</tt> doesn&#8217;t leak.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/reg_email_thr.t</i> tests the interaction of regex recursion and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/regexp_qr_embed_thr.t</i> tests the interaction of patterns with embedded <tt>&quot;qr//&quot;</tt> and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/regexp_unicode_prop.t</i> tests Unicode properties in regular expressions.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/regexp_unicode_prop_thr.t</i> tests the interaction of Unicode properties and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/reg_nc_tie.t</i> tests the tied methods of <tt>&quot;Tie::Hash::NamedCapture&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/reg_posixcc.t</i> checks that <font SIZE="-1">POSIX</font> character classes behave consistently.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/re.t</i> checks that exportable <tt>&quot;re&quot;</tt> functions in <i>universal.c</i> work.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/setpgrpstack.t</i> checks that <tt>&quot;setpgrp&quot;</tt> works.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/substr_thr.t</i> tests the interaction of <tt>&quot;substr&quot;</tt> and threads.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/upgrade.t</i> checks that upgrading and assigning scalars works.</dd>
<dt>&bull;</dt>
<dd> <i>t/uni/lex_utf8.t</i> checks that Unicode in the lexer works.</dd>
<dt>&bull;</dt>
<dd> <i>t/uni/tie.t</i> checks that Unicode and <tt>&quot;tie&quot;</tt> work.</dd>
<dt>&bull;</dt>
<dd> <i>t/comp/final_line_num.t</i> tests whether line numbers are correct at <font SIZE="-1">EOF</font></dd>
<dt>&bull;</dt>
<dd> <i>t/comp/form_scope.t</i> tests format scoping.</dd>
<dt>&bull;</dt>
<dd> <i>t/comp/line_debug.t</i> tests whether <tt>&quot;@{&quot;_&lt;$file&quot;}&quot;</tt> works.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/filetest_t.t</i> tests if -t file test works.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/qr.t</i> tests <tt>&quot;qr&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/utf8cache.t</i> tests malfunctions of the utf8 cache.</dd>
<dt>&bull;</dt>
<dd> <i>t/re/uniprops.t</i> test unicodes <tt>&quot;\p{}&quot;</tt> regex constructs.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/filehandle.t</i> tests some suitably portable filetest operators to check that they work as expected, particularly in the light of some internal changes made in how filehandles are blessed.</dd>
<dt>&bull;</dt>
<dd> <i>t/op/time_loop.t</i> tests that unix times greater than <tt>&quot;2**63&quot;</tt>, which can now be handed to <tt>&quot;gmtime&quot;</tt> and <tt>&quot;localtime&quot;</tt>, do not cause an internal overflow or an excessively long loop.</dd></dl>
<h2>New or Changed Diagnostics</h2>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <font SIZE="-1">SV</font> allocation tracing has been added to the diagnostics enabled by <tt>&quot;-Dm&quot;</tt>. The tracing can alternatively output via the <tt>&quot;PERL_MEM_LOG&quot;</tt> mechanism, if that was enabled when the <i>perl</i> binary was compiled.</dd>
<dt>&bull;</dt>
<dd> Smartmatch resolution tracing has been added as a new diagnostic. Use <tt>&quot;-DM&quot;</tt> to enable it.</dd>
<dt>&bull;</dt>
<dd> A new debugging flag <tt>&quot;-DB&quot;</tt> now dumps subroutine definitions, leaving <tt>&quot;-Dx&quot;</tt> for its original purpose of dumping syntax trees.</dd>
<dt>&bull;</dt>
<dd> Perl 5.12 provides a number of new diagnostic messages to help you write better code. See perldiag for details of these new messages.</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Bad plugin affecting keyword '%s'&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;gmtime(%.0f) too large&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Lexing code attempted to stuff non-Latin-1 character into Latin-1 input&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Lexing code internal error (%s)&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;localtime(%.0f) too large&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Overloaded dereference did not return a reference&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Overloaded qr did not return a REGEXP&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Perl_pmflag() is deprecated, and will be removed from the XS API&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;lvalue attribute ignored after the subroutine has been defined&quot;</tt> </dd>
<p> This new warning is issued when one attempts to mark a subroutine as lvalue after it has been defined.</p>
<dt>&bull;</dt>
<dd> Perl now warns you if <tt>&quot;++&quot;</tt> or <tt>&quot;--&quot;</tt> are unable to change the value because it&#8217;s beyond the limit of representation. </dd>
<p> This uses a new warnings category: &#8220;imprecision&#8221;.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;lc&quot;</tt>, <tt>&quot;uc&quot;</tt>, <tt>&quot;lcfirst&quot;</tt>, and <tt>&quot;ucfirst&quot;</tt> warn when passed undef.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Show constant in &quot;Useless use of a constant in void context&quot;&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Prototype after '%s'&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;panic: sv_chop %s&quot;</tt> </dd>
<p> This new fatal error occurs when the C routine <tt>&quot;Perl_sv_chop()&quot;</tt> was passed a position that is not within the scalar&#8217;s string buffer. This could be caused by buggy <font SIZE="-1">XS</font> code, and at this point recovery is not possible.</p>
<dt>&bull;</dt>
<dd> The fatal error <tt>&quot;Malformed UTF-8 returned by \N&quot;</tt> is now produced if the <tt>&quot;charnames&quot;</tt> handler returns malformed <font SIZE="-1">UTF-8.</font></dd>
<dt>&bull;</dt>
<dd> If an unresolved named character or sequence was encountered when compiling a regex pattern then the fatal error <tt>&quot;\N{NAME} must be resolved by the lexer&quot;</tt> is now produced. This can happen, for example, when using a single-quotish context like <tt>&quot;$re = '\N{SPACE}'; /$re/;&quot;</tt>. See perldiag for more examples of how the lexer can get bypassed.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Invalid hexadecimal number in \N{U+...}&quot;</tt> is a new fatal error triggered when the character constant represented by <tt>&quot;...&quot;</tt> is not a valid hexadecimal number.</dd>
<dt>&bull;</dt>
<dd> The new meaning of <tt>&quot;\N&quot;</tt> as <tt>&quot;[^
]&quot;</tt> is not valid in a bracketed character class, just like <tt>&quot;.&quot;</tt> in a character class loses its special meaning, and will cause the fatal error <tt>&quot;\N in a character class must be a named character: \N{...}&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> The rules on what is legal for the <tt>&quot;...&quot;</tt> in <tt>&quot;\N{...}&quot;</tt> have been tightened up so that unless the <tt>&quot;...&quot;</tt> begins with an alphabetic character and continues with a combination of alphanumerics, dashes, spaces, parentheses or colons then the warning <tt>&quot;Deprecated character(s) in \N{...} starting at '%s'&quot;</tt> is now issued.</dd>
<dt>&bull;</dt>
<dd> The warning <tt>&quot;Using just the first characters returned by \N{}&quot;</tt> will be issued if the <tt>&quot;charnames&quot;</tt> handler returns a sequence of characters which exceeds the limit of the number of characters that can be used. The message will indicate which characters were used and which were discarded.</dd></dl>
</dl>
<dl>
</dl>
</dl>
<h3>Changed Diagnostics</h3>
<p> A number of existing diagnostic messages have been improved or corrected:</p>
<dl>
<dt>&bull;</dt>
<dd> A new warning category <tt>&quot;illegalproto&quot;</tt> allows finer-grained control of warnings around function prototypes. </dd>
<p> The two warnings:</p>
<dl>
<dl>
<dt>&quot;Illegal character in prototype for %s : %s&quot;</dt>
<dd>
</dd><dt>&quot;Prototype after &#8216;%c&#8217; for %s : %s&quot;</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> have been moved from the <tt>&quot;syntax&quot;</tt> top-level warnings category into a new first-level category, <tt>&quot;illegalproto&quot;</tt>. These two warnings are currently the only ones emitted during parsing of an invalid/illegal prototype, so one can now use </p>
<pre>
  no warnings 'illegalproto';
</pre>
<p> to suppress only those, but not other syntax-related warnings. Warnings where prototypes are changed, ignored, or not met are still in the <tt>&quot;prototype&quot;</tt> category as before.</dd></dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Deep recursion on subroutine &quot;%s&quot;&quot;</tt> </dd>
<p> It is now possible to change the depth threshold for this warning from the default of 100, by recompiling the <i>perl</i> binary, setting the C pre-processor macro <tt>&quot;PERL_SUB_DEPTH_WARN&quot;</tt> to the desired value.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;Illegal character in prototype&quot;</tt> warning is now more precise when reporting illegal characters after _</dd>
<dt>&bull;</dt>
<dd> mro merging error messages are now very similar to those produced by Algorithm::C3.</dd>
<dt>&bull;</dt>
<dd> Amelioration of the error message &#8220;Unrecognized character <tt>%s</tt> in column <tt>%d</tt>&#8221; </dd>
<p> Changes the error message to &#8220;Unrecognized character <tt>%s</tt>; marked by &lt;&#8211; <font SIZE="-1">HERE</font> after <tt>%s</tt>&lt;&#8211; <font SIZE="-1">HERE</font> near column <tt>%d</tt>&#8221;. This should make it a little simpler to spot and correct the suspicious character.</p>
<dt>&bull;</dt>
<dd> Perl now explicitly points to <tt>$.</tt> when it causes an uninitialized warning for ranges in scalar context.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;split&quot;</tt> now warns when called in void context.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;printf&quot;</tt>-style functions called with too few arguments will now issue the warning <tt>&quot;Missing argument in %s&quot;</tt> [perl #71000]</dd>
<dt>&bull;</dt>
<dd> Perl now properly returns a syntax error instead of segfaulting if <tt>&quot;each&quot;</tt>, <tt>&quot;keys&quot;</tt>, or <tt>&quot;values&quot;</tt> is used without an argument.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;tell()&quot;</tt> now fails properly if called without an argument and when no previous file was read. </dd>
<p> <tt>&quot;tell()&quot;</tt> now returns <tt>&quot;-1&quot;</tt>, and sets errno to <tt>&quot;EBADF&quot;</tt>, thus restoring the 5.8.x behaviour.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;overload&quot;</tt> no longer implicitly unsets fallback on repeated &#8216;use overload&#8217; lines.</dd>
<dt>&bull;</dt>
<dd> <code>POSIX::strftime()</code> can now handle Unicode characters in the format string.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;syntax&quot;</tt> category was removed from 5 warnings that should only be in <tt>&quot;deprecated&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Three fatal <tt>&quot;pack&quot;</tt>/<tt>&quot;unpack&quot;</tt> error messages have been normalized to <tt>&quot;panic: %s&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Unicode character is illegal&quot;</tt> has been rephrased to be more accurate </dd>
<p> It now reads <tt>&quot;Unicode non-character is illegal in interchange&quot;</tt> and the perldiag documentation has been expanded a bit.</p>
<dt>&bull;</dt>
<dd> Currently, all but the first of the several characters that the <tt>&quot;charnames&quot;</tt> handler may return are discarded when used in a regular expression pattern bracketed character class. If this happens then the warning <tt>&quot;Using just the first character returned by \N{} in character class&quot;</tt> will be issued.</dd>
<dt>&bull;</dt>
<dd> The warning <tt>&quot;Missing right brace on \N{} or unescaped left brace after \N. Assuming the latter&quot;</tt> will be issued if Perl encounters a <tt>&quot;\N{&quot;</tt> but doesn&#8217;t find a matching <tt>&quot;}&quot;</tt>. In this case Perl doesn&#8217;t know if it was mistakenly omitted, or if &#8220;match non-newline&#8221; followed by &quot;match a <tt>&quot;{&quot;</tt>&quot; was desired. It assumes the latter because that is actually a valid interpretation as written, unlike the other case. If you meant the former, you need to add the matching right brace. If you did mean the latter, you can silence this warning by writing instead <tt>&quot;\N\{&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;gmtime&quot;</tt> and <tt>&quot;localtime&quot;</tt> called with numbers smaller than they can reliably handle will now issue the warnings <tt>&quot;gmtime(%.0f) too small&quot;</tt> and <tt>&quot;localtime(%.0f) too small&quot;</tt>.</dd></dl>
<p> The following diagnostic messages have been removed:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Runaway format&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Can't locate package %s for the parents of %s&quot;</tt> </dd>
<p> In general this warning it only got produced in conjunction with other warnings, and removing it allowed an <font SIZE="-1">ISA</font> lookup optimisation to be added.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;v-string in use/require is non-portable&quot;</tt></dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <i>h2ph</i> now looks in <tt>&quot;include-fixed&quot;</tt> too, which is a recent addition to gcc&#8217;s search path.</dd>
<dt>&bull;</dt>
<dd> <i>h2xs</i> no longer incorrectly treats enum values like macros. It also now handles C<font SIZE="-2">++</font> style comments (<tt>&quot;//&quot;</tt>) properly in enums.</dd>
<dt>&bull;</dt>
<dd> <i>perl5db.pl</i> now supports <tt>&quot;LVALUE&quot;</tt> subroutines. Additionally, the debugger now correctly handles proxy constant subroutines, and subroutine stubs.</dd>
<dt>&bull;</dt>
<dd> <i>perlbug</i> now uses <tt>%Module::CoreList::bug_tracker</tt> to print out upstream bug tracker URLs. If a user identifies a particular module as the topic of their bug report and we&#8217;re able to divine the <font SIZE="-1">URL</font> for its upstream bug tracker, perlbug now provide a message to the user explaining that the core copies the <font SIZE="-1">CPAN</font> version directly, and provide the <font SIZE="-1">URL</font> for reporting the bug directly to the upstream author. </dd>
<p> <i>perlbug</i> no longer reports &#8220;Message sent&#8221; when it hasn&#8217;t actually sent the message</p>
<dt>&bull;</dt>
<dd> <i>perlthanks</i> is a new utility for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising. If Perl 5.12 works well for you, please try out <i>perlthanks</i>. It will make the developers smile.</dd>
<dt>&bull;</dt>
<dd> Perl&#8217;s developers have fixed bugs in <i>a2p</i> having to do with the <tt>&quot;match()&quot;</tt> operator in list context. Additionally, <i>a2p</i> no longer generates code that uses the <tt>$[</tt> variable.</dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> U+0FFFF is now a legal character in regular expressions.</dd>
<dt>&bull;</dt>
<dd> pp_qr now always returns a new regexp <font SIZE="-1">SV.</font> Resolves <font SIZE="-1">RT</font> #69852. </dd>
<p> Instead of returning a(nother) reference to the (pre-compiled) regexp in the optree, use <code>reg_temp_copy()</code> to create a copy of it, and return a reference to that. This resolves issues about Regexp::DESTROY not being called in a timely fashion (the original bug tracked by <font SIZE="-1">RT</font> #69852), as well as bugs related to blessing regexps, and of assigning to regexps, as described in correspondence added to the ticket. </p>
<p> It transpires that we also need to undo the <code>SvPVX()</code> sharing when ithreads cloning a Regexp <font SIZE="-1">SV,</font> because mother_re is set to <font SIZE="-1">NULL,</font> instead of a cloned copy of the mother_re. This change might fix bugs with regexps and threads in certain other situations, but as yet neither tests nor bug reports have indicated any problems, so it might not actually be an edge case that it&#8217;s possible to reach.</p>
<dt>&bull;</dt>
<dd> Several compilation errors and segfaults when perl was built with <tt>&quot;-Dmad&quot;</tt> were fixed.</dd>
<dt>&bull;</dt>
<dd> Fixes for lexer <font SIZE="-1">API</font> changes in 5.11.2 which broke NYTProf&#8217;s savesrc option.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;-t&quot;</tt> should only return <font SIZE="-1">TRUE</font> for file handles connected to a <font SIZE="-1">TTY</font> </dd>
<p> The Microsoft C version of <tt>&quot;isatty()&quot;</tt> returns <font SIZE="-1">TRUE</font> for all character mode devices, including the <i>/dev/null</i>-style &#8220;nul&#8221; device and printers like &#8220;lpt1&#8221;.</p>
<dt>&bull;</dt>
<dd> Fixed a regression caused by commit fafafbaf which caused a panic during parameter passing [perl #70171]</dd>
<dt>&bull;</dt>
<dd> On systems which in-place edits without backup files, -i&#8217;*&#8217; now works as the documentation says it does [perl #70802]</dd>
<dt>&bull;</dt>
<dd> Saving and restoring magic flags no longer loses readonly flag.</dd>
<dt>&bull;</dt>
<dd> The malformed syntax <tt>&quot;grep EXPR LIST&quot;</tt> (note the missing comma) no longer causes abrupt and total failure.</dd>
<dt>&bull;</dt>
<dd> Regular expressions compiled with <tt>&quot;qr{}&quot;</tt> literals properly set <tt>&quot;$'&quot;</tt> when matching again.</dd>
<dt>&bull;</dt>
<dd> Using named subroutines with <tt>&quot;sort&quot;</tt> should no longer lead to bus errors [perl #71076]</dd>
<dt>&bull;</dt>
<dd> Numerous bugfixes catch small issues caused by the recently-added Lexer <font SIZE="-1">API.</font></dd>
<dt>&bull;</dt>
<dd> Smart match against <tt>@_</tt> sometimes gave false negatives. [perl #71078]</dd>
<dt>&bull;</dt>
<dd> <tt>$@</tt> may now be assigned a read-only value (without error or busting the stack).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;sort&quot;</tt> called recursively from within an active comparison subroutine no longer causes a bus error if run multiple times. [perl #71076]</dd>
<dt>&bull;</dt>
<dd> Tie::Hash::NamedCapture::* will not abort if passed bad input (<font SIZE="-1">RT</font> #71828)</dd>
<dt>&bull;</dt>
<dd> <tt>@_</tt> and <tt>$_</tt> no longer leak under threads (<font SIZE="-1">RT</font> #34342 and #41138, also #70602, #70974)</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;-I&quot;</tt> on shebang line now adds directories in front of <tt>@INC</tt> as documented, and as does <tt>&quot;-I&quot;</tt> when specified on the command-line.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;kill&quot;</tt> is now fatal when called on non-numeric process identifiers. Previously, an <tt>&quot;undef&quot;</tt> process identifier would be interpreted as a request to kill process 0, which would terminate the current process group on <font SIZE="-1">POSIX</font> systems. Since process identifiers are always integers, killing a non-numeric process is now fatal.</dd>
<dt>&bull;</dt>
<dd> 5.10.0 inadvertently disabled an optimisation, which caused a measurable performance drop in list assignment, such as is often used to assign function parameters from <tt>@_</tt>. The optimisation has been re-instated, and the performance regression fixed. (This fix is also present in 5.10.1)</dd>
<dt>&bull;</dt>
<dd> Fixed memory leak on <tt>&quot;while (1) { map 1, 1 }&quot;</tt> [<font SIZE="-1">RT</font> #53038].</dd>
<dt>&bull;</dt>
<dd> Some potential coredumps in PerlIO fixed [<font SIZE="-1">RT</font> #57322,54828].</dd>
<dt>&bull;</dt>
<dd> The debugger now works with lvalue subroutines.</dd>
<dt>&bull;</dt>
<dd> The debugger&#8217;s <tt>&quot;m&quot;</tt> command was broken on modules that defined constants [<font SIZE="-1">RT</font> #61222].</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;crypt&quot;</tt> and string complement could return tainted values for untainted arguments [<font SIZE="-1">RT</font> #59998].</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;-i&quot;</tt><i>.suffix</i> command-line switch now recreates the file using restricted permissions, before changing its mode to match the original file. This eliminates a potential race condition [<font SIZE="-1">RT</font> #60904].</dd>
<dt>&bull;</dt>
<dd> On some Unix systems, the value in <tt>$?</tt> would not have the top bit set (<tt>&quot;$? &amp; 128&quot;</tt>) even if the child core dumped.</dd>
<dt>&bull;</dt>
<dd> Under some circumstances, <tt>$^R</tt> could incorrectly become undefined [<font SIZE="-1">RT</font> #57042].</dd>
<dt>&bull;</dt>
<dd> In the <font SIZE="-1">XS API,</font> various hash functions, when passed a pre-computed hash where the key is <font SIZE="-1">UTF-8,</font> might result in an incorrect lookup.</dd>
<dt>&bull;</dt>
<dd> <font SIZE="-1">XS</font> code including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> before <i>perl.h</i> gave a compile-time error [<font SIZE="-1">RT</font> #57176].</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;$object-&gt;isa('Foo')&quot;</tt> would report false if the package <tt>&quot;Foo&quot;</tt> didn&#8217;t exist, even if the object&#8217;s <tt>@ISA</tt> contained <tt>&quot;Foo&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Various bugs in the new-to 5.10.0 mro code, triggered by manipulating <tt>@ISA</tt>, have been found and fixed.</dd>
<dt>&bull;</dt>
<dd> Bitwise operations on references could crash the interpreter, e.g. <tt>&quot;$x=\$y; $x |= &quot;foo&quot;&quot;</tt> [<font SIZE="-1">RT</font> #54956].</dd>
<dt>&bull;</dt>
<dd> Patterns including alternation might be sensitive to the internal <font SIZE="-1">UTF-8</font> representation, e.g. </dd>
<pre><code>
my $byte = chr(192);
my $utf8 = chr(192);
utf8::upgrade($utf8);
$utf8 = ~ / $byte | X
}
/ i;
#failed in 5.10.0
</code></pre>
<dt>&bull;</dt>
<dd> Within UTF8-encoded Perl source files (i.e. where <tt>&quot;use utf8&quot;</tt> is in effect), double-quoted literal strings could be corrupted where a <tt>&quot;
</dd></dl>