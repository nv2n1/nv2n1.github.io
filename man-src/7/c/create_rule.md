---
title: "create_rule(7)"
name: "create_rule"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_rule/"
description: "CREATE RULE – define a new rewrite rule"
---

<p>CREATE RULE &#8211; define a new rewrite rule </p>
<h2>Synopsis</h2>
<pre>CREATE [ OR REPLACE ] RULE <i>name</i> AS ON <i>event</i>
 TO <i>table</i> [ WHERE <i>condition</i> ]
 DO [ ALSO | INSTEAD ] { NOTHING | <i>command</i> | ( <i>command</i> ; <i>command</i> ... ) }</pre>
<h2>Description</h2>
<p><code>CREATE RULE</code> defines a new rule applying to a specified table or view. <code>CREATE OR REPLACE RULE</code> will either create a new rule, or replace an existing rule of the same name for the same table. </p>
<p> The PostgreSQL rule system allows one to define an alternative action to be performed on insertions, updates, or deletions in database tables. Roughly speaking, a rule causes additional commands to be executed when a given command on a given table is executed. Alternatively, an INSTEAD rule can replace a given command by another, or cause a command not to be executed at all. Rules are used to implement table views as well. It is important to realize that a rule is really a command transformation mechanism, or command macro. The transformation happens before the execution of the commands starts. If you actually want an operation that fires independently for each physical row, you probably want to use a trigger, not a rule. More information about the rules system is in in the documentation. </p>
<p> Presently, ON SELECT rules must be unconditional INSTEAD rules and must have actions that consist of a single <code>SELECT</code> command. Thus, an ON SELECT rule effectively turns the table into a view, whose visible contents are the rows returned by the rule&#8217;s <code>SELECT</code> command rather than whatever had been stored in the table (if anything). It is considered better style to write a <code>CREATE VIEW</code> command than to create a real table and define an ON SELECT rule for it. </p>
<p> You can create the illusion of an updatable view by defining ON INSERT, ON UPDATE, and ON DELETE rules (or any subset of those that&#8217;s sufficient for your purposes) to replace update actions on the view with appropriate updates on other tables. If you want to support <code>INSERT RETURNING</code> and so on, then be sure to put a suitable RETURNING clause into each of these rules. </p>
<p> There is a catch if you try to use conditional rules for view updates: there <code>must</code> be an unconditional INSTEAD rule for each action you wish to allow on the view. If the rule is conditional, or is not INSTEAD, then the system will still reject attempts to perform the update action, because it thinks it might end up trying to perform the action on the dummy table of the view in some cases. If you want to handle all the useful cases in conditional rules, add an unconditional DO INSTEAD NOTHING rule to ensure that the system understands it will never be called on to update the dummy table. Then make the conditional rules non-INSTEAD; in the cases where they are applied, they add to the default INSTEAD NOTHING action. (This method does not currently work to support RETURNING queries, however.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of a rule to create. This must be distinct from the name of any other rule for the same table. Multiple rules on the same table and same event type are applied in alphabetical name order.</p>
<dt><i>event</i></p>
<dd>The event is one of SELECT, INSERT, UPDATE, or DELETE.</p>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of the table or view the rule applies to.</p>
<dt><i>condition</i></p>
<dd>Any SQL conditional expression (returning <code>boolean</code>). The condition expression cannot refer to any tables except NEW and OLD, and cannot contain aggregate functions.</p>
<dt><code>INSTEAD</code></p>
<dd>INSTEAD indicates that the commands should be executed <code>instead of</code> the original command.</p>
<dt><code>ALSO</code></p>
<dd>ALSO indicates that the commands should be executed <code>in addition to</code> the original command. </p>
<p> If neither ALSO nor INSTEAD is specified, ALSO is the default.</p>
<dt><i>command</i></p>
<dd>The command or commands that make up the rule action. Valid commands are <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, or <code>NOTIFY</code>.</dl>
<p> Within <i>condition</i> and <i>command</i>, the special table names NEW and OLD can be used to refer to values in the referenced table. NEW is valid in ON INSERT and ON UPDATE rules to refer to the new row being inserted or updated. OLD is valid in ON UPDATE and ON DELETE rules to refer to the existing row being updated or deleted.</p>
<h2>Notes</h2>
<p>You must be the owner of a table to create or change rules for it. </p>
<p> In a rule for INSERT, UPDATE, or DELETE on a view, you can add a RETURNING clause that emits the view&#8217;s columns. This clause will be used to compute the outputs if the rule is triggered by an <code>INSERT RETURNING</code>, <code>UPDATE RETURNING</code>, or <code>DELETE RETURNING</code> command respectively. When the rule is triggered by a command without RETURNING, the rule&#8217;s RETURNING clause will be ignored. The current implementation allows only unconditional INSTEAD rules to contain RETURNING; furthermore there can be at most one RETURNING clause among all the rules for the same event. (This ensures that there is only one candidate RETURNING clause to be used to compute the results.) RETURNING queries on the view will be rejected if there is no RETURNING clause in any available rule. </p>
<p> It is very important to take care to avoid circular rules. For example, though each of the following two rule definitions are accepted by PostgreSQL, the <code>SELECT</code> command would cause PostgreSQL to report an error because of recursive expansion of a rule: </p>
<pre>CREATE RULE &quot;_RETURN&quot; AS
 ON SELECT TO t1
 DO INSTEAD 
 SELECT * FROM t2;
CREATE RULE &quot;_RETURN&quot; AS
 ON SELECT TO t2
 DO INSTEAD 
 SELECT * FROM t1;
SELECT * FROM t1;</pre>
<p>Presently, if a rule action contains a <code>NOTIFY</code> command, the <code>NOTIFY</code> command will be executed unconditionally, that is, the <code>NOTIFY</code> will be issued even if there are not any rows that the rule should apply to. For example, in: </p>
<pre>CREATE RULE notify_me AS ON UPDATE TO mytable DO ALSO NOTIFY mytable;
UPDATE mytable SET name = 'foo' WHERE id = 42;</pre>
<p>one <code>NOTIFY</code> event will be sent during the <code>UPDATE</code>, whether or not there are any rows that match the condition id = 42. This is an implementation restriction that might be fixed in future releases.</p>
<h2>Compatibility</h2>
<p><code>CREATE RULE</code> is a PostgreSQL language extension, as is the entire query rewrite system.</p>
