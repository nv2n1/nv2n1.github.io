---

title: "perl5120delta(1)"
name: "perl5120delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5120delta/"
description: "perl5120delta – what is new for perl v5.12.0"
---

<p> perl5120delta - what is new for perl v5.12.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.10.0 release and the 5.12.0 release. </p>
<p> Many of the bug fixes in 5.12.0 are already included in the 5.10.1 maintenance release. </p>
<p> You can see the list of those changes in the 5.10.1 release notes (perl5101delta).  </p>
<h2>Core Enhancements</h2>
<h3>New package NAME VERSION syntax</h3>
<p> This new syntax allows a module author to set the <code>$VERSION</code> of a namespace when the namespace is declared with &#8216;package&#8217;. It eliminates the need for <code>&quot;our $VERSION = ...&quot;</code> and similar constructs. E.g. </p>
<pre><code>      package Foo::Bar 1.23;
      # $Foo::Bar::VERSION == 1.23
</code></pre>
<p> There are several advantages to this: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>$VERSION</code> is parsed in exactly the same way as <code>&quot;use NAME VERSION&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$VERSION</code> is set at compile time </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$VERSION</code> is a version object that provides proper overloading of comparison operators so comparing <code>$VERSION</code> to decimal (1.23) or dotted-decimal (v1.2.3) version numbers works correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Eliminates <code>&quot;$VERSION = ...&quot;</code> and <code>&quot;eval $VERSION&quot;</code> clutter </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As it requires <font SIZE="-1">VERSION</font> to be a numeric literal or v-string literal, it can be statically parsed by toolchain modules without <code>&quot;eval&quot;</code> the way <font SIZE="-1">MM-</font>&gt;parse_version does for <code>&quot;$VERSION = ...&quot;</code> </p>
 </dd></dl>
<p> It does not break old code with only <code>&quot;package NAME&quot;</code>, but code that uses <code>&quot;package NAME VERSION&quot;</code> will need to be restricted to perl 5.12.0 or newer This is analogous to the change to <code>&quot;open&quot;</code> from two-args to three-args. Users requiring the latest Perl will benefit, and perhaps after several years, it will become a standard practice. </p>
<p> However, <code>&quot;package NAME VERSION&quot;</code> requires a new, &#8216;strict&#8217; version number format. See ``Version number formats&#8217;&#8216; for details.  </p>
<h3>The ... operator</h3>
<p> A new operator, <code>&quot;...&quot;</code>, nicknamed the Yada Yada operator, has been added. It is intended to mark placeholder code that is not yet implemented. See ``Yada Yada Operator&#8217;&#8216; in perlop.  </p>
<h3>Implicit strictures</h3>
<p> Using the <code>&quot;use VERSION&quot;</code> syntax with a version number greater or equal to 5.11.0 will lexically enable strictures just like <code>&quot;use strict&quot;</code> would do (in addition to enabling features.) The following: </p>
<pre><code>    use 5.12.0;
</code></pre>
<p> means: </p>
<pre><code>    use strict;
    use feature ':5.12';
</code></pre>
<h3>Unicode improvements</h3>
<p> Perl 5.12 comes with Unicode 5.2, the latest version available to us at the time of release. This version of Unicode was released in October 2009. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.2.0">http://www.unicode.org/versions/Unicode5.2.0</a>&gt; for further details about what&#8217;s changed in this version of the standard. See perlunicode for instructions on installing and using other versions of Unicode. </p>
<p> Additionally, Perl&#8217;s developers have significantly improved Perl&#8217;s Unicode implementation. For full details, see ``Unicode overhaul&#8217;&#8216; below.  </p>
<h3>Y2038 compliance</h3>
<p> Perl&#8217;s core time-related functions are now Y2038 compliant. (It may not mean much to you, but your kids will love it!)  </p>
<h3>qr overloading</h3>
<p> It is now possible to overload the <code>&quot;qr//&quot;</code> operator, that is, conversion to regexp, like it was already possible to overload conversion to boolean, string or number of objects. It is invoked when an object appears on the right hand side of the <code>&quot;=~&quot;</code> operator or when it is interpolated into a regexp. See overload.  </p>
<h3>Pluggable keywords</h3>
<p> Extension modules can now cleanly hook into the Perl parser to define new kinds of keyword-headed expression and compound statement. The syntax following the keyword is defined entirely by the extension. This allows a completely non-Perl sublanguage to be parsed inline, with the correct ops cleanly generated. </p>
<p> See ``PL_keyword_plugin&#8217;&#8216; in perlapi for the mechanism. The Perl core source distribution also includes a new module XS::APItest::KeywordRPN, which implements reverse Polish notation arithmetic via pluggable keywords. This module is mainly used for test purposes, and is not normally installed, but also serves as an example of how to use the new mechanism. </p>
<p> Perl&#8217;s developers consider this feature to be experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.  </p>
<h3>APIs for more internals</h3>
<p> The lowest layers of the lexer and parts of the pad system now have C APIs available to <font SIZE="-1">XS</font> extensions. These are necessary to support proper use of pluggable keywords, but have other uses too. The new APIs are experimental, and only cover a small proportion of what would be necessary to take full advantage of the core&#8217;s facilities in these areas. It is intended that the Perl 5.13 development cycle will see the addition of a full range of clean, supported interfaces. </p>
<p> Perl&#8217;s developers consider this feature to be experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.  </p>
<h3>Overridable function lookup</h3>
<p> Where an extension module hooks the creation of rv2cv ops to modify the subroutine lookup process, this now works correctly for bareword subroutine calls. This means that prototypes on subroutines referenced this way will be processed correctly. (Previously bareword subroutine names were initially looked up, for parsing purposes, by an unhookable mechanism, so extensions could only properly influence subroutine names that appeared with an <code>&quot;&amp;&quot;</code> sigil.)  </p>
<h3>A proper interface for pluggable Method Resolution Orders</h3>
<p> As of Perl 5.12.0 there is a new interface for plugging and using method resolution orders other than the default linear depth first search. The C3 method resolution order added in 5.10.0 has been re-implemented as a plugin, without changing its Perl-space interface. See perlmroapi for more information.  </p>
<h3>\N experimental regex escape</h3>
<p> Perl now supports <code>&quot;\N&quot;</code>, a new regex escape which you can think of as the inverse of <code>&quot;\n&quot;</code>. It will match any character that is not a newline, independently from the presence or absence of the single line match modifier <code>&quot;/s&quot;</code>. It is not usable within a character class. <code>&quot;\N{3}&quot;</code> means to match 3 non-newlines; <code>&quot;\N{5,}&quot;</code> means to match at least 5. <code>&quot;\N{NAME}&quot;</code> still means the character or sequence named <code>&quot;NAME&quot;</code>, but <code>&quot;NAME&quot;</code> no longer can be things like <code>3</code>, or <code>&quot;5,&quot;</code>. </p>
<p> This will break a custom charnames translator which allows numbers for character names, as <code>&quot;\N{3}&quot;</code> will now mean to match 3 non-newline characters, and not the character whose name is <code>3</code>. (No name defined by the Unicode standard is a number, so only custom translators might be affected.) </p>
<p> Perl&#8217;s developers are somewhat concerned about possible user confusion with the existing <code>&quot;\N{...}&quot;</code> construct which matches characters by their Unicode name. Consequently, this feature is experimental. We may remove it or change it in a backwards-incompatible way in Perl 5.14.  </p>
<h3>DTrace support</h3>
<p> Perl now has some support for DTrace. See ``DTrace support&#8217;&#8216; in <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.  </p>
<font SIZE="-1"></font><h3>Support for configure_requires in CPAN module metadata</h3>
<p> Both <code>&quot;CPAN&quot;</code> and <code>&quot;CPANPLUS&quot;</code> now support the <code>&quot;configure_requires&quot;</code> keyword in the <i></i><font SIZE="-1"><i>META</i></font><i>.yml</i> metadata file included in most recent <font SIZE="-1">CPAN</font> distributions. This allows distribution authors to specify configuration prerequisites that must be installed before running <i>Makefile.PL</i> or <i>Build.PL</i>. </p>
<p> See the documentation for <code>&quot;ExtUtils::MakeMaker&quot;</code> or <code>&quot;Module::Build&quot;</code> for more on how to specify <code>&quot;configure_requires&quot;</code> when creating a distribution for <font SIZE="-1">CPAN.</font>  </p>
<h3>each, keys, values are now more flexible</h3>
<p> The <code>&quot;each&quot;</code>, <code>&quot;keys&quot;</code>, <code>&quot;values&quot;</code> function can now operate on arrays.  </p>
<h3>when as a statement modifier</h3>
<p> <code>&quot;when&quot;</code> is now allowed to be used as a statement modifier.  </p>
<h3>$, flexibility</h3>
<p> The variable <code>$,</code> may now be tied.  </p>
<h3>// in when clauses</h3>
<p> // now behaves like || in when clauses  </p>
<h3>Enabling warnings from your shell environment</h3>
<p> You can now set <code>&quot;-W&quot;</code> from the <code>&quot;PERL5OPT&quot;</code> environment variable  </p>
<h3>delete local</h3>
<p> <code>&quot;delete local&quot;</code> now allows you to locally delete a hash entry.  </p>
<h3>New support for Abstract namespace sockets</h3>
<p> Abstract namespace sockets are Linux-specific socket type that live in <font SIZE="-1">AF_UNIX</font> family, slightly abusing it to be able to use arbitrary character arrays as addresses: They start with nul byte and are not terminated by nul byte, but with the length passed to the <code>socket()</code> system call.  </p>
<h3>32-bit limit on substr arguments removed</h3>
<p> The 32-bit limit on <code>&quot;substr&quot;</code> arguments has now been removed. The full range of the system&#8217;s signed and unsigned integers is now available for the <code>&quot;pos&quot;</code> and <code>&quot;len&quot;</code> arguments.  </p>
<h2>Potentially Incompatible Changes</h2>
<h3>Deprecations warn by default</h3>
<p> Over the years, Perl&#8217;s developers have deprecated a number of language features for a variety of reasons. Perl now defaults to issuing a warning if a deprecated language feature is used. Many of the deprecations Perl now warns you about have been deprecated for many years. You can find a list of what was deprecated in a given release of Perl in the <code>&quot;perl5xxdelta.pod&quot;</code> file for that release. </p>
<p> To disable this feature in a given lexical scope, you should use <code>&quot;no warnings &#8216;deprecated&#8217;;&quot;</code> For information about which language features are deprecated and explanations of various deprecation warnings, please see perldiag. See ``Deprecations&#8217;&#8216; below for the list of features and modules Perl&#8217;s developers have deprecated as part of this release.  </p>
<h3>Version number formats</h3>
<p> Acceptable version number formats have been formalized into ``strict&#8217;&#8216; and ``lax&#8217;&#8216; rules. <code>&quot;package NAME VERSION&quot;</code> takes a strict version number. <code>&quot;UNIVERSAL::VERSION&quot;</code> and the version object constructors take lax version numbers. Providing an invalid version will result in a fatal error. The version argument in <code>&quot;use NAME VERSION&quot;</code> is first parsed as a numeric literal or v-string and then passed to <code>&quot;UNIVERSAL::VERSION&quot;</code> (and must then pass the ``lax&#8217;&#8216; format test). </p>
<p> These formats are documented fully in the version module. To a first approximation, a ``strict&#8217;&#8216; version number is a positive decimal number (integer or decimal-fraction) without exponentiation or else a dotted-decimal v-string with a leading &#8216;v&#8217; character and at least three components. A ``lax&#8217;&#8216; version number allows v-strings with fewer than three components or without a leading &#8216;v&#8217;. Under ``lax&#8217;&#8216; rules, both decimal and dotted-decimal versions may have a trailing ``alpha&#8217;&#8216; component separated by an underscore character after a fractional or dotted-decimal component. </p>
<p> The version module adds <code>&quot;version::is_strict&quot;</code> and <code>&quot;version::is_lax&quot;</code> functions to check a scalar against these rules.  </p>
<h3>@INC reorganization</h3>
<p> In <code>@INC</code>, <code>&quot;ARCHLIB&quot;</code> and <code>&quot;PRIVLIB&quot;</code> now occur after the current version&#8217;s <code>&quot;site_perl&quot;</code> and <code>&quot;vendor_perl&quot;</code>. Modules installed into <code>&quot;site_perl&quot;</code> and <code>&quot;vendor_perl&quot;</code> will now be loaded in preference to those installed in <code>&quot;ARCHLIB&quot;</code> and <code>&quot;PRIVLIB&quot;</code>.  </p>
<h3>REGEXPs are now first class</h3>
<p> Internally, Perl now treats compiled regular expressions (such as those created with <code>&quot;qr//&quot;</code>) as first class entities. Perl modules which serialize, deserialize or otherwise have deep interaction with Perl&#8217;s internal data structures need to be updated for this change. Most affected <font SIZE="-1">CPAN</font> modules have already been updated as of this writing.  </p>
<h3>Switch statement changes</h3>
<p> The <code>&quot;given&quot;</code>/<code>&quot;when&quot;</code> switch statement handles complex statements better than Perl 5.10.0 did (These enhancements are also available in 5.10.1 and subsequent 5.10 releases.) There are two new cases where <code>&quot;when&quot;</code> now interprets its argument as a boolean, instead of an expression to be used in a smart match: </p>
<dl>
<dt>flip-flop operators</dt>
<dd> <p> The <code>&quot;..&quot;</code> and <code>&quot;...&quot;</code> flip-flop operators are now evaluated in boolean context, following their usual semantics; see ``Range Operators&#8217;&#8216; in perlop. </p>
<p> Note that, as in perl 5.10.0, <code>&quot;when (1..10)&quot;</code> will not work to test whether a given value is an integer between 1 and 10; you should use <code>&quot;when ([1..10])&quot;</code> instead (note the array reference). </p>
<p> However, contrary to 5.10.0, evaluating the flip-flop operators in boolean context ensures it can now be useful in a <code>&quot;when()&quot;</code>, notably for implementing bistable conditions, like in: </p>
<pre><code>    when (/^=begin/ .. /^=end/) {
      # do something
    }
</code></pre>
 </dd>
<dt>defined-or operator</dt>
<dd> <p> A compound expression involving the defined-or operator, as in <code>&quot;when (expr1 // expr2)&quot;</code>, will be treated as boolean if the first expression is boolean. (This just extends the existing rule that applies to the regular or operator, as in <code>&quot;when (expr1 || expr2)&quot;</code>.) </p>
 </dd></dl>
<h3>Smart match changes</h3>
<p> Since Perl 5.10.0, Perl&#8217;s developers have made a number of changes to the smart match operator. These, of course, also alter the behaviour of the switch statements where smart matching is implicitly used. These changes were also made for the 5.10.1 release, and will remain in subsequent 5.10 releases. </p>
<p> <i>Changes to type-based dispatch</i> </p>
<p> The smart match operator <code>&quot;~~&quot;</code> is no longer commutative. The behaviour of a smart match now depends primarily on the type of its right hand argument. Moreover, its semantics have been adjusted for greater consistency or usefulness in several cases. While the general backwards compatibility is maintained, several changes must be noted: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Code references with an empty prototype are no longer treated specially. They are passed an argument like the other code references (even if they choose to ignore it). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;%hash ~~ sub {}&quot;</code> and <code>&quot;@array ~~ sub {}&quot;</code> now test that the subroutine returns a true value for each key of the hash (or element of the array), instead of passing the whole hash or array as a reference to the subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Due to the commutativity breakage, code references are no longer treated specially when appearing on the left of the <code>&quot;~~&quot;</code> operator, but like any vulgar scalar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef ~~ %hash&quot;</code> is always false (since <code>&quot;undef&quot;</code> can&#8217;t be a key in a hash). No implicit conversion to <code>&quot;&quot;</code> is done (as was the case in perl 5.10.0). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$scalar ~~ @array&quot;</code> now always distributes the smart match across the elements of the array. It&#8217;s true if one element in <code>@array</code> verifies <code>&quot;$scalar ~~ $element&quot;</code>. This is a generalization of the old behaviour that tested whether the array contained the scalar. </p>
 </dd></dl>
<p> The full dispatch table for the smart match operator is given in ``Smart matching in detail&#8217;&#8216; in perlsyn. </p>
<p> <i>Smart match and overloading</i> </p>
<p> According to the rule of dispatch based on the rightmost argument type, when an object overloading <code>&quot;~~&quot;</code> appears on the right side of the operator, the overload routine will always be called (with a 3rd argument set to a true value, see overload.) However, when the object will appear on the left, the overload routine will be called only when the rightmost argument is a simple scalar. This way, distributivity of smart match across arrays is not broken, as well as the other behaviours with complex types (coderefs, hashes, regexes). Thus, writers of overloading routines for smart match mostly need to worry only with comparing against a scalar, and possibly with stringification overloading; the other common cases will be automatically handled consistently. </p>
<p> <code>&quot;~~&quot;</code> will now refuse to work on objects that do not overload it (in order to avoid relying on the object&#8217;s underlying structure). (However, if the object overloads the stringification or the numification operators, and if overload fallback is active, it will be used instead, as usual.)  </p>
<h3>Other potentially incompatible changes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The definitions of a number of Unicode properties have changed to match those of the current Unicode standard. These are listed above under ``Unicode overhaul&#8217;&#8216;. This change may break code that expects the old definitions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The boolkeys op has moved to the group of hash ops. This breaks binary compatibility. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filehandles are now always blessed into <code>&quot;IO::File&quot;</code>. </p>
<p> The previous behaviour was to bless Filehandles into FileHandle (an empty proxy class) if it was loaded into memory and otherwise to bless them into <code>&quot;IO::Handle&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The semantics of <code>&quot;use feature :5.10*&quot;</code> have changed slightly. See ``Modules and Pragmata&#8217;&#8216; for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s developers now use git, rather than Perforce. This should be a purely internal change only relevant to people actively working on the core. However, you may see minor difference in perl as a consequence of the change. For example in some of details of the output of <code>&quot;perl -V&quot;</code>. See perlrepository for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As part of the <code>&quot;Test::Harness&quot;</code> 2.x to 3.x upgrade, the experimental <code>&quot;Test::Harness::Straps&quot;</code> module has been removed. See ``Modules and Pragmata&#8217;&#8216; for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As part of the <code>&quot;ExtUtils::MakeMaker&quot;</code> upgrade, the <code>&quot;ExtUtils::MakeMaker::bytes&quot;</code> and <code>&quot;ExtUtils::MakeMaker::vmsish&quot;</code> modules have been removed from this distribution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::CoreList&quot;</code> no longer contains the <code>%:patchlevel</code> hash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length undef&quot;</code> now returns undef. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unsupported private C <font SIZE="-1">API</font> functions are now declared ``static&#8217;&#8216; to prevent leakage to Perl&#8217;s public <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To support the bootstrapping process, <i>miniperl</i> no longer builds with <font SIZE="-1">UTF-8</font> support in the regexp engine. </p>
<p> This allows a build to complete with <font SIZE="-1">PERL_UNICODE</font> set and a <font SIZE="-1">UTF-8</font> locale. Without this there&#8217;s a bootstrapping problem, as miniperl can&#8217;t load the <font SIZE="-1">UTF-8</font> components of the regexp engine, because they&#8217;re not yet built. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>miniperl</i>&#8216;s <code>@INC</code> is now restricted to just <code>&quot;-I...&quot;</code>, the split of <code>$ENV{PERL5LIB}</code>, and &quot;<code>&quot;.&quot;</code>&quot; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A space or a newline is now required after a <code>&quot;#line XXX&quot;</code> directive. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tied filehandles now have an additional method <font SIZE="-1">EOF</font> which provides the <font SIZE="-1">EOF</font> type. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> To better match all other flow control statements, <code>&quot;foreach&quot;</code> may no longer be used as an attribute. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s command-line switch ``-P&#8217;&#8216;, which was deprecated in version 5.10.0, has now been removed. The <font SIZE="-1">CPAN</font> module <code>&quot;Filter::cpp&quot;</code> can be used as an alternative. </p>
 </dd></dl>
<h2>Deprecations</h2>
<p> From time to time, Perl&#8217;s developers find it necessary to deprecate features or modules we&#8217;ve previously shipped as part of the core distribution. We are well aware of the pain and frustration that a backwards-incompatible change to Perl can cause for developers building or maintaining software in Perl. You can be sure that when we deprecate a functionality or syntax, it isn&#8217;t a choice we make lightly. Sometimes, we choose to deprecate functionality or syntax because it was found to be poorly designed or implemented. Sometimes, this is because they&#8217;re holding back other features or causing performance problems. Sometimes, the reasons are more complex. Wherever possible, we try to keep deprecated functionality available to developers in its previous form for at least one major release. So long as a deprecated feature isn&#8217;t actively disrupting our ability to maintain and extend Perl, we&#8217;ll try to leave it in place as long as possible. </p>
<p> The following items are now deprecated: </p>
<dl>
<dt>suidperl</dt>
<dd> <p> <code>&quot;suidperl&quot;</code> is no longer part of Perl. It used to provide a mechanism to emulate setuid permission bits on systems that don&#8217;t support it properly. </p>
 </dd>
<dt>Use of &quot;:=&quot; to mean an empty attribute list</dt>
<dd> <p> An accident of Perl&#8217;s parser meant that these constructions were all equivalent: </p>
<pre><code>    my $pi := 4;
    my $pi : = 4;
    my $pi : = 4;
</code></pre>
<p> with the <code>&quot;:&quot;</code> being treated as the start of an attribute list, which ends before the <code>&quot;=&quot;</code>. As whitespace is not significant here, all are parsed as an empty attribute list, hence all the above are equivalent to, and better written as </p>
<pre><code>    my $pi = 4;
</code></pre>
<p> because no attribute processing is done for an empty list. </p>
<p> As is, this meant that <code>&quot;:=&quot;</code> cannot be used as a new token, without silently changing the meaning of existing code. Hence that particular form is now deprecated, and will become a syntax error. If it is absolutely necessary to have empty attribute lists (for example, because of a code generator) then avoid the warning by adding a space before the <code>&quot;=&quot;</code>. </p>
 </dd>
<dt>&quot;UNIVERSAL-&gt;import()&quot;</dt>
<dd> <p> The method <code>&quot;UNIVERSAL-&gt;import()&quot;</code> is now deprecated. Attempting to pass import arguments to a <code>&quot;use UNIVERSAL&quot;</code> statement will result in a deprecation warning. </p>
 </dd>
<dt>Use of &quot;goto&quot; to jump into a construct</dt>
<dd> <p> Using <code>&quot;goto&quot;</code> to jump from an outer scope into an inner scope is now deprecated. This rare use case was causing problems in the implementation of scopes. </p>
 </dd>
<dt>Custom character names in \N{name} that don&#8217;t look like names</dt>
<dd> <p> In <code>&quot;\N{</code>name <code>}&quot;</code>, <i>name</i> can be just about anything. The standard Unicode names have a very limited domain, but a custom name translator could create names that are, for example, made up entirely of punctuation symbols. It is now deprecated to make names that don&#8217;t begin with an alphabetic character, and aren&#8217;t alphanumeric or contain other than a very few other characters, namely spaces, dashes, parentheses and colons. Because of the added meaning of <code>&quot;\N&quot;</code> (See &quot;<code>&quot;\N&quot;</code> experimental regex escape&quot;), names that look like curly brace -enclosed quantifiers won&#8217;t work. For example, <code>&quot;\N{3,4}&quot;</code> now means to match 3 to 4 non-newlines; before a custom name <code>&quot;3,4&quot;</code> could have been created. </p>
 </dd>
<dt>Deprecated Modules</dt>
<dd> <p> The following modules will be removed from the core distribution in a future release, and should be installed from <font SIZE="-1">CPAN</font> instead. Distributions on <font SIZE="-1">CPAN</font> which require these should add them to their prerequisites. The core versions of these modules warnings will issue a deprecation warning. </p>
<p> If you ship a packaged version of Perl, either alone or as part of a larger system, then you should carefully consider the repercussions of core module deprecations. You may want to consider shipping your default build of Perl with packages for some or all deprecated modules which install into <code>&quot;vendor&quot;</code> or <code>&quot;site&quot;</code> perl library directories. This will inhibit the deprecation warnings. </p>
<p> Alternatively, you may want to consider patching <i>lib/deprecate.pm</i> to provide deprecation warnings specific to your packaging system or distribution of Perl, consistent with how your packaging system or distribution manages a staged transition from a release where the installation of a single package provides the given functionality, to a later release where the system administrator needs to know to install multiple packages to get that same functionality. </p>
<p> You can silence these deprecation warnings by installing the modules in question from <font SIZE="-1">CPAN.</font> To install the latest version of all of them, just install <code>&quot;Task::Deprecations::5_12&quot;</code>. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>Class::ISA</dt>
<dd>  </dd>
<dt>Pod::Plainer</dt>
<dd>  </dd>
<dt>Shell</dt>
<dd>  </dd>
<dt>Switch</dt>
<dd> <p> Switch is buggy and should be avoided. You may find Perl&#8217;s new <code>&quot;given&quot;</code>/<code>&quot;when&quot;</code> feature a suitable replacement. See ``Switch statements&#8217;&#8216; in perlsyn for more information. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Assignment to $[</dt>
<dd>  </dd>
<dt>Use of the attribute :locked on subroutines</dt>
<dd>  </dd>
<dt>Use of &quot;locked&quot; with the attributes pragma</dt>
<dd>  </dd>
<dt>Use of &quot;unique&quot; with the attributes pragma</dt>
<dd>  </dd>
<dt>Perl_pmflag</dt>
<dd> <p> <code>&quot;Perl_pmflag&quot;</code> is no longer part of Perl&#8217;s public <font SIZE="-1">API.</font> Calling it now generates a deprecation warning, and it will be removed in a future release. Although listed as part of the <font SIZE="-1">API,</font> it was never documented, and only ever used in <i>toke.c</i>, and prior to 5.10, <i>regcomp.c</i>. In core, it has been replaced by a static function. </p>
 </dd>
<dt>Numerous Perl 4-era libraries</dt>
<dd> <p> <i>termcap.pl</i>, <i>tainted.pl</i>, <i>stat.pl</i>, <i>shellwords.pl</i>, <i>pwd.pl</i>, <i>open3.pl</i>, <i>open2.pl</i>, <i>newgetopt.pl</i>, <i>look.pl</i>, <i>find.pl</i>, <i>finddepth.pl</i>, <i>importenv.pl</i>, <i>hostname.pl</i>, <i>getopts.pl</i>, <i>getopt.pl</i>, <i>getcwd.pl</i>, <i>flush.pl</i>, <i>fastcwd.pl</i>, <i>exceptions.pl</i>, <i>ctime.pl</i>, <i>complete.pl</i>, <i>cacheout.pl</i>, <i>bigrat.pl</i>, <i>bigint.pl</i>, <i>bigfloat.pl</i>, <i>assert.pl</i>, <i>abbrev.pl</i>, <i>dotsh.pl</i>, and <i>timelocal.pl</i> are all now deprecated. Earlier, Perl&#8217;s developers intended to remove these libraries from Perl&#8217;s core for the 5.14.0 release. </p>
<p> During final testing before the release of 5.12.0, several developers discovered current production code using these ancient libraries, some inside the Perl core itself. Accordingly, the pumpking granted them a stay of execution. They will begin to warn about their deprecation in the 5.14.0 release and will be removed in the 5.16.0 release. </p>
 </dd></dl>
<h2>Unicode overhaul</h2>
<p> Perl&#8217;s developers have made a concerted effort to update Perl to be in sync with the latest Unicode standard. Changes for this include: </p>
<p> Perl can now handle every Unicode character property. New documentation, perluniprops, lists all available non-Unihan character properties. By default, perl does not expose Unihan, deprecated or Unicode-internal properties. See below for more details on these; there is also a section in the pod listing them, and explaining why they are not exposed. </p>
<p> Perl now fully supports the Unicode compound-style of using <code>&quot;=&quot;</code> and <code>&quot;:&quot;</code> in writing regular expressions: <code>&quot;\p{property=value}&quot;</code> and <code>&quot;\p{property:value}&quot;</code> (both of which mean the same thing). </p>
<p> Perl now fully supports the Unicode loose matching rules for text between the braces in <code>&quot;\p{...}&quot;</code> constructs. In addition, Perl allows underscores between digits of numbers. </p>
<p> Perl now accepts all the Unicode-defined synonyms for properties and property values. </p>
<p> <code>&quot;qr/\X/&quot;</code>, which matches a Unicode logical character, has been expanded to work better with various Asian languages. It now is defined as an <i>extended grapheme cluster</i>. (See &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;). Anything matched previously and that made sense will continue to be accepted. Additionally: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\X&quot;</code> will not break apart a <code>&quot;CR LF&quot;</code> sequence. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\X&quot;</code> will now match a sequence which includes the <code>&quot;ZWJ&quot;</code> and <code>&quot;ZWNJ&quot;</code> characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\X&quot;</code> will now always match at least one character, including an initial mark. Marks generally come after a base character, but it is possible in Unicode to have them in isolation, and <code>&quot;\X&quot;</code> will now handle that case, for example at the beginning of a line, or after a <code>&quot;ZWSP&quot;</code>. And this is the part where <code>&quot;\X&quot;</code> doesn&#8217;t match the things that it used to that don&#8217;t make sense. Formerly, for example, you could have the nonsensical case of an accented <font SIZE="-1">LF.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\X&quot;</code> will now match a (Korean) Hangul syllable sequence, and the Thai and Lao exception cases. </p>
 </dd></dl>
<p> Otherwise, this change should be transparent for the non-affected languages. </p>
<p> <code>&quot;\p{...}&quot;</code> matches using the Canonical_Combining_Class property were completely broken in previous releases of Perl. They should now work correctly. </p>
<p> Before Perl 5.12, the Unicode <code>&quot;Decomposition_Type=Compat&quot;</code> property and a Perl extension had the same name, which led to neither matching all the correct values (with more than 100 mistakes in one, and several thousand in the other). The Perl extension has now been renamed to be <code>&quot;Decomposition_Type=Noncanonical&quot;</code> (short: <code>&quot;dt=noncanon&quot;</code>). It has the same meaning as was previously intended, namely the union of all the non-canonical Decomposition types, with Unicode <code>&quot;Compat&quot;</code> being just one of those. </p>
<p> <code>&quot;\p{Decomposition_Type=Canonical}&quot;</code> now includes the Hangul syllables. </p>
<p> <code>&quot;\p{Uppercase}&quot;</code> and <code>&quot;\p{Lowercase}&quot;</code> now work as the Unicode standard says they should. This means they each match a few more characters than they used to. </p>
<p> <code>&quot;\p{Cntrl}&quot;</code> now matches the same characters as <code>&quot;\p{Control}&quot;</code>. This means it no longer will match Private Use (gc=co), Surrogates (gc=cs), nor Format (gc=cf) code points. The Format code points represent the biggest possible problem. All but 36 of them are either officially deprecated or strongly discouraged from being used. Of those 36, likely the most widely used are the soft hyphen (U+00AD), and <font SIZE="-1">BOM, ZWSP, ZWNJ, WJ,</font> and similar characters, plus bidirectional controls. </p>
<p> <code>&quot;\p{Alpha}&quot;</code> now matches the same characters as <code>&quot;\p{Alphabetic}&quot;</code>. Before 5.12, Perl&#8217;s definition included a number of things that aren&#8217;t really alpha (all marks) while omitting many that were. The definitions of <code>&quot;\p{Alnum}&quot;</code> and <code>&quot;\p{Word}&quot;</code> depend on Alpha&#8217;s definition and have changed accordingly. </p>
<p> <code>&quot;\p{Word}&quot;</code> no longer incorrectly matches non-word characters such as fractions. </p>
<p> <code>&quot;\p{Print}&quot;</code> no longer matches the line control characters: Tab, <font SIZE="-1">LF, CR, FF, VT,</font> and <font SIZE="-1">NEL.</font> This brings it in line with standards and the documentation. </p>
<p> <code>&quot;\p{XDigit}&quot;</code> now matches the same characters as <code>&quot;\p{Hex_Digit}&quot;</code>. This means that in addition to the characters it currently matches, <code>&quot;[A-Fa-f0-9]&quot;</code>, it will also match the 22 fullwidth equivalents, for example U+FF10: <font SIZE="-1">FULLWIDTH DIGIT ZERO.</font> </p>
<p> The Numeric type property has been extended to include the Unihan characters. </p>
<p> There is a new Perl extension, the &#8216;Present_In&#8217;, or simply &#8216;In&#8217;, property. This is an extension of the Unicode Age property, but <code>&quot;\p{In=5.0}&quot;</code> matches any code point whose usage has been determined <i>as of</i> Unicode version 5.0. The <code>&quot;\p{Age=5.0}&quot;</code> only matches code points added in <i>precisely</i> version 5.0. </p>
<p> A number of properties now have the correct values for unassigned code points. The affected properties are Bidi_Class, East_Asian_Width, Joining_Type, Decomposition_Type, Hangul_Syllable_Type, Numeric_Type, and Line_Break. </p>
<p> The Default_Ignorable_Code_Point, ID_Continue, and ID_Start properties are now up to date with current Unicode definitions. </p>
<p> Earlier versions of Perl erroneously exposed certain properties that are supposed to be Unicode internal-only. Use of these in regular expressions will now generate, if enabled, a deprecation warning message. The properties are: Other_Alphabetic, Other_Default_Ignorable_Code_Point, Other_Grapheme_Extend, Other_ID_Continue, Other_ID_Start, Other_Lowercase, Other_Math, and Other_Uppercase. </p>
<p> It is now possible to change which Unicode properties Perl understands on a per-installation basis. As mentioned above, certain properties are turned off by default. These include all the Unihan properties (which should be accessible via the <font SIZE="-1">CPAN</font> module Unicode::Unihan) and any deprecated or Unicode internal-only property that Perl has never exposed. </p>
<p> The generated files in the <code>&quot;lib/unicore/To&quot;</code> directory are now more clearly marked as being stable, directly usable by applications. New hash entries in them give the format of the normal entries, which allows for easier machine parsing. Perl can generate files in this directory for any property, though most are suppressed. You can find instructions for changing which are written in perluniprops.  </p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&quot;autodie&quot;</dt>
<dd> <p> <code>&quot;autodie&quot;</code> is a new lexically-scoped alternative for the <code>&quot;Fatal&quot;</code> module. The bundled version is 2.06_01. Note that in this release, using a string eval when <code>&quot;autodie&quot;</code> is in effect can cause the autodie behaviour to leak into the surrounding scope. See ``<font SIZE="-1">BUGS&#8217;&#8216;</font> in autodie for more details. </p>
<p> Version 2.06_01 has been added to the Perl core. </p>
 </dd>
<dt>&quot;Compress::Raw::Bzip2&quot;</dt>
<dd> <p> Version 2.024 has been added to the Perl core. </p>
 </dd>
<dt>&quot;overloading&quot;</dt>
<dd> <p> <code>&quot;overloading&quot;</code> allows you to lexically disable or enable overloading for some or all operations. </p>
<p> Version 0.001 has been added to the Perl core. </p>
 </dd>
<dt>&quot;parent&quot;</dt>
<dd> <p> <code>&quot;parent&quot;</code> establishes an <font SIZE="-1">ISA</font> relationship with base classes at compile time. It provides the key feature of <code>&quot;base&quot;</code> without further unwanted behaviors. </p>
<p> Version 0.223 has been added to the Perl core. </p>
 </dd>
<dt>&quot;Parse::CPAN::Meta&quot;</dt>
<dd> <p> Version 1.40 has been added to the Perl core. </p>
 </dd>
<dt>&quot;VMS::DCLsym&quot;</dt>
<dd> <p> Version 1.03 has been added to the Perl core. </p>
 </dd>
<dt>&quot;VMS::Stdio&quot;</dt>
<dd> <p> Version 2.4 has been added to the Perl core. </p>
 </dd>
<dt>&quot;XS::APItest::KeywordRPN&quot;</dt>
<dd> <p> Version 0.003 has been added to the Perl core. </p>
 </dd></dl>
<h3>Updated Pragmata</h3>
<dl>
<dt>&quot;base&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.15. </p>
 </dd>
<dt>&quot;bignum&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.23. </p>
 </dd>
<dt>&quot;charnames&quot;</dt>
<dd> <p> <code>&quot;charnames&quot;</code> now contains the Unicode <i>NameAliases.txt</i> database file. This has the effect of adding some extra <code>&quot;\N&quot;</code> character names that formerly wouldn&#8217;t have been recognised; for example, <code>&quot;\N{LATIN CAPITAL LETTER GHA}&quot;</code>. </p>
<p> Upgraded from version 1.06 to 1.07. </p>
 </dd>
<dt>&quot;constant&quot;</dt>
<dd> <p> Upgraded from version 1.13 to 1.20. </p>
 </dd>
<dt>&quot;diagnostics&quot;</dt>
<dd> <p> <code>&quot;diagnostics&quot;</code> now supports %.0f formatting internally. </p>
<p> <code>&quot;diagnostics&quot;</code> no longer suppresses <code>&quot;Use of uninitialized value in range (or flip)&quot;</code> warnings. [perl #71204] </p>
<p> Upgraded from version 1.17 to 1.19. </p>
 </dd>
<dt>&quot;feature&quot;</dt>
<dd> <p> In <code>&quot;feature&quot;</code>, the meaning of the <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> feature bundles has changed slightly. The last component, if any (i.e. <code>&quot;X&quot;</code>) is simply ignored. This is predicated on the assumption that new features will not, in general, be added to maintenance releases. So <code>&quot;:5.10&quot;</code> and <code>&quot;:5.10.X&quot;</code> have identical effect. This is a change to the behaviour documented for 5.10.0. </p>
<p> <code>&quot;feature&quot;</code> now includes the <code>&quot;unicode_strings&quot;</code> feature: </p>
<pre><code>    use feature &quot;unicode_strings&quot;;
</code></pre>
<p> This pragma turns on Unicode semantics for the case-changing operations (<code>&quot;uc&quot;</code>, <code>&quot;lc&quot;</code>, <code>&quot;ucfirst&quot;</code>, <code>&quot;lcfirst&quot;</code>) on strings that don&#8217;t have the internal <font SIZE="-1">UTF-8</font> flag set, but that contain single-byte characters between 128 and 255. </p>
<p> Upgraded from version 1.11 to 1.16. </p>
 </dd>
<dt>&quot;less&quot;</dt>
<dd> <p> <code>&quot;less&quot;</code> now includes the <code>&quot;stash_name&quot;</code> method to allow subclasses of <code>&quot;less&quot;</code> to pick where in %^H to store their stash. </p>
<p> Upgraded from version 0.02 to 0.03. </p>
 </dd>
<dt>&quot;lib&quot;</dt>
<dd> <p> Upgraded from version 0.5565 to 0.62. </p>
 </dd>
<dt>&quot;mro&quot;</dt>
<dd> <p> <code>&quot;mro&quot;</code> is now implemented as an <font SIZE="-1">XS</font> extension. The documented interface has not changed. Code relying on the implementation detail that some <code>&quot;mro::&quot;</code> methods happened to be available at all times gets to ``keep both pieces&#8217;&#8216;. </p>
<p> Upgraded from version 1.00 to 1.02. </p>
 </dd>
<dt>&quot;overload&quot;</dt>
<dd> <p> <code>&quot;overload&quot;</code> now allow overloading of &#8216;qr&#8217;. </p>
<p> Upgraded from version 1.06 to 1.10. </p>
 </dd>
<dt>&quot;threads&quot;</dt>
<dd> <p> Upgraded from version 1.67 to 1.75. </p>
 </dd>
<dt>&quot;threads::shared&quot;</dt>
<dd> <p> Upgraded from version 1.14 to 1.32. </p>
 </dd>
<dt>&quot;version&quot;</dt>
<dd> <p> <code>&quot;version&quot;</code> now has support for ``Version number formats&#8217;&#8216; as described earlier in this document and in its own documentation. </p>
<p> Upgraded from version 0.74 to 0.82. </p>
 </dd>
<dt>&quot;warnings&quot;</dt>
<dd> <p> <code>&quot;warnings&quot;</code> has a new <code>&quot;warnings::fatal_enabled()&quot;</code> function. It also includes a new <code>&quot;illegalproto&quot;</code> warning category. See also ``New or Changed Diagnostics&#8217;&#8216; for this change. </p>
<p> Upgraded from version 1.06 to 1.09. </p>
 </dd></dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</dt>
<dd> <p> Upgraded from version 0.24 to 0.38. </p>
 </dd>
<dt>&quot;Archive::Tar&quot;</dt>
<dd> <p> Upgraded from version 1.38 to 1.54. </p>
 </dd>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> <p> Upgraded from version 0.79 to 0.87. </p>
 </dd>
<dt>&quot;AutoLoader&quot;</dt>
<dd> <p> Upgraded from version 5.63 to 5.70. </p>
 </dd>
<dt>&quot;B::Concise&quot;</dt>
<dd> <p> Upgraded from version 0.74 to 0.78. </p>
 </dd>
<dt>&quot;B::Debug&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 1.12. </p>
 </dd>
<dt>&quot;B::Deparse&quot;</dt>
<dd> <p> Upgraded from version 0.83 to 0.96. </p>
 </dd>
<dt>&quot;B::Lint&quot;</dt>
<dd> <p> Upgraded from version 1.09 to 1.11_01. </p>
 </dd>
<dt>&quot;CGI&quot;</dt>
<dd> <p> Upgraded from version 3.29 to 3.48. </p>
 </dd>
<dt>&quot;Class::ISA&quot;</dt>
<dd> <p> Upgraded from version 0.33 to 0.36. </p>
<p> <font SIZE="-1">NOTE:</font> <code>&quot;Class::ISA&quot;</code> is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&quot;Compress::Raw::Zlib&quot;</dt>
<dd> <p> Upgraded from version 2.008 to 2.024. </p>
 </dd>
<dt>&quot;CPAN&quot;</dt>
<dd> <p> Upgraded from version 1.9205 to 1.94_56. </p>
 </dd>
<dt>&quot;CPANPLUS&quot;</dt>
<dd> <p> Upgraded from version 0.84 to 0.90. </p>
 </dd>
<dt>&quot;CPANPLUS::Dist::Build&quot;</dt>
<dd> <p> Upgraded from version 0.06_02 to 0.46. </p>
 </dd>
<dt>&quot;Data::Dumper&quot;</dt>
<dd> <p> Upgraded from version 2.121_14 to 2.125. </p>
 </dd>
<dt>&quot;DB_File&quot;</dt>
<dd> <p> Upgraded from version 1.816_1 to 1.820. </p>
 </dd>
<dt>&quot;Devel::PPPort&quot;</dt>
<dd> <p> Upgraded from version 3.13 to 3.19. </p>
 </dd>
<dt>&quot;Digest&quot;</dt>
<dd> <p> Upgraded from version 1.15 to 1.16. </p>
 </dd>
<dt>&quot;Digest::MD5&quot;</dt>
<dd> <p> Upgraded from version 2.36_01 to 2.39. </p>
 </dd>
<dt>&quot;Digest::SHA&quot;</dt>
<dd> <p> Upgraded from version 5.45 to 5.47. </p>
 </dd>
<dt>&quot;Encode&quot;</dt>
<dd> <p> Upgraded from version 2.23 to 2.39. </p>
 </dd>
<dt>&quot;Exporter&quot;</dt>
<dd> <p> Upgraded from version 5.62 to 5.64_01. </p>
 </dd>
<dt>&quot;ExtUtils::CBuilder&quot;</dt>
<dd> <p> Upgraded from version 0.21 to 0.27. </p>
 </dd>
<dt>&quot;ExtUtils::Command&quot;</dt>
<dd> <p> Upgraded from version 1.13 to 1.16. </p>
 </dd>
<dt>&quot;ExtUtils::Constant&quot;</dt>
<dd> <p> Upgraded from version 0.2 to 0.22. </p>
 </dd>
<dt>&quot;ExtUtils::Install&quot;</dt>
<dd> <p> Upgraded from version 1.44 to 1.55. </p>
 </dd>
<dt>&quot;ExtUtils::MakeMaker&quot;</dt>
<dd> <p> Upgraded from version 6.42 to 6.56. </p>
 </dd>
<dt>&quot;ExtUtils::Manifest&quot;</dt>
<dd> <p> Upgraded from version 1.51_01 to 1.57. </p>
 </dd>
<dt>&quot;ExtUtils::ParseXS&quot;</dt>
<dd> <p> Upgraded from version 2.18_02 to 2.21. </p>
 </dd>
<dt>&quot;File::Fetch&quot;</dt>
<dd> <p> Upgraded from version 0.14 to 0.24. </p>
 </dd>
<dt>&quot;File::Path&quot;</dt>
<dd> <p> Upgraded from version 2.04 to 2.08_01. </p>
 </dd>
<dt>&quot;File::Temp&quot;</dt>
<dd> <p> Upgraded from version 0.18 to 0.22. </p>
 </dd>
<dt>&quot;Filter::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.82 to 0.84. </p>
 </dd>
<dt>&quot;Filter::Util::Call&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&quot;Getopt::Long&quot;</dt>
<dd> <p> Upgraded from version 2.37 to 2.38. </p>
 </dd>
<dt>&quot;IO&quot;</dt>
<dd> <p> Upgraded from version 1.23_01 to 1.25_02. </p>
 </dd>
<dt>&quot;IO::Zlib&quot;</dt>
<dd> <p> Upgraded from version 1.07 to 1.10. </p>
 </dd>
<dt>&quot;IPC::Cmd&quot;</dt>
<dd> <p> Upgraded from version 0.40_1 to 0.54. </p>
 </dd>
<dt>&quot;IPC::SysV&quot;</dt>
<dd> <p> Upgraded from version 1.05 to 2.01. </p>
 </dd>
<dt>&quot;Locale::Maketext&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.14. </p>
 </dd>
<dt>&quot;Locale::Maketext::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.18 to 0.21. </p>
 </dd>
<dt>&quot;Log::Message&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&quot;Log::Message::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.04 to 0.06. </p>
 </dd>
<dt>&quot;Math::BigInt&quot;</dt>
<dd> <p> Upgraded from version 1.88 to 1.89_01. </p>
 </dd>
<dt>&quot;Math::BigInt::FastCalc&quot;</dt>
<dd> <p> Upgraded from version 0.16 to 0.19. </p>
 </dd>
<dt>&quot;Math::BigRat&quot;</dt>
<dd> <p> Upgraded from version 0.21 to 0.24. </p>
 </dd>
<dt>&quot;Math::Complex&quot;</dt>
<dd> <p> Upgraded from version 1.37 to 1.56. </p>
 </dd>
<dt>&quot;Memoize&quot;</dt>
<dd> <p> Upgraded from version 1.01_02 to 1.01_03. </p>
 </dd>
<dt>&quot;MIME::Base64&quot;</dt>
<dd> <p> Upgraded from version 3.07_01 to 3.08. </p>
 </dd>
<dt>&quot;Module::Build&quot;</dt>
<dd> <p> Upgraded from version 0.2808_01 to 0.3603. </p>
 </dd>
<dt>&quot;Module::CoreList&quot;</dt>
<dd> <p> Upgraded from version 2.12 to 2.29. </p>
 </dd>
<dt>&quot;Module::Load&quot;</dt>
<dd> <p> Upgraded from version 0.12 to 0.16. </p>
 </dd>
<dt>&quot;Module::Load::Conditional&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.34. </p>
 </dd>
<dt>&quot;Module::Loaded&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.06. </p>
 </dd>
<dt>&quot;Module::Pluggable&quot;</dt>
<dd> <p> Upgraded from version 3.6 to 3.9. </p>
 </dd>
<dt>&quot;Net::Ping&quot;</dt>
<dd> <p> Upgraded from version 2.33 to 2.36. </p>
 </dd>
<dt>&quot;NEXT&quot;</dt>
<dd> <p> Upgraded from version 0.60_01 to 0.64. </p>
 </dd>
<dt>&quot;Object::Accessor&quot;</dt>
<dd> <p> Upgraded from version 0.32 to 0.36. </p>
 </dd>
<dt>&quot;Package::Constants&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 0.02. </p>
 </dd>
<dt>&quot;PerlIO&quot;</dt>
<dd> <p> Upgraded from version 1.04 to 1.06. </p>
 </dd>
<dt>&quot;Pod::Parser&quot;</dt>
<dd> <p> Upgraded from version 1.35 to 1.37. </p>
 </dd>
<dt>&quot;Pod::Perldoc&quot;</dt>
<dd> <p> Upgraded from version 3.14_02 to 3.15_02. </p>
 </dd>
<dt>&quot;Pod::Plainer&quot;</dt>
<dd> <p> Upgraded from version 0.01 to 1.02. </p>
<p> <font SIZE="-1">NOTE:</font> <code>&quot;Pod::Plainer&quot;</code> is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&quot;Pod::Simple&quot;</dt>
<dd> <p> Upgraded from version 3.05 to 3.13. </p>
 </dd>
<dt>&quot;Safe&quot;</dt>
<dd> <p> Upgraded from version 2.12 to 2.22. </p>
 </dd>
<dt>&quot;SelfLoader&quot;</dt>
<dd> <p> Upgraded from version 1.11 to 1.17. </p>
 </dd>
<dt>&quot;Storable&quot;</dt>
<dd> <p> Upgraded from version 2.18 to 2.22. </p>
 </dd>
<dt>&quot;Switch&quot;</dt>
<dd> <p> Upgraded from version 2.13 to 2.16. </p>
<p> <font SIZE="-1">NOTE:</font> <code>&quot;Switch&quot;</code> is deprecated and may be removed from a future version of Perl. </p>
 </dd>
<dt>&quot;Sys::Syslog&quot;</dt>
<dd> <p> Upgraded from version 0.22 to 0.27. </p>
 </dd>
<dt>&quot;Term::ANSIColor&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 2.02. </p>
 </dd>
<dt>&quot;Term::UI&quot;</dt>
<dd> <p> Upgraded from version 0.18 to 0.20. </p>
 </dd>
<dt>&quot;Test&quot;</dt>
<dd> <p> Upgraded from version 1.25 to 1.25_02. </p>
 </dd>
<dt>&quot;Test::Harness&quot;</dt>
<dd> <p> Upgraded from version 2.64 to 3.17. </p>
 </dd>
<dt>&quot;Test::Simple&quot;</dt>
<dd> <p> Upgraded from version 0.72 to 0.94. </p>
 </dd>
<dt>&quot;Text::Balanced&quot;</dt>
<dd> <p> Upgraded from version 2.0.0 to 2.02. </p>
 </dd>
<dt>&quot;Text::ParseWords&quot;</dt>
<dd> <p> Upgraded from version 3.26 to 3.27. </p>
 </dd>
<dt>&quot;Text::Soundex&quot;</dt>
<dd> <p> Upgraded from version 3.03 to 3.03_01. </p>
 </dd>
<dt>&quot;Thread::Queue&quot;</dt>
<dd> <p> Upgraded from version 2.00 to 2.11. </p>
 </dd>
<dt>&quot;Thread::Semaphore&quot;</dt>
<dd> <p> Upgraded from version 2.01 to 2.09. </p>
 </dd>
<dt>&quot;Tie::RefHash&quot;</dt>
<dd> <p> Upgraded from version 1.37 to 1.38. </p>
 </dd>
<dt>&quot;Time::HiRes&quot;</dt>
<dd> <p> Upgraded from version 1.9711 to 1.9719. </p>
 </dd>
<dt>&quot;Time::Local&quot;</dt>
<dd> <p> Upgraded from version 1.18 to 1.1901_01. </p>
 </dd>
<dt>&quot;Time::Piece&quot;</dt>
<dd> <p> Upgraded from version 1.12 to 1.15. </p>
 </dd>
<dt>&quot;Unicode::Collate&quot;</dt>
<dd> <p> Upgraded from version 0.52 to 0.52_01. </p>
 </dd>
<dt>&quot;Unicode::Normalize&quot;</dt>
<dd> <p> Upgraded from version 1.02 to 1.03. </p>
 </dd>
<dt>&quot;Win32&quot;</dt>
<dd> <p> Upgraded from version 0.34 to 0.39. </p>
 </dd>
<dt>&quot;Win32API::File&quot;</dt>
<dd> <p> Upgraded from version 0.1001_01 to 0.1101. </p>
 </dd>
<dt>&quot;XSLoader&quot;</dt>
<dd> <p> Upgraded from version 0.08 to 0.10. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<dl>
<dt>&quot;attrs&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 1.02. </p>
 </dd>
<dt>&quot;CPAN::API::HOWTO&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was &#8216;undef&#8217;. </p>
 </dd>
<dt>&quot;CPAN::DeferedCode&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 5.50. </p>
 </dd>
<dt>&quot;CPANPLUS::inc&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was &#8216;undef&#8217;. </p>
 </dd>
<dt>&quot;DCLsym&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 1.03. </p>
 </dd>
<dt>&quot;ExtUtils::MakeMaker::bytes&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 6.42. </p>
 </dd>
<dt>&quot;ExtUtils::MakeMaker::vmsish&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 6.42. </p>
 </dd>
<dt>&quot;Stdio&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 2.3. </p>
 </dd>
<dt>&quot;Test::Harness::Assert&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.02. </p>
 </dd>
<dt>&quot;Test::Harness::Iterator&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.02. </p>
 </dd>
<dt>&quot;Test::Harness::Point&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.01. </p>
 </dd>
<dt>&quot;Test::Harness::Results&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.01. </p>
 </dd>
<dt>&quot;Test::Harness::Straps&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.26_01. </p>
 </dd>
<dt>&quot;Test::Harness::Util&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 0.01. </p>
 </dd>
<dt>&quot;XSSymSet&quot;</dt>
<dd> <p> Removed from the Perl core. Prior version was 1.1. </p>
 </dd></dl>
<h3>Deprecated Modules and Pragmata</h3>
<p> See ``Deprecated Modules&#8217;&#8216; above.  </p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> perlhaiku contains instructions on how to build perl for the Haiku platform. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlmroapi describes the new interface for pluggable Method Resolution Orders. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlperf, by Richard Foley, provides an introduction to the use of performance and optimization techniques which can be used with particular reference to perl programs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrepository describes how to access the perl source using the <i>git</i> version control system. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlpolicy extends the ``Social contract about contributed modules&#8217;&#8216; into the beginnings of a document on Perl porting policies. </p>
 </dd></dl>
<h3>Changes to Existing Documentation</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The various large <i>Changes*</i> files (which listed every change made to perl over the last 18 years) have been removed, and replaced by a small file, also called <i>Changes</i>, which just explains how that same information may be extracted from the git version control system. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Porting/patching.pod</i> has been deleted, as it mainly described interacting with the old Perforce-based repository, which is now obsolete. Information still relevant has been moved to perlrepository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The syntax <code>&quot;unless (EXPR) BLOCK else BLOCK&quot;</code> is now documented as valid, as is the syntax <code>&quot;unless (EXPR) BLOCK elsif (EXPR) BLOCK ... else BLOCK&quot;</code>, although actually using the latter may not be the best idea for the readability of your source code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documented -X overloading. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documented that <code>&quot;when()&quot;</code> treats specially most of the filetest operators </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documented <code>&quot;when&quot;</code> as a syntax modifier. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Eliminated ``Old Perl threads tutorial&#8217;&#8216;, which described 5005 threads. </p>
<p> <i>pod/perlthrtut.pod</i> is the same material reworked for ithreads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Correct previous documentation: v-strings are not deprecated </p>
<p> With version objects, we need them to use <font SIZE="-1">MODULE VERSION</font> syntax. This patch removes the deprecation notice. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Security contact information is now part of perlsec. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A significant fraction of the core documentation has been updated to clarify the behavior of Perl&#8217;s Unicode handling. </p>
<p> Much of the remaining core documentation has been reviewed and edited for clarity, consistent use of language, and to fix the spelling of Tom Christiansen&#8217;s name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Pod specification (perlpodspec) has been updated to bring the specification in line with modern usage already supported by most Pod systems. A parameter string may now follow the format name in a ``begin/end&#8217;&#8216; region. Links to URIs with a text description are now allowed. The usage of <code>&quot;L&lt;&quot;section&quot;&gt;&quot;</code> has been marked as deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if.pm has been documented in ``use&#8217;&#8216; in perlfunc as a means to get conditional loading of modules despite the implicit <font SIZE="-1">BEGIN</font> block around <code>&quot;use&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation for <code>$1</code> in perlvar.pod has been clarified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\N{U+</code>code point <code>}&quot;</code> is now documented. </p>
 </dd></dl>
<h2>Selected Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new internal cache means that <code>&quot;isa()&quot;</code> will often be faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The implementation of <code>&quot;C3&quot;</code> Method Resolution Order has been optimised - linearisation for classes with single inheritance is 40% faster. Performance for multiple inheritance is unchanged. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use locale&quot;</code>, the locale-relevant information is now cached on read-only values, such as the list returned by <code>&quot;keys %hash&quot;</code>. This makes operations such as <code>&quot;sort keys %hash&quot;</code> in the scope of <code>&quot;use locale&quot;</code> much faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Empty <code>&quot;DESTROY&quot;</code> methods are no longer called. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_sv_utf8_upgrade()&quot;</code> is now faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;keys&quot;</code> on empty hash is now faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;if (%foo)&quot;</code> has been optimized to be faster than <code>&quot;if (keys %foo)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The string repetition operator (<code>&quot;$str x $num&quot;</code>) is now several times faster when <code>$str</code> has length one or <code>$num</code> is large. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reversing an array to itself (as in <code>&quot;@a = reverse @a&quot;</code>) in void context now happens in-place and is several orders of magnitude faster than it used to be. It will also preserve non-existent elements whenever possible, i.e. for non magical arrays or tied arrays with <code>&quot;EXISTS&quot;</code> and <code>&quot;DELETE&quot;</code> methods. </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> perlapi, perlintern, perlmodlib and perltoc are now all generated at build time, rather than being shipped as part of the release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If <code>&quot;vendorlib&quot;</code> and <code>&quot;vendorarch&quot;</code> are the same, then they are only added to <code>@INC</code> once. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$Config{usedevel}</code> and the C-level <code>&quot;PERL_USE_DEVEL&quot;</code> are now defined if perl is built with <code>&quot;-Dusedevel&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> will enable use of <code>&quot;-fstack-protector&quot;</code>, to provide protection against stack-smashing attacks, if the compiler supports it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> will now determine the correct prototypes for re-entrant functions and for <code>&quot;gconvert&quot;</code> if you are using a C<font SIZE="-2">++</font> compiler rather than a C compiler. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Unix, if you build from a tree containing a git repository, the configuration process will note the commit hash you have checked out, for display in the output of <code>&quot;perl -v&quot;</code> and <code>&quot;perl -V&quot;</code>. Unpushed local commits are automatically added to the list of local patches displayed by <code>&quot;perl -V&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now supports SystemTap&#8217;s <code>&quot;dtrace&quot;</code> compatibility layer and an issue with linking <code>&quot;miniperl&quot;</code> has been fixed in the process. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perldoc now uses <code>&quot;less -R&quot;</code> instead of <code>&quot;less&quot;</code> for improved behaviour in the face of <code>&quot;groff&quot;</code>&#8216;s new usage of <font SIZE="-1">ANSI</font> escape codes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perl -V&quot;</code> now reports use of the compile-time options <code>&quot;USE_PERL_ATOF&quot;</code> and <code>&quot;USE_ATTRIBUTES_FOR_PERLIO&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> As part of the flattening of <i>ext</i>, all extensions on all platforms are built by <i>make_ext.pl</i>. This replaces the Unix-specific <i>ext/util/make_ext</i>, VMS-specific <i>make_ext.com</i> and Win32-specific <i>win32/buildext.pl</i>. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<p> Each release of Perl sees numerous internal changes which shouldn&#8217;t affect day to day usage but may still be notable for developers working with Perl&#8217;s source code. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The J.R.R. Tolkien quotes at the head of C source file have been checked and proper citations added, thanks to a patch from Tom Christiansen. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The internal structure of the dual-life modules traditionally found in the <i>lib/</i> and <i>ext/</i> directories in the perl source has changed significantly. Where possible, dual-lifed modules have been extracted from <i>lib/</i> and <i>ext/</i>. </p>
<p> Dual-lifed modules maintained by Perl&#8217;s developers as part of the Perl core now live in <i>dist/</i>. Dual-lifed modules maintained primarily on <font SIZE="-1">CPAN</font> now live in <i>cpan/</i>. When reporting a bug in a module located under <i>cpan/</i>, please send your bug report directly to the module&#8217;s bug tracker or author, rather than Perl&#8217;s bug tracker. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\N{...}&quot;</code> now compiles better, always forces <font SIZE="-1">UTF-8</font> internal representation </p>
<p> Perl&#8217;s developers have fixed several problems with the recognition of <code>&quot;\N{...}&quot;</code> constructs. As part of this, perl will store any scalar or regex containing <code>&quot;\N{</code>name <code>}&quot;</code> or <code>&quot;\N{U+</code>code point <code>}&quot;</code> in its definition in <font SIZE="-1">UTF-8</font> format. (This was true previously for all occurrences of <code>&quot;\N{</code>name <code>}&quot;</code> that did not use a custom translator, but now it&#8217;s always true.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl_magic_setmglob now knows about globs, fixing <font SIZE="-1">RT</font> #71254. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;SVt_RV&quot;</code> no longer exists. RVs are now stored in IVs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_vcroak()&quot;</code> now accepts a null first argument. In addition, a full audit was made of the ``not <font SIZE="-1">NULL&#8217;&#8216;</font> compiler annotations, and those for several other internal functions were corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New macros <code>&quot;dSAVEDERRNO&quot;</code>, <code>&quot;dSAVE_ERRNO&quot;</code>, <code>&quot;SAVE_ERRNO&quot;</code>, <code>&quot;RESTORE_ERRNO&quot;</code> have been added to formalise the temporary saving of the <code>&quot;errno&quot;</code> variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_sv_insert_flags&quot;</code> has been added to augment <code>&quot;Perl_sv_insert&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_newSV_type(type)&quot;</code> has been added, equivalent to <code>&quot;Perl_newSV()&quot;</code> followed by <code>&quot;Perl_sv_upgrade(type)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_newSVpvn_flags()&quot;</code> has been added, equivalent to <code>&quot;Perl_newSVpvn()&quot;</code> and then performing the action relevant to the flag. </p>
<p> Two flag bits are currently supported. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;SVf_UTF8&quot;</code> will call <code>&quot;SvUTF8_on()&quot;</code> for you. (Note that this does not convert a sequence of <font SIZE="-1">ISO 8859-1</font> characters to <font SIZE="-1">UTF-8</font>). A wrapper, <code>&quot;newSVpvn_utf8()&quot;</code> is available for this. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;SVs_TEMP&quot;</code> now calls <code>&quot;Perl_sv_2mortal()&quot;</code> on the new <font SIZE="-1">SV.</font> </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> There is also a wrapper that takes constant strings, <code>&quot;newSVpvs_flags()&quot;</code>. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> The function <code>&quot;Perl_croak_xs_usage&quot;</code> has been added as a wrapper to <code>&quot;Perl_croak&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now exports the functions <code>&quot;PerlIO_find_layer&quot;</code> and <code>&quot;PerlIO_list_alloc&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_na&quot;</code> has been exterminated from the core code, replaced by local <font SIZE="-1">STRLEN</font> temporaries, or <code>&quot;*_nolen()&quot;</code> calls. Either approach is faster than <code>&quot;PL_na&quot;</code>, which is a pointer dereference into the interpreter structure under ithreads, and a global variable otherwise. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_mg_free()&quot;</code> used to leave freed memory accessible via <code>&quot;SvMAGIC()&quot;</code> on the scalar. It now updates the linked list to remove each piece of magic as it is freed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under ithreads, the regex in <code>&quot;PL_reg_curpm&quot;</code> is now reference counted. This eliminates a lot of hackish workarounds to cope with it not being reference counted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_mg_magical()&quot;</code> would sometimes incorrectly turn on <code>&quot;SvRMAGICAL()&quot;</code>. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <i>public</i> <font SIZE="-1">IV</font> and <font SIZE="-1">NV</font> flags are now not set if the string value has trailing ``garbage&#8217;&#8216;. This behaviour is consistent with not setting the public <font SIZE="-1">IV</font> or <font SIZE="-1">NV</font> flags if the value is out of range for the type. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Uses of <code>&quot;Nullav&quot;</code>, <code>&quot;Nullcv&quot;</code>, <code>&quot;Nullhv&quot;</code>, <code>&quot;Nullop&quot;</code>, <code>&quot;Nullsv&quot;</code> etc have been replaced by <code>&quot;NULL&quot;</code> in the core code, and non-dual-life modules, as <code>&quot;NULL&quot;</code> is clearer to those unfamiliar with the core code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A macro <code>MUTABLE_PTR(p)</code> has been added, which on (non-pedantic) gcc will not cast away <code>&quot;const&quot;</code>, returning a <code>&quot;void *&quot;</code>. Macros <code>&quot;MUTABLE_SV(av)&quot;</code>, <code>&quot;MUTABLE_SV(cv)&quot;</code> etc build on this, casting to <code>&quot;AV *&quot;</code> etc without casting away <code>&quot;const&quot;</code>. This allows proper compile-time auditing of <code>&quot;const&quot;</code> correctness in the core, and helped picked up some errors (now fixed). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Macros <code>&quot;mPUSHs()&quot;</code> and <code>&quot;mXPUSHs()&quot;</code> have been added, for pushing SVs on the stack and mortalizing them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of the private structure <code>&quot;mro_meta&quot;</code> has changed slightly. Nothing outside the core should be accessing this directly anyway. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new tool, <i>Porting/expand-macro.pl</i> has been added, that allows you to view how a C preprocessor macro would be expanded when compiled. This is handy when trying to decode the macro hell that is the perl guts. </p>
 </dd></dl>
<h2>Testing</h2>
<h3>Testing improvements</h3>
<dl>
<dt>Parallel tests</dt>
<dd> <p> The core distribution can now run its regression tests in parallel on Unix-like platforms. Instead of running <code>&quot;make test&quot;</code>, set <code>&quot;TEST_JOBS&quot;</code> in your environment to the number of tests to run in parallel, and run <code>&quot;make test_harness&quot;</code>. On a Bourne-like shell, this can be done as </p>
<pre><code>    TEST_JOBS=3 make test_harness # Run 3 tests in parallel
</code></pre>
<p> An environment variable is used, rather than parallel make itself, because TAP::Harness needs to be able to schedule individual non-conflicting test scripts itself, and there is no standard interface to <code>&quot;make&quot;</code> utilities to interact with their job schedulers. </p>
<p> Note that currently some test scripts may fail when run in parallel (most notably <code>&quot;ext/IO/t/io_dir.t&quot;</code>). If necessary run just the failing scripts again sequentially and see if the failures go away. </p>
 </dd>
<dt>Test harness flexibility</dt>
<dd> <p> It&#8217;s now possible to override <code>&quot;PERL5OPT&quot;</code> and friends in <i>t/TEST</i> </p>
 </dd>
<dt>Test watchdog</dt>
<dd> <p> Several tests that have the potential to hang forever if they fail now incorporate a ``watchdog&#8217;&#8216; functionality that will kill them after a timeout, which helps ensure that <code>&quot;make test&quot;</code> and <code>&quot;make test_harness&quot;</code> run to completion automatically. </p>
 </dd></dl>
<h3>New Tests</h3>
<p> Perl&#8217;s developers have added a number of new tests to the core. In addition to the items listed below, many modules updated from <font SIZE="-1">CPAN</font> incorporate new tests. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Significant cleanups to core tests to ensure that language and interpreter features are not used before they&#8217;re tested. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;make test_porting&quot;</code> now runs a number of important pre-commit checks which might be of use to anyone working on the Perl core. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/porting/podcheck.t</i> automatically checks the well-formedness of <font SIZE="-1">POD</font> found in all .pl, .pm and .pod files in the <i></i><font SIZE="-1"><i>MANIFEST</i></font><i></i>, other than in dual-lifed modules which are primarily maintained outside the Perl core. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/porting/manifest.t</i> now tests that all files listed in <font SIZE="-1">MANIFEST</font> are present. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/while_readdir.t</i> tests that a bare readdir in while loop sets <code>$_</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/comp/retainedlines.t</i> checks that the debugger can retain source lines from <code>&quot;eval&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/io/perlio_fail.t</i> checks that bad layers fail. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/io/perlio_leaks.t</i> checks that PerlIO layers are not leaking. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/io/perlio_open.t</i> checks that certain special forms of open work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/io/perlio.t</i> includes general PerlIO tests. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/io/pvbm.t</i> checks that there is no unexpected interaction between the internal types <code>&quot;PVBM&quot;</code> and <code>&quot;PVGV&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/mro/package_aliases.t</i> checks that mro works properly in the presence of aliased packages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/dbm.t</i> tests <code>&quot;dbmopen&quot;</code> and <code>&quot;dbmclose&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/index_thr.t</i> tests the interaction of <code>&quot;index&quot;</code> and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/pat_thr.t</i> tests the interaction of esoteric patterns and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/qr_gc.t</i> tests that <code>&quot;qr&quot;</code> doesn&#8217;t leak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/reg_email_thr.t</i> tests the interaction of regex recursion and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/regexp_qr_embed_thr.t</i> tests the interaction of patterns with embedded <code>&quot;qr//&quot;</code> and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/regexp_unicode_prop.t</i> tests Unicode properties in regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/regexp_unicode_prop_thr.t</i> tests the interaction of Unicode properties and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/reg_nc_tie.t</i> tests the tied methods of <code>&quot;Tie::Hash::NamedCapture&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/reg_posixcc.t</i> checks that <font SIZE="-1">POSIX</font> character classes behave consistently. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/re.t</i> checks that exportable <code>&quot;re&quot;</code> functions in <i>universal.c</i> work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/setpgrpstack.t</i> checks that <code>&quot;setpgrp&quot;</code> works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/substr_thr.t</i> tests the interaction of <code>&quot;substr&quot;</code> and threads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/upgrade.t</i> checks that upgrading and assigning scalars works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/uni/lex_utf8.t</i> checks that Unicode in the lexer works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/uni/tie.t</i> checks that Unicode and <code>&quot;tie&quot;</code> work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/comp/final_line_num.t</i> tests whether line numbers are correct at <font SIZE="-1">EOF</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/comp/form_scope.t</i> tests format scoping. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/comp/line_debug.t</i> tests whether <code>&quot;@{&quot;_&lt;$file&quot;}&quot;</code> works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/filetest_t.t</i> tests if -t file test works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/qr.t</i> tests <code>&quot;qr&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/utf8cache.t</i> tests malfunctions of the utf8 cache. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/re/uniprops.t</i> test unicodes <code>&quot;\p{}&quot;</code> regex constructs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/filehandle.t</i> tests some suitably portable filetest operators to check that they work as expected, particularly in the light of some internal changes made in how filehandles are blessed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/op/time_loop.t</i> tests that unix times greater than <code>&quot;2**63&quot;</code>, which can now be handed to <code>&quot;gmtime&quot;</code> and <code>&quot;localtime&quot;</code>, do not cause an internal overflow or an excessively long loop. </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<h3>New Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">SV</font> allocation tracing has been added to the diagnostics enabled by <code>&quot;-Dm&quot;</code>. The tracing can alternatively output via the <code>&quot;PERL_MEM_LOG&quot;</code> mechanism, if that was enabled when the <i>perl</i> binary was compiled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Smartmatch resolution tracing has been added as a new diagnostic. Use <code>&quot;-DM&quot;</code> to enable it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new debugging flag <code>&quot;-DB&quot;</code> now dumps subroutine definitions, leaving <code>&quot;-Dx&quot;</code> for its original purpose of dumping syntax trees. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.12 provides a number of new diagnostic messages to help you write better code. See perldiag for details of these new messages. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Bad plugin affecting keyword &#8216;%s&#8217;&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;gmtime(%.0f) too large&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Lexing code attempted to stuff non-Latin-1 character into Latin-1 input&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Lexing code internal error (%s)&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;localtime(%.0f) too large&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Overloaded dereference did not return a reference&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Overloaded qr did not return a REGEXP&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Perl_pmflag() is deprecated, and will be removed from the XS API&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lvalue attribute ignored after the subroutine has been defined&quot;</code> </p>
<p> This new warning is issued when one attempts to mark a subroutine as lvalue after it has been defined. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now warns you if <code>&quot;++&quot;</code> or <code>&quot;--&quot;</code> are unable to change the value because it&#8217;s beyond the limit of representation. </p>
<p> This uses a new warnings category: ``imprecision&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;lc&quot;</code>, <code>&quot;uc&quot;</code>, <code>&quot;lcfirst&quot;</code>, and <code>&quot;ucfirst&quot;</code> warn when passed undef. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Show constant in &quot;Useless use of a constant in void context&quot;&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Prototype after &#8216;%s&#8217;&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;panic: sv_chop %s&quot;</code> </p>
<p> This new fatal error occurs when the C routine <code>&quot;Perl_sv_chop()&quot;</code> was passed a position that is not within the scalar&#8217;s string buffer. This could be caused by buggy <font SIZE="-1">XS</font> code, and at this point recovery is not possible. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The fatal error <code>&quot;Malformed UTF-8 returned by \N&quot;</code> is now produced if the <code>&quot;charnames&quot;</code> handler returns malformed <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If an unresolved named character or sequence was encountered when compiling a regex pattern then the fatal error <code>&quot;\N{NAME} must be resolved by the lexer&quot;</code> is now produced. This can happen, for example, when using a single-quotish context like <code>&quot;$re = &#8216;\N{SPACE}&#8216;; /$re/;&quot;</code>. See perldiag for more examples of how the lexer can get bypassed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Invalid hexadecimal number in \N{U+...}&quot;</code> is a new fatal error triggered when the character constant represented by <code>&quot;...&quot;</code> is not a valid hexadecimal number. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new meaning of <code>&quot;\N&quot;</code> as <code>&quot;[^\n]&quot;</code> is not valid in a bracketed character class, just like <code>&quot;.&quot;</code> in a character class loses its special meaning, and will cause the fatal error <code>&quot;\N in a character class must be a named character: \N{...}&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The rules on what is legal for the <code>&quot;...&quot;</code> in <code>&quot;\N{...}&quot;</code> have been tightened up so that unless the <code>&quot;...&quot;</code> begins with an alphabetic character and continues with a combination of alphanumerics, dashes, spaces, parentheses or colons then the warning <code>&quot;Deprecated character(s) in \N{...} starting at &#8216;%s&#8217;&quot;</code> is now issued. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning <code>&quot;Using just the first characters returned by \N{}&quot;</code> will be issued if the <code>&quot;charnames&quot;</code> handler returns a sequence of characters which exceeds the limit of the number of characters that can be used. The message will indicate which characters were used and which were discarded. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h3>Changed Diagnostics</h3>
<p> A number of existing diagnostic messages have been improved or corrected: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A new warning category <code>&quot;illegalproto&quot;</code> allows finer-grained control of warnings around function prototypes. </p>
<p> The two warnings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;Illegal character in prototype for %s : %s&quot;</dt>
<dd>  </dd>
<dt>&quot;Prototype after &#8216;%c&#8217; for %s : %s&quot;</dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd> <p> have been moved from the <code>&quot;syntax&quot;</code> top-level warnings category into a new first-level category, <code>&quot;illegalproto&quot;</code>. These two warnings are currently the only ones emitted during parsing of an invalid/illegal prototype, so one can now use </p>
<pre><code>  no warnings 'illegalproto';
</code></pre>
<p> to suppress only those, but not other syntax-related warnings. Warnings where prototypes are changed, ignored, or not met are still in the <code>&quot;prototype&quot;</code> category as before. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Deep recursion on subroutine &quot;%s&quot;&quot;</code> </p>
<p> It is now possible to change the depth threshold for this warning from the default of 100, by recompiling the <i>perl</i> binary, setting the C pre-processor macro <code>&quot;PERL_SUB_DEPTH_WARN&quot;</code> to the desired value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Illegal character in prototype&quot;</code> warning is now more precise when reporting illegal characters after _ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> mro merging error messages are now very similar to those produced by Algorithm::C3. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Amelioration of the error message ``Unrecognized character <code>%s</code> in column <code>%d</code>&#8216;&#8216; </p>
<p> Changes the error message to ``Unrecognized character <code>%s</code>; marked by &lt;-- <font SIZE="-1">HERE</font> after <code>%s</code>&lt;-- <font SIZE="-1">HERE</font> near column <code>%d</code>&#8216;&#8216;. This should make it a little simpler to spot and correct the suspicious character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now explicitly points to <code>$.</code> when it causes an uninitialized warning for ranges in scalar context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;split&quot;</code> now warns when called in void context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;printf&quot;</code>-style functions called with too few arguments will now issue the warning <code>&quot;Missing argument in %s&quot;</code> [perl #71000] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now properly returns a syntax error instead of segfaulting if <code>&quot;each&quot;</code>, <code>&quot;keys&quot;</code>, or <code>&quot;values&quot;</code> is used without an argument. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;tell()&quot;</code> now fails properly if called without an argument and when no previous file was read. </p>
<p> <code>&quot;tell()&quot;</code> now returns <code>&quot;-1&quot;</code>, and sets errno to <code>&quot;EBADF&quot;</code>, thus restoring the 5.8.x behaviour. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;overload&quot;</code> no longer implicitly unsets fallback on repeated &#8216;use overload&#8217; lines. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POSIX::strftime()</code> can now handle Unicode characters in the format string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;syntax&quot;</code> category was removed from 5 warnings that should only be in <code>&quot;deprecated&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Three fatal <code>&quot;pack&quot;</code>/<code>&quot;unpack&quot;</code> error messages have been normalized to <code>&quot;panic: %s&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Unicode character is illegal&quot;</code> has been rephrased to be more accurate </p>
<p> It now reads <code>&quot;Unicode non-character is illegal in interchange&quot;</code> and the perldiag documentation has been expanded a bit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Currently, all but the first of the several characters that the <code>&quot;charnames&quot;</code> handler may return are discarded when used in a regular expression pattern bracketed character class. If this happens then the warning <code>&quot;Using just the first character returned by \N{} in character class&quot;</code> will be issued. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warning <code>&quot;Missing right brace on \N{} or unescaped left brace after \N. Assuming the latter&quot;</code> will be issued if Perl encounters a <code>&quot;\N{&quot;</code> but doesn&#8217;t find a matching <code>&quot;}&quot;</code>. In this case Perl doesn&#8217;t know if it was mistakenly omitted, or if ``match non-newline&#8217;&#8216; followed by &quot;match a <code>&quot;{&quot;</code>&quot; was desired. It assumes the latter because that is actually a valid interpretation as written, unlike the other case. If you meant the former, you need to add the matching right brace. If you did mean the latter, you can silence this warning by writing instead <code>&quot;\N\{&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;gmtime&quot;</code> and <code>&quot;localtime&quot;</code> called with numbers smaller than they can reliably handle will now issue the warnings <code>&quot;gmtime(%.0f) too small&quot;</code> and <code>&quot;localtime(%.0f) too small&quot;</code>. </p>
 </dd></dl>
<p> The following diagnostic messages have been removed: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Runaway format&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Can&#8217;t locate package %s for the parents of %s&quot;</code> </p>
<p> In general this warning it only got produced in conjunction with other warnings, and removing it allowed an <font SIZE="-1">ISA</font> lookup optimisation to be added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;v-string in use/require is non-portable&quot;</code> </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>h2ph</i> now looks in <code>&quot;include-fixed&quot;</code> too, which is a recent addition to gcc&#8217;s search path. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>h2xs</i> no longer incorrectly treats enum values like macros. It also now handles C<font SIZE="-2">++</font> style comments (<code>&quot;//&quot;</code>) properly in enums. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perl5db.pl</i> now supports <code>&quot;LVALUE&quot;</code> subroutines. Additionally, the debugger now correctly handles proxy constant subroutines, and subroutine stubs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perlbug</i> now uses <code>%Module::CoreList::bug_tracker</code> to print out upstream bug tracker URLs. If a user identifies a particular module as the topic of their bug report and we&#8217;re able to divine the <font SIZE="-1">URL</font> for its upstream bug tracker, perlbug now provide a message to the user explaining that the core copies the <font SIZE="-1">CPAN</font> version directly, and provide the <font SIZE="-1">URL</font> for reporting the bug directly to the upstream author. </p>
<p> <i>perlbug</i> no longer reports ``Message sent&#8217;&#8216; when it hasn&#8217;t actually sent the message </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perlthanks</i> is a new utility for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising. If Perl 5.12 works well for you, please try out <i>perlthanks</i>. It will make the developers smile. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl&#8217;s developers have fixed bugs in <i>a2p</i> having to do with the <code>&quot;match()&quot;</code> operator in list context. Additionally, <i>a2p</i> no longer generates code that uses the <code>$[</code> variable. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> U+0FFFF is now a legal character in regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pp_qr now always returns a new regexp <font SIZE="-1">SV.</font> Resolves <font SIZE="-1">RT</font> #69852. </p>
<p> Instead of returning a(nother) reference to the (pre-compiled) regexp in the optree, use <code>reg_temp_copy()</code> to create a copy of it, and return a reference to that. This resolves issues about Regexp::DESTROY not being called in a timely fashion (the original bug tracked by <font SIZE="-1">RT</font> #69852), as well as bugs related to blessing regexps, and of assigning to regexps, as described in correspondence added to the ticket. </p>
<p> It transpires that we also need to undo the <code>SvPVX()</code> sharing when ithreads cloning a Regexp <font SIZE="-1">SV,</font> because mother_re is set to <font SIZE="-1">NULL,</font> instead of a cloned copy of the mother_re. This change might fix bugs with regexps and threads in certain other situations, but as yet neither tests nor bug reports have indicated any problems, so it might not actually be an edge case that it&#8217;s possible to reach. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several compilation errors and segfaults when perl was built with <code>&quot;-Dmad&quot;</code> were fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixes for lexer <font SIZE="-1">API</font> changes in 5.11.2 which broke NYTProf&#8217;s savesrc option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-t&quot;</code> should only return <font SIZE="-1">TRUE</font> for file handles connected to a <font SIZE="-1">TTY</font> </p>
<p> The Microsoft C version of <code>&quot;isatty()&quot;</code> returns <font SIZE="-1">TRUE</font> for all character mode devices, including the <i>/dev/null</i>-style ``nul&#8217;&#8216; device and printers like ``lpt1&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a regression caused by commit fafafbaf which caused a panic during parameter passing [perl #70171] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On systems which in-place edits without backup files, -i&#8217;*&#8216; now works as the documentation says it does [perl #70802] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Saving and restoring magic flags no longer loses readonly flag. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The malformed syntax <code>&quot;grep EXPR LIST&quot;</code> (note the missing comma) no longer causes abrupt and total failure. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expressions compiled with <code>&quot;qr{}&quot;</code> literals properly set <code>&quot;$&#8216;&quot;</code> when matching again. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using named subroutines with <code>&quot;sort&quot;</code> should no longer lead to bus errors [perl #71076] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numerous bugfixes catch small issues caused by the recently-added Lexer <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Smart match against <code>@_</code> sometimes gave false negatives. [perl #71078] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$@</code> may now be assigned a read-only value (without error or busting the stack). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort&quot;</code> called recursively from within an active comparison subroutine no longer causes a bus error if run multiple times. [perl #71076] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Hash::NamedCapture::* will not abort if passed bad input (<font SIZE="-1">RT</font> #71828) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@_</code> and <code>$_</code> no longer leak under threads (<font SIZE="-1">RT</font> #34342 and #41138, also #70602, #70974) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-I&quot;</code> on shebang line now adds directories in front of <code>@INC</code> as documented, and as does <code>&quot;-I&quot;</code> when specified on the command-line. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;kill&quot;</code> is now fatal when called on non-numeric process identifiers. Previously, an <code>&quot;undef&quot;</code> process identifier would be interpreted as a request to kill process 0, which would terminate the current process group on <font SIZE="-1">POSIX</font> systems. Since process identifiers are always integers, killing a non-numeric process is now fatal. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.10.0 inadvertently disabled an optimisation, which caused a measurable performance drop in list assignment, such as is often used to assign function parameters from <code>@_</code>. The optimisation has been re-instated, and the performance regression fixed. (This fix is also present in 5.10.1) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed memory leak on <code>&quot;while (1) { map 1, 1 }&quot;</code> [<font SIZE="-1">RT</font> #53038]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some potential coredumps in PerlIO fixed [<font SIZE="-1">RT</font> #57322,54828]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger now works with lvalue subroutines. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger&#8217;s <code>&quot;m&quot;</code> command was broken on modules that defined constants [<font SIZE="-1">RT</font> #61222]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;crypt&quot;</code> and string complement could return tainted values for untainted arguments [<font SIZE="-1">RT</font> #59998]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-i&quot;</code><i>.suffix</i> command-line switch now recreates the file using restricted permissions, before changing its mode to match the original file. This eliminates a potential race condition [<font SIZE="-1">RT</font> #60904]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On some Unix systems, the value in <code>$?</code> would not have the top bit set (<code>&quot;$? &amp; 128&quot;</code>) even if the child core dumped. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under some circumstances, <code>$^R</code> could incorrectly become undefined [<font SIZE="-1">RT</font> #57042]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the <font SIZE="-1">XS API,</font> various hash functions, when passed a pre-computed hash where the key is <font SIZE="-1">UTF-8,</font> might result in an incorrect lookup. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">XS</font> code including <i></i><font SIZE="-1"><i>XSUB</i></font><i>.h</i> before <i>perl.h</i> gave a compile-time error [<font SIZE="-1">RT</font> #57176]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$object-&gt;isa(&#8216;Foo&#8217;)&quot;</code> would report false if the package <code>&quot;Foo&quot;</code> didn&#8217;t exist, even if the object&#8217;s <code>@ISA</code> contained <code>&quot;Foo&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various bugs in the new-to 5.10.0 mro code, triggered by manipulating <code>@ISA</code>, have been found and fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bitwise operations on references could crash the interpreter, e.g. <code>&quot;$x=\$y; $x |= &quot;foo&quot;&quot;</code> [<font SIZE="-1">RT</font> #54956]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Patterns including alternation might be sensitive to the internal <font SIZE="-1">UTF-8</font> representation, e.g. </p>
<pre><code>    my $byte = chr(192);
    my $utf8 = chr(192); utf8::upgrade($utf8);
    $utf8 =~ /$byte|X}/i; # failed in 5.10.0
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Within UTF8-encoded Perl source files (i.e. where <code>&quot;use utf8&quot;</code> is in effect), double-quoted literal strings could be corrupted where a <code>&quot;\xNN&quot;</code>, <code>&quot;\0NNN&quot;</code> or <code>&quot;\N{}&quot;</code> is followed by a literal character with ordinal value greater than 255 [<font SIZE="-1">RT</font> #59908]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;B::Deparse&quot;</code> failed to correctly deparse various constructs: <code>&quot;readpipe STRING&quot;</code> [<font SIZE="-1">RT</font> #62428], <code>&quot;CORE::require(STRING)&quot;</code> [<font SIZE="-1">RT</font> #62488], <code>&quot;sub foo(_)&quot;</code> [<font SIZE="-1">RT</font> #62484]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;setpgrp&quot;</code> with no arguments could corrupt the perl stack. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The block form of <code>&quot;eval&quot;</code> is now specifically trappable by <code>&quot;Safe&quot;</code> and <code>&quot;ops&quot;</code>. Previously it was erroneously treated like string <code>&quot;eval&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, the two characters <code>&quot;[~&quot;</code> were sometimes parsed as the smart match operator (<code>&quot;~~&quot;</code>) [<font SIZE="-1">RT</font> #63854]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, the <code>&quot;*&quot;</code> quantifier in patterns was sometimes treated as <code>&quot;{0,32767}&quot;</code> [<font SIZE="-1">RT</font> #60034, #60464]. For example, this match would fail: </p>
<pre><code>    (&quot;ab&quot; x 32768) =~ /^(ab)*$/
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;shmget&quot;</code> was limited to a 32 bit segment size on a 64 bit <font SIZE="-1">OS</font> [<font SIZE="-1">RT</font> #63924]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;next&quot;</code> or <code>&quot;last&quot;</code> to exit a <code>&quot;given&quot;</code> block no longer produces a spurious warning like the following: </p>
<pre><code>    Exiting given via last at foo.pl line 123
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a format to a glob could corrupt the format; e.g.: </p>
<pre><code>     *bar=*foo{FORMAT}; # foo format now bad
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to coerce a typeglob to a string or number could cause an assertion failure. The correct error message is now generated, <code>&quot;Can&#8217;t coerce GLOB to </code>$type <code>&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use filetest &#8216;access&#8217;&quot;</code>, <code>&quot;-x&quot;</code> was using the wrong access mode. This has been fixed [<font SIZE="-1">RT</font> #49003]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length&quot;</code> on a tied scalar that returned a Unicode value would not be correct the first time. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using an array <code>&quot;tie&quot;</code> inside in array <code>&quot;tie&quot;</code> could <font SIZE="-1">SEGV.</font> This has been fixed. [<font SIZE="-1">RT</font> #51636] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A race condition inside <code>&quot;PerlIOStdio_close()&quot;</code> has been identified and fixed. This used to cause various threading issues, including SEGVs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;unpack&quot;</code>, the use of <code>&quot;()&quot;</code> groups in scalar context was internally placing a list on the interpreter&#8217;s stack, which manifested in various ways, including SEGVs. This is now fixed [<font SIZE="-1">RT</font> #50256]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Magic was called twice in <code>&quot;substr&quot;</code>, <code>&quot;\&amp;$x&quot;</code>, <code>&quot;tie $x, $m&quot;</code> and <code>&quot;chop&quot;</code>. These have all been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A 5.10.0 optimisation to clear the temporary stack within the implicit loop of <code>&quot;s///ge&quot;</code> has been reverted, as it turned out to be the cause of obscure bugs in seemingly unrelated parts of the interpreter [commit ef0d4e17921ee3de]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The line numbers for warnings inside <code>&quot;elsif&quot;</code> are now correct. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;..&quot;</code> operator now works correctly with ranges whose ends are at or close to the values of the smallest and largest integers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;binmode STDIN, &#8216;:raw&#8217;&quot;</code> could lead to segmentation faults on some platforms. This has been fixed [<font SIZE="-1">RT</font> #54828]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An off-by-one error meant that <code>&quot;index $str, ...&quot;</code> was effectively being executed as <code>&quot;index &quot;$str\0&quot;, ...&quot;</code>. This has been fixed [<font SIZE="-1">RT</font> #53746]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various leaks associated with named captures in regexes have been fixed [<font SIZE="-1">RT</font> #57024]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A weak reference to a hash would leak. This was affecting <code>&quot;DBI&quot;</code> [<font SIZE="-1">RT</font> #56908]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using (?|) in a regex could cause a segfault [<font SIZE="-1">RT</font> #59734]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of a <font SIZE="-1">UTF-8</font> <code>&quot;tr//&quot;</code> within a closure could cause a segfault [<font SIZE="-1">RT</font> #61520]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;Perl_sv_chop()&quot;</code> or otherwise upgrading an <font SIZE="-1">SV</font> could result in an unaligned 64-bit access on the <font SIZE="-1">SPARC</font> architecture [<font SIZE="-1">RT</font> #60574]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, <code>&quot;inc_version_list&quot;</code> would incorrectly list <code>&quot;5.10.*&quot;</code> after <code>&quot;5.8.*&quot;</code>; this affected the <code>@INC</code> search order [<font SIZE="-1">RT</font> #67628]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, <code>&quot;pack &quot;a*&quot;, $tainted_value&quot;</code> returned a non-tainted value [<font SIZE="-1">RT</font> #52552]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, <code>&quot;printf&quot;</code> and <code>&quot;sprintf&quot;</code> could produce the fatal error <code>&quot;panic: utf8_mg_pos_cache_update&quot;</code> when printing <font SIZE="-1">UTF-8</font> strings [<font SIZE="-1">RT</font> #62666]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, a dynamically created <code>&quot;AUTOLOAD&quot;</code> method might be missed (method cache issue) [<font SIZE="-1">RT</font> #60220,60232]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the 5.10.0 release, a combination of <code>&quot;use feature&quot;</code> and <code>&quot;//ee&quot;</code> could cause a memory leak [<font SIZE="-1">RT</font> #63110]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-C&quot;</code> on the shebang (<code>&quot;#!&quot;</code>) line is once more permitted if it is also specified on the command line. <code>&quot;-C&quot;</code> on the shebang line used to be a silent no-op <i>if</i> it was not also on the command line, so perl 5.10.0 disallowed it, which broke some scripts. Now perl checks whether it is also on the command line and only dies if it is not [<font SIZE="-1">RT</font> #67880]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In 5.10.0, certain types of re-entrant regular expression could crash, or cause the following assertion failure [<font SIZE="-1">RT</font> #60508]: </p>
<pre><code>    Assertion rx-&gt;sublen &gt;= (s - rx-&gt;subbeg) + i failed
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now includes previously missing files from the Unicode Character Database. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now honors <code>&quot;TMPDIR&quot;</code> when opening an anonymous temporary file. </p>
 </dd></dl>
<h2>Platform Specific Changes</h2>
<p> Perl is incredibly portable. In general, if a platform has a C compiler, someone has ported Perl to it (or will soon). We&#8217;re happy to announce that Perl 5.12 includes support for several new platforms. At the same time, it&#8217;s time to bid farewell to some (very) old friends.  </p>
<h3>New Platforms</h3>
<dl>
<dt>Haiku</dt>
<dd> <p> Perl&#8217;s developers have merged patches from Haiku&#8217;s maintainers. Perl should now build on Haiku. </p>
 </dd>
<dt>MirOS <font SIZE="-1">BSD</font></dt>
<dd> <p> Perl should now build on MirOS <font SIZE="-1">BSD.</font> </p>
 </dd></dl>
<h3>Discontinued Platforms</h3>
<dl>
<dt>Domain/OS</dt>
<dd>  </dd>
<dt>MiNT</dt>
<dd>  </dd>
<dt>Tenon MachTen</dt>
<dd>  </dd></dl>
<h3>Updated Platforms</h3>
<dl>
<dt><font SIZE="-1">AIX</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Removed <i>libbsd</i> for <font SIZE="-1">AIX 5L</font> and 6.1. Only <code>&quot;flock()&quot;</code> was used from <i>libbsd</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Removed <i>libgdbm</i> for <font SIZE="-1">AIX 5L</font> and 6.1 if <i>libgdbm</i> &lt; 1.8.3-5 is installed. The <i>libgdbm</i> is delivered as an optional package with the <font SIZE="-1">AIX</font> Toolbox. Unfortunately the versions below 1.8.3-5 are broken. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hints changes mean that <font SIZE="-1">AIX 4.2</font> should work again. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Cygwin</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl now supports IPv6 on Cygwin 1.7 and newer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Cygwin we now strip the last number from the <font SIZE="-1">DLL.</font> This has been the behaviour in the cygwin.com build for years. The hints files have been updated. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Darwin (Mac <font SIZE="-1">OS X</font>)</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Skip testing the be_BY.CP1131 locale on Darwin 10 (Mac <font SIZE="-1">OS X 10.6</font>), as it&#8217;s still buggy. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Correct infelicities in the regexp used to identify buggy locales on Darwin 8 and 9 (Mac <font SIZE="-1">OS X 10.4</font> and 10.5, respectively). </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>DragonFly <font SIZE="-1">BSD</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Fix thread library selection [perl #69686] </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>FreeBSD</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The hints files now identify the correct threading libraries on FreeBSD 7 and later. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Irix</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> We now work around a bizarre preprocessor bug in the Irix 6.5 compiler: <code>&quot;cc -E -&quot;</code> unfortunately goes into K&amp;R mode, but <code>&quot;cc -E file.c&quot;</code> doesn&#8217;t. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>NetBSD</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Hints now supports versions 5.*. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>OpenVMS</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-UDEBUGGING&quot;</code> is now the default on <font SIZE="-1">VMS.</font> </p>
<p> Like it has been everywhere else for ages and ages. Also make command-line selection of -UDEBUGGING and -DDEBUGGING work in configure.com; before the only way to turn it off was by saying no in answer to the interactive question. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The default pipe buffer size on <font SIZE="-1">VMS</font> has been updated to 8192 on 64-bit systems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reads from the in-memory temporary files of <code>&quot;PerlIO::scalar&quot;</code> used to fail if <code>$/</code> was set to a numeric reference (to indicate record-style reads). This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">VMS</font> now supports <code>&quot;getgrgid&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many improvements and cleanups have been made to the <font SIZE="-1">VMS</font> file name handling and conversion code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Enabling the <code>&quot;PERL_VMS_POSIX_EXIT&quot;</code> logical name now encodes a <font SIZE="-1">POSIX</font> exit status in a <font SIZE="-1">VMS</font> condition value for better interaction with <font SIZE="-1">GNV</font>&#8216;s bash shell and other utilities that depend on <font SIZE="-1">POSIX</font> exit values. See ``$?&#8216;&#8216; in perlvms for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Copy&quot;</code> now detects Unix compatibility mode on <font SIZE="-1">VMS.</font> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Stratus <font SIZE="-1">VOS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Various changes from Stratus have been merged in. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Symbian</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> There is now support for Symbian S60 3.2 <font SIZE="-1">SDK</font> and S60 5.0 <font SIZE="-1">SDK.</font> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Windows</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl 5.12 supports Windows 2000 and later. The supporting code for legacy versions of Windows is still included, but will be removed during the next development cycle. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Initial support for building Perl with MinGW-w64 is now available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perl.exe</i> now includes a manifest resource to specify the <code>&quot;trustInfo&quot;</code> settings for Windows Vista and later. Without this setting Windows would treat <i>perl.exe</i> as a legacy application and apply various heuristics like redirecting access to protected file system areas (like the ``Program Files&#8217;&#8216; folder) to the users ``VirtualStore&#8217;&#8216; instead of generating a proper ``permission denied&#8217;&#8216; error. </p>
<p> The manifest resource also requests the Microsoft Common-Controls version 6.0 (themed controls introduced in Windows <font SIZE="-1">XP</font>). Check out the Win32::VisualStyles module on <font SIZE="-1">CPAN</font> to switch back to old style unthemed controls for legacy applications. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-t&quot;</code> filetest operator now only returns true if the filehandle is connected to a console window. In previous versions of Perl it would return true for all character mode devices, including <i></i><font SIZE="-1"><i>NUL</i></font><i></i> and <i></i><font SIZE="-1"><i>LPT1</i></font><i></i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-p&quot;</code> filetest operator now works correctly, and the Fcntl::S_IFIFO constant is defined when Perl is compiled with Microsoft Visual C. In previous Perl versions <code>&quot;-p&quot;</code> always returned a false value, and the Fcntl::S_IFIFO constant was not defined. </p>
<p> This bug is specific to Microsoft Visual C and never affected Perl binaries built with MinGW. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The socket error codes are now more widely supported: The <font SIZE="-1">POSIX</font> module will define the symbolic names, like <font SIZE="-1">POSIX::EWOULDBLOCK,</font> and stringification of socket error codes in $! works as well now; </p>
<pre><code>  C:\&gt;perl -MPOSIX -E &quot;$!=POSIX::EWOULDBLOCK; say $!&quot;
  A non-blocking socket operation could not be completed immediately.
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>flock()</code> will now set sensible error codes in $!. Previous Perl versions copied the value of $^E into $!, which caused much confusion. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>select()</code> now supports all empty <code>&quot;fd_set&quot;</code>s more correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&#8216;.\foo&#8217;</code> and <code>&#8216;..\foo&#8217;</code> were treated differently than <code>&#8216;./foo&#8217;</code> and <code>&#8216;../foo&#8217;</code> by <code>&quot;do&quot;</code> and <code>&quot;require&quot;</code> [<font SIZE="-1">RT</font> #63492]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improved message window handling means that <code>&quot;alarm&quot;</code> and <code>&quot;kill&quot;</code> messages will no longer be dropped under race conditions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various bits of Perl&#8217;s build infrastructure are no longer converted to win32 line endings at release time. If this hurts you, please report the problem with the perlbug program included with perl. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>Known Problems</h2>
<p> This is a list of some significant unfixed bugs, which are regressions from either 5.10.x or 5.8.x. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Some <font SIZE="-1">CPANPLUS</font> tests may fail if there is a functioning file <i>../../cpanp-run-perl</i> outside your build directory. The failure shouldn&#8217;t imply there&#8217;s a problem with the actual functional software. The bug is already fixed in [<font SIZE="-1">RT</font> #74188] and is scheduled for inclusion in perl-v5.12.1. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;List::Util::first&quot;</code> misbehaves in the presence of a lexical <code>$_</code> (typically introduced by <code>&quot;my $_&quot;</code> or implicitly by <code>&quot;given&quot;</code>). The variable which gets set for each iteration is the package variable <code>$_</code>, not the lexical <code>$_</code> [<font SIZE="-1">RT</font> #67694]. </p>
<p> A similar issue may occur in other modules that provide functions which take a block as their first argument, like </p>
<pre><code>    foo { ... $_ ...} list
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some regexes may run much more slowly when run in a child thread compared with the thread the pattern was compiled into [<font SIZE="-1">RT</font> #55600]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Things like <code>&quot;&quot;\N{LATIN SMALL LIGATURE FF}&quot; =~ /\N{LATIN SMALL LETTER F}+/&quot;</code> will appear to hang as they get into a very long running loop [<font SIZE="-1">RT</font> #72998]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several porters have reported mysterious crashes when Perl&#8217;s entire test suite is run after a build on certain Windows 2000 systems. When run by hand, the individual tests reportedly work fine. </p>
 </dd></dl>
<h2>Errata</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> This one is actually a change introduced in 5.10.0, but it was missed from that release&#8217;s perldelta, so it is mentioned here instead. </p>
<p> A bugfix related to the handling of the <code>&quot;/m&quot;</code> modifier and <code>&quot;qr&quot;</code> resulted in a change of behaviour between 5.8.x and 5.10.0: </p>
<pre><code>    # matches in 5.8.x, doesn't match in 5.10.0
    $re = qr/^bar/; &quot;foo\nbar&quot; =~ /$re/m;
</code></pre>
 </dd></dl>
<h2>Acknowledgements</h2>
<p> Perl 5.12.0 represents approximately two years of development since Perl 5.10.0 and contains over 750,000 lines of changes across over 3,000 files from over 200 authors and committers. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.12.0: </p>
<p> Aaron Crane, Abe Timmerman, Abhijit Menon-Sen, Abigail, Adam Russell, Adriano Ferreira, Ævar Arnfjörð Bjarmason, Alan Grover, Alexandr Ciornii, Alex Davies, Alex Vandiver, Andreas Koenig, Andrew Rodland, andrew [at] sundale.net, Andy Armstrong, Andy Dougherty, Jose AUGUSTE-ETIENNE, Benjamin Smith, Ben Morrow, bharanee rathna, Bo Borgerson, Bo Lindbergh, Brad Gilbert, Bram, Brendan O&#8217;Dea, brian d foy, Charles Bailey, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Christoph Lamprecht, Chris Williams, chromatic, Claes Jakobsson, Craig A. Berry, Dan Dascalescu, Daniel Frederick Crisman, Daniel M. Quinlan, Dan Jacobson, Dan Kogai, Dave Mitchell, Dave Rolsky, David Cantrell, David Dick, David Golden, David Mitchell, David M. Syzdek, David Nicol, David Wheeler, Dennis Kaarsemaker, Dintelmann, Peter, Dominic Dunlop, Dr.Ruud, Duke Leto, Enrico Sorcinelli, Eric Brine, Father Chrysostomos, Florian Ragwitz, Frank Wiegand, Gabor Szabo, Gene Sullivan, Geoffrey T. Dairiki, George Greer, Gerard Goossen, Gisle Aas, Goro Fuji, Graham Barr, Green, Paul, Hans Dieter Pearcey, Harmen, H. Merijn Brand, Hugo van der Sanden, Ian Goodacre, Igor Sutton, Ingo Weinhold, James Bence, James Mastros, Jan Dubois, Jari Aalto, Jarkko Hietaniemi, Jay Hannah, Jerry Hedden, Jesse Vincent, Jim Cromie, Jody Belka, John E. Malmberg, John Malmberg, John Peacock, John Peacock via <font SIZE="-1">RT,</font> John P. Linderman, John Wright, Josh ben Jore, Jos I. Boumans, Karl Williamson, Kenichi Ishigaki, Ken Williams, Kevin Brintnall, Kevin Ryde, Kurt Starsinic, Leon Brocard, Lubomir Rintel, Luke Ross, Marcel Grünauer, Marcus Holland-Moritz, Mark Jason Dominus, Marko Asplund, Martin Hasch, Mashrab Kuvatov, Matt Kraai, Matt S Trout, Max Maischein, Michael Breen, Michael Cartmell, Michael G Schwern, Michael Witten, Mike Giroux, Milosz Tanski, Moritz Lenz, Nicholas Clark, Nick Cleaton, Niko Tyni, Offer Kaye, Osvaldo Villalon, Paul Fenwick, Paul Gaborit, Paul Green, Paul Johnson, Paul Marquess, Philip Hazel, Philippe Bruhat, Rafael Garcia-Suarez, Rainer Tammer, Rajesh Mandalemula, Reini Urban, Renée Bäcker, Ricardo Signes, Ricardo <font SIZE="-1">SIGNES,</font> Richard Foley, Rich Rauenzahn, Rick Delaney, Risto Kankkunen, Robert May, Roberto C. Sanchez, Robin Barker, <font SIZE="-1">SADAHIRO</font> Tomoyuki, Salvador Ortiz Garcia, Sam Vilain, Scott Lanning, Sébastien Aperghis-Tramoni, Sérgio Durigan Júnior, Shlomi Fish, Simon &#8216;corecode&#8217; Schubert, Sisyphus, Slaven Rezic, Smylers, Steffen Müller, Steffen Ullrich, Stepan Kasal, Steve Hay, Steven Schubiger, Steve Peters, Tels, The Doctor, Tim Bunce, Tim Jenness, Todd Rinaldo, Tom Christiansen, Tom Hukins, Tom Wyant, Tony Cook, Torsten Schoenfeld, Tye McQueen, Vadim Konovalov, Vincent Pit, Hio <font SIZE="-1">YAMASHINA,</font> Yasuhiro Matsumoto, Yitzchak Scott-Thoennes, Yuval Kogman, Yves Orton, Zefram, Zsban Ambrus </p>
<p> This is woefully incomplete as it&#8217;s automatically generated from version control history. In particular, it doesn&#8217;t include the names of the (very much appreciated) contributors who reported issues in previous versions of Perl that helped make Perl 5.12.0 better. For a more complete list of all of Perl&#8217;s historical contributors, please see the <code>&quot;AUTHORS&quot;</code> file in the Perl 5.12.0 distribution. </p>
<p> Our ``retired&#8217;&#8216; pumpkings Nicholas Clark and Rafael Garcia-Suarez deserve special thanks for their brilliant and substantive ongoing contributions. Nicholas personally authored over 30% of the patches since 5.10.0. Rafael comes in second in patch authorship with 11%, but is first by a long shot in committing patches authored by others, pushing 44% of the commits since 5.10.0 in this category, often after providing considerable coaching to the patch authors. These statistics in no way comprise all of their contributions, but express in shorthand that we couldn&#8217;t have done it without them. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a>&gt;. There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analyzed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<p> &lt;<a rel="nofollow" href="http://dev.perl.org/perl5/errata.html">http://dev.perl.org/perl5/errata.html</a>&gt; for a list of issues found after this release, as well as a list of <font SIZE="-1">CPAN</font> modules known to be incompatible with this release. </p>
