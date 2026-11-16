---
title: "gm-delegations-converter(8)"
name: "gm-delegations-converter"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gm-delegations-converter/"
description: "gm-delegations-converter – converts delegations database between supported formats"
---

<p>gm-delegations-converter &#8211; converts delegations database between supported formats </p>
<h2>Description</h2>
<p><code>gm-delegations-converter</code> converts delegations backend database storing information about accepted delegated credentials between supported formats. So far supported formats are Berkeley DB and SQLite. Converted database is stored in same location as the original one. Hence original database is overwritten and ready to be used immediately. </p>
<h2>Synopsis</h2>
<p>gm-jobs [OPTION&#8230;] </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show help for available options</dd>
<dt><code>-c, &#8211;conffile=file</code></dt>
<dd>use specified configuration file</dd>
<dt><code>-d, &#8211;controldir=dir</code></dt>
<dd>read information from specified control directory</dd>
<dt><code>-i, &#8211;input=database format</code></dt>
<dd>specifies format of original database. By default the value from configuration file is used. The possible values are bdb (Berkeley DB) and sqlite (SQLite).</dd>
<dt><code>-o, &#8211;output=database format</code></dt>
<dd>specifies format to convert database into. By default it is opposite to one specified in configuration file. </dd>
</dl>
<h2>Author</h2>
<p>Aleksandr Konstantinov &lt;akonstantinov at dot yahoo dot com&gt;</p>
