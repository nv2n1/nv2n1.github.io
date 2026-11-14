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
<dd>Create a new Dpkg::BuildFlags object. It will be initialized based on the value of several configuration files and environment variables.
<dt>$bf-&gt;<i>load_vendor_defaults()</i>
<dd>Reset the flags stored to the default set provided by the vendor.
<dt>$bf-&gt;<i>load_system_config()</i>
<dd>Update flags from the system configuration.
<dt>$bf-&gt;<i>load_user_config()</i>
<dd>Update flags from the user configuration.
<dt>$bf-&gt;<i>load_environment_config()</i>
<dd>Update flags based on user directives stored in the environment. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for details.
<dt>$bf-&gt;<i>load_maintainer_config()</i>
<dd>Update flags based on maintainer directives stored in the environment. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for details.
<dt>$bf-&gt;<i>load_config()</i>
<dd>Call successively <i>load_system_config()</i>, <i>load_user_config()</i>, <i>load_environment_config()</i> and <i>load_maintainer_config()</i> to update the default build flags defined by the vendor.
<dt>$bf-&gt;set($flag, $value, $source, $maint)
<dd>Update the build flag <tt>$flag</tt> with value <tt>$value</tt> and record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
<dt>$bf-&gt;set_feature($area, $feature, $enabled)
<dd>Update the boolean state of whether a specific feature within a known feature area has been enabled. The only currently known feature area is ``hardening''.
<dt>$bf-&gt;strip($flag, $value, $source, $maint)
<dd>Update the build flag <tt>$flag</tt> by stripping the flags listed in <tt>$value</tt> and record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
<dt>$bf-&gt;append($flag, $value, $source, $maint)
<dd>Append the options listed in <tt>$value</tt> to the current value of the flag <tt>$flag</tt>. Record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
<dt>$bf-&gt;prepend($flag, $value, $source, $maint)
<dd>Prepend the options listed in <tt>$value</tt> to the current value of the flag <tt>$flag</tt>. Record its origin as <tt>$source</tt> (if defined). Record it as maintainer modified if <tt>$maint</tt> is defined and true.
<dt>$bf-&gt;update_from_conffile($file, $source)
<dd>Update the current build flags based on the configuration directives contained in <tt>$file</tt>. See <i><a HREF="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></i>(1) for the format of the directives. 

 <tt>$source</tt> is the origin recorded for any build flag set or modified.
<dt>$bf-&gt;get($flag)
<dd>Return the value associated to the flag. It might be undef if the flag doesn't exist.
<dt>$bf-&gt;<i>get_feature_areas()</i>
<dd>Return the feature areas (i.e. the area values has_features will return true for).
<dt>$bf-&gt;get_features($area)
<dd>Return, for the given area, a hash with keys as feature names, and values as booleans indicating whether the feature is enabled or not.
<dt>$bf-&gt;get_origin($flag)
<dd>Return the origin associated to the flag. It might be undef if the flag doesn't exist.
<dt>$bf-&gt;is_maintainer_modified($flag)
<dd>Return true if the flag is modified by the maintainer.
<dt>$bf-&gt;has_features($area)
<dd>Returns true if the given area of features is known, and false otherwise. The only currently recognized area is ``hardening''.
<dt>$bf-&gt;has($option)
<dd>Returns a boolean indicating whether the flags exists in the object.
<dt>my @flags = $bf-&gt;<i>list()</i>
<dd>Returns the list of flags stored in the object.</dl><h2>Changes</h2><h3>Version 1.03</h3>New method: <tt>$bf</tt>-&gt;<i>get_feature_areas()</i> to list possible values for <tt>$bf</tt>-&gt;get_features. 

 New method <tt>$bf</tt>-&gt;<i>is_maintainer_modified()</i> and new optional parameter to <tt>$bf</tt>-&gt;<i>set()</i>, <tt>$bf</tt>-&gt;<i>append()</i>, <tt>$bf</tt>-&gt;<i>prepend()</i>, <tt>$bf</tt>-&gt;<i>strip()</i>.
<h3>Version 1.02</h3>New methods: <tt>$bf</tt>-&gt;<i>get_features()</i>, <tt>$bf</tt>-&gt;<i>has_features()</i>, <tt>$bf</tt>-&gt;<i>set_feature()</i>.
<h3>Version 1.01</h3>New method: <tt>$bf</tt>-&gt;<i>prepend()</i> very similar to <i>append()</i>. Implement support of the prepend operation everywhere. 

 New method: <tt>$bf</tt>-&gt;<i>load_maintainer_config()</i> that update the build flags based on the package maintainer directives.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;
