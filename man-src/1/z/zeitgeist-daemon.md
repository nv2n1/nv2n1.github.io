---
title: "zeitgeist-daemon(1)"
name: "zeitgeist-daemon"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zeitgeist-daemon/"
description: "zeitgeist-daemon – D-Bus interface providing a log of activities"
---

<h2 class="name">NAME</h2>
<p> zeitgeist-daemon &#8211; D-Bus interface providing a log of activities</p>
<h2>SYNOPSIS</h2>
<p> <code>zeitgeist-daemon</code> <i>[OPTION]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>zeitgeist-daemon</code> is daemon providing an activity log. That is, it consists of a central database for events such as file usage, browser history, calendar entries, etc. </p>
<p> All this information is made available to external applications which communicate with <code>zeitgeist-daemon</code> over D-Bus. Interested applications can request information, insert new events or delete existing events. </p>
<p> Zeitgeist is also capable of establishing relationships between activities. Its purpose is enabling an activity-aware desktop with adaptive user interfaces. </p>
<p> By default, <code>zeitgeist-daemon</code> will also start the bundled logging application <code>zeitgeist-datahub</code>. </p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with options starting with two dashes (`&#8211;&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>&#8211;no-datahub</code></p>
<dd> Do not start <code>zeitgeist-datahub</code> together with this daemon.</p>
<dt><code>-r, &#8211;replace</code></p>
<dd> Replace any existing Zeitgeist instance if there is one already running. If this option isn&#8217;t used, <code>zeitgeist-daemon</code> will refuse to start if another running instance is found.</p>
<dt><code>&#8211;log-level=</code><i>LOG_LEVEL</i></p>
<dd> Specifies how much information should be printed to the standard output. Possible values are: DEBUG, INFO, WARNING, ERROR, CRITICAL.</p>
<dt><code>&#8211;log-file=</code><i>LOG_FILE</i></p>
<dd> Specifies a file to which log output will be appended.</p>
<dt><code>-q, &#8211;quit</code></p>
<dd> Stop a currently running Zeitgeist instance and exit. This lets Zeitgeist finish any operation it may currently be doing.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Shows which version of Zeitgeist is being executed.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Shows a short help message listing all supported options. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>ZEITGEIST_DATA_PATH</code></p>
<dd> Overrides the directory where user data files are placed. The default value is that of XDG&#8217;s data dir (usually ~/.local/share/zeitgeist).</p>
<dt><code>ZEITGEIST_DATABASE_PATH</code></p>
<dd> This variable lets you specify an override for the filename of the main database. The default value is $ZEITGEIST_DATA_PATH/activity.sqlite.</p>
<dt><code>ZEITGEIST_DATABASE_BACKUP_PATH</code></p>
<dd> This variable lets you specify an override for the filename of a possible database backup. The default value is $ZEITGEIST_DATA_PATH/activity.sqlite.bck.</p>
<dt><code>ZEITGEIST_DISABLED_EXTENSIONS</code></p>
<dd> This variable lets you specify comma separated list of extension names which shouldn&#8217;t be loaded. The names are extracted from type names of the extensions, so to disable extension with type name ZeitgeistDataSourceRegistry, value of the variable should be DataSourceRegistry. </p>
</dl>
<h2>SIGNALS</h2>
<p> <i>SIGHUP</i>: zeitgeist-daemon will shut itself down in a clean way.</p>
<dl>
<dt>
<dd> It is recommended that system updates of Zeitgeist send this signal to all running instances of zeitgeist-daemon. DBus activation will make sure the updated software is automatically restarted when needed. </p>
</dl>
<h2>EXIT CODES</h2>
<dl>
<dt><code>0</code></p>
<dd> Zeitgeist terminated normally.</p>
<dt><code>1</code></p>
<dd> An unspecified error occurred.</p>
<dt><code>10</code></p>
<dd> There is already a running Zeitgeist instance.</p>
<dt><code>21</code></p>
<dd> Could not access the database file.</p>
<dt><code>22</code></p>
<dd> The database file is locked. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>zeitgeist-datahub</code>, <code>gnome-activity-journal</code> </p>
<h2>BUGS</h2>
<p> Please report any bugs on <a rel="nofollow" href="https://bugs.launchpad.net/zeitgeist.">https://bugs.launchpad.net/zeitgeist.</a> </p>
<h2>AUTHORS</h2>
<p> Please see the AUTHORS file bundled with this application for a complete list of contributors. </p>
<h2>LICENSE</h2>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 2.1 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>Index</h2>
