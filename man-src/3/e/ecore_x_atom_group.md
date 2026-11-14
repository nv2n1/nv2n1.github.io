---
title: "ecore_x_atom_group(3)"
name: "ecore_x_atom_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_atom_group/"
description: "XCB Atom Functions – Functions that operate on atoms."
---

<p>XCB Atom Functions &#8211; Functions that operate on atoms. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_atom_get_prefetch</code> (const char *name)<br />
 <i>Sends the InternAtom request. </i><br />
 EAPI void <code>ecore_x_atom_get_fetch</code> (void)<br />
 <i>Gets the reply of the InternAtom request sent by </i><code>ecore_x_atom_get_prefetch()</code>.<br />
 EAPI Ecore_X_Atom <code>ecore_x_atom_get</code> (const char *name __UNUSED__)<br />
 <i>Retrieves the atom value associated to a name. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on atoms.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_X_Atom ecore_x_atom_get (const char *name __UNUSED__)</h3>
<p>Retrieves the atom value associated to a name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Unused.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Associated atom value.</dl>
<p> Retrieves the atom value associated to a name. The reply is the returned value of the function ecore_xcb_intern_atom_reply(). If reply is NULL, the NULL atom is returned. Otherwise, the atom associated to the name is returned. </p>
<p> To use this function, you must call before, and in order, <code>ecore_x_atom_get_prefetch()</code>, which sends the InternAtom request, then <code>ecore_x_atom_get_fetch()</code>, which gets the reply. </p>
<p> References ecore_x_atom_get().</p>
<h3>EAPI void ecore_x_atom_get_prefetch (const char * name)</h3>
<p>Sends the InternAtom request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Name of the requested atom.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
