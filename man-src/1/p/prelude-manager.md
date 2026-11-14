---
title: "prelude-manager(1)"
name: "prelude-manager"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prelude-manager/"
description: "prelude-manager – Collects and normalize events."
---

<h2>NAME</h2>
<p> prelude-manager &#8211; Collects and normalize events.</p>
<h2>SYNOPSIS</h2>
<p> <code>prelude-manager [options]</code></p>
<h2>DESCRIPTION</h2>
<p> Prelude Manager is a high-availability server which can collect, filter, relay, reverse-relay, normalize and store events. Events can come from registered analyzers and/or managers. The common usage is to store nomalized events into a database, thus this can be extended to store informations in plain text or xml files. </p>
<h2>OPTIONS</h2>
<p> Some prelude-manager option are contextual, they have to be prefixed by another. </p>
<p> <code>&#8211;prelude</code> Prelude generic options </p>
<p> <code>&#8211;profile=&lt;name&gt;</code> Profile to use for this analyzer </p>
<p> <code>&#8211;heartbeat-interval=&lt;interval&gt;</code> Number of seconds between two heartbeat </p>
<p> <code>&#8211;server-addr=&lt;address&gt;</code> Address where this sensor should report to (addr:port) </p>
<p> <code>&#8211;analyzer-name=&lt;name&gt;</code> Name for this analyzer </p>
<dl>
<dt><code>&#8211;db=&lt;INAME&gt;</code></p>
<dd> Options for the libpreludedb plugin </p>
<p> <code>-t, &#8211;type=&lt;type&gt;</code> Type of database (mysql/pgsql/sqlite3) </p>
<p> <code>-l, &#8211;log=&lt;file name&gt;</code> Log all queries in a file, should be only used for debugging purpose </p>
<p> <code>-h, &#8211;host=&lt;address&gt;</code> The host where the database server is running (in case of client/server database) </p>
<p> <code>-f, &#8211;file=&lt;file name&gt;</code> The file where the database is stored (in case of file based database) </p>
<p> <code>-p, &#8211;port=&lt;port number&gt;</code> The port where the database server is listening (in case of client/server database) </p>
<p> <code>-d, &#8211;name=&lt;name&gt;</code> The name of the database where the alerts will be stored </p>
<p> <code>-u, &#8211;user=&lt;user&gt;</code> User of the database (in case of client/server database) </p>
<p> <code>-P, &#8211;pass=&lt;password&gt;</code> Password for the user (in case of client/server database)</p>
<dt>
<dd>
<p> <code>&#8211;debug=&lt;INAME&gt;</code> Option for the debug plugin </p>
<p> <code>-o, &#8211;object=&lt;name&gt;</code> Name of IDMEF object to print (no object provided will print the entire message) </p>
<p> <code>-l, &#8211;logfile=&lt;file name&gt;</code> Specify output file to use (default to stdout)</p>
<dt>
<dd>
<p> <code>&#8211;relaying=&lt;INAME&gt;</code> Relaying plugin option </p>
<p> <code>-p, &#8211;parent-managers=&lt;address&gt;</code> List of managers address:port pair where messages should be sent to</p>
<dt>
<dd>
<p> <code>&#8211;textmod=&lt;INAME&gt;</code> Option for the textmod plugin </p>
<p> <code>-l, &#8211;logfile=&lt;file name&gt;</code> Specify logfile to use</p>
<dt>
<dd>
<p> <code>&#8211;xmlmod=&lt;INAME&gt;</code> Option for the xmlmod plugin </p>
<p> <code>-l, &#8211;logfile=&lt;file name&gt;</code> Specify output file to use </p>
<p> <code>-v, &#8211;validate=&lt;xml&gt;</code> Validate IDMEF XML output against DTD </p>
<p> <code>-f, &#8211;format=&lt;format&gt;</code> Format XML output so that it is readable </p>
<p> <code>-d, &#8211;disable-buffering=&lt;boolean&gt;</code> Disable output file buffering to prevent truncated tags </p>
<p> <code>&#8211;idmef-criteria-filter=&lt;INAME&gt;</code> Filter message based on IDMEF criteria </p>
<p> <code>-r, &#8211;rule=&lt;rule&gt;</code> Filter rule, or filename containing rule </p>
<p> <code>&#8211;hook=&lt;value&gt;</code> Where the filter should be hooked (reporting|reverse-relaying|plugin name)</p>
<dt>
<dd>
<p> <code>&#8211;config=&lt;file name&gt;</code> Configuration file to use</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version number</p>
<dt><code>-D, &#8211;debug-level=&lt;level&gt;</code></p>
<dd> Run in debug mode</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Run in daemon mode</p>
<dt><code>-P, &#8211;pidfile=&lt;file name&gt;</code></p>
<dd> Write Prelude PID to pidfile</p>
<dt><code>-c, &#8211;child-managers=&lt;address&gt;</code></p>
<dd> List of managers address:port pair where messages should be gathered from</p>
<dt><code>-l, &#8211;listen=&lt;address&gt;</code></p>
<dd> Address the sensors server should listen on (addr:port)</p>
<dt><code>-f, &#8211;failover=&lt;boolean&gt;</code></p>
<dd> Enable failover for specified report plugin</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help </p>
</dl>
<h2>FILES</h2>
<p> <code>/etc/prelude/prelude-manager.conf </code> &#8211; the configuration file </p>
<h2>BUGS</h2>
<p> This man page hadn&#8217;t been proof-read yet. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-prelude-adduser/">prelude-adduser</a>(1) </p>
<h2>Index</h2>
