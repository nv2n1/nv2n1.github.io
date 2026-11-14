---
title: "create_domain(7)"
name: "create_domain"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_domain/"
description: "CREATE DOMAIN – define a new domain"
---

<p>CREATE DOMAIN &#8211; define a new domain </p>
<h2>Synopsis</h2>
<pre>CREATE DOMAIN <i>name</i> [ AS ] <i>data_type</i>
 [ DEFAULT <i>expression</i> ]
 [ <i>constraint</i> [ ... ] ]
where <i>constraint</i> is:
[ CONSTRAINT <i>constraint_name</i> ]
{ NOT NULL | NULL | CHECK (<i>expression</i>) }</pre>
<h2>Description</h2>
<p><code>CREATE DOMAIN</code> creates a new domain. A domain is essentially a data type with optional constraints (restrictions on the allowed set of values). The user who defines a domain becomes its owner. </p>
<p> If a schema name is given (for example, CREATE DOMAIN myschema.mydomain &#8230;) then the domain is created in the specified schema. Otherwise it is created in the current schema. The domain name must be unique among the types and domains existing in its schema. </p>
<p> Domains are useful for abstracting common constraints on fields into a single location for maintenance. For example, several tables might contain email address columns, all requiring the same CHECK constraint to verify the address syntax. Define a domain rather than setting up each table&#8217;s constraint individually.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of a domain to be created.</p>
<dt><i>data_type</i></p>
<dd>The underlying data type of the domain. This can include array specifiers.</p>
<dt><code>DEFAULT </code><i>expression</i></p>
<dd>The DEFAULT clause specifies a default value for columns of the domain data type. The value is any variable-free expression (but subqueries are not allowed). The data type of the default expression must match the data type of the domain. If no default value is specified, then the default value is the null value. </p>
<p> The default expression will be used in any insert operation that does not specify a value for the column. If a default value is defined for a particular column, it overrides any default associated with the domain. In turn, the domain default overrides any default value associated with the underlying data type.</p>
<dt><code>CONSTRAINT </code><i>constraint_name</i></p>
<dd>An optional name for a constraint. If not specified, the system generates a name.</p>
<dt><code>NOT NULL</code></p>
<dd>Values of this domain are not allowed to be null.</p>
<dt><code>NULL</code></p>
<dd>Values of this domain are allowed to be null. This is the default. </p>
<p> This clause is only intended for compatibility with nonstandard SQL databases. Its use is discouraged in new applications.</p>
<dt><code>CHECK (</code><i>expression</i><code>)</code></p>
<dd>CHECK clauses specify integrity constraints or tests which values of the domain must satisfy. Each constraint must be an expression producing a Boolean result. It should use the key word VALUE to refer to the value being tested. </p>
<p> Currently, CHECK expressions cannot contain subqueries nor refer to variables other than VALUE.</dl>
<h2>Examples</h2>
<p>This example creates the <code>us_postal_code</code> data type and then uses the type in a table definition. A regular expression test is used to verify that the value looks like a valid US postal code: </p>
<pre>CREATE DOMAIN us_postal_code AS TEXT
CHECK(
 VALUE ~ '^\d{5}$'
OR VALUE ~ '^\d{5}-\d{4}$'
);
CREATE TABLE us_snail_addy (
 address_id SERIAL PRIMARY KEY,
 street1 TEXT NOT NULL,
 street2 TEXT,
 street3 TEXT,
 city TEXT NOT NULL,
 postal us_postal_code NOT NULL
);</pre>
<h2>Compatibility</h2>
<p>The command <code>CREATE DOMAIN</code> conforms to the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER DOMAIN [<code><a href="/docs/linux/man/7-alter_domain/">alter_domain</a></code>(7)], DROP DOMAIN [<code><a href="/docs/linux/man/7-drop_domain/">drop_domain</a></code>(7)] </p>
