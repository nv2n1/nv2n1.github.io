---
title: "list_intro(3)"
name: "list_intro"
section: "3"
letter: "l"
url: "/docs/linux/man/3-list_intro/"
description: "list_intro – a library providing generic list functionality and database-like list management"
---

<h2 class="name">NAME</h2>
<p> list_intro &#8211; a library providing generic list functionality and database-like list management </p>
<h2>DESCRIPTION</h2>
<p> The Grid Engine List Library provides the functionality of a generic list. This means the list functions are applicable to every list based on a number of certain basic types. List definitions are extensible on a per-program basis as long as the old fields remain in the list definition. [Note that the information here is probably outdated.]</p>
<h2>LIBRARY FUNCTIONS</h2>
<p> The list library provides the following functions. See the adoc-derived documentation for more information.</p>
<h3>LIST FUNCTIONS</h3>
<dl>
<dt><code>lCreateList</code></p>
<dd> Create a generic list</p>
<dt><code>lFreeList</code></p>
<dd> Free the memory allocated for a generic list and all its sublists</p>
<dt><code>lCopyList</code></p>
<dd> Copy a generic list with all its sublists and strings</p>
<dt><code>lAddList</code></p>
<dd> Concatenate two generic lists</p>
<dt><code>lSortList</code></p>
<dd> Sort a generic list</p>
<dt><code>lDumpList</code></p>
<dd> Dump a generic list to file</p>
<dt><code>lUndumpList</code></p>
<dd> Undump a generic list with all its data from file</p>
<dt><code>lWriteList</code></p>
<dd> Write a generic list to stdout</p>
<dt><code>lGetListName</code></p>
<dd> Return the name of a generic list</p>
<dt><code>lGetListDescr</code></p>
<dd> Return a pointer to the descriptor of a generic list</p>
<dt><code>lGetNumberOfElem</code></p>
<dd> Return the number of list elements contained in a generic list</dl>
<h3>LIST ELEMENT FUNCTIONS</h3>
<dl>
<dt><code>lCreateElem</code></p>
<dd> Create a generic list element</p>
<dt><code>lAppendElem</code></p>
<dd> Append a list element to an existing list</p>
<dt><code>lInsertElem</code></p>
<dd> Insert a list element into an existing list after a specified element</p>
<dt><code>lDechainElem</code></p>
<dd> Dechain a list element from a list, the dechained element is not freed</p>
<dt><code>lFindFirst</code></p>
<dd> Find the first list element matching specified conditions</p>
<dt><code>lFindNext</code></p>
<dd> Find the next list element starting at a certain list element matching specified conditions copy a list element partially (i.e. select specific fields that will be copied)</p>
<dt><code>lDumpElem</code></p>
<dd> Dump a list element to file</p>
<dt><code>lUndumpElem</code></p>
<dd> Undump a list element from file into memory</p>
<dt><code>lWriteElem</code></p>
<dd> Write a list element to stdout get the field position of a list element field with name &#8216;nm&#8217;</dl>
<h3>FIELD ACCESS FUNCTIONS</h3>
<dl>
<dt><code>lGetInt</code>,&nbsp;<code>Lgetulong</code>,&nbsp;<code>Lgetstring</code>,&nbsp;<code>Lgetlist</code>,&nbsp;<code>Lgetfloat</code>,&nbsp;<code>Lgetdouble</code>,&nbsp;<code>lGetChar</code>,&nbsp;<code>lGetLong</code></p>
<dd> Get the value of the specified type from a list element field; the element and the field name are delivered as arguments</p>
<dt><code>lSetInt</code>,&nbsp;<code>lSetUlong</code>,&nbsp;<code>lSetString</code>,&nbsp;<code>lSetList</code>,&nbsp;<code>lSetFloat</code>,&nbsp;<code>lSetDouble</code>,&nbsp;<code>lSetChar</code>,&nbsp;<code>lSetLong</code></p>
<dd> Set the value of the specified type in a corresponding list element field; the element, the field name and a new value are delivered as arguments</p>
<dt><code>lGetPosInt</code>,&nbsp;<code>lGetPosUlong</code>,&nbsp;<code>lGetPosString</code>,&nbsp;<code>lGetPosList</code>,&nbsp;<code>lGetPosFloat</code>,&nbsp;<code>lGetPosDouble</code>,&nbsp;<code>lGetPosChar</code>,&nbsp;<code>lGetPosLong</code></p>
<dd> Get the value of the specified type in a corresponding list element field; the element and the field position are delivered as arguments</p>
<dt><code>lSetPosInt</code>,&nbsp;<code>lSetPosUlong</code>,&nbsp;<code>lSetPosString</code>,&nbsp;<code>lSetPosList</code>,&nbsp;<code>lSetPosFloat</code>,&nbsp;<code>lSetPosDouble</code>,&nbsp;<code>lSetPosChar</code>,&nbsp;<code>lSetPosLong</code></p>
<dd> Set the value of the specified type in a corresponding list element field; the element, the field position and the new value are delivered as arguments</dl>
<h3>LIST DESCRIPTOR FUNCTIONS</h3>
<dl>
<dt><code>lInit</code></p>
<dd> Initialize the name to string conversion</p>
<dt><code>lNm2Str</code></p>
<dd> Convert an int value specifying a fieldname to its corresponding name string</p>
<dt><code>lCountDescr</code></p>
<dd> Get the number of fields of a descriptor</p>
<dt><code>lGetPosInDescr</code></p>
<dd> Get the position of the field named &#8216;nm&#8217; from the descriptor</p>
<dt><code>lDumpDescr</code></p>
<dd> Dump a list descriptor to a file</p>
<dt><code>lUndumpDescr</code></p>
<dd> Undump a list descriptor from a file to memory</p>
<dt><code>lWriteDescr</code></p>
<dd> Write a descriptor to stdout</dl>
<h3>LIST DATABASE FUNCTIONS</h3>
<dl>
<dt><code>lSelect</code></p>
<dd> Select returns a list of elements that match the specified conditions.</p>
<dt><code>lJoinSublist</code></p>
<dd> Join a specified list with one of its sublists; one can specify conditions for the list and the sublist. The joined list is returned and the original list is unchanged.</p>
<dt><code>lJoin</code></p>
<dd> Join two lists which fulfill the specified conditions to a new list that contains the enumerated fields. The joined list is returned and the original lists are unaltered.</p>
<dt><code>lWhere</code></p>
<dd> Build a lCondition data structure which is used as condition for various functions as lSelect or lJoin</p>
<dt><code>lFreeWhere</code></p>
<dd> Free a lCondition data structure</p>
<dt><code>lWriteWhere</code></p>
<dd> Write a lCondition data structure to stdout</p>
<dt><code>lWhat</code></p>
<dd> Build a lEnumeration data structure which is used to specify the fields that are contained in a newly created list element</p>
<dt><code>lFreeWhat</code></p>
<dd> Free a lEnumeration data structure</p>
<dt><code>lWriteWhat</code></p>
<dd> Write a lEnumeration data structure to stdout</p>
<dt><code>lCountWhat</code></p>
<dd> Count the number of fields in a lEnumeration data structure</dl>
<h3>DATA STRUCTURES</h3>
<p> The following essential data structures are used by the various list library functions.</p>
<dl>
<dt><code>lDescr *</code><i>descriptor</i></p>
<dd> The descriptor contains the information which fields (name, type) are contained in a list.</p>
<dt><code>lList *</code><i>list</i></p>
<dd> The lList pointer specifies a list created by lCreateList or any of the other functions generating a list. Here the name of the list, a reference to the descriptor, the number of contained list elements and a reference to the first and last list element are stored.</p>
<dt><code>lListElem *</code><i>list_element</i></p>
<dd> The lListElem pointer is returned on creation of a new list element and contains the actual data.</p>
<dt><code>lConditionI *</code><i>conditions</i></p>
<dd> The lCondition pointer is a representation of logically connected compare operations. It serves to decide whether it should be operated on a special list element.</p>
<dt><code>lEnumeration *</code><i>field_enumerations</i></p>
<dd> The lEnumeration pointer specifies which fields of a given list element shall be involved in a specified action. It is possible under certain circumstances to specify all fields or no field at all.</p>
<dt><code>lSortOrder *</code><i>sorting_order</i></p>
<dd> The lSortOrder pointer is used to specify sorting criteria for a generic list. It is possible to declare combined sorting keys.</dl>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
