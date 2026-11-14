---
title: "npm-update(1)"
name: "npm-update"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-update/"
description: "npm-update – Update a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-update</code> &#8211; Update a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm update[-g][&lt;pkg&gt;...] aliases : up, upgrade
</code></pre>
</dl>
<h3>Description</h3>
<p> This command will update all the packages listed to the latest version (specified by the <code>tag</code> config), respecting semver. </p>
<p> It will also install missing packages. As with all commands that install packages, the <code>&#8211;dev</code> flag will cause <code>devDependencies</code> to be processed as well. </p>
<p> If the <code>-g</code> flag is specified, this command will update globally installed packages. </p>
<p> If no package name is specified, all packages in the specified location (global or local) will be updated. </p>
<p> As of <code>npm [at] 2.6.1</code>, the <code>npm update</code> will only inspect top-level packages. Prior versions of <code>npm</code> would also recursively inspect all dependencies. To get the old behavior, use <code>npm &#8211;depth 9999 update</code>. </p>
<p> As of <code>npm [at] 5.0.0</code>, the <code>npm update</code> will change <code>package.json</code> to save the new version as the minimum required dependency. To get the old behavior, use <code>npm update &#8211;no-save</code>.</p>
<h3>Example</h3>
<p> IMPORTANT VERSION NOTE: these examples assume <code>npm [at] 2.6.1</code> or later. For older versions of <code>npm</code>, you must specify <code>&#8211;depth 0</code> to get the behavior described below. </p>
<p> For the examples below, assume that the current package is <code>app</code> and it depends on dependencies, <code>dep1</code> (<code>dep2</code>, .. etc.). The published versions of <code>dep1</code> are: </p>
<dl>
<dt>
<dd>
<pre><code>
{
    "dist-tags" : {"latest" : "1.2.2"},
                  "versions" : [
                      "1.2.2",
                      "1.2.1",
                      "1.2.0",
                      "1.1.2",
                      "1.1.1",
                      "1.0.0",
                      "0.4.1",
                      "0.4.0",
                      "0.2.0"
                  ]
}
</code></pre>
</dl>
<h3>Caret Dependencies</h3>
<p> If <code>app</code>&#8216;s <code>package.json</code> contains: </p>
<dl>
<dt>
<dd>
<pre>
&quot;dependencies&quot;: {
  &quot;dep1&quot;: &quot;^1.1.1&quot;
}
</pre>
</dl>
<p> Then <code>npm update</code> will install <code>dep1 [at] 1.2.2</code>, because <code>1.2.2</code> is <code>latest</code> and <code>1.2.2</code> satisfies <code>^1.1.1</code>.</p>
<h3>Tilde Dependencies</h3>
<p> However, if <code>app</code>&#8216;s <code>package.json</code> contains: </p>
<dl>
<dt>
<dd>
<pre>
&quot;dependencies&quot;: {
  &quot;dep1&quot;: &quot;~1.1.1&quot;
}
</pre>
</dl>
<p> In this case, running <code>npm update</code> will install <code>dep1 [at] 1.1.2</code>. Even though the <code>latest</code> tag points to <code>1.2.2</code>, this version does not satisfy <code>~1.1.1</code>, which is equivalent to <code>&gt;=1.1.1 &lt;1.2.0</code>. So the highest-sorting version that satisfies <code>~1.1.1</code> is used, which is <code>1.1.2</code>.</p>
<h3>Caret Dependencies below 1.0.0</h3>
<p> Suppose <code>app</code> has a caret dependency on a version below <code>1.0.0</code>, for example: </p>
<dl>
<dt>
<dd>
<pre>
&quot;dependencies&quot;: {
  &quot;dep1&quot;: &quot;^0.2.0&quot;
}
</pre>
</dl>
<p> <code>npm update</code> will install <code>dep1 [at] 0.2.0</code>, because there are no other versions which satisfy <code>^0.2.0</code>. </p>
<p> If the dependence were on <code>^0.4.0</code>: </p>
<dl>
<dt>
<dd>
<pre>
&quot;dependencies&quot;: {
  &quot;dep1&quot;: &quot;^0.4.0&quot;
}
</pre>
</dl>
<p> Then <code>npm update</code> will install <code>dep1 [at] 0.4.1</code>, because that is the highest-sorting version that satisfies <code>^0.4.0</code> (<code>&gt;= 0.4.0 &lt;0.5.0</code>)</p>
<h3>Updating Globally-Installed Packages</h3>
<p> <code>npm update -g</code> will apply the <code>update</code> action to each globally installed package that is <code>outdated</code> &#8212; that is, has a version that is different from <code>wanted</code>. </p>
<p> Note: Globally installed packages are treated as if they are installed with a caret semver range specified. So if you require to update to <code>latest</code> you may need to run <code>npm install -g [&lt;pkg&gt;&#8230;]</code> </p>
<p> NOTE: If a package has been upgraded to a version newer than <code>latest</code>, it will be <i>downgraded</i>.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help install</p>
<dt>&bull;</p>
<dd> npm help outdated</p>
<dt>&bull;</p>
<dd> npm help shrinkwrap</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help ls </p>
</dl>
</dl>
<h2>Index</h2>
