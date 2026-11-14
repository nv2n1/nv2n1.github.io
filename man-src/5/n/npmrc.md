---
title: "npmrc(5)"
name: "npmrc"
section: "5"
letter: "n"
url: "/docs/linux/man/5-npmrc/"
description: "npmrc – The npm config files"
---

<p><code>npmrc</code> &#8211; The npm config files</p>
<h3>Description</h3>
<p>npm gets its config settings from the command line, environment variables, and <code>npmrc</code> files. The <code>npm config</code> command can be used to update and edit the contents of the user and global npmrc files. For a list of available configuration options, see npm help config.</p>
<h3>Files</h3>
<p>The four relevant files are:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>per-project config file (/path/to/my/project/.npmrc)</p>
<dt>&bull;</p>
<dd>per-user config file (~/.npmrc)</p>
<dt>&bull;</p>
<dd>global config file ($PREFIX/etc/npmrc)</p>
<dt>&bull;</p>
<dd>npm builtin config file (/path/to/npm/npmrc)  All npm config files are an ini-formatted list of <code>key = value</code> parameters. Environment variables can be replaced using <code>${VARIABLE_NAME}</code>. For example:</p>
<dl>
<dd>
<pre>prefix = ${HOME}/.npm-packages</pre>
</dl>
<p> Each of these files is loaded, and config options are resolved in priority order. For example, a setting in the userconfig file would override the setting in the globalconfig file. Array values are specified by adding &quot;[]&quot; after the key name. For example:</p>
<dl>
<dd>
<pre>key[] = &quot;first value&quot;
key[] = &quot;second value&quot;</pre>
</dl>
<h3>Comments</h3>
<p>Lines in <code>.npmrc</code> files are interpreted as comments when they begin with a <code>;</code> or <code>#</code> character. <code>.npmrc</code> files are parsed by npm/ini <i><a rel="nofollow" href="https://github.com/npm/ini">https://github.com/npm/ini</a></i>, which specifies this comment syntax. For example:</p>
<dl>
<dd>
<pre># last modified: 01 Jan 2016
; Set a new registry for a scoped package
@myscope:registry=<a rel="nofollow" href="https://mycustomregistry.example.org">https://mycustomregistry.example.org</a></pre>
</dl>
<h3>Per-project config file</h3>
<p>When working locally in a project, a <code>.npmrc</code> file in the root of the project (ie, a sibling of <code>node_modules</code> and <code>package.json</code>) will set config values specific to this project. Note that this only applies to the root of the project that you&#8217;re running npm in. It has no effect when your module is published. For example, you can&#8217;t publish a module that forces itself to install globally, or in a different location. Additionally, this file is not read in global mode, such as when running <code>npm install -g</code>.</p>
<h3>Per-user config file</h3>
<p><code>$HOME/.npmrc</code> (or the <code>userconfig</code> param, if set in the environment or on the command line)</p>
<h3>Global config file</h3>
<p><code>$PREFIX/etc/npmrc</code> (or the <code>globalconfig</code> param, if set above): This file is an ini-file formatted list of <code>key = value</code> parameters. Environment variables can be replaced as above.</p>
<h3>Built-in config file</h3>
<p><code>path/to/npm/itself/npmrc</code> This is an unchangeable &quot;builtin&quot; configuration file that npm keeps consistent across updates. Set fields in here using the <code>./configure</code> script that comes with npm. This is primarily for distribution maintainers to override default configs in a standard and consistent manner.</p>
<h3>See also</h3>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>npm help folders</p>
<dt>&bull;</p>
<dd>npm help config</p>
<dt>&bull;</p>
<dd>npm help config</p>
<dt>&bull;</p>
<dd>npm help package.json</p>
<dt>&bull;</p>
<dd>npm help npm </p>
