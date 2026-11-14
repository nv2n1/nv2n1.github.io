---
title: "xkbgetcompatmap(3)"
name: "xkbgetcompatmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetcompatmap/"
description: "XkbGetCompatMap – Fetch any combination of the current compatibility map components from the server"
---

<p>XkbGetCompatMap &#8211; Fetch any combination of the current compatibility map components from the server </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetCompatMap</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescRec *</code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of compatibility map components to fetch</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description where results placed</dl>
<h2>Description</h2>
<p>When another client modifies the compatibility map, you are notified if you have selected for XkbCompatMapNotify events. <i>XkbGetCompatMap </i> is particularly useful when you receive an event of this type, as it allows you to update your program&#8217;s version of the compatibility map to match the modified version now in the server. If your program is dealing with multiple servers and needs to configure them all in a similar manner, the updated compatibility map may be used to reconfigure other servers. </p>
<p> <i>XkbGetCompatMap </i> fetches the components of the compatibility map specified in <i>which </i> from the server specified by <i>display </i> and places them in the <i>compat </i> structure of the keyboard description <i>xkb. </i> Valid values for <i>which </i> are an inclusive OR of the values shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Compatibility Map Component Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Value</td>
<td>Affecting
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSymInterpMask</td>
<td>(1&lt;&lt;0)</td>
<td>Symbol interpretations
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupCompatMask</td>
<td>(1&lt;&lt;1)</td>
<td>Group maps
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllCompatMask</td>
<td>(0x3)</td>
<td>All compatibility map components
</td>
</tr>
</table>
<p> If no compatibility map structure is allocated in <i>xkb </i> upon entry, <i>XkbGetCompatMap </i> allocates one. If one already exists, its contents are overwritten with the returned results. </p>
<p> <i>XkbGetCompatMap </i> fetches compatibility map information for the device specified by the <i>device_spec </i> field of <i>xkb. </i> Unless you have specifically modified this field, it is the default keyboard device. <i>XkbGetCompatMap </i> returns Success if successful, BadAlloc if it is unable to obtain necessary storage for either the return values or work space, BadMatch if the <i>dpy </i> field of the <i>xkb </i> argument is non-NULL and does not match the <i>display </i> argument, and BadLength under certain conditions caused by server or Xkb implementation errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadLength</code></p>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid </p>
</dl>
