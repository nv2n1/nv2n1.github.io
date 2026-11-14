---
title: "zos-remote-conf(5)"
name: "zos-remote-conf"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zos-remote-conf/"
description: "zos-remote.conf – the audisp-racf plugin configuration file"
---

<p>zos-remote.conf &#8211; the audisp-racf plugin configuration file</p>
<h2>Description</h2>
<p><code>zos-remote.conf</code> controls the configuration for the <code><a href="/docs/linux/man/8-audispd-zos-remote/">audispd-zos-remote</a></code>(8) Audit dispatcher plugin. The default location for this file is <i>/etc/audisp/zos-remote.conf</i>, however, a different file can be specified as the first argument to the <code>audispd-zos-remote</code> plugin. See <code><a href="/docs/linux/man/8-audispd-zos-remote/">audispd-zos-remote</a></code>(8) and <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). The options available are as follows:</p>
<dl>
<dt><i>server</i></p>
<dd>This is the IBM z/OS ITDS server hostname or IP address</p>
<dt><i>port</i></p>
<dd>The port number where ITDS is running on the z/OS server. Default is 389 (ldap port)</p>
<dt><i>user</i></p>
<dd>The z/OS RACF user ID which the audispd-zos-remote plugin will use to perform Remote Audit requests. This user needs READ access to FACILITY Class resource IRR.LDAP.REMOTE.AUDIT (See <code><a href="/docs/linux/man/8-audispd-zos-remote/">audispd-zos-remote</a></code>(8)).</p>
<dt><i>password</i></p>
<dd>The password associated the the z/OS user ID configured above.</p>
<dt><i>timeout</i></p>
<dd>The number in seconds that <code>audispd-zos-remote</code> plugin will wait before giving up in connection attempts and event submissions. The default value is 15</p>
<dt><i>q_depth</i></p>
<dd>The <code>audispd-zos-remote</code> plugin will queue inputed events to the maximum of <i>q_depth</i> events while trying to submit those remotely. This can handle burst of events or in case of a slow network connection. However, the <code>audispd-zos-remote</code> plugin will drop events in case the queue is full. The default queue depth is 64 &#8211; Increase this value in case you are experiencing event drop due to full queue (<code>audispd-zos-remote</code> will log this to syslog).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd-zos-remote/">audispd-zos-remote</a></code>(8)</p>
<h2>Author</h2>
<p>Klaus Heinrich Kiwi &lt;klausk [at] br.ibm.com&gt;</p>
