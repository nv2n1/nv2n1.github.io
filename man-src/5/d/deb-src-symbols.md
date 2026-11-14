---
title: "deb-src-symbols(5)"
name: "deb-src-symbols"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-src-symbols/"
description: "deb-src-symbols – Debian’s extended shared library template file"
---

<p>deb-src-symbols &#8211; Debian&#8217;s extended shared library template file</p>
<h2>Synopsis</h2>
<p><code>debian/</code><i>package</i><code>.symbols.</code><i>arch</i>, <code>debian/symbols.</code><i>arch</i>, <code>debian/</code><i>package</i><code>.symbols</code>, <code>debian/symbols</code></p>
<h2>Description</h2>
<p>The symbol file templates are shipped in Debian source packages, and its format is a superset of the symbols files shipped in binary packages, see <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5).</p>
<h3>Comments</h3>
<p>Comments are supported in template symbol files. Any line with &#8216;#&#8217; as the first character is a comment except if it starts with &#8216;#include&#8217; (see section <code>Using includes</code>). Lines starting with &#8216;#MISSING:&#8217; are special comments documenting symbols that have disappeared.</p>
<h3>Using #PACKAGE# substitution</h3>
<p>In some rare cases, the name of the library varies between architectures. To avoid hardcoding the name of the package in the symbols file, you can use the marker <i>#PACKAGE#</i>. It will be replaced by the real package name during installation of the symbols files. Contrary to the <i>#MINVER#</i> marker, <i>#PACKAGE#</i> will never appear in a symbols file inside a binary package.</p>
<h3>Using symbol tags</h3>
<p>Symbol tagging is useful for marking symbols that are special in some way. Any symbol can have an arbitrary number of tags associated with it. While all tags are parsed and stored, only some of them are understood by <code>dpkg-gensymbols</code> and trigger special handling of the symbols. See subsection <code>Standard symbol tags</code> for reference of these tags. Tag specification comes right before the symbol name (no whitespace is allowed in between). It always starts with an opening bracket <code>(</code>, ends with a closing bracket <code>)</code> and must contain at least one tag. Multiple tags are separated by the <code>|</code> character. Each tag can optionally have a value which is separated form the tag name by the <code>=</code> character. Tag names and values can be arbitrary strings except they cannot contain any of the special <code>)</code> <code>|</code> <code>=</code> characters. Symbol names following a tag specification can optionally be quoted with either <code>&#8216;</code> or <code>&quot;</code> characters to allow whitespaces in them. However, if there are no tags specified for the symbol, quotes are treated as part of the symbol name which continues up until the first space. </p>
<pre> (tag1=i am marked|tag name with space)&quot;tagged quoted symbol&quot;@Base 1.0
 (optional)tagged_unquoted_symbol [at] Base 1.0 1
 untagged_symbol [at] Base 1.0</pre>
<p>The first symbol in the example is named <i>tagged quoted symbol</i> and has two tags: <i>tag1</i> with value <i>i am marked</i> and <i>tag name with space</i> that has no value. The second symbol named <i>tagged_unquoted_symbol</i> is only tagged with the tag named <i>optional</i>. The last symbol is an example of the normal untagged symbol. Since symbol tags are an extension of the <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5) format, they can only be part of the symbols files used in source packages (those files should then be seen as templates used to build the symbols files that are embedded in binary packages). When <code>dpkg-gensymbols</code> is called without the <code>-t</code> option, it will output symbols files compatible to the <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5) format: it fully processes symbols according to the requirements of their standard tags and strips all tags from the output. On the contrary, in template mode (<code>-t</code>) all symbols and their tags (both standard and unknown ones) are kept in the output and are written in their original form as they were loaded.</p>
<h3>Standard symbol tags</h3>
<dl>
<dt><code>optional</code></p>
<dd>A symbol marked as optional can disappear from the library at any time and that will never cause <code>dpkg-gensymbols</code> to fail. However, disappeared optional symbols will continuously appear as <font SIZE="-1">MISSING</font> in the diff in each new package revision. This behaviour serves as a reminder for the maintainer that such a symbol needs to be removed from the symbol file or readded to the library. When the optional symbol, which was previously declared as <font SIZE="-1">MISSING,</font> suddenly reappears in the next revision, it will be upgraded back to the &#8220;existing&#8221; status with its minimum version unchanged. This tag is useful for symbols which are private where their disappearance do not cause <font SIZE="-1">ABI</font> breakage. For example, most of C<font SIZE="-2">++</font> template instantiations fall into this category. Like any other tag, this one may also have an arbitrary value: it could be used to indicate why the symbol is considered optional.</p>
<dt><code>arch=</code><i>architecture-list</i></p>
<dd>
<dt><code>arch-bits=</code><i>architecture-bits</i></p>
<dd>
<dt><code>arch-endian=</code><i>architecture-endianness</i></p>
<dd>These tags allow one to restrict the set of architectures where the symbol is supposed to exist. The <code>arch-bits</code> and <code>arch-endian</code> tags are supported since dpkg 1.18.0. When the symbols list is updated with the symbols discovered in the library, all arch-specific symbols which do not concern the current host architecture are treated as if they did not exist. If an arch-specific symbol matching the current host architecture does not exist in the library, normal procedures for missing symbols apply and it may cause <code>dpkg-gensymbols</code> to fail. On the other hand, if the arch-specific symbol is found when it was not supposed to exist (because the current host architecture is not listed in the tag or does not match the endianness and bits), it is made arch neutral (i.e. the arch, arch-bits and arch-endian tags are dropped and the symbol will appear in the diff due to this change), but it is not considered as new. When operating in the default non-template mode, among arch-specific symbols only those that match the current host architecture are written to the symbols file. On the contrary, all arch-specific symbols (including those from foreign arches) are always written to the symbol file when operating in template mode. The format of <i>architecture-list</i> is the same as the one used in the <code>Build-Depends</code> field of <i>debian/control</i> (except the enclosing square brackets []). For example, the first symbol from the list below will be considered only on alpha, any-amd64 and ia64 architectures, the second only on linux architectures, while the third one anywhere except on armel. </p>
<pre> (arch=alpha any-amd64 ia64)64bit_specific_symbol [at] Base 1.0
 (arch=linux-any)linux_specific_symbol [at] Base 1.0
 (arch=!armel)symbol_armel_does_not_have [at] Base 1.0</pre>
<p>The <i>architecture-bits</i> is either <code>32</code> or <code>64</code>. </p>
<pre> (arch-bits=32)32bit_specific_symbol [at] Base 1.0
 (arch-bits=64)64bit_specific_symbol [at] Base 1.0</pre>
<p>The <i>architecture-endianness</i> is either <code>little</code> or <code>big</code>. </p>
<pre> (arch-endian=little)little_endian_specific_symbol [at] Base 1.0
 (arch-endian=big)big_endian_specific_symbol [at] Base 1.0</pre>
<p>Multiple restrictions can be chained. </p>
<pre> (arch-bits=32|arch-endian=little)32bit_le_symbol [at] Base 1.0</pre>
<dt><code>allow-internal</code></p>
<dd>dpkg-gensymbols has a list of internal symbols that should not appear in symbols files as they are usually only side-effects of implementation details of the toolchain (since dpkg 1.20.1). If for some reason, you really want one of those symbols to be included in the symbols file, you should tag the symbol with <code>allow-internal</code>. It can be necessary for some low level toolchain libraries like &#8220;libgcc&#8221;.</p>
<dt><code>ignore-blacklist</code></p>
<dd>A deprecated alias for <code>allow-internal</code> (since dpkg 1.20.1, supported since dpkg 1.15.3).</p>
<dt><code>c++</code></p>
<dd>Denotes <i>c++</i> symbol pattern. See <code>Using symbol patterns</code> subsection below.</p>
<dt><code>symver</code></p>
<dd>Denotes <i>symver</i> (symbol version) symbol pattern. See <code>Using symbol patterns</code> subsection below.</p>
<dt><code>regex</code></p>
<dd>Denotes <i>regex</i> symbol pattern. See <code>Using symbol patterns</code> subsection below.</dl>
<h3>Using symbol patterns</h3>
<p>Unlike a standard symbol specification, a pattern may cover multiple real symbols from the library. <code>dpkg-gensymbols</code> will attempt to match each pattern against each real symbol that does <i>not</i> have a specific symbol counterpart defined in the symbol file. Whenever the first matching pattern is found, all its tags and properties will be used as a basis specification of the symbol. If none of the patterns matches, the symbol will be considered as new. A pattern is considered lost if it does not match any symbol in the library. By default this will trigger a <code>dpkg-gensymbols</code> failure under <code>-c1</code> or higher level. However, if the failure is undesired, the pattern may be marked with the <i>optional</i> tag. Then if the pattern does not match anything, it will only appear in the diff as <font SIZE="-1">MISSING.</font> Moreover, like any symbol, the pattern may be limited to the specific architectures with the <i>arch</i> tag. Please refer to <code>Standard symbol tags</code> subsection above for more information. Patterns are an extension of the <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5) format hence they are only valid in symbol file templates. Pattern specification syntax is not any different from the one of a specific symbol. However, symbol name part of the specification serves as an expression to be matched against <i>name [at] version</i> of the real symbol. In order to distinguish among different pattern types, a pattern will typically be tagged with a special tag. At the moment, <code>dpkg-gensymbols</code> supports three basic pattern types:</p>
<dl>
<dt><code>c++</code></p>
<dd>This pattern is denoted by the <i>c++</i> tag. It matches only C<font SIZE="-2">++</font> symbols by their demangled symbol name (as emitted by <code>c++<a href="/docs/linux/man/1-filt/">filt</a></code>(1) utility). This pattern is very handy for matching symbols which mangled names might vary across different architectures while their demangled names remain the same. One group of such symbols is <i>non-virtual thunks</i> which have architecture specific offsets embedded in their mangled names. A common instance of this case is a virtual destructor which under diamond inheritance needs a non-virtual thunk symbol. For example, even if _ZThn8_N3NSB6ClassDD1Ev [at] Base on 32bit architectures will probably be _ZThn16_N3NSB6ClassDD1Ev [at] Base on 64bit ones, it can be matched with a single <i>c++</i> pattern: </p>
<pre> libdummy.so.1 libdummy1 #MINVER#
 [...]
 (c++)&quot;non-virtual thunk to NSB::ClassD::~ClassD()@Base&quot; 1.0
 [...]</pre>
<p>The demangled name above can be obtained by executing the following command: </p>
<pre> $ echo '_ZThn8_N3NSB6ClassDD1Ev [at] Base' | c++filt</pre>
<p>Please note that while mangled name is unique in the library by definition, this is not necessarily true for demangled names. A couple of distinct real symbols may have the same demangled name. For example, that&#8217;s the case with non-virtual thunk symbols in complex inheritance configurations or with most constructors and destructors (since g++ typically generates two real symbols for them). However, as these collisions happen on the <font SIZE="-1">ABI</font> level, they should not degrade quality of the symbol file.</p>
<dt><code>symver</code></p>
<dd>This pattern is denoted by the <i>symver</i> tag. Well maintained libraries have versioned symbols where each version corresponds to the upstream version where the symbol got added. If that&#8217;s the case, you can use a <i>symver</i> pattern to match any symbol associated to the specific version. For example: </p>
<pre> libc.so.6 libc6 #MINVER#
 (symver)GLIBC_2.0 2.0
 [...]
 (symver)GLIBC_2.7 2.7
 access [at] GLIBC_2.0 2.2</pre>
<p>All symbols associated with versions <font SIZE="-1">GLIBC_2.0</font> and <font SIZE="-1">GLIBC_2.7</font> will lead to minimal version of 2.0 and 2.7 respectively with the exception of the symbol access [at] GLIBC_2.0. The latter will lead to a minimal dependency on libc6 version 2.2 despite being in the scope of the &#8220;(symver)GLIBC_2.0&#8221; pattern because specific symbols take precedence over patterns. Please note that while old style wildcard patterns (denoted by &#8220;*@version&#8221; in the symbol name field) are still supported, they have been deprecated by new style syntax &#8220;(symver|optional)version&#8221;. For example, &#8220;*@GLIBC_2.0 2.0&#8221; should be written as &#8220;(symver|optional)GLIBC_2.0 2.0&#8221; if the same behaviour is needed.</p>
<dt><code>regex</code></p>
<dd>Regular expression patterns are denoted by the <i>regex</i> tag. They match by the perl regular expression specified in the symbol name field. A regular expression is matched as it is, therefore do not forget to start it with the <i>^</i> character or it may match any part of the real symbol <i>name [at] version</i> string. For example: </p>
<pre> libdummy.so.1 libdummy1 #MINVER#
 (regex)&quot;^mystack_.*@Base$&quot; 1.0
 (regex|optional)&quot;private&quot; 1.0</pre>
<p>Symbols like &#8220;mystack_new [at] Base&#8221;, &#8220;mystack_push [at] Base&#8221;, &#8220;mystack_pop [at] Base&#8221; etc. will be matched by the first pattern while e.g. &#8220;ng_mystack_new [at] Base&#8221; won&#8217;t. The second pattern will match all symbols having the string &#8220;private&#8221; in their names and matches will inherit <i>optional</i> tag from the pattern.</dl>
<p> Basic patterns listed above can be combined where it makes sense. In that case, they are processed in the order in which the tags are specified. For example, both: </p>
<pre> (c++|regex)&quot;^NSA::ClassA::Private::privmethod\d\(int\)@Base&quot; 1.0
 (regex|c++)N3NSA6ClassA7Private11privmethod\dEi [at] Base 1.0</pre>
<p>will match symbols &#8220;_ZN3NSA6ClassA7Private11privmethod1Ei [at] Base&#8221; and &#8220;_ZN3NSA6ClassA7Private11privmethod2Ei [at] Base&#8221;. When matching the first pattern, the raw symbol is first demangled as C<font SIZE="-2">++</font> symbol, then the demangled name is matched against the regular expression. On the other hand, when matching the second pattern, regular expression is matched against the raw symbol name, then the symbol is tested if it is C<font SIZE="-2">++</font> one by attempting to demangle it. A failure of any basic pattern will result in the failure of the whole pattern. Therefore, for example, &#8220;__N3NSA6ClassA7Private11privmethod\dEi [at] Base&#8221; will not match either of the patterns because it is not a valid C<font SIZE="-2">++</font> symbol. In general, all patterns are divided into two groups: aliases (basic <i>c++</i> and <i>symver</i>) and generic patterns (<i>regex</i>, all combinations of multiple basic patterns). Matching of basic alias-based patterns is fast (<a href="/docs/linux/man/1-o/">O</a>(1)) while generic patterns are O(N) (N &#8211; generic pattern count) for each symbol. Therefore, it is recommended not to overuse generic patterns. When multiple patterns match the same real symbol, aliases (first <i>c++</i>, then <i>symver</i>) are preferred over generic patterns. Generic patterns are matched in the order they are found in the symbol file template until the first success. Please note, however, that manual reordering of template file entries is not recommended because <code>dpkg-gensymbols</code> generates diffs based on the alphanumerical order of their names.</p>
<h3>Using includes</h3>
<p>When the set of exported symbols differ between architectures, it may become inefficient to use a single symbol file. In those cases, an include directive may prove to be useful in a couple of ways:</p>
<dl>
<dt>&bull;</p>
<dd>You can factorize the common part in some external file and include that file in your <i>package</i>.symbols.<i>arch</i> file by using an include directive like this: </p>
<pre><code>#include &quot;I&lt;packages&gt;.symbols.common&quot;



&bull;
The include directive may also be tagged like any symbol:
(tag|...|tagN)#include &quot;file-to-include&quot;</code></pre>
<p> As a result, all symbols included from <i>file-to-include</i> will be considered to be tagged with <i>tag</i> &#8230; <i>tagN</i> by default. You can use this feature to create a common <i>package</i>.symbols file which includes architecture specific symbol files: common_symbol1 [at] Base 1.0<br />
(arch=amd64 ia64 alpha)#include &quot;package.symbols.64bit&quot;<br />
(arch=!amd64 !ia64 !alpha)#include &quot;package.symbols.32bit&quot;<br />
common_symbol2 [at] Base 1.0 The symbols files are read line by line, and include directives are processed as soon as they are encountered. This means that the content of the included file can override any content that appeared before the include directive and that any content after the directive can override anything contained in the included file. Any symbol (or even another #include directive) in the included file can specify additional tags or override values of the inherited tags in its tag specification. However, there is no way for the symbol to remove any of the inherited tags. An included file can repeat the header line containing the <font SIZE="-1">SONAME</font> of the library. In that case, it overrides any header line previously read. However, in general it&#8217;s best to avoid duplicating header lines. One way to do it is the following: </p>
<pre><code>#include &quot;libsomething1.symbols.common&quot;
arch_specific_symbol [at] Base 1.0</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-gensymbols/">dpkg-gensymbols</a></code>(1). </p>
