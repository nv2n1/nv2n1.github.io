---
title: "dpkgvendor(3)"
name: "dpkgvendor"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgvendor/"
---

Dpkg::Vendor - get access to some vendor specific information 

<h2>Description</h2>The files in <tt>$Dpkg::CONFDIR</tt>/origins/ can provide information about various vendors who are providing Debian packages. Currently those files look like this: 

 <pre> Vendor: Debian
 Vendor-URL: <a rel="nofollow" HREF="https://www.debian.org/">https://www.debian.org/</a>
 Bugs: debbugs://bugs.debian.org</pre>If the vendor derives from another vendor, the file should document the relationship by listing the base distribution in the Parent field: 

 <pre> Parent: Debian</pre>The file should be named according to the vendor name.
<h2>Functions</h2><dl COMPACT><dt>$dir = <i>Dpkg::Vendor::get_vendor_dir()</i>
<dd>Returns the current dpkg origins directory name, where the vendor files are stored.
<dt>$fields = Dpkg::Vendor::get_vendor_info($name)
<dd>Returns a Dpkg::Control object with the information parsed from the corresponding vendor file in <tt>$Dpkg::CONFDIR</tt>/origins/. If <tt>$name</tt> is omitted, it will use <tt>$Dpkg::CONFDIR</tt>/origins/default which is supposed to be a symlink to the vendor of the currently installed operating system. Returns undef if there's no file for the given vendor.
<dt>$name = Dpkg::Vendor::get_vendor_file($name)
<dd>Check if there's a file for the given vendor and returns its name.
<dt>$name = <i>Dpkg::Vendor::get_current_vendor()</i>
<dd>Returns the name of the current vendor. If <font SIZE="-1">DEB_VENDOR</font> is set, it uses that first, otherwise it falls back to parsing <tt>$Dpkg::CONFDIR</tt>/origins/default. If that file doesn't exist, it returns undef.
<dt>$object = Dpkg::Vendor::get_vendor_object($name)
<dd>Return the Dpkg::Vendor::* object of the corresponding vendor. If <tt>$name</tt> is omitted, return the object of the current vendor. If no vendor can be identified, then return the Dpkg::Vendor::Default object.
<dt>Dpkg::Vendor::run_vendor_hook($hookid, @params)
<dd>Run a hook implemented by the current vendor object.</dl><h2>Changes</h2><h3>Version 1.01</h3>New function: <i>get_vendor_dir()</i>.
<h3>Version 1.00</h3>Mark the module as public.
