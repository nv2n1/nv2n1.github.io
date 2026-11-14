---
title: "alembic(1)"
name: "alembic"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alembic/"
description: "alembic – manual page for alembic 0.8.7"
---

<h2>NAME</h2>
<p> alembic &#8211; manual page for alembic 0.8.7</p>
<h2>DESCRIPTION</h2>
<p> usage: <code>-c</code> [-h] [-c CONFIG] [-n NAME] [-x X] [&#8211;raiseerr]</p>
<dl>
<dt>
<dd> {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade} &#8230;</dl>
<h3>positional arguments:</h3>
<dl>
<dt>
<dd> {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade}</p>
<dt>branches</p>
<dd> Show current branch points</p>
<dt>current</p>
<dd> Display the current revision for a database.</p>
<dt>downgrade</p>
<dd> Revert to a previous version.</p>
<dt>edit</p>
<dd> Edit revision script(s) using $EDITOR</p>
<dt>heads</p>
<dd> Show current available heads in the script directory</p>
<dt>history</p>
<dd> List changeset scripts in chronological order.</p>
<dt>init</p>
<dd> Initialize a new scripts directory.</p>
<dt>list_templates</p>
<dd> List available templates</p>
<dt>merge</p>
<dd> Merge two revisions together. Creates a new migration file. .. versionadded:: 0.7.0 .. seealso:: :ref:`branches`</p>
<dt>revision</p>
<dd> Create a new revision file.</p>
<dt>show</p>
<dd> Show the revision(s) denoted by the given symbol.</p>
<dt>stamp</p>
<dd> &#8216;stamp&#8217; the revision table with the given revision; don&#8217;t run any migrations.</p>
<dt>upgrade</p>
<dd> Upgrade to a later version.</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-c</code> CONFIG, <code>&#8211;config</code> CONFIG</p>
<dd> Alternate config file</p>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</p>
<dd> Name of section in .ini file to use for Alembic config</p>
<dt><code>-x</code> X</p>
<dd> Additional arguments consumed by custom env.py scripts, e.g. <code>-x</code> setting1=somesetting <code>-x</code> setting2=somesetting</p>
<dt><code>&#8211;raiseerr</code></p>
<dd> Raise a full stack trace on error </p>
</dl>
<h2>Index</h2>
