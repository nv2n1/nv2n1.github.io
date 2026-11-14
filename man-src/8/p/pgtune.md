---
title: "pgtune(8)"
name: "pgtune"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pgtune/"
---

pgtune - PostgreSQL Config Tuner

<h2>Synopsis</h2>

<pre>pgtune -i $PGDATA/postgresql.conf -o $PGDATA/postgresql.conf.pgtune</pre>

<h2>Description</h2>

Pgtune takes the wimpy default postgresql.conf and expands the database server to be as powerful as the hardware it's being deployed on. 

 pgtune works by taking an existing postgresql.conf file as an input, making changes to it based on the amount of RAM in your server and suggested workload, and output a new file.

<h2>Options</h2>

-i, --input-config
<dl><dd>Specifies the current postgresql.conf file.</dl>
 

 -o, --input-config
<dl><dd>Specifies the file name for the new postgresql.conf file.</dl>
 

 -M, --memory
<dl><dd>Use this parameter to specify total system memory. If not specified, pgtune will attempt to detect memory size.</dl>
 

 -T, --type
<dl><dd>Specifies database type. Valid options are: DW, OLTP, Web, Mixed, Desktop</dl>
 

 -c, --connections
<dl><dd>Specifies number of maximum connections expected. If not specified, it depends on database type.</dl>
 

 -D, --debug
<dl><dd>Enables debugging mode.</dl>
 

 -S, --settings
<dl><dd>Directory where settings data files are located at. Defaults to the directory where the script is being run from. The RPM package includes a patch to use the correct location these files were installed into.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-postgres/">postgres</a>(1)

<h2>Authors</h2>

This man page is written by Miroslav Suchy for Fedora.
