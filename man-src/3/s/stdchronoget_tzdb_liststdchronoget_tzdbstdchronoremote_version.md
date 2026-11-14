---
title: "stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_version(3)"
name: "stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_version"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_version/"
description: "std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version, – std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,"
---

<p>std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version, &#8211; std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,</p>
<h2>Synopsis</h2>
<p>std::chrono::tzdb_list&amp;&nbsp;<wbr>get_tzdb_list();&nbsp;<wbr><code>(1)</code>&nbsp;<wbr><i>(since C++20)</i><br />
const std::chrono::tzdb&amp;&nbsp;<wbr>get_tzdb();&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr><i>(since C++20)</i><br />
std::string remote_version();&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(3)</code>&nbsp;<wbr><i>(since C++20)</i><br />
const std::chrono::tzdb&amp;&nbsp;<wbr>reload_tzdb();&nbsp;<wbr>&nbsp;<wbr><code>(4)</code>&nbsp;<wbr><i>(since C++20)</i><br />
These functions provide access to the program-wide time zone database.<br />
1)&nbsp;<wbr>Returns a reference to the global std::chrono::tzdb_list singleton. If this is<br />
the first access to the database, initialize the database. After the initialization,<br />
the database will hold a single initialized std::chrono::tzdb object. This function<br />
is thread-safe: concurrent calls to this function from multiple threads do not<br />
introduce a data race.<br />
2)&nbsp;<wbr>Returns a reference to the first std::chrono::tzdb object held by the tzdb_list<br />
singleton. Equivalent to std::chrono::get_tzdb_list().front().<br />
3)&nbsp;<wbr>Returns a string containing the latest remote database version.<br />
4)&nbsp;<wbr>If remote_version()&nbsp;<wbr>!=&nbsp;<wbr>get_tzdb().version, pushes a new tzdb object representing<br />
the remote database to the front of the tzdb_list singleton referenced by<br />
get_tzdb_list(). Otherwise there are no effects. No references, pointers or<br />
iterators are invalidated. Calling this function concurrently with<br />
get_tzdb_list().front()&nbsp;<wbr>or get_tzdb_list().erase_after()&nbsp;<wbr>does not introduce a data<br />
race. </p>
<h2>Exceptions</h2>
<p>1)&nbsp;<wbr>std::runtime_error if for any reason a reference to a tzdb_list containing one or<br />
more valid tzdb cannot be returned.</p>
<h2>Return value</h2>
<p>1)&nbsp;<wbr>A reference to the global std::chrono::tzdb_list singleton.<br />
2)&nbsp;<wbr>std::chrono::get_tzdb_list().front().<br />
3)&nbsp;<wbr>A string containing the latest remote database version.<br />
4)&nbsp;<wbr>std::chrono::get_tzdb_list().front()&nbsp;<wbr>(after any update made by this function). </p>
