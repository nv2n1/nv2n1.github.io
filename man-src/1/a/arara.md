---

title: "arara(1)"
name: "arara"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arara/"
description: "arara – a TeX automation tool based on rules and directives."
---

<p> <code>arara</code> [<i>options</i>] <i>documents</i>&#8230;</p>
<p> <code>arara</code> is a TeX automation tool based on rules and directives. It gives you a way to enhance your TeX experience. The tool is an effort to provide a concise way to automate the daily TeX workflow for users and also package writers. Users might write their own rules when the provided ones do not suffice. </p>
<p> arara takes a list of documents as input. They will be processed according to their directives. Options apply to the execution of all documents.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;log</code></dt>
<dd> Generate a log output.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Print or suppress command output.</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> Go through all the motions of running a command but with no actual calls.</dd>
<dt><code>&#8211;safe-run</code></dt>
<dd> Run in safe mode and disable potentially harmful features.</dd>
<dt><code>&#8211;header</code></dt>
<dd> Extract directives only in the file header.</dd>
<dt><code>&#8211;preamble</code></dt>
<dd> Set the file preamble as named based on the configuration file.</dd>
<dt><code>&#8211;timeout</code></dt>
<dd> Sets an execution timeout for spawned processes.</dd>
<dt><code>&#8211;language</code></dt>
<dd> Set the localization to the language specified by code.</dd>
<dt><code>&#8211;max-loops</code></dt>
<dd> Set the number &gt; 0 of loops for looping directives.</dd>
<dt><code>&#8211;working-directory</code></dt>
<dd> Set the working directory for the whole execution.</dd>
<dt><code>&#8211;call-property</code></dt>
<dd> Pass a property as key=value parameter into the application to be used within the session.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show a help message and exit.</dd></dl>
<h2>BUGS</h2>
<p> Issue tracker at </p>
