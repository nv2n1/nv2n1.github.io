---
title: "fail2ban(1)"
name: "fail2ban"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fail2ban/"
description: "fail2ban – a set of server and client programs to limit brute force authentication attempts."
---

<h2>NAME</h2>
<p> fail2ban &#8211; a set of server and client programs to limit brute force authentication attempts.</p>
<h2>DESCRIPTION</h2>
<p> Fail2Ban consists of a client, server and configuration files to limit brute force authentication attempts. </p>
<p> The server program <code>fail2ban-server</code> is responsible for monitoring log files and issuing ban/unban commands. It gets configured through a simple protocol by <code>fail2ban-client</code>, which can also read configuration files and issue corresponding configuration commands to the server. </p>
<p> For details on the configuration of fail2ban see the <a href="/docs/linux/man/5-jail-conf/">jail.conf</a>(5) manual page. A jail (as specified in jail.conf) couples filters and actions definitions for any given list of files to get monitored. </p>
<p> For details on the command-line options of fail2ban-server see the <a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) manual page. </p>
<p> For details on the command-line options and commands for configuring the server via fail2ban-client see the <a href="/docs/linux/man/1-fail2ban-client/">fail2ban-client</a>(1) manual page. </p>
<p> For testing regular expressions specified in a filter using the fail2ban-regex program may be of use and its manual page is <a href="/docs/linux/man/1-fail2ban-regex/">fail2ban-regex</a>(1). </p>
<h2>LIMITATION</h2>
<p> Fail2Ban is able to reduce the rate of incorrect authentications attempts however it cannot eliminate the risk that weak authentication presents. Configure services to use only two factor or public/private authentication mechanisms if you really want to protect services. </p>
<p> A local user is able to inject messages into syslog and using a Fail2Ban jail that reads from syslog, they can effectively trigger a DoS attack against any IP. Know this risk and configure Fail2Ban/grant shell access accordingly. </p>
<h2>FILES</h2>
<p> <i>/etc/fail2ban/*</i></p>
<h2>AUTHOR</h2>
<p> Manual page written by Daniel Black and Yaroslav Halchenko</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/fail2ban/fail2ban/issues">https://github.com/fail2ban/fail2ban/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013<br />
 Copyright of modifications held by their respective authors. Licensed under the GNU General Public License v2 (GPL).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) <a href="/docs/linux/man/1-fail2ban-client/">fail2ban-client</a>(1) <a href="/docs/linux/man/1-fail2ban-regex/">fail2ban-regex</a>(1) <a href="/docs/linux/man/5-jail-conf/">jail.conf</a>(5) </p>
<h2>Index</h2>
