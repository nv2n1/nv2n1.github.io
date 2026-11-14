---
title: "condor_who(1)"
name: "condor_who"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_who/"
description: "condor_who Display information about owners of jobs and jobs running on an execute machine"
---

<h2>Name</h2>
<p> <i>condor_who</i> Display information about owners of jobs and jobs running on an execute machine </p>
<h2>Synopsis</h2>
<p> <i>condor_who</i> [ <i>help options</i> ] [ <i>address options</i> ] [ <i>display options</i> ] </p>
<h2>Description</h2>
<p> <i>condor_who</i> queries and displays information about the user that owns the jobs running on a machine. It is intended to be run on an execute machine. </p>
<p> The options that may be supplied to <i>condor_who</i> belong to three groups:</p>
<dl>
<dt>
<dd> * <code>Help options</code> provide information about the <i>condor_who</i> tool.</p>
<dt>
<dd> * <code>Address options</code> allow destination specification for query.</p>
<dt>
<dd> * <code>Display options</code> control the formatting and which of the queried information to display.</dl>
<p> At any time, only one <code>help option</code> and one <code>address option</code> may be specified. Any number of <code>display options</code> may be specified. </p>
<p> <i>condor_who</i> obtains its information about jobs by talking to one or more <i>condor_startd</i> daemons. So, <i>condor_who</i> must identify the command port of any <i>condor_startd</i> daemons. An <code>address option</code> provides this information. If <i>no</i> <code>address option</code> is given on the command line, then <i>condor_who</i> searches using this ordering:</p>
<dl>
<dt>
<dd> 1. A defined value of the environment variable CONDOR_CONFIG specifies the directory where log and address files are to be scanned for needed information.</p>
<dt>
<dd> 2. With the aim of finding all <i>condor_startd</i> daemons, <i>condor_who</i> utilizes the same algorithm it would using the <code>-allpids</code> option. The Linux <i>ps</i> or the Windows <i>tasklist</i> program obtains all PIDs. As Linux root or Windows administrator , the Linux <i>lsof</i> or the Windows <i>netstat</i> identifies open sockets and from there the PIDs of listen sockets. Correlating the two lists of PIDs results in identifying the command ports of all <i>condor_startd</i> daemons.</dl>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> (help option) Display usage information</p>
<dt>
<dd></dl>
<p> <code>-daemons</code></p>
<dl>
<dt>
<dd> (help option) Display information about the daemons running on the specified machine, including the daemon&#8217;s PID, IP address and command port</p>
<dt>
<dd></dl>
<p> <code>-diagnostic</code></p>
<dl>
<dt>
<dd> (help option) Display extra information helpful for debugging</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> (help option) Display PIDs and addresses of daemons</p>
<dt>
<dd></dl>
<p> <code>-address </code> <i>hostaddress</i></p>
<dl>
<dt>
<dd> (address option) Identify the <i>condor_startd</i> host address to query</p>
<dt>
<dd></dl>
<p> <code>-allpids</code></p>
<dl>
<dt>
<dd> (address option) Query all local <i>condor_startd</i> daemons</p>
<dt>
<dd></dl>
<p> <code>-logdir </code> <i>directoryname</i></p>
<dl>
<dt>
<dd> (address option) Specifies the directory containing log and address files that <i>condor_who</i> will scan to search for command ports of <i>condor_start</i> daemons to query</p>
<dt>
<dd></dl>
<p> <code>-pid </code> <i>PID</i></p>
<dl>
<dt>
<dd> (address option) Use the given <i>PID</i> to identify the <i>condor_startd</i> daemon to query</p>
<dt>
<dd></dl>
<p> <code>-long</code></p>
<dl>
<dt>
<dd> (display option) Display entire ClassAds</p>
<dt>
<dd></dl>
<p> <code>-wide</code></p>
<dl>
<dt>
<dd> (display option) Displays fields without truncating them in order to fit screen width</p>
<dt>
<dd></dl>
<p> <code>-format </code> <i>fmt attr</i></p>
<dl>
<dt>
<dd> (display option) Display attribute <i>attr</i> in format <i>fmt</i> . To display the attribute or expression the format must contain a single <a href="/docs/linux/man/3-printf/">printf</a>(3) -style conversion specifier. Attributes must be from the resource ClassAd. Expressions are ClassAd expressions and may refer to attributes in the resource ClassAd. If the attribute is not present in a given ClassAd and cannot be parsed as an expression, then the format option will be silently skipped. %r prints the unevaluated, or raw values. The conversion specifier must match the type of the attribute or expression. %s is suitable for strings such as Name , %d for integers such as LastHeardFrom , and %f for floating point numbers such as LoadAvg . %v identifies the type of the attribute, and then prints the value in an appropriate format. %V identifies the type of the attribute, and then prints the value in an appropriate format as it would appear in the <code>-long</code> format. As an example, strings used with %V will have quote marks. An incorrect format will result in undefined behavior. Do not use more than one conversion specifier in a given format. More than one conversion specifier will result in undefined behavior. To output multiple attributes repeat the <code>-format</code> option once for each desired attribute. Like <a href="/docs/linux/man/3-printf/">printf</a>(3) -style formats, one may include other text that will be reproduced directly. A format without any conversion specifiers may be specified, but an attribute is still required. Include n to specify a line break.</p>
<dt>
<dd></dl>
<p> <code>-autoformat[:rtn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> (display option) Display machine ClassAd attribute values formatted in a default way according to their attribute types. This option takes an arbitrary number of attribute names as arguments, and prints out their values. It is like the <code>-format</code> option, but no format strings are required. It is assumed that no attribute names begin with a dash character, so that the next word that begins with dash is the start of the next option. The <code>autoformat</code> option may be followed by a colon character and formatting qualifiers:</p>
<dt>
<dd> <code>r</code> print unevaluated, or raw values,</p>
<dt>
<dd> <code>t</code> add a tab character before each field instead of the default space character,</p>
<dt>
<dd> <code>n</code> add a newline character after each field,</p>
<dt>
<dd> <code>,</code> add a comma character after each field,</p>
<dt>
<dd> <code>l</code> label each field,</p>
<dt>
<dd> <code>V</code> use %V rather than %v for formatting,</p>
<dt>
<dd> <code>h</code> print headings before the first line of output.</p>
<dt>
<dd> The newline and comma characters may <i>not</i> be used together.</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> <i>Example 1</i> Sample output from the local machine, which is running a single HTCondor job. Note that the output of the PROGRAM field will be truncated to fit the display, similar to the artificial truncation shown in this example output. </p>
<p> % condor_who </p>
<p> OWNER CLIENT SLOT JOB RUNTIME PID PROGRAM<br />
 smith1 [at] crane.cs.wisc.edu crane.cs.wisc.edu 2 320.0 0+00:00:08 7776 D:\scratch
