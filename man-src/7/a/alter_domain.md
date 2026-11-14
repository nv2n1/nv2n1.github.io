---
title: "alter_domain(7)"
name: "alter_domain"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_domain/"
description: "ALTER DOMAIN – change the definition of a domain"
---

<p>ALTER DOMAIN &#8211; change the definition of a domain </p>
<h2>Synopsis</h2>
<pre>ALTER DOMAIN <i>name</i>
 { SET DEFAULT <i>expression</i> | DROP DEFAULT }
ALTER DOMAIN <i>name</i>
 { SET | DROP } NOT NULL
ALTER DOMAIN <i>name</i>
 ADD <i>domain_constraint</i>
ALTER DOMAIN <i>name</i>
 DROP CONSTRAINT <i>constraint_name</i> [ RESTRICT | CASCADE ]
ALTER DOMAIN <i>name</i>
 OWNER TO <i>new_owner</i> 
ALTER DOMAIN <i>name</i>
 SET SCHEMA <i>new_schema</i> </pre>
<h2>Description</h2>
<p><code>ALTER DOMAIN</code> changes the definition of an existing domain. There are several sub-forms:</p>
<dl>
<dt><code>SET/DROP DEFAULT</code></p>
<dd>These forms set or remove the default value for a domain. Note that defaults only apply to subsequent <code>INSERT</code> commands; they do not affect rows already in a table using the domain.</p>
<dt><code>SET/DROP NOT NULL</code></p>
<dd>These forms change whether a domain is marked to allow NULL values or to reject NULL values. You can only SET NOT NULL when the columns using the domain contain no null values.</p>
<dt><code>ADD </code><i>domain_constraint</i></p>
<dd>This form adds a new constraint to a domain using the same syntax as CREATE DOMAIN [<code><a href="/docs/linux/man/7-create_domain/">create_domain</a></code>(7)]. This will only succeed if all columns using the domain satisfy the new constraint.</p>
<dt><code>DROP CONSTRAINT</code></p>
<dd>This form drops constraints on a domain.</p>
<dt><code>OWNER</code></p>
<dd>This form changes the owner of the domain to the specified user.</p>
<dt><code>SET SCHEMA</code></p>
<dd>This form changes the schema of the domain. Any constraints associated with the domain are moved into the new schema as well.</dl>
<p> You must own the domain to use <code>ALTER DOMAIN</code>. To change the schema of a domain, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the domain&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the domain. However, a superuser can alter ownership of any domain anyway.) </p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (possibly schema-qualified) of an existing domain to alter.</p>
<dt><i>domain_constraint</i></p>
<dd>New domain constraint for the domain.</p>
<dt><i>constraint_name</i></p>
<dd>Name of an existing constraint to drop.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the constraint.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the constraint if there are any dependent objects. This is the default behavior.</p>
<dt><i>new_owner</i></p>
<dd>The user name of the new owner of the domain.</p>
<dt><i>new_schema</i></p>
<dd>The new schema for the domain.</dl>
<h2>Notes</h2>
<p>Currently, <code>ALTER DOMAIN ADD CONSTRAINT</code> and <code>ALTER DOMAIN SET NOT NULL</code> will fail if the named domain or any derived domain is used within a composite-type column of any table in the database. They should eventually be improved to be able to verify the new constraint for such nested columns.</p>
<h2>Examples</h2>
<p>To add a NOT NULL constraint to a domain: </p>
<pre>ALTER DOMAIN zipcode SET NOT NULL;</pre>
<p>To remove a NOT NULL constraint from a domain: </p>
<pre>ALTER DOMAIN zipcode DROP NOT NULL;</pre>
<p>To add a check constraint to a domain: </p>
<pre><code>ALTER DOMAIN zipcode ADD CONSTRAINT zipchk CHECK (char_length(VALUE) = 5);</code></pre>
<p> To remove a check constraint from a domain: </p>
<pre>ALTER DOMAIN zipcode DROP CONSTRAINT zipchk;</pre>
<p>To move the domain into a different schema: </p>
<pre>ALTER DOMAIN zipcode SET SCHEMA customers;</pre>
<h2>Compatibility</h2>
<p><code>ALTER DOMAIN</code> conforms to the SQL standard, except for the OWNER and SET SCHEMA variants, which are PostgreSQL extensions.</p>
<h2>See Also</h2>
<p>CREATE DOMAIN [<code><a href="/docs/linux/man/7-create_domain/">create_domain</a></code>(7)], DROP DOMAIN [<code><a href="/docs/linux/man/7-drop_domain/">drop_domain</a></code>(7)] </p>
