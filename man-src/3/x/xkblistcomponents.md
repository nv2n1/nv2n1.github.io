---
title: "xkblistcomponents(3)"
name: "xkblistcomponents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblistcomponents/"
description: "XkbListComponents – List of components for one or more component types"
---

<p>XkbListComponents &#8211; List of components for one or more component types </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbComponentListPtr XkbListComponents</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>XkbComponentNamesPtr </code><i>ptrns</i><code>,</code> <code>int *</code><i>max_inout</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; ptrns</i></p>
<dd>namelist for components of interest</p>
<dt><i>&#8211; max_inout</i></p>
<dd>max # returned names, # left over</dl>
<h2>Description</h2>
<p>You may ask the server for a list of components for one or more component types. The request takes the form of a set of patterns, one pattern for each of the component types, including a pattern for the complete keyboard description. To obtain this list, use <i>XkbListComponents.</i> </p>
<p> <i>XkbListComponents </i> queries the server for a list of component names matching the patterns specified in <i>ptrns. </i> It waits for a reply and returns the matching component names in an XkbComponentListRec structure. When you are done using the structure, you should free it using <i>XkbFreeComponentList. device_spec </i> indicates a particular device in which the caller is interested. A server is allowed (but not required) to restrict its reply to portions of the database that are relevant for that particular device. </p>
<p> <i>ptrns </i> is a pointer to an XkbComponentNamesRec. Each of the fields in <i>ptrns </i> contains a pattern naming the components of interest. Each of the patterns is composed of characters from the ISO Latin1 encoding, but can contain only parentheses, the wildcard characters `?&#8217; and `*&#8217;, and characters permitted in a component class or member name. A pattern may be NULL, in which case no components for that type is returned. Pattern matches with component names are case sensitive. The `?&#8217; wildcard matches any single character, except a left or right parenthesis; the `*&#8217; wildcard matches any number of characters, except a left or right parenthesis. If an implementation allows additional characters in a component class or member name other than those required by the Xkb extension, the result of comparing one of the additional characters to either of the wildcard characters is implementation-dependent. </p>
<p> If a pattern contains illegal characters, the illegal characters are ignored. The matching process is carried out as if the illegal characters were omitted from the pattern. </p>
<p> <i>max_inout </i> is used to throttle the amount of data passed to and from the server. On input, it specifies the maximum number of names to be returned (the total number of names in all component categories). Upon return from <i>XkbListComponents, </i> max_inout contains the number of names that matched the request but were not returned because of the limit. </p>
<p> <code>Component Names</code> </p>
<p> Component names have the form <i>class(member) </i> where <i>class </i> describes a subset of the available components for a particular type and the optional <i>member </i> identifies a specific component from that subset. For example, the name &quot;atlantis(acme)&quot; for a symbols component might specify the symbols used for the atlantis national keyboard layout by the vendor &quot;acme.&quot; Each class has an optional <i>default </i> member &#8211; references that specify a class but not a member refer to the default member of the class, if one exists. Xkb places no constraints on the interpretation of the class and member names used in component names. </p>
<p> The <i>class </i> and <i>member </i> names are both specified using characters from the Latin-1 character set. Xkb implementations must accept all alphanumeric characters, minus (`-&#8216;) and underscore (`_&#8217;) in class or member names, and must not accept parentheses, plus, vertical bar, percent sign, asterisk, question mark, or white space. The use of other characters is implementation-dependent.</p>
<h2>Structures</h2>
<p>The component name patterns used to describe the request are passed to <i>XkbListComponents </i> using an XkbComponentNamesRec structure. This structure has no special allocation constraints or interrelationships with other structures; allocate and free this structure using standard <i>malloc </i> and <i>free </i> calls or their equivalent: </p>
<pre> typedef struct _XkbComponentNames {
 char * keymap; /* keymap names */
 char * keycodes; /* keycode names */
 char * types; /* type names */
 char * compat; /* compatibility map names */
 char * symbols; /* symbol names */
 char * geometry; /* geometry names */
 } XkbComponentNamesRec, *XkbComponentNamesPtr;</pre>
<p><i>XkbListComponents </i> returns a pointer to an XkbComponentListRec: </p>
<pre> typedef struct _XkbComponentList {
 int num_keymaps; /* number of entries in keymap */
 int num_keycodes; /* number of entries in keycodes */
 int num_types; /* number of entries in types */
 int num_compat; /* number of entries in compat */
 int num_symbols; /* number of entries in symbols */
 int num_geometry; /* number of entries in geometry;
 XkbComponentNamePtr keymap; /* keymap names */
 XkbComponentNamePtr keycodes; /* keycode names */
 XkbComponentNamePtr types; /* type names */
 XkbComponentNamePtr compat; /* compatibility map names */
 XkbComponentNamePtr symbols; /* symbol names */
 XkbComponentNamePtr geometry; /* geometry names */
 } XkbComponentListRec, *XkbComponentListPtr;
 
 typedef struct _XkbComponentName {
 unsigned short flags; /* hints regarding component name */
 char * name; /* name of component */
 } XkbComponentNameRec, *XkbComponentNamePtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreecomponentlist/">XkbFreeComponentList</a></code>(3)</p>
<h2>Notes</h2>
<p>Note that the structure used to specify patterns on input is an XkbComponentNamesRec, and that used to hold the individual component names upon return is an XkbComponentNameRec (no trailing `s&#8217; in Name).</p>
