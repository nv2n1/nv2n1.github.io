---
title: "bugzilla(1)"
name: "bugzilla"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bugzilla/"
description: "bugzilla – command-line interface to Bugzilla over XML-RPC"
---

<h2>NAME</h2>
<p> bugzilla &#8211; command-line interface to Bugzilla over XML-RPC</p>
<h2>SYNOPSIS</h2>
<p> <code>bugzilla</code> [<i>options</i>] [<i>command</i>] [<i>command-options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>bugzilla</code> is a command-line utility that allows access to the XML-RPC interface provided by Bugzilla. </p>
<p> <i>command</i> is one of:<br />
 <i></i> * login &#8211; log into the given bugzilla instance<br />
 <i></i> * new &#8211; create a new bug<br />
 <i></i> * query &#8211; search for bugs matching given criteria<br />
 <i></i> * modify &#8211; modify existing bugs<br />
 <i></i> * attach &#8211; attach files to existing bugs, or get attachments<br />
 <i></i> * info &#8211; get info about the given bugzilla instance</p>
<h2>GLOBAL OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>&#8211;help, -h</p>
<dd> show this help message and exit</p>
<dt>&#8211;bugzilla=BUGZILLA</p>
<dd> bugzilla XMLRPC URI. default: <a rel="nofollow" href="https://bugzilla.redhat.com/xmlrpc.cgi">https://bugzilla.redhat.com/xmlrpc.cgi</a></p>
<dt>&#8211;nosslverify</p>
<dd> Don&#8217;t error on invalid bugzilla SSL certificate</p>
<dt>&#8211;user=USER</p>
<dd> Optional bugzilla login username</p>
<dt>&#8211;password=PASSWORD</p>
<dd> Optional bugzilla login password</p>
<dt>&#8211;login</p>
<dd> Run interactive &quot;login&quot; before performing the specified command.</p>
<dt>&#8211;ensure-logged-in</p>
<dd> Raise an error if we aren&#8217;t logged in to bugzilla. Consider using this if you are depending on cached credentials, to ensure that when they expire the tool errors, rather than subtly change output.</p>
<dt>&#8211;no-cache-credentials</p>
<dd> Don&#8217;t save any bugzilla cookies or tokens to disk, and don&#8217;t use any pre-existing credentials.</p>
<dt>&#8211;cookiefile=COOKIEFILE</p>
<dd> cookie file to use for bugzilla authentication</p>
<dt>&#8211;tokenfile=TOKENFILE</p>
<dd> token file to use for bugzilla authentication</p>
<dt>&#8211;verbose</p>
<dd> give more info about what&#8217;s going on</p>
<dt>&#8211;debug</p>
<dd> output bunches of debugging info</dl>
<h2>&#8216;NEW&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;product=PRODUCT, -p PRODUCT</p>
<dd> REQUIRED: product name</p>
<dt>&#8211;version=VERSION, -v VERSION</p>
<dd> REQUIRED: product version</p>
<dt>&#8211;component=COMPONENT, -c COMPONENT</p>
<dd> REQUIRED: component name</p>
<dt>&#8211;sub-component=SUB_COMPONENT</p>
<dd> Optional sub component name</p>
<dt>&#8211;short_desc=SUMMARY, &#8211;summary=SUMMARY, -s SUMMARY</p>
<dd> REQUIRED: bug summary</p>
<dt>&#8211;comment=DESCRIPTION, -l DESCRIPTION</p>
<dd> initial bug comment</p>
<dt>&#8211;os=OS, -o OS</p>
<dd> Operating system</p>
<dt>&#8211;arch=ARCH, -a ARCH</p>
<dd> Arch this bug occurs on</p>
<dt>&#8211;severity=SEVERITY</p>
<dd> Bug severity</p>
<dt>&#8211;priority=PRIORITY</p>
<dd> Bug priority</p>
<dt>&#8211;url=URL, -u URL</p>
<dd> URL for further bug info</p>
<dt>&#8211;cc=CC[, CC, &#8230;]</p>
<dd> add emails to initial CC list</p>
<dt>&#8211;blocked=BUGID[, BUGID, &#8230;]</p>
<dd> add bug_ids blocked by this bug</p>
<dt>&#8211;dependson=BUGID[, BUGID, &#8230;]</p>
<dd> add bug_ids that this bug depends on</p>
<dt>&#8211;groups=GROUP[, GROUP, &#8230;]</p>
<dd> add groups to which bug is visible</p>
<dt>&#8211;assigned_to=ASSIGNED_TO</p>
<dd> Assign bugzilla to specified email address</p>
<dt>&#8211;qa_contact=QA_CONTACT</p>
<dd> Set QA contact to specified email address</p>
<dt>&#8211;keywords=KEYWORD[, KEYWORD, &#8230;]</p>
<dd> Set specified keywords on new bugzilla</p>
<dt>&#8211;alias=ALIAS</p>
<dd> An alias (name) for the bug (must be unique)</p>
<dt>&#8211;field=FIELD=VALUE</p>
<dd> Set a specified field. FIELD is expected to be the raw name used by the bugzilla instance. No safety checks are perfomed when using this option. </p>
</dl>
<h2>OUTPUT FORMAT &#8216;NEW&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;full, -f</p>
<dd> output detailed bug info</p>
<dt>&#8211;ids, -i</p>
<dd> output only bug IDs</p>
<dt>&#8211;extra, -e</p>
<dd> output additional bug information (keywords, Whiteboards, etc.)</p>
<dt>&#8211;oneline</p>
<dd> one line summary of the bug (useful for scripts)</p>
<dt>&#8211;raw</p>
<dd> raw output of the bugzilla contents</p>
<dt>&#8211;outputformat=OUTPUTFORMAT</p>
<dd> Print output in the form given. You can use RPM-style tags that match bug fields, e.g.: &#8216;%{id}: %{summary}&#8217;. See the man page section &#8216;OUTPUT FORMAT&#8217; for more details.</dl>
<h2>&#8216;QUERY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;bug_id=BUG_ID, -b BUG_ID</p>
<dd> specify individual bugs by IDs, separated with commas</p>
<dt>&#8211;product=PRODUCT, -p PRODUCT</p>
<dd> product name, comma-separated (list with &#8216;bugzilla info &#8211;products&#8217;)</p>
<dt>&#8211;version=VERSION, -v VERSION</p>
<dd> product version, comma-separated</p>
<dt>&#8211;component=COMPONENT, -c COMPONENT</p>
<dd> component name(s), comma-separated (list with &#8216;bugzilla info &#8211;components PRODUCT&#8217;)</p>
<dt>&#8211;sub-component=SUB_COMPONENT</p>
<dd> Sub component. Can be specified multiple times</p>
<dt>&#8211;components_file=COMPONENTS_FILE</p>
<dd> list of component names from a file, one component per line (list with &#8216;bugzilla info -c PRODUCT&#8217;)</p>
<dt>&#8211;long_desc=LONG_DESC, -l LONG_DESC</p>
<dd> search inside bug comments</p>
<dt>&#8211;target_milestone=TARGET_MILESTONE, -m TARGET_MILESTONE</p>
<dd> search for a target milestone</p>
<dt>&#8211;short_desc=SHORT_DESC, -s SHORT_DESC</p>
<dd> search bug summaries</p>
<dt>&#8211;bug_status=BUG_STATUS, -t BUG_STATUS</p>
<dd> comma-separated list of bug statuses to accept [Default:all]</p>
<dt>&#8211;bug_severity=BUG_SEVERITY, &#8211;severity=BUG_SEVERITY, -x BUG_SEVERITY</p>
<dd> search severities, comma-separated</p>
<dt>&#8211;priority=PRIORITY, -z PRIORITY</p>
<dd> search priorities, comma-separated</p>
<dt>&#8211;from-url=FROM_URL</p>
<dd> Use the query given by a query.cgi URL. (Use quotes!)</p>
<dt>&#8211;quicksearch=QUICKSEARCH</p>
<dd> Search using bugzilla&#8217;s quicksearch functionality.</p>
<dt>&#8211;savedsearch=SAVEDSEARCH</p>
<dd> Name of a bugzilla saved search. If you don&#8217;t own this saved search, you must passed &#8211;savedsearch_sharer_id.</p>
<dt>&#8211;savedsearch-sharer-id=SAVEDSEARCH_SHARER_ID</p>
<dd> Owner ID of the &#8211;savedsearch. You can get this ID from the URL bugzilla generates when running the saved search from the web UI.</p>
<dt>&#8211;field=FIELD=VALUE</p>
<dd> Query a specified field. FIELD is expected to be the raw name used by the bugzilla instance. No safety checks are perfomed when using this option. </p>
</dl>
<h2>EMAIL &#8216;QUERY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;emailtype=EMAILTYPE, -E EMAILTYPE</p>
<dd> Email: specify searching option for emails, ie. substring, notsubstring, exact, &#8230; [Default: substring]</p>
<dt>&#8211;cc=CC, -o CC</p>
<dd> Email: search cc lists for given address</p>
<dt>&#8211;reporter=REPORTER, -r REPORTER</p>
<dd> Email: search reporter email for given address</p>
<dt>&#8211;assigned_to=ASSIGNED_TO, -a ASSIGNED_TO</p>
<dd> Email: search for bugs assigned to this address</p>
<dt>&#8211;qa_contact=QA_CONTACT, -q QA_CONTACT</p>
<dd> Email: search for bugs which have QA Contact assigned to this address </p>
</dl>
<h2>STRING SEARCH &#8216;QUERY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;url=URL, -u URL</p>
<dd> search keywords field for given url</p>
<dt>&#8211;url_type=URL_TYPE, -U URL_TYPE</p>
<dd> specify searching option for urls, ie. anywords, allwords, nowords</p>
<dt>&#8211;keywords=KEYWORDS, -k KEYWORDS</p>
<dd> search keywords field for specified words</p>
<dt>&#8211;keywords_type=KEYWORDS_TYPE, -K KEYWORDS_TYPE</p>
<dd> specify searching option for keywords, ie. anywords, allwords, nowords</p>
<dt>&#8211;status_whiteboard=STATUS_WHITEBOARD, -w STATUS_WHITEBOARD</p>
<dd> search Status Whiteboard field for specified words</p>
<dt>&#8211;status_whiteboard_type=STATUS_WHITEBOARD_TYPE, -W STATUS_WHITEBOARD_TYPE</p>
<dd> specify searching option for Status Whiteboard, ie. anywords, allwords, nowords</p>
<dt>&#8211;tags=TAGS</p>
<dd> Search bug &#8216;tags&#8217; field </p>
</dl>
<h2>BOOLEAN &#8216;QUERY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;booleantype=BOOLEANTYPE, -B BOOLEANTYPE</p>
<dd> specify searching option for booleans, ie. substring, notsubstring, exact, &#8230; [Default: substring]</p>
<dt>&#8211;boolean_query=BOOLEAN_QUERY</p>
<dd> Create your own query. Format: BooleanName-Condition-Parameter &amp;/| &#8230; . ie, keywords-substring-Partner &amp; keywords-notsubstring-OtherQA</p>
<dt>&#8211;blocked=BLOCKED</p>
<dd> Search for bugs that block this bug ID</p>
<dt>&#8211;dependson=DEPENDSON</p>
<dd> Search for bugs that depend on this bug ID</p>
<dt>&#8211;flag=FLAG</p>
<dd> Search for bugs that have certain flag states present. Ex &#8211;flags=dev_ack+</p>
<dt>&#8211;qa_whiteboard=QA_WHITEBOARD</p>
<dd> search for bugs that have certain QA Whiteboard text present</p>
<dt>&#8211;devel_whiteboard=DEVEL_WHITEBOARD</p>
<dd> search for bugs that have certain Devel Whiteboard text present</p>
<dt>&#8211;alias=ALIAS</p>
<dd> search for bugs that have the provided alias</p>
<dt>&#8211;fixed_in=FIXED_IN</p>
<dd> search Status Whiteboard field for specified words </p>
</dl>
<h2>OUTPUT FORMAT &#8216;QUERY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;full, -f</p>
<dd> output detailed bug info</p>
<dt>&#8211;ids, -i</p>
<dd> output only bug IDs</p>
<dt>&#8211;extra, -e</p>
<dd> output additional bug information (keywords, Whiteboards, etc.)</p>
<dt>&#8211;oneline</p>
<dd> one line summary of the bug (useful for scripts)</p>
<dt>&#8211;raw</p>
<dd> raw output of the bugzilla contents</p>
<dt>&#8211;outputformat=OUTPUTFORMAT</p>
<dd> Print output in the form given. You can use RPM-style tags that match bug fields, e.g.: &#8216;%{id}: %{summary}&#8217;. See the man page section &#8216;OUTPUT FORMAT&#8217; for more details.</dl>
<h2>&#8216;MODIFY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;field=FIELD=VALUE</p>
<dd> Modify a specified field. FIELD is expected to be the raw name used by the bugzilla instance. No safety checks are perfomed when using this option. </p>
</dl>
<h2>BUG DETAILS</h2>
<dl>
<dt>&#8211;product=PRODUCT</p>
<dd> Reassign bug to different product</p>
<dt>&#8211;component=COMPONENT, -c COMPONENT</p>
<dd> Reassign bug to different component</p>
<dt>&#8211;sub-component=SUB_COMPONENT</p>
<dd> Reassign bug to different sub-component (rhbz extension)</p>
<dt>&#8211;version=VERSION, -v VERSION</p>
<dd> Reassign bug to different version</p>
<dt>&#8211;os=OS, -o OS</p>
<dd> Change operating system this bug occurs on</p>
<dt>&#8211;arch=ARCH, -a ARCH</p>
<dd> Change arch this bug occurs on</p>
<dt>&#8211;url=URL, -u URL</p>
<dd> URL for further bug info</p>
<dt>&#8211;alias=ALIAS</p>
<dd> An alias (name) for the bug (must be unique) </p>
</dl>
<h2>BUG STATUS &#8216;MODIFY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;status=STATUS, -s STATUS</p>
<dd> Change status of bug</p>
<dt>&#8211;close=RESOLUTION, -k RESOLUTION</p>
<dd> Close with the given resolution</p>
<dt>&#8211;dupeid=ORIGINAL, -d ORIGINAL</p>
<dd> ID of original bug (implies -k DUPLICATE)</p>
<dt>&#8211;fixed_in=VERSION, -F VERSION</p>
<dd> &quot;Fixed in version&quot; field </p>
</dl>
<h2>COMMENT &#8216;MODIFY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;comment=COMMENT, -l COMMENT</p>
<dd> Add a comment</p>
<dt>&#8211;private, -p</p>
<dd> Mark new comment as private</p>
<dt>&#8211;summary=SUMMARY</p>
<dd> Change bug summary </p>
</dl>
<h2>CONTACT &#8216;MODIFY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;assignee=ASSIGNEE</p>
<dd> Assign bugzilla to assignee</p>
<dt>&#8211;cc=EMAIL</p>
<dd> Alter CC list. EMAIL appends, -EMAIL removes.</p>
<dt>&#8211;qa_contact=QA_CONTACT</p>
<dd> Change QA contact</p>
<dt>&#8211;reset-assignee</p>
<dd> Reset assignee to component default</p>
<dt>&#8211;reset-qa-contact</p>
<dd> Reset QA contact to component default</p>
<dt>&#8211;groups=GROUP[, GROUP, &#8230;]</p>
<dd> add groups to which bug is visible </p>
</dl>
<h2>TRACKING &#8216;MODIFY&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;flag=FLAG, -f FLAG</p>
<dd> Update bugzilla flags with requested type, ie fedora-cvs?, or needinfoX to clear (Use a new option for each flag)</p>
<dt>&#8211;severity=SEVERITY</p>
<dd> Change bug severity</p>
<dt>&#8211;priority=PRIORITY</p>
<dd> Change bug priority</p>
<dt>&#8211;target_milestone=TARGET_MILESTONE</p>
<dd> Set target milestone</p>
<dt>&#8211;target_release=TARGET_RELEASE</p>
<dd> Set target release</p>
<dt>&#8211;blocked=BUGID[, BUGID, &#8230;]</p>
<dd> Add bug_ids blocked by this bug. BUGID appends, -BUGID removes, =BUGID overwrites</p>
<dt>&#8211;dependson=BUGID[, BUGID, &#8230;]</p>
<dd> Alter depends_on list. BUGID appends, -BUGID removes, =BUGID overwrites</p>
<dt>&#8211;keywords=KEYWORD</p>
<dd> Alter bug keywords list. KEYWORD appends, -KEYWORD removes, =KEYWORD overwrites</p>
<dt>&#8211;whiteboard=TEXT</p>
<dd> Alter status whiteboard text. TEXT appends, -TEXT removes, =TEXT overwrites</p>
<dt>&#8211;devel_whiteboard=TEXT</p>
<dd> Alter devel whiteboard text. TEXT appends, -TEXT removes, =TEXT overwrites</p>
<dt>&#8211;internal_whiteboard=TEXT</p>
<dd> Alter internal whiteboard text. TEXT appends, -TEXT removes, =TEXT overwrites</p>
<dt>&#8211;qa_whiteboard=TEXT</p>
<dd> Alter QA whiteboard. TEXT appends, -TEXT removes, =TEXT overwrites</p>
<dt>&#8211;tags=TEXT</p>
<dd> Alter bug &#8216;tags&#8217; fieldTEXT appends, -TEXT removes</dl>
<h2>&#8216;ATTACH&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;file=FILENAME, -f FILENAME</p>
<dd> File to attach, or filename for data provided on stdin</p>
<dt>&#8211;description=DESCRIPTION, -d DESCRIPTION</p>
<dd> A short description of the file being attached</p>
<dt>&#8211;type=MIMETYPE, -t MIMETYPE</p>
<dd> Mime-type for the file being attached</p>
<dt>&#8211;get=ATTACHID, -g ATTACHID</p>
<dd> Download the attachment with the given ID</p>
<dt>&#8211;getall=BUGID, &#8211;get-all=BUGID</p>
<dd> Download all attachments on the given bug</dl>
<h2>&#8216;INFO&#8217; OPTIONS</h2>
<dl>
<dt>&#8211;products, -p</p>
<dd> Get a list of products</p>
<dt>&#8211;components=PRODUCT, -c PRODUCT</p>
<dd> List the components in the given product</p>
<dt>&#8211;component_owners=PRODUCT, -o PRODUCT</p>
<dd> List components (and their owners)</p>
<dt>&#8211;versions=VERSION, -v VERSION</p>
<dd> List the versions for the given product</dl>
<h2>OUTPUT FORMAT</h2>
<p> The output of the bugzilla tool should NEVER BE PARSED unless you are using a custom &#8211;outputformat. For everything else, just don&#8217;t parse it, the formats are not stable and are subject to change. </p>
<p> &#8211;outputformat allows printing arbitrary bug data in a user preferred format. For example, to print a returned bug ID, component, and product, separated with ::, do: </p>
<p> &#8211;outputformat &quot;%{id}::%{component}::%{product}&quot; </p>
<p> The fields (like &#8216;id&#8217;, &#8216;component&#8217;, etc.) are the names of the values returned by bugzilla&#8217;s XMLRPC interface. To see a list of all fields, check the API documentation in the &#8216;SEE ALSO&#8217; section. Alternatively, run a &#8216;bugzilla &#8211;debug query &#8230;&#8217; and look at the key names returned in the query results. Also, in most cases, using the name of the associated command line switch should work, like &#8211;bug_status becomes %{bug_status}, etc. </p>
<h2>AUTHENTICATION COOKIES AND TOKENS</h2>
<p> Older bugzilla instances use cookie-based authentication, and bugzilla.redhat.com uses a non-cookie token system. </p>
<p> When you log into bugzilla with the &quot;login&quot; subcommand or the &quot;&#8211;login&quot; argument, we cache the cookie in ~/.bugzillacookies. If you are using bugzilla.redhat.com, we also cache the token in ~/.bugzillatoken. </p>
<p> To perform an authenticated bugzilla command on a new machine, run a one time &quot;bugzilla login&quot; to cache credentials before running the desired command. You can also run &quot;bugzilla &#8211;login&quot; and the login process will be initiated before invoking the command. </p>
<p> Additionally, the &#8211;no-cache-credentials option will tell the bugzilla tool to _not_ save any credentials to ~/.bugzillacookies or ~/.bugzillatoken. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> bugzilla query &#8211;bug_id 62037 </p>
<p> bugzilla query &#8211;version 15 &#8211;component python-bugzilla </p>
<p> # All boolean options can be formatted like this<br />
 bugzilla query &#8211;blocked &quot;123456 | 224466&quot; </p>
<p> bugzilla login </p>
<p> bugzilla new -p Fedora -v rawhide -c python-bugzilla \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;summary&nbsp;<wbr>&quot;python-bugzilla causes headaches&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;comment&nbsp;<wbr>&quot;python-bugzilla made my brain hurt when I used it.&quot; </p>
<p> bugzilla attach &#8211;file ~/Pictures/cam1.jpg &#8211;desc &quot;me, in pain&quot; $BUGID </p>
<p> bugzilla attach &#8211;getall $BUGID </p>
<p> bugzilla modify &#8211;close NOTABUG &#8211;comment &quot;Actually, you&#8217;re hungover.&quot; $BUGID </p>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>bugzilla</code> normally returns 0 if the requested command was successful. Otherwise, exit status is 1 if <code>bugzilla</code> is interrupted by the user (or a login attempt fails), 2 if a socket error occurs (e.g. TCP connection timeout), and 3 if the server returns an XML-RPC fault.</p>
<h2>BUGS</h2>
<p> Please report any bugs as github issues at<br />
 <a rel="nofollow" href="https://github.com/python-bugzilla/python-bugzilla">https://github.com/python-bugzilla/python-bugzilla</a><br />
 to the mailing list at<br />
 <a rel="nofollow" href="https://fedorahosted.org/mailman/listinfo/python-bugzilla">https://fedorahosted.org/mailman/listinfo/python-bugzilla</a></p>
<h2>SEE ALSO</h2>
<pre>
<a rel="nofollow" href="http://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html">http://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html</a>
<a rel="nofollow" href="https://bugzilla.redhat.com/docs/en/html/api/Bugzilla/WebService/Bug.html">https://bugzilla.redhat.com/docs/en/html/api/Bugzilla/WebService/Bug.html</a>
</pre>
<h2>Index</h2>
