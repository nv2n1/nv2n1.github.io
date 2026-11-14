---
title: "dpkg(3)"
name: "dpkg"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkg/"
---

Dpkg - module with core variables 

<h2>Description</h2>The Dpkg module provides a set of variables with information concerning this system installation.
<h2>Variables</h2><dl COMPACT><dt>$Dpkg::PROGNAME
<dd>Contains the name of the current program.
<dt>$Dpkg::PROGVERSION
<dd>Contains the version of the dpkg suite.
<dt>$Dpkg::CONFDIR
<dd>Contains the path to the dpkg system configuration directory.
<dt>$Dpkg::ADMINDIR
<dd>Contains the path to the dpkg database directory.
<dt>$Dpkg::LIBDIR
<dd>Contains the path to the dpkg methods and plugins directory.
<dt>$Dpkg::DATADIR
<dd>Contains the path to the dpkg architecture tables directory.</dl><h2>Changes</h2><h3>Version 1.01</h3>New variables: <tt>$PROGNAME</tt>, <tt>$PROGVERSION</tt>, <tt>$CONFDIR</tt>, <tt>$ADMINDIR</tt>, <tt>$LIBDIR</tt> and <tt>$DATADIR</tt>. 

 Deprecated variables: <tt>$version</tt>, <tt>$admindir</tt>, <tt>$dpkglibdir</tt> and <tt>$pkgdatadir</tt>.
<h3>Version 1.00</h3>Mark the module as public.
