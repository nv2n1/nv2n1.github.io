---
title: "rlm_mschap(5)"
name: "rlm_mschap"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_mschap/"
description: "rlm_mschap – FreeRADIUS Module"
---

<p>rlm_mschap &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_mschap</i> module provides MS-CHAP and MS-CHAPv2 authentication support. This module validates a user with MS-CHAP or MS-CHAPv2 authentication. If called in Authorize, it will look for MS-CHAP Challenge/Response attributes in the Acess-Request and adds an Auth-Type attribute set to MS-CHAP in the Config-Items list unless Auth-Type has already set. The module can authenticate the MS-CHAP session via plain-text passwords (User-Password attribute), or NT passwords (NT-Password attribute). The module cannot perform authentication against an NT domain. The module also enforces the SMB-Account-Ctrl attribute. See the Samba documentation for the meaning of SMB account control. The module does not read Samba password files. Instead, the fIrlm_passwd module can be used to read a Samba password file, and supply an NT-Password attribute which this module can use. The main configuration items to be aware of are:</p>
<dl>
<dt>authtype</dt>
<dd>This is the string used to set the authtype. Normally it should be left to the default value of MS-CHAP.</dd>
<dt>use_mppe</dt>
<dd>Unless this is set to &#8216;no&#8217;, FreeRADIUS will add MS-CHAP-MPPE-Keys for MS-CHAPv1 and MS-MPPE-Recv-Key/MS-MPPE-Send-Key for MS-CHAPv2. The default is &#8216;yes&#8217;.</dd>
<dt>require_encryption</dt>
<dd>If MPPE is enabled, setting this attribute to &#8216;yes&#8217; will cause the MS-MPPE-Encryption-Policy attribute to be set to require encryption. The default is &#8216;no&#8217;.</dd>
<dt>require_strong</dt>
<dd>If MPPE is enabled, setting this attribute to &#8216;yes&#8217; will cause the MS-MPPE-Encryption-Types attribute to be set to require a 128 bit key. The default is &#8216;no&#8217;.</dd>
<dt>with_ntdomain_hack</dt>
<dd>Windows clients send User-Name in the form of &quot;DOMAIN\User&quot;, but send the challenge/response based only on the User portion. Setting this value to yes, enables a work-around for this error. The default is &#8216;no&#8217;.  </dd></dl>
 <h2>CONFIGURATION</h2>
 <dl>
<dd>  <pre><code>modules {
  ...

  mschap {

        authtype = MS-CHAP

        use_mppe = yes

  }

  ...

}

 ...

authorize {
  ...

  mschap

  ...

}
 ...

authenticate {
  ...

  mschap

  ...

}
</code></pre>
  </dd></dl>
 <h2>SECTIONS</h2>
 <code>authorization,</code> <code>authentication</code> <h2>FILES</h2>
 <i>/etc/raddb/radiusd.conf</i> <h2>SEE ALSO</h2>
 <code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd.conf/">radiusd.conf</a></code>(5)  <h2>AUTHOR</h2>
 Chris Parker, cparker [at] segv.org 
