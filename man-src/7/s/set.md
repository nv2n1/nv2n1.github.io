---
title: "set(7)"
name: "set"
section: "7"
letter: "s"
url: "/docs/linux/man/7-set/"
description: "SET – change a run-time parameter"
---

<p>SET &#8211; change a run-time parameter </p>
<h2>Synopsis</h2>
<pre><code>SET [ SESSION | LOCAL ] configuration_parameter { TO | = } { value | 'value' | DEFAULT }
SET [ SESSION | LOCAL ] TIME ZONE { timezone | LOCAL | DEFAULT }</code></pre>
<h2>Description</h2>
<p>The <code>SET</code> command changes run-time configuration parameters. Many of the run-time parameters listed in in the documentation can be changed on-the-fly with <code>SET</code>. (But some require superuser privileges to change, and others cannot be changed after server or session start.) <code>SET</code> only affects the value used by the current session. If <code>SET</code> (or equivalently <code>SET SESSION</code>) is issued within a transaction that is later aborted, the effects of the <code>SET</code> command disappear when the transaction is rolled back. Once the surrounding transaction is committed, the effects will persist until the end of the session, unless overridden by another <code>SET</code>. The effects of <code>SET LOCAL</code> last only till the end of the current transaction, whether committed or not. A special case is <code>SET</code> followed by <code>SET LOCAL</code> within a single transaction: the <code>SET LOCAL</code> value will be seen until the end of the transaction, but afterwards (if the transaction is committed) the <code>SET</code> value will take effect. The effects of <code>SET</code> or <code>SET LOCAL</code> are also canceled by rolling back to a savepoint that is earlier than the command. If <code>SET LOCAL</code> is used within a function that has a SET option for the same variable (see CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)]), the effects of the <code>SET LOCAL</code> command disappear at function exit; that is, the value in effect when the function was called is restored anyway. This allows <code>SET LOCAL</code> to be used for dynamic or repeated changes of a parameter within a function, while still having the convenience of using the SET option to save and restore the caller&#8217;s value. However, a regular <code>SET</code> command overrides any surrounding function&#8217;s SET option; its effects will persist unless rolled back.</p>
<dl>
<dd><code>Note:</code> In PostgreSQL versions 8.0 through 8.2, the effects of a <code>SET LOCAL</code> would be canceled by releasing an earlier savepoint, or by successful exit from a <code>PL/pgSQL</code> exception block. This behavior has been changed because it was deemed unintuitive.</dl>
<h2>Parameters</h2>
<dl>
<dt><code>SESSION</code></p>
<dd>Specifies that the command takes effect for the current session. (This is the default if neither SESSION nor LOCAL appears.)</p>
<dt><code>LOCAL</code></p>
<dd>Specifies that the command takes effect for only the current transaction. After <code>COMMIT</code> or <code>ROLLBACK</code>, the session-level setting takes effect again. Note that <code>SET LOCAL</code> will appear to have no effect if it is executed outside a <code>BEGIN</code> block, since the transaction will end immediately.</p>
<dt><i>configuration_parameter</i></p>
<dd>Name of a settable run-time parameter. Available parameters are documented in in the documentation and below.</p>
<dt><i>value</i></p>
<dd>New value of parameter. Values can be specified as string constants, identifiers, numbers, or comma-separated lists of these, as appropriate for the particular parameter. DEFAULT can be written to specify resetting the parameter to its default value (that is, whatever value it would have had if no <code>SET</code> had been executed in the current session).</dl>
<p> Besides the configuration parameters documented in in the documentation, there are a few that can only be adjusted using the <code>SET</code> command or that have a special syntax:</p>
<dl>
<dt><code>SCHEMA</code></p>
<dd>SET SCHEMA &#8216;<i>value</i>&#8216; is an alias for SET search_path TO <i>value</i>. Only one schema can be specified using this syntax.</p>
<dt><code>NAMES</code></p>
<dd>SET NAMES <i>value</i> is an alias for SET client_encoding TO <i>value</i>.</p>
<dt><code>SEED</code></p>
<dd>Sets the internal seed for the random number generator (the function <code>random</code>). Allowed values are floating-point numbers between -1 and 1, which are then multiplied by 231-1. </p>
<p> The seed can also be set by invoking the function <code>setseed</code>: </p>
<pre>SELECT setseed(<i>value</i>);</pre>
<dt><code>TIME ZONE</code></p>
<dd>SET TIME ZONE <i>value</i> is an alias for SET timezone TO <i>value</i>. The syntax SET TIME ZONE allows special syntax for the time zone specification. Here are examples of valid values:</p>
<dl>
<dd>
<dl>
<dt><code>&#8216;PST8PDT&#8217;</code></p>
<dd>The time zone for Berkeley, California.</p>
<dt><code>&#8216;Europe/Rome&#8217;</code></p>
<dd>The time zone for Italy.</p>
<dt><code>-7</code></p>
<dd>The time zone 7 hours west from UTC (equivalent to PDT). Positive values are east from UTC.</p>
<dt><code>INTERVAL &#8216;-08:00&#8217; HOUR TO MINUTE</code></p>
<dd>The time zone 8 hours west from UTC (equivalent to PST).</p>
<dt><code>LOCAL</code></p>
<dd>
<dt><code>DEFAULT</code></p>
<dd>Set the time zone to your local time zone (that is, the server&#8217;s default value of timezone; if this has not been explicitly set anywhere, it will be the zone that the server&#8217;s operating system defaults to).</dl>
</dl>
</dl>
<p> See in the documentation for more information about time zones.</p>
<h2>Notes</h2>
<p>The function <code>set_config</code> provides equivalent functionality; see in the documentation. Also, it is possible to UPDATE the <code>pg_settings</code> system view to perform the equivalent of <code>SET</code>.</p>
<h2>Examples</h2>
<p>Set the schema search path: </p>
<pre>SET search_path TO my_schema, public;</pre>
<p>Set the style of date to traditional POSTGRES with &#8220;day before month&#8221; input convention: </p>
<pre>SET datestyle TO postgres, dmy;</pre>
<p>Set the time zone for Berkeley, California: </p>
<pre>SET TIME ZONE 'PST8PDT';</pre>
<p>Set the time zone for Italy: </p>
<pre>SET TIME ZONE 'Europe/Rome';</pre>
<h2>Compatibility</h2>
<p>SET TIME ZONE extends syntax defined in the SQL standard. The standard allows only numeric time zone offsets while PostgreSQL allows more flexible time-zone specifications. All other SET features are PostgreSQL extensions.</p>
<h2>See Also</h2>
<p>RESET [<code><a href="/docs/linux/man/7-reset/">reset</a></code>(7)], SHOW [<code><a href="/docs/linux/man/7-show/">show</a></code>(7)] </p>
