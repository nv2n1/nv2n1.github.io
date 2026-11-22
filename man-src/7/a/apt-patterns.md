---
title: "apt-patterns(7)"
name: "apt-patterns"
section: "7"
letter: "a"
url: "/docs/linux/man/7-apt-patterns/"
description: "apt-patterns – Syntax and semantics of apt search patterns"
---

<p>apt-patterns &#8211; Syntax and semantics of apt search patterns</p>
<h2>Description</h2>
<p>Starting with version 2.0, <code>APT</code> provides support for patterns, which can be used to query the apt cache for packages.</p>
<h2>Logic Patterns</h2>
<p>These patterns provide the basic means to combine other patterns into more complex expressions, as well as ?true and ?false patterns. </p>
<p> ?and(PATTERN, PATTERN, &#8230;), PATTERN PATTERN &#8230;</p>
<dl>
<dd>Selects objects where all specified patterns match.</dd></dl>
<p> ?false, ~F</p>
<dl>
<dd>Selects nothing.</dd></dl>
<p> ?not(PATTERN), !PATTERN</p>
<dl>
<dd>Selects objects where PATTERN does not match.</dd></dl>
<p> ?or(PATTERN, PATTERN, &#8230;), PATTERN | PATTERN | &#8230;</p>
<dl>
<dd>Selects objects where at least one of the specified patterns match.</dd></dl>
<p> ?true, ~T</p>
<dl>
<dd>Selects all objects.</dd></dl>
<p> (PATTERN)</p>
<dl>
<dd>Selects the same as PATTERN, can be used to work around precedence, for example, (~ramd64|~ri386)~nfoo</dd></dl>
<h2>Narrowing Patterns</h2>
<p>?all-versions(PATTERN)</p>
<dl>
<dd>Selects packages where all versions match PATTERN. When matching versions instead, same as PATTERN.</dd></dl>
<p> ?any-version(PATTERN)</p>
<dl>
<dd>Selects any version where the pattern matches on the version. </dd>
<p> For example, while ?and(?version(1),?version(2)) matches a package which has one version containing 1 and one version containing 2, ?any-version(?and(?version(1),?version(2))) restricts the ?and to act on the same version.</dl>
<p> ?narrow(PATTERN&#8230;)</p>
<dl>
<dd>Selects any version matching all PATTERNs, short for ?any-version(?and(PATTERN&#8230;)).</dd></dl>
<h2>Package Patterns</h2>
<p>These patterns select specific packages. </p>
<p> ?architecture(WILDCARD), ~rWILDCARD</p>
<dl>
<dd>Selects packages matching the specified architecture, which may contain wildcards using any.</dd></dl>
<p> ?automatic, ~M</p>
<dl>
<dd>Selects packages that were installed automatically.</dd></dl>
<p> ?broken, ~b</p>
<dl>
<dd>Selects packages that have broken dependencies.</dd></dl>
<p> ?config-files, ~c</p>
<dl>
<dd>Selects packages that are not fully installed, but have solely residual configuration files left.</dd></dl>
<p> ?essential, ~E</p>
<dl>
<dd>Selects packages that have Essential: yes set in their control file.</dd></dl>
<p> ?exact-name(NAME)</p>
<dl>
<dd>Selects packages with the exact specified name.</dd></dl>
<p> ?garbage, ~g</p>
<dl>
<dd>Selects packages that can be removed automatically.</dd></dl>
<p> ?installed, ~i</p>
<dl>
<dd>Selects packages that are currently installed.</dd></dl>
<p> ?name(REGEX), ~nREGEX</p>
<dl>
<dd>Selects packages where the name matches the given regular expression.</dd></dl>
<p> ?obsolete, ~o</p>
<dl>
<dd>Selects packages that no longer exist in repositories.</dd></dl>
<p> ?upgradable, ~U</p>
<dl>
<dd>Selects packages that can be upgraded (have a newer candidate).</dd></dl>
<p> ?virtual, ~v</p>
<dl>
<dd>Selects all virtual packages; that is packages without a version. These exist when they are referenced somewhere in the archive, for example because something depends on that name.</dd></dl>
<h2>Version Patterns</h2>
<p>These patterns select specific versions of a package. </p>
<p> ?archive(REGEX), ~AREGEX</p>
<dl>
<dd>Selects versions that come from the archive that matches the specified regular expression. Archive, here, means the values after a= in <code>apt-cache policy</code>.</dd></dl>
<p> ?codename(REGEX)</p>
<dl>
<dd>Selects versions that come from the codename that matches the specified regular expression. Codename, here, means the values after n= in <code>apt-cache policy</code>.</dd></dl>
<p> ?origin(REGEX), ~OREGEX</p>
<dl>
<dd>Selects versions that come from the origin that matches the specified regular expression. Origin, here, means the values after o= in <code>apt-cache policy</code>.</dd></dl>
<p> ?section(REGEX), ~sREGEX</p>
<dl>
<dd>Selects versions where the section matches the specified regular expression.</dd></dl>
<p> ?source-package(REGEX), ~eREGEX</p>
<dl>
<dd>Selects versions where the source package name matches the specified regular expression.</dd></dl>
<p> ?source-version(REGEX)</p>
<dl>
<dd>Selects versions where the source package version matches the specified regular expression.</dd></dl>
<p> ?version(REGEX), ~VREGEX</p>
<dl>
<dd>Selects versions where the version string matches the specified regular expression.</dd></dl>
<p> ?priority(NAME), ~pNAME</p>
<dl>
<dd>Selects versions where the Priority string equals the given name.</dd></dl>
<h2>Package Relationship Patterns</h2>
<p>These patterns match specific package versions that depend/conflict with some other packages. </p>
<p> ?depends(PATTERN), ~DPATTERN, ?pre-depends(PATTERN), ~DPre-Depends:PATTERN, ?suggests(PATTERN), ~DSuggests:PATTERN, ?conflicts(PATTERN), ~DConflicts:PATTERN, ?replaces(PATTERN), ~DReplaces:PATTERN, ?obsoletes(PATTERN), ~DObsoletes:PATTERN, ?breaks(PATTERN), ~DBreaks:PATTERN, ?enhances(PATTERN), ~DEnhances:PATTERN</p>
<dl>
<dd>Selects versions depending/pre-depending/suggesting/conflicting/etc on/with/ packages matching PATTERN.</dd></dl>
<p> ?reverse-<i>depType</i>(PATTERN), ~R<i>DepType</i>:PATTERN</p>
<dl>
<dd>Opposite of ?depends and friends &#8211; selects all packages that have reverse-dependencies (versions) matching PATTERN. </dd>
<p> <i>depType</i> is one of the dependency types such as depends, so that we don&#8217;t have to repeat the entire list from the first paragraph here.</dl>
<h2>Examples</h2>
<p>apt remove ?garbage</p>
<dl>
<dd>Remove all packages that are automatically installed and no longer needed &#8211; same as apt autoremove</dd></dl>
<p> apt purge ?config-files</p>
<dl>
<dd>Purge all packages that only have configuration files left</dd></dl>
<p> apt list &#8216;~i !~M (~slibs|~sperl|~spython)&#8217;</p>
<dl>
<dd>List all manually-installed packages in sections matching libs, perl, or python.</dd></dl>
<h2>Migrating From Aptitude</h2>
<p>Patterns in apt are heavily inspired by patterns in aptitude, but with some tweaks: </p>
<dl>
<dd>&bull; Syntax is uniform: If there is an opening parenthesis after a term, it is always assumed to be the beginning of an argument list. </dd>
<p> In aptitude, a syntactic form &quot;?foo(bar)&quot; could mean &quot;?and(?foo,bar)&quot; if foo does not take an argument. In APT, this will cause an error.</dl>
<dl>
<dd>&bull; Not all patterns are supported.</dd></dl>
<dl>
<dd>&bull; Some additional patterns are available, for example, for finding gstreamer codecs.</dd></dl>
<dl>
<dd>&bull; Escaping terms with ~ is not supported.</dd></dl>
<dl>
<dd>&bull; A trailing comma is allowed in argument lists</dd></dl>
<dl>
<dd>&bull; ?narrow accepts infinite arguments</dd></dl>
<dl>
<dd>&bull; foo cannot be used as a shortform for ?name(foo), as this can cause typos to go unnoticed: Consider ?and(&#8230;,~poptional): this requires the package to have required priority, but if you do not type the ~, it would require the package name to contain poptional.</dd></dl>
<dl>
<dd>&bull; Grouping patterns with (&#8230;) or writing ?or(A,B) as A|B are not supported. We do not believe that the use of | is that common, and the grouping is not necessary without it.</dd></dl>
<dl>
<dd>&bull; Dependency types for ~D and related operators need to be specified in the canonical case.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8)</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[][1]. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code>reportbug</code>(1) command.</p>
<h2>Author</h2>
<p>APT was written by the APT team &lt;apt [at] packages.debian.org&gt;.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>APT bug page</dd>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dd></dl>
</dl>