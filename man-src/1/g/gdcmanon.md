---
title: "gdcmanon(1)"
name: "gdcmanon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmanon/"
description: "gdcmanon – .TH \"gdcmanon\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmanon &#8211; .TH &quot;gdcmanon&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmanon &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre><code>
gdcmanon[options] file - in file - out gdcmanon[options] dir - in dir - out
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmanon</code> tool is an implementation of PS 3.15 / E.1 / Basic Application Level Confidentiality Profile (Implementation of E.1.1 De-identify &amp; E.1.2 Re-identify) </p>
<p> This tool is split into two very different operating mode: </p>
<dl>
<dt>*</p>
<dd> An implementation of PS 3.15, see -e and -d flags</p>
<dt>*</p>
<dd> A dumb mode, see &#8211;dumb</dl>
<p> Dumb mode and PS 3.15 do not work well together, you should really only use one type of anonymization. In case of doubt, avoid using &#8211;dumb. </p>
<p> In order to use the PS 3.15 implementation (-d &amp; -e flag), you&#8217;ll need a certificate to do de-identification operations, and the associated private key to do the re-identification operation. If you are only doing a one-shot anonymization and do not need to properly re-identify the DICOM file, you can safely discard the private key and only keep the certificate. See OpenSSL section below for an example on how to generate the private key/certificate pair. </p>
<p> gdcmanon will exit early if OpenSSL was not configured/build properly into the library (see GDCM_USE_SYSTEM_OPENSSL in cmake).</p>
<h2>PARAMETERS</h2>
<pre>
file-in   DICOM input filename
file-out  DICOM output filename
</pre>
<p> or </p>
<pre>
file-in   DICOM input directory
file-out  DICOM output directory
</pre>
<h2>OPTIONS</h2>
<p> You need to specify at least one operating mode, from the following list (and only one):</p>
<h3>Required parameters</h3>
<pre>
  -e --de-identify            De-identify DICOM (default)
  -d --re-identify            Re-identify DICOM
     --dumb                   Dumb mode anonymizer
</pre>
<p> Warning when operating in dumb mode, you need to also specify an operation to do, such as &#8216;remove&#8217; or &#8217;empty&#8217; a tag, see below the dumb mode options.</p>
<h3>OPTIONS</h3>
<p>&#8211; i&#8211; input DICOM filename / directory &#8211; o&#8211; output DICOM filename / directory &#8211; r&#8211; recursive recursively process(sub -)directories.&#8211;continue Do not stop when file found is not DICOM.&#8211;root &#8211; uid Root UID.&#8211;resources &#8211; path Resources path.- k&#8211; key Path to RSA Private Key.- c&#8211; certificate Path to Certificate.</p>
<h3>encryption options</h3>
<p>&#8211;des DES.&#8211;des3 Triple DES.&#8211;aes128 AES 128. &#8211;aes192 AES 192. &#8211;aes256 AES 256.</p>
<h3>dumb mode options</h3>
<pre>
     --empty   %d,%d           DICOM tag(s) to empty
     --remove  %d,%d           DICOM tag(s) to remove
     --replace %d,%d,%s        DICOM tag(s) to replace
</pre>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit &#8211;<br />
    v&#8211; version<br />
        print version information and exit &#8211;<br />
    V&#8211; verbose<br />
        verbose<br />
        mode(warning + error)<br />
            .-<br />
    W&#8211; warning<br />
    warning mode,<br />
    print warning information<br />
        &#8211; E&#8211; error<br />
        error mode,<br />
    print error information<br />
        &#8211; D&#8211; debug<br />
        debug mode,<br />
    print debug information</p>
<h3>environment variable</h3>
<pre>
  GDCM_ROOT_UID Root UID
  GDCM_RESOURCES_PATH path pointing to resources files (Part3.xml, ...)
</pre>
<h2>Typical usage</h2>
<h3>De-identification (anonymization, encrypt)</h3>
<p> The only thing required for this operation is a certificate file (in PEM format). </p>
<pre>
$ gdcmanon --certificate certificate.pem -e original.dcm original_anonymized.dcm
</pre>
<h3>Re-identification (de-anonymization,decrypt)</h3>
<p> The only thing required for this operation is a private key (in PEM format). It is required that the private key used for the re-identification process, was the actual private key used to generate the certificate file (certificate.pem) used during the de-identification step. </p>
<pre>
$ gdcmanon --key privatekey.pem -d original_anonymized.dcm original_copy.dcm
</pre>
<p> You can then check that original.dcm and original_copy.dcm are identical.</p>
<h3>Multiple files caveat</h3>
<p> It is very important to understand the following section, when anonymizing more than one single file. When anonymizing multiple DICOM files, you are required to use the directory input. You cannot call multiple time the gdcmanon command line tool. Indeed the tool stores in memory during the process only a hash table of conversion so that each time a particular value is found it get always replaced by the same de-identified value (think: consistant Series Instance UID).</p>
<h3>Dumb mode</h3>
<p> This functionality is not described in the DICOM standard. Users are advised that improper use of that mode is not recommended, meaning that important tag can be empty/remove/replace resulting in illegal/invalid DICOM file. Only use when you know what you are doing. If you delete a Type 1 attribute, chance is that your DICOM file will be not accepted in most DICOM third party viewer. Unfortunately this is often this mode that is implemented in popular DICOM Viewer, always prefer what the DICOM standard describes, and avoid the dumb mode. </p>
<p> The following example shows how to use dumb mode and achieve 5 operations at the same time: </p>
<dl>
<dt>*</p>
<dd> Empty the tag (0010,0010) Patient&#8217;s Name,</p>
<dt>*</p>
<dd> Empty the tag (0010,0020) Patient ID,</p>
<dt>*</p>
<dd> Remove the tag (0010,0040) Patient&#8217;s Sex</p>
<dt>*</p>
<dd> Remove the tag (0010,1010) Patient&#8217;s Age</p>
<dt>*</p>
<dd> Replace the tag (0010,1030) Patient&#8217;s Weight with the value &#8217;10&#8217;</dl>
<p> You are required to check which DICOM attribute is Type 1 and Type 1C, before trying to &#8216;Empty&#8217; or &#8216;Remove&#8217; a particular DICOM attribute. For the same reason, you are required to check what are valid value in a replace operation. </p>
<p>$ gdcmanon&#8211; dumb&#8211; empty 10, 10 &#8211;empty 10, 20 &#8211;remove 10, 40 &#8211;remove 10, 1010 &#8211;replace 10, 1030, 10 012345.002.050.dcm out.dcm</p>
<p> Multiple operation of &#8211;dumb mode can take place, just reuse the output of the previous operation. Always use gdcmdump on the input and output file to check what was actually achieved. You can use a diff program to check only what changed (see <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) for example).</p>
<h3>Irreversible Anonymization</h3>
<p> In some very case, one would want to anonymize using the PS 3.15 mode so as to take benefit of the automatic conversion of all content that could contain Patient related information. </p>
<p> In the end all Patient related information has been removed and has been secretely stored in the 0400,0500 DICOM attribute. However to make sure that no-one ever try to break that security using brute-force algorithm, one want want to remove completely this DICOM attribute. This will make the DICOM: </p>
<dl>
<dt>*</p>
<dd> Completely free of any Patient related information (as per PS 3.15 specification)</p>
<dt>*</p>
<dd> Remove any mean of people to brute force attack the file to find out the identity of the Patient</dl>
<p> In this case one could simply do, as a first step execute the reversible anonymizer: </p>
<pre>
 gdcmanon -c certificate.pem input.dcm anonymized_reversible.dcm
</pre>
<p> and now completely remove the DICOM attribute containing the secretly encrypted Patient related information: </p>
<pre><code>
gdcmanon-- dumb-- remove 400, 500 --remove 12, 62 --remove 12, 63 anonymized_reversible.dcm anonymized_irreversible.dcm
</code></pre>
<h2>OpenSSL</h2>
<p> On most system you can have access to OpenSSL to generate the Private Key/Certificate pair.</p>
<h3>Generating a Private Key</h3>
<p> Command line to generate a rsa key (512bit) </p>
<pre>
$ openssl genrsa -out CA_key.pem
</pre>
<p> Command line to generate a rsa key (2048bit) </p>
<pre>
$ openssl genrsa -out CA_key.pem 2048 
</pre>
<p> Command line to generate a rsa key (2048bit) + passphrase </p>
<pre>
$ openssl genrsa -des3 -out CA_key.pem 2048 
</pre>
<h3>Generating a Certificate</h3>
<p> From your previously generated Private Key, you can now generate a certificate in PEM (DER format is currently not supported). </p>
<pre>
$ openssl req -new -key CA_key.pem -x509 -days 365 -out CA_cert.cer
</pre>
<h2>DICOM Standard:</h2>
<p> Page to the DICOM Standard: </p>
<p> <a rel="nofollow" href="http://dicom.nema.org/">http://dicom.nema.org/</a> </p>
<p> The DICOM Standard at the time of releasing gdcmanon is: </p>
<p> <a href="ftp://medical.nema.org/medical/dicom/2008/">ftp://medical.nema.org/medical/dicom/2008/</a> </p>
<p> Direct link to PS 3.15-2008: </p>
<p> <a href="ftp://medical.nema.org/medical/dicom/2008/08_15pu.pdf">ftp://medical.nema.org/medical/dicom/2008/08_15pu.pdf</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmconv/">gdcmconv</a></code>(1), <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcminfo/">gdcminfo</a></code>(1), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
