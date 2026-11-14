---
title: "perldbmfilter(1)"
name: "perldbmfilter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldbmfilter/"
description: "perldbmfilter – Perl DBM Filters"
---

<h2 class="name">NAME</h2>
<p> perldbmfilter &#8211; Perl DBM Filters </p>
<h2>SYNOPSIS</h2>
<pre><code>
$db = tie % hash, 'DBM', ... $old_filter = $db-&gt;filter_store_key(sub{...});
$old_filter = $db-&gt;filter_store_value(sub{...});
$old_filter = $db-&gt;filter_fetch_key(sub{...});
$old_filter = $db-&gt;filter_fetch_value(sub{...});
</code></pre>
<h2>DESCRIPTION</h2>
<p> The four <tt>&quot;filter_*&quot;</tt> methods shown above are available in all the <font SIZE="-1">DBM</font> modules that ship with Perl, namely DB_File, GDBM_File, NDBM_File, ODBM_File and SDBM_File. </p>
<p> Each of the methods works identically, and is used to install (or uninstall) a single <font SIZE="-1">DBM</font> Filter. The only difference between them is the place that the filter is installed. </p>
<p> To summarise:</p>
<dl>
<dt><code>filter_store_key</code></p>
<dd> If a filter has been installed with this method, it will be invoked every time you write a key to a <font SIZE="-1">DBM</font> database.</p>
<dt><code>filter_store_value</code></p>
<dd> If a filter has been installed with this method, it will be invoked every time you write a value to a <font SIZE="-1">DBM</font> database.</p>
<dt><code>filter_fetch_key</code></p>
<dd> If a filter has been installed with this method, it will be invoked every time you read a key from a <font SIZE="-1">DBM</font> database.</p>
<dt><code>filter_fetch_value</code></p>
<dd> If a filter has been installed with this method, it will be invoked every time you read a value from a <font SIZE="-1">DBM</font> database.</dl>
<p> You can use any combination of the methods from none to all four. </p>
<p> All filter methods return the existing filter, if present, or <tt>&quot;undef&quot;</tt> if not. </p>
<p> To delete a filter pass <tt>&quot;undef&quot;</tt> to it.</p>
<h3>The Filter</h3>
<p> When each filter is called by Perl, a local copy of <tt>$_</tt> will contain the key or value to be filtered. Filtering is achieved by modifying the contents of <tt>$_</tt>. The return code from the filter is ignored.</p>
<h3>An Example: the <font SIZE="-1">NULL</font> termination problem.</h3>
<p> <font SIZE="-1">DBM</font> Filters are useful for a class of problems where you <i>always</i> want to make the same transformation to all keys, all values or both. </p>
<p> For example, consider the following scenario. You have a <font SIZE="-1">DBM</font> database that you need to share with a third-party C application. The C application assumes that <i>all</i> keys and values are <font SIZE="-1">NULL</font> terminated. Unfortunately when Perl writes to <font SIZE="-1">DBM</font> databases it doesn&#8217;t use <font SIZE="-1">NULL</font> termination, so your Perl application will have to manage <font SIZE="-1">NULL</font> termination itself. When you write to the database you will have to use something like this: </p>
<pre>
    $hash{&quot;$key
