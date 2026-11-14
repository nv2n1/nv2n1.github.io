---
title: "zarafa-search-cfg(5)"
name: "zarafa-search-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-search-cfg/"
description: "zarafa-search.cfg – The Zarafa Search configuration file"
---

<p>zarafa-search.cfg &#8211; The Zarafa Search configuration file</p>
<h2>Synopsis</h2>
<p><code>search.cfg</code></p>
<h2>Description</h2>
<p>The search.cfg is a configuration file for the Zarafa Search Service. search.cfg contains instructions for the software to set up the connection, indexing and logging systems.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<h2>Explanation Of The Server Settings Parameters</h2>
<p><code>server_socket</code></p>
<dl>
<dd>Socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the server process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the server process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-search.pid</i></dl>
<p> <code>running_path</code></p>
<dl>
<dd>Change directory to this path when running in daemonize mode. When using the -F switch to run in the foreground the directory will not be changed. </p>
<p> Default: <i>/</i></dl>
<p> <code>limit_results</code></p>
<dl>
<dd>Limit the number of results returned to the server. If set to a nonzero value, only the N most relevant results will be returned to the server. This in turn limits the number of results that the user will see. If the limit is set to 0, all results will be returned. </p>
<p> Default:<i>0</i></dl>
<h2>Explanation Of The Ssl Settings Parameters</h2>
<p><code>ssl_key_file</code></p>
<dl>
<dd>The file containing the private key and certificate. Please read the SSL section in the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual on how to create this file. </p>
<p> Default: <i>/etc/zarafa/ssl/search.pem</i></dl>
<p> <code>ssl_key_pass</code></p>
<dl>
<dd>Enter you password here when your key file contains a password to be readable. </p>
<p> No default set.</dl>
<p> <code>ssl_private_key_file</code></p>
<dl>
<dd>zarafa-search will use this file as private key for SSL TLS. This file can be created with: <code>openssl genrsa -out /etc/zarafa/search/privkey.pem 2048</code>. </p>
<p> Default: <i>/etc/zarafa/search/privkey.pem</i></dl>
<p> <code>ssl_certificate_file</code></p>
<dl>
<dd>zarafa-search will use this file as certificate for SSL TLS. A self-signed certificate can be created with: <code>openssl req -new -x509 -key /etc/zarafa/search/privkey.pem -out /etc/zarafa/search/cert.pem -days 1095</code>. </p>
<p> Default: <i>/etc/zarafa/search/cert.pem</i></dl>
<h2>Explanation Of The Logging Settings Parameters</h2>
<p><code>log_method</code></p>
<dl>
<dd>The method which should be used for logging. Valid values are: </p>
<p> <i>syslog</i></p>
<dl>
<dd>Use the Linux system log. All messages will be written to the mail facility. See also <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5).</dl>
<p> <i>file</i></p>
<dl>
<dd>Log to a file. The filename will be specified in <code>log_file</code>.</dl>
<p> Default: <i>file</i></dl>
<p> <code>log_file</code></p>
<dl>
<dd>When logging to a file, specify the filename in this parameter. Use <i>&#8211;</i> (minus sign) for stderr output. </p>
<p> Default: <i>/var/log/zarafa/search.log</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<h2>Explanation Of The Search Settings Parameters</h2>
<p><code>server_bind_name</code></p>
<dl>
<dd>Connection path to which other processes can connect with the zarafa-search for performing search queries. </p>
<p> Use <i><a rel="nofollow" href="http://0.0.0.0:port">http://0.0.0.0:port</a></i> to listen as an HTTP service on all network interfaces on the given <i>port</i> number. </p>
<p> Default: <i>file:///var/run/zarafa-search</i></dl>
<p> <code>index_path</code></p>
<dl>
<dd>Directory under which all index files will be placed. </p>
<p> Default: <i>/var/lib/zarafa/index/</i></dl>
<h2>Explanation Of The Index Optimize Schedule Parameters</h2>
<p><code>optimize_start</code></p>
<dl>
<dd>Start the optimization routine at this hour every day. The routine optimizes every index, removing old data and recompressing it, making it faster and smaller. Notation is in 24h format, default starts at 2 am. </p>
<p> Default: <i>2</i></dl>
<p> <code>optimize_stop</code></p>
<dl>
<dd>Stop the optimization routine at this hour when not all files were processed. The routine will continue were left off the next day it&#8217;s started. The current file being processed will be finished, so the time will be passed. Notation is in 24h format, default stops at 5 am. </p>
<p> Default: <i>5</i></dl>
<p> <code>optimize_age</code></p>
<dl>
<dd>Only optimize the index file if it wasn&#8217;t optmized for the past X days. Notation is in days, default is to optimize an index each week. </p>
<p> Default: <i>7</i></dl>
<h2>Explanation Of The Attachment Search Settings Parameters</h2>
<p><code>index_attachments</code></p>
<dl>
<dd>Enable indexing of attachments. When attachments are being indexed, searching for keywords in the body of a message will automatically cause the attachment to be searched as well. </p>
<p> This will slow down the indexing process, require more system memory and increases index file size. </p>
<p> Default: <i>no</i></dl>
<p> <code>index_attachment_max_size</code></p>
<dl>
<dd>Maxiumum file size for attachments to be indexed. Any attachment larger then this amount will not be indexed. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>5M</i></dl>
<p> <code>index_attachment_parser</code></p>
<dl>
<dd>For indexing attachment each file must be converted into plain-text by a parser. For this purpose the <i>attachments_parser</i> script has been installed which can be configured to parse specific mime-types. </p>
<p> It is highly advisable to check the <i>attachments_parser.db</i> file to add or remove parser command for specific mime-types and/or file-extensions. </p>
<p> Default: <i>/etc/zarafa/searchscripts/attachments_parser</i></dl>
<p> <code>index_attachment_parser_max_memory</code></p>
<dl>
<dd>Limit the maximum amount of memory (in bytes) the parser may use for converting the attachment into plain-text. If this limit is exceeded the parser will be killed and the attachment will not be completely converted. If the value is set to <i>0</i> the limit is considered as infinite. </p>
<p> The attachment parser depends on external tools to convert attachments to plain-text, by limiting the amount of resources the parser is allowed to use problems can be prevented when the selected external tool misbehaves with certain attachments. </p>
<p> Default: <i>0</i> bytes</dl>
<p> <code>index_attachment_parser_max_cputime</code></p>
<dl>
<dd>Limit the maximum cpu time (in seconds) the parser may use for converting the attachment into plain-text. If this limit is exceeded the parser will be killed and the attachment will not be completely converted. If the value is set to <i>0</i> the limit is considered as infinite. </p>
<p> The attachment parser depends on external tools to convert attachments to plain-text, by limiting the amount of resources the parser is allowed to use problems can be prevented when the selected external tool misbehaves with certain attachments. </p>
<p> Default: <i>0</i> seconds</dl>
<p> <code>index_attachment_mime_filter</code></p>
<dl>
<dd>Some attachments are not intresting to run through the parser. With this option you can filter out attachment which have a specific mimetype. Only the first part of the mimetype should be given here. Good examples of a mimetype to filter is &#8216;image&#8217;, &#8216;audio&#8217; and &#8216;video&#8217;. This field is space separated. </p>
<p> Default:</dl>
<p> <code>index_attachment_extension_filter</code></p>
<dl>
<dd>As the mime filter above, but works on the attachment extension. This is only tested if the mimetype of an attachment was unknown. Good examples of an extension to filter is &#8216;gif&#8217;, &#8216;jpeg&#8217;, &#8216;jpg&#8217; and &#8216;png&#8217;. This field is space separated. </p>
<p> Default:</dl>
<p> <code>index_max_clauses</code></p>
<dl>
<dd>This is the maximum number of clauses that can be present in a Lucene search query, after expansion. You can raise this limit if you are experiencing a Too Many Clauses error during searches. </p>
<p> Default: <i>50000</i> clauses</dl>
<h2>Explanation Of The Index Filters Settings Parameters</h2>
<p><code>index_exclude_properties</code></p>
<dl>
<dd>Some properties are ignored because they contain unrelated information for users to find their messages on. A default set of ignored property ids is set here, but can be expanded. Only the id part of a property is needed, and must be string typed properties. The field is space separated. </p>
<p> Default: 007D 0064 0C1E 0075 678E 678F</dl>
<p> <code>term_cache_size</code></p>
<dl>
<dd>The size in bytes of the term cache used when writing terms to the index. A larger term cache will increase indexing speed when indexing large number of documents in a single store. This will barely affect incremental updates after the initial indexing has finished. This value may contain a k, m or g multiplier. </p>
<p> Default: 64M</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-search/">zarafa-search</a></code>(1) </p>
