---
title: "dpkgbuildoptions(3)"
name: "dpkgbuildoptions"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgbuildoptions/"
---

Dpkg::BuildOptions - parse and update build options 

<h2>Description</h2>The Dpkg::BuildOptions object can be used to manipulate options stored in environment variables like <font SIZE="-1">DEB_BUILD_OPTIONS</font> and <font SIZE="-1">DEB_BUILD_MAINT_OPTIONS.</font>
<h2>Functions</h2><dl COMPACT><dt>my $bo = Dpkg::BuildOptions-&gt;new(%opts)
<dd>Create a new Dpkg::BuildOptions object. It will be initialized based on the value of the environment variable named <tt>$opts</tt>{envvar} (or <font SIZE="-1">DEB_BUILD_OPTIONS</font> if that option is not set).
<dt>$bo-&gt;<i>reset()</i>
<dd>Reset the object to not have any option (it's empty).
<dt>$bo-&gt;merge($content, $source)
<dd>Merge the options set in <tt>$content</tt> and record that they come from the source <tt>$source</tt>. <tt>$source</tt> is mainly used in warning messages currently to indicate where invalid options have been detected. 

 <tt>$content</tt> is a space separated list of options with optional assigned values like ``nocheck parallel=2''.
<dt>$bo-&gt;set($option, $value, [$source])
<dd>Store the given option in the objet with the given value. It's legitimate for a value to be undefined if the option is a simple boolean (its presence means true, its absence means false). The <tt>$source</tt> is optional and indicates where the option comes from. 

 The known options have their values checked for sanity. Options without values have their value removed and options with invalid values are discarded.
<dt>$bo-&gt;get($option)
<dd>Return the value associated to the option. It might be undef even if the option exists. You might want to check with <tt>$bo</tt>-&gt;has($option) to verify if the option is stored in the object.
<dt>$bo-&gt;has($option)
<dd>Returns a boolean indicating whether the option is stored in the object.
<dt>$string = $bo-&gt;output($fh)
<dd>Return a string representation of the build options suitable to be assigned to an environment variable. Can optionnaly output that string to the given filehandle.
<dt>$bo-&gt;export([$var])
<dd>Export the build options to the given environment variable. If omitted, the environment variable defined at creation time is assumed. The value set to the variable is also returned.</dl><h2>Changes</h2><h3>Version 1.01</h3>Enable to use another environment variable instead of <font SIZE="-1">DEB_BUILD_OPTIONS.</font> Thus add support for the ``envvar'' option at creation time.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;
