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
</dt><dd> Licence: simplified <font SIZE="-1">BSD</font>
</dd><dt>&bull;
</dt><dd> All data is maintained in <font SIZE="-1">RAM</font>
</dd><dt>&bull;
</dt><dd> Data persistence is implemented using Write Ahead Log and snapshotting
</dd><dt>&bull;
</dt><dd> Supports asynchronous replication and hot standby
</dd><dt>&bull;
</dt><dd> Uses coroutines and asynchronous I/O to implement high-performance lock-free access to data
</dd><dt>&bull;
</dt><dd> Available on Linux, FreeBSD, Mac <font SIZE="-1">OS X</font>
</dd><dt>&bull;
</dt><dd> Stored procedures in Lua are supported.</dd></dl>

<h3>Data model</h3>

 The basic atom of storage in Tarantool is called tuple. A tuple can have arbitrary number of fields. The first field or fields in the tuple are always the identifying unique key. Tuples form spaces. It is possible to search tuples in spaces using the primary or secondary keys. It is possible to change, as well as add or remove fields.

<h2>Command-line options</h2>

<dl>
<dt>-h, --help
</dt><dd> Displays helpscreen and exits.
</dd><dt>-V, --version
</dt><dd> Prints program version and exits. 
</dd></dl>
