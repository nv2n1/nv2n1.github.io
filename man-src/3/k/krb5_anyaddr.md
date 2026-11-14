---
title: "krb5_anyaddr(3)"
name: "krb5_anyaddr"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_anyaddr/"
description: "Heimdal Kerberos 5 address functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 address functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_sockaddr2address</code> (krb5_context context, const struct sockaddr *sa, krb5_address *addr)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_sockaddr2port</code> (krb5_context context, const struct sockaddr *sa, int16_t *port)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_addr2sockaddr</code> (krb5_context context, const krb5_address *addr, struct sockaddr *sa, krb5_socklen_t *sa_size, int port)&quot; </p>
<p> KRB5_LIB_FUNCTION size_t<br />
 KRB5_LIB_CALL <code>krb5_max_sockaddr_size</code> (void)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_sockaddr_uninteresting</code> (const struct sockaddr *sa)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_h_addr2sockaddr</code> (krb5_context context, int af, const char *addr, struct sockaddr *sa, krb5_socklen_t *sa_size, int port)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_h_addr2addr</code> (krb5_context context, int af, const char *haddr, krb5_address *addr)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_anyaddr</code> (krb5_context context, int af, struct sockaddr *sa, krb5_socklen_t *sa_size, int port)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_print_address</code> (const krb5_address *addr, char *str, size_t len, size_t *ret_len)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_parse_address</code> (krb5_context context, const char *string, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_address_order</code> (krb5_context context, const krb5_address *addr1, const krb5_address *addr2) </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_address_compare</code> (krb5_context context, const krb5_address *addr1, const krb5_address *addr2)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_address_search</code> (krb5_context context, const krb5_address *addr, const krb5_addresses *addrlist)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_address</code> (krb5_context context, krb5_address *address)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_addresses</code> (krb5_context context, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_address</code> (krb5_context context, const krb5_address *inaddr, krb5_address *outaddr)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_addresses</code> (krb5_context context, const krb5_addresses *inaddr, krb5_addresses *outaddr)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_append_addresses</code> (krb5_context context, krb5_addresses *dest, const krb5_addresses *source)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_make_addrport</code> (krb5_context context, krb5_address **res, const krb5_address *addr, int16_t port)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_address_prefixlen_boundary</code> (krb5_context context, const krb5_address *inaddr, unsigned long prefixlen, krb5_address *low, krb5_address *high)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_addr2sockaddr (krb5_contextcontext, const krb5_address *addr, struct sockaddr *sa, krb5_socklen_t *sa_size, intport)</h3>
<p> krb5_addr2sockaddr sets the &#8216;struct sockaddr sockaddr&#8217; from addr and port. The argument sa_size should initially contain the size of the sa and after the call, it will contain the actual length of the address. In case of the sa is too small to fit the whole address, the up to *sa_size will be stored, and then *sa_size will be set to the required length. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>addr</i> the address to copy the from<br />
 <i>sa</i> the struct sockaddr that will be filled in<br />
 <i>sa_size</i> pointer to length of sa, and after the call, it will contain the actual length of the address.<br />
 <i>port</i> set port in sa.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0. Will return KRB5_PROG_ATYPE_NOSUPP in case address type is not supported.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_address_compare (krb5_contextcontext, const krb5_address *addr1, const krb5_address *addr2)</h3>
<p> krb5_address_compare compares the addresses addr1 and addr2. Returns TRUE if the two addresses are the same. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>addr1</i> address to compare<br />
 <i>addr2</i> address to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an TRUE is the address are the same FALSE if not</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_address_order (krb5_contextcontext, const krb5_address *addr1, const krb5_address *addr2)</h3>
<p> krb5_address_order compares the addresses addr1 and addr2 so that it can be used for sorting addresses. If the addresses are the same address krb5_address_order will return 0. Behavies like <a href="/docs/linux/man/2-memcmp/">memcmp</a>(2). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>addr1</i> krb5_address to compare<br />
 <i>addr2</i> krb5_address to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> &lt; 0 if address addr1 in &#8216;less&#8217; then addr2. 0 if addr1 and addr2 is the same address, &gt; 0 if addr2 is &#8216;less&#8217; then addr1.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_address_prefixlen_boundary (krb5_contextcontext, const krb5_address *inaddr, unsigned longprefixlen, krb5_address *low, krb5_address *high)</h3>
<p> Calculate the boundary addresses of `inaddr&#8217;/`prefixlen&#8217; and store them in `low&#8217; and `high&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>inaddr</i> address in prefixlen that the bondery searched<br />
 <i>prefixlen</i> width of boundery<br />
 <i>low</i> lowest address<br />
 <i>high</i> highest address</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_address_search (krb5_contextcontext, const krb5_address *addr, const krb5_addresses *addrlist)</h3>
<p> krb5_address_search checks if the address addr is a member of the address set list addrlist . </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>addr</i> address to search for.<br />
 <i>addrlist</i> list of addresses to look in for addr.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_anyaddr (krb5_contextcontext, intaf, struct sockaddr *sa, krb5_socklen_t *sa_size, intport)</h3>
<p> krb5_anyaddr fills in a &#8216;struct sockaddr sa&#8217; that can be used to <a href="/docs/linux/man/2-bind/">bind</a>(2) to. The argument sa_size should initially contain the size of the sa, and after the call, it will contain the actual length of the address. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>af</i> address family<br />
 <i>sa</i> sockaddr<br />
 <i>sa_size</i> lenght of sa.<br />
 <i>port</i> for to fill into sa.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_append_addresses (krb5_contextcontext, krb5_addresses *dest, const krb5_addresses *source)</h3>
<p> krb5_append_addresses adds the set of addresses in source to dest. While copying the addresses, duplicates are also sorted out. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>dest</i> destination of copy operation<br />
 <i>source</i> adresses that are going to be added to dest</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_address (krb5_contextcontext, const krb5_address *inaddr, krb5_address *outaddr)</h3>
<p> krb5_copy_address copies the content of address inaddr to outaddr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>inaddr</i> pointer to source address<br />
 <i>outaddr</i> pointer to destination address</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_addresses (krb5_contextcontext, const krb5_addresses *inaddr, krb5_addresses *outaddr)</h3>
<p> krb5_copy_addresses copies the content of addresses inaddr to outaddr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>inaddr</i> pointer to source addresses<br />
 <i>outaddr</i> pointer to destination addresses</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_address (krb5_contextcontext, krb5_address *address)</h3>
<p> krb5_free_address frees the data stored in the address that is alloced with any of the krb5_address functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>address</i> addresss to be freed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_addresses (krb5_contextcontext, krb5_addresses *addresses)</h3>
<p> krb5_free_addresses frees the data stored in the address that is alloced with any of the krb5_address functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>addresses</i> addressses to be freed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_h_addr2addr (krb5_contextcontext, intaf, const char *haddr, krb5_address *addr)</h3>
<p> krb5_h_addr2addr works like krb5_h_addr2sockaddr with the exception that it operates on a krb5_address instead of a struct sockaddr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>af</i> address family<br />
 <i>haddr</i> host address from struct hostent.<br />
 <i>addr</i> returned krb5_address.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_h_addr2sockaddr (krb5_contextcontext, intaf, const char *addr, struct sockaddr *sa, krb5_socklen_t *sa_size, intport)</h3>
<p> krb5_h_addr2sockaddr initializes a &#8216;struct sockaddr sa&#8217; from af and the &#8216;struct hostent&#8217; (see <a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a>(3) ) h_addr_list component. The argument sa_size should initially contain the size of the sa, and after the call, it will contain the actual length of the address. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>af</i> addresses<br />
 <i>addr</i> address<br />
 <i>sa</i> returned struct sockaddr<br />
 <i>sa_size</i> size of sa<br />
 <i>port</i> port to set in sa.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_make_addrport (krb5_contextcontext, krb5_address **res, const krb5_address *addr, int16_tport)</h3>
<p> Create an address of type KRB5_ADDRESS_ADDRPORT from (addr, port) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>res</i> built address from addr/port<br />
 <i>addr</i> address to use<br />
 <i>port</i> port to use</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION size_t KRB5_LIB_CALL krb5_max_sockaddr_size (void)</h3>
<p> krb5_max_sockaddr_size returns the max size of the .Li struct sockaddr that the Kerberos library will return. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an size_t of the maximum struct sockaddr.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_parse_address (krb5_contextcontext, const char *string, krb5_addresses *addresses)</h3>
<p> krb5_parse_address returns the resolved hostname in string to the krb5_addresses addresses . </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>string</i><br />
 <i>addresses</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_print_address (const krb5_address *addr, char *str, size_tlen, size_t *ret_len)</h3>
<p> krb5_print_address prints the address in addr to the string string that have the length len. If ret_len is not NULL, it will be filled with the length of the string if size were unlimited (not including the final NUL) . </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>addr</i> address to be printed<br />
 <i>str</i> pointer string to print the address into<br />
 <i>len</i> length that will fit into area pointed to by &#8216;str&#8217;.<br />
 <i>ret_len</i> return length the str.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_sockaddr2address (krb5_contextcontext, const struct sockaddr *sa, krb5_address *addr)</h3>
<p> krb5_sockaddr2address stores a address a &#8216;struct sockaddr&#8217; sa in the krb5_address addr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>sa</i> a struct sockaddr to extract the address from<br />
 <i>addr</i> an Kerberos 5 address to store the address in.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_sockaddr2port (krb5_contextcontext, const struct sockaddr *sa, int16_t *port)</h3>
<p> krb5_sockaddr2port extracts a port (if possible) from a &quot;struct sockaddr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>sa</i> a struct sockaddr to extract the port from<br />
 <i>port</i> a pointer to an int16_t store the port in.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0. Will return KRB5_PROG_ATYPE_NOSUPP in case address type is not supported.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_sockaddr_uninteresting (const struct sockaddr *sa)</h3>
<p> krb5_sockaddr_uninteresting returns TRUE for all .Fa sa that the kerberos library thinks are uninteresting. One example are link local addresses. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sa</i> pointer to struct sockaddr that might be interesting.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return a non zero for uninteresting addresses.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
