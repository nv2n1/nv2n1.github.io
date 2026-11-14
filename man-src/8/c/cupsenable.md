---
title: "cupsenable(8)"
name: "cupsenable"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsenable/"
description: "cupsdisable, cupsenable – stop/start printers and classes"
---

<p>cupsdisable, cupsenable &#8211; stop/start printers and classes</p>
<h2>Synopsis</h2>
<p><code>cupsdisable</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-c</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-r</code> <i>reason</i> ] [ <code>&#8211;hold</code> ] <i>destination(s)</i><br />
 <code>cupsenable</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-c</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>&#8211;release</code> ] <i>destination(s)</i></p>
<h2>Description</h2>
<p><code>cupsenable</code> starts the named printers or classes while <code>cupsdisable</code> stops the named printers or classes.</p>
<h2>Options</h2>
<p>The following options may be used:</p>
<dl>
<dt><code>-E</code></p>
<dd>Forces encryption of the connection to the server.</p>
<dt><code>-U </code><i>username</i></p>
<dd>Uses the specified username when connecting to the server.</p>
<dt><code>-c</code></p>
<dd>Cancels all jobs on the named destination.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd>Uses the specified server and port.</p>
<dt><code>&#8211;hold</code></p>
<dd>Holds remaining jobs on the named printer. Useful for allowing the current job to complete before performing maintenance.</p>
<dt><code>-r &quot;</code><i>reason</i><code>&quot;</code></p>
<dd>Sets the message associated with the stopped state. If no reason is specified then the message is set to &quot;Reason Unknown&quot;.</p>
<dt><code>&#8211;release</code></p>
<dd>Releases pending jobs for printing. Use after running <code>cupsdisable</code> with the <i>&#8211;hold</i> option to resume printing.</dl>
<h2>Conforming To</h2>
<p>Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> The System V versions of these commands are <code>disable</code> and <code>enable</code>, respectively. They have been renamed to avoid conflicts with the <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) build-in commands of the same names. </p>
<p> The CUPS versions of <code>disable</code> and <code>enable</code> may ask the user for an access password depending on the printing system configuration. This differs from the System V versions which require the root user to execute these commands.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cupsaccept/">cupsaccept</a></code>(8), <code><a href="/docs/linux/man/8-cupsreject/">cupsreject</a></code>(8), <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
