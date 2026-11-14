---
title: "npm-config(1)"
name: "npm-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-config/"
description: "npm-config – Manage the npm configuration files"
---

<h2 class="name">NAME</h2>
<p> <code>npm-config</code> &#8211; Manage the npm configuration files </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm config set&lt;key&gt;&lt;value&gt;[-g | --global] npm config get&lt;key&gt;
    npm config delete&lt;key&gt;
        npm config list[-l][--json] npm config edit
            npm get&lt;key&gt;
                npm set&lt;key&gt;&lt;value&gt;[-g | --global] aliases : c
</code></pre>
</dl>
<h3>Description</h3>
<p> npm gets its config settings from the command line, environment variables, <code>npmrc</code> files, and in some cases, the <code>package.json</code> file. </p>
<p> See npm help npmrc for more information about the npmrc files. </p>
<p> See npm help config for a more thorough discussion of the mechanisms involved. </p>
<p> The <code>npm config</code> command can be used to update and edit the contents of the user and global npmrc files.</p>
<h3>Sub-commands</h3>
<p> Config supports the following sub-commands:</p>
<h3>set</h3>
<dl>
<dt>
<dd>
<pre>
npm config set key value
</pre>
</dl>
<p> Sets the config key to the value. </p>
<p> If value is omitted, then it sets it to &quot;true&quot;.</p>
<h3>get</h3>
<dl>
<dt>
<dd>
<pre>
npm config get key
</pre>
</dl>
<p> Echo the config value to stdout.</p>
<h3>list</h3>
<dl>
<dt>
<dd>
<pre>
npm config list
</pre>
</dl>
<p> Show all the config settings. Use <code>-l</code> to also show defaults. Use <code>&#8211;json</code> to show the settings in json format.</p>
<h3>delete</h3>
<dl>
<dt>
<dd>
<pre>
npm config delete key
</pre>
</dl>
<p> Deletes the key from all configuration files.</p>
<h3>edit</h3>
<dl>
<dt>
<dd>
<pre>
npm config edit
</pre>
</dl>
<p> Opens the config file in an editor. Use the <code>&#8211;global</code> flag to edit the global config.</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help folders</p>
<dt>&bull;</p>
<dd> npm help config</p>
<dt>&bull;</p>
<dd> npm help package.json</p>
<dt>&bull;</p>
<dd> npm help npmrc</p>
<dt>&bull;</p>
<dd> npm help npm </p>
</dl>
</dl>
<h2>Index</h2>
