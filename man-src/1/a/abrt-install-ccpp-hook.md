---

title: "abrt-install-ccpp-hook(1)"
name: "abrt-install-ccpp-hook"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-install-ccpp-hook/"
---

abrt-install-ccpp-hook - Install coredump handler. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-install-ccpp-hook</i> install | uninstall | is-installed

<h2>DESCRIPTION</h2>

 

 <i>abrt-install-ccpp-hook</i> registers ABRT coredump handler (which saves segfault data) into kernel.

<h2>OPTIONS</h2>

 

 install
<dl>
<dt>
</dt><dd> Install coredump handler.</dd></dl>
 

 uninstall
<dl>
<dt>
</dt><dd> Uninstall coredump handler.</dd></dl>
 

 is-installed
<dl>
<dt>
</dt><dd> Returns 0 if handler is installed, otherwise 1.</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
