---
title: "prwd(1)"
name: "prwd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prwd/"
description: "prwd – universal shell prompt"
---

<h2>NAME</h2>
<p> <code>prwd</code> &#8211; universal shell prompt</p>
<h2>SYNOPSIS</h2>
<p> <code>prwd</code> [-<code>aVh </code></p>
<h2>DESCRIPTION</h2>
<p> ] <code>prwd</code> is a replacement for your shell&#8217;s PS1, it provides a simple templating language with commands to customize your prompt. <code>prwd</code> keeps your prompt consistent between shells, provides fast template commands to display contextual information such as hostname, path, current git/hg branch without an inordinate amount of slow shell scripting. </p>
<p> The command-line options are as follows:</p>
<dl>
<dt><code>-V</code></p>
<dd> Show current version.</p>
<dt><code>-h</code></p>
<dd> Show usage.</p>
<dt><code>-t </code><i>template</i></p>
<dd> Use the provided template instead of the one defined in the configuration file or the one defined in the environment variable PRWD. This is particularly useful for testing a new template. Use single quote (&#8216;) around your template to avoid your shell to expand the $ variable.</p>
<dt><code>-a</code></p>
<dd> Outputs all the aliases starting with &#8216;$&#8217; as shell variable exports. The output from this command is meant to be used with eval in your .profile file, see section ALIAS VARIABLES in the <a href="/docs/linux/man/5-prwdrc/">prwdrc</a>(5) manual for more detailed information.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>prwd</code> can read its template from a configuration file, a command-line parameters or the following environment variable:</p>
<dl>
<dt><code>PRWD</code></p>
<dd> The template used to render your prompt. This value will override the default internal template and can be overridden by the configuration file.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.prwdrc </code></p>
<dd> defines all the configuration, overrides PRWD and the internal defaults. See <a href="/docs/linux/man/5-prwdrc/">prwdrc</a>(5) for configuratiom syntax and parameters.</dl>
<h2>SETUP</h2>
<p> You&#8217;ll need to place this line in your ~/.profile (your mileage may vary): </p>
<blockquote>
<pre>
export PS1='`prwd`'
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-prwdrc/">prwdrc</a>(5), <a href="/docs/linux/man/1-pwd/">pwd</a>(1), <a href="/docs/linux/man/1-csh/">csh</a>(1), <a href="/docs/linux/man/1-ksh/">ksh</a>(1), <a href="/docs/linux/man/1-sh/">sh</a>(1), <a href="/docs/linux/man/3-getcwd/">getcwd</a>(3)</p>
<h2>AUTHORS</h2>
<p> prwd was written by Bertrand Janin &lt;b@janin.com&gt; and is distributed under an ISC license (BSD compatible, OSI compatible). </p>
<h2>Index</h2>
