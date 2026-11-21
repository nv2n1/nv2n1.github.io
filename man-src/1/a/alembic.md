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
</dt><dd> {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade} &#8230;</dd></dl>
<h3>positional arguments:</h3>
<dl>
<dt>
</dt><dd> {branches,current,downgrade,edit,heads,history,init,list_templates,merge,revision,show,stamp,upgrade}</dd>
<dt>branches</dt>
<dd> Show current branch points</dd>
<dt>current</dt>
<dd> Display the current revision for a database.</dd>
<dt>downgrade</dt>
<dd> Revert to a previous version.</dd>
<dt>edit</dt>
<dd> Edit revision script(s) using $EDITOR</dd>
<dt>heads</dt>
<dd> Show current available heads in the script directory</dd>
<dt>history</dt>
<dd> List changeset scripts in chronological order.</dd>
<dt>init</dt>
<dd> Initialize a new scripts directory.</dd>
<dt>list_templates</dt>
<dd> List available templates</dd>
<dt>merge</dt>
<dd> Merge two revisions together. Creates a new migration file. .. versionadded:: 0.7.0 .. seealso:: :ref:`branches`</dd>
<dt>revision</dt>
<dd> Create a new revision file.</dd>
<dt>show</dt>
<dd> Show the revision(s) denoted by the given symbol.</dd>
<dt>stamp</dt>
<dd> &#8216;stamp&#8217; the revision table with the given revision; don&#8217;t run any migrations.</dd>
<dt>upgrade</dt>
<dd> Upgrade to a later version.</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-c</code> CONFIG, <code>&#8211;config</code> CONFIG</dt>
<dd> Alternate config file</dd>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</dt>
<dd> Name of section in .ini file to use for Alembic config</dd>
<dt><code>-x</code> X</dt>
<dd> Additional arguments consumed by custom env.py scripts, e.g. <code>-x</code> setting1=somesetting <code>-x</code> setting2=somesetting</dd>
<dt><code>&#8211;raiseerr</code></dt>
<dd> Raise a full stack trace on error </dd>
</dl>
