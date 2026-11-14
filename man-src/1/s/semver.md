---
title: "semver(1)"
name: "semver"
section: "1"
letter: "s"
url: "/docs/linux/man/1-semver/"
description: "semver – The semantic versioner for npm"
---

<h2 class="name">NAME</h2>
<p> <code>semver</code> &#8211; The semantic versioner for npm </p>
<h2>Install</h2>
<dl>
<dt>
<dd>
<pre>
npm install semver
`
</pre>
</dl>
<h2>Usage</h2>
<p> As a node module: </p>
<dl>
<dt>
<dd>
<pre><code>
const semver = require('semver')
                   semver.valid('1.2.3')                                    // '1.2.3'
               semver.valid('a.b.c')                                        // null
               semver.clean('  =v1.2.3   ')                                 // '1.2.3'
               semver.satisfies('1.2.3', '1.x || &gt;=2.5.0 || 5.0.0 - 7.2.3') // true
               semver.gt('1.2.3', '9.8.7')                                  // false
               semver.lt('1.2.3', '9.8.7')                                  // true
               semver.minVersion('&gt;=1.0.0')                                 // '1.0.0'
               semver.valid(semver.coerce('v2'))                            // '2.0.0'
               semver.valid(semver.coerce('42.6.7.9.3-alpha'))              // '42.6.7'
</code></pre>
</dl>
<p> You can also just load the module for the function that you care about, if you&#8217;d like to minimize your footprint. </p>
<dl>
<dt>
<dd>
// load the whole API at once in a single object<br />
const semver = require(&#8216;semver&#8217;)<br />
    // or just load the bits you need<br />
    // all of them listed here, just pick and choose what you want<br />
    // classes<br />
    const SemVer = require(&#8216;semver/classes/semver&#8217;)<br />
        const Comparator = require(&#8216;semver/classes/comparator&#8217;)<br />
            const Range = require(&#8216;semver/classes/range&#8217;)<br />
    // functions for working with versions<br />
    const semverParse = require(&#8216;semver/functions/parse&#8217;)<br />
        const semverValid = require(&#8216;semver/functions/valid&#8217;)<br />
            const semverClean = require(&#8216;semver/functions/clean&#8217;)<br />
                const semverInc = require(&#8216;semver/functions/inc&#8217;)<br />
                    const semverDiff = require(&#8216;semver/functions/diff&#8217;)<br />
                        const semverMajor = require(&#8216;semver/functions/major&#8217;)<br />
                            const semverMinor = require(&#8216;semver/functions/minor&#8217;)<br />
                                const semverPatch = require(&#8216;semver/functions/patch&#8217;)<br />
                                    const semverPrerelease = require(&#8216;semver/functions/prerelease&#8217;)<br />
                                        const semverCompare = require(&#8216;semver/functions/compare&#8217;)<br />
                                            const semverRcompare = require(&#8216;semver/functions/rcompare&#8217;)<br />
                                                const semverCompareLoose = require(&#8216;semver/functions/compare-loose&#8217;)<br />
                                                    const semverCompareBuild = require(&#8216;semver/functions/compare-build&#8217;)<br />
                                                        const semverSort = require(&#8216;semver/functions/sort&#8217;)<br />
                                                            const semverRsort = require(&#8216;semver/functions/rsort&#8217;)<br />
    // low-level comparators between versions<br />
    const semverGt = require(&#8216;semver/functions/gt&#8217;)<br />
        const semverLt = require(&#8216;semver/functions/lt&#8217;)<br />
            const semverEq = require(&#8216;semver/functions/eq&#8217;)<br />
                const semverNeq = require(&#8216;semver/functions/neq&#8217;)<br />
                    const semverGte = require(&#8216;semver/functions/gte&#8217;)<br />
                        const semverLte = require(&#8216;semver/functions/lte&#8217;)<br />
                            const semverCmp = require(&#8216;semver/functions/cmp&#8217;)<br />
                                const semverCoerce = require(&#8216;semver/functions/coerce&#8217;)<br />
    // working with ranges<br />
    const semverSatisfies = require(&#8216;semver/functions/satisfies&#8217;)<br />
        const semverMaxSatisfying = require(&#8216;semver/ranges/max-satisfying&#8217;)<br />
            const semverMinSatisfying = require(&#8216;semver/ranges/min-satisfying&#8217;)<br />
                const semverToComparators = require(&#8216;semver/ranges/to-comparators&#8217;)<br />
                    const semverMinVersion = require(&#8216;semver/ranges/min-version&#8217;)<br />
                        const semverValidRange = require(&#8216;semver/ranges/valid&#8217;)<br />
                            const semverOutside = require(&#8216;semver/ranges/outside&#8217;)<br />
                                const semverGtr = require(&#8216;semver/ranges/gtr&#8217;)<br />
                                    const semverLtr = require(&#8216;semver/ranges/ltr&#8217;)<br />
                                        const semverIntersects = require(&#8216;semver/ranges/intersects&#8217;)
</dl>
<p> As a command-line utility: </p>
<dl>
<dt>
<dd>
$ semver &#8211; h A JavaScript implementation of the https : // semver.org/ specification<br />
                                                        Copyright Isaac Z.Schlueter Usage : semver[options]&lt;version&gt;[&lt;version&gt;[&#8230;]] Prints valid versions sorted by SemVer precedence Options : -r&#8211; range&lt;range&gt;<br />
                                                                                                                                                                                                     Print versions that match the specified range.-<br />
    i&#8211; increment[&lt;level&gt;] Increment a version by the specified level.Level can<br />
        be one of : major,<br />
    minor, patch, premajor, preminor,<br />
    prepatch, or prerelease.Default level is &#8216;patch&#8217;.Only one version may be specified.&#8211;preid&lt;identifier&gt;<br />
                      Identifier to be used to prefix premajor,<br />
    preminor,<br />
    prepatch or prerelease version increments.- l&#8211; loose Interpret versions and ranges loosely &#8211; p&#8211; include &#8211; prerelease Always include prerelease versions in range matching &#8211; c&#8211; coerce Coerce a string into SemVer if possible (does not imply&#8211; loose)&#8211; rtl Coerce version strings right to left&#8211; ltr Coerce version strings left to right(default) Program exits successfully if any valid version satisfies all supplied ranges, and prints all satisfying versions.If no satisfying versions are found, then exits failure.Versions are printed in ascending order, so supplying multiple versions to the utility will just sort them.
</dl>
<h2>Versions</h2>
<p> A &quot;version&quot; is described by the <code>v2.0.0</code> specification found at <a rel="nofollow" href="https://semver.org/.">https://semver.org/.</a> </p>
<p> A leading <code>&quot;=&quot;</code> or <code>&quot;v&quot;</code> character is stripped off and ignored.</p>
<h2>Ranges</h2>
<p> A <code>version range</code> is a set of <code>comparators</code> which specify versions that satisfy the range. </p>
<p> A <code>comparator</code> is composed of an <code>operator</code> and a <code>version</code>. The set of primitive <code>operators</code> is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>&lt;</code> Less than</p>
<dt>&bull;</p>
<dd> <code>&lt;=</code> Less than or equal to</p>
<dt>&bull;</p>
<dd> <code>&gt;</code> Greater than</p>
<dt>&bull;</p>
<dd> <code>&gt;=</code> Greater than or equal to</p>
<dt>&bull;</p>
<dd> <code>=</code> Equal. If no operator is specified, then equality is assumed, so this operator is optional, but MAY be included. </p>
</dl>
</dl>
<p> For example, the comparator <code>&gt;=1.2.7</code> would match the versions <code>1.2.7</code>, <code>1.2.8</code>, <code>2.5.3</code>, and <code>1.3.9</code>, but not the versions <code>1.2.6</code> or <code>1.1.0</code>. </p>
<p> Comparators can be joined by whitespace to form a <code>comparator set</code>, which is satisfied by the <code>intersection</code> of all of the comparators it includes. </p>
<p> A range is composed of one or more comparator sets, joined by <code>||</code>. A version matches a range if and only if every comparator in at least one of the <code>||</code>-separated comparator sets is satisfied by the version. </p>
<p> For example, the range <code>&gt;=1.2.7 &lt;1.3.0</code> would match the versions <code>1.2.7</code>, <code>1.2.8</code>, and <code>1.2.99</code>, but not the versions <code>1.2.6</code>, <code>1.3.0</code>, or <code>1.1.0</code>. </p>
<p> The range <code>1.2.7 || &gt;=1.2.9 &lt;2.0.0</code> would match the versions <code>1.2.7</code>, <code>1.2.9</code>, and <code>1.4.6</code>, but not the versions <code>1.2.8</code> or <code>2.0.0</code>.</p>
<h3>Prerelease Tags</h3>
<p> If a version has a prerelease tag (for example, <code>1.2.3-alpha.3</code>) then it will only be allowed to satisfy comparator sets if at least one comparator with the same <code>[major, minor, patch]</code> tuple also has a prerelease tag. </p>
<p> For example, the range <code>&gt;1.2.3-alpha.3</code> would be allowed to match the version <code>1.2.3-alpha.7</code>, but it would <i>not</i> be satisfied by <code>3.4.5-alpha.9</code>, even though <code>3.4.5-alpha.9</code> is technically &quot;greater than&quot; <code>1.2.3-alpha.3</code> according to the SemVer sort rules. The version range only accepts prerelease tags on the <code>1.2.3</code> version. The version <code>3.4.5</code> <i>would</i> satisfy the range, because it does not have a prerelease flag, and <code>3.4.5</code> is greater than <code>1.2.3-alpha.7</code>. </p>
<p> The purpose for this behavior is twofold. First, prerelease versions frequently are updated very quickly, and contain many breaking changes that are (by the author&#8217;s design) not yet fit for public consumption. Therefore, by default, they are excluded from range matching semantics. </p>
<p> Second, a user who has opted into using a prerelease version has clearly indicated the intent to use <i>that specific</i> set of alpha/beta/rc versions. By including a prerelease tag in the range, the user is indicating that they are aware of the risk. However, it is still not appropriate to assume that they have opted into taking a similar risk on the <i>next</i> set of prerelease versions. </p>
<p> Note that this behavior can be suppressed (treating all prerelease versions as if they were normal versions, for the purpose of range matching) by setting the <code>includePrerelease</code> flag on the options object to any functions <i><a rel="nofollow" href="https://github.com/npm/node-semver#functions">https://github.com/npm/node-semver#functions</a></i> that do range matching.</p>
<h3>Prerelease Identifiers</h3>
<p> The method <code>.inc</code> takes an additional <code>identifier</code> string argument that will append the value of the string as a prerelease identifier: </p>
<dl>
<dt>
<dd>
<pre>
semver.inc('1.2.3', 'prerelease', 'beta')
// '1.2.4-beta.0'
</pre>
</dl>
<p> command-line example: </p>
<dl>
<dt>
<dd>
<pre>
$ semver 1.2.3 -i prerelease --preid beta
1.2.4-beta.0
</pre>
</dl>
<p> Which then can be used to increment further: </p>
<dl>
<dt>
<dd>
<pre>
$ semver 1.2.4-beta.0 -i prerelease
1.2.4-beta.1
</pre>
</dl>
<h3>Advanced Range Syntax</h3>
<p> Advanced range syntax desugars to primitive comparators in deterministic ways. </p>
<p> Advanced ranges may be combined in the same way as primitive comparators using white space or <code>||</code>.</p>
<h3>Hyphen Ranges <code>X.Y.Z &#8211; A.B.C</code></h3>
<p> Specifies an inclusive set.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>1.2.3 &#8211; 2.3.4</code> := <code>&gt;=1.2.3 &lt;=2.3.4</code> </p>
</dl>
</dl>
<p> If a partial version is provided as the first version in the inclusive range, then the missing pieces are replaced with zeroes.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>1.2 &#8211; 2.3.4</code> := <code>&gt;=1.2.0 &lt;=2.3.4</code> </p>
</dl>
</dl>
<p> If a partial version is provided as the second version in the inclusive range, then all versions that start with the supplied parts of the tuple are accepted, but nothing that would be greater than the provided tuple parts.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>1.2.3 &#8211; 2.3</code> := <code>&gt;=1.2.3 &lt;2.4.0</code></p>
<dt>&bull;</p>
<dd> <code>1.2.3 &#8211; 2</code> := <code>&gt;=1.2.3 &lt;3.0.0</code> </p>
</dl>
</dl>
<h3>X-Ranges <code>1.2.x</code> <code>1.X</code> <code>1.2.*</code> <code>*</code></h3>
<p> Any of <code>X</code>, <code>x</code>, or <code>*</code> may be used to &quot;stand in&quot; for one of the numeric values in the <code>[major, minor, patch]</code> tuple.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>*</code> := <code>&gt;=0.0.0</code> (Any version satisfies)</p>
<dt>&bull;</p>
<dd> <code>1.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code> (Matching major version)</p>
<dt>&bull;</p>
<dd> <code>1.2.x</code> := <code>&gt;=1.2.0 &lt;1.3.0</code> (Matching major and minor versions) </p>
</dl>
</dl>
<p> A partial version range is treated as an X-Range, so the special character is in fact optional.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>&quot;&quot;</code> (empty string) := <code>*</code> := <code>&gt;=0.0.0</code></p>
<dt>&bull;</p>
<dd> <code>1</code> := <code>1.x.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd> <code>1.2</code> := <code>1.2.x</code> := <code>&gt;=1.2.0 &lt;1.3.0</code> </p>
</dl>
</dl>
<h3>Tilde Ranges <code>~1.2.3</code> <code>~1.2</code> <code>~1</code></h3>
<p> Allows patch-level changes if a minor version is specified on the comparator. Allows minor-level changes if not.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>~1.2.3</code> := <code>&gt;=1.2.3 &lt;1.(2+1).0</code> := <code>&gt;=1.2.3 &lt;1.3.0</code></p>
<dt>&bull;</p>
<dd> <code>~1.2</code> := <code>&gt;=1.2.0 &lt;1.(2+1).0</code> := <code>&gt;=1.2.0 &lt;1.3.0</code> (Same as <code>1.2.x</code>)</p>
<dt>&bull;</p>
<dd> <code>~1</code> := <code>&gt;=1.0.0 &lt;(1+1).0.0</code> := <code>&gt;=1.0.0 &lt;2.0.0</code> (Same as <code>1.x</code>)</p>
<dt>&bull;</p>
<dd> <code>~0.2.3</code> := <code>&gt;=0.2.3 &lt;0.(2+1).0</code> := <code>&gt;=0.2.3 &lt;0.3.0</code></p>
<dt>&bull;</p>
<dd> <code>~0.2</code> := <code>&gt;=0.2.0 &lt;0.(2+1).0</code> := <code>&gt;=0.2.0 &lt;0.3.0</code> (Same as <code>0.2.x</code>)</p>
<dt>&bull;</p>
<dd> <code>~0</code> := <code>&gt;=0.0.0 &lt;(0+1).0.0</code> := <code>&gt;=0.0.0 &lt;1.0.0</code> (Same as <code>0.x</code>)</p>
<dt>&bull;</p>
<dd> <code>~1.2.3-beta.2</code> := <code>&gt;=1.2.3-beta.2 &lt;1.3.0</code> Note that prereleases in the <code>1.2.3</code> version will be allowed, if they are greater than or equal to <code>beta.2</code>. So, <code>1.2.3-beta.4</code> would be allowed, but <code>1.2.4-beta.2</code> would not, because it is a prerelease of a different <code>[major, minor, patch]</code> tuple. </p>
</dl>
</dl>
<h3>Caret Ranges <code>^1.2.3</code> <code>^0.2.5</code> <code>^0.0.4</code></h3>
<p> Allows changes that do not modify the left-most non-zero element in the <code>[major, minor, patch]</code> tuple. In other words, this allows patch and minor updates for versions <code>1.0.0</code> and above, patch updates for versions <code>0.X &gt;=0.1.0</code>, and <i>no</i> updates for versions <code>0.0.X</code>. </p>
<p> Many authors treat a <code>0.x</code> version as if the <code>x</code> were the major &quot;breaking-change&quot; indicator. </p>
<p> Caret ranges are ideal when an author may make breaking changes between <code>0.2.4</code> and <code>0.3.0</code> releases, which is a common practice. However, it presumes that there will <i>not</i> be breaking changes between <code>0.2.4</code> and <code>0.2.5</code>. It allows for changes that are presumed to be additive (but non-breaking), according to commonly observed practices.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>^1.2.3</code> := <code>&gt;=1.2.3 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd> <code>^0.2.3</code> := <code>&gt;=0.2.3 &lt;0.3.0</code></p>
<dt>&bull;</p>
<dd> <code>^0.0.3</code> := <code>&gt;=0.0.3 &lt;0.0.4</code></p>
<dt>&bull;</p>
<dd> <code>^1.2.3-beta.2</code> := <code>&gt;=1.2.3-beta.2 &lt;2.0.0</code> Note that prereleases in the <code>1.2.3</code> version will be allowed, if they are greater than or equal to <code>beta.2</code>. So, <code>1.2.3-beta.4</code> would be allowed, but <code>1.2.4-beta.2</code> would not, because it is a prerelease of a different <code>[major, minor, patch]</code> tuple.</p>
<dt>&bull;</p>
<dd> <code>^0.0.3-beta</code> := <code>&gt;=0.0.3-beta &lt;0.0.4</code> Note that prereleases in the <code>0.0.3</code> version <i>only</i> will be allowed, if they are greater than or equal to <code>beta</code>. So, <code>0.0.3-pr.2</code> would be allowed. </p>
</dl>
</dl>
<p> When parsing caret ranges, a missing <code>patch</code> value desugars to the number <code>0</code>, but will allow flexibility within that value, even if the major and minor versions are both <code>0</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>^1.2.x</code> := <code>&gt;=1.2.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd> <code>^0.0.x</code> := <code>&gt;=0.0.0 &lt;0.1.0</code></p>
<dt>&bull;</p>
<dd> <code>^0.0</code> := <code>&gt;=0.0.0 &lt;0.1.0</code> </p>
</dl>
</dl>
<p> A missing <code>minor</code> and <code>patch</code> values will desugar to zero, but also allow flexibility within those values, even if the major version is zero.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>^1.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd> <code>^0.x</code> := <code>&gt;=0.0.0 &lt;1.0.0</code> </p>
</dl>
</dl>
<h3>Range Grammar</h3>
<p> Putting all this together, here is a Backus-Naur grammar for ranges, for the benefit of parser authors: </p>
<dl>
<dt>
<dd>
<pre><code>
range-set  ::= range ( logical-or range ) *
logical-or ::= ( ' ' ) * '||' ( ' ' ) *
range      ::= hyphen | simple ( ' ' simple ) * | ''
hyphen     ::= partial ' - ' partial
simple     ::= primitive | partial | tilde | caret
primitive  ::= ( '&lt;' | '&gt;' | '&gt;=' | '&lt;=' | '=' ) partial
partial    ::= xr ( '.' xr ( '.' xr qualifier ? )? )?
xr         ::= 'x' | 'X' | '*' | nr
nr         ::= '0' | ['1'-'9'] ( ['0'-'9'] ) *
tilde      ::= '~' partial
caret      ::= '^' partial
qualifier  ::= ( '-' pre )? ( '+' build )?
pre        ::= parts
build      ::= parts
parts      ::= part ( '.' part ) *
part       ::= nr | [-0-9A-Za-z]+
</code></pre>
</dl>
<h2>Functions</h2>
<p> All methods and classes take a final <code>options</code> object argument. All options in this object are <code>false</code> by default. The options supported are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>loose</code> Be more forgiving about not-quite-valid semver strings. (Any resulting output will always be 100% strict compliant, of course.) For backwards compatibility reasons, if the <code>options</code> argument is a boolean value instead of an object, it is interpreted to be the <code>loose</code> param.</p>
<dt>&bull;</p>
<dd> <code>includePrerelease</code> Set to suppress the default behavior <i><a rel="nofollow" href="https://github.com/npm/node-semver#prerelease-tags">https://github.com/npm/node-semver#prerelease-tags</a></i> of excluding prerelease tagged versions from ranges unless they are explicitly opted into. </p>
</dl>
</dl>
<p> Strict-mode Comparators and Ranges will be strict about the SemVer strings that they parse.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>valid(v)</code>: Return the parsed version, or null if it&#8217;s not valid.</p>
<dt>&bull;</p>
<dd> <code>inc(v, release)</code>: Return the version incremented by the release type (<code>major</code>, <code>premajor</code>, <code>minor</code>, <code>preminor</code>, <code>patch</code>, <code>prepatch</code>, or <code>prerelease</code>), or null if it&#8217;s not valid</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>premajor</code> in one call will bump the version up to the next major version and down to a prerelease of that major version. <code>preminor</code>, and <code>prepatch</code> work the same way.</p>
<dt>&bull;</p>
<dd> If called from a non-prerelease version, the <code>prerelease</code> will work the same as <code>prepatch</code>. It increments the patch version, then makes a prerelease. If the input version is already a prerelease it simply increments it. </p>
</dl>
</dl>
<dt>&bull;</p>
<dd> <code>prerelease(v)</code>: Returns an array of prerelease components, or null if none exist. Example: <code>prerelease(&#8216;1.2.3-alpha.1&#8217;) -&gt; [&#8216;alpha&#8217;, 1]</code></p>
<dt>&bull;</p>
<dd> <code>major(v)</code>: Return the major version number.</p>
<dt>&bull;</p>
<dd> <code>minor(v)</code>: Return the minor version number.</p>
<dt>&bull;</p>
<dd> <code>patch(v)</code>: Return the patch version number.</p>
<dt>&bull;</p>
<dd> <code>intersects(r1, r2, loose)</code>: Return true if the two supplied ranges or comparators intersect.</p>
<dt>&bull;</p>
<dd> <code>parse(v)</code>: Attempt to parse a string as a semantic version, returning either a <code>SemVer</code> object or <code>null</code>. </p>
</dl>
</dl>
<h3>Comparison</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>gt(v1, v2)</code>: <code>v1 &gt; v2</code></p>
<dt>&bull;</p>
<dd> <code>gte(v1, v2)</code>: <code>v1 &gt;= v2</code></p>
<dt>&bull;</p>
<dd> <code>lt(v1, v2)</code>: <code>v1 &lt; v2</code></p>
<dt>&bull;</p>
<dd> <code>lte(v1, v2)</code>: <code>v1 &lt;= v2</code></p>
<dt>&bull;</p>
<dd> <code>eq(v1, v2)</code>: <code>v1 == v2</code> This is true if they&#8217;re logically equivalent, even if they&#8217;re not the exact same string. You already know how to compare strings.</p>
<dt>&bull;</p>
<dd> <code>neq(v1, v2)</code>: <code>v1 != v2</code> The opposite of <code>eq</code>.</p>
<dt>&bull;</p>
<dd> <code>cmp(v1, comparator, v2)</code>: Pass in a comparison string, and it&#8217;ll call the corresponding function above. <code>&quot;===&quot;</code> and <code>&quot;!==&quot;</code> do simple string comparison, but are included for completeness. Throws if an invalid comparison string is provided.</p>
<dt>&bull;</p>
<dd> <code>compare(v1, v2)</code>: Return <code>0</code> if <code>v1 == v2</code>, or <code>1</code> if <code>v1</code> is greater, or <code>-1</code> if <code>v2</code> is greater. Sorts in ascending order if passed to <code>Array.sort()</code>.</p>
<dt>&bull;</p>
<dd> <code>rcompare(v1, v2)</code>: The reverse of compare. Sorts an array of versions in descending order when passed to <code>Array.sort()</code>.</p>
<dt>&bull;</p>
<dd> <code>compareBuild(v1, v2)</code>: The same as <code>compare</code> but considers <code>build</code> when two versions are equal. Sorts in ascending order if passed to <code>Array.sort()</code>. <code>v2</code> is greater. Sorts in ascending order if passed to <code>Array.sort()</code>.</p>
<dt>&bull;</p>
<dd> <code>diff(v1, v2)</code>: Returns difference between two versions by the release type (<code>major</code>, <code>premajor</code>, <code>minor</code>, <code>preminor</code>, <code>patch</code>, <code>prepatch</code>, or <code>prerelease</code>), or null if the versions are the same. </p>
</dl>
</dl>
<h3>Comparators</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>intersects(comparator)</code>: Return true if the comparators intersect </p>
</dl>
</dl>
<h3>Ranges</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>validRange(range)</code>: Return the valid range or null if it&#8217;s not valid</p>
<dt>&bull;</p>
<dd> <code>satisfies(version, range)</code>: Return true if the version satisfies the range.</p>
<dt>&bull;</p>
<dd> <code>maxSatisfying(versions, range)</code>: Return the highest version in the list that satisfies the range, or <code>null</code> if none of them do.</p>
<dt>&bull;</p>
<dd> <code>minSatisfying(versions, range)</code>: Return the lowest version in the list that satisfies the range, or <code>null</code> if none of them do.</p>
<dt>&bull;</p>
<dd> <code>minVersion(range)</code>: Return the lowest version that can possibly match the given range.</p>
<dt>&bull;</p>
<dd> <code>gtr(version, range)</code>: Return <code>true</code> if version is greater than all the versions possible in the range.</p>
<dt>&bull;</p>
<dd> <code>ltr(version, range)</code>: Return <code>true</code> if version is less than all the versions possible in the range.</p>
<dt>&bull;</p>
<dd> <code>outside(version, range, hilo)</code>: Return true if the version is outside the bounds of the range in either the high or low direction. The <code>hilo</code> argument must be either the string <code>&#8216;&gt;&#8217;</code> or <code>&#8216;&lt;&#8216;</code>. (This is the function called by <code>gtr</code> and <code>ltr</code>.)</p>
<dt>&bull;</p>
<dd> <code>intersects(range)</code>: Return true if any of the ranges comparators intersect </p>
</dl>
</dl>
<p> Note that, since ranges may be non-contiguous, a version might not be greater than a range, less than a range, <i>or</i> satisfy a range! For example, the range <code>1.2 &lt;1.2.9 || &gt;2.0.0</code> would have a hole from <code>1.2.9</code> until <code>2.0.0</code>, so the version <code>1.2.10</code> would not be greater than the range (because <code>2.0.1</code> satisfies, which is higher), nor less than the range (since <code>1.2.8</code> satisfies, which is lower), and it also does not satisfy the range. </p>
<p> If you want to know if a version satisfies or does not satisfy a range, use the <code>satisfies(version, range)</code> function.</p>
<h3>Coercion</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>coerce(version, options)</code>: Coerces a string to semver if possible </p>
</dl>
</dl>
<p> This aims to provide a very forgiving translation of a non-semver string to semver. It looks for the first digit in a string, and consumes all remaining characters which satisfy at least a partial semver (e.g., <code>1</code>, <code>1.2</code>, <code>1.2.3</code>) up to the max permitted length (256 characters). Longer versions are simply truncated (<code>4.6.3.9.2-alpha2</code> becomes <code>4.6.3</code>). All surrounding text is simply ignored (<code>v3.4 replaces v3.3.1</code> becomes <code>3.4.0</code>). Only text which lacks digits will fail coercion (<code>version one</code> is not valid). The maximum length for any semver component considered for coercion is 16 characters; longer components will be ignored (<code>10000000000000000.4.7.4</code> becomes <code>4.7.4</code>). The maximum value for any semver component is <code>Number.MAX_SAFE_INTEGER || (2**53 &#8211; 1)</code>; higher value components are invalid (<code>9999999999999999.4.7.4</code> is likely invalid). </p>
<p> If the <code>options.rtl</code> flag is set, then <code>coerce</code> will return the right-most coercible tuple that does not share an ending index with a longer coercible tuple. For example, <code>1.2.3.4</code> will return <code>2.3.4</code> in rtl mode, not <code>4.0.0</code>. <code>1.2.3/4</code> will return <code>4.0.0</code>, because the <code>4</code> is not a part of any other overlapping SemVer tuple.</p>
<h3>Clean</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>clean(version)</code>: Clean a string to be a valid semver if possible </p>
</dl>
</dl>
<p> This will return a cleaned and trimmed semver version. If the provided version is not valid a null will be returned. This does not work for ranges. </p>
<p> ex.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; = v 2.1.5foo&#8217;)</code>: <code>null</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; = v 2.1.5foo&#8217;, { loose: true })</code>: <code>&#8216;2.1.5-foo&#8217;</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; = v 2.1.5-foo&#8217;)</code>: <code>null</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; = v 2.1.5-foo&#8217;, { loose: true })</code>: <code>&#8216;2.1.5-foo&#8217;</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216;=v2.1.5&#8217;)</code>: <code>&#8216;2.1.5&#8217;</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; =v2.1.5&#8217;)</code>: <code>2.1.5</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216; 2.1.5 &#8216;)</code>: <code>&#8216;2.1.5&#8217;</code></p>
<dt>&bull;</p>
<dd> <code>s.clean(&#8216;~1.0.0&#8217;)</code>: <code>null</code> </p>
</dl>
</dl>
<h2>Exported Modules</h2>
<p> &lt;!&#8211; TODO: Make sure that all of these items are documented (classes aren&#8217;t, eg), and then pull the module name into the documentation for that specific thing. &#8211;&gt; </p>
<p> You may pull in just the part of this semver utility that you need, if you are sensitive to packing and tree-shaking concerns. The main <code>require(&#8216;semver&#8217;)</code> export uses getter functions to lazily load the parts of the API that are used. </p>
<p> The following modules are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/classes&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/classes/comparator&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/classes/range&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/classes/semver&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/clean&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/cmp&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/coerce&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/compare&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/compare-build&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/compare-loose&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/diff&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/eq&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/gt&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/gte&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/inc&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/lt&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/lte&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/major&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/minor&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/neq&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/parse&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/patch&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/prerelease&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/rcompare&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/rsort&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/satisfies&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/sort&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/functions/valid&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/gtr&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/intersects&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/ltr&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/max-satisfying&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/min-satisfying&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/min-version&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/outside&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/to-comparators&#8217;)</code></p>
<dt>&bull;</p>
<dd> <code>require(&#8216;semver/ranges/valid&#8217;)</code> </p>
</dl>
</dl>
<h2>Index</h2>
<dt><a href="#lbAO">Functions</a></p>
<dd>
<dt><a href="#lbAU">Exported Modules</a></p>
<dd></dl>
