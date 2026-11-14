---
title: "radiusd-conf(5)"
name: "radiusd-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-radiusd-conf/"
description: "radiusd.conf – configuration file for the FreeRADIUS server"
---

<p>radiusd.conf &#8211; configuration file for the FreeRADIUS server</p>
<h2>Description</h2>
<p>The <code>radiusd.conf</code> file resides in the radius database directory, by default <code>/etc/raddb</code>. It defines the global configuration for the FreeRADIUS RADIUS server.</p>
<h2>Contents</h2>
<p>There are a large number of configuration parameters for the server. Most are documented in the file itself as comments. This page documents only the format of the file. Please read the <code>radiusd.conf</code> file itself for more information. </p>
<p> The configuration file parser is independent of the server configuration. This means that you can put almost anything into the configuration file. So long as it is properly formatted, the server will start. </p>
<p> When the server parses the configuration file, it looks only for those configurations it understands. Extra configuration items are ignored. This &quot;feature&quot; can be (ab)used in certain interesting ways.</p>
<h2>File Format</h2>
<p>The file format is line-based, like many other Unix configuration files. Each entry in the file must be placed on a line by itself, although continuations are supported. </p>
<p> The file consists of configuration items (variable = value pairs), sections, and comments.</p>
<dl>
<dt>Variables</p>
<dd>Variables can be set via: </p>
<dl>
<dd>
<pre><br>
 name = value</pre>
</dl>
<p> Single and double-quoted strings are permitted: </p>
<dl>
<dd>
<pre><br>
 string1 = &quot;hello world&quot;
<br>
 string2 = 'hello mom'</pre>
</dl>
<dt>Sections</p>
<dd>A section begins with a section name, followed on the same line by an open bracket &#8216;<code>{</code>&#8216;. Section may contain other sections, comments, or variables. Sections may be nested to any depth, limited only by available memory. A section ends with a close bracket &#8216;<code>}</code>&#8216;, on a line by itself. </p>
<dl>
<dd>
<pre><br>
 section {
<br>
 ...
<br>
 }</pre>
</dl>
<p> Sections can sometimes have a second name following the first one. The situations where this is legal depend on the context. See the examples and comments in the <code>radiusd.conf</code> file for more information. </p>
<dl>
<dd>
<pre><br>
 section foo {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>Comments</p>
<dd>Any line beginning with a (<code>#</code>) is deemed to be a comment, and is ignored. Comments can appear after a variable or section definitions. </p>
<dl>
<dd>
<pre><br>
 # comment
<br>
 foo = bar # set variable 'foo' to value 'bar'
<br>
 section { # start of section
<br>
 ...
<br>
 } # end of section</pre>
</dl>
<dt>Continuations</p>
<dd>Long lines can be broken up via continuations, using &#8216;\&#8217; as the last character of the line. For example, the following entry: </p>
<dl>
<dd>
<pre><br>
 foo = &quot;blah \
<br>
 blah \
<br>
 blah&quot;</pre>
</dl>
<p> will set the value of the variable &quot;foo&quot; to &quot;blah blah blah&quot;. Any CR or LF is not turned into a space, but all other whitespace is preserved in the final value.</dl>
<h2>References</h2>
<p>The value of a variable can reference another variable. These references are evaluated when the configuration file is loaded, which means that there is no run-time cost associated with them. This feature is most useful for turning long, repeated pieces of text into short ones. </p>
<p> Variables are referenced by ${variable_name}, as in the following examples. </p>
<dl>
<dd>
<pre> foo = bar # set variable 'foo' to value 'bar'
<br>
 who = ${foo} # sets variable 'who' to value of variable 'foo'
<br>
 my = &quot;${foo} a&quot; # sets variable 'my' to &quot;bar a&quot;</pre>
</dl>
<p> If the variable exists in a section or subsection, it can be referenced as ${section.subsection.variable}. Forward references are not allowed. Relative references are allowed, by pre-pending the name with one or more period. </p>
<dl>
<dd>
<pre> blogs = ${.foo}</pre>
</dl>
<p> Will set variable <code>blogs</code> to the value of variable <code>foo</code>, from the current section. </p>
<dl>
<dd>
<pre> blogs = ${..foo}</pre>
</dl>
<p> Will set variable <code>blogs</code> to the value of variable <code>foo</code>, from the section which contains the current section. </p>
<dl>
<dd>
<pre> blogs = ${modules.detail.filename}</pre>
</dl>
<p> Will set variable <code>blogs</code> to the value of variable <code>filename</code>, of the <code>detail</code> module, which is in the <code>modules</code> section of the configuration file. </p>
<p> Properties of anonymous parent sections may also be referenced, currently <code>name</code> and <code>instance</code> are supported. </p>
<dl>
<dd>
<pre> modules {
 example foo {
 file = ${.:name}
 }
 }</pre>
</dl>
<p> Will set variable <code>file</code> to the name of the containing section (example). </p>
<dl>
<dd>
<pre> modules {
 example foo {
 file = ${.:instance}
 }
 }</pre>
</dl>
<p> Will set variable <code>file</code> to the instance name of the containing section (foo). </p>
<dl>
<dd>
<pre> modules {
 example foo {
 file = ${..:name}
 }
 }</pre>
</dl>
<p> Will set variable <code>file</code> to the name of the parent of the containing section (modules).</p>
<h2>Files</h2>
<p>/etc/raddb/radiusd.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8) <code><a href="/docs/linux/man/5-unlang/">unlang</a></code>(5)</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
