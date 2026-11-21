---

title: "npm-outdated(1)"
name: "npm-outdated"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-outdated/"
description: "npm-outdated – Check for outdated packages"
---

<p> <code>npm-outdated</code> &#8211; Check for outdated packages </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre><code>
npm outdated[[&lt;@scope&gt; / ]&lt;pkg&gt;...]
</code></pre>
</dd></dl>
<h3>Description</h3>
<p> This command will check the registry to see if any (or, specific) installed packages are currently outdated. </p>
<p> In the output:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>wanted</code> is the maximum version of the package that satisfies the semver range specified in <code>package.json</code>. If there&#8217;s no available semver range (i.e. you&#8217;re running <code>npm outdated &#8211;global</code>, or the package isn&#8217;t included in <code>package.json</code>), then <code>wanted</code> shows the currently-installed version.</dd>
<dt>&bull;</dt>
<dd> <code>latest</code> is the version of the package tagged as latest in the registry. Running <code>npm publish</code> with no special configuration will publish the package with a dist-tag of <code>latest</code>. This may or may not be the maximum version of the package, or the most-recently published version of the package, depending on how the package&#8217;s developer manages the latest dist-tag <i>npm-dist-tag</i>.</dd>
<dt>&bull;</dt>
<dd> <code>location</code> is where in the dependency tree the package is located. Note that <code>npm outdated</code> defaults to a depth of 0, so unless you override that, you&#8217;ll always be seeing only top-level dependencies that are outdated.</dd>
<dt>&bull;</dt>
<dd> <code>package type</code> (when using <code>&#8211;long</code> / <code>-l</code>) tells you whether this package is a <code>dependency</code> or a <code>devDependency</code>. Packages not included in <code>package.json</code> are always marked <code>dependencies</code>.</dd>
<dt>&bull;</dt>
<dd> <code>homepage</code> (when using <code>&#8211;long</code> / <code>-l</code>) is the <code>homepage</code> value contained in the package&#8217;s <code>package.json</code></dd>
<dt>&bull;</dt>
<dd> Red means there&#8217;s a newer version matching your semver requirements, so you should update now.</dd>
<dt>&bull;</dt>
<dd> Yellow indicates that there&#8217;s a newer version above your semver requirements (usually new major, or new 0.x minor) so proceed with caution. </dd>
</dl>
</dl>
<h3>An example</h3>
<dl>
<dt>
</dt><dd>
<pre>
$ npm outdated
Package      Current   Wanted   Latest  Location
glob          5.0.15   5.0.15    6.0.1  test-outdated-output
nothingness    0.0.3      git      git  test-outdated-output
npm            3.5.1    3.5.2    3.5.1  test-outdated-output
local-dev      0.0.3   linked   linked  test-outdated-output
once           1.3.2    1.3.3    1.3.3  test-outdated-output
</pre>
</dd></dl>
<p> With these <code>dependencies</code>: </p>
<dl>
<dt>
</dt><dd>
<pre>
{
  &quot;glob&quot;: &quot;^5.0.15&quot;,
  &quot;nothingness&quot;: &quot;github:othiym23/nothingness#master&quot;,
  &quot;npm&quot;: &quot;^3.5.1&quot;,
  &quot;once&quot;: &quot;^1.3.1&quot;
}
</pre>
</dd></dl>
<p> A few things to note:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <code>glob</code> requires <code>^5</code>, which prevents npm from installing <code>glob@6</code>, which is outside the semver range.</dd>
<dt>&bull;</dt>
<dd> Git dependencies will always be reinstalled, because of how they&#8217;re specified. The installed committish might satisfy the dependency specifier (if it&#8217;s something immutable, like a commit SHA), or it might not, so <code>npm outdated</code> and <code>npm update</code> have to fetch Git repos to check. This is why currently doing a reinstall of a Git dependency always forces a new clone and install.</dd>
<dt>&bull;</dt>
<dd> <code>npm [at] 3.5.2</code> is marked as &quot;wanted&quot;, but &quot;latest&quot; is <code>npm [at] 3.5.1</code> because npm uses dist-tags to manage its <code>latest</code> and <code>next</code> release channels. <code>npm update</code> will install the <i>newest</i> version, but <code>npm install npm</code> (with no semver range) will install whatever&#8217;s tagged as <code>latest</code>.</dd>
<dt>&bull;</dt>
<dd> <code>once</code> is just plain out of date. Reinstalling <code>node_modules</code> from scratch or running <code>npm update</code> will bring it up to spec. </dd>
</dl>
</dl>
<h3>Configuration</h3>
<h3>json</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Show information in JSON format.</p>
<h3>long</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Show extended information.</p>
<h3>parseable</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Show parseable output instead of tree view.</p>
<h3>global</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: false</dd>
<dt>&bull;</dt>
<dd> Type: Boolean </dd>
</dl>
</dl>
<p> Check packages in the global install prefix instead of in the current project.</p>
<h3>depth</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Default: 0</dd>
<dt>&bull;</dt>
<dd> Type: Int </dd>
</dl>
</dl>
<p> Max depth for checking dependency tree.</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help update</dd>
<dt>&bull;</dt>
<dd> npm help dist-tag</dd>
<dt>&bull;</dt>
<dd> npm help registry</dd>
<dt>&bull;</dt>
<dd> npm help folders </dd>
</dl>
</dl>
