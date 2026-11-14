---
title: "bti(1)"
name: "bti"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bti/"
description: "bti – send a tweet to twitter.com from the command line"
---

<h2 class="name">NAME</h2>
<p> bti &#8211; send a tweet to twitter.com from the command line </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bti</code> [<code>&#8211;account account</code>] [<code>&#8211;password password</code>] [<code>&#8211;action action</code>] [<code>&#8211;user screenname</code>] [<code>&#8211;host HOST_NAME</code>] [<code>&#8211;proxy PROXY:PORT</code>] [<code>&#8211;logfile LOGFILE</code>] [<code>&#8211;config CONFIGFILE</code>] [<code>&#8211;replyto ID</code>] [<code>&#8211;retweet ID</code>] [<code>&#8211;page PAGENUMBER</code>] [<code>&#8211;bash</code>] [<code>&#8211;shrink-urls</code>] [<code>&#8211;debug</code>] [<code>&#8211;dry-run</code>] [<code>&#8211;verbose</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>bti sends a tweet message to twitter.com.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;account account</code></p>
<dl>
<dt>
<dd> Specify the twitter.com account name.</dl>
<p> <code>&#8211;password password</code></p>
<dl>
<dt>
<dd> Specify the password of your twitter.com account.</dl>
<p> <code>&#8211;action action</code></p>
<dl>
<dt>
<dd> Specify the action which you want to perform. Valid options are &quot;update&quot; to send a message, &quot;friends&quot; to see your friends timeline, &quot;public&quot; to track public timeline, &quot;replies&quot; to see replies to your messages, &quot;user&quot; to see a specific user&#8217;s timeline and &quot;direct&quot; to send a direct message to a friend. Default is &quot;update&quot;.</dl>
<p> <code>&#8211;user screenname</code></p>
<dl>
<dt>
<dd> Specify the user whose messages you want to see when the action is &quot;user&quot;, and the reciever of the direct message when the action is &quot;direct&quot; (the sender must be following the receiver).</dl>
<p> <code>&#8211;host HOST_NAME</code></p>
<dl>
<dt>
<dd> Specify the host which you want to send your message to. Valid options are &quot;twitter&quot; to send to twitter.com. </p>
<p> If no host is specified, the default is to send to twitter.com.</dl>
<p> <code>&#8211;proxy PROXY:PORT</code></p>
<dl>
<dt>
<dd> Specify a http proxy value. This is not a required option, and only needed by systems that are behind a http proxy. </p>
<p> If &#8211;proxy is not specified but the environment variable &#8216;http_proxy&#8217; is set the latter will be used.</dl>
<p> <code>&#8211;logfile LOGFILE</code></p>
<dl>
<dt>
<dd> Specify a logfile for bti to write status messages to. LOGFILE is in relation to the user&#8217;s home directory, not an absolute path to a file.</dl>
<p> <code>&#8211;config CONFIGFILE</code></p>
<dl>
<dt>
<dd> Specify a config file for bti to read from. By default, bti looks in the ~/.bti file for config values. This default location can be overridden by setting a specific file with this option.</dl>
<p> <code>&#8211;replyto ID</code></p>
<dl>
<dt>
<dd> Status ID of a single post to which you want to create a threaded reply to. </p>
<p> For twitter, this is ignored unless the message starts with the @name of the owner of the post with the status ID. </p>
<p> For status.net, this can link any two messages into context with each other. Status.net will also link a message that contains an @name without this without regard to context.</dl>
<p> <code>&#8211;retweet ID</code></p>
<dl>
<dt>
<dd> Status ID of a single post which you want to retweet.</dl>
<p> <code>&#8211;shrink-urls</code></p>
<dl>
<dt>
<dd> Scans the tweet text for valid URL patterns and passes each through the supplied bti-shrink-urls script. The script will pass the URL to a web service that shrinks the URLs, making it more suitable for micro-blogging. </p>
<p> The following URL shrinking services are available: <a rel="nofollow" href="http://2tu.us/">http://2tu.us/</a> (default) and <a href="http://bit.ly">http://bit.ly</a> / <a href="http://j.mp">http://j.mp</a> </p>
<p> See the documentation for bti-shrink-urls for the configuration options.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Print a whole bunch of debugging messages to stdout.</dl>
<p> <code>&#8211;page PAGENUMBER</code></p>
<dl>
<dt>
<dd> When the action is to retrieve updates, it usually retrieves only one page. If this option is used, the page number can be specified.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Performs all steps that would normally be done for a given action, but will not connect to the service to post or retrieve data.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode. Print status IDs and timestamps.</dl>
<p> <code>&#8211;bash</code></p>
<dl>
<dt>
<dd> Add the working directory and a &#8216;$&#8217; in the tweet message to help specify it is coming from a command line. Don&#8217;t put the working directory and the &#8216;$&#8217; in the tweet message. </p>
<p> This option implies <code>&#8211;background</code>.</dl>
<p> <code>&#8211;background</code></p>
<dl>
<dt>
<dd> Do not report back any errors that might have happened when sending the message, and send it in the background, returning immediately, allowing the user to continue on.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version number.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help text.</dl>
<h2>DESCRIPTION</h2>
<p> bti provides an easy way to send tweet messages direct from the command line or any script. It reads the message on standard input and uses the account and password settings either from the command line options, or from a config file, to send the message out. </p>
<p> Its primary focus is to allow you to log everything that you type into a bash shell, in a crazy, &quot;this is what I&#8217;m doing right now!&quot; type of way, letting the world follow along with you constant moving between directories and refreshing your email queue to see if there&#8217;s anything interesting going on. </p>
<p> To hook bti up to your bash shell, export the following variable: </p>
<p> PROMPT_COMMAND=&#8217;history 1 | sed -e &quot;s/^\s*[0-9]*\s*//&quot; | bti &#8211;bash&#8217; </p>
<p> This example assumes that you have the ~/.bti set up with your account and password information already in it, otherwise you can specify them as an option.</p>
<h2>CONFIGURATION</h2>
<p> The account and password can be stored in a configuration file in the users home directory in a file named .bti. The structure of this file is as follows: </p>
<p> <code>account</code></p>
<dl>
<dt>
<dd> The twitter.com account name you wish to use to send this message with.</dl>
<p> <code>password</code></p>
<dl>
<dt>
<dd> The twitter.com password for the account you wish to use to send this message with.</dl>
<p> <code>&#8211;action action</code></p>
<dl>
<dt>
<dd> Specify the action which you want to perform. Valid options are &quot;update&quot; to send a message, &quot;friends&quot; to see your friends timeline, &quot;public&quot; to track public timeline, &quot;replies&quot; to see replies to your messages and &quot;user&quot; to see a specific user&#8217;s timeline.</dl>
<p> <code>&#8211;user screenname</code></p>
<dl>
<dt>
<dd> Specify the user you want to see his/her messages while the action is &quot;user&quot;.</dl>
<p> <code>host</code></p>
<dl>
<dt>
<dd> The host you want to use to send the message to. Valid options is &quot;twitter&quot; or &quot;custom&quot; to specify your own server.</dl>
<p> <code>proxy</code></p>
<dl>
<dt>
<dd> The http proxy needed to send data out to the Internet.</dl>
<p> <code>logfile</code></p>
<dl>
<dt>
<dd> The logfile name for bti to write what happened to. This file is relative to the user&#8217;s home directory. If this file is not specified here or on the command line, no logging will be written to the disk.</dl>
<p> <code>replyto</code></p>
<dl>
<dt>
<dd> The status ID to which all notices will be linked to. </p>
<p> There is no sane reason for a need to have this set in a config file. One such reason is to have all your messages as children to a particular status.</dl>
<p> <code>shrink-urls</code></p>
<dl>
<dt>
<dd> Setting this variable to &#8216;true&#8217; or &#8216;yes&#8217; will enable the URL shrinking feature. This is equivalent to using the &#8211;shrink-urls option.</dl>
<p> <code>verbose</code></p>
<dl>
<dt>
<dd> Setting this variable to &#8216;true&#8217; or &#8216;yes&#8217; will enable the verbose mode.</dl>
<p> There is an example config file called bti.example in the source tree that shows the structure of the file if you need an example to work off of. </p>
<p> Configuration options have the following priority: </p>
<dl>
<dt>
<dd> command line option</dl>
<dl>
<dt>
<dd> config file option</dl>
<dl>
<dt>
<dd> environment variables</dl>
<p> For example, command line options always override any config file option, or any environment variables. Unless a config file is specified by the command line. At that point, the new config file is read, and any previous options set by a command line option, would be overridden.</p>
<h2>AUTHOR</h2>
<p> Written by Greg Kroah-Hartman &lt;&lt;greg [at] kroah.com&gt;&gt; and Amir Mohammad Saied &lt;&lt;amirsaied [at] gmail.com&gt;&gt;. </p>
<h2>Index</h2>
