---
title: "krb5_425_conv_principal(3)"
name: "krb5_425_conv_principal"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_425_conv_principal/"
description: "krb5_425_conv_principal krb5_425_conv_principal_ext krb5_524_conv_principal – converts to and from version 4 principals"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_425_conv_principal</code> <code>krb5_425_conv_principal_ext</code> <code>krb5_524_conv_principal</code> &#8211; converts to and from version 4 principals </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fn krb5_425_conv_principal krb5_context context const char *name const char *instance const char *realm krb5_principal *principal Ft krb5_error_code Fn krb5_425_conv_principal_ext krb5_context context const char *name const char *instance const char *realm krb5_boolean (*func)(krb5_context, krb5_principal) krb5_boolean resolve krb5_principal *principal Ft krb5_error_code Fn krb5_524_conv_principal krb5_context context const krb5_principal principal char *name char *instance char *realm</p>
<h2>DESCRIPTION</h2>
<p> Converting between version 4 and version 5 principals can at best be described as a mess. </p>
<p> A version 4 principal consists of a name, an instance, and a realm. A version 5 principal consists of one or more components, and a realm. In some cases also the first component/name will differ between version 4 and version 5. Furthermore the second component of a host principal will be the fully qualified domain name of the host in question, while the instance of a version 4 principal will only contain the first part (short hostname). Because of these problems the conversion between principals will have to be site customized. </p>
<p> Fn krb5_425_conv_principal_ext will try to convert a version 4 principal, given by Fa name , Fa instance , and Fa realm , to a version 5 principal. This can result in several possible principals, and if Fa func is non-NULL, it will be called for each candidate principal. Fa func should return true if the principal was &#8220;good&#8221; To accomplish this, Fn krb5_425_conv_principal_ext will look up the name in krb5.conf It first looks in the <code>v4_name_convert/host</code> subsection, which should contain a list of version 4 names whose instance should be treated as a hostname. This list can be specified for each realm (in the <code>realms</code> section), or in the <code>libdefaults</code> section. If the name is found the resulting name of the principal will be the value of this binding. The instance is then first looked up in <code>v4_instance_convert</code> for the specified realm. If found the resulting value will be used as instance (this can be used for special cases), no further attempts will be made to find a conversion if this fails (with Fa func ) . If the Fa resolve parameter is true, the instance will be looked up with Fn gethostbyname . This can be a time consuming, error prone, and unsafe operation. Next a list of hostnames will be created from the instance and the <code>v4_domains</code> variable, which should contain a list of possible domains for the specific realm. </p>
<p> On the other hand, if the name is not found in a <code>host</code> section, it is looked up in a <code>v4_name_convert/plain</code> binding. If found here the name will be converted, but the instance will be untouched. </p>
<p> This list of default host-type conversions is compiled-in: </p>
<blockquote>
<pre><code>
v4_name_convert = {
    host = {
        ftp = ftp
            hprop = hprop
                imap = imap
                    pop = pop
                        rcmd = host
                            smtp = smtp}}
</code></pre>
</blockquote>
<p> It will only be used if there isn&#8217;t an entry for these names in the config file, so you can override these defaults. </p>
<p> Fn krb5_425_conv_principal will call Fn krb5_425_conv_principal_ext with <code>NULL</code> as Fa func , and the value of <code>v4_instance_resolve</code> (from the <code>libdefaults</code> section) as Fa resolve . </p>
<p> Fn krb5_524_conv_principal basically does the opposite of Fn krb5_425_conv_principal , it just doesn&#8217;t have to look up any names, but will instead truncate instances found to belong to a host principal. The Fa name , Fa instance , and Fa realm should be at least 40 characters long.</p>
<h2>EXAMPLES</h2>
<p> Since this is confusing an example is in place. </p>
<p> Assume that we have the &#8220;foo.com&#8221; and &#8220;bar.com&#8221; domains that have shared a single version 4 realm, FOO.COM. The version 4 krb.realms file looked like: </p>
<blockquote>
<pre>
foo.com         FOO.COM
.foo.com        FOO.COM
.bar.com        FOO.COM
</pre>
</blockquote>
<p> A krb5.conf file that covers this case might look like: </p>
<blockquote><p>
[libdefaults] v4_instance_resolve = yes<br />
                                        [realms] FOO.COM = {<br />
    kdc = kerberos.foo.com<br />
              v4_instance_convert = {<br />
        foo = foo.com} v4_domains = foo.com}
 </p></blockquote>
<p> With this setup and the following host table: </p>
<blockquote>
<pre>
foo.com
a-host.foo.com
b-host.bar.com
</pre>
</blockquote>
<p> the following conversions will be made: </p>
<blockquote>
<pre><code>
rcmd.a - host-&gt;host / a - host.foo.com ftp.b - host-&gt;ftp / b - host.bar.com pop.foo-&gt;pop / foo.com ftp.other-&gt;ftp / other.foo.com other.a - host-&gt;other / a - host
</code></pre>
</blockquote>
<p> The first three are what you expect. If you remove the &#8220;v4_domains&#8221; the fourth entry will result in an error (since the host &#8220;other&#8221; can&#8217;t be found). Even if &#8220;a-host&#8221; is a valid host name, the last entry will not be converted, since the &#8220;other&#8221; name is not known to represent a host-type principal. If you turn off &#8220;v4_instance_resolve&#8221; the second example will result in &#8220;ftp/b-host.foo.com&#8221; (because of the default domain). And all of this is of course only valid if you have working name resolving.</p>
<h2>SEE ALSO</h2>
<p> krb5_build_principal3, krb5_free_principal3, krb5_parse_name3, krb5_sname_to_principal3, krb5_unparse_name3, krb5.conf5 </p>
<h2>Index</h2>
