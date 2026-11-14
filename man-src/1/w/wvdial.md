---
title: "wvdial(1)"
name: "wvdial"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvdial/"
description: "wvdial – PPP dialer with built-in intelligence."
---

<h2 class="name">NAME</h2>
<p> wvdial &#8211; PPP dialer with built-in intelligence. </p>
<h2>SYNOPSIS</h2>
<p> <code>wvdial</code> [ <i>OPTIONS</i> ] [ <i>SECTION</i> ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>wvdial</code> is an intelligent PPP dialer, which means that it dials a modem and starts PPP in order to connect to the Internet. It is something like the <code><a href="/docs/linux/man/8-chat/">chat</a></code>(8) program, except that it uses heuristics to guess how to dial and log into your server rather than forcing you to write a login script. </p>
<p> When <code>wvdial</code> starts, it first loads its configuration from <i>/etc/wvdial.conf</i> and <i>~/.wvdialrc</i> which contains basic information about the modem port, speed, and init string, along with information about your Internet Service Provider (ISP), such as the phone number, your username, and your password. </p>
<p> Then it initializes your modem and dials the server and waits for a connection (a CONNECT string from the modem). It understands and responds to typical connection problems (like BUSY and NO DIALTONE). </p>
<p> Any time after connecting, <code>wvdial</code> will start PPP if it sees a PPP sequence from the server. Otherwise, it tries to convince the server to start PPP by doing the following:</p>
<dl>
<dt>&bull;</p>
<dd> responding to any login/password prompts it sees;</p>
<dt>&bull;</p>
<dd> interpreting &#8220;choose one of the following&#8221;-style menus;</p>
<dt>&bull;</p>
<dd> eventually, sending the word &#8220;ppp&#8221; (a common terminal server command).</dl>
<p> If all of this fails, <code>wvdial</code> just runs <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) and hopes for the best. It will bring up the connection, and then wait patiently for you to drop the link by pressing CTRL-C.</p>
<h2>OPTIONS</h2>
<p> Several options are recognized by <code>wvdial</code>.</p>
<dl>
<dt><code>-c, &#8211;chat</code></p>
<dd> Run wvdial as a chat replacement from within pppd, instead of the more normal method of having wvdial negotiate the connection and then call pppd.</p>
<dt><code>-C, &#8211;config=CONFIGFILE</code></p>
<dd> Run wvdial with CONFIGFILE as the configuration file, instead of <i>/etc/wvdial.conf</i>. This is mainly useful only if you want to have per-user configurations, or you want to avoid having dial-up information (usernames, passwords, calling card numbers, etc.) in a system wide configuration file.</p>
<dt><code>&#8211;remotename</code></p>
<dd> Override the Remote Name setting in the dialer configuration section of the configuration file. This is mainly useful when you dial to multiple systems with the same user name and password, and you don&#8217;t want to use inheritance to override this setting (which is the recommended way to do it).</p>
<dt><code>-n, &#8211;no-syslog</code></p>
<dd> Don&#8217;t output debug information to the syslog daemon (only useful together with &#8211;chat).</dl>
<p> <code>wvdial</code> is normally run without command line options, in which case it reads its configuration from the <i>[Dialer Defaults]</i> section of <i>/etc/wvdial.conf</i>. (The configuration file is described in more detail in <code><a href="/docs/linux/man/5-wvdial-conf/">wvdial.conf</a></code>(5) manual page.) </p>
<p> One or more <i>SECTION</i>s of <i>/etc/wvdial.conf</i> may be specified on the command line. Settings in these sections will override settings in <i>[Dialer Defaults]</i>. </p>
<p> For example, the command:</p>
<dl>
<dt>
<dd> <code>wvdial phone2</code></dl>
<p> will read default options from the <i>[Dialer Defaults]</i> section, then override any or all of the options with those found in the <i>[Dialer phone2]</i> section. </p>
<p> If more than one section is specified, they are processed in the order they are given. Each section will override all the sections that came before it. </p>
<p> For example, the command:</p>
<dl>
<dt>
<dd> <code>wvdial phone2 pulse shh</code></dl>
<p> will read default options from the <i>[Dialer Defaults]</i> section, then override any or all of the options with those found in the <i>[Dialer phone2]</i> section, followed by the <i>[Dialer pulse]</i> section, and lastly the <i>[Dialer shh]</i> section. </p>
<p> Using this method, it is possible to easily configure <code>wvdial</code> to switch between different internet providers, modem init strings, account names, and so on without specifying the same configuration information over and over.</p>
<h2>BUGS</h2>
<p> &#8220;Intelligent&#8221; programs are frustrating when they don&#8217;t work right. This version of <code>wvdial</code> has only minimal support for disabling or overriding its &#8220;intelligence&#8221;, with the &#8220;Stupid Mode&#8221;, &#8220;Login Prompt&#8221;, and &#8220;Password Prompt&#8221; options. So, in general if you have a nice ISP, it will probably work, and if you have a weird ISP, it might not. </p>
<p> Still, it&#8217;s not much good if it doesn&#8217;t work for you, right? Don&#8217;t be fooled by the fact that <code>wvdial</code> finally made it to version 1.00; it could well contain many bugs and misfeatures. Let us know if you have problems by sending e-mail to <code>&lt;wvdial-list [at] lists.nit.ca&gt;</code>. </p>
<p> You may encounter some error messages if you don&#8217;t have write access to <code>/etc/ppp/pap-secrets</code> and <code>/etc/ppp/chap-secrets</code>. Unfortunately, there&#8217;s really no nice way around this yet.</p>
<h2>FILES</h2>
<dl>
<dt>/etc/wvdial.conf</p>
<dd> Configuration file which contains modem, dialing, and login information. See <code><a href="/docs/linux/man/5-wvdial-conf/">wvdial.conf</a></code>(5).</p>
<dt>/dev/ttyS*</p>
<dd> Serial port devices.</p>
<dt>/etc/ppp/peers/wvdial</p>
<dd> Required for correct authentication in pppd version 2.3.0 or newer.</p>
<dt>/etc/ppp/{pap,chap}-secrets</p>
<dd> Contains a list of usernames and passwords used by pppd for authentication. <code>wvdial</code> maintains this list automatically.</dl>
<h2>AUTHORS</h2>
<p> Dave Coombs and Avery Pennarun for Net Integration Technologies. We would also like to thank SuSE and RedHat for adding a number of various cool features to <code>wvdial</code>. Thanks guys!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-wvdial-conf/">wvdial.conf</a></code>(5), <code><a href="/docs/linux/man/1-wvdialconf/">wvdialconf</a></code>(1), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-chat/">chat</a></code>(8). </p>
<h2>Index</h2>
