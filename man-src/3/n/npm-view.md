---
title: "npm-view(3)"
name: "npm-view"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-view/"
description: "npm-view — View registry info"
---

<p><code>npm-view</code> &#8212; View registry info</p>
<h2>Synopsis</h2>
<pre>npm.commands.view(args, [silent,] callback)</pre>
<h2>Description</h2>
<p>This command shows data about a package and prints it to the stream referenced by the <code>outfd</code> config, which defaults to stdout. </p>
<p> The &quot;args&quot; parameter is an ordered list that closely resembles the command-line usage. The elements should be ordered such that the first element is the package and version (package [at] version). The version is optional. After that, the rest of the parameters are fields with optional subfields (&quot;field.subfield&quot;) which can be used to get only the information desired from the registry. </p>
<p> The callback will be passed all of the data returned by the query. </p>
<p> For example, to get the package registry entry for the <code>connect</code> package, you can do this:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;connect&quot;], callback)</pre>
<dd></dl>
<p> If no version is specified, &quot;latest&quot; is assumed. </p>
<p> Field names can be specified after the package descriptor. For example, to show the dependencies of the <code>ronn</code> package at version 0.3.5, you could do the following:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;ronn [at] 0.3.5&quot;, &quot;dependencies&quot;], callback)</pre>
<dd></dl>
<p> You can view child field by separating them with a period. To view the git repository URL for the latest version of npm, you could do this:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;npm&quot;, &quot;repository.url&quot;], callback)</pre>
<dd></dl>
<p> For fields that are arrays, requesting a non-numeric field will return all of the values from the objects in the list. For example, to get all the contributor names for the &quot;express&quot; project, you can do this:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;express&quot;, &quot;contributors.email&quot;], callback)</pre>
<dd></dl>
<p> You may also use numeric indices in square braces to specifically select an item in an array field. To just get the email address of the first contributor in the list, you can do this:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;express&quot;, &quot;contributors[0].email&quot;], callback)</pre>
<dd></dl>
<p> Multiple fields may be specified, and will be printed one after another. For exampls, to get all the contributor names and email addresses, you can do this:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;express&quot;, &quot;contributors.name&quot;, &quot;contributors.email&quot;], callback)</pre>
<dd></dl>
<p> &quot;Person&quot; fields are shown as a string if they would be shown as an object. So, for example, this will show the list of npm contributors in the shortened string format. (See <code>npm help json</code> for more on this.)</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;npm&quot;, &quot;contributors&quot;], callback)</pre>
<dd></dl>
<p> If a version range is provided, then data will be printed for every matching version of the package. This will show which version of jsdom was required by each matching version of yui3:</p>
<dl>
<dd>
<pre>npm.commands.view([&quot;yui3@'&gt;0.5.4'&quot;, &quot;dependencies.jsdom&quot;], callback)</pre>
<dd></dl>
<h2>Output</h2>
<p>If only a single string field for a single version is output, then it will not be colorized or quoted, so as to enable piping the output to another command. </p>
<p> If the version range matches multiple versions, than each printed value will be prefixed with the version it applies to. </p>
<p> If multiple fields are requested, than each of them are prefixed with the field name. </p>
<p> Console output can be disabled by setting the &#8216;silent&#8217; parameter to true.</p>
<h2>Return Value</h2>
<p>The data returned will be an object in this formation:</p>
<dl>
<dd>
<pre>{ &lt;version&gt;:
 { &lt;field&gt;: &lt;value&gt;
 , ... }
, ... }</pre>
<dd></dl>
<p> corresponding to the list of fields selected. </p>
