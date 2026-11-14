---
title: "pg_test_fsync(1)"
name: "pg_test_fsync"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_test_fsync/"
description: "pg_test_fsync – determine fastest wal_sync_method for PostgreSQL"
---

<h2 class="name">NAME</h2>
<p> pg_test_fsync &#8211; determine fastest wal_sync_method for PostgreSQL </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_test_fsync</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_test_fsync is intended to give you a reasonable idea of what the fastest wal_sync_method is on your specific system, as well as supplying diagnostic information in the event of an identified I/O problem. However, differences shown by pg_test_fsync might not make any difference in real database throughput, especially since many database servers are not speed-limited by their transaction logs.</p>
<h2>OPTIONS</h2>
<p> pg_test_fsync accepts the following command-line options: </p>
<p> <code>-f</code>, <code>&#8211;filename</code></p>
<dl>
<dt>
<dd> Specifies the file name to write test data in. This file should be in the same file system that the pg_xlog directory is or will be placed in. (pg_xlog contains the WAL files.) The default is pg_test_fsync.out in the current directory.</dl>
<p> <code>-s</code>, <code>&#8211;secs-per-test</code></p>
<dl>
<dt>
<dd> Specifies the number of seconds for each test. The more time per test, the greater the test&#8217;s accuracy, but the longer it takes to run. The default is 2 seconds, which allows the program to complete in about 30 seconds.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the pg_test_fsync version and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_test_fsync command line arguments, and exit.</dl>
<h2>AUTHOR</h2>
<p> Bruce Momjian &lt;bruce [at] momjian.us&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1) </p>
<h2>Index</h2>
