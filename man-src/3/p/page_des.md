---
title: "page_des(3)"
name: "page_des"
section: "3"
letter: "p"
url: "/docs/linux/man/3-page_des/"
description: "page_des – DES – Data Encryption Standard crypto interface See the library functions here: DES crypto functions"
---

<p>page_des &#8211; DES &#8211; Data Encryption Standard crypto interface See the library functions here: <code>DES crypto functions</code> </p>
<p> DES was created by IBM, modififed by NSA and then adopted by NBS (now NIST) and published ad FIPS PUB 46 (updated by FIPS 46-1). </p>
<p> Since the 19th May 2005 DES was withdrawn by NIST and should no longer be used. See <code>EVP &#8211; generic crypto interface</code> for replacement encryption algorithms and interfaces. </p>
<p> Read more the iteresting history of DES on Wikipedia </p>
<p><a rel="nofollow" href="http://www.wikipedia.org/wiki/Data_Encryption_Standard">http://www.wikipedia.org/wiki/Data_Encryption_Standard</a> .</p>
<h2>DES key generation</h2>
<p>To generate a DES key safely you have to use the code-snippet below. This is because the <code>DES_random_key()</code> can fail with an abort() in case of and failure to start the random generator. </p>
<p> There is a replacement function <code>DES_new_random_key()</code>, however that function does not exists in OpenSSL. </p>
<pre>* DES_cblock key;
* do {
* if (RAND_rand(&amp;key, sizeof(key)) != 1)
* goto failure;
* DES_set_odd_parity(key);
* } while (DES_is_weak_key(&amp;key));
* </pre>
<h2>DES implementation history</h2>
<p>There was no complete BSD licensed, fast, GPL compatible implementation of DES, so Love wrote the part that was missing, fast key schedule setup and adapted the interface to the orignal libdes. </p>
<p> The document that got me started for real was &#8216;Efficient<br />
&nbsp;<wbr>&nbsp;<wbr>Implementation of the Data Encryption Standard&#8217;&nbsp;<wbr>by Dag Arne Osvik. I never got to the PC1 transformation was working, instead I used table-lookup was used for all key schedule setup. The document was very useful since it de-mystified other implementations for me. </p>
<p> The core DES function (SBOX + P transformation) is from Richard Outerbridge public domain DES implementation. My sanity is saved thanks to his work. Thank you Richard.</p>
