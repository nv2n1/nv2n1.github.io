---
title: "getcert-list(1)"
name: "getcert-list"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-list/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert list [options] </p>
<h2>DESCRIPTION</h2>
<p> Queries <i>certmonger</i> for a list of certificates which it is monitoring or attempting to obtain. </p>
<h2>ENROLLMENT OPTIONS</h2>
<dl>
<dt><code>-c</code> NAME</p>
<dd> List only entries which use the specified CA. The name of the CA should correspond to one listed by <i>getcert list-cas</i>. </p>
</dl>
<h2>LISTING OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> List only entries which are either currently being enrolled or refreshed.</p>
<dt><code>-t</code></p>
<dd> List only entries which are not currently being enrolled or refreshed. </p>
<dt><code>-d</code> DIR</p>
<dd> List only entries which use an NSS database in the specified directory for storing the certificate.</p>
<dt><code>-n</code> NAME</p>
<dd> List only tracking requests which use an NSS database and the specified nickname for storing the certificate.</p>
<dt><code>-f</code> FILE</p>
<dd> List only tracking requests which specify that the certificate should be stored in the specified file.</p>
<dt><code>-i</code> NAME</p>
<dd> List only tracking requests which use this request nickname. </p>
</dl>
<h2>STATES</h2>
<dl>
<dt>NEED_KEY_PAIR</p>
<dd> The service is about to generate a new key pair.</p>
<dt>GENERATING_KEY_PAIR</p>
<dd> The service is currently generating a new key pair.</p>
<dt>NEED_KEY_GEN_PERMS</p>
<dd> The service encountered a filesystem permission error while attempting to save the newly-generated key pair.</p>
<dt>NEED_KEY_GEN_PIN</p>
<dd> The service is missing the PIN which is required to access an NSS database in order to save the newly-generated key pair, or it has an incorrect PIN for a database.</p>
<dt>NEED_KEY_GEN_TOKEN</p>
<dd> The service was unable to find a suitable token to use for generating the new key pair.</p>
<dt>HAVE_KEY_PAIR</p>
<dd> The service has successfully generated a new key pair.</p>
<dt>NEED_KEYINFO</p>
<dd> The service needs to read information about the key pair.</p>
<dt>READING_KEYINFO</p>
<dd> The service is currently reading information about the key pair.</p>
<dt>NEED_KEYINFO_READ_PIN</p>
<dd> The service is missing the PIN which is required to access an NSS database in order to read information about the newly-generated key pair, or it has an incorrect PIN for a database, or has an incorrect password for accessing a key stored in encrypted PEM format.</p>
<dt>NEED_KEYINFO_READ_TOKEN</p>
<dd> The service was unable to find the token in which the key pair is supposed to be stored.</p>
<dt>HAVE_KEYINFO</p>
<dd> The service has successfully read information about the key pair.</p>
<dt>NEED_CSR</p>
<dd> The service is about to generate a new signing request.</p>
<dt>GENERATING_CSR</p>
<dd> The service is generating a signing request.</p>
<dt>NEED_CSR_GEN_PIN</p>
<dd> The service is missing the PIN which is required to access an NSS database in order to use the key pair, or it has an incorrect PIN for a database, or has an incorrect password for reading a key stored in encrypted PEM format.</p>
<dt>NEED_CSR_GEN_TOKEN</p>
<dd> The service was unable to find the token in which the key pair is supposed to be stored.</p>
<dt>HAVE_CSR</p>
<dd> The service has successfully generated a signing request.</p>
<dt>NEED_SCEP_DATA</p>
<dd> The service is about to generate data specifically needed for connecting to a CA using SCEP.</p>
<dt>GENERATING_SCEP_DATA</p>
<dd> The service is generating data specifically needed for connecting to a CA using SCEP.</p>
<dt>NEED_SCEP_GEN_PIN</p>
<dd> The service is missing the PIN which is required to access an NSS database in order to use the key pair, or it has an incorrect PIN for a database, or has an incorrect password for reading a key stored in encrypted PEM format.</p>
<dt>NEED_SCEP_GEN_TOKEN</p>
<dd> The service was unable to find the token in which the key pair is supposed to be stored.</p>
<dt>NEED_SCEP_ENCRYPTION_CERT</p>
<dd> The service is waiting until it can retrieve a copy of the CA&#8217;s certificate before it can generate data required for connecting to the CA using SCEP.</p>
<dt>NEED_SCEP_RSA_CLIENT_KEY</p>
<dd> The CA should be contacted using SCEP, but SCEP requires the client key pair to be an RSA key pair, and it is not.</p>
<dt>HAVE_SCEP_DATA</p>
<dd> The service has successfully generated data for use in SCEP.</p>
<dt>NEED_TO_SUBMIT</p>
<dd> The service is about to submit a signing request to a CA for signing.</p>
<dt>SUBMITTING</p>
<dd> The service is currently submitting a signing request to a CA for signing.</p>
<dt>NEED_CA</p>
<dd> The service can&#8217;t submit a request to a CA because it doesn&#8217;t know which CA to use.</p>
<dt>CA_UNREACHABLE</p>
<dd> The service was unable to contact the CA, but it will try again later.</p>
<dt>CA_UNCONFIGURED</p>
<dd> The service is missing configuration which will be needed in order to successfully contact the CA.</p>
<dt>CA_REJECTED</p>
<dd> The CA rejected the signing request.</p>
<dt>CA_WORKING</p>
<dd> The CA has not yet approved or rejected the request. The service will check on the status of the request later.</p>
<dt>NEED_TO_SAVE_CERT</p>
<dd> The CA approved the signing request, and the service is about to save the issued certificate to the location where it has been told to save it.</p>
<dt>PRE_SAVE_CERT</p>
<dd> The service is running a configured pre-saving command before saving the newly-issued certificate to the location where it has been told to save it.</p>
<dt>START_SAVING_CERT</p>
<dd> The service is starting to save the issued certificate to the location where it has been told to save it.</p>
<dt>SAVING_CERT</p>
<dd> The service is attempting to save the issued certificate to the location where it has been told to save it.</p>
<dt>NEED_CERTSAVE_PERMS</p>
<dd> The service encountered a filesystem permission error while attempting to save the newly-issued certificate to the location where it has been told to save it.</p>
<dt>NEED_CERTSAVE_TOKEN</p>
<dd> The service is unable to find the token in which the newly-issued certificate is to be stored.</p>
<dt>NEED_CERTSAVE_PIN</p>
<dd> The service is missing the PIN which is required to access an NSS database in order to save the newly-issued certificate to the location where it has been told to save it.</p>
<dt>NEED_TO_SAVE_CA_CERTS</p>
<dd> The service is about to save the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>START_SAVING_CA_CERTS</p>
<dd> The service is starting to save the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>SAVING_CA_CERTS</p>
<dd> The service is saving the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>NEED_TO_SAVE_ONLY_CA_CERTS</p>
<dd> The service is about to save the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>START_SAVING_ONLY_CA_CERTS</p>
<dd> The service is starting to save the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>SAVING_ONLY_CA_CERTS</p>
<dd> The service is saving the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>NEED_CA_CERT_SAVE_PERMS</p>
<dd> NEED_ONLY_CA_CERT_SAVE_PERMS The service encountered a filesystem permission error while attempting to save the certificate of the issuing CA to the locations where it has been told to save them.</p>
<dt>NEED_TO_READ_CERT</p>
<dd> The service is about to read the issued certificate from the location where it has been told to save it.</p>
<dt>READING_CERT</p>
<dd> The service is reading the issued certificate from the location where it has been told to save it.</p>
<dt>SAVED_CERT</p>
<dd> The service has finished finished saving the issued certificate and the issuer&#8217;s certificate to the locations where it has been told to save them.</p>
<dt>POST_SAVED_CERT</p>
<dd> The service is running a configured post-saving command after saving the newly-issued certificate to the location where it has been told to save them.</p>
<dt>MONITORING</p>
<dd> The service is monitoring the certificate and waiting for its not-valid-after date to approach. This is expected to be the status most often seen.</p>
<dt>NEED_TO_NOTIFY_VALIDITY</p>
<dd> The service is about to notify the system administrator that the certificate&#8217;s not-valid-after date is approaching.</p>
<dt>NOTIFYING_VALIDITY</p>
<dd> The service is notifying the system administrator that the certificate&#8217;s not-valid-after date is approaching.</p>
<dt>NEED_TO_NOTIFY_REJECTION</p>
<dd> The service is about to notify the system administrator that the CA rejected the signing request.</p>
<dt>NOTIFYING_REJECTION</p>
<dd> The service is notifying the system administrator that the CA rejected the signing request.</p>
<dt>NEED_TO_NOTIFY_ISSUED_SAVE_FAILED</p>
<dd> The service is needs to notify the system administrator that the CA issued a certificate, but that there was a problem saving the certificate to the location where the service was told to save it.</p>
<dt>NOTIFYING_ISSUED_SAVE_FAILED</p>
<dd> The service is is notifying the system administrator that the CA issued a certificate, but that there was a problem saving the certificate to the location where the service was told to save it.</p>
<dt>NEED_TO_NOTIFY_ISSUED_CA_SAVE_FAILED</p>
<dd> The service is needs to notify the system administrator that the CA issued a certificate, and the issued certificate was saved to the location where the service has been told to save it, but that there was a problem saving the CA&#8217;s certificate to the locations where the service was told to save it.</p>
<dt>NOTIFYING_ISSUED_CA_SAVE_FAILED</p>
<dd> The service is notifying the system administrator that the CA issued a certificate, and the issued certificate was saved to the location where the service has been told to save it, but that there was a problem saving the CA&#8217;s certificate to the locations where the service was told to save it.</p>
<dt>NEED_TO_NOTIFY_ISSUED_SAVED</p>
<dd> The service is needs to notify the system administrator that the CA issued a certificate and it has been saved to the location where the service has been told to save it.</p>
<dt>NOTIFYING_ISSUED_SAVED</p>
<dd> The service is notifying the system administrator that the CA issued a certificate and it has been saved to the location where the service has been told to save it.</p>
<dt>NEED_TO_NOTIFY_ONLY_CA_SAVE_FAILED</p>
<dd> The service needs to notify the system administrator that there was a problem saving the CA&#8217;s certificates to the specified location.</p>
<dt>NOTIFYING_ONLY_CA_SAVE_FAILED</p>
<dd> The service is notifying the system administrator that there was a problem saving the CA&#8217;s certificates to the specified location.</p>
<dt>NEED_GUIDANCE</p>
<dd> An unhandled error was encountered while attempting to contact the CA, or there is the service has just been told to monitor a certificate which does not exist and for which it has no location specified for storing a key pair that could be used to generate a signing request to obtain one.</p>
<dt>NEWLY_ADDED</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one.</p>
<dt>NEWLY_ADDED_START_READING_KEYINFO</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and is about to check if there is already a key pair present.</p>
<dt>NEWLY_ADDED_READING_KEYINFO</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and is checking if there is already a key pair present.</p>
<dt>NEWLY_ADDED_NEED_KEYINFO_READ_PIN</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and was unable to check if a key pair was present because it is missing the PIN which is required to access an NSS database, or because it has an incorrect PIN for a database.</p>
<dt>NEWLY_ADDED_NEED_KEYINFO_READ_TOKEN</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and was unable to check if a key pair was present because the token which should be used for storing the key pair is not present.</p>
<dt>NEWLY_ADDED_START_READING_CERT</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and is about to check if a certificate is already present in the specified location.</p>
<dt>NEWLY_ADDED_READING_CERT</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and is checking if a certificate is already present in the specified location.</p>
<dt>NEWLY_ADDED_DECIDING</p>
<dd> The service has just been told to track a certificate, or to generate a signing request to obtain one, and is determining its next course of action. </p>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
