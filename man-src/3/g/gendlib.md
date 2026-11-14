---
title: "gendlib(3)"
name: "gendlib"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gendlib/"
description: "gendlib – perl library for querying genders file"
---

<h2>NAME</h2>
<p> gendlib &#8211; perl library for querying genders file</p>
<h2>SYNOPSIS</h2>
<p> require &#8220;/usr/lib/genders/gendlib.pl&#8221;;</p>
<h2>DESCRIPTION</h2>
<p> This package contains common functions for manipulating the genders file. Previously this code existed only in the nodeattr command, but applications that must repeatedly call nodeattr would spend a great deal of time reading and parsing the genders file. These functions create an in-memory cache of genders on the first call; subsequent calls need only reference the in-memory copy and are thus speeded up. </p>
<p> <code>Initialization:</code> </p>
<p> Genders::init([$path_genders])</p>
<dl>
<dt>
<dd> Function normally called internally for initialization. It can be called externally with a non-default genders file path and subsequent operations will use this non-default data. May be called more than once to change genders file.</dl>
<p> <code>Simple Queries:</code> </p>
<p> Genders::hasattr($attribute, [$node])</p>
<dl>
<dt>
<dd> Return 1 if node has attribute, 0 if not. If node is not specified, use local node.</dl>
<p> Genders::getattrval($attribute, [$node])</p>
<dl>
<dt>
<dd> Return value of attribute held by node, or empty string if no value or node does not have attribute. If node is not specified, use local node.</dl>
<p> Genders::getnode([$attribute])</p>
<dl>
<dt>
<dd> Return a list of nodes having the specified attribute. If a value is also specified (&quot;attr=val&quot;), only nodes with the specified attribute and value are returned. If no attribute is specified, getnode returns all the nodes listed in the genders file.</dl>
<p> Genders::getattr([$node])</p>
<dl>
<dt>
<dd> Return a list of attributes held by node. If node is not specified, use local node.</dl>
<p> <code>Complex Queries:</code> </p>
<p> Genders::getallattr()</p>
<dl>
<dt>
<dd> Return a list of all attributes in the genders file (one cluster only).</dl>
<p> Genders::get_node_hash(\%node)</p>
<dl>
<dt>
<dd> Get a copy of hash of attributes to node lists for the current cluster (a &quot;hash of lists&quot;). Ensure that keys exist for all possible attributes across clusters (though they may point to empty lists).</dl>
<p> Genders::get_clusters()</p>
<dl>
<dt>
<dd> Return a list with the local cluster name as the first and only element. get_clusters() returns a list instead of a scalar for backwards compatability. If the local cluster name is not known, null is returned.</dl>
<p> Genders::gendexp($exp, [$node])</p>
<dl>
<dt>
<dd> Evaluate expression involving genders attributes and return the result of the evaluation. Any legal perl expresion using numeric constants, genders attributes (which are converted into $variables), and the following operators is valid: !, ||, &amp;&amp;, *, +, -, /. If $node is not specified, assume the local host.</dl>
<p> <code>Conversion:</code> </p>
<p> Genders::to_altnames()</p>
<dl>
<dt>
<dd> Given a list of hostnames as they appear in the genders file, return a list of alternate names. On the SP, genders names are assumed to be the initial_hostnames, and we use the SDR to convert to reliable_hostnames. On other systems, we look for the value of the altname attribute in the genders file. If the input hostname cannot be converted, it is preserved in the output.</dl>
<p> Genders::to_gendnames()</p>
<dl>
<dt>
<dd> Performs the inverse of the to_altnames() function. Just like to_altnames(), an input hostname is preserved in the output if it cannot be converted.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nodeattr/">nodeattr</a>(1), <a href="/docs/linux/man/3-libgenders/">libgenders</a>(3), <a href="/docs/linux/man/3-libgenders/">Libgenders</a>(3) </p>
<h2>Index</h2>
