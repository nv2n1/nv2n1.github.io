---
title: "libsolv(3)"
name: "libsolv"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsolv/"
description: "libsolv – package dependency solver library using a satisfiability algorithm"
---

<h2 class="name">NAME</h2>
<p> libsolv &#8211; package dependency solver library using a satisfiability algorithm </p>
<h2>DOCUMENTATION</h2>
<p> The libsolv documentation is split into multiple parts: </p>
<p> <code>libsolv-history</code></p>
<dl>
<dt>
<dd> how the libsolv library came into existence</dl>
<p> <code>libsolv-constantids</code></p>
<dl>
<dt>
<dd> fixed Ids for often used strings</dl>
<p> <code>libsolv-bindings</code></p>
<dl>
<dt>
<dd> access libsolv from perl/python/ruby</dl>
<p> <code>libsolv-pool</code></p>
<dl>
<dt>
<dd> libsolv&#8217;s pool object</dl>
<h2>POINTER VALIDITY</h2>
<p> Note that all pointers to objects that have an Id have only a limited validity period, with the exception of Repo pointers. There are only guaranteed to be valid until a new object of that type is added or an object of that type is removed. Thus pointers to Solvable objects are only valid until another solvable is created, because adding a Solvable may relocate the Pool&#8217;s Solvable array. This is also true for Pool strings, you should use solv_strdup() to create a copy of the string if you want to use it at some later time. You should use the Ids in the code and not the pointers, except for short times where you know that the pointer is safe. </p>
<p> Note also that the data lookup functions or the dataiterator also return values with limited lifetime, this is especially true for data stored in the paged data segment of solv files. This is normally data that consists of big strings like package descriptions or is not often needed like package checksums. Thus looking up a description of a solvable and then looking up the description of a different solvable or even the checksum of the same solvable may invalidate the first result. (The dataiterator supports a dataiterator_strdup() function to create a safe copy.) </p>
<p> The language bindings already deal with pointer validity, so you do not have to worry about this issue when using the bindings.</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
