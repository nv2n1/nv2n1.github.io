---
title: "smokeping(1)"
name: "smokeping"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smokeping/"
description: "smokeping – Commandline tool for SmokePing"
---

<h2 class="name">NAME</h2>
<p> smokeping &#8211; Commandline tool for SmokePing </p>
<h2>SYNOPSIS</h2>
<p> <code>smokeping</code> [ <code>&#8211;email</code> | <code>&#8211;makepod</code> | <code>&#8211;version</code> | <code>&#8211;restart</code> ] </p>
<pre><code>
 Options:
 --man[=x]    Show the manpage for the program (or for probe x, if specified)
 --help       Help :-)
 --email      Send SmokePing Agents to all Targets marked DYNAMIC
 --config=x   Use a config file different from the default
 --check      Just check the config file syntax, don't start the daemon
 --makepod[=x] Create POD documentation on Config file (or for probe x, if specified)
 --version    Show SmokePing Version
 --debug      Run Only once and do not Fork
 --debug-daemon Start the daemon with debugging enabled
 --restart    Restart SmokePing
 --reload     Reload configuration in the running process without interrupting 
              any probes
 --nodaemon    Do no daemonize the process (no fork)
 --filter=x   Only measure entries which pass the filter x
 --logfile=x    Append warnings to logfile x.
 --static[=x] Generates a static website in directory x.  If x is left out,
              pagedir from the config is used.
 --nosleep    For debugging you may want to run SmokePing without sleep interval
 --gen-examples Generate the smokeping_examples document and example config files
                (to be used while building inside the smokeping distribution)
                With --check : check the syntax of the generated examples.
 --master-url=s Run smokeping in slave mode. Attach to master for config.
 --slave-name=s By default the slave will use whatever it thinks its name
                is, when talking to its master. In some cases you may
                probably want to override this.
 --shared-secret=s File containing the shared secret for talking to the server.
 --cache-dir=s Directory for temporary data storage when running in slave mode.
 --pid-dir=s Directory for the PID file when running in slave mode.
             (optional, defaults to --cache-dir)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>smokeping</code> tool is the commandline part of the SmokePing system. Its main function is to run as a daemon and send Pings to all the Targets you have specified in the Config file. When you call <code>smokeping</code> without arguments it will start as a daemon and do its work. </p>
<p> If called with an argument, then further functions can be activated, as seen in the Synopsis above. The <code>&#8211;email</code> function is explained in the documentation on the config file. </p>
<p> The <code>&#8211;filter</code> option allows you to run the daemon on a big config file, but have the config file filtered and only measure the entries that pass the filter. This is useful for remote measurement. Run Smokeping with two exclusive filters in two locations and rsync the rrds back to the webserver host where you run the cgi. Filters act on the section names in the config file. Multiple section names are concatenated with <code>/</code> like path names: </p>
<pre>
 *** targets ***
 + A
 ....
 + B
 ...
 ++ C
</pre>
<p> This gives </p>
<pre>
 /A
</pre>
<p> and </p>
<pre>
 /B, /B/C
</pre>
<p> If I want to monitor /A my filter would look like this: </p>
<pre>
 --filter=/A
</pre>
<p> Filters follow regular expression syntax. The are always anchored at the tip of the string. by adding a <code>!</code> to the front of the filter string you negate it. Matching entries will be excluded from monitoring. Multiple <code>&#8211;filter</code> arguments can be used to assemble complex filters: </p>
<pre>
  --filter=/A --filter=/B
</pre>
<p> would include all the targets </p>
<pre>
  --filter=/A --filter=/B --filter=!/B/C
</pre>
<p> would include all but /B/C. </p>
<p> The <code>&#8211;makepod</code> does get used internally to produce the documentation on the SmokePing configuration file. </p>
<p> Please refer to the installation document for detailed setup instructions.</p>
<h2>SETUP</h2>
<p> When installing SmokePing, this file has to be adjusted to fit your local system. Three paths have to be entered. </p>
<p> One pointing to your <code>rrdtool</code> installation </p>
<pre>
 use lib qw(/usr/pack/rrdtool-1.0.33-to/lib/perl);
</pre>
<p> One pointing to the place where you have installed the SmokePing libraries </p>
<pre>
 use lib qw(/home/oetiker/public_html/smokeping/lib);
</pre>
<p> The third path is the argument to the Smokeping::main command. It points to the SmokePing configuration file. </p>
<pre><code>
use Smokeping;
Smokeping::main("/home/oetiker/.smokeping/config");
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002 by Tobias Oetiker. All right reserved.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
