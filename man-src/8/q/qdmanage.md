---
title: "qdmanage(8)"
name: "qdmanage"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qdmanage/"
description: "qdmanage – dispatch management tool"
---

<p>qdmanage &#8211; dispatch management tool</p>
<h2>Synopsis</h2>
<p>qdmanage <i>operation</i> [<i>options&#8230;</i>] [<i>arguments&#8230;</i>]</p>
<h2>Description</h2>
<p>An AMQP management client for use with qdrouterd. Sends AMQP management operations requests and prints the response in JSON format. This is a generic AMQP management tool and can be used with any standard AMQP managed endpoint, not just with qdrouter.</p>
<h2>Operations</h2>
<dl>
<dt><i>query</i> [<i>ATTR</i>&#8230;]</p>
<dd>Print the attributes named in the ATTR list or all attributes if none are listed. Print attributes for all entities by default, use &#8211;type, &#8211;name and &#8211;identity options to restrict what is printed.</p>
<dt><i>create</i> [<i>ATTR=VALUE</i>&#8230;]</p>
<dd>Create a new entity with the specified attributes. With the &#8211;stdin option, read attributes from stdin. This can be a JSON map of attributes to create a single entity, or a JSON list of maps to create multiple entitiees.</p>
<dt><i>read</i></p>
<dd>Print the attributes of an entity specified by the &#8211;name or &#8211;identity options. With the &#8211;stdin option, create entities based on data from stdin. This can be a JSON map of attributes to create a single entity, or a JSON list of maps to create multiple entitiees.</p>
<dt><i>update</i> [<i>ATTR=VALUE</i>&#8230;]</p>
<dd>Update the attributes of an existing entity. With the &#8211;stdin option, read attributes from stdin. This can be a JSON map of attributes to update a single entity, or a JSON list of maps to update multiple entitiees. If an ATTR name is listed with no =VALUE, that attribute will be deleted from the entity.</p>
<dt><i>delete</i></p>
<dd>Delete an entity specified by the &#8211;name or &#8211;identity options.</p>
<dt><i>get-types</i> [<i>TYPE</i>]</p>
<dd>List entity types with their base types. With no arguments list all types.</p>
<dt><i>get-operations</i> [<i>TYPE</i>]</p>
<dd>List entity types with their operations. With no arguments list all types.</p>
<dt><i>get-attributes</i> [<i>TYPE</i>]</p>
<dd>List entity types with their attributes. With no arguments list all types.</p>
<dt><i>get-annotations</i> [<i>TYPE</i>]</p>
<dd>List entity types with their annotations. With no arguments list all types.</p>
<dt><i>get-mgmt-nodes</i></p>
<dd>List all other known management nodes connected to this one.</p>
<dt><i>get-json-schema</i> [<i>INDENT</i>]</p>
<dd>Get the router schema in JSON format. Optional integer indent for formatted output.</p>
<dt><i>get-log</i> [<i>INDENT</i>]</p>
<dd>Get recent log entries from the router.</dl>
<h2>Options</h2>
<p>-h, &#8211;help : show this help message and exit </p>
<p> &#8211;version : Print version and exit. </p>
<p> &#8211;type=TYPE : Type of entity to operate on. </p>
<p> &#8211;name=NAME : Name of entity to operate on. </p>
<p> &#8211;identity=ID : Identity of entity to operate on. </p>
<p> &#8211;indent=INDENT : Pretty-printing indent. -1 means don&#8217;t pretty-print </p>
<p> &#8211;stdin : Read attributes as JSON map or list of maps from </p>
<p> &#8211;body=BODY : JSON value to use as body of a non-standard operation </p>
<p> &#8211;properties=PROPERTIES : JSON map to use as properties for a non-standard operation call.</p>
<h3>Connection Options</h3>
<p>-b URL, &#8211;bus=URL : URL of the messaging bus to connect to (default </p>
<p> -r ROUTER-ID, &#8211;router=ROUTER-ID : Router to be queried </p>
<p> -t SECS, &#8211;timeout=SECS : Maximum time to wait for connection in seconds (default 5) </p>
<p> &#8211;ssl-certificate=CERT : Client SSL certificate (PEM Format) </p>
<p> &#8211;ssl-key=KEY : Client SSL private key (PEM Format) </p>
<p> &#8211;ssl-trustfile=TRUSTED-CA-DB : Trusted Certificate Authority Database file (PEM Format) </p>
<p> &#8211;ssl-password=PASSWORD : Certificate password, will be prompted if not specifed.</p>
<h2>Files</h2>
<dl>
<dt><code>/usr//usr/share/doc/qpid-dispatch/qdrouter.json</code></p>
<dd>Management schema for qdrouterd.</p>
<dt><code>/usr//usr/share/doc/qpid-dispatch/qdrouter.json.readme.txt</code></p>
<dd>Explanation of the management schema.</dl>
<h2>Examples</h2>
<p>Show the logging configuration </p>
<pre>qdmanage query --type=log</pre>
<p>Enable debug and higher log messages by default: </p>
<pre>qdmanage udpdate name=log/DEFAULT enable=debug+</pre>
<p>Enable trace log messages only for the MESSAGE moudle and direct MESSAGE logs to the file &quot;test.log&quot; </p>
<pre>qdmanage udpdate name=log/MESSAGE enable=trace output=test.log</pre>
<p>Set MESSAGE logging back to the default: </p>
<pre>qdmanage udpdate name=log/MESSAGE enable=default</pre>
<p>Disable MESSAGE logging: </p>
<pre>qdmanage udpdate name=log/MESSAGE enable=none</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-qdrouterd/">qdrouterd</a>(8)</i>, <i><a href="/docs/linux/man/8-qdstat/">qdstat</a>(8)</i>, <i><a href="/docs/linux/man/5-qdrouterd-conf/">qdrouterd.conf</a>(5)</i> </p>
<p> <i><a rel="nofollow" href="http://qpid.apache.org/components/dispatch-router">http://qpid.apache.org/components/dispatch-router</a></i></p>
<h2>Copyright</h2>
<p>2013, Apache Qpid &lt;<a rel="nofollow" href="http://qpid.apache.org/">http://qpid.apache.org/</a>&gt;</p>
