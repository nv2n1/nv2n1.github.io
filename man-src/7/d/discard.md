---
title: "discard(7)"
name: "discard"
section: "7"
letter: "d"
url: "/docs/linux/man/7-discard/"
description: "DISCARD – discard session state"
---

<p>DISCARD &#8211; discard session state </p>
<h2>Synopsis</h2>
<pre>DISCARD { ALL | PLANS | TEMPORARY | TEMP }</pre>
<h2>Description</h2>
<p><code>DISCARD</code> releases internal resources associated with a database session. These resources are normally released at the end of the session. </p>
<p> <code>DISCARD TEMP</code> drops all temporary tables created in the current session. <code>DISCARD PLANS</code> releases all internally cached query plans. <code>DISCARD ALL</code> resets a session to its original state, discarding temporary resources and resetting session-local configuration changes.</p>
<h2>Parameters</h2>
<dl>
<dt><code>TEMPORARY or TEMP</code></p>
<dd>Drops all temporary tables created in the current session.</p>
<dt><code>PLANS</code></p>
<dd>Releases all cached query plans.</p>
<dt><code>ALL</code></p>
<dd>Releases all temporary resources associated with the current session and resets the session to its initial state. Currently, this has the same effect as executing the following sequence of statements: </p>
<pre>SET SESSION AUTHORIZATION DEFAULT;
RESET ALL;
DEALLOCATE ALL;
CLOSE ALL;
UNLISTEN *;
SELECT pg_advisory_unlock_all();
DISCARD PLANS;
DISCARD TEMP;</pre>
</dl>
<h2>Notes</h2>
<p><code>DISCARD ALL</code> cannot be executed inside a transaction block.</p>
<h2>Compatibility</h2>
<p><code>DISCARD</code> is a PostgreSQL extension.</p>
