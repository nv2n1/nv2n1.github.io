---
title: "oddjobd(5)"
name: "oddjobd"
section: "5"
letter: "o"
url: "/docs/linux/man/5-oddjobd/"
description: "oddjobd.conf – configuration for oddjobd"
---

<p>oddjobd.conf &#8211; configuration for oddjobd</p>
<h2>Description</h2>
<p>The <code>/etc/oddjobd.conf</code> configuration file specifies which services the <i>oddjobd</i> server provides over the D-Bus, and authorization rules which are enforced in addition to those enforced by the system message bus. The configuration file is an XML document. The top-level element type is <i>&lt;oddjobconfig&gt;</i>, which contains one or more <i>&lt;service&gt;</i> elements. Each <i>&lt;service&gt;</i> describes a service which will be provided on the system-wide message bus. Each <i>&lt;object&gt;</i> describes an object path which will will be recognized by the specified service. The object path may include wildcards, in which case any call to an object with a path name which matches the specified path will be accepted. An object contains one or more <i>&lt;interface&gt;</i> elements, each of which describes a group of methods described in <i>&lt;method&gt;</i> elements. Each <i>&lt;method&gt;</i> element must specify the method name as a value for its <i>name</i> attribute and may include a <i>&lt;helper</i>&gt; element which the name of an executable to run as its <i>exec</i> attribute and the number of arguments which will be passed to the helper as its <i>argument</i> attribute. A <i>&lt;helper&gt;</i> may also include attributes indicating whether or not the invoking user&#8217;s name should be prepended to that argument list, and whether that argument list should be passed in to the helper via stdin (the default) or on its command line. Each <i>&lt;oddjobconfig&gt;</i>, <i>&lt;service&gt;</i>, <i>&lt;object&gt;</i>, <i>&lt;interface&gt;</i>, or <i>&lt;method&gt;</i> element may also include authorization elements <i>&lt;allow&gt;</i> and <i>&lt;deny&gt;</i>. Each <i>&lt;allow&gt;</i> or <i>&lt;deny&gt;</i> rule specifies some combination of a user name and/or a UID range which the invoking user must match for the rule to apply. A rule can also specify the caller&#8217;s SELinux context, user, role, or execution domain, and be applied or not based on whether or not policy is being enforced. All <i>&lt;deny&gt;</i> rules for the method are checked first, followed by all of its <i>&lt;allow&gt;</i> rules. If no matches are found, the <i>&lt;deny&gt;</i> rules for the containing <i>&lt;interface&gt;</i> element are checked, followed by its <i>&lt;allow&gt;</i> rules, and so on. If all ACLs are searched and no matches turn up, access is denied. The <i>oddjobd</i> server will automatically supply information used by the D-Bus introspection mechanism on behalf of your objects, but only if the client which is requesting the information is allowed to invoke the <i>Introspect</i> method of the <i>org.freedesktop.DBus.Introspectable</i> interface provided by the object. The configuration file may also indicate that the contents of other files should be read by the configuration parser, using an <i>&lt;include&gt;</i> element. </p>
<h2>Examples</h2>
<p>Here is an example file:<br />
&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&lt;oddjobconfig/&gt; Another:<br />
&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&lt;oddjobconfig&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;allow user=&quot;wally&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;service name=&quot;com.redhat.oddjob&quot;&gt;<br />
&lt;allow user=&quot;polly&quot;/&gt;<br />
&lt;object name=&quot;/com/redhat/oddjob&quot;&gt;<br />
&nbsp;<wbr>&lt;allow user=&quot;holly&quot;/&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;com.redhat.oddjob&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;allow user=&quot;bob&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;method name=&quot;pwd&quot;&gt;<br />
&lt;helper exec=&quot;/bin/pwd&quot;&nbsp;<wbr>argument_count=&quot;0&quot;&nbsp;<wbr>prepend_user_name=&quot;no&quot;/&gt;<br />
&lt;allow user=&quot;jimmy&quot;/&gt;<br />
&lt;allow user=&quot;billy&quot;/&gt;<br />
&lt;allow min_uid=&quot;0&quot;&nbsp;<wbr>max_uid=&quot;1000&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/method&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;method name=&quot;reboot&quot;&gt;<br />
&lt;helper exec=&quot;/sbin/reboot&quot;&nbsp;<wbr>argument_count=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/method&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;org.freedesktop.DBus.Introspectable&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;allow min_uid=&quot;0&quot;&nbsp;<wbr>max_uid=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&lt;/object&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/service&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;include ignore_missing=&quot;yes&quot;&gt;/etc/oddjobd-local.conf&lt;/include&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;include ignore_missing=&quot;yes&quot;&gt;/etc/oddjobd.conf.d/*.conf&lt;/include&gt;<br />
&nbsp;<wbr>&lt;/oddjobconfig&gt; And another:<br />
&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&lt;oddjobconfig&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;service name=&quot;com.example.management&quot;&gt;<br />
&lt;object name=&quot;/com/example/power&quot;&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;com.example.shutdown&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;method name=&quot;reboot&quot;&gt;<br />
&lt;allow user=&quot;root&quot;/&gt;<br />
&lt;helper exec=&quot;/sbin/reboot&quot;&nbsp;<wbr>argument_count=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/method&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;org.freedesktop.DBus.Introspectable&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;allow min_uid=&quot;0&quot;&nbsp;<wbr>max_uid=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&lt;/object&gt;<br />
&lt;object name=&quot;/com/example/power&quot;&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;com.example.shutdown&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;method name=&quot;poweroff&quot;&gt;<br />
&lt;allow user=&quot;root&quot;/&gt;<br />
&lt;helper exec=&quot;/sbin/poweroff&quot;&nbsp;<wbr>argument_count=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/method&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&nbsp;<wbr>&lt;interface name=&quot;org.freedesktop.DBus.Introspectable&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;allow min_uid=&quot;0&quot;&nbsp;<wbr>max_uid=&quot;0&quot;/&gt;<br />
&nbsp;<wbr>&lt;/interface&gt;<br />
&lt;/object&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/service&gt;<br />
&nbsp;<wbr>&lt;/oddjobconfig&gt; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oddjob_request/">oddjob_request</a></code>(1) <code><a href="/docs/linux/man/5-oddjob-conf/">oddjob.conf</a></code>(5) <code><a href="/docs/linux/man/8-oddjobd/">oddjobd</a></code>(8) </p>
