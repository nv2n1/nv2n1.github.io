---
title: "keylist(3)"
name: "keylist"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keylist/"
description: "TclX_NewKeyedListObj, TclX_KeyedListGet, TclX_KeyedListSet, TclX_KeyedListDelete, TclX_KeyedListGetKeys – Keyed list management routines."
---

<p>TclX_NewKeyedListObj, TclX_KeyedListGet, TclX_KeyedListSet, TclX_KeyedListDelete, TclX_KeyedListGetKeys &#8211; Keyed list management routines. </p>
<h2>Synopsis</h2>
<pre>#include &lt;tclExtend.h&gt;
Tcl_Obj *
TclX_NewKeyedListObj (void);
int
TclX_KeyedListGet (Tcl_Interp *interp,
 Tcl_Obj *keylPtr,
 char *key,
 Tcl_Obj **valuePtrPtr);
int
TclX_KeyedListSet (Tcl_Interp *interp,
 Tcl_Obj *keylPtr,
 char *key,
 Tcl_Obj *valuePtr);
int
TclX_KeyedListDelete (Tcl_Interp *interp,
 Tcl_Obj *keylPtr,
 char *key);
int
TclX_KeyedListGetKeys (Tcl_Interp *interp,
 Tcl_Obj *keylPtr,
 char *key,
 Tcl_Obj **listObjPtrPtr);</pre>
<h2>Description</h2>
<p>These routines perform operations on keyed lists. See the <i>Extended Tcl</i> man page for a description of keyed lists.</p>
<h3>TclX_NewKeyedListObj</h3>
<p>Create and initialize a new keyed list object. </p>
<p> Returns:</p>
<dl COMPACT>
<dd>A pointer to the object.</dl>
<h3>TclX_KeyedListGet</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>Retrieve a key value from a keyed list. </p>
<p> Parameters:</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; Error message will be return in result if there is an error.<br />
 <code>o </code><i>keylPtr</i> &#8211; Keyed list object to get key from.<br />
 <code>o </code><i>key</i> &#8211; The name of the key to extract. Will recusively process sub-keys seperated by `.&#8217;.<br />
 <code>o </code><i>valueObjPtrPtr</i> &#8211; If the key is found, a pointer to the key object<br />
&nbsp;<wbr>is returned here.&nbsp;<wbr>&nbsp;<wbr>NULL is returned if the key is not present.
</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>o TCL_OK</code> &#8211; If the key value was returned.<br />
 <code>o TCL_BREAK</code> &#8211; If the key was not found.<br />
 <code>o TCL_ERROR</code> &#8211; If an error occured.
</dl>
<h3>TclX_KeyedListSet</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>Set a key value in keyed list object. </p>
<p> Parameters:</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; Error message will be return in result object.<br />
 <code>o </code><i>keylPtr</i> &#8211; Keyed list object to update.<br />
 <code>o </code><i>key</i> &#8211; The name of the key to extract. Will recusively process sub-key seperated by `.&#8217;.<br />
 <code>o </code><i>valueObjPtr</i> &#8211; The value to set for the key.
</dl>
<p> Returns:</p>
<dl COMPACT>
<dd>&nbsp;<wbr>&nbsp;<wbr>TCL_OK or TCL_ERROR.</dl>
<h3>TclX_KeyedListDelete</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>Delete a key value from keyed list. </p>
<p> Parameters:</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; Error message will be return in result if there is an error.<br />
 <code>o </code><i>keylPtr</i> &#8211; Keyed list object to update.<br />
 <code>o </code><i>key</i> &#8211; The name of the key to extract. Will recusively process sub-key seperated by `.&#8217;.
</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>o TCL_OK</code> &#8211; If the key was deleted.<br />
 <code>o TCL_BREAK</code> &#8211; If the key was not found.<br />
 <code>o TCL_ERROR</code> &#8211; If an error occured.
</dl>
<h3>TclX_KeyedListGetKeys</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>Retrieve a list of keyed list keys. </p>
<p> Parameters:</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; Error message will be return in result if there is an error.<br />
 <code>o </code><i>keylPtr</i> &#8211; Keyed list object to get key from.<br />
 <code>o </code><i>key</i> &#8211; The name of the key to get the sub keys for. NULL or empty to retrieve all top level keys.<br />
 <code>o </code><i>listObjPtrPtr</i> &#8211; List object is returned here with key as values.</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>o TCL_OK</code> &#8211; If the zero or more key where returned.<br />
 <code>o TCL_BREAK</code> &#8211; If the key was not found.<br />
 <code>o TCL_ERROR</code> &#8211; If an error occured.
</dl>
