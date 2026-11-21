---
title: "flamerobin(1)"
name: "flamerobin"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flamerobin/"
description: "flamerobin – management and data manipulation tool for the Firebird DBMS"
---

<p>FlameRobin 0.7</p>
<h2 class="name">NAME</h2>
<p> <code>flamerobin</code> &#8211; management and data manipulation tool for the Firebird DBMS </p>
<h2>SYNOPSIS</h2>
<p> <code>flamerobin</code> [ &#8211;<code>h </code><i>directory </i> &#8211;<code>-home = </code><i>directory </i>] [ &#8211;<code>uh </code><i>directory </i> &#8211;<code>-user-home = </code><i>directory </i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>flamerobin</code> is a graphical frontend to the Firebird DBMS. It is small and simple, yet offers all the basic features needed to create and manipulate databases, execute queries and perform administrative tasks. </p>
<p> This manual page only documents the run-time options and environment of <code>.</code> Information about using the GUI may be obtained by selecting the Help &#8211; Manual menu item once the application is running. </p>
<p> <code>flamerobin</code> uses two directory hierarchies for its normal operation. The <i>data directory</i> contains the templates for property pages, the default configuration and the on-line documentation grouped into three sub-directories as follows:</p>
<dl>
<dt><code>conf-defs </code></dt>
<dd> default configuration</dd>
<dt><code>docs </code></dt>
<dd> on-line documentation</dd>
<dt><code>html-templates </code></dt>
<dd> templates for property pages</dd></dl>
<p> The <i>user home directory</i> contains the per-user configuration, comprising three entries: </p>
<dl>
<dt><code>fr_databases.conf </code></dt>
<dd> this file stores the user&#8217;s registered databases.</dd>
<dt><code>fr_settings.conf </code></dt>
<dd> this file stores the user&#8217;s preferences related to the <code>flamerobin</code> GUI.</dd>
<dt><code>history </code></dt>
<dd> this directory holds the SQL statement history, one item per file.</dd></dl>
<p> <code>flamerobin</code> accepts several options, which are described as follows:</p>
<dl>
<dt><code>-h </code><i>directory</i></dt>
<dd>
</dd><dt><code>&#8211;home = </code><i>directory</i></dt>
<dd> Use <i>directory</i> as the <i>data directory</i> (but see Sx ENVIRONMENT below). </dd>
<dt><code>-uh </code><i>directory</i></dt>
<dd>
</dd><dt><code>&#8211;user-home = </code><i>directory</i></dt>
<dd> Use <i>directory</i> as the <i>user home directory</i> (but see Sx ENVIRONMENT and Sx CAVEATS below).</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FR_HOME</code></dt>
<dd> Specifies an alternate location for the <code>flamerobin</code> <i>data directory</i> </dd>
<p> If both &#8211;<code>h</code> (or &#8211;<code>-home</code> and this environment variable are set, the command line argument takes precedence.</p>
<dt><code>FR_USER_HOME</code></dt>
<dd> Specifies an alternate location for the <code>flamerobin</code> <i>user home directory</i> </dd>
<p> If both &#8211;<code>uh</code> (or &#8211;<code>-user-home</code> and this environment variable are set, the command line argument takes precedence.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/flamerobin </code></dt>
<dd> The default <code>flamerobin</code> <i>data directory</i></dd>
<dt><code>~/.flamerobin </code></dt>
<dd> The default <code>flamerobin</code> <i>user home directory</i></dd></dl>
<h2>AUTHORS</h2>
<p> <code>flamerobin</code> was written by An The FlameRobin Development Team Aq Pa <a rel="nofollow" href="http://www.flamerobin.org/">http://www.flamerobin.org/</a> .</p>
<h2>CAVEATS</h2>
<p> <code>flamerobin</code> only writes files under the <i>user home directory</i> If <code>flamerobin</code> is configured so that this directory and the files contained therein are shared among several users or concurrent instances of <code>,</code> no precaution is taken to avoid overwriting settings created by other users or other application instances.</p>
<h2>NOTES</h2>
<p> The specification of the <i>data directory</i> and the <i>user home directory</i> (regardless of whether they occur in the environment or on the command line) may be the literal string &#8220;$app&#8221; which translates to a common data folder determined at compilation time, or &#8220;$user&#8221; which translates to the user local data directory. These options currently have effect only on Windows platform. </p>
