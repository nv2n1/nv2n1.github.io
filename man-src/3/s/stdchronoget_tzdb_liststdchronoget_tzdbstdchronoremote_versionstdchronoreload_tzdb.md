---
title: "stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_versionstdchronoreload_tzdb(3)"
name: "stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_versionstdchronoreload_tzdb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoget_tzdb_liststdchronoget_tzdbstdchronoremote_versionstdchronoreload_tzdb/"
description: "std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,std::chrono::reload_tzdb – std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,std::chrono::rel..."
---

<p>std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,std::chrono::reload_tzdb &#8211; std::chrono::get_tzdb_list,std::chrono::get_tzdb,std::chrono::remote_version,std::chrono::reload_tzdb</p>
<h2>Synopsis</h2>
<p>std::chrono::tzdb_list&amp; get_tzdb_list(); <code>(1)</code> <i>(since C++20)</i><br />
const std::chrono::tzdb&amp; get_tzdb(); <code>(2)</code> <i>(since C++20)</i><br />
std::string remote_version(); <code>(3)</code> <i>(since C++20)</i><br />
const std::chrono::tzdb&amp; reload_tzdb(); <code>(4)</code> <i>(since C++20)</i><br />
These functions provide access to the program-wide time zone database.<br />
1) Returns a reference to the global std::chrono::tzdb_list singleton. If this is the first access to the database, initialize the database. After the initialization, the database will hold a single initialized std::chrono::tzdb object. This function is thread-safe: concurrent calls to this function from multiple threads do not introduce a data race.<br />
2) Returns a reference to the first std::chrono::tzdb object held by the tzdb_list singleton. Equivalent to std::chrono::get_tzdb_list().front().<br />
3) Returns a string containing the latest remote database version.<br />
4) If remote_version() != get_tzdb().version, pushes a new tzdb object representing the remote database to the front of the tzdb_list singleton referenced by get_tzdb_list(). Otherwise there are no effects. No references, pointers or iterators are invalidated. Calling this function concurrently with get_tzdb_list().front() or get_tzdb_list().erase_after() does not introduce a data race. </p>
<h2>Exceptions</h2>
<p>1) std::runtime_error if for any reason a reference to a tzdb_list containing one or more valid tzdb cannot be returned.</p>
<h2>Return value</h2>
<p>1) A reference to the global std::chrono::tzdb_list singleton.<br />
2) std::chrono::get_tzdb_list().front().<br />
3) A string containing the latest remote database version.<br />
4) std::chrono::get_tzdb_list().front() (after any update made by this function). </p>
