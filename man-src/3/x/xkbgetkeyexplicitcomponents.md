---
title: "xkbgetkeyexplicitcomponents(3)"
name: "xkbgetkeyexplicitcomponents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeyexplicitcomponents/"
description: "XkbGetKeyExplicitComponents – Obtain the explicit components (the explicit array) for a subset of the keys in a keyboard description"
---

<p>XkbGetKeyExplicitComponents &#8211; Obtain the explicit components (the explicit array) for a subset of the keys in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyExplicitComponents</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key to fetch</p>
<dt><i>&#8211; num</i></p>
<dd>number of keys for which to get explicit info</p>
<dt><i>&#8211; xkb</i></p>
<dd>Xkb description in which to put results</dl>
<h2>Description</h2>
<p>Whenever a client remaps the keyboard using core protocol requests, Xkb examines the map to determine likely default values for the components that cannot be specified using the core protocol (see Core Keyboard Mapping to Xkb Keyboard Mapping Transformation for more information on how Xkb chooses the default values). </p>
<p> DO THE FOUR PAGES OF &quot;CORE KEYBOARD MAPPING TO XKB KEYBOARD MAPPING TRANSFORMATION&quot; NEED TO BE ADDED HERE? </p>
<p> This automatic remapping might replace definitions explicitly requested by an application, so the Xkb keyboard description defines an explicit components mask for each key. Any aspects of the automatic remapping listed in the explicit components mask for a key are not changed by the automatic keyboard mapping.<br />
&nbsp; The explicit components masks are held in the <i>explicit </i> field of the server map, which is an array indexed by keycode. Each entry in this array is a mask that is a bitwise inclusive OR of the values shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Explicit Component Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Bit in Explicit Mask</td>
<td>Value</td>
<td>Protects Against
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType1</td>
<td>(1&lt;&lt;0)</td>
<td> Automatic determination of the key type associated with Group1.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType2</td>
<td>(1&lt;&lt;1)</td>
<td> Automatic determination of the key type associated with Group2.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType3</td>
<td>(1&lt;&lt;2)</td>
<td> Automatic determination of the key type associated with Group3.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitKeyType4</td>
<td>(1&lt;&lt;3)</td>
<td> Automatic determination of the key type associated with Group4.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitInterpret</td>
<td>(1&lt;&lt;4)</td>
<td> Application of any of the fields of a symbol interpretation to the key in question.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitAutoRepeat</td>
<td>(1&lt;&lt;5)</td>
<td> Automatic determination of auto-repeat status for the key, as specified in a symbol interpretation.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitBehavior</td>
<td>(1&lt;&lt;6)</td>
<td> Automatic assignment of the XkbKB_Lock behavior to the key, if the XkbSI_LockingKey flag is set in a symbol interpretation.
</td>
</tr>
<tr VALIGN=top>
<td>ExplicitVModMap</td>
<td>(1&lt;&lt;7)</td>
<td> Automatic determination of the virtual modifier map for the key based on the actions assigned to the key and the symbol interpretations that match the key.
</td>
</tr>
</table>
<p> <i>XkbGetKeyExplicitComponents </i> sends a request to the server to obtain the explicit components for <i>num </i> keys on the keyboard starting with key <i>first. </i> It waits for a reply and returns the explicit components in the <i>server-&gt;explicit </i> array of <i>xkb. </i> If successful, <i>XkbGetKeyExplicitComponents </i> returns Success. The <i>xkb </i> parameter must be a pointer to a valid Xkb keyboard description. </p>
<p> If the <i>server </i> map in the <i>xkb </i> parameter has not been allocated, <i>XkbGetKeyExplicitComponents </i> allocates and initializes it before obtaining the actions. </p>
<p> If the server does not have a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbGetKeyExplicitComponents </i> returns BadMatch. If <i>num </i> is less than 1 or greater than XkbMaxKeyCount, <i>XkbGetKeyExplicitComponents </i> returns BadValue. If any allocation errors occur, <i>XkbGetKeyExplicitComponents </i> returns BadAlloc.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
