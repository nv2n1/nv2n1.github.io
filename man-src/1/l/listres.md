---
title: "listres(1)"
name: "listres"
section: "1"
letter: "l"
url: "/docs/linux/man/1-listres/"
description: "listres – list resources in widgets"
---

<h2 class="name">NAME</h2>
<p> listres &#8211; list resources in widgets </p>
<h2>SYNOPSIS</h2>
<p> <code>listres</code> [-option &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>listres</i> program generates a list of a widget&#8217;s resource database. The class in which each resource is first defined, the instance and class name, and the type of each resource is listed. If no specific widgets or the <i>-all</i> switch are given, a two-column list of widget names and their class hierarchies is printed.</p>
<h2>OPTIONS</h2>
<p> <i>Listres</i> accepts all of the standard toolkit command line options along with those listed below:</p>
<dl>
<dt><code>-all</code></p>
<dd> This option indicates that <i>listres</i> should print information for all known widgets and objects.</p>
<dt><code>-nosuper</code></p>
<dd> This option indicates that resources that are inherited from a superclass should not be listed. This is useful for determining which resources are new to a subclass.</p>
<dt><code>-variable</code></p>
<dd> This option indicates that widgets should be identified by the names of the class record variables rather than the class name given in the variable. This is useful for distinguishing subclasses that have the same class name as their superclasses.</p>
<dt><code>-top </code><i>name</i></p>
<dd> This option specifies the name of the widget to be treated as the top of the hierarchy. Case is not significant, and the name may match either the class variable name or the class name. The default is &#8220;core&#8221;.</p>
<dt><code>-format </code><i>printf-string</i></p>
<dd> This option specifies the <i>printf</i>-style format string to be used to print out the name, instance, class, and type of each resource.</dl>
<h2>X DEFAULTS</h2>
<p> To be written.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), appropriate widget documents</p>
<h2>BUGS</h2>
<p> On operating systems that do not support dynamic linking of run-time routines, this program must have all of its known widgets compiled in. The sources provide several tools for automating this process for various widget sets.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
