---
title: "set_constraints(7)"
name: "set_constraints"
section: "7"
letter: "s"
url: "/docs/linux/man/7-set_constraints/"
description: "SET CONSTRAINTS – set constraint checking modes for the current transaction"
---

<p>SET CONSTRAINTS &#8211; set constraint checking modes for the current transaction </p>
<h2>Synopsis</h2>
<pre>SET CONSTRAINTS { ALL | <i>name</i> [, ...] } { DEFERRED | IMMEDIATE }</pre>
<h2>Description</h2>
<p><code>SET CONSTRAINTS</code> sets the behavior of constraint checking within the current transaction. IMMEDIATE constraints are checked at the end of each statement. DEFERRED constraints are not checked until transaction commit. Each constraint has its own IMMEDIATE or DEFERRED mode. </p>
<p> Upon creation, a constraint is given one of three characteristics: DEFERRABLE INITIALLY DEFERRED, DEFERRABLE INITIALLY IMMEDIATE, or NOT DEFERRABLE. The third class is always IMMEDIATE and is not affected by the <code>SET CONSTRAINTS</code> command. The first two classes start every transaction in the indicated mode, but their behavior can be changed within a transaction by <code>SET CONSTRAINTS</code>. </p>
<p> <code>SET CONSTRAINTS</code> with a list of constraint names changes the mode of just those constraints (which must all be deferrable). The current schema search path is used to find the first matching name if no schema name is specified. <code>SET CONSTRAINTS ALL</code> changes the mode of all deferrable constraints. </p>
<p> When <code>SET CONSTRAINTS</code> changes the mode of a constraint from DEFERRED to IMMEDIATE, the new mode takes effect retroactively: any outstanding data modifications that would have been checked at the end of the transaction are instead checked during the execution of the <code>SET CONSTRAINTS</code> command. If any such constraint is violated, the <code>SET CONSTRAINTS</code> fails (and does not change the constraint mode). Thus, <code>SET CONSTRAINTS</code> can be used to force checking of constraints to occur at a specific point in a transaction. </p>
<p> Currently, only foreign key constraints are affected by this setting. Check and unique constraints are always effectively not deferrable. Triggers that are declared as &#8220;constraint triggers&#8221; are also affected.</p>
<h2>Notes</h2>
<p>This command only alters the behavior of constraints within the current transaction. Thus, if you execute this command outside of a transaction block (<code>BEGIN</code>/<code>COMMIT</code> pair), it will not appear to have any effect.</p>
<h2>Compatibility</h2>
<p>This command complies with the behavior defined in the SQL standard, except for the limitation that, in PostgreSQL, it only applies to foreign-key constraints.</p>
