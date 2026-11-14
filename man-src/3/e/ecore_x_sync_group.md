---
title: "ecore_x_sync_group(3)"
name: "ecore_x_sync_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_sync_group/"
description: "X Sync Extension Functions – Functions related to the X Sync extension."
---

<p>X Sync Extension Functions &#8211; Functions related to the X Sync extension. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_x_sync_query</code> (void)<br />
 <i>Return whether the X server supports the Sync Extension. </i><br />
 EAPI Ecore_X_Sync_Alarm <code>ecore_x_sync_alarm_new</code> (Ecore_X_Sync_Counter counter)<br />
 <i>Create a new alarm. </i><br />
 EAPI int <code>ecore_x_sync_alarm_free</code> (Ecore_X_Sync_Alarm alarm)<br />
 <i>Delete an alarm. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to the X Sync extension.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_x_sync_alarm_free (Ecore_X_Sync_Alarm alarm)</h3>
<p>Delete an alarm. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alarm</i> The alarm to delete.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> Delete the alarm. Returns 1 on success, 0 otherwise.</p>
<h3>EAPI Ecore_X_Sync_Alarm ecore_x_sync_alarm_new (Ecore_X_Sync_Counter counter)</h3>
<p>Create a new alarm. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>counter</i> A counter.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly created alarm.</dl>
<p> Create a new alarm. </p>
<p> References ecore_x_sync().</p>
<h3>EAPI int ecore_x_sync_query (void)</h3>
<p>Return whether the X server supports the Sync Extension. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the X Sync Extension is available, 0 otherwise.</dl>
<p> Return 1 if the X server supports the Sync Extension version 3.0, 0 otherwise.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
