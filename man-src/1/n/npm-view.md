---
title: "npm-view(1)"
name: "npm-view"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-view/"
description: "npm-view – View registry info"
---

<h2 class="name">NAME</h2>
<p> <code>npm-view</code> &#8211; View registry info </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm view[&lt;@scope&gt; / ]&lt;name&gt;[@&lt;version&gt;][&lt;field&gt;[.&lt;subfield&gt;]...] aliases : info, show, v
</code></pre>
</dl>
<h3>Description</h3>
<p> This command shows data about a package and prints it to the stream referenced by the <code>outfd</code> config, which defaults to stdout. </p>
<p> To show the package registry entry for the <code>connect</code> package, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view connect
</pre>
</dl>
<p> The default version is &quot;latest&quot; if unspecified. </p>
<p> Field names can be specified after the package descriptor. For example, to show the dependencies of the <code>ronn</code> package at version 0.3.5, you could do the following: </p>
<dl>
<dt>
<dd>
<pre>
npm view ronn [at] 0.3.5 dependencies
</pre>
</dl>
<p> You can view child fields by separating them with a period. To view the git repository URL for the latest version of npm, you could do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view npm repository.url
</pre>
</dl>
<p> This makes it easy to view information about a dependency with a bit of shell scripting. For example, to view all the data about the version of opts that ronn depends on, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view opts@$(npm view ronn dependencies.opts)
</pre>
</dl>
<p> For fields that are arrays, requesting a non-numeric field will return all of the values from the objects in the list. For example, to get all the contributor names for the &quot;express&quot; project, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view express contributors.email
</pre>
</dl>
<p> You may also use numeric indices in square braces to specifically select an item in an array field. To just get the email address of the first contributor in the list, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view express contributors[0].email
</pre>
</dl>
<p> Multiple fields may be specified, and will be printed one after another. For example, to get all the contributor names and email addresses, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view express contributors.name contributors.email
</pre>
</dl>
<p> &quot;Person&quot; fields are shown as a string if they would be shown as an object. So, for example, this will show the list of npm contributors in the shortened string format. (See npm help <code>package.json</code> for more on this.) </p>
<dl>
<dt>
<dd>
<pre>
npm view npm contributors
</pre>
</dl>
<p> If a version range is provided, then data will be printed for every matching version of the package. This will show which version of jsdom was required by each matching version of yui3: </p>
<dl>
<dt>
<dd>
<pre>
npm view yui3@'&gt;0.5.4' dependencies.jsdom
</pre>
</dl>
<p> To show the <code>connect</code> package version history, you can do this: </p>
<dl>
<dt>
<dd>
<pre>
npm view connect versions
</pre>
</dl>
<h3>Output</h3>
<p> If only a single string field for a single version is output, then it will not be colorized or quoted, so as to enable piping the output to another command. If the field is an object, it will be output as a JavaScript object literal. </p>
<p> If the &#8211;json flag is given, the outputted fields will be JSON. </p>
<p> If the version range matches multiple versions, than each printed value will be prefixed with the version it applies to. </p>
<p> If multiple fields are requested, than each of them are prefixed with the field name.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help search</p>
<dt>&bull;</p>
<dd> npm help registry</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help docs </p>
</dl>
</dl>
<h2>Index</h2>
