---
title: "condor_userprio(1)"
name: "condor_userprio"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_userprio/"
description: "condor_userprio Manage user priorities"
---

<h2>Name</h2>
<p> <i>condor_userprio</i> Manage user priorities </p>
<h2>Synopsis</h2>
<p> <i>condor_userprio</i> <code>-help</code> </p>
<p> <i>condor_userprio</i> [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>Edit option</code> ] [ <code>Display options</code> ] [ <code>-inputfile </code> <i>filename</i> ] </p>
<h2>Description</h2>
<p> <i>condor_userprio</i> either modifies priority-related information or displays priority-related information. Displayed information comes from the accountant log, where the <i>condor_negotiator</i> daemon stores historical usage information in the file at $(SPOOL) /Accountantnew.log . Which fields are displayed changes based on command line arguments. <i>condor_userprio</i> with no arguments, lists the active users along with their priorities, in increasing priority order. The <code>-all</code> option can be used to display more detailed information about each user, resulting in a rather wide display, and includes the following columns: </p>
<p> <code>Effective Priority</code></p>
<dl>
<dt>
<dd> The effective priority value of the user, which is used to calculate the user&#8217;s share when allocating resources. A lower value means a higher priority, and the minimum value (highest priority) is 0.5. The effective priority is calculated by multiplying the real priority by the priority factor.</p>
<dt>
<dd></dl>
<p> <code>Real Priority</code></p>
<dl>
<dt>
<dd> The value of the real priority of the user. This value follows the user&#8217;s resource usage.</p>
<dt>
<dd></dl>
<p> <code>Priority Factor</code></p>
<dl>
<dt>
<dd> The system administrator can set this value for each user, thus controlling a user&#8217;s effective priority relative to other users. This can be used to create different classes of users.</p>
<dt>
<dd></dl>
<p> <code>Res Used</code></p>
<dl>
<dt>
<dd> The number of resources currently used.</p>
<dt>
<dd></dl>
<p> <code>Accumulated Usage</code></p>
<dl>
<dt>
<dd> The accumulated number of resource-hours used by the user since the usage start time.</p>
<dt>
<dd></dl>
<p> <code>Usage Start Time</code></p>
<dl>
<dt>
<dd> The time since when usage has been recorded for the user. This time is set when a user job runs for the first time. It is reset to the present time when the usage for the user is reset.</p>
<dt>
<dd></dl>
<p> <code>Last Usage Time</code></p>
<dl>
<dt>
<dd> The most recent time a resource usage has been recorded for the user.</p>
<dt>
<dd></dl>
<p> By default only users for whom usage was recorded in the last 24 hours, or whose priority is greater than the minimum are listed. </p>
<p> The <code>-pool</code> option can be used to contact a different central manager than the local one (the default). </p>
<p> For security purposes of authentication and authorization, specifying an Edit Option requires the ADMINISTRATOR level of access. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Contact the specified <i>centralmanagerhostname</i> with an optional port number, instead of the local central manager. This can be used to check other pools. NOTE: The host name (and optional port) specified refer to the host name (and port) of the <i>condor_negotiator</i> to query for user priorities. This is slightly different than most HTCondor tools that support a <code>-pool</code> option, and instead expect the host name (and port) of the <i>condor_collector</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-inputfile </code> <i>filename</i></p>
<dl>
<dt>
<dd> Introduced for debugging purposes, read priority information from <i>filename</i> . The contents of <i>filename</i> are expected to be the same as captured output from running a condor_userprio -long command.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-delete </code> <i>username</i></p>
<dl>
<dt>
<dd> (Edit option) Remove the specified <i>username</i> from HTCondor&#8217;s accounting.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-resetall</code></p>
<dl>
<dt>
<dd> (Edit option) Reset the accumulated usage of all the users to zero.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-resetusage </code> <i>username</i></p>
<dl>
<dt>
<dd> (Edit option) Reset the accumulated usage of the user specified by <i>username</i> to zero.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-setaccum </code> <i>username value</i></p>
<dl>
<dt>
<dd> (Edit option) Set the accumulated usage of the user specified by <i>username</i> to the specified floating point <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-setbegin </code> <i>username value</i></p>
<dl>
<dt>
<dd> (Edit option) Set the begin usage time of the user specified by <i>username</i> to the specified <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-setfactor </code> <i>username value</i></p>
<dl>
<dt>
<dd> (Edit option) Set the priority factor of the user specified by <i>username</i> to the specified <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-setlast </code> <i>username value</i></p>
<dl>
<dt>
<dd> (Edit option) Set the last usage time of the user specified by <i>username</i> to the specified <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-setprio </code> <i>username value</i></p>
<dl>
<dt>
<dd> (Edit option) Set the real priority of the user specified by <i>username</i> to the specified <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-activefrom </code> <i>month day year</i></p>
<dl>
<dt>
<dd> (Display option) Display information for users who have some recorded accumulated usage since the specified date.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-af[:rtgn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> (Display option) The same as <code>-autoformat</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-all</code></p>
<dl>
<dt>
<dd> (Display option) Display all available fields about each group or user.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-allusers</code></p>
<dl>
<dt>
<dd> (Display option) Display information for all the users who have some recorded accumulated usage.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-autoformat[:rtgn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> (Display option) Modifies the display of information when using the <code>-long</code> option. Implies use of the <code>-modular</code> option and displays ClassAd attribute values formatted in a default way according to their attribute types and with attribute names consistent with the <code>-modular</code> option. This option takes an arbitrary number of attribute names as arguments, and prints out their values. It is assumed that no attribute names begin with a dash character, so that the next word that begins with dash is the start of the next option. Option <code>-autoformat:h</code> gives a tabular output with column headings. The <code>-autoformat</code> option may be followed by a colon character and formatting qualifiers:</p>
<dt>
<dd> <code>r</code> print unevaluated, or raw values,</p>
<dt>
<dd> <code>t</code> add a tab character before each field instead of the default space character,</p>
<dt>
<dd> <code>g</code> inject a newline between ClassAds,</p>
<dt>
<dd> <code>n</code> add a newline character after each field,</p>
<dt>
<dd> <code>,</code> add a comma character after each field,</p>
<dt>
<dd> <code>l</code> label each field,</p>
<dt>
<dd> <code>V</code> use %V formatting, where string values are quoted,</p>
<dt>
<dd> <code>h</code> print headings before the first line of output.</p>
<dt>
<dd> The newline and comma characters may <i>not</i> be used together.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>&lt;expr&gt;</i></p>
<dl>
<dt>
<dd> (Display option) To be used in conjunction with the <code>-long</code> <code>-modular</code> or the <code>-autoformat</code> options. Displays users and groups that match the &lt;expr&gt; .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-debug[:&lt;opts&gt;]</code></p>
<dl>
<dt>
<dd> (Display option) Without <code>:&lt;opts&gt;</code> specified, use configured debug level to send debugging output to stderr . With <code>:&lt;opts&gt;</code> specified, these options are debug levels that override any configured debug levels for this command&#8217;s execution to send debugging output to stderr .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-flat</code></p>
<dl>
<dt>
<dd> (Display option) Display information such that users within hierarchical groups are <i>not</i> listed with their group.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-getreslist </code> <i>username</i></p>
<dl>
<dt>
<dd> (Display option) Display all the resources currently allocated to the user specified by <i>username</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-grouporder</code></p>
<dl>
<dt>
<dd> (Display option) Display submitter information with accounting group entries at the top of the list, and in breadth-first order within the group hierarchy tree.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-grouprollup</code></p>
<dl>
<dt>
<dd> (Display option) For hierarchical groups, the display shows sums as computed for groups, and these sums include sub groups.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-hierarchical</code></p>
<dl>
<dt>
<dd> (Display option) Display information such that users within hierarchical groups are listed with their group.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-legacy</code></p>
<dl>
<dt>
<dd> (Display option) For use with the <code>-long</code> option, displays attribute names and values as a single ClassAd.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-long</code></p>
<dl>
<dt>
<dd> (Display option) A verbose output which displays entire ClassAds.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-modular</code></p>
<dl>
<dt>
<dd> (Display option) Modifies the display when using the <code>-long</code> option, such that attribute names and values are shown as distinct ClassAds.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-most</code></p>
<dl>
<dt>
<dd> (Display option) Display fields considered to be the most useful. This is the default set of fields displayed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-priority</code></p>
<dl>
<dt>
<dd> (Display option) Display fields with user priority information.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-quotas</code></p>
<dl>
<dt>
<dd> (Display option) Display fields relevant to hierarchical group quotas.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-usage</code></p>
<dl>
<dt>
<dd> (Display option) Display usage information for each group or user.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> <i>Example 1</i> Since the output varies due to command line arguments, here is an example of the default output for a pool that does not use Hierarchical Group Quotas. This default output is the same as given with the <code>-most</code> Display option. </p>
<p> Last Priority Update: 1/19 13:14 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Effective&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Priority&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Res&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total Usage&nbsp;<wbr>&nbsp;<wbr>Time Since<br />
 User Name Priority Factor In Use (wghted-hrs) Last Usage<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;-<br />
 www-cndr [at] cs.wisc.edu 0.56 1.00 0 591998.44 0+16:30<br />
 joey [at] cs.wisc.edu 1.00 1.00 1 990.15 &lt;now&gt;<br />
 suzy [at] cs.wisc.edu 1.53 1.00 0 261.78 0+09:31<br />
 leon [at] cs.wisc.edu 1.63 1.00 2 12597.82 &lt;now&gt;<br />
 raj [at] cs.wisc.edu 3.34 1.00 0 8049.48 0+01:39<br />
 jose [at] cs.wisc.edu 3.62 1.00 4 58137.63 &lt;now&gt;<br />
 betsy [at] cs.wisc.edu 13.47 1.00 0 1475.31 0+22:46<br />
 petra [at] cs.wisc.edu 266.02 500.00 1 288082.03 &lt;now&gt;<br />
 carmen [at] cs.wisc.edu 329.87 10.00 634 2685305.25 &lt;now&gt;<br />
 carlos [at] cs.wisc.edu 687.36 10.00 0 76555.13 0+14:31<br />
 ali [at] proj1.wisc.edu 5000.00 10000.00 0 1315.56 0+03:33<br />
 apu [at] nnland.edu 5000.00 10000.00 0 482.63 0+09:56<br />
 pop [at] proj1.wisc.edu 26688.11 10000.00 1 49560.88 &lt;now&gt;<br />
 franz [at] cs.wisc.edu 29352.06 500.00 109 600277.88 &lt;now&gt;<br />
 martha [at] nnland.edu 58030.94 10000.00 0 48212.79 0+12:32<br />
 izzi [at] nnland.edu 62106.40 10000.00 0 6569.75 0+02:26<br />
 marta [at] cs.wisc.edu 62577.84 500.00 29 193706.30 &lt;now&gt;<br />
 kris [at] proj1.wisc.edu 100597.94 10000.00 0 20814.24 0+04:26<br />
 boss [at] proj1.wisc.edu 318229.25 10000.00 3 324680.47 &lt;now&gt;<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;-<br />
 Number of users: 19 784 4969073.00 0+23:59 </p>
<p> <i>Example 2</i> This is an example of the default output for a pool that uses hierarchical groups, and the groups accept surplus. This leads to a very wide display. </p>
<p> % condor_userprio -pool crane.cs.wisc.edu -allusers<br />
 Last Priority Update: 1/19 13:18<br />
 Group Config Use Effective Priority Res Total Usage Time Since </p>
<p>&nbsp;<wbr>&nbsp;<wbr>User Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Quota&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Surplus&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Priority&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Factor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>In Use&nbsp;<wbr>(wghted-hrs)&nbsp;<wbr>Last Usage<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;-<br />
 &lt;none&gt; 0.00 yes 1.00 0 6.78 9+03:52 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>johnsm [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6.62&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9+19:42 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>John.Smith [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9+03:52 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sedge [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.05&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13+03:03 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Duck [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>31+00:28 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>other [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.04&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16+03:42<br />
 Duck 2.00 no 1.00 0 0.02 13+02:57 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>goose [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13+02:57<br />
 Sedge 4.00 no 1.00 0 0.17 9+03:07 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>johnsm [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9+03:08 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Half [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>31+00:02 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>John.Smith [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.05&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9+03:07 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>other [at] crane.cs.wisc.edu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>28+19:34<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212;- &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212; &#8212;&#8212; &#8212;&#8212;&#8212;&#8212; &#8212;&#8212;&#8212;-<br />
 Number of users: 10 ByQuota 0 6.97 </p>
<h2>Exit Status</h2>
<p> <i>condor_userprio</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
