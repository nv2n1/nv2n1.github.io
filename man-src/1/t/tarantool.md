---
title: "tarantool(1)"
name: "tarantool"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tarantool/"
---

<h2 class="name">NAME</h2>
 

 tarantool- a Lua application server and a NoSQL database 

<h2>SYNOPSIS</h2>

 <pre>
    tarantool [OPTIONS]
</pre>

<h2>DESCRIPTION</h2>

 Tarantool is a Lua application server and a NoSQL database. 

 Its key properties include:
<dl>
<dt>&bull;
<dd> Licence: simplified <font SIZE="-1">BSD</font>
<dt>&bull;
<dd> All data is maintained in <font SIZE="-1">RAM</font>
<dt>&bull;
<dd> Data persistence is implemented using Write Ahead Log and snapshotting
<dt>&bull;
<dd> Supports asynchronous replication and hot standby
<dt>&bull;
<dd> Uses coroutines and asynchronous I/O to implement high-performance lock-free access to data
<dt>&bull;
<dd> Available on Linux, FreeBSD, Mac <font SIZE="-1">OS X</font>
<dt>&bull;
<dd> Stored procedures in Lua are supported.</dl>

<h3>Data model</h3>

 The basic atom of storage in Tarantool is called tuple. A tuple can have arbitrary number of fields. The first field or fields in the tuple are always the identifying unique key. Tuples form spaces. It is possible to search tuples in spaces using the primary or secondary keys. It is possible to change, as well as add or remove fields.

<h2>Command-line options</h2>

<dl>
<dt>-h, --help
<dd> Displays helpscreen and exits.
<dt>-V, --version
<dd> Prints program version and exits. 

</dl>

<h2>Index</h2>


