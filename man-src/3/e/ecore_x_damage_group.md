---
title: "ecore_x_damage_group(3)"
name: "ecore_x_damage_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_damage_group/"
description: "X Damage Extension Functions – Functions related to the X Damage extension."
---

<p>X Damage Extension Functions &#8211; Functions related to the X Damage extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_damage_query</code> (void)<br />
 <i>Return whether the Damage Extension is available. </i><br />
 EAPI Ecore_X_Damage <code>ecore_x_damage_new</code> (Ecore_X_Drawable drawable, Ecore_X_Damage_Report_Level level)<br />
 <i>Creates a damage object. </i><br />
 EAPI void <code>ecore_x_damage_del</code> (Ecore_X_Damage damage)<br />
 <i>Destroys a damage object. </i><br />
 EAPI void <code>ecore_x_damage_subtract</code> (Ecore_X_Damage damage, Ecore_X_Region repair, Ecore_X_Region parts)<br />
 <i>Synchronously modifies the region. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X Damage extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_damage_del (Ecore_X_Damage damage)</h3>
<p>Destroys a damage object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>damage</i> The damage object to destroy.</dl>
<p> Destroys the damage object damage.</p>
<h3>EAPI Ecore_X_Damage ecore_x_damage_new (Ecore_X_Drawable drawable, Ecore_X_Damage_Report_Level level)</h3>
<p>Creates a damage object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>drawable</i> The drawable to monotor.<br />
 <i>level</i> The level of the damage report.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The damage object.</dl>
<p> Creates a damage object to monitor changes to drawable, with the level level.</p>
<h3>EAPI int ecore_x_damage_query (void)</h3>
<p>Return whether the Damage Extension is available. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the Damage Extension is available, 0 if not.</dl>
<p> Return 1 if the X server supports the Damage Extension version 1.0, 0 otherwise.</p>
<h3>EAPI void ecore_x_damage_subtract (Ecore_X_Damage damage, Ecore_X_Region repair, Ecore_X_Region parts)</h3>
<p>Synchronously modifies the region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>damage</i> The damage object to destroy.<br />
 <i>repair</i> The repair region.<br />
 <i>parts</i> The parts region.</dl>
<p> Synchronously modifies the regions in the following manner: If repair is XCB_NONE: 1) parts = damage 2) damage = &lt;empty&gt; Otherwise: 1) parts = damage INTERSECT repair 2) damage = damage &#8211; parts 3) Generate DamageNotify for remaining damage areas</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
