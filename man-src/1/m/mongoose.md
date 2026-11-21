---
title: "mongoose(1)"
name: "mongoose"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongoose/"
description: "mongoose – lightweight web server"
---

<h2>NAME</h2>
<p> <code>mongoose</code> &#8211; lightweight web server</p>
<h2>SYNOPSIS</h2>
<p> [<i>config_file</i> ]<br />
 [<i>OPTIONS</i> ]<br />
 &#8211;<code>A </code><i>htpasswd_file domain_name user_name password</i></p>
<h2>DESCRIPTION</h2>
<p> is small, fast and easy to use web server with CGI, SSL, MD5 authorization, and basic SSI support. </p>
<p> does not detach from terminal, and uses current working directory as the web root, unless &#8211;<code>r</code> option is specified. It is possible to specify multiple ports to listen on. For example, to make mongoose listen on HTTP port 80 and HTTPS port 443, one should start it as: &#8211;<code>s </code><i>cert.pem &#8211;</i><code>p </code><i>80,443s</i> </p>
<p> Unlike other web servers, does not expect CGI scripts to be put in a special directory. CGI scripts can be anywhere. CGI (and SSI) files are recognized by the file extension. </p>
<p> If no arguments are given, searches for a configuration file called &quot;mongoose.conf&quot; in the same directory where mongoose binary is located. Alternatively, a file name could be specified in the command line. Format of the configuration file is the same as for the command line options except that each option must be specified on a separate line, leading dashes for option names must be omitted. Lines beginning with &#8216;#&#8217; and empty lines are ignored. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A </code><i>htpasswd_file domain_name user_name password</i></dt>
<dd> Add/edit user&#8217;s password in the passwords file. Deleting users can be done with any text editor. Functionality is similar to Apache&#8217;s <code>htdigest</code> utility.</dd>
<dt><code>-C </code><i>cgi_extensions</i></dt>
<dd> Comma-separated list of CGI extensions. All files having these extensions are treated as CGI scripts. Default: &quot;.cgi,.pl,.php&quot;</dd>
<dt><code>-E </code><i>cgi_environment</i></dt>
<dd> Extra environment variables to be passed to the CGI script in addition to standard ones. The list must be comma-separated list of X=Y pairs, like this: &quot;VARIABLE1=VALUE1,VARIABLE2=VALUE2&quot;. Default: &quot;&quot;</dd>
<dt><code>-G </code><i>put_delete_passwords_file</i></dt>
<dd> PUT and DELETE passwords file. This must be specified if PUT or DELETE methods are used. Default: &quot;&quot;</dd>
<dt><code>-I </code><i>cgi_interpreter</i></dt>
<dd> Use <i>cgi_interpreter</i> as a CGI interpreter for all CGI scripts regardless script extension. Default: &quot;&quot;. Mongoose decides which interpreter to use by looking at the first line of a CGI script.</dd>
<dt><code>-M </code><i>max_request_size</i></dt>
<dd> Maximum HTTP request size in bytes. Default: &quot;16384&quot;</dd>
<dt><code>-P </code><i>protect_uri</i></dt>
<dd> Comma separated list of URI=PATH pairs, specifying that given URIs must be protected with respected password files. Default: &quot;&quot;</dd>
<dt><code>-R </code><i>authentication_domain</i></dt>
<dd> Authorization realm. Default: &quot;mydomain.com&quot;</dd>
<dt><code>-S </code><i>ssi_extensions</i></dt>
<dd> Comma separated list of SSI extensions. Unknown SSI directives are silently ignored. Currently, two SSI directives supported, &quot;include&quot; and &quot;exec&quot;. Default: &quot;shtml,shtm&quot;</dd>
<dt><code>-a </code><i>access_log_file</i></dt>
<dd> Access log file. Default: &quot;&quot;, no logging is done.</dd>
<dt><code>-d </code><i>enable_directory_listing</i></dt>
<dd> Enable/disable directory listing. Default: &quot;yes&quot;</dd>
<dt><code>-e </code><i>error_log_file</i></dt>
<dd> Error log file. Default: &quot;&quot;, no errors are logged.</dd>
<dt><code>-g </code><i>global_passwords_file</i></dt>
<dd> Location of a global passwords file. If set, per-directory .htpasswd files are ignored, and all requests must be authorised against that file. Default: &quot;&quot;</dd>
<dt><code>-i </code><i>index_files</i></dt>
<dd> Comma-separated list of files to be treated as directory index files. Default: &quot;index.html,index.htm,index.cgi&quot;</dd>
<dt><code>-l </code><i>access_control_list</i></dt>
<dd> Specify access control list (ACL). ACL is a comma separated list of IP subnets, each subnet is prepended by &#8216;-&#8216; or &#8216;+&#8217; sign. Plus means allow, minus means deny. If subnet mask is omitted, like &quot;-1.2.3.4&quot;, then it means single IP address. Mask may vary from 0 to 32 inclusive. On each request, full list is traversed, and last match wins. Default setting is to allow all. For example, to allow only 192.168/16 subnet to connect, run &quot;mongoose -0.0.0.0/0,+192.168/16&quot;. Default: &quot;&quot;</dd>
<dt><code>-m </code><i>extra_mime_types</i></dt>
<dd> Extra mime types to recognize, in form &quot;extension1=type1,extension2=type2,&#8230;&quot;. Extension must include dot. Example: &quot;mongoose -m .cpp=plain/text,.java=plain/text&quot;. Default: &quot;&quot;</dd>
<dt><code>-p </code><i>listening_ports</i></dt>
<dd> Comma-separated list of ports to listen on. If the port is SSL, a letter &#8216;s&#8217; must be appeneded, for example, &quot;-p 80,443s&quot; will open port 80 and port 443, and connections on port 443 will be SSL-ed. It is possible to specify an IP address to bind to. In this case, an IP address and a colon must be prepended to the port number. For example, to bind to a loopback interface on port 80 and to all interfaces on HTTPS port 443, use &quot;mongoose -p 127.0.0.1:80,443s&quot;. Default: &quot;8080&quot;</dd>
<dt><code>-r </code><i>document_root</i></dt>
<dd> Location of the WWW root directory. A comma separated list of URI_PREFIX=DIRECTORY pairs could be appended to it, allowing Mongoose to serve from multiple directories. For example, &quot;mongoose -p /var/www,/config=/etc,/garbage=/tmp&quot;. Default: &quot;.&quot;</dd>
<dt><code>-s </code><i>ssl_certificate</i></dt>
<dd> Location of SSL certificate file. Default: &quot;&quot;</dd>
<dt><code>-t </code><i>num_threads</i></dt>
<dd> Number of worker threads to start. Default: &quot;10&quot;</dd>
<dt><code>-u </code><i>run_as_user</i></dt>
<dd> Switch to given user&#8217;s credentials after startup. Default: &quot;&quot;</dd></dl>
<h2>EMBEDDING</h2>
<p> was designed to be embeddable into C/C++ applications. Since the source code is contained in single C file, it is fairly easy to embed it and follow the updates. Please refer to <a rel="nofollow" href="http://code.google.com/p/mongoose">http://code.google.com/p/mongoose</a> for details. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>-r </code><i>/var/www,/aa=/tmp,/bb=/etc &#8211;</i><code>s </code><i>/etc/cert.pem &#8211;</i><code>p </code><i>8080,8043s</i></dt>
<dd> Start listening on port 8080 for HTTP, and 8043 for HTTPS connections. Use /etc/cert.pem as SSL certificate file. Web root is /var/www. In addition, map directory /tmp to URI /aa, directory /etc to URI /bb.</dd>
<dt><code>-l </code><i>-0.0.0.0/0,+10.0.0.0/8,+1.2.3.4</i></dt>
<dd> Deny connections from everywhere, allow only IP address 1.2.3.4 and all IP addresses from 10.0.0.0/8 subnet to connect.</dd></dl>
<h2>COPYRIGHT</h2>
<p> is licensed under the terms of the MIT license.</p>
<h2>AUTHOR</h2>
<p> An Sergey Lyubka Aq valenok [at] gmail.com . </p>
