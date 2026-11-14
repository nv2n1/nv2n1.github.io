---
title: "xkbaddgeomkeyalias(3)"
name: "xkbaddgeomkeyalias"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddgeomkeyalias/"
description: "XkbAddGeomKeyAlias – Add one key alias to an existing keyboard geometry description"
---

<p>XkbAddGeomKeyAlias &#8211; Add one key alias to an existing keyboard geometry description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbKeyAliasPtr XkbAddGeomKeyAlias</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>char *</code><i>alias</i><code>,</code> <code>char *</code><i>real</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry to be updated</p>
<dt><i>&#8211; alias</i></p>
<dd>alias to be added</p>
<dt><i>&#8211; real</i></p>
<dd>real name to be bound to the new alias</dl>
<h2>Description</h2>
<p>Xkb provides functions to add a single new element to the top-level keyboard geometry. In each case the <i>num_ * </i> fields of the corresponding structure is incremented by 1. These functions do not change <i>sz_* </i> unless there is no more room in the array. Some of these functions fill in the values of the element&#8217;s structure from the arguments. For other functions, you must explicitly write code to fill the structure&#8217;s elements. </p>
<p> The top-level geometry description includes a list of <i>geometry properties. </i> A geometry property associates an arbitrary string with an equally arbitrary name. Programs that display images of keyboards can use geometry properties as hints, but they are not interpreted by Xkb. No other geometry structures refer to geometry properties. </p>
<p> <i>XkbAddGeomKeyAlias </i> adds one key alias with the value <i>alias </i> to the geometry <i>geom, </i> and associates it with the key whose real name is <i>real. XkbAddGeomKeyAlias </i> returns NULL if any of the parameters is empty or if it was not able to allocate space for the alias. To allocate space for an arbitrary number of aliases, use the <i>XkbAllocGeomKeyAliases </i> function.</p>
<h2>Structures</h2>
<pre> typedef struct {
 char real[XkbKeyNameLength]; /* this key name must be in the keys array */
 char alias[XkbKeyNameLength]; /* symbolic key name as alias for the key */
 } XkbKeyAliasRec,*XkbKeyAliasPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocgeomkeyaliases/">XkbAllocGeomKeyAliases</a></code>(3)</p>
