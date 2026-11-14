---
title: "deb-substvars(5)"
name: "deb-substvars"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-substvars/"
description: "deb-substvars – Debian source substitution variables"
---

<p>deb-substvars &#8211; Debian source substitution variables</p>
<h2>Synopsis</h2>
<p><code>debian/substvars</code>, <code>debian/</code><i>binary-package</i><code>.substvars</code></p>
<h2>Description</h2>
<p>Before <code>dpkg-source</code>, <code>dpkg-gencontrol</code> and <code>dpkg-genchanges</code> write their control information (to the source control file <code>.dsc</code> for <code>dpkg-source</code> and to standard output for <code>dpkg-gencontrol</code> and <code>dpkg-genchanges</code>) they perform some variable substitutions on the output file. </p>
<p> A variable substitution has the form <code>${</code><i>variable-name</i><code>}</code>. Variable names consist of alphanumerics (a-zA-Z0-9), hyphens (-) and colons (:) and start with an alphanumeric, and are case-sensitive, even though they might refer to other entities which are case-preserving. Variable substitutions are performed repeatedly until none are left; the full text of the field after the substitution is rescanned to look for more substitutions. </p>
<p> After all the substitutions have been done each occurrence of the string <code>${}</code> (which is not a legal substitution) is replaced with a <code>$</code> sign. This can be used as an escape sequence such as <code>${}{</code><i></i><font SIZE="-1"><i>VARIABLE</i></font><i></i><code>}</code> which will end up as <code>${</code><i></i><font SIZE="-1"><i>VARIABLE</i></font><i></i><code>}</code> on the output. </p>
<p> While variable substitution is done on all control fields, some of those fields are used and needed during the build when the substitution did not yet occur. That&#8217;s why you can&#8217;t use variables in the <code>Package</code>, <code>Source</code> and <code>Architecture</code> fields. </p>
<p> Variable substitution happens on the content of the fields after they have been parsed, thus if you want a variable to expand over multiple lines you do not have to include a space after the newline. This is done implicitly when the field is output. For example, if the variable <code>${Description}</code> is set to &#8220;foo is bar.${Newline}foo is great.&#8221; and if you have the following field: </p>
<pre> Description: foo application
 ${Description}
 .
 More text.</pre>
<p>It will result in: </p>
<pre> Description: foo application
 foo is bar.
 foo is great.
 .
 More text.</pre>
<p>Variables can be set using the <code>-V</code> common option. They can be also specified in the file <code>debian/substvars</code> (or whatever other file is specified using the <code>-T</code> option). This file consists of lines of the form <i>name</i><code>=</code><i>value</i>. Trailing whitespace on each line, blank lines, and lines starting with a <code>#</code> symbol (comments) are ignored. </p>
<p> Additionally, the following standard variables are available:</p>
<dl>
<dt><code>Arch</code></p>
<dd>The current host architecture (i.e. the architecture the package is being built for, the equivalent of <font SIZE="-1"><code>DEB_HOST_ARCH</code></font>).</p>
<dt><code>vendor:Name</code></p>
<dd>The current vendor name (since dpkg 1.20.0). This value comes from the <code>Vendor</code> field for the current vendor&#8217;s origin file, as <code><a href="/docs/linux/man/1-dpkg-vendor/">dpkg-vendor</a></code>(1) would retrieve it.</p>
<dt><code>vendor:Id</code></p>
<dd>The current vendor <font SIZE="-1">ID</font> (since dpkg 1.20.0). This is just the lowercase variant of <code>vendor:Name</code>.</p>
<dt><code>source:Version</code></p>
<dd>The source package version (since dpkg 1.13.19).</p>
<dt><code>source:Upstream-Version</code></p>
<dd>The upstream source package version, including the Debian version epoch if any (since dpkg 1.13.19).</p>
<dt><code>binary:Version</code></p>
<dd>The binary package version (which may differ from <code>source:Version</code> in a binNMU for example; since dpkg 1.13.19).</p>
<dt><code>Source-Version</code></p>
<dd>The source package version (from the changelog file). This variable is now <code>obsolete</code> and emits an error when used as its meaning is different from its function, please use the <code>source:Version</code> or <code>binary:Version</code> as appropriate.</p>
<dt><code>source:Synopsis</code></p>
<dd>The source package synopsis, extracted from the source stanza <code>Description</code> field, if it exists (since dpkg 1.19.0).</p>
<dt><code>source:Extended-Description</code></p>
<dd>The source package extended description, extracted from the source stanza <code>Description</code> field, if it exists (since dpkg 1.19.0).</p>
<dt><code>Installed-Size</code></p>
<dd>The approximate total size of the package&#8217;s installed files. This value is copied into the corresponding control file field; setting it will modify the value of that field. If this variable is not set <code>dpkg-gencontrol</code> will compute the default value by accumulating the size of each regular file and symlink rounded to 1 KiB used units, and a baseline of 1 KiB for any other filesystem object type. With hardlinks only being counted once as a regular file. </p>
<p> <code>Note:</code> Take into account that this can only ever be an approximation, as the actual size used on the installed system will depend greatly on the filesystem used and its parameters, which might end up using either more or less space than the specified in this field.</p>
<dt><code>Extra-Size</code></p>
<dd>Additional disk space used when the package is installed. If this variable is set its value is added to that of the <code>Installed-Size</code> variable (whether set explicitly or using the default value) before it is copied into the <code>Installed-Size</code> control file field.</p>
<dt><code>S:</code><i>fieldname</i></p>
<dd>The value of the source stanza field <i>fieldname</i> (which must be given in the canonical capitalisation; since dpkg 1.18.11). Setting these variables has no effect other than on places where they are expanded explicitly. These variables are only available when generating binary control files.</p>
<dt><code>F:</code><i>fieldname</i></p>
<dd>The value of the output field <i>fieldname</i> (which must be given in the canonical capitalisation). Setting these variables has no effect other than on places where they are expanded explicitly.</p>
<dt><code>Format</code></p>
<dd>The <code>.changes</code> file format version generated by this version of the source packaging scripts. If you set this variable the contents of the <code>Format</code> field in the <code>.changes</code> file will change too.</p>
<dt><code>Newline</code>, <code>Space</code>, <code>Tab</code></p>
<dd>These variables each hold the corresponding character.</p>
<dt><code>shlibs:</code><i>dependencyfield</i></p>
<dd>Variable settings with names of this form are generated by <code>dpkg-shlibdeps</code>.</p>
<dt><code>dpkg:Upstream-Version</code></p>
<dd>The upstream version of dpkg (since dpkg 1.13.19).</p>
<dt><code>dpkg:Version</code></p>
<dd>The full version of dpkg (since dpkg 1.13.19).</dl>
<p> If a variable is referred to but not defined it generates a warning and an empty value is assumed.</p>
<h2>Files</h2>
<dl>
<dt><code>debian/substvars</code></p>
<dd>List of substitution variables and values.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-vendor/">dpkg-vendor</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-genchanges/">dpkg-genchanges</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-source/">dpkg-source</a></code>(1). </p>
