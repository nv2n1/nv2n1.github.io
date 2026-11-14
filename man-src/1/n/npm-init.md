---
title: "npm-init(1)"
name: "npm-init"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-init/"
description: "npm-init – create a package.json file"
---

<h2 class="name">NAME</h2>
<p> <code>npm-init</code> &#8211; create a package.json file </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm init[--force | -f | --yes | -y | --scope] npm init&lt;@scope&gt;(same as `npx&lt;@scope&gt; / create`)
    npm init[&lt;@scope&gt; / ]&lt;name&gt;(same as `npx[&lt;@scope&gt; / ] create - &lt;name&gt;`)
</code></pre>
</dl>
<h3>Examples</h3>
<p> Create a new React-based project using <code>create-react-app</code> <i><a rel="nofollow" href="https://npm.im/create-react-app">https://npm.im/create-react-app</a></i>: </p>
<dl>
<dt>
<dd>
<pre>
$ npm init react-app ./my-react-app
</pre>
</dl>
<p> Create a new <code>esm</code>-compatible package using <code>create-esm</code> <i><a rel="nofollow" href="https://npm.im/create-esm">https://npm.im/create-esm</a></i>: </p>
<dl>
<dt>
<dd>
<pre>
$ mkdir my-esm-lib &amp;&amp; cd my-esm-lib
$ npm init esm --yes
</pre>
</dl>
<p> Generate a plain old package.json using legacy init: </p>
<dl>
<dt>
<dd>
<pre>
$ mkdir my-npm-pkg &amp;&amp; cd my-npm-pkg
$ git init
$ npm init
</pre>
</dl>
<p> Generate it without having it ask any questions: </p>
<dl>
<dt>
<dd>
<pre>
$ npm init -y
</pre>
</dl>
<h3>Description</h3>
<p> <code>npm init &lt;initializer&gt;</code> can be used to set up a new or existing npm package. </p>
<p> <code>initializer</code> in this case is an npm package named <code>create-&lt;initializer&gt;</code>, which will be installed by <code>npx</code> <i><a rel="nofollow" href="https://npm.im/npx">https://npm.im/npx</a></i>, and then have its main bin executed &#8212; presumably creating or updating <code>package.json</code> and running any other initialization-related operations. </p>
<p> The init command is transformed to a corresponding <code>npx</code> operation as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm init foo</code> -&gt; <code>npx create-foo</code></p>
<dt>&bull;</p>
<dd> <code>npm init @usr/foo</code> -&gt; <code>npx @usr/create-foo</code></p>
<dt>&bull;</p>
<dd> <code>npm init @usr</code> -&gt; <code>npx @usr/create</code> </p>
</dl>
</dl>
<p> Any additional options will be passed directly to the command, so <code>npm init foo &#8211;hello</code> will map to <code>npx create-foo &#8211;hello</code>. </p>
<p> If the initializer is omitted (by just calling <code>npm init</code>), init will fall back to legacy init behavior. It will ask you a bunch of questions, and then write a package.json for you. It will attempt to make reasonable guesses based on existing fields, dependencies, and options selected. It is strictly additive, so it will keep any fields and values that were already set. You can also use <code>-y</code>/<code>&#8211;yes</code> to skip the questionnaire altogether. If you pass <code>&#8211;scope</code>, it will create a scoped package.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://github.com/isaacs/init-package-json">https://github.com/isaacs/init-package-json</a></p>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> npm help version</p>
<dt>&bull;</p>
<dd> npm help scope </p>
</dl>
</dl>
<h2>Index</h2>
