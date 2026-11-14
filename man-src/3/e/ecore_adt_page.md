---
title: "ecore_adt_page(3)"
name: "ecore_adt_page"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_adt_page/"
description: "Ecore_ADT_Page – Ecore Abstract Data Types This page briefly describes the different abstract data types that are provided by the Ecore library for general usage."
---

<p>Ecore_ADT_Page &#8211; Ecore Abstract Data Types This page briefly describes the different abstract data types that are provided by the Ecore library for general usage. </p>
<p> You need to include the <code>Ecore_Data.h </code> to use them. </p>
<h2>List</h2>
<p>A list is a simple data type where one each piece of data points to another piece of data. </p>
<p> Associated modules that describe the List ADT include: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>List Creation/Destruction Functions</code></p>
<dt>*</p>
<dd><code>List Item Adding Functions</code></p>
<dt>*</p>
<dd><code>List Item Removing Functions</code></p>
<dt>*</p>
<dd><code>List Traversal Functions</code></p>
<dt>*</p>
<dd><code>List Node Functions</code></dl>
<p> Examples involving lists include: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>list_example.c </code></dl>
<h2>Doubly Linked List</h2>
<p>A doubly linked list is like a linked list, only each piece of data can also point to the piece before it. In other words, you can traverse a doubly linked list in both directions. </p>
<p> Associated modules that describe the DList ADT include: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>Doubly Linked List Creation/Destruction Functions</code></p>
<dt>*</p>
<dd><code>Doubly Linked List Adding Functions</code></p>
<dt>*</p>
<dd><code>Doubly Linked List Removing Functions</code></dl>
<h2>Hash</h2>
<p>A hash is an abstract data type where one value is associated with another value. Instead of each element of the group being accessible using a number, each element is accessed using another object. </p>
<p> Associated modules that describe the Hash ADT include: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>Hash Creation Functions</code></p>
<dt>*</p>
<dd><code>Hash Destruction Functions</code></p>
<dt>*</p>
<dd><code>Hash Data Functions</code></dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Finish this.</dl>
