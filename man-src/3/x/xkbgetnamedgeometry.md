---
title: "xkbgetnamedgeometry(3)"
name: "xkbgetnamedgeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetnamedgeometry/"
description: "XkbGetNamedGeometry – Loads a keyboard geometry description from this database by name"
---

<p>XkbGetNamedGeometry &#8211; Loads a keyboard geometry description from this database by name </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetNamedGeometry</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>Atom </code><i>name</i><code>);</code></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description into which the geometry should be loaded</p>
<dt><i>&#8211; name</i></p>
<dd>name of the geometry to be loaded</dl>
<h2>Description</h2>
<p>It is also possible to load a keyboard geometry by name. The X server maintains a database of keyboard components (see below). </p>
<p> <i>XkbGetNamedGeometry </i> can return BadName if the name cannot be found. </p>
<p> The X server maintains a database of keyboard components, identified by component type. The database contains all the information necessary to build a complete keyboard description for a particular device, as well as to assemble partial descriptions. Table 1 identifies the component types and the type of information they contain. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Server Database Keyboard Components
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Component</td>
<td>Component Primary Contents</td>
<td>May also contain
</td>
</tr>
<tr VALIGN=top>
<td>Type</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Keymap</td>
<td> Complete keyboard description<br />
 Normally assembled using a complete component from each of the other types </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Keycodes</td>
<td> Symbolic name for each key<br />
 Minimum and maximum legal keycodes </td>
<td> Aliases for some keys<br />
 Symbolic names for indicators<br />
 Description of indicators physically present
</td>
</tr>
<tr VALIGN=top>
<td>Types</td>
<td>Key types</td>
<td> Real modifier bindings and symbolic names for some virtual modifiers
</td>
</tr>
<tr VALIGN=top>
<td>Compatibility</td>
<td> Rules used to assign actions to keysyms </td>
<td> Maps for some indicators<br />
 Real modifier bindings and symbolic names for some virtual modifiers
</td>
</tr>
<tr VALIGN=top>
<td>Symbols</td>
<td> Symbol mapping for keyboard keys<br />
 Modifier mapping<br />
 Symbolic names for groups </td>
<td> Explicit actions and behaviors for some keys<br />
 Real modifier bindings and symbolic names for some virtual modifiers
</td>
</tr>
<tr VALIGN=top>
<td>Geometry</td>
<td>Layout of the keyboard</td>
<td> Aliases for some keys; overrides keycodes component aliases<br />
 Symbolic names for some indicators<br />
 Description of indicators physically present
</td>
</tr>
</table>
<p> While a keymap is a database entry for a complete keyboard description, and therefore logically different from the individual component database entries, the rules for processing keymap entries are identical to those for the individual components. In the discussion that follows, the term component is used to refer to either individual components or a keymap. </p>
<p> There may be multiple entries for each of the component types. An entry may be either <i>complete </i> or <i>partial. </i> Partial entries describe only a piece of the corresponding keyboard component and are designed to be combined with other entries of the same type to form a complete entry. </p>
<p> For example, a partial symbols map might describe the differences between a common ASCII keyboard and some national layout. Such a partial map is not useful on its own because it does not include those symbols that are the same on both the ASCII and national layouts (such as function keys). On the other hand, this partial map can be used to configure <i>any </i> ASCII keyboard to use a national layout. </p>
<p> When a keyboard description is built, the components are processed in the order in which they appear in Table 1; later definitions override earlier ones.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadName</code></p>
<dd>A font or color of the specified name does not exist. </p>
</dl>
