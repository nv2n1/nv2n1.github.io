---
title: "xkbchangemap(3)"
name: "xkbchangemap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangemap/"
description: "XkbChangeMap – Update only partial components of a keyboard description, modify the appropriate fields in the server and map components of a local copy of the keyboard description"
---

<p>XkbChangeMap &#8211; Update only partial components of a keyboard description, modify the appropriate fields in the server and map components of a local copy of the keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbMapChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>description from which new values are taken</p>
<dt><i>&#8211; changes</i></p>
<dd>identifies component parts to update</dl>
<h2>Description</h2>
<p>To update only partial components of a keyboard description, modify the appropriate fields in the server and map components of a local copy of the keyboard description, then call <i>XkbChangeMap </i> with an XkbMapChangesRec structure indicating which components have changed. </p>
<p> <i>XkbChangeMap </i> copies any components specified by the <i>changes </i> structure from the keyboard description, <i>xkb, </i> to the X server specified by <i>dpy.</i> </p>
<p> If any components specified by <i>changes </i> are not present in the <i>xkb </i> parameter, <i>XkbChangeMap </i> returns False. Otherwise, it sends a request to the server and returns True. </p>
<p> <i>XkbChangeMap </i> can generate BadAlloc, BadLength, and BadValue protocol errors.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The XkbChangeMap function returns True if the components specified by <i>changes </i> are present in the <i>xkb </i> parameter.</p>
<dt>False</p>
<dd>The XkbChangeMap function returns False if the components specified by <i>changes </i> are not present in the <i>xkb </i> parameter.</dl>
<h2>Structures</h2>
<p>Use the XkbMapChangesRec structure to identify and track partial modifications to the mapping components and to reduce the amount of traffic between the server and clients. </p>
<pre>typedef struct _XkbMapChanges {
 unsigned short changed; /* identifies valid components in 
structure */
 KeyCode min_key_code; /* lowest numbered keycode for device 
*/
 KeyCode max_key_code; /* highest numbered keycode for device 
*/
 unsigned char first_type; /* index of first key type modified */
 unsigned char num_types; /* # types modified */
 KeyCode first_key_sym; /* first key whose key_sym_map changed 
*/
 unsigned char num_key_syms; /* # key_sym_map entries changed */
 KeyCode first_key_act; /* first key whose key_acts entry 
changed */
 unsigned char num_key_acts; /* # key_acts entries changed */
 KeyCode first_key_behavior; /* first key whose behaviors changed */
 unsigned char num_key_behaviors; /* # behaviors entries changed */
 KeyCode first_key_explicit; /* first key whose explicit entry 
changed */
 unsigned char num_key_explicit; /* # explicit entries changed */
 KeyCode first_modmap_key; /* first key whose modmap entry changed 
*/
 unsigned char num_modmap_keys; /* # modmap entries changed */
 KeyCode first_vmodmap_key; /* first key whose vmodmap changed */
 unsigned char num_vmodmap_keys; /* # vmodmap entries changed */
 unsigned char pad1; /* reserved */
 unsigned short vmods; /* mask indicating which vmods changed 
*/
} XkbMapChangesRec,*XkbMapChangesPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadLength</code></p>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
