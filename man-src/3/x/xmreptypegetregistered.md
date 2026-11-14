---
title: "xmreptypegetregistered(3)"
name: "xmreptypegetregistered"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypegetregistered/"
description: "XmRepTypeGetRegistered — A representation type manager function that returns a copy of the registration list"
---

<p><code>XmRepTypeGetRegistered</code> &#8212; A representation type manager function that returns a copy of the registration list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>XmRepTypeList XmRepTypeGetRegistered</code>(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmRepTypeGetRegistered</code> retrieves information about all representation types that are registered with the representation type manager. The registration list is an array of structures, each of which contains information for a representation type entry. The end of the registration list is marked with a representation type entry whose <i>rep_type_name</i> field has a NULL pointer. This routine allocates memory for the returned data. The application must free this memory using <code>XtFree</code>. </p>
<p> The representation type entry structure contains the following information: </p>
<pre>typedef struct
{
 String <i>rep_type_name</i>;
 String *<i>value_names</i>;
 unsigned char *<i>values</i>;
 unsigned char <i>num_values</i>;
 Boolean <i>reverse_installed</i>;
 XmRepTypeId <i>rep_type_id</i>;
} XmRepTypeEntryRec, *XmRepTypeList;
(<code>void</code>)</pre>
<dl COMPACT>
<dt><i>rep_type_name</i></p>
<dd>The name of the representation type</p>
<dt><i>value_names</i></p>
<dd>An array of representation type value names</p>
<dt><i>values</i></p>
<dd>An array of representation type numerical values</p>
<dt><i>num_values</i></p>
<dd>The number of values associated with the representation type</p>
<dt><i>reverse_installed</i></p>
<dd>A flag that indicates whether or not the reverse converter is installed</p>
<dt><i>rep_type_id</i></p>
<dd>The identification number of the representation type</dl>
<h2>Return</h2>
<p>Returns a pointer to the registration list of representation types.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3) and <code><a href="/docs/linux/man/3-xmreptypegetrecord/">XmRepTypeGetRecord</a></code>(3).</p>
