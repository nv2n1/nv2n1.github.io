---
title: "proxycertinfo(3)"
name: "proxycertinfo"
section: "3"
letter: "p"
url: "/docs/linux/man/3-proxycertinfo/"
description: "ProxyCertInfo –"
---

<p>ProxyCertInfo &#8211;</p>
<h3>Data Structures</h3>
<pre><code>struct PROXYCERTINFO_st


This typedef maintains information about a proxy certificate.



ASN1_METHOD





ASN1_METHOD * PROXYCERTINFO_asn1_meth ()



New





PROXYCERTINFO * PROXYCERTINFO_new ()



Free.





void PROXYCERTINFO_free (PROXYCERTINFO *cert_info)



Duplicate





PROXYCERTINFO * PROXYCERTINFO_dup (PROXYCERTINFO *cert_info)



Compare





int PROXYCERTINFO_cmp (const PROXYCERTINFO *a, const PROXYCERTINFO *b)



Print to a BIO stream





int PROXYCERTINFO_print (BIO *bp, PROXYCERTINFO *cert_info)



Print To Stream





int PROXYCERTINFO_print_fp (FILE *fp, PROXYCERTINFO *cert_info)



Set the Policy Field





int PROXYCERTINFO_set_policy (PROXYCERTINFO *cert_info, PROXYPOLICY *policy)



Get the Policy Field





PROXYPOLICY * PROXYCERTINFO_get_policy (PROXYCERTINFO *cert_info)



Set the Path Length Field





int PROXYCERTINFO_set_path_length (PROXYCERTINFO *cert_info, long path_length)



Get Path Length Field





long PROXYCERTINFO_get_path_length (PROXYCERTINFO *cert_info)



Convert PROXYCERTINFO to DER encoded form





int i2d_PROXYCERTINFO (PROXYCERTINFO *cert_info, unsigned char **pp)



Convert a PROXYCERTINFO to internal form





PROXYCERTINFO * d2i_PROXYCERTINFO (PROXYCERTINFO **cert_info, unsigned char **pp, long length)



Convert old PROXYCERTINFO to DER encoded form





int i2d_PROXYCERTINFO_OLD (PROXYCERTINFO *cert_info, unsigned char **pp)



Convert a old PROXYCERTINFO to internal form





PROXYCERTINFO * d2i_PROXYCERTINFO_OLD (PROXYCERTINFO **cert_info, unsigned char **pp, long length)</code></pre>
<h2>Detailed Description</h2>
<p><code>Author:</code></p>
<dl>
<dd>Sam Meder </p>
<p> Sam Lang</dl>
<p> The proxycertinfo.h file defines a method of maintaining information about proxy certificates.</p>
<h2>Function Documentation</h2>
<h3>ASN1_METHOD* PROXYCERTINFO_asn1_meth ()</h3>
<p>Define the functions required for manipulating a PROXYCERTINFO and its ASN1 form. Creates an ASN1_METHOD structure, which contains pointers to routines that convert any PROXYCERTINFO structure to its associated ASN1 DER encoded form and vice-versa. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>the ASN1_METHOD object</dl>
<h3><code>PROXYCERTINFO</code>* PROXYCERTINFO_new ()</h3>
<p>Create a new PROXYCERTINFO. Allocates and initializes a new PROXYCERTINFO structure. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>pointer to the new PROXYCERTINFO</dl>
<h3>void PROXYCERTINFO_free (<code>PROXYCERTINFO</code> * cert_info)</h3>
<p>Free a PROXYCERTINFO. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> pointer to the PROXYCERTINFO structure to be freed.</dl>
<h3><code>PROXYCERTINFO</code>* PROXYCERTINFO_dup (<code>PROXYCERTINFO</code> * cert_info)</h3>
<p>Makes a copy of a PROXYCERTINFO. Makes a copy of a PROXYCERTINFO structure </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO structure to copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the copied PROXYCERTINFO structure</dl>
<h3>int PROXYCERTINFO_cmp (const <code>PROXYCERTINFO</code> * a, const <code>PROXYCERTINFO</code> * b)</h3>
<p>Compares two PROXYCERTINFO structures. <code>Parameters:</code></p>
<dl>
<dd><i>a</i> pointer to the first PROXYCERTINFO structure<br />
 <i>b</i> pointer to the second PROXYCERTINFO structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>an integer &#8211; the result of the comparison. The comparison compares each of the fields, so if any of those fields are not equal then a nonzero value is returned. Equality is indicated by returning a 0.</dl>
<h3>int PROXYCERTINFO_print (BIO * bp, <code>PROXYCERTINFO</code> * cert_info)</h3>
<p>print the PROXYCERTINFO structure to stdout <code>Parameters:</code></p>
<dl>
<dd><i>bp</i> the BIO to print to<br />
 <i>cert_info</i> the PROXYCERTINFO to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, 0 on error</dl>
<h3>int PROXYCERTINFO_print_fp (FILE * fp, <code>PROXYCERTINFO</code> * cert_info)</h3>
<p>print the PROXYCERTINFO structure to the specified file stream <code>Parameters:</code></p>
<dl>
<dd><i>fp</i> the file stream (FILE *) to print to<br />
 <i>cert_info</i> the PROXYCERTINFO structure to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the number of characters printed</dl>
<h3>int PROXYCERTINFO_set_policy (<code>PROXYCERTINFO</code> * cert_info, <code>PROXYPOLICY</code> * policy)</h3>
<p>Sets the policy on the PROXYCERTINFO Since this is an optional field in the ASN1 encoding, this variable can be set to NULL through this function &#8211; which means that when the PROXYCERTINFO is encoded the policy won&#8217;t be included. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO object to set the policy of<br />
 <i>policy</i> the PROXYPOLICY to set it to</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 if success, 0 if error</dl>
<h3><code>PROXYPOLICY</code>* PROXYCERTINFO_get_policy (<code>PROXYCERTINFO</code> * cert_info)</h3>
<p>Gets the policy on the PROXYCERTINFO. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO to get the policy of</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the PROXYPOLICY of the PROXYCERTINFO</dl>
<h3>int PROXYCERTINFO_set_path_length (<code>PROXYCERTINFO</code> * cert_info, long path_length)</h3>
<p>Sets the path length of the PROXYCERTINFO. The path length specifices the maximum depth of the path of the Proxy Certificates that can be signed by an End Entity Certificate (EEC) or Proxy Certificate. </p>
<p> Since this is an optional field in its ASN1 coded representation, it can be set to NULL through this function &#8211; which means that it won&#8217;t be included in the encoding. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO to set the path length of<br />
 <i>path_length</i> the path length to set it to if -1 is passed in, the path length gets unset, which configures the PROXYCERTINFO to not include the path length in the DER encoding</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, 0 on error</dl>
<h3>long PROXYCERTINFO_get_path_length (<code>PROXYCERTINFO</code> * cert_info)</h3>
<p>Gets the path length of the PROXYCERTINFO. <code>See also:</code></p>
<dl>
<dd><code>PROXYCERTINFO_set_path_length</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO to get the path length from</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the path length of the PROXYCERTINFO, or -1 if not set</dl>
<h3>int i2d_PROXYCERTINFO (<code>PROXYCERTINFO</code> * cert_info, unsigned char ** pp)</h3>
<p>Converts the PROXYCERTINFO structure from internal format to a DER encoded ASN.1 string. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the PROXYCERTINFO structure to convert<br />
 <i>pp</i> the resulting DER encoded string</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the length of the DER encoded string</dl>
<h3><code>PROXYCERTINFO</code>* d2i_PROXYCERTINFO (<code>PROXYCERTINFO</code> ** cert_info, unsigned char ** pp, long length)</h3>
<p>Convert from a DER encoded ASN.1 string of a PROXYCERTINFO to its internal structure. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the resulting PROXYCERTINFO in internal form<br />
 <i>pp</i> the DER encoded ASN.1 string containing the PROXYCERTINFO<br />
 <i>length</i> the length of the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the resulting PROXYCERTINFO in internal form</dl>
<h3>int i2d_PROXYCERTINFO_OLD (<code>PROXYCERTINFO</code> * cert_info, unsigned char ** pp)</h3>
<p>Converts the old PROXYCERTINFO structure from internal format to a DER encoded ASN.1 string. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the old PROXYCERTINFO structure to convert<br />
 <i>pp</i> the resulting DER encoded string</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the length of the DER encoded string</dl>
<h3><code>PROXYCERTINFO</code>* d2i_PROXYCERTINFO_OLD (<code>PROXYCERTINFO</code> ** cert_info, unsigned char ** pp, long length)</h3>
<p>Convert from a DER encoded ASN.1 string of a old PROXYCERTINFO to its internal structure. <code>Parameters:</code></p>
<dl>
<dd><i>cert_info</i> the resulting old PROXYCERTINFO in internal form<br />
 <i>pp</i> the DER encoded ASN.1 string containing the old PROXYCERTINFO<br />
 <i>length</i> the length of the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the resulting old PROXYCERTINFO in internal form</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus gsi proxy ssl from the source code.</p>
