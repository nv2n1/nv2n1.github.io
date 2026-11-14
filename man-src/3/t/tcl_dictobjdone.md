---
title: "tcl_dictobjdone(3)"
name: "tcl_dictobjdone"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_dictobjdone/"
description: "Tcl_NewDictObj, Tcl_DictObjPut, Tcl_DictObjGet, Tcl_DictObjRemove, Tcl_DictObjSize, Tcl_DictObjFirst, Tcl_DictObjNext, Tcl_DictObjDone, Tcl_DictObjPutKeyList, Tcl_DictObjRemoveKeyList – manipulate ..."
---

<p>Tcl_NewDictObj, Tcl_DictObjPut, Tcl_DictObjGet, Tcl_DictObjRemove, Tcl_DictObjSize, Tcl_DictObjFirst, Tcl_DictObjNext, Tcl_DictObjDone, Tcl_DictObjPutKeyList, Tcl_DictObjRemoveKeyList &#8211; manipulate Tcl objects as dictionaries </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewDictObj</code>()
int
<code>Tcl_DictObjGet</code>(<i>interp, dictPtr, keyPtr, valuePtrPtr</i>)
int
<code>Tcl_DictObjPut</code>(<i>interp, dictPtr, keyPtr, valuePtr</i>)
int
<code>Tcl_DictObjRemove</code>(<i>interp, dictPtr, keyPtr</i>)
int
<code>Tcl_DictObjSize</code>(<i>interp, dictPtr, sizePtr</i>)
int
<code>Tcl_DictObjFirst</code>(<i>interp, dictPtr, searchPtr,
 keyPtrPtr, valuePtrPtr, donePtr</i>)
void
<code>Tcl_DictObjNext</code>(<i>searchPtr, keyPtrPtr, valuePtrPtr, donePtr</i>)
void
<code>Tcl_DictObjDone</code>(<i>searchPtr</i>)
int
<code>Tcl_DictObjPutKeyList</code>(<i>interp, dictPtr, keyc, keyv, valuePtr</i>)
int
<code>Tcl_DictObjRemoveKeyList</code>(<i>interp, dictPtr, keyc, keyv</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) If an error occurs while converting an object to be a dictionary object, an error message is left in the interpreter&#8217;s result object unless <i>interp</i> is NULL.</p>
<dd>Tcl_Obj <i>*dictPtr</i> (in/out) Points to the dictionary object to be manipulated. If <i>dictPtr</i> does not already point to a dictionary object, an attempt will be made to convert it to one.</p>
<dd>Tcl_Obj <i>*keyPtr</i> (in) Points to the key for the key/value pair being manipulated within the dictionary object.</p>
<dd>Tcl_Obj <i>**keyPtrPtr</i> (out) Points to a variable that will have the key from a key/value pair placed within it. May be NULL to indicate that the caller is not interested in the key.</p>
<dd>Tcl_Obj <i>*valuePtr</i> (in) Points to the value for the key/value pair being manipulate within the dictionary object (or sub-object, in the case of <code>Tcl_DictObjPutKeyList</code>.)</p>
<dd>Tcl_Obj <i>**valuePtrPtr</i> (out) Points to a variable that will have the value from a key/value pair placed within it. For <code>Tcl_DictObjFirst</code> and <code>Tcl_DictObjNext</code>, this may be NULL to indicate that the caller is not interested in the value.</p>
<dd>int <i>*sizePtr</i> (out) Points to a variable that will have the number of key/value pairs contained within the dictionary placed within it.</p>
<dd>Tcl_DictSearch <i>*searchPtr</i> (in/out) Pointer to record to use to keep track of progress in enumerating all key/value pairs in a dictionary. The contents of the record will be initialized by the call to <code>Tcl_DictObjFirst</code>. If the enumerating is to be terminated before all values in the dictionary have been returned, the search record <i>must</i> be passed to <code>Tcl_DictObjDone</code> to enable the internal locks to be released.</p>
<dd>int <i>*donePtr</i> (out) Points to a variable that will have a non-zero value written into it when the enumeration of the key/value pairs in a dictionary has completed, and a zero otherwise.</p>
<dd>int <i>keyc</i> (in) Indicates the number of keys that will be supplied in the <i>keyv</i> array.</p>
<dd>Tcl_Obj *const <i>*keyv</i> (in) Array of <i>keyc</i> pointers to objects that <code>Tcl_DictObjPutKeyList</code> and <code>Tcl_DictObjRemoveKeyList</code> will use to locate the key/value pair to manipulate within the sub-dictionaries of the main dictionary object passed to them. </p>
</dl>
<h2>Description</h2>
<p>Tcl dictionary objects have an internal representation that supports efficient mapping from keys to values and which guarantees that the particular ordering of keys within the dictionary remains the same modulo any keys being deleted (which removes them from the order) or added (which adds them to the end of the order). If reinterpreted as a list, the values at the even-valued indices in the list will be the keys of the dictionary, and each will be followed (in the odd-valued index) by the value associated with that key. </p>
<p> The procedures described in this man page are used to create, modify, index, and iterate over dictionary objects from C code. </p>
<p> <code>Tcl_NewDictObj</code> creates a new, empty dictionary object. The string representation of the object will be invalid, and the reference count of the object will be zero. </p>
<p> <code>Tcl_DictObjGet</code> looks up the given key within the given dictionary and writes a pointer to the value associated with that key into the variable pointed to by <i>valuePtrPtr</i>, or a NULL if the key has no mapping within the dictionary. The result of this procedure is <code>TCL_OK</code>, or <code>TCL_ERROR</code> if the <i>dictPtr</i> cannot be converted to a dictionary. </p>
<p> <code>Tcl_DictObjPut</code> updates the given dictionary so that the given key maps to the given value; any key may exist at most once in any particular dictionary. The dictionary must not be shared, but the key and value may be. This procedure may increase the reference count of both key and value if it proves necessary to store them. Neither key nor value should be NULL. The result of this procedure is <code>TCL_OK</code>, or <code>TCL_ERROR</code> if the <i>dictPtr</i> cannot be converted to a dictionary. </p>
<p> <code>Tcl_DictObjRemove</code> updates the given dictionary so that the given key has no mapping to any value. The dictionary must not be shared, but the key may be. The key actually stored in the dictionary will have its reference count decremented if it was present. It is not an error if the key did not previously exist. The result of this procedure is <code>TCL_OK</code>, or <code>TCL_ERROR</code> if the <i>dictPtr</i> cannot be converted to a dictionary. </p>
<p> <code>Tcl_DictObjSize</code> updates the given variable with the number of key/value pairs currently in the given dictionary. The result of this procedure is <code>TCL_OK</code>, or <code>TCL_ERROR</code> if the <i>dictPtr</i> cannot be converted to a dictionary. </p>
<p> <code>Tcl_DictObjFirst</code> commences an iteration across all the key/value pairs in the given dictionary, placing the key and value in the variables pointed to by the <i>keyPtrPtr</i> and <i>valuePtrPtr</i> arguments (which may be NULL to indicate that the caller is uninterested in they key or variable respectively.) The next key/value pair in the dictionary may be retrieved with <code>Tcl_DictObjNext</code>. Concurrent updates of the dictionary&#8217;s internal representation will not modify the iteration processing unless the dictionary is unshared, when this will trigger premature termination of the iteration instead (which Tcl scripts cannot trigger via the <code>dict</code> command.) The <i>searchPtr</i> argument points to a piece of context that is used to identify which particular iteration is being performed, and is initialized by the call to <code>Tcl_DictObjFirst</code>. The <i>donePtr</i> argument points to a variable that is updated to be zero of there are further key/value pairs to be iterated over, or non-zero if the iteration is complete. The order of iteration is implementation-defined. If the <i>dictPtr</i> argument cannot be converted to a dictionary, <code>Tcl_DictObjFirst</code> returns <code>TCL_ERROR</code> and the iteration is not commenced, and otherwise it returns <code>TCL_OK</code>. </p>
<p> When <code>Tcl_DictObjFirst</code> is called upon a dictionary, a lock is placed on the dictionary to enable that dictionary to be iterated over safely without regard for whether the dictionary is modified during the iteration. Because of this, once the iteration over a dictionary&#8217;s keys has finished (whether because all values have been iterated over as indicated by the variable indicated by the <i>donePtr</i> argument being set to one, or because no further values are required) the <code>Tcl_DictObjDone</code> function must be called with the same <i>searchPtr</i> as was passed to <code>Tcl_DictObjFirst</code> so that the internal locks can be released. Once a particular <i>searchPtr</i> is passed to <code>Tcl_DictObjDone</code>, passing it to <code>Tcl_DictObjNext</code> (without first initializing it with <code>Tcl_DictObjFirst</code>) will result in no values being produced and the variable pointed to by <i>donePtr</i> being set to one. It is safe to call <code>Tcl_DictObjDone</code> multiple times on the same <i>searchPtr</i> for each call to <code>Tcl_DictObjFirst</code>. </p>
<p> The procedures <code>Tcl_DictObjPutKeyList</code> and <code>Tcl_DictObjRemoveKeyList</code> are the close analogues of <code>Tcl_DictObjPut</code> and <code>Tcl_DictObjRemove</code> respectively, except that instead of working with a single dictionary, they are designed to operate on a nested tree of dictionaries, with inner dictionaries stored as values inside outer dictionaries. The <i>keyc</i> and <i>keyv</i> arguments specify a list of keys (with outermost keys first) that acts as a path to the key/value pair to be affected. Note that there is no corresponding operation for reading a value for a path as this is easy to construct from repeated use of <code>Tcl_DictObjGet</code>. With <code>Tcl_DictObjPutKeyList</code>, nested dictionaries are created for non-terminal keys where they do not already exist. With <code>Tcl_DictObjRemoveKeyList</code>, all non-terminal keys must exist and have dictionaries as their values.</p>
<h2>Example</h2>
<p>Using the dictionary iteration interface to search determine if there is a key that maps to itself: </p>
<dl COMPACT>
<dd>
<pre>Tcl_DictSearch search;
Tcl_Obj *key, *value;
int done;
/*
 * Assume interp and objPtr are parameters. This is the
 * idiomatic way to start an iteration over the dictionary; it
 * sets a lock on the internal representation that ensures that
 * there are no concurrent modification issues when normal
 * reference count management is also used. The lock is
 * released automatically when the loop is finished, but must
 * be released manually when an exceptional exit from the loop
 * is performed. However it is safe to try to release the lock
 * even if we've finished iterating over the loop.
 */
if (<code>Tcl_DictObjFirst</code>(interp, objPtr, &amp;search,
 &amp;key, &amp;value, &amp;done) != TCL_OK) {
 return TCL_ERROR;
}
for (; !done ; <code>Tcl_DictObjNext</code>(&amp;search, &amp;key, &amp;value, &amp;done)) {
 /*
 * Note that strcmp() is not a good way of comparing
 * objects and is just used here for demonstration
 * purposes.
 */
 if (!strcmp(Tcl_GetString(key), Tcl_GetString(value))) {
 break;
 }
}
<code>Tcl_DictObjDone</code>(&amp;search);
Tcl_SetObjResult(interp, Tcl_NewBooleanObj(!done));
return TCL_OK;</pre>
</dl>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_DecrRefCount, Tcl_IncrRefCount, Tcl_InitObjHashTable</p>
<h2>Keywords</h2>
<p>dict, dict object, dictionary, dictionary object, hash table, iteration, object</p>
