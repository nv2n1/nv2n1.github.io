---
title: "dpkgvendordefault(3)"
name: "dpkgvendordefault"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgvendordefault/"
---

Dpkg::Vendor::Default - default vendor object 

<h2>Description</h2>A vendor object is used to provide vendor specific behaviour in various places. This is the default object used in case there's none for the current vendor or in case the vendor could not be identified (see Dpkg::Vendor documentation). 

 It provides some hooks that are called by various dpkg-* tools. If you need a new hook, please file a bug against dpkg-dev and explain your need. Note that the hook <font SIZE="-1">API</font> has no guaranty to be stable over an extended period. If you run an important distribution that makes use of vendor hooks, you'd better submit them for integration so that we avoid breaking your code.
<h2>Functions</h2><dl COMPACT><dt>$vendor_obj = Dpkg::Vendor::Default-&gt;<i>new()</i>
<dd>Creates the default vendor object. Can be inherited by all vendor objects if they don't need any specific initialization at object creation time.
<dt>$vendor_obj-&gt;run_hook($id, @params)
<dd>Run the corresponding hook. The parameters are hook-specific. The supported hooks are:
<dl COMPACT><dd><dl COMPACT><dt>before-source-build ($srcpkg)
<dd>The first parameter is a Dpkg::Source::Package object. The hook is called just before the execution of <tt>$srcpkg</tt>-&gt;<i>build()</i>.
<dt>keyrings ()
<dd>The hook is called when dpkg-source is checking a signature on a source package. It takes no parameters, but returns a (possibly empty) list of vendor-specific keyrings.
<dt>register-custom-fields ()
<dd>The hook is called in Dpkg::Control::Fields to register custom fields. You should return a list of arrays. Each array is an operation to perform. The first item is the name of the operation and corresponds to a field_* function provided by Dpkg::Control::Fields. The remaining fields are the parameters that are passed unchanged to the corresponding function. 

 Known operations are ``register'', ``insert_after'' and ``insert_before''.
<dt>post-process-changelog-entry ($fields)
<dd>The hook is called in Dpkg::Changelog to post-process a Dpkg::Changelog::Entry after it has been created and filled with the appropriate values.
<dt>update-buildflags ($flags)
<dd>The hook is called in Dpkg::BuildFlags to allow the vendor to override the default values set for the various build flags. <tt>$flags</tt> is a Dpkg::BuildFlags object.</dl></dl><dl COMPACT><dd></dl></dl><h2>Changes</h2><h3>Version 0.xx</h3>This is a private module.
