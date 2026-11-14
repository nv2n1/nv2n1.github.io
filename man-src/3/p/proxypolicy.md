---
title: "proxypolicy(3)"
name: "proxypolicy"
section: "3"
letter: "p"
url: "/docs/linux/man/3-proxypolicy/"
description: "ProxyPolicy –"
---

<p>ProxyPolicy &#8211;</p>
<h3>Data Structures</h3>
<pre><code>struct PROXYPOLICY_st



Get a method for ASN1 conversion





ASN1_METHOD * PROXYPOLICY_asn1_meth ()



New





PROXYPOLICY * PROXYPOLICY_new ()



Free





void PROXYPOLICY_free (PROXYPOLICY *policy)



Duplicate





PROXYPOLICY * PROXYPOLICY_dup (PROXYPOLICY *policy)



Compare





int PROXYPOLICY_cmp (const PROXYPOLICY *a, const PROXYPOLICY *b)



Print to a BIO stream





int PROXYPOLICY_print (BIO *bp, PROXYPOLICY *policy)



Print to a File Stream





int PROXYPOLICY_print_fp (FILE *fp, PROXYPOLICY *policy)



Set the Policy Language Field





int PROXYPOLICY_set_policy_language (PROXYPOLICY *policy, ASN1_OBJECT *policy_language)



Get the Policy Language Field





ASN1_OBJECT * PROXYPOLICY_get_policy_language (PROXYPOLICY *policy)



Set the Policy Field





int PROXYPOLICY_set_policy (PROXYPOLICY *proxypolicy, unsigned char *policy, int length)



Get the Policy Field





unsigned char * PROXYPOLICY_get_policy (PROXYPOLICY *policy, int *length)



Convert from Internal to DER encoded form





int i2d_PROXYPOLICY (PROXYPOLICY *a, unsigned char **pp)



Convert from DER encoded form to Internal





PROXYPOLICY * d2i_PROXYPOLICY (PROXYPOLICY **a, unsigned char **pp, long length)</code></pre>
<h2>Detailed Description</h2>
<p><code>Author:</code></p>
<dl>
<dd>Sam Meder </p>
<p> Sam Lang</dl>
<p> The proxypolicy set of data structures and functions provides an interface to generating a PROXYPOLICY structure which is maintained as a field in the PROXYCERTINFO structure, and ultimately gets written to a DER encoded string. </p>
<p> <code>See also:</code></p>
<dl>
<dd>Further Information about proxy policies is available in the X.509 Proxy Certificate Profile document.</dl>
<h2>Function Documentation</h2>
<h3>ASN1_METHOD* PROXYPOLICY_asn1_meth ()</h3>
<p>Creates an ASN1_METHOD structure, which contains pointers to routines that convert any PROXYPOLICY structure to its associated ASN1 DER encoded form and vice-versa. <code>Returns:</code></p>
<dl>
<dd>the ASN1_METHOD object</dl>
<h3><code>PROXYPOLICY</code>* PROXYPOLICY_new ()</h3>
<p>Allocates and initializes a new PROXYPOLICY structure. <code>Returns:</code></p>
<dl>
<dd>pointer to the new PROXYPOLICY</dl>
<h3>void PROXYPOLICY_free (<code>PROXYPOLICY</code> * policy)</h3>
<p>Frees a PROXYPOLICY. <code>Parameters:</code></p>
<dl>
<dd><i>policy</i> the proxy policy to free</dl>
<h3><code>PROXYPOLICY</code>* PROXYPOLICY_dup (<code>PROXYPOLICY</code> * policy)</h3>
<p>Makes a copy of the proxypolicy &#8211; this function allocates space for a new PROXYPOLICY, so the returned PROXYPOLICY must be freed when its no longer needed. <code>Parameters:</code></p>
<dl>
<dd><i>policy</i> the proxy policy to copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the new PROXYPOLICY</dl>
<h3>int PROXYPOLICY_cmp (const <code>PROXYPOLICY</code> * a, const <code>PROXYPOLICY</code> * b)</h3>
<p>Compares two PROXYPOLICY structs for equality This function first compares the policy language numeric id&#8217;s, if they&#8217;re equal, it then compares the two policies. <code>Returns:</code></p>
<dl>
<dd>0 if equal, nonzero if not</dl>
<h3>int PROXYPOLICY_print (BIO * bp, <code>PROXYPOLICY</code> * policy)</h3>
<p>Prints the PROXYPOLICY struct using the BIO stream. <code>Parameters:</code></p>
<dl>
<dd><i>bp</i> the BIO stream to print to<br />
 <i>policy</i> the PROXYPOLICY to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, 0 on error</dl>
<h3>int PROXYPOLICY_print_fp (FILE * fp, <code>PROXYPOLICY</code> * policy)</h3>
<p>Prints the PROXYPOLICY to the file stream FILE*. <code>Parameters:</code></p>
<dl>
<dd><i>fp</i> the FILE* stream to print to<br />
 <i>policy</i> the PROXYPOLICY to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>number of bytes printed, -2 or -1 on error</dl>
<h3>int PROXYPOLICY_set_policy_language (<code>PROXYPOLICY</code> * policy, ASN1_OBJECT * policy_language)</h3>
<p>Sets the policy language of the PROXYPOLICY. <code>Parameters:</code></p>
<dl>
<dd><i>policy</i> the PROXYPOLICY to set the policy language of<br />
 <i>policy_language</i> the policy language to set it to</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, 0 on error</dl>
<h3>ASN1_OBJECT* PROXYPOLICY_get_policy_language (<code>PROXYPOLICY</code> * policy)</h3>
<p>Gets the policy language of the PROXYPOLICY. <code>Parameters:</code></p>
<dl>
<dd><i>policy</i> the proxy policy to get the policy language of</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the policy language as an ASN1_OBJECT</dl>
<h3>int PROXYPOLICY_set_policy (<code>PROXYPOLICY</code> * proxypolicy, unsigned char * policy, int length)</h3>
<p>Sets the policy of the PROXYPOLICY. <code>Parameters:</code></p>
<dl>
<dd><i>proxypolicy</i> the proxy policy to set the policy of<br />
 <i>policy</i> the policy to set it to<br />
 <i>length</i> the length of the policy</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, 0 on error</dl>
<h3>unsigned char* PROXYPOLICY_get_policy (<code>PROXYPOLICY</code> * policy, int * length)</h3>
<p>Gets the policy of a PROXYPOLICY. <code>Parameters:</code></p>
<dl>
<dd><i>policy</i> the PROXYPOLICY to get the policy of<br />
 <i>length</i> the length of the returned policy &#8211; this value gets set by this function</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the policy</dl>
<h3>int i2d_PROXYPOLICY (<code>PROXYPOLICY</code> * a, unsigned char ** pp)</h3>
<p>Converts a PROXYPOLICY from its internal structure to a DER encoded form. <code>Parameters:</code></p>
<dl>
<dd><i>a</i> the PROXYPOLICY to convert<br />
 <i>pp</i> the buffer to put the DER encoding in</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the length of the DER encoding in bytes</dl>
<h3><code>PROXYPOLICY</code>* d2i_PROXYPOLICY (<code>PROXYPOLICY</code> ** a, unsigned char ** pp, long length)</h3>
<p>Converts the PROXYPOLICY from its DER encoded form to an internal PROXYPOLICY structure. <code>Parameters:</code></p>
<dl>
<dd><i>a</i> the PROXYPOLICY struct to set<br />
 <i>pp</i> the DER encoding to get the PROXYPOLICY from<br />
 <i>length</i> the length of the DER encoding</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the resulting PROXYPOLICY in its internal structure form &#8211; this variable has been allocated using _new routines, so it needs to be freed once its no longer used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus gsi proxy ssl from the source code.</p>
