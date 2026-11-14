---
title: "lock(7)"
name: "lock"
section: "7"
letter: "l"
url: "/docs/linux/man/7-lock/"
description: "LOCK – lock a table"
---

<p>LOCK &#8211; lock a table </p>
<h2>Synopsis</h2>
<pre>LOCK [ TABLE ] [ ONLY ] <i>name</i> [, ...] [ IN <i>lockmode</i> MODE ] [ NOWAIT ]
where <i>lockmode</i> is one of:
 ACCESS SHARE | ROW SHARE | ROW EXCLUSIVE | SHARE UPDATE EXCLUSIVE
 | SHARE | SHARE ROW EXCLUSIVE | EXCLUSIVE | ACCESS EXCLUSIVE</pre>
<h2>Description</h2>
<p><code>LOCK TABLE</code> obtains a table-level lock, waiting if necessary for any conflicting locks to be released. If NOWAIT is specified, <code>LOCK TABLE</code> does not wait to acquire the desired lock: if it cannot be acquired immediately, the command is aborted and an error is emitted. Once obtained, the lock is held for the remainder of the current transaction. (There is no <code>UNLOCK TABLE</code> command; locks are always released at transaction end.) </p>
<p> When acquiring locks automatically for commands that reference tables, PostgreSQL always uses the least restrictive lock mode possible. <code>LOCK TABLE</code> provides for cases when you might need more restrictive locking. For example, suppose an application runs a transaction at the Read Committed isolation level and needs to ensure that data in a table remains stable for the duration of the transaction. To achieve this you could obtain SHARE lock mode over the table before querying. This will prevent concurrent data changes and ensure subsequent reads of the table see a stable view of committed data, because SHARE lock mode conflicts with the ROW EXCLUSIVE lock acquired by writers, and your <code>LOCK TABLE </code><i>name</i><code> IN SHARE MODE</code> statement will wait until any concurrent holders of ROW EXCLUSIVE mode locks commit or roll back. Thus, once you obtain the lock, there are no uncommitted writes outstanding; furthermore none can begin until you release the lock. </p>
<p> To achieve a similar effect when running a transaction at the Serializable isolation level, you have to execute the <code>LOCK TABLE</code> statement before executing any <code>SELECT</code> or data modification statement. A serializable transaction&#8217;s view of data will be frozen when its first <code>SELECT</code> or data modification statement begins. A <code>LOCK TABLE</code> later in the transaction will still prevent concurrent writes &#8212; but it won&#8217;t ensure that what the transaction reads corresponds to the latest committed values. </p>
<p> If a transaction of this sort is going to change the data in the table, then it should use SHARE ROW EXCLUSIVE lock mode instead of SHARE mode. This ensures that only one transaction of this type runs at a time. Without this, a deadlock is possible: two transactions might both acquire SHARE mode, and then be unable to also acquire ROW EXCLUSIVE mode to actually perform their updates. (Note that a transaction&#8217;s own locks never conflict, so a transaction can acquire ROW EXCLUSIVE mode when it holds SHARE mode &#8212; but not if anyone else holds SHARE mode.) To avoid deadlocks, make sure all transactions acquire locks on the same objects in the same order, and if multiple lock modes are involved for a single object, then transactions should always acquire the most restrictive mode first. </p>
<p> More information about the lock modes and locking strategies can be found in in the documentation.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing table to lock. If ONLY is specified, only that table is locked. If ONLY is not specified, the table and all its descendant tables (if any) are locked. </p>
<p> The command LOCK TABLE a, b; is equivalent to LOCK TABLE a; LOCK TABLE b;. The tables are locked one-by-one in the order specified in the <code>LOCK TABLE</code> command.</p>
<dt><i>lockmode</i></p>
<dd>The lock mode specifies which locks this lock conflicts with. Lock modes are described in in the documentation. </p>
<p> If no lock mode is specified, then ACCESS EXCLUSIVE, the most restrictive mode, is used.</p>
<dt><code>NOWAIT</code></p>
<dd>Specifies that <code>LOCK TABLE</code> should not wait for any conflicting locks to be released: if the specified lock(s) cannot be acquired immediately without waiting, the transaction is aborted.</dl>
<h2>Notes</h2>
<p>LOCK TABLE &#8230; IN ACCESS SHARE MODE requires SELECT privileges on the target table. All other forms of <code>LOCK</code> require at least one of UPDATE, DELETE, or TRUNCATE privileges. </p>
<p> <code>LOCK TABLE</code> is useless outside a transaction block: the lock would remain held only to the completion of the statement. Therefore PostgreSQL reports an error if <code>LOCK</code> is used outside a transaction block. Use BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)] and COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] (or ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)]) to define a transaction block. </p>
<p> <code>LOCK TABLE</code> only deals with table-level locks, and so the mode names involving ROW are all misnomers. These mode names should generally be read as indicating the intention of the user to acquire row-level locks within the locked table. Also, ROW EXCLUSIVE mode is a sharable table lock. Keep in mind that all the lock modes have identical semantics so far as <code>LOCK TABLE</code> is concerned, differing only in the rules about which modes conflict with which. For information on how to acquire an actual row-level lock, see in the documentation and the FOR UPDATE/FOR SHARE Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] in the <code>SELECT</code> reference documentation.</p>
<h2>Examples</h2>
<p>Obtain a SHARE lock on a primary key table when going to perform inserts into a foreign key table: </p>
<pre><code>BEGIN WORK;
LOCK TABLE films IN SHARE MODE;
SELECT id FROM films
    WHERE name = 'Star Wars: Episode I - The Phantom Menace';
--Do ROLLBACK if record was not returned
    INSERT INTO films_user_comments VALUES(_id_, 'GREAT! I was waiting for it for so long!');
COMMIT WORK;</code></pre>
<p> Take a SHARE ROW EXCLUSIVE lock on a primary key table when going to perform a delete operation: </p>
<pre>BEGIN WORK;
LOCK TABLE films IN SHARE ROW EXCLUSIVE MODE;
DELETE FROM films_user_comments WHERE id IN
 (SELECT id FROM films WHERE rating &lt; 5);
DELETE FROM films WHERE rating &lt; 5;
COMMIT WORK;</pre>
<h2>Compatibility</h2>
<p>There is no <code>LOCK TABLE</code> in the SQL standard, which instead uses <code>SET TRANSACTION</code> to specify concurrency levels on transactions. PostgreSQL supports that too; see SET TRANSACTION [<code><a href="/docs/linux/man/7-set_transaction/">set_transaction</a></code>(7)] for details. </p>
<p> Except for ACCESS SHARE, ACCESS EXCLUSIVE, and SHARE UPDATE EXCLUSIVE lock modes, the PostgreSQL lock modes and the <code>LOCK TABLE</code> syntax are compatible with those present in Oracle.</p>
