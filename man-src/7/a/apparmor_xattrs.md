---
title: "apparmor_xattrs(7)"
name: "apparmor_xattrs"
section: "7"
letter: "a"
url: "/docs/linux/man/7-apparmor_xattrs/"
description: "apparmor_xattrs – AppArmor profile"
---

<p>apparmor_xattrs &#8211; AppArmor profile </p>
<p> <a href="/docs/linux/man/7-xattr/">xattr</a>(7) matching</p>
<h2>Description</h2>
<p>AppArmor profiles can conditionally match files based on the presence and value of extended attributes in addition to file path. The following profile applies to any file under &#8220;/usr/bin&#8221; where the &#8220;security.apparmor&#8221; extended attribute has the value &#8220;trusted&#8221;: </p>
<pre><code>profile trusted /usr/bin/* xattrs=(security.apparmor=&quot;trusted&quot;) {
# ...
}</code></pre>
<p> Note that &#8220;security.apparmor&#8221; and &#8220;trusted&#8221; are arbitrary, and profiles can match based on the value of any attribute. The xattrs value may also contain a path regex: profile trusted /usr/bin/* xattrs=(user.trust=&quot;tier/*&quot;) {</p>
<p># &#8230;<br />
} The <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1) and <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1) tools can be used to view and manage xattr values: $ setfattr -n &#8216;security.apparmor&#8217; -v &#8216;trusted&#8217; /usr/bin/example-tool<br />
$ getfattr &#8211;absolute-names -d -m &#8211; /usr/bin/example-tool<br />
# file: usr/bin/example-tool<br />
security.apparmor=&quot;trusted&quot; The priority of each profile is determined by the length of the path, then the number of xattrs specified. A more specific path is preferred over xattr matches: </p>
<pre><code># Highest priority, longest path.
profile example1 /usr/bin/example-tool {
# ...
}

# Lower priority than the longer path, but higher priority than a rule
# with fewer xattr matches.
profile example2 /usr/** xattrs=(
security.apparmor=&quot;trusted&quot;
user.domain=&quot;**&quot;
) {
# ...
}

# Lowest priority. Same path length as the second profile, but has
# fewer xattr matches.
profile example2 /usr/** {
# ...
}</code></pre>
<p> xattr matching requires the following kernel feature: </p>
<pre> /sys/kernel/security/apparmor/features/domain/attach_conditions/xattr</pre>
<h2>Known Issues</h2>
<p>AppArmor profiles currently can&#8217;t reliably match extended attributes with binary values such as security.evm and security.ima. In the future AppArmor may gain the ability to match based on the presence of certain attributes while ignoring their values.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apparmor/">apparmor</a></code>(8), <code><a href="/docs/linux/man/8-apparmor_parser/">apparmor_parser</a></code>(8), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7), <code><a href="/docs/linux/man/1-aa-autodep/">aa-autodep</a></code>(1), <code><a href="/docs/linux/man/1-clean/">clean</a></code>(1), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
