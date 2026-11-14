---
title: "slapo-ppolicy(5)"
name: "slapo-ppolicy"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-ppolicy/"
description: "slapo-ppolicy – Password Policy overlay to slapd"
---

<p>slapo-ppolicy &#8211; Password Policy overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>ppolicy</code> overlay is an implementation of the most recent IETF Password Policy proposal for LDAP. When instantiated, it intercepts, decodes and applies specific password policy controls to overall use of a backend database, changes to user password fields, etc. The overlay provides a variety of password control mechanisms. They include password aging &#8212; both minimum and maximum ages, password reuse and duplication control, account time-outs, mandatory password resets, acceptable password content, and even grace logins. Different groups of users may be associated with different password policies, and there is no limit to the number of password policies that may be created. Note that some of the policies do not take effect when the operation is performed with the <code>rootdn</code> identity; all the operations, when performed with any other identity, may be subjected to constraints, like access control. Note that the IETF Password Policy proposal for LDAP makes sense when considering a single-valued password attribute, while the userPassword attribute allows multiple values. This implementation enforces a single value for the userPassword attribute, despite its specification. </p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> configuration options apply to the ppolicy overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>ppolicy_default &lt;policyDN&gt;</code></p>
<dd>Specify the DN of the pwdPolicy object to use when no specific policy is set on a given user&#8217;s entry. If there is no specific policy for an entry and no default is given, then no policies will be enforced.</p>
<dt><code>ppolicy_forward_updates</code></p>
<dd>Specify that policy state changes that result from Bind operations (such as recording failures, lockout, etc.) on a consumer should be forwarded to a master instead of being written directly into the consumer&#8217;s local database. This setting is only useful on a replication consumer, and also requires the <code>updateref</code> setting and <code>chain</code> overlay to be appropriately configured.</p>
<dt><code>ppolicy_hash_cleartext</code></p>
<dd>Specify that cleartext passwords present in Add and Modify requests should be hashed before being stored in the database. This violates the X.500/LDAP information model, but may be needed to compensate for LDAP clients that don&#8217;t use the Password Modify extended operation to manage passwords. It is recommended that when this option is used that compare, search, and read access be denied to all directory users.</p>
<dt><code>ppolicy_use_lockout</code></p>
<dd>A client will always receive an LDAP <code>InvalidCredentials</code> response when Binding to a locked account. By default, when a Password Policy control was provided on the Bind request, a Password Policy response will be included with no special error code set. This option changes the Password Policy response to include the <code>AccountLocked</code> error code. Note that sending the <code>AccountLocked</code> error code provides useful information to an attacker; sites that are sensitive to security issues should not enable this option. </p>
</dl>
<h2>Object Class</h2>
<p>The <code>ppolicy</code> overlay depends on the <code>pwdPolicy</code> object class. The definition of that class is as follows: </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.2.1<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;pwdPolicy&#8217;<br />
&nbsp;<wbr>AUXILIARY<br />
&nbsp;<wbr>SUP top<br />
&nbsp;<wbr>MUST&nbsp;<wbr>(&nbsp;<wbr>pwdAttribute&nbsp;<wbr>)<br />
&nbsp;<wbr>MAY&nbsp;<wbr>(<br />
&nbsp;<wbr>&nbsp;<wbr>pwdMinAge&nbsp;<wbr>$&nbsp;<wbr>pwdMaxAge&nbsp;<wbr>$&nbsp;<wbr>pwdInHistory&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdCheckQuality&nbsp;<wbr>$&nbsp;<wbr>pwdMinLength&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdExpireWarning&nbsp;<wbr>$&nbsp;<wbr>pwdGraceAuthnLimit&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdLockout&nbsp;<wbr>$&nbsp;<wbr>pwdLockoutDuration&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdMaxFailure&nbsp;<wbr>$&nbsp;<wbr>pwdFailureCountInterval&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdMustChange&nbsp;<wbr>$&nbsp;<wbr>pwdAllowUserChange&nbsp;<wbr>$<br />
&nbsp;<wbr>&nbsp;<wbr>pwdSafeModify&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> This implementation also provides an additional <code>pwdPolicyChecker</code> objectclass, used for password quality checking (see below). </p>
<dl>
<dd>( 1.3.6.1.4.1.4754.2.99.1<br />
&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;pwdPolicyChecker&#8217;<br />
&nbsp;<wbr>AUXILIARY<br />
&nbsp;<wbr>SUP top<br />
&nbsp;<wbr>MAY&nbsp;<wbr>(&nbsp;<wbr>pwdCheckModule&nbsp;<wbr>)&nbsp;<wbr>)</dl>
<p> Every account that should be subject to password policy control should have a <code>pwdPolicySubentry</code> attribute containing the DN of a valid <code>pwdPolicy</code> entry, or they can simply use the configured default. In this way different users may be managed according to different policies.</p>
<h2>Object Class Attributes</h2>
<p>Each one of the sections below details the meaning and use of a particular attribute of this <code>pwdPolicy</code> object class. </p>
<p> <code>pwdAttribute</code> </p>
<p> This attribute contains the name of the attribute to which the password policy is applied. For example, the password policy may be applied to the <code>userPassword</code> attribute. </p>
<p> Note: in this implementation, the only value accepted for <code>pwdAttribute</code> is <i> userPassword .</i> </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.1<br />
NAME&nbsp;<wbr>&#8216;pwdAttribute&#8217;<br />
EQUALITY objectIdentifierMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.38&nbsp;<wbr>)</dl>
<p> <code>pwdMinAge</code> </p>
<p> This attribute contains the number of seconds that must elapse between modifications allowed to the password. If this attribute is not present, zero seconds is assumed (i.e. the password may be modified whenever and however often is desired). </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.2<br />
NAME&nbsp;<wbr>&#8216;pwdMinAge&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdMaxAge</code> </p>
<p> This attribute contains the number of seconds after which a modified password will expire. If this attribute is not present, or if its value is zero (0), then passwords will not expire. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.3<br />
NAME&nbsp;<wbr>&#8216;pwdMaxAge&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdInHistory</code> </p>
<p> This attribute is used to specify the maximum number of used passwords that will be stored in the <code>pwdHistory</code> attribute. If the <code>pwdInHistory</code> attribute is not present, or if its value is zero (0), used passwords will not be stored in <code>pwdHistory</code> and thus any previously-used password may be reused. No history checking occurs if the password is being modified by the <code>rootdn</code>, although the password is saved in the history. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.4<br />
NAME&nbsp;<wbr>&#8216;pwdInHistory&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdCheckQuality</code> </p>
<p> This attribute indicates if and how password syntax will be checked while a password is being modified or added. If this attribute is not present, or its value is zero (0), no syntax checking will be done. If its value is one (1), the server will check the syntax, and if the server is unable to check the syntax, whether due to a client-side hashed password or some other reason, it will be accepted. If its value is two (2), the server will check the syntax, and if the server is unable to check the syntax it will return an error refusing the password. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.5<br />
NAME&nbsp;<wbr>&#8216;pwdCheckQuality&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdMinLength</code> </p>
<p> When syntax checking is enabled (see also the <code>pwdCheckQuality</code> attribute), this attribute contains the minimum number of characters that will be accepted in a password. If this attribute is not present, minimum password length is not enforced. If the server is unable to check the length of the password, whether due to a client-side hashed password or some other reason, the server will, depending on the value of <code>pwdCheckQuality</code>, either accept the password without checking it (if <code>pwdCheckQuality</code> is zero (0) or one (1)) or refuse it (if <code>pwdCheckQuality</code> is two (2)). </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.6<br />
NAME&nbsp;<wbr>&#8216;pwdMinLength&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdExpireWarning</code> </p>
<p> This attribute contains the maximum number of seconds before a password is due to expire that expiration warning messages will be returned to a user who is authenticating to the directory. If this attribute is not present, or if the value is zero (0), no warnings will be sent. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.7<br />
NAME&nbsp;<wbr>&#8216;pwdExpireWarning&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdGraceAuthnLimit</code> </p>
<p> This attribute contains the number of times that an expired password may be used to authenticate a user to the directory. If this attribute is not present or if its value is zero (0), users with expired passwords will not be allowed to authenticate to the directory. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.8<br />
NAME&nbsp;<wbr>&#8216;pwdGraceAuthnLimit&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdLockout</code> </p>
<p> This attribute specifies the action that should be taken by the directory when a user has made a number of failed attempts to authenticate to the directory. If <code>pwdLockout</code> is set (its value is &quot;TRUE&quot;), the user will not be allowed to attempt to authenticate to the directory after there have been a specified number of consecutive failed bind attempts. The maximum number of consecutive failed bind attempts allowed is specified by the <code>pwdMaxFailure</code> attribute. If <code>pwdLockout</code> is not present, or if its value is &quot;FALSE&quot;, the password may be used to authenticate no matter how many consecutive failed bind attempts have been made. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.9<br />
NAME&nbsp;<wbr>&#8216;pwdLockout&#8217;<br />
EQUALITY booleanMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.7<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdLockoutDuration</code> </p>
<p> This attribute contains the number of seconds during which the password cannot be used to authenticate the user to the directory due to too many consecutive failed bind attempts. (See also <code>pwdLockout</code> and <code>pwdMaxFailure</code>.) If <code>pwdLockoutDuration</code> is not present, or if its value is zero (0), the password cannot be used to authenticate the user to the directory again until it is reset by an administrator. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.10<br />
NAME&nbsp;<wbr>&#8216;pwdLockoutDuration&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdMaxFailure</code> </p>
<p> This attribute contains the number of consecutive failed bind attempts after which the password may not be used to authenticate a user to the directory. If <code>pwdMaxFailure</code> is not present, or its value is zero (0), then a user will be allowed to continue to attempt to authenticate to the directory, no matter how many consecutive failed bind attempts have occurred with that user&#8217;s DN. (See also <code>pwdLockout</code> and <code>pwdLockoutDuration</code>.) </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.11<br />
NAME&nbsp;<wbr>&#8216;pwdMaxFailure&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdFailureCountInterval</code> </p>
<p> This attribute contains the number of seconds after which old consecutive failed bind attempts are purged from the failure counter, even though no successful authentication has occurred. If <code>pwdFailureCountInterval</code> is not present, or its value is zero (0), the failure counter will only be reset by a successful authentication. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.12<br />
NAME&nbsp;<wbr>&#8216;pwdFailureCountInterval&#8217;<br />
EQUALITY integerMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.27<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdMustChange</code> </p>
<p> This attribute specifies whether users must change their passwords when they first bind to the directory after a password is set or reset by the administrator, or not. If <code>pwdMustChange</code> has a value of &quot;TRUE&quot;, users must change their passwords when they first bind to the directory after a password is set or reset by the administrator. If <code>pwdMustChange</code> is not present, or its value is &quot;FALSE&quot;, users are not required to change their password upon binding after the administrator sets or resets the password. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.13<br />
&nbsp;<wbr>&nbsp;<wbr>NAME&nbsp;<wbr>&#8216;pwdMustChange&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>EQUALITY booleanMatch<br />
&nbsp;<wbr>&nbsp;<wbr>SYNTAX 1.3.6.1.4.1.1466.115.121.1.7<br />
&nbsp;<wbr>&nbsp;<wbr>SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdAllowUserChange</code> </p>
<p> This attribute specifies whether users are allowed to change their own passwords or not. If <code>pwdAllowUserChange</code> is set to &quot;TRUE&quot;, or if the attribute is not present, users will be allowed to change their own passwords. If its value is &quot;FALSE&quot;, users will not be allowed to change their own passwords. </p>
<p> Note: this implies that when <code>pwdAllowUserChange</code> is set to &quot;TRUE&quot;, users will still be able to change the password of another user, subjected to access control. This restriction only applies to modifications of ones&#8217;s own password. It should also be noted that <code>pwdAllowUserChange</code> was defined in the specification to provide rough access control to the password attribute in implementations that do not allow fine-grain access control. Since OpenLDAP provides fine-grain access control, the use of this attribute is discouraged; ACLs should be used instead (see <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) for details). </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.14<br />
NAME&nbsp;<wbr>&#8216;pwdAllowUserChange&#8217;<br />
EQUALITY booleanMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.7<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdSafeModify</code> </p>
<p> This attribute denotes whether the user&#8217;s existing password must be sent along with their new password when changing a password. If <code>pwdSafeModify</code> is set to &quot;TRUE&quot;, the existing password must be sent along with the new password. If the attribute is not present, or its value is &quot;FALSE&quot;, the existing password need not be sent along with the new password. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.15<br />
NAME&nbsp;<wbr>&#8216;pwdSafeModify&#8217;<br />
EQUALITY booleanMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.7<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> <code>pwdCheckModule</code> </p>
<p> This attribute names a user-defined loadable module that must instantiate the check_password() function. This function will be called to further check a new password if <code>pwdCheckQuality</code> is set to one (1) or two (2), after all of the built-in password compliance checks have been passed. This function will be called according to this function prototype:</p>
<dl>
<dd>int <i>check_password</i> (char *pPasswd, char **ppErrStr, Entry *pEntry);</dl>
<p> The <code>pPasswd</code> parameter contains the clear-text user password, the <code>ppErrStr</code> parameter contains a double pointer that allows the function to return human-readable details about any error it encounters. The optional <code>pEntry</code> parameter, if non-NULL, carries a pointer to the entry whose password is being checked. If <code>ppErrStr</code> is NULL, then <i>funcName</i> must NOT attempt to use it/them. A return value of LDAP_SUCCESS from the called function indicates that the password is ok, any other value indicates that the password is unacceptable. If the password is unacceptable, the server will return an error to the client, and <code>ppErrStr</code> may be used to return a human-readable textual explanation of the error. The error string must be dynamically allocated as it will be free()&#8217;d by slapd. </p>
<dl>
<dd>( 1.3.6.1.4.1.4754.1.99.1<br />
NAME&nbsp;<wbr>&#8216;pwdCheckModule&#8217;<br />
EQUALITY caseExactIA5Match<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.26<br />
SINGLE-VALUE&nbsp;<wbr>)</dl>
<p> Note: The user-defined loadable module named by <code>pwdCheckModule </code> must be in <code>slapd&#8217;s</code> standard executable search PATH. </p>
<p> Note: <code>pwdCheckModule</code> is a non-standard extension to the LDAP password policy proposal.</p>
<h2>Operational Attributes</h2>
<p>The operational attributes used by the <code>ppolicy</code> module are stored in the user&#8217;s entry. Most of these attributes are not intended to be changed directly by users; they are there to track user activity. They have been detailed here so that administrators and users can both understand the workings of the <code>ppolicy</code> module. </p>
<p> Note that the current IETF Password Policy proposal does not define how these operational attributes are expected to behave in a replication environment. In general, authentication attempts on a slave server only affect the copy of the operational attributes on that slave and will not affect any attributes for a user&#8217;s entry on the master server. Operational attribute changes resulting from authentication attempts on a master server will usually replicate to the slaves (and also overwrite any changes that originated on the slave). These behaviors are not guaranteed and are subject to change when a formal specification emerges. </p>
<p> <code>userPassword</code> </p>
<p> The <code>userPassword</code> attribute is not strictly part of the <code>ppolicy</code> module. It is, however, the attribute that is tracked and controlled by the module. Please refer to the standard OpenLDAP schema for its definition. </p>
<p> <code>pwdPolicySubentry</code> </p>
<p> This attribute refers directly to the <code>pwdPolicy</code> subentry that is to be used for this particular directory user. If <code>pwdPolicySubentry</code> exists, it must contain the DN of a valid <code>pwdPolicy</code> object. If it does not exist, the <code>ppolicy</code> module will enforce the default password policy rules on the user associated with this authenticating DN. If there is no default, or the referenced subentry does not exist, then no policy rules will be enforced. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.23<br />
NAME&nbsp;<wbr>&#8216;pwdPolicySubentry&#8217;<br />
DESC&nbsp;<wbr>&#8216;The pwdPolicy subentry in effect for<br />
&nbsp;<wbr>this object&#8217;<br />
EQUALITY distinguishedNameMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.12<br />
SINGLE-VALUE<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation)</dl>
<p> <code>pwdChangedTime</code> </p>
<p> This attribute denotes the last time that the entry&#8217;s password was changed. This value is used by the password expiration policy to determine whether the password is too old to be allowed to be used for user authentication. If <code>pwdChangedTime</code> does not exist, the user&#8217;s password will not expire. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.16<br />
NAME&nbsp;<wbr>&#8216;pwdChangedTime&#8217;<br />
DESC&nbsp;<wbr>&#8216;The time the password was last changed&#8217;<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.24<br />
EQUALITY generalizedTimeMatch<br />
ORDERING generalizedTimeOrderingMatch<br />
SINGLE-VALUE<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation)</dl>
<p> <code>pwdAccountLockedTime</code> </p>
<p> This attribute contains the time that the user&#8217;s account was locked. If the account has been locked, the password may no longer be used to authenticate the user to the directory. If <code>pwdAccountLockedTime </code> is set to 000001010000Z, the user&#8217;s account has been permanently locked and may only be unlocked by an administrator. Note that account locking only takes effect when the <code>pwdLockout</code> password policy attribute is set to &quot;TRUE&quot;. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.17<br />
NAME&nbsp;<wbr>&#8216;pwdAccountLockedTime&#8217;<br />
DESC&nbsp;<wbr>&#8216;The time an user account was locked&#8217;<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.24<br />
EQUALITY generalizedTimeMatch<br />
ORDERING generalizedTimeOrderingMatch<br />
SINGLE-VALUE<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation)</dl>
<p> <code>pwdFailureTime</code> </p>
<p> This attribute contains the timestamps of each of the consecutive authentication failures made upon attempted authentication to this DN (i.e. account). If too many timestamps accumulate here (refer to the <code>pwdMaxFailure</code> password policy attribute for details), and the <code>pwdLockout</code> password policy attribute is set to &quot;TRUE&quot;, the account may be locked. (Please also refer to the <code>pwdLockout</code> password policy attribute.) Excess timestamps beyond those allowed by <code>pwdMaxFailure</code> may also be purged. If a successful authentication is made to this DN (i.e. to this user account), then <code>pwdFailureTime </code> will be cleansed of entries. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.19<br />
NAME&nbsp;<wbr>&#8216;pwdFailureTime&#8217;<br />
DESC&nbsp;<wbr>&#8216;The timestamps of the last consecutive<br />
&nbsp;<wbr>authentication failures&#8217;<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.24<br />
EQUALITY generalizedTimeMatch<br />
ORDERING generalizedTimeOrderingMatch<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation&nbsp;<wbr>)</dl>
<p> <code>pwdHistory</code> </p>
<p> This attribute contains the history of previously used passwords for this DN (i.e. for this user account). The values of this attribute are stored in string format as follows: </p>
<dl>
<dd>pwdHistory=</p>
<dl>
<dd>time &quot;#&quot; syntaxOID &quot;#&quot; length &quot;#&quot; data</dl>
<p> time=</p>
<dl>
<dd>GeneralizedTime as specified in section 3.3.13 of [RFC4517]</dl>
<p> syntaxOID = numericoid</p>
<dl>
<dd>This is the string representation of the dotted-decimal OID that defines the syntax used to store the password. numericoid is described in section 1.4 of [RFC4512].</dl>
<p> length = NumericString</p>
<dl>
<dd>The number of octets in the data. NumericString is described in section 3.3.23 of [RFC4517].</dl>
<p> data =</p>
<dl>
<dd>Octets representing the password in the format specified by syntaxOID.</dl>
</dl>
<p> This format allows the server to store and transmit a history of passwords that have been used. In order for equality matching on the values in this attribute to function properly, the time field is in GMT format. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.20<br />
NAME&nbsp;<wbr>&#8216;pwdHistory&#8217;<br />
DESC&nbsp;<wbr>&#8216;The history of user passwords&#8217;<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.40<br />
EQUALITY octetStringMatch<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation)</dl>
<p> <code>pwdGraceUseTime</code> This attribute contains the list of timestamps of logins made after the user password in the DN has expired. These post-expiration logins are known as &quot;<i>grace logins</i>&quot;. If too many <i>grace logins</i> have been used (please refer to the <code>pwdGraceLoginLimit</code> password policy attribute), then the DN will no longer be allowed to be used to authenticate the user to the directory until the administrator changes the DN&#8217;s <code>userPassword</code> attribute. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.21<br />
NAME&nbsp;<wbr>&#8216;pwdGraceUseTime&#8217;<br />
DESC&nbsp;<wbr>&#8216;The timestamps of the grace login once the password has expired&#8217;<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.24<br />
EQUALITY generalizedTimeMatch<br />
NO-USER-MODIFICATION<br />
USAGE directoryOperation)</dl>
<p> <code>pwdReset</code> </p>
<p> This attribute indicates whether the user&#8217;s password has been reset by the administrator and thus must be changed upon first use of this DN for authentication to the directory. If <code>pwdReset </code> is set to &quot;TRUE&quot;, then the password was reset and the user must change it upon first authentication. If the attribute does not exist, or is set to &quot;FALSE&quot;, the user need not change their password due to administrative reset. </p>
<dl>
<dd>( 1.3.6.1.4.1.42.2.27.8.1.22<br />
NAME&nbsp;<wbr>&#8216;pwdReset&#8217;<br />
DESC&nbsp;<wbr>&#8216;The indication that the password has<br />
&nbsp;<wbr>been reset&#8217;<br />
EQUALITY booleanMatch<br />
SYNTAX 1.3.6.1.4.1.1466.115.121.1.7<br />
SINGLE-VALUE<br />
USAGE directoryOperation)</dl>
<h2>Examples</h2>
<pre><code>database bdb
suffix dc=example,dc=com
...
overlay ppolicy
ppolicy_default &quot;cn=Standard,ou=Policies,dc=example,dc=com&quot;
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapo-chain/">slapo-chain</a></code>(5). &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a> IETF LDAP password policy proposal by P. Behera, L. Poitou and J. Sermersheim: documented in IETF document &quot;draft-behera-ldap-password-policy-09.txt&quot;. </p>
<h2>Bugs</h2>
<p>The LDAP Password Policy specification is not yet an approved standard, and it is still evolving. This code will continue to be in flux until the specification is finalized. </p>
<h2>Acknowledgements</h2>
<p>This module was written in 2004 by Howard Chu of Symas Corporation with significant input from Neil Dunbar and Kartik Subbarao of Hewlett-Packard. </p>
<p> This manual page borrows heavily and shamelessly from the specification upon which the password policy module it describes is based. This source is the IETF LDAP password policy proposal by P. Behera, L. Poitou and J. Sermersheim. The proposal is fully documented in the IETF document named draft-behera-ldap-password-policy-09.txt, written in July of 2005. </p>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
