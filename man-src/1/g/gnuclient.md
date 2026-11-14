---
title: "gnuclient(1)"
name: "gnuclient"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnuclient/"
description: "gnuserv, gnuclient – Server and Clients for XEmacs"
---

<h2 class="name">NAME</h2>
<p> gnuserv, gnuclient &#8211; Server and Clients for XEmacs </p>
<h2>SYNOPSIS</h2>
<p> <code>gnuclient</code> [-nw] [-display display] [-q] [-v] [-l library] [-batch] [-f function] [-eval form] [-h hostname] [-p port] [-r remote-pathname] [[+line] file] &#8230;<br />
 <code>gnudoit [-q] </code> form<br />
 <code>gnuserv</code><br />
 <code>gnuattach </code> Removed as of gnuserv 3.x</p>
<h2>DESCRIPTION</h2>
<p> <i>gnuserv</i> is a server program run as a subprocess of XEmacs to handle all incoming and outgoing requests from <i>gnuclient</i>. It is not usually invoked directly, but is started from XEmacs by loading the <i>gnuserv</i> package and evaluating the Lisp form (gnuserv-start). </p>
<p> <i>gnuclient</i> allows the user to request a running XEmacs process to edit the named files or directories and/or evaluate lisp forms. Depending on your environment, TTY, X, GTK, or MS Windows frames, as well as batch (frameless) execution of Lisp may be available. One typical use for this is with a dialup connection to a machine on which an XEmacs process is currently running. </p>
<p> <i>gnudoit</i> is a shell script frontend to &#8220;gnuclient -batch -eval form&#8221;. Its use is deprecated. Try to get used to calling gnuclient directly. </p>
<p> <i>gnuattach</i> no longer exists. Its functionality has been replaced by <i>gnuclient -nw</i>.</p>
<h2>OPTIONS</h2>
<p> <i>gnuclient</i> supports as many of the command line options of Emacs as make sense in this context. In addition it adds a few of its own.<br />
 For backward compatibility, &#8220;long&#8221; options (.e., with doubled hyphen) may be specified using a single hyphen instead of a doubled one. Similarly, the &#8220;-nw&#8221; option is a historical artifact: a multiletter option with no double-hyphen version.</p>
<dl>
<dt><code>-nw</code></p>
<dd> This option makes <i>gnuclient</i> act as a frontend such that XEmacs can attach to the current TTY. XEmacs will then open a new TTY frame. The effect is similar to having started a new XEmacs on this TTY with the &#8220;-nw&#8221; option. It currently only works if XEmacs is running on the same machine as gnuclient. This is the default if the `DISPLAY&#8217; environment variable is not set.</p>
<dt><code>&#8211;display</code><i> display, </i><code>-display</code><i> display</i></p>
<dd> If this option is given or the `DISPLAY&#8217; environment variable is set then gnuclient will tell XEmacs to edit files in a frame on the specified X device.</p>
<dt><code>-q</code></p>
<dd> This option informs <i>gnuclient</i> to exit once connection has been made with the XEmacs process. Normally <i>gnuclient</i> waits until all of the files on the command line have been finished with (their buffers killed) by the XEmacs process, and all the forms have been evaluated. Note that this is <i>different</i> from XEmacs itself, where this option means to inhibit loading of the user init file.</p>
<dt><code>-v</code></p>
<dd> When this option is specified <i>gnuclient</i> will request for the specified files to be viewed instead of edited.</p>
<dt><code>-l</code><i> library</i></p>
<dd> Tell Emacs to load the specified library.</p>
<dt><code>-batch</code></p>
<dd> Tell Emacs not to open any frames. Just load libraries and evaluate lisp code. If no files to execute, functions to call or forms to eval are given using the <code>-l</code>, <code>-f</code>, or <code>-eval</code> options, then forms to eval are read from STDIN.</p>
<dt><code>-f</code><i> function,</i></p>
<dd> Make Emacs execute the lisp function.</p>
<dt><code>&#8211;eval</code><i> form, </i><code>-eval</code><i> form</i></p>
<dd> Make Emacs execute the Lisp form.</p>
<dt><code>-h</code><i> hostname</i></p>
<dd> Used only with Internet-domain sockets, this option specifies the host machine which should be running <i>gnuserv</i>. If this option is not specified then the value of the environment variable GNU_HOST is used if set. If no hostname is specified, and the GNU_HOST variable is not set, an Internet connection will not be attempted. N.B.: <i>gnuserv</i> does NOT allow Internet connections unless XAUTH authentication is used or the GNU_SECURE variable has been specified and points at a file listing all trusted hosts. (See SECURITY below.) </p>
<p> An Internet address (&#8220;dotted-quad&#8221;) may be specified instead of a hostname. IPv6 support is not robust. </p>
<p> A hostname of <code>unix</code> can be used to specify that the connection to the server should use a Unix-domain socket (if supported) rather than an Internet-domain socket.</p>
<dt><code>-p</code><i> port</i></p>
<dd> Used only with Internet-domain sockets, this option specifies the service port used to communicate between server and clients. If this option is not specified, then the value of the environment variable GNU_PORT is used, if set, otherwise a service called &#8220;gnuserv&#8221; is looked up in the services database. Finally, if no other value can be found for the port, then a default port is used which is usually 21490 + uid.<br />
 Note that since <i>gnuserv</i> doesn&#8217;t allow command-line options, the port for it will have to be specified via one of the alternative methods.</p>
<dt><code>-r</code><i> pathname</i></p>
<dd> Used only with Internet-domain sockets, the pathname argument may be needed to inform XEmacs how to reach the root directory of a remote machine. <i>gnuclient</i> prepends this string to each path argument given. For example, if you were trying to edit a file on a client machine called otter, whose root directory was accessible from the server machine via the path /net/otter, then this argument should be set to &#8216;/net/otter&#8217;. If this option is omitted, then the value is taken from the environment variable GNU_NODE, if set, or the empty string otherwise.</p>
<dt><code>[+n] file</code></p>
<dd> This is the path of the file to be edited. If the file is a directory, then the directory browsers dired or monkey are usually invoked instead. The cursor is put at line number &#8216;n&#8217; if specified. </p>
</dl>
<h2>SETUP</h2>
<p> <i>gnuserv</i> is included with recent versions of XEmacs; no installation is required. The server must be started before clients may attempt to connect. Start the server by evaluating the Lisp form (gnuserv-start), or interactively by typing `M-x gnuserv-start&#8217;. </p>
<h2>CONFIGURATION</h2>
<p> The behavior of this suite of programs can be customized to a large extent. Type `M-x customize-group RET gnuserv RET&#8217;. More documentation can be found in the file `gnuserv.el&#8217; </p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd> gnuclient -q -f mh-smail<br />
 gnuclient -h cuckoo -r /ange [at] otter: /tmp/*<br />
 gnuclient -nw ../src/listproc.c</dl>
<p> More examples and sample wrapper scripts are provided in the etc/gnuserv directory of the XEmacs installation. </p>
<h2>SYSV IPC</h2>
<p> SysV IPC is a build-time option, enabled by defining the symbol SYSV_IPC at the top of gnuserv.h. It is used to communicate between <i>gnuclient</i> and <i>gnuserv</i>. It is incompatible with both Unix-domain and Internet-domain socket communication as described below. A file called /tmp/gsrv??? is created as a key for the message queue, and if removed will cause the communication between server and client to fail until the server is restarted.</p>
<h2>UNIX-DOMAIN SOCKETS</h2>
<p> Unix-domain sockets are a build-time option, enabled by defining the symbol UNIX_DOMAIN_SOCKETS at the top of gnuserv.h. A Unix-domain socket is used to communicate between <i>gnuclient</i> and <i>gnuserv</i>. A file called /tmp/gsrvdir????/gsrv is created for communication. If the symbol USE_TMPDIR is set at the top of gnuserv.h, $TMPDIR, when set, is used instead of /tmp. If that file is deleted, or TMPDIR has different values for the server and the client, communication between server and client will fail. Only the user running gnuserv will be able to connect to the socket.</p>
<h2>INTERNET-DOMAIN SOCKETS</h2>
<p> Internet-domain sockets are a build-time option, enabled by defining the symbol INTERNET_DOMAIN_SOCKETS at the top of gnuserv.h. Internet-domain sockets are used to communicate between <i>gnuclient</i> and <i>gnuserv</i>. Both Internet-domain and Unix-domain sockets can be used at the same time. If a hostname is specified via -h or via the GNU_HOST environment variable, <i>gnuclient</i> establish connections using an Internet domain socket. If not, a local connection is attempted via either a Unix-domain socket or SYSV IPC.</p>
<h2>SECURITY</h2>
<p> Using Internet-domain sockets, a more robust form of security is needed that wasn&#8217;t necessary with either Unix-domain sockets or SysV IPC. Currently, two authentication protocols are supported to provide this: MIT-MAGIC-COOKIE-1 (based on the X11 <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program) and a simple host-based access control mechanism, hereafter called GNUSERV-1. The GNUSERV-1 protocol is always available. Support for MIT-MAGIC-COOKIE-1 is enabled (by defining AUTH_MAGIC_COOKIE at the top of gnuserv.h. </p>
<p> <i>gnuserv</i>, using GNUSERV-1, performs a limited form of access control at the machine level. By default no Internet-domain socket is opened. If the variable GNU_SECURE can be found in <i>gnuserv</i>&#8216;s environment, and it names a readable filename, then this file is opened and assumed to be a list of hosts, one per line, from which the server will allow requests. Connections from any other host will be rejected. Even the machine on which <i>gnuserv</i> is running is not permitted to make connections via the Internet socket unless its hostname is explicitly specified in this file. Note that a host may be either a numeric IP address or a hostname, and that <i>any</i> user on an approved host may connect to your gnuserv and execute arbitrary Lisp (e.g., delete all your files). If this file contains a lot of hostnames then the server may take quite a long time to start up. </p>
<p> When the MIT-MAGIC-COOKIE-1 protocol is enabled, an Internet socket <i>is</i> opened by default. <i>gnuserv</i> will accept a connection from any host, and will wait for a &quot;magic cookie&quot; (essentially, a password) to be presented by the client. If the client doesn&#8217;t present the cookie, or if the cookie is wrong, the authentication of the client is considered to have failed. At this point. <i>gnuserv</i> falls back to the GNUSERV-1 protocol; If the client is calling from a host listed in the GNU_SECURE file, the connection will be accepted, otherwise it will be rejected.</p>
<dl>
<dt><i>Using MIT-MAGIC-COOKIE-1 authentication</i></p>
<dd> When the <i>gnuserv</i> server is started, it looks for a cookie defined for display 999 on the machine where it is running. If the cookie is found, it will be stored for use as the authentication cookie. These cookies are defined in an authorization file (usually ~/.Xauthority) that is manipulated by the X11 <a href="/docs/linux/man/1-xauth/">xauth</a>(1) program. For example, a machine &quot;kali&quot; which runs an emacs that invokes <i>gnuserv</i> should respond as follows (at the shell prompt) when set up correctly.</dl>
<dl>
<dt>
<dd> kali% xauth list<br />
 GS65.SP.CS.CMU.EDU:0 MIT-MAGIC-COOKIE-1 11223344<br />
 KALI.FTM.CS.CMU.EDU:999 MIT-MAGIC-COOKIE-1 1234</dl>
<dl>
<dt>
<dd> In the above case, the authorization file defines two cookies. The second one, defined for screen 999 on the server machine, is used for gnuserv authentication. </p>
<p> On the client machine&#8217;s side, the authorization file must contain an identical line, specifying the <i>server&#8217;s </i> cookie. In other words, on a machine &quot;foobar&quot; which wishes to connect to &quot;kali,&quot; the `xauth list&#8217; output should contain the line: </p>
<dl>
<dt>
<dd> KALI.FTM.CS.CMU.EDU:999 MIT-MAGIC-COOKIE-1 1234</dl>
<p> For more information on authorization files, take a look at the xauth(1X11) man page, or invoke xauth interactively (without any arguments) and type &quot;help&quot; at the prompt. Remember that case in the name of the authorization protocol (i.e.`MIT-MAGIC-COOKIE-1&#8242;) <i>is</i> significant!</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> Default X (or GTK) device for display of edit frame. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/tmp/gsrv???</code></p>
<dd> (SYSV_IPC only)</p>
<dt><code>/tmp/gsrvdir???/gsrv</code></p>
<dd> (unix domain sockets only)</p>
<dt><code>~/.xemacs/init.el</code></p>
<dd> XEmacs customization file, see <a href="/docs/linux/man/1-xemacs/">xemacs</a>(1).</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>xauth(1X11), Xsecurity(1X11), gnuserv.el</p>
<dd></dl>
<h2>BUGS</h2>
<p> NULs occurring in result strings don&#8217;t get passed back to gnudoit properly. </p>
<h2>AUTHOR.</h2>
<p> Andy Norman (ange [at] hplb.hpl.hp.com), based heavily upon etc/emacsclient.c, etc/server.c and lisp/server.el from the GNU Emacs 18.52 distribution. Various modifications from Bob Weiner (weiner [at] mot.com), Darrell Kindred (dkindred [at] cmu.edu), Arup Mukherjee (arup [at] cmu.edu), Ben Wing (ben [at] xemacs.org) and Hrvoje Niksic (hniksic [at] xemacs.org). </p>
<h2>Index</h2>
