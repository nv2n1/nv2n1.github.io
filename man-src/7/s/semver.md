---
title: "semver(7)"
name: "semver"
section: "7"
letter: "s"
url: "/docs/linux/man/7-semver/"
description: "semver – The semantic versioner for npm"
---

<p><code>semver</code> &#8211; The semantic versioner for npm</p>
<h2>Usage</h2>
<pre>$ npm install semver
semver.valid('1.2.3') // '1.2.3'
semver.valid('a.b.c') // null
semver.clean(' =v1.2.3 ') // '1.2.3'
semver.satisfies('1.2.3', '1.x || &gt;=2.5.0 || 5.0.0 - 7.2.3') // true
semver.gt('1.2.3', '9.8.7') // false
semver.lt('1.2.3', '9.8.7') // true</pre>
<p>As a command-line utility:</p>
<dl>
<dd>
<pre>$ semver -h
Usage: semver &lt;version&gt; [&lt;version&gt; [...]] [-r &lt;range&gt; | -i &lt;inc&gt; | --preid &lt;identifier&gt; | -l | -rv]
Test if version(s) satisfy the supplied range(s), and sort them.
Multiple versions or ranges may be supplied, unless increment
option is specified. In that case, only a single version may
be used, and it is incremented by the specified level
Program exits successfully if any valid version satisfies
all supplied ranges, and prints all satisfying versions.
If no versions are valid, or ranges are not satisfied,
then exits failure.
Versions are printed in ascending order, so supplying
multiple versions to the utility will just sort them.</pre>
<dd></dl>
<h2>Versions</h2>
<p>A &quot;version&quot; is described by the <code>v2.0.0</code> specification found at <i><a rel="nofollow" href="http://semver.org/">http://semver.org/</a></i>. </p>
<p> A leading <code>&quot;=&quot;</code> or <code>&quot;v&quot;</code> character is stripped off and ignored.</p>
<h2>Ranges</h2>
<p>A <code>version range</code> is a set of <code>comparators</code> which specify versions that satisfy the range. </p>
<p> A <code>comparator</code> is composed of an <code>operator</code> and a <code>version</code>. The set of primitive <code>operators</code> is:</p>
<dl>
<dt>&bull;</p>
<dd><code>&lt;</code> Less than</p>
<dt>&bull;</p>
<dd><code>&lt;=</code> Less than or equal to</p>
<dt>&bull;</p>
<dd><code>&gt;</code> Greater than</p>
<dt>&bull;</p>
<dd><code>&gt;=</code> Greater than or equal to</p>
<dt>&bull;</p>
<dd><code>=</code> Equal. If no operator is specified, then equality is assumed, so this operator is optional, but MAY be included.</p>
<dd></dl>
<p> For example, the comparator <code>&gt;=1.2.7</code> would match the versions <code>1.2.7</code>, <code>1.2.8</code>, <code>2.5.3</code>, and <code>1.3.9</code>, but not the versions <code>1.2.6</code> or <code>1.1.0</code>. </p>
<p> Comparators can be joined by whitespace to form a <code>comparator set</code>, which is satisfied by the <code>intersection</code> of all of the comparators it includes. </p>
<p> A range is composed of one or more comparator sets, joined by <code>||</code>. A version matches a range if and only if every comparator in at least one of the <code>||</code>-separated comparator sets is satisfied by the version. </p>
<p> For example, the range <code>&gt;=1.2.7 &lt;1.3.0</code> would match the versions <code>1.2.7</code>, <code>1.2.8</code>, and <code>1.2.99</code>, but not the versions <code>1.2.6</code>, <code>1.3.0</code>, or <code>1.1.0</code>. </p>
<p> The range <code>1.2.7 || &gt;=1.2.9 &lt;2.0.0</code> would match the versions <code>1.2.7</code>, <code>1.2.9</code>, and <code>1.4.6</code>, but not the versions <code>1.2.8</code> or <code>2.0.0</code>.</p>
<h3>Prerelease Tags</h3>
<p>If a version has a prerelease tag (for example, <code>1.2.3-alpha.3</code>) then it will only be allowed to satisfy comparator sets if at least one comparator with the same <code>[major, minor, patch]</code> tuple also has a prerelease tag. </p>
<p> For example, the range <code>&gt;1.2.3-alpha.3</code> would be allowed to match the version <code>1.2.3-alpha.7</code>, but it would <i>not</i> be satisfied by <code>3.4.5-alpha.9</code>, even though <code>3.4.5-alpha.9</code> is technically &quot;greater than&quot; <code>1.2.3-alpha.3</code> according to the SemVer sort rules. The version range only accepts prerelease tags on the <code>1.2.3</code> version. The version <code>3.4.5</code> <i>would</i> satisfy the range, because it does not have a prerelease flag, and <code>3.4.5</code> is greater than <code>1.2.3-alpha.7</code>. </p>
<p> The purpose for this behavior is twofold. First, prerelease versions frequently are updated very quickly, and contain many breaking changes that are (by the author&#8217;s design) not yet fit for public consumption. Therefore, by default, they are excluded from range matching semantics. </p>
<p> Second, a user who has opted into using a prerelease version has clearly indicated the intent to use <i>that specific</i> set of alpha/beta/rc versions. By including a prerelease tag in the range, the user is indicating that they are aware of the risk. However, it is still not appropriate to assume that they have opted into taking a similar risk on the <i>next</i> set of prerelease versions. </p>
<p> The method <code>.inc</code> takes an additional <code>identifier</code> string argument that will append the value of the string as a prerelease identifier:</p>
<dl>
<dd>
<pre>&gt; semver.inc('1.2.3', 'pre', 'beta')
'1.2.4-beta.0'</pre>
<dd></dl>
<p> command-line example:</p>
<dl>
<dd>
<pre>$ semver 1.2.3 -i prerelease --preid beta
1.2.4-beta.0</pre>
<dd></dl>
<p> Which then can be used to increment further:</p>
<dl>
<dd>
<pre>$ semver 1.2.4-beta.0 -i prerelease
1.2.4-beta.1</pre>
<dd></dl>
<h3>Advanced Range Syntax</h3>
<p>Advanced range syntax desugars to primitive comparators in deterministic ways. </p>
<p> Advanced ranges may be combined in the same way as primitive comparators using white space or <code>||</code>. </p>
<p> Specifies an inclusive set.</p>
<dl>
<dt>&bull;</p>
<dd><code>1.2.3 &#8211; 2.3.4</code> := <code>&gt;=1.2.3 &lt;=2.3.4</code></p>
<dd></dl>
<p> If a partial version is provided as the first version in the inclusive range, then the missing pieces are replaced with zeroes.</p>
<dl>
<dt>&bull;</p>
<dd><code>1.2 &#8211; 2.3.4</code> := <code>&gt;=1.2.0 &lt;=2.3.4</code></p>
<dd></dl>
<p> If a partial version is provided as the second version in the inclusive range, then all versions that start with the supplied parts of the tuple are accepted, but nothing that would be greater than the provided tuple parts.</p>
<dl>
<dt>&bull;</p>
<dd><code>1.2.3 &#8211; 2.3</code> := <code>&gt;=1.2.3 &lt;2.4.0</code></p>
<dt>&bull;</p>
<dd><code>1.2.3 &#8211; 2</code> := <code>&gt;=1.2.3 &lt;3.0.0</code></p>
<dd></dl>
<p> Any of <code>X</code>, <code>x</code>, or <code>*</code> may be used to &quot;stand in&quot; for one of the numeric values in the <code>[major, minor, patch]</code> tuple.</p>
<dl>
<dt>&bull;</p>
<dd><code>*</code> := <code>&gt;=0.0.0</code> (Any version satisfies)</p>
<dt>&bull;</p>
<dd><code>1.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code> (Matching major version)</p>
<dt>&bull;</p>
<dd><code>1.2.x</code> := <code>&gt;=1.2.0 &lt;1.3.0</code> (Matching major and minor versions)</p>
<dd></dl>
<p> A partial version range is treated as an X-Range, so the special character is in fact optional.</p>
<dl>
<dt>&bull;</p>
<dd><code>&quot;&quot;</code> (empty string) := <code>*</code> := <code>&gt;=0.0.0</code></p>
<dt>&bull;</p>
<dd><code>1</code> := <code>1.x.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd><code>1.2</code> := <code>1.2.x</code> := <code>&gt;=1.2.0 &lt;1.3.0</code></p>
<dd></dl>
<p> Allows patch-level changes if a minor version is specified on the comparator. Allows minor-level changes if not.</p>
<dl>
<dt>&bull;</p>
<dd><code>~1.2.3</code> := <code>&gt;=1.2.3 &lt;1.(2+1).0</code> := <code>&gt;=1.2.3 &lt;1.3.0</code></p>
<dt>&bull;</p>
<dd><code>~1.2</code> := <code>&gt;=1.2.0 &lt;1.(2+1).0</code> := <code>&gt;=1.2.0 &lt;1.3.0</code> (Same as <code>1.2.x</code>)</p>
<dt>&bull;</p>
<dd><code>~1</code> := <code>&gt;=1.0.0 &lt;(1+1).0.0</code> := <code>&gt;=1.0.0 &lt;2.0.0</code> (Same as <code>1.x</code>)</p>
<dt>&bull;</p>
<dd><code>~0.2.3</code> := <code>&gt;=0.2.3 &lt;0.(2+1).0</code> := <code>&gt;=0.2.3 &lt;0.3.0</code></p>
<dt>&bull;</p>
<dd><code>~0.2</code> := <code>&gt;=0.2.0 &lt;0.(2+1).0</code> := <code>&gt;=0.2.0 &lt;0.3.0</code> (Same as <code>0.2.x</code>)</p>
<dt>&bull;</p>
<dd><code>~0</code> := <code>&gt;=0.0.0 &lt;(0+1).0.0</code> := <code>&gt;=0.0.0 &lt;1.0.0</code> (Same as <code>0.x</code>)</p>
<dt>&bull;</p>
<dd><code>~1.2.3-beta.2</code> := <code>&gt;=1.2.3-beta.2 &lt;1.3.0</code> Note that prereleases in the <code>1.2.3</code> version will be allowed, if they are greater than or equal to <code>beta.2</code>. So, <code>1.2.3-beta.4</code> would be allowed, but <code>1.2.4-beta.2</code> would not, because it is a prerelease of a different <code>[major, minor, patch]</code> tuple.</p>
<dd></dl>
<p> Allows changes that do not modify the left-most non-zero digit in the <code>[major, minor, patch]</code> tuple. In other words, this allows patch and minor updates for versions <code>1.0.0</code> and above, patch updates for versions <code>0.X &gt;=0.1.0</code>, and <i>no</i> updates for versions <code>0.0.X</code>. </p>
<p> Many authors treat a <code>0.x</code> version as if the <code>x</code> were the major &quot;breaking-change&quot; indicator. </p>
<p> Caret ranges are ideal when an author may make breaking changes between <code>0.2.4</code> and <code>0.3.0</code> releases, which is a common practice. However, it presumes that there will <i>not</i> be breaking changes between <code>0.2.4</code> and <code>0.2.5</code>. It allows for changes that are presumed to be additive (but non-breaking), according to commonly observed practices.</p>
<dl>
<dt>&bull;</p>
<dd><code>^1.2.3</code> := <code>&gt;=1.2.3 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd><code>^0.2.3</code> := <code>&gt;=0.2.3 &lt;0.3.0</code></p>
<dt>&bull;</p>
<dd><code>^0.0.3</code> := <code>&gt;=0.0.3 &lt;0.0.4</code></p>
<dt>&bull;</p>
<dd><code>^1.2.3-beta.2</code> := <code>&gt;=1.2.3-beta.2 &lt;2.0.0</code> Note that prereleases in the <code>1.2.3</code> version will be allowed, if they are greater than or equal to <code>beta.2</code>. So, <code>1.2.3-beta.4</code> would be allowed, but <code>1.2.4-beta.2</code> would not, because it is a prerelease of a different <code>[major, minor, patch]</code> tuple.</p>
<dt>&bull;</p>
<dd><code>^0.0.3-beta</code> := <code>&gt;=0.0.3-beta &lt;0.0.4</code> Note that prereleases in the <code>0.0.3</code> version <i>only</i> will be allowed, if they are greater than or equal to <code>beta</code>. So, <code>0.0.3-pr.2</code> would be allowed.</p>
<dd></dl>
<p> When parsing caret ranges, a missing <code>patch</code> value desugars to the number <code>0</code>, but will allow flexibility within that value, even if the major and minor versions are both <code>0</code>.</p>
<dl>
<dt>&bull;</p>
<dd><code>^1.2.x</code> := <code>&gt;=1.2.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd><code>^0.0.x</code> := <code>&gt;=0.0.0 &lt;0.1.0</code></p>
<dt>&bull;</p>
<dd><code>^0.0</code> := <code>&gt;=0.0.0 &lt;0.1.0</code></p>
<dd></dl>
<p> A missing <code>minor</code> and <code>patch</code> values will desugar to zero, but also allow flexibility within those values, even if the major version is zero.</p>
<dl>
<dt>&bull;</p>
<dd><code>^1.x</code> := <code>&gt;=1.0.0 &lt;2.0.0</code></p>
<dt>&bull;</p>
<dd><code>^0.x</code> := <code>&gt;=0.0.0 &lt;1.0.0</code></p>
<dd></dl>
<h2>Functions</h2>
<p>All methods and classes take a final <code>loose</code> boolean argument that, if true, will be more forgiving about not-quite-valid semver strings. The resulting output will always be 100% strict, of course. </p>
<p> Strict-mode Comparators and Ranges will be strict about the SemVer strings that they parse.</p>
<dl>
<dt>&bull;</p>
<dd><code>valid(v)</code>: Return the parsed version, or null if it&#8217;s not valid.</p>
<dt>&bull;</p>
<dd>
<dt>&bull;</p>
<dd><code>premajor</code> in one call will bump the version up to the next major version and down to a prerelease of that major version. <code>preminor</code>, and <code>prepatch</code> work the same way.</p>
<dt>&bull;</p>
<dd>If called from a non-prerelease version, the <code>prerelease</code> will work the same as <code>prepatch</code>. It increments the patch version, then makes a prerelease. If the input version is already a prerelease it simply increments it.</p>
<dd>
<dt>&bull;</p>
<dd><code>major(v)</code>: Return the major version number.</p>
<dt>&bull;</p>
<dd><code>minor(v)</code>: Return the minor version number.</p>
<dt>&bull;</p>
<dd><code>patch(v)</code>: Return the patch version number.</p>
<dd></dl>
<h3>Comparison</h3>
<dl>
<dt>&bull;</p>
<dd><code>gt(v1, v2)</code>: <code>v1 &gt; v2</code></p>
<dt>&bull;</p>
<dd><code>gte(v1, v2)</code>: <code>v1 &gt;= v2</code></p>
<dt>&bull;</p>
<dd><code>lt(v1, v2)</code>: <code>v1 &lt; v2</code></p>
<dt>&bull;</p>
<dd><code>lte(v1, v2)</code>: <code>v1 &lt;= v2</code></p>
<dt>&bull;</p>
<dd><code>eq(v1, v2)</code>: <code>v1 == v2</code> This is true if they&#8217;re logically equivalent, even if they&#8217;re not the exact same string. You already know how to compare strings.</p>
<dt>&bull;</p>
<dd><code>neq(v1, v2)</code>: <code>v1 != v2</code> The opposite of <code>eq</code>.</p>
<dt>&bull;</p>
<dd><code>cmp(v1, comparator, v2)</code>: Pass in a comparison string, and it&#8217;ll call the corresponding function above. <code>&quot;===&quot;</code> and <code>&quot;!==&quot;</code> do simple string comparison, but are included for completeness. Throws if an invalid comparison string is provided.</p>
<dt>&bull;</p>
<dd><code>compare(v1, v2)</code>: Return <code>0</code> if <code>v1 == v2</code>, or <code>1</code> if <code>v1</code> is greater, or <code>-1</code> if <code>v2</code> is greater. Sorts in ascending order if passed to <code>Array.sort()</code>.</p>
<dt>&bull;</p>
<dd><code>rcompare(v1, v2)</code>: The reverse of compare. Sorts an array of versions in descending order when passed to <code>Array.sort()</code>.</p>
<dt>&bull;</p>
<dd><code>diff(v1, v2)</code>: Returns difference between two versions by the release type (<code>major</code>, <code>premajor</code>, <code>minor</code>, <code>preminor</code>, <code>patch</code>, <code>prepatch</code>, or <code>prerelease</code>), or null if the versions are the same.</p>
<dd></dl>
<h3>Ranges</h3>
<dl>
<dt>&bull;</p>
<dd><code>validRange(range)</code>: Return the valid range or null if it&#8217;s not valid</p>
<dt>&bull;</p>
<dd><code>satisfies(version, range)</code>: Return true if the version satisfies the range.</p>
<dt>&bull;</p>
<dd><code>maxSatisfying(versions, range)</code>: Return the highest version in the list that satisfies the range, or <code>null</code> if none of them do.</p>
<dt>&bull;</p>
<dd><code>gtr(version, range)</code>: Return <code>true</code> if version is greater than all the versions possible in the range.</p>
<dt>&bull;</p>
<dd><code>ltr(version, range)</code>: Return <code>true</code> if version is less than all the versions possible in the range.</p>
<dt>&bull;</p>
<dd><code>outside(version, range, hilo)</code>: Return true if the version is outside the bounds of the range in either the high or low direction. The <code>hilo</code> argument must be either the string <code>&#8216;&gt;&#8217;</code> or <code>&#8216;&lt;&#8216;</code>. (This is the function called by <code>gtr</code> and <code>ltr</code>.)</p>
<dd></dl>
<p> Note that, since ranges may be non-contiguous, a version might not be greater than a range, less than a range, <i>or</i> satisfy a range! For example, the range <code>1.2 &lt;1.2.9 || &gt;2.0.0</code> would have a hole from <code>1.2.9</code> until <code>2.0.0</code>, so the version <code>1.2.10</code> would not be greater than the range (because <code>2.0.1</code> satisfies, which is higher), nor less than the range (since <code>1.2.8</code> satisfies, which is lower), and it also does not satisfy the range. </p>
<p> If you want to know if a version satisfies or does not satisfy a range, use the <code>satisfies(version, range)</code> function.</p>
