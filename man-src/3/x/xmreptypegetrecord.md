---
title: "xmreptypegetrecord(3)"
name: "xmreptypegetrecord"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmreptypegetrecord/"
description: "XmRepTypeGetRecord — A representation type manager function that returns information about a representation type"
---

<p><code>XmRepTypeGetRecord</code> &#8212; A representation type manager function that returns information about a representation type</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RepType.h&gt;
<code>XmRepTypeEntry XmRepTypeGetRecord</code>(
<code>XmRepTypeId rep_type_id</code>);</pre>
<h2>Description</h2>
<p><code>XmRepTypeGetRecord</code> retrieves information about a particular representation type that is registered with the representation type manager. This routine allocates memory for the returned data. The application must free this memory using <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>rep_type_id</i></dt>
<dd>The identification number of the representation type</dd></dl>
<p> The representation type entry structure contains the following information: </p>
<pre>typedef struct
{
 String <i>rep_type_name</i>;
 String *<i>value_names</i>;
 unsigned char *<i>values</i>;
 unsigned char <i>num_values</i>;
 Boolean <i>reverse_installed</i>;
 XmRepTypeId <i>rep_type_id</i>;
} XmRepTypeEntryRec, *XmRepTypeEntry;
(<code>void</code>)</pre>
<dl COMPACT>
<dt><i>rep_type_name</i></dt>
<dd>The name of the representation type</dd>
<dt><i>value_names</i></dt>
<dd>An array of representation type value names</dd>
<dt><i>values</i></dt>
<dd>An array of representation type numerical values</dd>
<dt><i>num_values</i></dt>
<dd>The number of values associated with the representation type</dd>
<dt><i>reverse_installed</i></dt>
<dd>A flag that indicates whether or not the reverse converter is installed</dd>
<dt><i>rep_type_id</i></dt>
<dd>The identification number of the representation type</dd></dl>
<h2>Return</h2>
<p>Returns a pointer to the representation type entry structure that describes the representation type.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmreptypegetid/">XmRepTypeGetId</a></code>(3), <code><a href="/docs/linux/man/3-xmreptypegetregistered/">XmRepTypeGetRegistered</a></code>(3), and <code><a href="/docs/linux/man/3-xmreptyperegister/">XmRepTypeRegister</a></code>(3).</p>
