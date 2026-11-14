---
title: "dpkgbuildenv(3)"
name: "dpkgbuildenv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgbuildenv/"
---

Dpkg::BuildEnv - track build environment 

<h2>Description</h2>The Dpkg::BuildEnv module is used by dpkg-buildflags to track the build environment variables being used and modified.
<h2>Functions</h2><dl COMPACT><dt>$bf-&gt;set($varname, $value)
<dd>Update the build environment variable <tt>$varname</tt> with value <tt>$value</tt>. Record it as being accessed and modified.
<dt>$bf-&gt;get($varname)
<dd>Get the build environment variable <tt>$varname</tt> value. Record it as being accessed.
<dt>$bf-&gt;has($varname)
<dd>Return a boolean indicating whether the environment variable exists. Record it as being accessed.
<dt>my @list = $bf-&gt;<i>list_accessed()</i>
<dd>Returns a list of all environment variables that have been accessed.
<dt>my @list = $bf-&gt;<i>list_modified()</i>
<dd>Returns a list of all environment variables that have been modified.</dl><h2>Changes</h2><h3>Version 0.xx</h3>This is a private module.
