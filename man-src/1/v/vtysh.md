---
title: "vtysh(1)"
name: "vtysh"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vtysh/"
description: "vtysh – a integrated shell for Quagga routing software"
---

<h2>NAME</h2>
<p> vtysh &#8211; a integrated shell for Quagga routing software</p>
<h2>SYNOPSIS</h2>
<p> <code>vtysh</code> [ <code>-b</code> ]<br />
 <code>vtysh</code> [ <code>-E</code> ] [ <code>-d</code> <i>daemon</i> ] ] [ <code>-c</code> <i>command</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>vtysh</code> is a integrated shell for <code>Quagga</code> routing engine.</p>
<h2>OPTIONS</h2>
<p> Options available for the <code>vtysh</code> command:</p>
<dl>
<dt><code>-b, &#8211;boot</code></p>
<dd> Execute boot startup configuration. It makes sense only if integrated config file is in use (not default in Quagga). See Info file <code>Quagga</code> for more info.</p>
<dt><code>-c, &#8211;command </code><i>command</i></p>
<dd> Specify command to be executed under batch mode. It behaves like -c option in any other shell &#8211; <i>command</i> is executed and <code>vtysh</code> exits. </p>
<p> It&#8217;s useful for gathering info from Quagga routing software or reconfiguring daemons from inside shell scripts, etc. Note that multiple commands may be executed by using more than one -c option and/or embedding linefeed characters inside the <i>command</i> string.</p>
<dt><code>-d, &#8211;daemon </code><i>daemon_name</i></p>
<dd> Specify which daemon to connect to. By default, <code>vtysh</code> attempts to connect to all Quagga daemons running on the system. With this flag, one can specify a single daemon to connect to instead. For example, specifying &#8216;-d ospfd&#8217; will connect only to ospfd. This can be particularly useful inside scripts with -c where the command is targeted for a single daemon.</p>
<dt><code>-e, &#8211;execute </code><i>command</i></p>
<dd> Alias for -c. It&#8217;s here only for compatibility with Zebra routing software and older Quagga versions. This will be removed in future.</p>
<dt><code>-E, &#8211;echo</code></p>
<dd> When the -c option is being used, this flag will cause the standard <code>vtysh</code> prompt and command to be echoed prior to displaying the results. This is particularly useful to separate the results when executing multiple commands.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a usage message on standard output and exit.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>VTYSH_PAGER</code></p>
<dd> This should be the name of the pager to use. Default is <code>more</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/local/etc/vtysh.conf</code></p>
<dd> The default location of the <code>vtysh</code> config file.</p>
<dt><code>/usr/local/etc/Quagga.conf</code></p>
<dd> The default location of the integrated Quagga routing engine config file if integrated config file is in use (not default).</dl>
<h2>WARNING</h2>
<p> This man page is intended to be a quick reference for command line options. The definitive document is the Info file <code>Quagga</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-bgpd/">bgpd</a></code>(8), <code><a href="/docs/linux/man/8-ripd/">ripd</a></code>(8), <code><a href="/docs/linux/man/8-ripngd/">ripngd</a></code>(8), <code><a href="/docs/linux/man/8-ospfd/">ospfd</a></code>(8), <code><a href="/docs/linux/man/8-ospf6d/">ospf6d</a></code>(8), <code><a href="/docs/linux/man/8-isisd/">isisd</a></code>(8), <code><a href="/docs/linux/man/8-zebra/">zebra</a></code>(8)</p>
<h2>BUGS</h2>
<p> <code>vtysh</code> eats bugs for breakfast. If you have food for the maintainers try <code><a rel="nofollow" href="http://bugzilla.quagga.net">http://bugzilla.quagga.net</a></code></p>
<h2>AUTHORS</h2>
<p> See <code><a rel="nofollow" href="http://www.zebra.org">http://www.zebra.org</a></code> and <code><a rel="nofollow" href="http://www.quagga.net">http://www.quagga.net</a></code> or the Info file for an accurate list of authors. </p>
<h2>Index</h2>
