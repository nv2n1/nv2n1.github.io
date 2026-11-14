---
title: "postgresql-setup(1)"
name: "postgresql-setup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postgresql-setup/"
description: "postgresql-setup – manual page for postgresql-setup 9.2.18"
---

<h2>NAME</h2>
<p> postgresql-setup &#8211; manual page for postgresql-setup 9.2.18</p>
<h2>SYNOPSIS</h2>
<p> <code>postgresql-setup</code> <i>{initdb|upgrade} </i>[<i>SERVICE_NAME</i>]</p>
<h2>DESCRIPTION</h2>
<p> Script is aimed to help sysadmin with basic database cluster administration. </p>
<p> The SERVICE_NAME is used for selection of proper unit configuration file; For more info and howto/when use this script please look at the docu file <i>/usr/share/doc/postgresql-9.2.18/README.rpm-dist</i>. The &#8216;postgresql&#8217; string is used when no SERVICE_NAME is explicitly passed.</p>
<h3>Available operation mode:</h3>
<dl>
<dt>initdb</p>
<dd> Create a new PostgreSQL database cluster. This is usually the first action you perform after PostgreSQL server installation.</p>
<dt>upgrade</p>
<dd> Upgrade PostgreSQL database cluster to be usable with new server. Use this if you upgraded your PostgreSQL server to newer major version (currently from 8.4 to 9.2).</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>PGSETUP_INITDB_OPTIONS</p>
<dd> Options carried by this variable are passed to subsequent call of `initdb` binary (see man <a href="/docs/linux/man/1-initdb/">initdb</a>(1)). This variable is used also during &#8216;upgrade&#8217; mode because the new cluster is actually re-initialized from the old one.</p>
<dt>PGSETUP_PGUPGRADE_OPTIONS</p>
<dd> Options in this variable are passed next to the subsequent call of `pg_upgrade`. For more info about possible options please look at man <a href="/docs/linux/man/1-pg_upgrade/">pg_upgrade</a>(1).</p>
<dt>PGSETUP_DEBUG</p>
<dd> Set to &#8216;1&#8217; if you want to see debugging output. </p>
</dl>
<h2>Index</h2>
