---
title: "dpkgbuildflags(3)"
name: "dpkgbuildflags"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgbuildflags/"
---

Dpkg::BuildFlags - query build flags 

<h2>Description</h2>The Dpkg::BuildFlags object is used by dpkg-buildflags and can be used to query the same information.
<h2>Functions</h2><dl COMPACT><dt>my $bf = Dpkg::BuildFlags-&gt;<i>new()</i>
</dt><dd>Create a new Dpkg::BuildFlags object. It will be initialized based on the value of several configuration files and environment variables.
</dd><dt>$bf-&gt;<i>load_vendor_defaults()</i>
</dt><dd>Reset the flags stored to the default set provided by the vendor.
</dd><dt>$bf-&gt;<i>load_system_config()</i>
</dt><dd>Update flags from the system configuration.
</dd><dt>$bf-&gt;<i>load_user_config()</i>
</dt><dd>Update flags from the user configuration.
</dd><dt>$bf-&gt;<i>load_environment_config()</i>
</dt><dd>Update flags based on user directives stored in the environment. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for details.
</dd><dt>$bf-&gt;<i>load_maintainer_config()</i>
</dt><dd>Update flags based on maintainer directives stored in the environment. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for details.
</dd><dt>$bf-&gt;<i>load_config()</i>
</dt><dd>Call successively <i>load_system_config()</i>, <i>load_user_config()</i>, <i>load_environment_config()</i> and <i>load_maintainer_config()</i> to update the default build flags defined by the vendor.
</dd><dt>$bf-&gt;set($flag, $value, $source, $maint)
</dt><dd>Update the build flag <tt>$flag</tt> with value <tt>$value</tt> and record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
</dd><dt>$bf-&gt;set_feature($area, $feature, $enabled)
</dt><dd>Update the boolean state of whether a specific feature within a known feature area has been enabled. The only currently known feature area is ``hardening''.
</dd><dt>$bf-&gt;strip($flag, $value, $source, $maint)
</dt><dd>Update the build flag <tt>$flag</tt> by stripping the flags listed in <tt>$value</tt> and record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
</dd><dt>$bf-&gt;append($flag, $value, $source, $maint)
</dt><dd>Append the options listed in <tt>$value</tt> to the current value of the flag <tt>$flag</tt>. Record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
</dd><dt>$bf-&gt;prepend($flag, $value, $source, $maint)
</dt><dd>Prepend the options listed in <tt>$value</tt> to the current value of the flag <tt>$flag</tt>. Record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
</dd><dt>$bf-&gt;update_from_conffile($file, $source)
</dt><dd>Update the current build flags based on the configuration directives contained in <tt>$file</tt>. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for the format of the directives. 
 <tt>$source</tt> is the origin recorded for any build flag set or modified.
</dd><dt>$bf-&gt;get($flag)
</dt><dd>Return the value associated to the flag. It might be undef if the flag doesn't exist.
</dd><dt>$bf-&gt;<i>get_feature_areas()</i>
</dt><dd>Return the feature areas (i.e. the area values has_features will return true for).
</dd><dt>$bf-&gt;get_features($area)
</dt><dd>Return, for the given area, a hash with keys as feature names, and values as booleans indicating whether the feature is enabled or not.
</dd><dt>$bf-&gt;get_origin($flag)
</dt><dd>Return the origin associated to the flag. It might be undef if the flag doesn't exist.
</dd><dt>$bf-&gt;is_maintainer_modified($flag)
</dt><dd>Return true if the flag is modified by the maintainer.
</dd><dt>$bf-&gt;has_features($area)
</dt><dd>Returns true if the given area of features is known, and false otherwise. The only currently recognized area is ``hardening''.
</dd><dt>$bf-&gt;has($option)
</dt><dd>Returns a boolean indicating whether the flags exists in the object.
</dd><dt>my @flags = $bf-&gt;<i>list()</i>
</dt><dd>Returns the list of flags stored in the object.</dd></dl><h2>Changes</h2><h3>Version 1.03</h3>New method: <tt>$bf</tt>-&gt;<i>get_feature_areas()</i> to list possible values for <tt>$bf</tt>-&gt;get_features. 

 New method <tt>$bf</tt>-&gt;<i>is_maintainer_modified()</i> and new optional parameter to <tt>$bf</tt>-&gt;<i>set()</i>, <tt>$bf</tt>-&gt;<i>append()</i>, <tt>$bf</tt>-&gt;<i>prepend()</i>, <tt>$bf</tt>-&gt;<i>strip()</i>.
<h3>Version 1.02</h3>New methods: <tt>$bf</tt>-&gt;<i>get_features()</i>, <tt>$bf</tt>-&gt;<i>has_features()</i>, <tt>$bf</tt>-&gt;<i>set_feature()</i>.
<h3>Version 1.01</h3>New method: <tt>$bf</tt>-&gt;<i>prepend()</i> very similar to <i>append()</i>. Implement support of the prepend operation everywhere. 

 New method: <tt>$bf</tt>-&gt;<i>load_maintainer_config()</i> that update the build flags based on the package maintainer directives.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;
