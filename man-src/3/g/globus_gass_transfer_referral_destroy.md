---
title: "globus_gass_transfer_referral_destroy(3)"
name: "globus_gass_transfer_referral_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_referral_destroy/"
description: "Referrals –"
---

<h2 class="name">NAME</h2>
<p> Referrals &#8211; </p>
<p> GASS Referrals.</p>
<h3>Functions</h3>
<p> globus_size_t <code>globus_gass_transfer_referral_get_count</code> (globus_gass_transfer_referral_t *referral) </p>
<p> char * <code>globus_gass_transfer_referral_get_url</code> (globus_gass_transfer_referral_t *referral, globus_size_t index) </p>
<p> int <code>globus_gass_transfer_referral_destroy</code> (globus_gass_transfer_referral_t *referral) </p>
<h2>Detailed Description</h2>
<p> GASS Referrals. </p>
<p> The GASS Transfer API supports referring URL requests to alternate URLs via referrals. Referrals are essentially pointers to another URL or URLs which contain the same file as the original location which a client has requested of a server. Referrals may span multiple protocol schemes, though not all protocols may be able to generate referrals. For example, an HTTP server may refer a client to another HTTP server, an HTTPS server. </p>
<p> Upon receiving a referred response from a server, a client should query the request handle to determine from where the file can be retrieved.</p>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_referral_destroy (globus_gass_transfer_referral_t *referral)</h3>
<p> Free all memory used by a referral. </p>
<p> This function frees all memory used by this referral. After calling this function, the strings returned by calling <code>globus_gass_transfer_referral_get_url()</code> must not be accessed. Any further attempts to extract informatoin from this referral will fail. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>referral</i> The referral to destroy.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The referral was successfully destroyed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The referral parameter was GLOBUS_NULL. It could not be destroyed.</dl>
<h3>globus_size_t globus_gass_transfer_referral_get_count (globus_gass_transfer_referral_t *referral)</h3>
<p> Get the number of URLs in this referral. </p>
<p> This function examines the referral to determine if the number of URLs which are contained in it. Each of these URLs should either point to another referral, or to a URL containing the equivalent file as the original URL request which caused this referral. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>referral</i> The referral structure to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the number of URL entries in the referral, or 0, if there are none.</dl>
<h3>char* globus_gass_transfer_referral_get_url (globus_gass_transfer_referral_t *referral, globus_size_tindex)</h3>
<p> Get a URL string from a referral. </p>
<p> This function examines the referral to retrieve a URL string from it. A valid referal will contain one or more strings. They are indexed from 0 to the value returned by <code>globus_gass_transfer_referral_get_count()</code> &#8211; 1. </p>
<p> The string returned by this function must not be freed by the caller. It will remain valid until the referral structure is destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>referral</i> The referral structure to query.<br />
 <i>index</i> The URL to extract from the referral.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns a string pointer containing the URL, or NULL if the index or referral were invalid.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
