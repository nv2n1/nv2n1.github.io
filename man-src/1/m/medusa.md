---
title: "medusa(1)"
name: "medusa"
section: "1"
letter: "m"
url: "/docs/linux/man/1-medusa/"
description: "MEDUSA – Parallel Network Login Auditor"
---

<h2>NAME</h2>
<p> MEDUSA &#8211; Parallel Network Login Auditor</p>
<h2>SYNOPSIS</h2>
<p> <code>medusa</code> [-h host|-H file] [-u username|-U file] [-p password|-P file] [-C file] -M module [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> <i>Medusa</i> is intended to be a speedy, massively parallel, modular, login brute-forcer. The goal is to support as many services which allow remote authentication as possible. The author considers following items to some of the key features of this application: </p>
<p> *Thread-based parallel testing. Brute-force testing can be performed against multiple hosts, users or passwords concurrently. </p>
<p> *Flexible user input. Target information (host/user/password) can be specified in a variety of ways. For example, each item can be either a single entry or a file containing multiple entries. Additionally, a combination file format allows the user to refine their target listing. </p>
<p> *Modular design. Each service module exists as an independent .mod file. This means that no modifications are necessary to the core application in order to extend the supported list of services for brute-forcing. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h [TARGET]</code></p>
<dd> Target hostname or IP address. </p>
<dt><code>-H [FILE]</code></p>
<dd> Reads target specifications from the file specified rather than from the command line. The file should contain a list separated by newlines. </p>
<dt><code>-u [TARGET]</code></p>
<dd> Target username. </p>
<dt><code>-U [FILE]</code></p>
<dd> Reads target usernames from the file specified rather than from the command line. The file should contain a list separated by newlines. </p>
<dt><code>-p [TARGET]</code></p>
<dd> Target password. </p>
<dt><code>-P [FILE]</code></p>
<dd> Reads target passwords from the file specified rather than from the command line. The file should contain a list separated by newlines. </p>
<dt><code>-C [FILE]</code></p>
<dd> File containing combo entries. Combo files are colon separated and in the following format: host:user:password. If any of the three fields are left empty, the respective information should be provided either as a single global value or as a list in a file. </p>
<p> The following combinations are possible in the combo file: 1.) foo:bar:fud 2.) foo:bar: 3.) foo:: 4.) :bar:fud 5.) :bar: 6.) ::fud 7.) foo::fud </p>
<p> Medusa also supports using PwDump files as a combo file. The format of these files should be user:id:lm:ntlm:::. We look for &#8216;:::&#8217; at the end of the first line to determine if the file contains PwDump output. </p>
<dt><code>-O [FILE]</code></p>
<dd> File to append log information to. Medusa will log all accounts credentials found to be valid or cause an unknown error. It will also log the start and stop times of an audit, along with the calling parameters. </p>
<dt><code>-e [n/s/ns]</code></p>
<dd> Additional password checks ([n] No Password, [s] Password = Username). If both options are being used, they should be specified together (&quot;-e ns&quot;). If only a single option is being called use either &quot;-e n&quot; or &quot;-e s&quot;. </p>
<dt><code>-M [TEXT]</code></p>
<dd> Name of the module to execute (without the .mod extension). </p>
<dt><code>-m [TEXT]</code></p>
<dd> Parameter to pass to the module. This can be passed multiple times with a different parameter each time and they will all be sent to the module (i.e. -m Param1 -m Param2, etc.) </p>
<dt><code>-d</code></p>
<dd> Dump all known modules. </p>
<dt><code>-n [NUM]</code></p>
<dd> Use for non-default TCP port number. </p>
<dt><code>-s</code></p>
<dd> Enable SSL. </p>
<dt><code>-g [NUM]</code></p>
<dd> Give up after trying to connect for NUM seconds (default 3). </p>
<dt><code>-r [NUM]</code></p>
<dd> Sleep NUM seconds between retry attempts (default 3). </p>
<dt><code>-R [NUM]</code></p>
<dd> Attempt NUM retries before giving up. The total number of attempts will be NUM + 1. </p>
<dt><code>-c [NUM]</code></p>
<dd> Set the number of usec that are waited during a test of the established network socket. Some services (e.g. FTP, IMAP, POP3, and SMTP) may be configured to drop connections after an arbitrary number of failed logon attempts. We try to reuse the established connection to send authentication attempts until this disconnect occurs, at which point the connection is reestablished. To accomplish this, we check the socket to see if it&#8217;s still alive before authenticating within select modules. The default is perform a 1 usec check. It may be necessary to specify much larger values. For example, a 1000 usec was needed against our test vsftp server to avoid issues with its built-in anti-bruteforce mechanisms. </p>
<dt><code>-t [NUM]</code></p>
<dd> Total number of logins to be tested concurrently. It should be noted that rougly t x T threads could be running at any one time. 381 appears to be the limit on my fairly boring Gentoo Linux host. </p>
<dt><code>-T [NUM]</code></p>
<dd> Total number of hosts to be tested concurrently. </p>
<dt><code>-L</code></p>
<dd> Parallelize logins using one username per thread. The default is to process the entire username before proceeding. </p>
<dt><code>-f</code></p>
<dd> Stop scanning host after first valid username/password found. </p>
<dt><code>-F</code></p>
<dd> Stop audit after first valid username/password found on any host. </p>
<dt><code>-b</code></p>
<dd> Suppress startup banner </p>
<dt><code>-q</code></p>
<dd> Display module&#8217;s usage information. This should be used in conjunction with the &quot;-M&quot; option. For example, &quot;medusa -M smbnt -q&quot;. </p>
<dt><code>-v [NUM]</code></p>
<dd> Verbose level [0 &#8211; 6 (more)]. All messages at or below the specified level will be displayed. The default level is 5. </p>
<p> The following is the breakdown of the verbose levels: 0) EXIT APPLICATION 1) MESSAGE WITHOUT TAG 2) LOG MESSAGE WITHOUT TAG 3) IMPORTANT MESSAGE 4) ACCOUNT FOUND 5) ACCOUNT CHECK 6) GENERAL MESSAGE </p>
<dt><code>-w [NUM]</code></p>
<dd> Error debug level [0 &#8211; 10 (more)]. All messages at or below the specified level will be displayed. The default level is 5. </p>
<p> The following is the breakdown of the error levels: 0) FATAL 1) ALERT 2) CRITICAL 3) ERROR 4) WARNING 5) NOTICE 6) INFO 7) DEBUG 8) DEBUG &#8211; AUDIT 9) DEBUG &#8211; SERVER 10) DEBUG &#8211; MODULE </p>
<dt><code>-V</code></p>
<dd> Display version </p>
<dt><code>-Z [TEXT]</code></p>
<dd> Allows basic resuming of a previous scan. The supplied parameter describes which hosts were completed, which were partially tested and which had not been started. When Medusa receives a SIGINT, it will calculate and display a &quot;resume map&quot;. This map can then be supplied to the next run. For example, &quot;medusa [OPTIONS PREVIOUSLY USED] -Z h6u1u2h8.&quot;. In this particular example, hosts 1-5 were completed, host 6 was partially done (user 1 was partially completed and user 2 and beyond had not been started), host 7 was completed and host 8 and beyond had not been started. Medusa will parse this map and skip hosts and users accordingly. It should be noted that only host and user-level, not password-level, resuming is supported. If a user had been previously started, but was not completed, it will be tested from the start of its respective password list. </p>
</dl>
<h2>AUTHOR</h2>
<p> JoMo-Kun &lt;jmk [at] foofus.net&gt; fizzgig &lt;fizzgig [at] foofus.net&gt;</p>
<h2>BUGS</h2>
<p> Found a bug? Feel free to send in a patch. </p>
<h2>Index</h2>
