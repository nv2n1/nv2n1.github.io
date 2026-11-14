---
title: "dnf-plugin-repoquery(8)"
name: "dnf-plugin-repoquery"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-repoquery/"
description: "dnf.plugin.repoquery – DNF repoquery Plugin"
---

<p>dnf.plugin.repoquery &#8211; DNF repoquery Plugin </p>
<p> Query package information from Yum repositories.</p>
<h2>Synopsis</h2>
<p><code>dnf repoquery [&lt;select-options&gt;] [&lt;query-options&gt;] [&lt;pkg-spec&gt;]</code> <code>dnf repoquery &#8211;querytags</code></p>
<h2>Description</h2>
<p><i>repoquery</i> searches the available Yum repositories for selected packages and displays the requested information about them. It is an equivalent of <code>rpm -q</code> for remote repositories.</p>
<h3>Select Options</h3>
<p>Together with <code>&lt;pkg-spec&gt;</code>, control what packages are displayed in the output. If <code>&lt;pkg-spec&gt;</code> is given, the set of resulting packages matching the specification. All packages are considered if no <code>&lt;pkg-spec&gt;</code> is specified.</p>
<dl>
<dt><code>&lt;pkg-spec&gt;</code></p>
<dd>Package specification like: name[-[epoch:]version[-release]][.arch]. See <a rel="nofollow" href="http://dnf.readthedocs.org/en/latest/command_ref.html#specifying-packages">http://dnf.readthedocs.org/en/latest/command_ref.html#specifying-packages</a></p>
<dt><code>&#8211;arch &lt;arch&gt;</code></p>
<dd>Limit the resulting set only to packages of arch <code>&lt;arch&gt;</code>.</p>
<dt><code>-f &lt;file&gt;</code>, <code>&#8211;file &lt;file&gt;</code></p>
<dd>Limit the resulting set only to package that owns <code>&lt;file&gt;</code>.</p>
<dt><code>&#8211;repoid &lt;id&gt;</code></p>
<dd>Limit the resulting set only to packages from repo identified by <code>&lt;id&gt;</code>.</p>
<dt><code>&#8211;whatprovides &lt;capability&gt;</code></p>
<dd>Limit the resulting set only to packages that provide <code>&lt;capability&gt;</code>.</p>
<dt><code>&#8211;whatrequires &lt;capability&gt;</code></p>
<dd>Limit the resulting set only to packages that require <code>&lt;capability&gt;</code>.</dl>
<h3>Query Options</h3>
<p>Set what information is displayed about each package. </p>
<p> The following are mutually exclusive, i.e. at most one can be specified. If no query option is given, matching packages are displayed in the standard NEVRA notation.</p>
<dl>
<dt><code>&#8211;conflicts</code></p>
<dd>Display capabilities that the package conflicts with. Same as <code>&#8211;qf &quot;%{conflicts}</code>.</p>
<dt><code>-i, &#8211;info</code></p>
<dd>Show detailed information about the package.</p>
<dt><code>-l, &#8211;list</code></p>
<dd>Show list of files in the package.</p>
<dt><code>-s, &#8211;source</code></p>
<dd>Show package source RPM name.</p>
<dt><code>&#8211;obsoletes</code></p>
<dd>Display capabilities that the package obsoletes. Same as <code>&#8211;qf &quot;%{obsoletes}</code>.</p>
<dt><code>&#8211;provides</code></p>
<dd>Display capabilities provided by the package. Same as <code>&#8211;qf &quot;%{provides}</code>.</p>
<dt><code>&#8211;qf &lt;format&gt;</code>, <code>&#8211;queryformat &lt;format&gt;</code></p>
<dd>Custom display format. <code>&lt;format&gt;</code> is a string to output for each matched package. Every occurrence of <code>%{&lt;tag&gt;}</code> within is replaced by corresponding attribute of the package. List of recognized tags can be displayed by running <code>dnf repoquery &#8211;querytags</code>.</p>
<dt><code>&#8211;requires</code></p>
<dd>Display capabilities that the package depends on. Same as <code>&#8211;qf &quot;%{requires}</code>.</dl>
<h2>Examples</h2>
<p>Display NEVRAS of all available packages matching <code>light*</code>: </p>
<pre>dnf repoquery 'light*'</pre>
<p>Display requires of all ligttpd packages: </p>
<pre>dnf repoquery --requires lighttpd</pre>
<p>Display source rpm of ligttpd package: </p>
<pre>dnf repoquery --source lighttpd</pre>
<p>Display package name that owns the given file: </p>
<pre>dnf repoquery --file /etc/lighttpd/lighttpd.conf</pre>
<p>Display name, architecture and the containing repository of all lighttpd packages: </p>
<pre>dnf repoquery --queryformat '%{name}.%{arch} : %{reponame}' lighttpd</pre>
<p>Display all available packages providing &quot;webserver&quot;: </p>
<pre>dnf repoquery --whatprovides webserver</pre>
<p>Display all available packages providing &quot;webserver&quot; but only for &quot;i686&quot; architecture: </p>
<pre>dnf repoquery --whatprovides webserver --arch i686</pre>
<h2>Author</h2>
<p>See AUTHORS in your Core DNF Plugins distribution</p>
<h2>Copyright</h2>
<p>2014, Red Hat, Licensed under GPLv2+</p>
