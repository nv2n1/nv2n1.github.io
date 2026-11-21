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
<dt><code>lCreateList</code></dt>
<dd> Create a generic list</dd>
<dt><code>lFreeList</code></dt>
<dd> Free the memory allocated for a generic list and all its sublists</dd>
<dt><code>lCopyList</code></dt>
<dd> Copy a generic list with all its sublists and strings</dd>
<dt><code>lAddList</code></dt>
<dd> Concatenate two generic lists</dd>
<dt><code>lSortList</code></dt>
<dd> Sort a generic list</dd>
<dt><code>lDumpList</code></dt>
<dd> Dump a generic list to file</dd>
<dt><code>lUndumpList</code></dt>
<dd> Undump a generic list with all its data from file</dd>
<dt><code>lWriteList</code></dt>
<dd> Write a generic list to stdout</dd>
<dt><code>lGetListName</code></dt>
<dd> Return the name of a generic list</dd>
<dt><code>lGetListDescr</code></dt>
<dd> Return a pointer to the descriptor of a generic list</dd>
<dt><code>lGetNumberOfElem</code></dt>
<dd> Return the number of list elements contained in a generic list</dd></dl>
<h3>LIST ELEMENT FUNCTIONS</h3>
<dl>
<dt><code>lCreateElem</code></dt>
<dd> Create a generic list element</dd>
<dt><code>lAppendElem</code></dt>
<dd> Append a list element to an existing list</dd>
<dt><code>lInsertElem</code></dt>
<dd> Insert a list element into an existing list after a specified element</dd>
<dt><code>lDechainElem</code></dt>
<dd> Dechain a list element from a list, the dechained element is not freed</dd>
<dt><code>lFindFirst</code></dt>
<dd> Find the first list element matching specified conditions</dd>
<dt><code>lFindNext</code></dt>
<dd> Find the next list element starting at a certain list element matching specified conditions copy a list element partially (i.e. select specific fields that will be copied)</dd>
<dt><code>lDumpElem</code></dt>
<dd> Dump a list element to file</dd>
<dt><code>lUndumpElem</code></dt>
<dd> Undump a list element from file into memory</dd>
<dt><code>lWriteElem</code></dt>
<dd> Write a list element to stdout get the field position of a list element field with name &#8216;nm&#8217;</dd></dl>
<h3>FIELD ACCESS FUNCTIONS</h3>
<dl>
<dt><code>lGetInt</code>,&nbsp;<code>Lgetulong</code>,&nbsp;<code>Lgetstring</code>,&nbsp;<code>Lgetlist</code>,&nbsp;<code>Lgetfloat</code>,&nbsp;<code>Lgetdouble</code>,&nbsp;<code>lGetChar</code>,&nbsp;<code>lGetLong</code></dt>
<dd> Get the value of the specified type from a list element field; the element and the field name are delivered as arguments</dd>
<dt><code>lSetInt</code>,&nbsp;<code>lSetUlong</code>,&nbsp;<code>lSetString</code>,&nbsp;<code>lSetList</code>,&nbsp;<code>lSetFloat</code>,&nbsp;<code>lSetDouble</code>,&nbsp;<code>lSetChar</code>,&nbsp;<code>lSetLong</code></dt>
<dd> Set the value of the specified type in a corresponding list element field; the element, the field name and a new value are delivered as arguments</dd>
<dt><code>lGetPosInt</code>,&nbsp;<code>lGetPosUlong</code>,&nbsp;<code>lGetPosString</code>,&nbsp;<code>lGetPosList</code>,&nbsp;<code>lGetPosFloat</code>,&nbsp;<code>lGetPosDouble</code>,&nbsp;<code>lGetPosChar</code>,&nbsp;<code>lGetPosLong</code></dt>
<dd> Get the value of the specified type in a corresponding list element field; the element and the field position are delivered as arguments</dd>
<dt><code>lSetPosInt</code>,&nbsp;<code>lSetPosUlong</code>,&nbsp;<code>lSetPosString</code>,&nbsp;<code>lSetPosList</code>,&nbsp;<code>lSetPosFloat</code>,&nbsp;<code>lSetPosDouble</code>,&nbsp;<code>lSetPosChar</code>,&nbsp;<code>lSetPosLong</code></dt>
<dd> Set the value of the specified type in a corresponding list element field; the element, the field position and the new value are delivered as arguments</dd></dl>
<h3>LIST DESCRIPTOR FUNCTIONS</h3>
<dl>
<dt><code>lInit</code></dt>
<dd> Initialize the name to string conversion</dd>
<dt><code>lNm2Str</code></dt>
<dd> Convert an int value specifying a fieldname to its corresponding name string</dd>
<dt><code>lCountDescr</code></dt>
<dd> Get the number of fields of a descriptor</dd>
<dt><code>lGetPosInDescr</code></dt>
<dd> Get the position of the field named &#8216;nm&#8217; from the descriptor</dd>
<dt><code>lDumpDescr</code></dt>
<dd> Dump a list descriptor to a file</dd>
<dt><code>lUndumpDescr</code></dt>
<dd> Undump a list descriptor from a file to memory</dd>
<dt><code>lWriteDescr</code></dt>
<dd> Write a descriptor to stdout</dd></dl>
<h3>LIST DATABASE FUNCTIONS</h3>
<dl>
<dt><code>lSelect</code></dt>
<dd> Select returns a list of elements that match the specified conditions.</dd>
<dt><code>lJoinSublist</code></dt>
<dd> Join a specified list with one of its sublists; one can specify conditions for the list and the sublist. The joined list is returned and the original list is unchanged.</dd>
<dt><code>lJoin</code></dt>
<dd> Join two lists which fulfill the specified conditions to a new list that contains the enumerated fields. The joined list is returned and the original lists are unaltered.</dd>
<dt><code>lWhere</code></dt>
<dd> Build a lCondition data structure which is used as condition for various functions as lSelect or lJoin</dd>
<dt><code>lFreeWhere</code></dt>
<dd> Free a lCondition data structure</dd>
<dt><code>lWriteWhere</code></dt>
<dd> Write a lCondition data structure to stdout</dd>
<dt><code>lWhat</code></dt>
<dd> Build a lEnumeration data structure which is used to specify the fields that are contained in a newly created list element</dd>
<dt><code>lFreeWhat</code></dt>
<dd> Free a lEnumeration data structure</dd>
<dt><code>lWriteWhat</code></dt>
<dd> Write a lEnumeration data structure to stdout</dd>
<dt><code>lCountWhat</code></dt>
<dd> Count the number of fields in a lEnumeration data structure</dd></dl>
<h3>DATA STRUCTURES</h3>
<p> The following essential data structures are used by the various list library functions.</p>
<dl>
<dt><code>lDescr *</code><i>descriptor</i></dt>
<dd> The descriptor contains the information which fields (name, type) are contained in a list.</dd>
<dt><code>lList *</code><i>list</i></dt>
<dd> The lList pointer specifies a list created by lCreateList or any of the other functions generating a list. Here the name of the list, a reference to the descriptor, the number of contained list elements and a reference to the first and last list element are stored.</dd>
<dt><code>lListElem *</code><i>list_element</i></dt>
<dd> The lListElem pointer is returned on creation of a new list element and contains the actual data.</dd>
<dt><code>lConditionI *</code><i>conditions</i></dt>
<dd> The lCondition pointer is a representation of logically connected compare operations. It serves to decide whether it should be operated on a special list element.</dd>
<dt><code>lEnumeration *</code><i>field_enumerations</i></dt>
<dd> The lEnumeration pointer specifies which fields of a given list element shall be involved in a specified action. It is possible under certain circumstances to specify all fields or no field at all.</dd>
<dt><code>lSortOrder *</code><i>sorting_order</i></dt>
<dd> The lSortOrder pointer is used to specify sorting criteria for a generic list. It is possible to declare combined sorting keys.</dd></dl>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
