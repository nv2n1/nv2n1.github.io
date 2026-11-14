---
title: "reset(7)"
name: "reset"
section: "7"
letter: "r"
url: "/docs/linux/man/7-reset/"
description: "RESET – restore the value of a run-time parameter to the default value"
---

<p>RESET &#8211; restore the value of a run-time parameter to the default value </p>
<h2>Synopsis</h2>
<pre>RESET <i>configuration_parameter</i>
RESET ALL</pre>
<h2>Description</h2>
<p><code>RESET</code> restores run-time parameters to their default values. <code>RESET</code> is an alternative spelling for </p>
<pre>SET <i>configuration_parameter</i> TO DEFAULT</pre>
<p>Refer to SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] for details. </p>
<p> The default value is defined as the value that the parameter would have had, if no <code>SET</code> had ever been issued for it in the current session. The actual source of this value might be a compiled-in default, the configuration file, command-line options, or per-database or per-user default settings. This is subtly different from defining it as &#8220;the value that the parameter had at session start&#8221;, because if the value came from the configuration file, it will be reset to whatever is specified by the configuration file now. See in the documentation for details. </p>
<p> The transactional behavior of <code>RESET</code> is the same as <code>SET</code>: its effects will be undone by transaction rollback.</p>
<h2>Parameters</h2>
<dl>
<dt><i>configuration_parameter</i></p>
<dd>Name of a settable run-time parameter. Available parameters are documented in in the documentation and on the SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] reference page.</p>
<dt><code>ALL</code></p>
<dd>Resets all settable run-time parameters to default values.</dl>
<h2>Examples</h2>
<p>Set the timezone configuration variable to its default value: </p>
<pre>RESET timezone;</pre>
<h2>Compatibility</h2>
<p><code>RESET</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)], SHOW [<code><a href="/docs/linux/man/7-show/">show</a></code>(7)] </p>
