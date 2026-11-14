---
title: "nodeattr(1)"
name: "nodeattr"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nodeattr/"
description: "nodeattr – query genders file"
---

<h2>NAME</h2>
<p> nodeattr &#8211; query genders file</p>
<h2>SYNOPSIS</h2>
<p> <code>nodeattr</code> <i>[-f genders] [-q | -c | -n | -s] [-X exclude_query] query</i><br />
 <code>nodeattr</code> <i>[-f genders] [-q | -c | -n | -s] -A</i><br />
 <code>nodeattr</code> <i>[-f genders] [-v] [node] attr[=val]</i><br />
 <code>nodeattr</code> <i>[-f genders] -Q [node] query</i><br />
 <code>nodeattr</code> <i>[-f genders] -V [-U] attr</i><br />
 <code>nodeattr</code> <i>[-f genders] -l [node]</i><br />
 <code>nodeattr</code> <i>[-f genders] -k</i><br />
 <code>nodeattr</code> <i>[-f genders] -d genders</i><br />
 <code>nodeattr</code> <i>[-f genders] &#8211;expand</i><br />
 <code>nodeattr</code> <i>[-f genders] &#8211;compress</i> </p>
<h2>DESCRIPTION</h2>
<p> When invoked with the <i>-q</i> , <i>-c</i> , <i>-n</i> , or <i>-s</i> arguments, <code>nodeattr</code> reads the genders file and outputs a list of nodes that match the specified query. The nodes are listed in hostlist format, comma separated lists, newline separated lists, or space separated lists respectively. Genders queries will query the genders database for a set of nodes based on the union, intersection, difference, or complement of genders attributes and values. The set operation union is represented by two pipe symbols (&#8216;||&#8217;), intersection by two ampersand symbols (&#8216;&amp;&amp;&#8217;), difference by two minus symbols (&#8216;&#8211;&#8216;), and complement by a tilde (&#8216;~&#8217;). Parentheses may be used to change the order of operations. The <i>-X</i> argument and query can be used to exclude nodes from the resulting output. A query can be replaced with the <i>-A</i> option to cause <code>nodeattr</code> to print all the nodes listed in the genders database. </p>
<p> When called with a node name (optional) and attribute name, <code>nodeattr</code> returns <i>0</i> to the environment if the node has the attribute; else <i>1</i>. If <i>-v</i> is present, the attribute name and any value (see below) is printed on the standard output. If a node name is not specified, the local host is assumed. </p>
<p> When called with the <i>-Q</i> argument, <code>nodeattr</code> will check if the node name (optional) is met by the attribute and value conditions specified in the query. If the conditions are met, <code>nodeattr</code> returns <i>0</i> to the environment; else <i>1</i>. The query format is identical to the format listed above. If a node name is not specified, the local host is assumed. </p>
<p> The <i>-V</i> option causes <code>nodeattr</code> to print all of the values that exist for a particular attribute. Also specifing <i>-U</i> with <i>-V</i> causes <code>nodeattr</code> to print out only unique values for the particular attribute. </p>
<p> The <i>-l</i> option causes <code>nodeattr</code> to print the attributes of the specified node. If no node is listed, all attributes in the genders file are listed. </p>
<p> The <i>-k</i> option checks the genders file for parse errors and proper formatting. If errors are found, information about the error will be output to standard error. </p>
<p> <code>Nodeattr </code> will always check the default genders file, but a different genders file can be specified with the <i>-f</i> option. </p>
<p> The <i>-d</i> option allows the specified genders database to be compared to the filename indicated by the <i>-f</i> option or the default genders database. The differences contained in the specified database will be output to standard error. </p>
<p> The <i>&#8211;expand</i> option will take a genders database, expand all hostranges, and output a new genders database. The subsequent database will be identical to the first, but every node will be listed on a separate line. This option may be useful for debugging or determining the difference between databases. </p>
<p> The <i>&#8211;compress</i> is opposite of the <i>&#8211;expand</i> option. It will output a new identical genders database with hostranges of nodes with identical attributes. Depending on the setup of your genders database, the resulting database may be longer or shorter. This option may be useful as a beginning step to compressing an existing genders database. </p>
<p> Attribute names may optionally appear in the genders file with an equal sign followed by a value. <code>Nodeattr</code> ignores these values except when the <i>-v </i> option requests that the value, if any, be displayed; and when an attribute is specified on the command line with a value, in which case only an attribute with the specified value in the genders file will match.</p>
<h2>EXAMPLES</h2>
<p> Retrieve a comma separated list of all login nodes:</p>
<dl>
<dt>
<dd> nodeattr -c login</dl>
<p> Retrieve a hostlist formatted list of all login nodes:</p>
<dl>
<dt>
<dd> nodeattr -q login</dl>
<p> Retrieve a comma separated list of nodes with 4 cpus:</p>
<dl>
<dt>
<dd> nodeattr -c cpus=4</dl>
<p> Retrieve a comma separated list of all login and management nodes:</p>
<dl>
<dt>
<dd> nodeattr -c &quot;login||mgmt&quot;</dl>
<p> Retrieve a comma separated list of all login nodes with 4 cpus:</p>
<dl>
<dt>
<dd> nodeattr -c &quot;login&amp;&amp;cpus=4&quot;</dl>
<p> Retrieve a comma separated list of all nodes that are not login or management nodes:</p>
<dl>
<dt>
<dd> nodeattr -c &quot;~(login||mgmt)&quot;</dl>
<p> To use nodeattr with pdsh to run a command on all fddi nodes:</p>
<dl>
<dt>
<dd> pdsh -w`nodeattr -c fddi` command</dl>
<p> To use nodeattr in a ksh script to collect a list of users on login nodes:</p>
<dl>
<dt>
<dd> for i in `nodeattr -n login`; do rsh $i who; done</dl>
<p> To verify whether or not this node is a head node:</p>
<dl>
<dt>
<dd> nodeattr head &amp;&amp; echo yes</dl>
<p> To verify whether or not this node is a head node and ntpserver:</p>
<dl>
<dt>
<dd> nodeattr -Q &quot;head&amp;&amp;ntpserver&quot; &amp;&amp; echo yes</dl>
<h2>FILES</h2>
<p> /etc/genders </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libgenders/">libgenders</a>(3) </p>
<h2>Index</h2>
