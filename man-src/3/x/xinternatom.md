---
title: "xinternatom(3)"
name: "xinternatom"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xinternatom/"
description: "XInternAtom, XInternAtoms, XGetAtomName, XGetAtomNames – create or return atom names"
---

<p>XInternAtom, XInternAtoms, XGetAtomName, XGetAtomNames &#8211; create or return atom names </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Atom XInternAtom(Display *<i>display</i>, char *<i>atom_name</i>, Bool <i>only_if_exists</i>);</p>
<dd>Status XInternAtoms(Display *<i>display</i>, char **<i>names</i>, int <i>count</i>, Bool <i>only_if_exists</i>, Atom *<i>atoms_return</i>);</p>
<dd>char *XGetAtomName(Display *<i>display</i>, Atom <i>atom</i>);</p>
<dd>Status XGetAtomNames(Display *<i>display</i>, Atom *<i>atoms</i>, int <i>count</i>, char **<i>names_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>atom</i></p>
<dd>Specifies the atom for the property name you want returned.</p>
<dt><i>atoms</i></p>
<dd>Specifies the array of atoms.</p>
<dt><i>atom_name</i></p>
<dd>Specifies the name associated with the atom you want returned.</p>
<dt><i>atoms_return</i></p>
<dd>Returns the atoms.</p>
<dt><i>count</i></p>
<dd>Specifies the number of atom names in the array.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>names</i></p>
<dd>Specifies the array of atom names.</p>
<dt><i>names_return</i></p>
<dd>Returns the atom names.</p>
<dt><i>only_if_exists</i></p>
<dd>Specifies a Boolean value that indicates whether the atom must be created.</dl>
<h2>Description</h2>
<p>The <code>XInternAtom</code> function returns the atom identifier associated with the specified atom_name string. If only_if_exists is <code>False</code>, the atom is created if it does not exist. Therefore, <code>XInternAtom</code> can return <code>None</code>. If the atom name is not in the Host Portable Character Encoding, the result is implementation-dependent. Uppercase and lowercase matter; the strings &#8220;thing&#8221;, &#8220;Thing&#8221;, and &#8220;thinG&#8221; all designate different atoms. The atom will remain defined even after the client&#8217;s connection closes. It will become undefined only when the last connection to the X server closes. </p>
<p> <code>XInternAtom</code> can generate <code>BadAlloc</code> and <code>BadValue</code> errors. </p>
<p> The <code>XInternAtoms</code> function returns the atom identifiers associated with the specified names. The atoms are stored in the atoms_return array supplied by the caller. Calling this function is equivalent to calling <code>XInternAtom</code> for each of the names in turn with the specified value of only_if_exists, but this function minimizes the number of round-trip protocol exchanges between the client and the X server. </p>
<p> This function returns a nonzero status if atoms are returned for all of the names; otherwise, it returns zero. </p>
<p> <code>XInternAtoms</code> can generate <code>BadAlloc</code> and <code>BadValue</code> errors. </p>
<p> The <code>XGetAtomName</code> function returns the name associated with the specified atom. If the data returned by the server is in the Latin Portable Character Encoding, then the returned string is in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. To free the resulting string, call <code>XFree</code>. </p>
<p> <code>XGetAtomName</code> can generate a <code>BadAtom</code> error. </p>
<p> The <code>XGetAtomNames</code> function returns the names associated with the specified atoms. The names are stored in the names_return array supplied by the caller. Calling this function is equivalent to calling <code>XGetAtomName</code> for each of the atoms in turn, but this function minimizes the number of round-trip protocol exchanges between the client and the X server. </p>
<p> This function returns a nonzero status if names are returned for all of the atoms; otherwise, it returns zero. </p>
<p> <code>XGetAtomNames</code> can generate a <code>BadAtom</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xgetwindowproperty/">XGetWindowProperty</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
