---
title: "dpkgsubstvars(3)"
name: "dpkgsubstvars"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgsubstvars/"
---

Dpkg::Substvars - handle variable substitution in strings 

<h2>Description</h2>It provides some an object which is able to substitute variables in strings.
<h2>Methods</h2><dl COMPACT><dt>my $s = Dpkg::Substvars-&gt;new($file)
</dt><dd>Create a new object that can do substitutions. By default it contains generic substitutions like ${Newline}, ${Space}, ${Tab}, ${dpkg:Version} and ${dpkg:Upstream-Version}. 
 Additional substitutions will be read from the <tt>$file</tt> passed as parameter. 
 It keeps track of which substitutions were actually used (only counting <i>substvars()</i>, not <i>get()</i>), and warns about unused substvars when asked to. The substitutions that are always present are not included in these warnings.
</dd><dt>$s-&gt;set($key, $value)
</dt><dd>Add/replace a substitution.
</dd><dt>$s-&gt;set_as_used($key, $value)
</dt><dd>Add/replace a substitution and mark it as used (no warnings will be produced even if unused).
</dd><dt>$s-&gt;set_as_auto($key, $value)
</dt><dd>Add/replace a substitution and mark it as used and automatic (no warnings will be produced even if unused).
</dd><dt>$s-&gt;get($key)
</dt><dd>Get the value of a given substitution.
</dd><dt>$s-&gt;delete($key)
</dt><dd>Remove a given substitution.
</dd><dt>$s-&gt;mark_as_used($key)
</dt><dd>Prevents warnings about a unused substitution, for example if it is provided by default.
</dd><dt>$s-&gt;no_warn($key)
</dt><dd>Obsolete function, use <i>mark_as_used()</i> instead.
</dd><dt>$s-&gt;load($file)
</dt><dd>Add new substitutions read from <tt>$file</tt>.
</dd><dt>$s-&gt;parse($fh, $desc)
</dt><dd>Add new substitutions read from the filehandle. <tt>$desc</tt> is used to identify the filehandle in error messages.
</dd><dt>$s-&gt;set_version_substvars($sourceversion, $binaryversion)
</dt><dd>Defines ${binary:Version}, ${source:Version} and ${source:Upstream-Version} based on the given version strings. 
 These will never be warned about when unused.
</dd><dt>$s-&gt;<i>set_arch_substvars()</i>
</dt><dd>Defines architecture variables: ${Arch}. 
 This will never be warned about when unused.
</dd><dt>$newstring = $s-&gt;substvars($string)
</dt><dd>Substitutes variables in <tt>$string</tt> and return the result in <tt>$newstring</tt>.
</dd><dt>$s-&gt;<i>warn_about_unused()</i>
</dt><dd>Issues warning about any variables that were set, but not used.
</dd><dt>$s-&gt;set_msg_prefix($prefix)
</dt><dd>Define a prefix displayed before all warnings/error messages output by the module.
</dd><dt>$s-&gt;save($file)
</dt><dd>Store all substitutions variables except the automatic ones in the indicated file.
</dd><dt>&quot;$s&quot;
</dt><dd>Return a string representation of all substitutions variables except the automatic ones.
</dd><dt>$str = $s-&gt;output($fh)
</dt><dd>Print all substitutions variables except the automatic ones in the filehandle and return the content written.</dd></dl><h2>Changes</h2><h3>Version 1.03</h3>New method: <tt>$s</tt>-&gt;<i>set_as_auto()</i>.
<h3>Version 1.02</h3>New argument: Accept a <tt>$binaryversion</tt> in <tt>$s</tt>-&gt;<i>set_version_substvars()</i>, passing a single argument is still supported. 

 New method: <tt>$s</tt>-&gt;<i>mark_as_used()</i>. 

 Deprecated method: <tt>$s</tt>-&gt;<i>no_warn()</i>, use <tt>$s</tt>-&gt;<i>mark_as_used()</i> instead.
<h3>Version 1.01</h3>New method: <tt>$s</tt>-&gt;<i>set_as_used()</i>.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
