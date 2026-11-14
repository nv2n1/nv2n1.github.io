---
title: "incoming-conf(5)"
name: "incoming-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-incoming-conf/"
description: "incoming.conf – Configuration of incoming news feeds"
---

<p>incoming.conf &#8211; Configuration of incoming news feeds</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/incoming.conf consists of three types of entries: key/value, peer and group. Comments are from the hash character <tt>&quot;#&quot;</tt> to the end of the line. Blank lines are ignored. All key/value entries within each type must not be duplicated. Key/value entries are a keyword immediately followed by a colon, at least one blank and a value. For example: </p>
<pre> max-connections: 10</pre>
<p>A legal key does not contains blanks, colons, nor <tt>&quot;#&quot;</tt>. There are three different types of values: integers, booleans, and strings. Integers are as to be expected. A boolean value is either <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt> (case is significant). A string value is any other sequence of characters. If the string needs to contain whitespace, then it must be quoted with double quotes. </p>
<p> Peer entries look like: </p>
<pre> peer &lt;name&gt; {
 # body
 }</pre>
<p>The word <tt>&quot;peer&quot;</tt> is required. &lt;name&gt; is a label for this peer. It is any string valid as a key. The body of a peer entry contains some number of key/value entries. </p>
<p> Group entries look like: </p>
<pre> group &lt;name&gt; {
 # body
 }</pre>
<p>The word <tt>&quot;group&quot;</tt> is required. &lt;name&gt; is any string valid as a key. The body of a group entry contains any number of the three types of entries. So key/value pairs can be defined inside a group, and peers can be nested inside a group, and other groups can be nested inside a group. Key/value entries that are defined outside of all peer and group entries are said to be at global scope. Global key/value entries act as defaults for peers. When <code>innd</code> looks for a specific value in a peer entry (for example, the maximum number of connections to allow), if the value is not defined in the peer entry, then the enclosing groups are examined for the entry (starting at the closest enclosing group). If there are no enclosing groups, or the enclosing groups don&#8217;t define the key/value, then the value at global scope is used. A small example could be: </p>
<pre> # Global value applied to all peers that have no value of their own.
 max-connections: 5
 # A peer definition.
 peer uunet {
 hostname: usenet1.uu.net
 }
 peer vixie {
 hostname: gw.home.vix.com
 max-connections: 10 # Override global value.
 }
 # A group of two peers which can open more connections than normal.
 group fast-sites {
 max-connections: 15
 # Another peer. The max-connections: value from the
 # fast-sites group scope is used.
 peer data.ramona.vix.com {
 hostname: data.ramona.vix.com
 }
 peer bb.home.vix.com {
 hostname: bb.home.vix.com
 max-connections: 20 # He can really cook.
 }
 }</pre>
<p>Given the above configuration file, the defined peers would have the following values for the <i>max-connections</i> key. </p>
<pre> uunet 5
 vixie 10
 data.ramona.vix.com 15
 bb.home.vix.com 20</pre>
<h2>Parameters</h2>
<p>The following keys are allowed:</p>
<dl>
<dt><i>comment</i></p>
<dd>This key requires a string value. Reserved for future use. The default is an empty string.</p>
<dt><i>email</i></p>
<dd>This key requires a string value. Reserved for future use. The default is an empty string.</p>
<dt><i>hold-time</i></p>
<dd>This key requires a positive integer value. It defines the hold time before closing, if the connection is over <i>max-connections</i>. A value of zero specifies immediate close. The default is <tt>0</tt>.</p>
<dt><i>hostname</i></p>
<dd>This key requires a string value. It is a list of hostnames separated by a comma. A hostname is the host&#8217;s fully qualified domain name, or the dotted-quad <font SIZE="-1">IP</font> address of the peer for IPv4, or the colon-separated <font SIZE="-1">IP</font> address of the peer for IPv6. If this key is not present in a peer block, the hostname defaults to the label of the peer.</p>
<dt><i>identd</i></p>
<dd>This key requires a string value. It is used if you wish to require a peer&#8217;s user name retrieved through <code>identd</code> match the specified string. Note that currently <code>innd</code> does not implement any timeout in <code>identd</code> callbacks, so enabling this option may cause <code>innd</code> to hang if the remote peer does not respond to <code>ident</code> callbacks in a reasonable timeframe. The default is an empty string, that is to say no <code>identd</code>.</p>
<dt><i>ignore</i></p>
<dd>This key requires a boolean value. Setting this entry causes <code>innd</code> to refuse every article sent via <font SIZE="-1">CHECK</font> or <font SIZE="-1">IHAVE</font> by this peer. The default is false.</p>
<dt><i>max-connections</i></p>
<dd>This key requires a positive integer value. It defines the maximum number of connections allowed. A value of zero specifies an unlimited number of maximum connections (<tt>&quot;unlimited&quot;</tt> or <tt>&quot;none&quot;</tt> can be used as synonyms). The default is <tt>0</tt>.</p>
<dt><i>nolist</i></p>
<dd>This key requires a boolean value. It defines whether a peer is allowed to issue list command. The default is false, that is to say it can.</p>
<dt><i>noresendid</i></p>
<dd>This key requires a boolean value. It defines whether <code>innd</code> should send <tt>438</tt> (response to <font SIZE="-1">CHECK</font>, in streaming mode) or <tt>435</tt> (response to <font SIZE="-1">IHAVE</font> in non-streaming mode) responses instead of <tt>431</tt> (response to <font SIZE="-1">CHECK</font>) or <tt>436</tt> (response to <font SIZE="-1">IHAVE</font>) if a message is offered that is already received from another peer. The deferral feature can be useful for peers that resend messages right away, as <code>innfeed</code> does. The default is false: the deferral feature is used so that the peer receives <tt>431</tt> and <tt>436</tt> codes, and therefore resends the article later.</p>
<dt><i>password</i></p>
<dd>This key requires a string value. It is used if you wish to require a peer to supply a password via <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER/PASS</font>. The default is an empty string, that it to say no password.</p>
<dt><i>patterns</i></p>
<dd>This key requires a string value. It is a list of <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5)-style list of newsgroups which are to be accepted from this host. The default is the string <tt>&quot;*&quot;</tt>, that is to say all groups are accepted.</p>
<dt><i>skip</i></p>
<dd>This key requires a boolean value. Setting this entry causes this peer to be skipped. The default is false.</p>
<dt><i>streaming</i></p>
<dd>This key requires a boolean value. It defines whether streaming commands (<font SIZE="-1">CHECK</font> and <font SIZE="-1">TAKETHIS</font>) are allowed from this peer. The default is true.</dl>
<h2>History</h2>
<p>Written by Fabien Tassin &lt;fta [at] sofaraway.org&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> incoming.conf.pod 9591 2013-12-19 17:48:54Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
