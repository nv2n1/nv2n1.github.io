---
title: "wiredtiger(3)"
name: "wiredtiger"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wiredtiger/"
description: "WiredTiger – Getting Started with the API WiredTiger applications will generally use the following classes to access and manage data:"
---

<p>WiredTiger &#8211; Getting Started with the API WiredTiger applications will generally use the following classes to access and manage data: </p>
<dl>
<dt>&bull;</p>
<dd>a <code>WT_CONNECTION</code> represents a connection to a database. Most applications will only open one connection to a database for each process. All methods in <code>WT_CONNECTION</code> are thread safe.</p>
<dt>&bull;</p>
<dd>a <code>WT_SESSION</code> represents a context in which database operations are performed. Sessions are opened on a specified connection, and applications must open a single session for each thread accessing the database.</p>
<dt>&bull;</p>
<dd>a <code>WT_CURSOR</code> represents a cursor over a collection of data. Cursors are opened in the context of a session (which may have an associated transaction), and can query and update records. In the common case, a cursor is used to access records in a table. However, cursors can be used on subsets of tables (such as a single column or a projection of multiple columns), as an interface to statistics, configuration data or application-specific data sources.</dl>
<p> Handles and operations are <code>configured using strings</code>, which keeps the set of methods in the API relatively small and makes the interface very similar regardless of the programming language used in the application. WiredTiger supports the C, C++, Java and Python programming languages (among others). </p>
<p> By default, WiredTiger works as a traditional key/value store, where the keys and values are raw byte arrays accessed using a <code>WT_ITEM</code> structure. Keys and values may be up to (4GB &#8211; 512B) bytes in size, but depending on how <code>WT_SESSION::create</code> &#8216;maximum item sizes&#8217; are configured, large key and value items will be stored on overflow pages. </p>
<p> WiredTiger also supports a <code>schema layer</code> so that keys and values types can be chosen from a list, or composite keys or values made up of columns with any combination of types. The size (4GB &#8211; 512B) byte limit on keys and values still applies. </p>
<p> All applications that use WiredTiger will be structured roughly as follows. The code below is taken from the complete example program <code>ex_access.c</code>.</p>
<h2>Connecting to a database</h2>
<p>To access a database, first open a connection and create a session handle for the single thread accessing the database: </p>
<pre> WT_CONNECTION *conn;
 WT_CURSOR *cursor;
 WT_SESSION *session;
 const char *key, *value;
 int ret;
 /*
 * Create a clean test directory for this run of the test program if the
 * environment variable isn't already set (as is done by make check).
 */
 if (getenv(&quot;WIREDTIGER_HOME&quot;) == NULL) {
 home = &quot;WT_HOME&quot;;
 ret = system(&quot;rm -rf WT_HOME &amp;&amp; mkdir WT_HOME&quot;);
 } else
 home = NULL;
 /* Open a connection to the database, creating it if necessary. */
 if ((ret = wiredtiger_open(home, NULL, &quot;create&quot;, &amp;conn)) != 0 ||
 (ret = conn-&gt;open_session(conn, NULL, NULL, &amp;session)) != 0) {
 fprintf(stderr, &quot;Error connecting to %s: %s,
 home, wiredtiger_strerror(ret));
 return (ret);
 }</pre>
<p>&nbsp;<wbr>The configuration string&nbsp;<wbr>&#8216;create&#8217;&nbsp;<wbr>is passed to&nbsp;<wbr><code>wiredtiger_open</code>&nbsp;<wbr>to indicate the database should be created if it does not already exist. </p>
<p> The code block above also shows simple error handling with <code>wiredtiger_strerror</code> (a function that returns a string describing an error code passed as its argument). More complex error handling can be configured by passing an implementation of <code>WT_EVENT_HANDLER</code> to <code>wiredtiger_open</code> or <code>WT_CONNECTION::open_session</code>.</p>
<h2>Creating a table</h2>
<p>Create a table we can use to store data: </p>
<pre> ret = session-&gt;create(session,
 &quot;table:access&quot;, &quot;key_format=S,value_format=S&quot;);</pre>
<p>&nbsp;<wbr>This call creates a table called&nbsp;<wbr>&#8216;access&#8217;, configured to use strings for its key and value columns.&nbsp;<wbr>(See&nbsp;<wbr><code>Schema, Columns, Column Groups, Indices and Projections</code>&nbsp;<wbr>for more information on tables with other types of key and value columns.)</p>
<h2>Accessing data with cursors</h2>
<p>Now that we have a table, we open a cursor to perform some operations on it: </p>
<pre> ret = session-&gt;open_cursor(session,
 &quot;table:access&quot;, NULL, NULL, &amp;cursor);</pre>
<p>&nbsp;<wbr>Here, the string&nbsp;<wbr>&#8216;table:access&#8217;&nbsp;<wbr>specifies that we are opening the cursor on the table named&nbsp;<wbr>&#8216;access&#8217;. </p>
<p> Then we insert a new row into the table. The <code>WT_CURSOR::set_key</code> and <code>WT_CURSOR::set_value</code> calls put the application&#8217;s key and value into the cursor, respectively. The <code>WT_CURSOR::insert</code> call creates a record containing that value and inserts it into the table. </p>
<pre> cursor-&gt;set_key(cursor, &quot;key1&quot;); /* Insert a record. */
 cursor-&gt;set_value(cursor, &quot;value1&quot;);
 ret = cursor-&gt;insert(cursor);</pre>
<p>&nbsp;<wbr>Now we iterate through all of the records in the table, printing them out as we go: </p>
<pre> ret = cursor-&gt;reset(cursor); /* Restart the scan. */
 while ((ret = cursor-&gt;next(cursor)) == 0) {
 ret = cursor-&gt;get_key(cursor, &amp;key);
 ret = cursor-&gt;get_value(cursor, &amp;value);
 printf(&quot;Got record: %s : %s, key, value);
 }</pre>
<p>&nbsp;<wbr>Note that the key and value parts of the records are returned as C strings because the table was created that way&nbsp;<wbr>(even if it was created by a previous run of the example). No data extraction or conversion is required in the application. </p>
<p> Because the cursor was positioned in the table after the <code>WT_CURSOR::insert</code> call, we had to re-position it using the WT_CURSOR::first call; if we weren&#8217;t using the cursor for the call to <code>WT_CURSOR::insert</code> above, this loop would simplify to: </p>
<pre>while ((ret = cursor-&gt;next(cursor)) == 0) {
 ...
}</pre>
<h2>Closing handles</h2>
<p>Lastly, we close the connection, which implicitly closes the cursor and session handles: </p>
<pre> ret = conn-&gt;close(conn, NULL);</pre>
