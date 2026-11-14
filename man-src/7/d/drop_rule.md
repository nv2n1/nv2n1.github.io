---
title: "drop_rule(7)"
name: "drop_rule"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_rule/"
description: "DROP RULE – remove a rewrite rule"
---

<p>DROP RULE &#8211; remove a rewrite rule </p>
<h2>Synopsis</h2>
<pre>DROP RULE [ IF EXISTS ] <i>name</i> ON <i>relation</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP RULE</code> drops a rewrite rule.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the rule does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of the rule to drop.</p>
<dt><i>relation</i></p>
<dd>The name (optionally schema-qualified) of the table or view that the rule applies to.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the rule.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the rule if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To drop the rewrite rule newrule: </p>
<pre>DROP RULE newrule ON mytable;</pre>
<h2>Compatibility</h2>
<p>There is no <code>DROP RULE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE RULE [<code><a href="/docs/linux/man/7-create_rule/">create_rule</a></code>(7)] </p>
