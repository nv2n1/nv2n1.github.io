---
title: "nget(1)"
name: "nget"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nget/"
description: "nget – retrieve files from NNTP (usenet news) hosts"
---

<h2>NAME</h2>
<p> nget &#8211; retrieve files from NNTP (usenet news) hosts</p>
<h2>SYNOPSIS</h2>
<p> <code>nget [&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>nget</code> retrieves messages matching a regular expression, and decodes any files contained within. Multipart messages are automatically pieced together. Parts from multiple servers will be combined if needed.</p>
<h2>OPTIONS</h2>
<p> The order options are specified is significant. In general, an option will only affect options that come after it on the command line. </p>
<dl>
<dt>-q/&#8211;quiet</p>
<dd> When specified once, will disable printing of auto-updating text to allow the output to be redirected/logged without garbage in it. When specified twice, will disable printing of merely informative messages. Errors will still be printed.</p>
<dt>-h/&#8211;host host</p>
<dd> Force only the given host to be used for subsequent commands. (Must be configured in .ngetrc.) Can reset to standard auto-choosing method with -h &quot;&quot;</p>
<dt>-a/&#8211;available</p>
<dd> Update the list of available newsgroups. Subsequent -r/-R commands can be use to search for newsgroups.</p>
<dt>-A/&#8211;quickavailable</p>
<dd> Like -a/&#8211;available, but does not update the list, only makes it available for searching.</p>
<dt>-X/&#8211;xavailable</p>
<dd> Search the group list, but without loading cache file or retrieving full group list. Instead, the search will be done on the server. Compared to -a/-A this has the advantage of not requiring any disk space for cache files, and not requiring the initial retrieval of the full group list. The disadvantages are not all servers supporting the required NNTP extensions, the inability to use complex regexs due to the need to convert it to the simpler wildmat format, and the possibility that the commands can be quite slow if the server is overloaded (you may need to increase the timeout value in some cases).</p>
<dt>-g/&#8211;group group(s)</p>
<dd> Update the list of available files in group(s). Multiple groups can be specified by seperating them with commas. All cached groups can be selected with &quot;*&quot;. If a host has been specified before with -h, it will retrieve headers only from that host. Otherwise it will retrieve headers for all hosts above _glevel (see configuration section for more info on priorities.) Subsequent -r/-R commands can be used to retrieve files.</p>
<dt>-G/&#8211;quickgroup group(s)</p>
<dd> Like &#8211;group, but does not retrieve new headers.</p>
<dt>-x/&#8211;xgroup group(s)</p>
<dd> Use group(s) for subsequent -r commands, but without loading cache file or retrieving full header list. Instead, the XPAT command will used to retrieve only the matching headers. Compared to -g/-G this has the advantage of not requiring any disk space for cache files, and not requiring the initial retrieval of the full header list. The disadvantages are not all servers supporting XPAT, the inability to use complex regexs due to the need to convert it to the simpler wildmat format, and the possibility that the xpat command can be quite slow if the server is overloaded (you may need to increase the timeout value in some cases).</p>
<dt>-F/&#8211;flushserver host</p>
<dd> Following -g/-G: Flush all headers for server from current group(s).<br />
 Following -a/-A: Flush all groups/descriptions for server from grouplist.</p>
<dt>-r/&#8211;retrieve regex</p>
<dd> Following -g/-G/-x: Matches regex against subjects of previously selected group(s), and retrieves ones that match.<br />
 Following -a/-A: Matches regex against newsgroup names and descriptions and lists ones that match. (-T required)</p>
<dt>-R/&#8211;expretrieve expression</p>
<dd> Like -r, but matches expression instead of merely a regexp. (see EXPRETRIEVE EXPRESSIONS section for more info.) Expression is a postfix expression that can contain these keywords:<br />
 Following -g/-G: subject, author, lines, bytes, have, req, date, age, update, updateage, messageid(or mid), references. Note that the &#8211;limit argument does not affect the option, if you want to limit based on number of lines, add it as part of the expression.<br />
 Following -a/-A: group, desc.</p>
<dt>-@/&#8211;list LISTFILE</p>
<dd> Specify a file to load a list of command line args from. Looks in ~/.nget5/lists/ dir by default. A # char in a listfile that is the first character on a line or is preceeded by whitespace and not quoted starts a comment which lasts until the end of the line.</p>
<dt>-p/&#8211;path DIRECTORY</p>
<dd> Path to store subsequent retrieves. Also sets -P, and clears previously specified dupepaths. Relative to path which nget was started in. (Except in the case of inside a -@, which will be relative to the cwd at the time of the -@.)</p>
<dt>-P/&#8211;temppath DIRECTORY</p>
<dd> Store temporary files in path instead of the current dir.</p>
<dt>&#8211;dupepath DIRECTORY</p>
<dd> Check for dupe files from specified path in addition to normal path. Can be specified multiple times.</p>
<dt>-m/&#8211;makedirs no,yes,ask,&lt;max # of directory levels to create&gt;</p>
<dd> Make dirs specified by -p and -P. Default is no. If yes, will make dirs automatically. If #, if the number of directories that would need to be created is greater than the number given, the answer will be interpreted as no. If ask, nget will prompt the user when trying to change to a dir that does not exist. Valid responses to the prompt are y[es], n[o], and a max number of directory levels to create. (This means that if you get in the habit of answering &quot;1&quot; rather than &quot;y&quot;, and one day typo the first portion of a path you won&#8217;t accidentally create a bunch of dirs in the wrong place.)</p>
<dt>-T/&#8211;testmode</p>
<dd> Causes &#8211;retrieve to merely print out all matching files.</p>
<dt>&#8211;text ignore,files,mbox[:filename]</p>
<dd> Specifies how to handle text posts. The default is files. OPT can be ignore to save only binaries, &quot;files&quot; to save each text post in a different file, and &quot;mbox&quot; to save each text post as a message in a mbox format mailbox. The name of the mbox file to save in can be specified with mbox:filename, the default is nget.mbox. If the filename ends in .gz, it will automatically be gzipped. Unless the filename has an absolute path, it is interpreted as relative to the retrieve path.</p>
<dt>&#8211;save-binary-info yes,no</p>
<dd> Specifies whether to save text messages for posts that contained only binary data. (If you want to see the headers.)</p>
<dt>&#8211;test-multiserver OPT</p>
<dd> Causes testmode to display which servers have parts of each file. OPT may be no to disable(default), long for a verbose output, and short for a more condensed form. (In short mode, the shortname of each server is printed with no seperating space, and it is upper-cased if that server does not have all the parts. If the server has no shortname specified, it defaults to the first char of the server alias.)</p>
<dt>&#8211;fullxover OPT</p>
<dd> Override the fullxover settings of the config file. The default is -1, which doesn&#8217;t override.</p>
<dt>-M/&#8211;mark</p>
<dd> Mark matched files as retrieved.</p>
<dt>-U/&#8211;unmark</p>
<dd> Unmark matched files as retrieved. (Automatically sets -dI)</p>
<dt>-t/&#8211;tries int</p>
<dd> Set maximum number of retries. -1 will retry indefinatly (probably not a good idea).</p>
<dt>-l/&#8211;limit int</p>
<dd> Set the minimum number of lines a message (or total number of lines for a multi-part message) must have to be considered for retrieval.</p>
<dt>-L/&#8211;maxlines int</p>
<dd> Set the maximum number of lines a message must have to be considered for retrieval. (-1 for unlimited)</p>
<dt>-s/&#8211;delay int</p>
<dd> Set the number of seconds to wait between retry attempts.</p>
<dt>&#8211;timeout int</p>
<dd> Set the number of seconds to wait for a reply from the nntp server before giving up.</p>
<dt>-i/&#8211;incomplete</p>
<dd> Retrieve files with missing parts.</p>
<dt>-I/&#8211;complete</p>
<dd> Retrieve only files with all parts.</p>
<dt>&#8211;decode</p>
<dd> Decode and delete temp files (default)</p>
<dt>-k/&#8211;keep</p>
<dd> Decode and keep temp files.</p>
<dt>-K/&#8211;no-decode</p>
<dd> Keep temp files, and don&#8217;t try to decode them.</p>
<dt>-c/&#8211;case</p>
<dd> Match case sensitively.</p>
<dt>-C/&#8211;nocase</p>
<dd> Match case insensitively.</p>
<dt>&#8211;autopar</p>
<dd> Enable automatic parfile handling. (default) Only download as many par files as needed to replace missing or corrupt files.</p>
<dt>&#8211;no-autopar</p>
<dd> Disable automatic parfile handling. All parfiles that match the expression will be downloaded.</p>
<dt>-d/&#8211;dupecheck FLAGS</p>
<dd> Check to make sure you don&#8217;t already have files. This is done in two ways. The first (&quot;f&quot;) is by compiling a list of all files in the current directory, then checking against all messages to be retrieved to see if one of the filenames shows up in the subject. This works reasonably well, though sometimes the filename isn&#8217;t in the subject. It can also cause problems if you happen to have files in the directory named silly things like &quot;a&quot;, in which case all messages with the word &quot;a&quot; in them will be skipped. However, it is still smart enough not to skip messages that merely have a word containing &quot;a&quot;.<br />
 The second method (&quot;i&quot;) is by setting a flag in the header cache that will prevent it from being retrieved again. You can use combos such as -dfi to check both, -dFi to only check the flag, -dfI to only check files, etc.<br />
 The third (&quot;m&quot;) will cause files that are found by the dupe file check (&quot;f&quot;) to be marked as retrieved in the cache. (Useful for handling crossposted binaries and/or binaries saved with another newsreader.)</p>
<dt>-D/&#8211;nodupecheck</p>
<dd> Don&#8217;t check either of the &#8211;dupecheck methods, retrieve any messages that match.</p>
<dt>-N/&#8211;noconnect</p>
<dd> Do not connect to any server for retrieving articles. Useful for trying to decode as much as you have. (if you got stuff with -K or ngetlite.)</p>
<dt>-w/&#8211;writelite LITEFILE</p>
<dd> Write a list of parts to retrieve with ngetlite.</p>
<dt>&#8211;help</p>
<dd> Show help.</dl>
<h2>EXPRETRIEVE EXPRESSIONS</h2>
<p> Expressions are in postfix order. For the int, date, and age types, standard int comparisons are allowed (==, !=, &lt;, &lt;=, &gt;, &gt;=). For regex types, ==(=~), !=(!~) are allowed. Thus a comparison would take the following form:<br />
 Infix: &lt;keyword&gt; &lt;operator&gt; &lt;value&gt; Postfix: &lt;keyword&gt; &lt;value&gt; &lt;operator&gt; Comparisons can be joined with &amp;&amp;(and), ||(or).<br />
 Infix: &lt;comparison&gt; &amp;&amp; &lt;comparison&gt; Postfix: &lt;comparison&gt; &lt;comparison&gt; &amp;&amp;</p>
<h3>-g/-G keywords</h3>
<dl>
<dt>subject (regex)</p>
<dd> Matches the Subject: header.</p>
<dt>author (regex)</p>
<dd> Matches the From: header.</p>
<dt>lines (int)</p>
<dd> Matches the Lines: header.</p>
<dt>bytes (int)</p>
<dd> Matches the length of the message in bytes</p>
<dt>have (int)</p>
<dd> Matches the number of parts of a multipart file that we have.</p>
<dt>req (int)</p>
<dd> Matches the total number of parts of a multipart file.</p>
<dt>date (date)</p>
<dd> Matches the Date: header. All the standard formats are accepted.</p>
<dt>age (age)</p>
<dd> Matches the time since the Date: header.<br />
 Format: [X y[ears]] [X mo[nths]] [X w[eeks]] [X d[ays]] [X h[ours]] [X m[inutes]] [X s[econds]]<br />
 Ex.: &quot;6 months 7 hours 8 minutes&quot;<br />
 Ex.: &quot;6mo7h8m&quot;</p>
<dt>update (date)</p>
<dd> Matches the &quot;update time&quot; of the cache item. That is, the most recent time that a new part of the file has been added. For example, if part 1 was added one day, and part 2 only appeared on the server the next day, then the update time would be when part 2 was added on the second day. But if both parts were seen on the first day, then seen again from a different server on the second day, the update time would stay at the original value.</p>
<dt>updateage (age)</p>
<dd> Matches the time since the update of the cache item.</p>
<dt>messageid (regex), mid (regex)</p>
<dd> Matches the Message-ID header. (For multi-part posts, it matches the message-id of the first part.)</p>
<dt>references (regex)</p>
<dd> Matches any of the message&#8217;s References.</dl>
<h3>-a/-A keywords</h3>
<dl>
<dt>group (regex)</p>
<dd> Matches the newsgroup name.</p>
<dt>desc (regex)</p>
<dd> Matches the newsgroup description.</dl>
<h2>CONFIGURATION</h2>
<p> Upon startup, nget will read ~/.nget5/.ngetrc for default configuration values and host/group aliases. An example .ngetrc should have been included with nget. nget will also check ~/_nget5/ and _ngetrc if needed, to handle OS and filesystems that can&#8217;t (or won&#8217;t) handle files starting with a period. Options are specified one per line in the form:</p>
<dl>
<dt>
<dd> <code>key=value</code></dl>
<p> Values may be strings(any sequence of characters ending in a newline, not quoted), integers(whole numbers), floats(decimal numbers), boolean(0=false/1=true). Subsections are specified in the form:</p>
<dl>
<dt>
<dd> <code>{section_name</code></p>
<dl>
<dt>
<dd> <code>data</code></dl>
<p> <code>}</code></dl>
<p> where data is any number of options.</p>
<h3>Global Configuration Options</h3>
<dl>
<dt>limit (int, default=0)</p>
<dd> Default value for -l/&#8211;limit</p>
<dt>tries (int, default=20)</p>
<dd> Default value for -t/&#8211;tries</p>
<dt>delay (int, default=1)</p>
<dd> Default value for -s/&#8211;delay</p>
<dt>usegz (int, default=-1)</p>
<dd> Default gzip compression level to use for cache/midinfo files (can be overridden on a per-group basis). Acceptable values are -1=zlib default, 0=uncompressed, and 1-9.</p>
<dt>timeout (int, default=180)</p>
<dd> Seconds to wait for a reply from the nntp server before giving up.</p>
<dt>maxstreaming (int, default=64)</p>
<dd> Sets how many xover commands will be sent at once, when using fullxover. maxstreaming=0 will disable streaming. Note that setting maxstreaming too high can cause your connection to deadlock if the write buffer is filled up and the write command blocks, but the server will never read more commands since it is waiting for us to read what it has already sent us.</p>
<dt>maxconnections (int, default=-1)</p>
<dd> Maximum number of connections to open at once, -1 to allow unlimited open connections. When reached, the servers used least recently will be disconnected first. (Note that regardless of this setting, nget never opens more than one connection per server.)</p>
<dt>idletimeout (int, default=300)</p>
<dd> Max seconds to keep an idle connection to a nntp server open.</p>
<dt>curservmult (float, default=2.0)</p>
<dd> Priority multiplier given to servers which are currently connected. This can be used to avoid excessive server switching. (Set to 1.0 if you want to disable it.)</p>
<dt>penaltystrikes (int, default=3)</p>
<dd> Number of consecutive connect errors before penalizing a server, -1 to disable penalization.</p>
<dt>initialpenalty (int, default=180)</p>
<dd> Number of seconds to ignore a penalized server for.</p>
<dt>penaltymultiplier (float, default=2.0)</p>
<dd> Multiplier for penalty time for each time the penalty time runs out and the server continues to be down.</p>
<dt>case (boolean, default=0)</p>
<dd> Default for regex case sensitivity. (0=-C/&#8211;nocase, 1=-c/&#8211;case)</p>
<dt>complete (boolean, default=1)</p>
<dd> Default for incomplete file filter. (0=-i/&#8211;incomplete, 1=-I/&#8211;complete)</p>
<dt>dupeidcheck (boolean, default=1)</p>
<dd> Default for already downloaded file filter. (0=-dI, 1=-di)</p>
<dt>dupefilecheck (boolean, default=1)</p>
<dd> Default for duplicate file filter. (0=-dF, 1=-df)</p>
<dt>autopar (boolean, default=1)</p>
<dd> Default for automatic par handling. (0=&#8211;no-autopar, 1=&#8211;autopar)</p>
<dt>autopar_optimistic (boolean, default=0)</p>
<dd> One problem with automatic par handling, is that sometimes people do multi-day posts and post the par files first. If autopar_optimistic is enabled, it will assume that when there aren&#8217;t enough .pxx files, that it must just be a multi-day post and will not grab any pxx files. If autopar_optimistic is off, it grab all the pxx files so that if they expire before more are posted, we will already have them.</p>
<dt>quiet (boolean, default=0)</p>
<dd> Default for quiet option. (0=normal, 1=-q)</p>
<dt>tempshortnames (boolean, default=0)</p>
<dd> 1=Use 8.3 tempfile names (for old dos partitions, etc), 0=Use 17.3 tempfile names</p>
<dt>fatal_user_errors (boolean, default=0)</p>
<dd> Makes user/path errors cause an immediate exit rather than continuing if possible.</p>
<dt>unequal_line_error (boolean, default=0)</p>
<dd> If set, downloaded articles whose actual number of lines does not match the expected value will be regarded as an error and ignored. If 0, a warning will be generated but the article will be accepted.</p>
<dt>fullxover (int, default=0)</p>
<dd> Controls whether nget will check for articles added or removed out of order when updating header cache. fullxover=0 will follow the nntp spec and assume articles are always added and removed in the correct order. fullxover=1 will assume articles may be added out of order, but are still removed in order. fullxover=2 handles articles being added and removed in any order.</p>
<dt>makedirs (special, default=no)</p>
<dd> Create non-existant directories specified by -p/-P? (yes/no/ask/#)</p>
<dt>test_multiserver (special, default=no)</p>
<dd> Display multiserver file complition info in testmode output? (no=no, short=show shortname of each server that has parts of the file, lowercase when complete and uppercase when that server only has some parts, long=show fullname of each server along with a count of how many parts it has if it does not have them all.)</p>
<dt>text (special, default=files)</p>
<dd> Default for the &#8211;text option (possible values are ignore,files,mbox[:filename]).</p>
<dt>save_binary_info (boolean, default=0)</p>
<dd> Default for the &#8211;save-binary-info option.</p>
<dt>cachedir (string)</p>
<dd> Specifies a different location to store cache files. Could be used to share a single cache dir between a trusted group of users, to reduce HD/bandwidth usage, while still allowing each user to have their own config/midinfo files.)</dl>
<h3>Host Configuration</h3>
<p> Host configuration is done in the halias section, with a subsection for each host containing its options:</p>
<dl>
<dt>address (string, required)</p>
<dd> Address of the server, with optional port number seperated by a colon. To specify a literal IPv6 address with a port number, use the format &quot;[address]:port&quot;.</p>
<dt>id (int, required)</p>
<dd> An identifier for this server. The id uniquely identifies a certain set of header cache data. You may specify the same id in more than one host, for example if you have multiple accounts on a server to avoid to storing the same cache data multiple times. The id should not be changed after you have used it. Must be greater than 0 and less than ULONG_MAX. (usually 4294967295).</p>
<dt>shortname (string, default=first character of host alias)</p>
<dd> The shortname to use for this server.</p>
<dt>user (string)</p>
<dd> Username for the server, if it requires authorization.</p>
<dt>pass (string)</p>
<dd> Password for the server, if it requires authorization.</p>
<dt>fullxover (int)</p>
<dd> Override global fullxover setting for this server only.</p>
<dt>maxstreaming (int)</p>
<dd> Override global maxstreaming setting for this server only.</p>
<dt>idletimeout (int)</p>
<dd> Override global idletimeout setting for this server only.</p>
<dt>linelenience (special, default=0)</p>
<dd> The linelenience option may be specified as either a single int, or two ints seperated by a comma. If only a single int, X is specified, then it will be interpeted as shorthand for &quot;-X,+X&quot;. These values specify the ammount that the real (recieved) number of lines (inclusive) for an article may deviate from the values returned by the server in the header listings. For example, &quot;-1,2&quot; means that the real number of lines may be one less than, equal to, one greater than, or two greater than the expected amount. For example, the following host section defines a single host &quot;host1&quot;, with nntp authentication for user &quot;bob&quot;, password &quot;something&quot;, and the fullxover option enabled.</p>
<dl>
<dt>
<dd> <code>{halias</code></p>
<dl>
<dt>
<dd> <code>{host1</code></p>
<dl>
<dt>
<dd> <code>addr=news.host1.com</code><br />
 <code>id=3838</code><br />
 <code>user=bob</code><br />
 <code>pass=something</code><br />
 <code>fullxover=1</code><br />
 <code>linelenience=-1,2</code></dl>
<p> <code>}</code></dl>
<p> <code>}</code></dl>
</dl>
<h3>Server Priority Configuration</h3>
<p> Multiserver priorities are defined in the hpriority section. Multiple priority groups can be made, and different newsgroups can be configured to use their own priority grouping, or they will default to the &quot;default&quot; group. The -a option will use the &quot;_grouplist&quot; priority group if it exists, otherwise it will use the &quot;default&quot; group. The hpriority section contains a subsection for each priority group, with data items of server=prio-multiplier, and the special items _level=float and _glevel=float. _level sets the priority level assigned to any host not listed in the group, and _glevel sets the required priority needed for -g and -a to automatically use that host. Both _level and _glevel default to 1.0 if not specified. The priority group &quot;trustsizes&quot; also has special meaning, and is used to choose which servers reporting of article line/byte counts to trust when reporting to the user. For example, the following section defines the default priority group and the trustsizes priority group. If all hosts have a certain article, goodhost will be most likely to be chosen, and badhost least likely. It also sets the default priority level to 1.01, meaning any hosts not listed in this group will have a priority of 1.01. When using -g without first specifying a host, only those with prios 1.2 or above will be selected.</p>
<dl>
<dt>
<dd> <code>{hpriority</code></p>
<dl>
<dt>
<dd> <code>{default</code></p>
<dl>
<dt>
<dd> <code>_level=1.01</code><br />
 <code>_glevel=1.2</code><br />
 <code>host1=1.9</code><br />
 <code>goodhost=2.0</code><br />
 <code>badhost=0.9</code></dl>
<p> <code>}</code><br />
 <code>{trustsizes</code></p>
<dl>
<dt>
<dd> <code>goodhost=5.0</code><br />
 <code>badhost=0.1</code></dl>
<p> <code>}</code></dl>
<p> <code>}</code></dl>
<h3>Newsgroup Alias Configuration</h3>
<p> Newsgroup aliases are defined in the galias section. An alias can be a simple alias=fullname data item, or a subsection containing group=, prio=, and usegz= items. The per-group usegz setting will override the global setting. An alias can also refer to multiple groups (either fullnames or further aliases). For example, the following galias section defines an alias of &quot;abpl&quot; for the group &quot;alt.binaries.pictures.linux&quot;, &quot;chocobo&quot; for the group &quot;alt.chocobo&quot;, and ospics for both alt.binaries.pictures.linux and alt.binaries.pictures.freebsd. In addition, the chocobo group is assigned to use the chocoprios priority grouping when deciding what server to retrieve from.</p>
<dl>
<dt>
<dd> <code>{galias</code></p>
<dl>
<dt>
<dd> <code>abpl=alt.binaries.pictures.linux</code><br />
 <code>{chocobo</code></p>
<dl>
<dt>
<dd> <code>group=alt.chocobo</code><br />
 <code>prio=chocoprios</code></dl>
<p> <code>}</code><br />
 <code>ospics=abpl,alt.binaries.pictures.freebsd</code></dl>
<p> <code>}</code></dl>
<h2>EXIT STATUS</h2>
<p> On exit, nget will display a summary of the run. The summary is split into three parts: </p>
<dl>
<dt>OK</p>
<dd> Lists successful operations.</p>
<dl>
<dt>
<dd>
<dl>
<dt>total</p>
<dd> Total number of &quot;logical messages&quot; retrieved (after joining parts).</p>
<dt>uu</p>
<dd> Number of uuencoded files.</p>
<dt>base64</p>
<dd> Number of Base64 (Mime) files.</p>
<dt>XX</p>
<dd> Number of xxencoded files.</p>
<dt>binhex</p>
<dd> Number of Binhex encoded files.</p>
<dt>plaintext</p>
<dd> Number of plaintext files saved.</p>
<dt>qp</p>
<dd> Number of Quoted-Printable encoded files.</p>
<dt>yenc</p>
<dd> Number of yEncoded files.</p>
<dt>dupe</p>
<dd> Number of decoded files that were exact dupes of existing files, and thus deleted.</p>
<dt>skipped</p>
<dd> Number of files that were queued to download but turned out to be dupes after decoding earlier parts and comparing their filenames to the subject line. (Same method thats used for the dupe file check when queueing them up, just that the filename(s) of any decoded files cannot be known until they are downloaded, so some of the checking must occur during the run rather than at queue time.)</p>
<dt>group</p>
<dd> Number of groups successfully updated.</p>
<dt>grouplist</p>
<dd> Newsgroup list successfully updated.</p>
<dt>autopar</p>
<dd> Number of parity sets that are complete.</dl>
</dl>
<dt>WARNINGS</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>group</p>
<dd> Updating group info failed for some (but not all) attempted servers.</p>
<dt>xover</p>
<dd> Weird things happened while updating group info.</p>
<dt>grouplist</p>
<dd> Updating newsgroup list failed for some (but not all) attempted servers.</p>
<dt>retrieve</p>
<dd> Article retrieval failed for some (but not all) attempted servers.</p>
<dt>undecoded</p>
<dd> Articles were not decoded (usually because -K was used).</p>
<dt>unequal_line_count</p>
<dd> Some articles retrieved had different line counts than the server said they should. (And unequal_line_error is set to 0).</p>
<dt>dupe</p>
<dd> Number of decoded files that had the same name as existing files, but different content.</p>
<dt>autopar</p>
<dd> Weirdness encountered reading par files, such as encountering unknown par versions, or non-ascii filenames in the pars.</dl>
</dl>
<dt>ERRORS</p>
<dd> Lists errors that occured. In addition, the exit status will be set to a bitwise OR of the codes of all errors that occured. (Note that some errors share an exit code, since there are only 8 bits available.)</p>
<dl>
<dt>
<dd>
<dl>
<dt>decode (exit code 1)</p>
<dd> Number of file decoding errors.</p>
<dt>autopar (exit code 2)</p>
<dd> Number of parity sets that could not be completed.</p>
<dt>path (exit code 4)</p>
<dd> Errors changing to paths specified with -p or -P.</p>
<dt>user (exit code 4)</p>
<dd> User errors, such as trying -r without specifying a group first.</p>
<dt>retrieve (exit code 8)</p>
<dd> Number of times article retrieval failed for all attempted servers.</p>
<dt>group (exit code 16)</p>
<dd> Number of times header retrieval failed for all attempted servers.</p>
<dt>grouplist (exit code 32)</p>
<dd> Number of times newsgroup list retrieval failed for all attempted servers.</p>
<dt>fatal (exit code 128)</p>
<dd> Error preventing further operation, such as &quot;No space left on device&quot;.</p>
<dt>other (exit code 64)</p>
<dd> Any other kind of error.</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<p> The simplest possible example. Retrieve and decode everything from alt.binaries.test that you haven&#8217;t already gotten before:<br />
 <code>nget -g alt.binaries.test -r &quot;&quot;</code> get listing of all files matching penguin.*png from alt.binaries.pictures.linux (note this is a regex, equivilant to standard shell glob of penguin*png.. see the <a href="/docs/linux/man/7-regex/">regex</a>(7) or grep manpage for more info on regular expressions.)<br />
 <code>nget -g alt.binaries.pictures.linux -DTr &quot;penguin.*png&quot;</code> retrieve all the ones that have more than 50 lines:<br />
 <code>nget -g alt.binaries.pictures.linux -l 50 -r &quot;penguin.*png&quot;</code> equivilant to above, using -R:<br />
 <code>nget -g alt.binaries.pictures.linux -R &quot;lines 50 &gt; subject penguin.*png == &amp;&amp;&quot;</code><br />
 (basically (lines &gt; 50) &amp;&amp; (subject == penguin.*png)) flush all headers from host goodhost in group alt.binaries.pictures.linux:<br />
 <code>nget -Galt.binaries.pictures.linux -Fgoodhost</code> retrieve/update group list, and list all groups with &quot;linux&quot; in the name or description:<br />
 <code>nget -a -Tr linux</code> equivilant to above, using -R:<br />
 <code>nget -a -TR &quot;group linux == desc linux == ||&quot;</code> flush all groups from host goodhost in grouplist:<br />
 <code>nget -A -Fgoodhost</code></p>
<h2>NOTES</h2>
<p> Running multiple copies of nget at once should be safe. It uses file locking, so there should be no way for the files to actually get corrupted. However if you have two ngets doing a -g on the same group at the same time, it would duplicate the download for both processes. If you are using -G there is no problem at all. (Theoretically you might be able to cause some sort of problems by downloading the same files from the same group in the same directory at the same time..)</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>HOME</p>
<dd> Where to put .nget5 directory. (put nget files $HOME/.nget5/)</p>
<dt>NGETHOME</p>
<dd> Override HOME var (put nget files in $NGETHOME)</p>
<dt>NGETCACHE</p>
<dd> Override HOME/NGETHOME vars and .ngetrc cachedir option (put nget cache files in $NGETCACHE)</p>
<dt>NGETRC</p>
<dd> Alternate configuration file to use.</dl>
<h2>FILES</h2>
<dl>
<dt>~/.nget5/</p>
<dd> All configuration and cache files are stored here. Changed to .nget5/ because cache format changed in nget 0.27. (The 5 in the directory name is for file format version 5, not nget version 5.) To upgrade a .nget4 directory to .nget5, simply run &quot;mv ~/.nget4 ~/.nget5 ; rm ~/.nget5/*,cache*&quot;</p>
<dt>~/.nget5/.ngetrc</p>
<dd> Configuration file. If you store authentication information here, be sure to set it readable only by owner.</p>
<dt>~/_nget5/_ngetrc</p>
<dd> Alternate location, use this if you can&#8217;t create a dir/file starting with a period.</p>
<dt>~/.nget5/lists/</p>
<dd> Default directory for listfiles.</dl>
<h2>AUTHOR</h2>
<p> Matthew Mueller &lt;donut AT dakotacom.net&gt; The latest version, and other programs I have written, are available from:<br />
 <a rel="nofollow" href="http://www.dakotacom.net/~donut/programs/">http://www.dakotacom.net/~donut/programs/</a></p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Frank Pilhofer, author of uulib, which nget depends upon for uudecoding the files once they are downloaded. <a rel="nofollow" href="http://www.fpx.de/fp/Software/UUDeview/">http://www.fpx.de/fp/Software/UUDeview/</a> Peter Brian Clements, author of par2-cmdline, which nget uses a stripped down version of for its par2 checking. <a rel="nofollow" href="http://parchive.sourceforge.net/">http://parchive.sourceforge.net/</a> The Unix-socket-faq, which my url for has gone bad, but is supposedly posted monthly on comp.unix.programmer. Beej&#8217;s Guide to Network Programming at <a rel="nofollow" href="http://www.ecst.csuchico.edu/~beej/guide/net/">http://www.ecst.csuchico.edu/~beej/guide/net/</a> Jean-loup Gailly and Mark Adler, for the zlib library.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ngetlite/">ngetlite</a></code>(1), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) </p>
<h2>Index</h2>
